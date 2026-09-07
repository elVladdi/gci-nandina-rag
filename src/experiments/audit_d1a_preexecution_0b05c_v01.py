"""Audit the unresolved D1a pre-execution questions for corrective gate 0B-05C.

This module is deliberately forensic.  It never loads a model, an index, or an
evaluator, and it never creates a corrected corpus or retrieval output.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
INPUT_MAIN = "37eaa712bd12914b97e8fc108b96dc6e68c4e460"
TRAINING_RUNNER_COMMIT = "a91269ed3b5c52d08511063465be130adf185f0a"
CONFIG_COMMIT = "c82e6232ef5f0678c3b10fbdb9c3850910aacee0"
SELECTOR_COMMIT = "3f30db4d65faac2e8d8b7ab75aad33119d3bca0b"
AFFECTED_CODES = ("87044110", "87045110")
CONFIG_PATH = "src/configs/text2trade_mnrl_v0.2.json"
TRAINING_RUNNER_PATH = "src/experiments/train_text2trade_mnrl_v02.py"
SELECTOR_PATH = "src/retrieval/text2trade_mnrl_v02.py"
REPRODUCIBILITY_MANIFEST_PATH = "docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json"
TRAINING_METADATA_PATH = "outputs/training/text2trade_mnrl_v0.2/training_metadata.json"
TOP200_PATH = "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl"


class ContractViolation(ValueError):
    """Raised when frozen D1a evidence cannot support the requested audit."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(payload, dict), f"Expected JSON object: {path}")
    return payload


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, f"CSV without header: {path}")
        return [{str(key): "" if value is None else str(value).strip() for key, value in row.items() if key is not None} for row in reader]


def normalize_nandina(value: object) -> str:
    """Normalize only representation for equality against an eight-digit code."""

    return re.sub(r"\D", "", "" if value is None else str(value).strip())


def git_bytes(root: Path, revision: str, relative_path: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{relative_path}"],
        check=False,
        capture_output=True,
    )
    require(result.returncode == 0, f"Cannot read Git evidence {revision}:{relative_path}: {result.stderr.decode('utf-8', errors='replace')}")
    return result.stdout


def git_blob_sha(root: Path, revision: str, relative_path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", f"{revision}:{relative_path}"],
        check=False,
        capture_output=True,
        text=True,
    )
    require(result.returncode == 0, f"Cannot resolve Git blob {revision}:{relative_path}: {result.stderr.strip()}")
    return result.stdout.strip()


def project_path(root: Path, relative_path: str) -> Path:
    path = (root / relative_path).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes project root: {relative_path}")
    return path


def choose_hard_negative(case_id: str, positive_code: str, training_codes: Sequence[str]) -> tuple[str, str]:
    """Reconstruct the frozen selector from the evidenced D1a runner."""

    same_hs4 = [code for code in training_codes if code != positive_code and code[:4] == positive_code[:4]]
    same_chapter = [code for code in training_codes if code != positive_code and code[:2] == positive_code[:2]]
    other = [code for code in training_codes if code != positive_code]
    for level, pool in (
        ("same_hs4_different_code", same_hs4),
        ("same_chapter_different_code", same_chapter),
        ("other_historical_code", other),
    ):
        if pool:
            index = int(hashlib.sha256(case_id.encode("utf-8")).hexdigest(), 16) % len(pool)
            return pool[index], level
    raise ContractViolation(f"No negative available for {case_id} / {positive_code}")


def rows_by_unique_positive_batches(rows: Sequence[dict[str, str]], batch_size: int) -> list[list[dict[str, str]]]:
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sorted(rows, key=lambda item: (item["positive_code"], item["case_id"])):
        buckets[row["positive_code"]].append(row)
    codes = sorted(buckets)
    batches: list[list[dict[str, str]]] = []
    cursor = 0
    while any(buckets.values()):
        batch: list[dict[str, str]] = []
        for offset in range(len(codes)):
            code = codes[(cursor + offset) % len(codes)]
            if buckets[code]:
                batch.append(buckets[code].pop(0))
            if len(batch) == batch_size:
                break
        require(batch, "Frozen batch reconstruction produced an empty batch")
        batches.append(batch)
        cursor = (cursor + len(batch)) % len(codes)
    return batches


def reconstruct_training_records(config: Mapping[str, Any], root: Path) -> tuple[list[dict[str, str]], list[list[dict[str, str]]], Counter[str]]:
    frozen = config["frozen_inputs"]
    columns = config["columns"]
    historical_path = project_path(root, str(frozen["historical_csv"]))
    historical_rows = read_csv(historical_path)
    require(sha256_file(historical_path) == frozen["historical_sha256"], "Historical training input hash differs from frozen D1a config")
    training_codes = sorted({normalize_nandina(row[columns["label"]]) for row in historical_rows if normalize_nandina(row[columns["label"]])})
    records: list[dict[str, str]] = []
    levels: Counter[str] = Counter()
    for row in historical_rows:
        case_id = row["case_id"].strip()
        positive_code = normalize_nandina(row[columns["label"]])
        require(case_id and positive_code, "Historical training row lacks case_id or positive NANDINA")
        negative_code, level = choose_hard_negative(case_id, positive_code, training_codes)
        records.append(
            {
                "case_id": case_id,
                "positive_code": positive_code,
                "negative_code": negative_code,
                "negative_level": level,
            }
        )
        levels[level] += 1
    batches = rows_by_unique_positive_batches(records, int(config["training"]["batch_size"]))
    require(all(len({row["positive_code"] for row in batch}) == len(batch) for batch in batches), "Reconstructed MNRL batch repeats a positive code")
    return records, batches, levels


def validate_training_evidence(root: Path, config: Mapping[str, Any], records: Sequence[Mapping[str, str]], batches: Sequence[Sequence[Mapping[str, str]]], levels: Mapping[str, int]) -> dict[str, Any]:
    reproducibility = load_json(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))
    metadata_path = project_path(root, TRAINING_METADATA_PATH)
    metadata = load_json(metadata_path)
    expected_metadata = reproducibility["small_local_outputs_not_committed"]["training_metadata"]
    require(sha256_file(metadata_path) == expected_metadata["sha256"], "Training metadata hash differs from reproducibility manifest")
    config_blob = git_bytes(root, CONFIG_COMMIT, CONFIG_PATH)
    config_sha = sha256_bytes(config_blob)
    require(metadata["config"]["sha256"] == config_sha, "Training metadata config hash differs from frozen Git config")
    require(metadata["command"] == "python -B -m src.experiments.train_text2trade_mnrl_v02", "Training metadata command differs")
    require(metadata["training"]["seed"] == config["training"]["seed"], "Training seed differs from frozen config")
    require(metadata["pairs"]["historical_rows"] == len(records), "Training metadata historical row count differs")
    require(metadata["pairs"]["normative_positive_rows"] == len(records), "Training metadata positive row count differs")
    require(metadata["pairs"]["negative_level_counts"] == dict(sorted(levels.items())), "Training metadata negative-level counts differ")
    require(metadata["pairs"]["batch_count"] == len(batches), "Training metadata batch count differs")
    require(metadata["pairs"]["positive_codes_unique_within_every_batch"] is True, "Training metadata does not confirm unique positive codes")
    for key in ("historical", "eval", "corpus"):
        path = project_path(root, metadata["inputs"][key]["path"])
        require(sha256_file(path) == metadata["inputs"][key]["sha256"], f"Training metadata input hash differs: {key}")
    runner_bytes = git_bytes(root, TRAINING_RUNNER_COMMIT, TRAINING_RUNNER_PATH)
    selector_bytes = git_bytes(root, SELECTOR_COMMIT, SELECTOR_PATH)
    return {
        "status": "DETERMINISTIC_RECONSTRUCTION_MATCHES_TRAINING_METADATA",
        "execution_repository_head": "UNKNOWN",
        "limitation": "The full repository HEAD at execution was not versioned; the runner, selector, config, frozen inputs, seed, pair counts, negative-level counts, batch count, and model metadata are evidenced.",
        "reproducibility_manifest": {
            "path": REPRODUCIBILITY_MANIFEST_PATH,
            "sha256": sha256_file(project_path(root, REPRODUCIBILITY_MANIFEST_PATH)),
        },
        "training_metadata": {
            "path": TRAINING_METADATA_PATH,
            "sha256": sha256_file(metadata_path),
            "started_at_utc": metadata["started_at_utc"],
            "finished_at_utc": metadata["finished_at_utc"],
            "command": metadata["command"],
        },
        "runner": {
            "path": TRAINING_RUNNER_PATH,
            "commit": TRAINING_RUNNER_COMMIT,
            "blob_sha": git_blob_sha(root, TRAINING_RUNNER_COMMIT, TRAINING_RUNNER_PATH),
            "sha256": sha256_bytes(runner_bytes),
        },
        "selector": {
            "path": SELECTOR_PATH,
            "commit": SELECTOR_COMMIT,
            "blob_sha": git_blob_sha(root, SELECTOR_COMMIT, SELECTOR_PATH),
            "sha256": sha256_bytes(selector_bytes),
        },
        "config": {
            "path": CONFIG_PATH,
            "commit": CONFIG_COMMIT,
            "blob_sha": git_blob_sha(root, CONFIG_COMMIT, CONFIG_PATH),
            "sha256": config_sha,
        },
        "frozen_inputs": {
            key: {
                "path": metadata["inputs"][key]["path"],
                "sha256": metadata["inputs"][key]["sha256"],
            }
            for key in ("historical", "eval", "corpus")
        },
        "reconstruction": {
            "records": len(records),
            "batches": len(batches),
            "seed": config["training"]["seed"],
            "negative_level_counts": dict(sorted(levels.items())),
        },
    }


def training_exposure(
    records: Sequence[Mapping[str, str]],
    batches: Sequence[Sequence[Mapping[str, str]]],
    evidence: Mapping[str, Any],
) -> dict[str, Any]:
    by_code: dict[str, dict[str, Any]] = {}
    for code in AFFECTED_CODES:
        positives = sum(row["positive_code"] == code for row in records)
        explicit_negatives = sum(row["negative_code"] == code for row in records)
        batches_with_positive = [batch for batch in batches if any(row["positive_code"] == code for row in batch)]
        co_batch_opportunities = sum(len(batch) - 1 for batch in batches_with_positive)
        implicit_status = "CONFIRMED" if co_batch_opportunities else "NOT_IDENTIFIED"
        if positives or explicit_negatives:
            effective = "CONFIRMED_AS_POSITIVE_OR_EXPLICIT_HARD_NEGATIVE"
        elif co_batch_opportunities:
            effective = "IMPLICIT_IN_BATCH_ONLY"
        else:
            effective = "NO_EFFECTIVE_EXPOSURE_IDENTIFIED"
        by_code[code] = {
            "code": code,
            "positive_training_occurrences": positives,
            "explicit_hard_negative_occurrences": explicit_negatives,
            "implicit_in_batch_exposure": {
                "status": implicit_status,
                "batches_with_positive_document": len(batches_with_positive),
                "co_batch_negative_opportunities": co_batch_opportunities,
                "interpretation": "Positive-document co-batch opportunities under MNRL; this is not reclassified as an explicit hard negative.",
            },
            "effective_optimizer_exposure": effective,
            "evidence_artifact": evidence["training_metadata"]["path"],
            "artifact_hash_or_run_metadata": {
                "training_metadata_sha256": evidence["training_metadata"]["sha256"],
                "command": evidence["training_metadata"]["command"],
                "runner_commit": evidence["runner"]["commit"],
                "runner_blob_sha": evidence["runner"]["blob_sha"],
                "selector_commit": evidence["selector"]["commit"],
                "selector_blob_sha": evidence["selector"]["blob_sha"],
                "config_commit": evidence["config"]["commit"],
                "config_blob_sha": evidence["config"]["blob_sha"],
            },
        }
    confirmed = any(item["positive_training_occurrences"] or item["explicit_hard_negative_occurrences"] for item in by_code.values())
    return {
        "by_code": by_code,
        "D1A_TRAINING_EXPOSURE": "CONFIRMED" if confirmed else "NO_EFFECTIVE_EXPOSURE_IDENTIFIED",
        "POSITIVE_EXPOSURE": "CONFIRMED" if any(item["positive_training_occurrences"] for item in by_code.values()) else "NONE_IDENTIFIED",
        "EXPLICIT_HARD_NEGATIVE_EXPOSURE": "CONFIRMED" if any(item["explicit_hard_negative_occurrences"] for item in by_code.values()) else "NONE_IDENTIFIED",
        "IMPLICIT_IN_BATCH_EXPOSURE": "CONFIRMED" if any(item["implicit_in_batch_exposure"]["status"] == "CONFIRMED" for item in by_code.values()) else "NOT_IDENTIFIED",
        "MODEL_POLICY": "CONTROLLED_RETRAINING" if confirmed else "FREEZE_ORIGINAL_D1A_WEIGHTS",
    }


def scan_top200(root: Path) -> dict[str, Any]:
    reproducibility = load_json(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))
    path = project_path(root, TOP200_PATH)
    expected = reproducibility["small_local_outputs_not_committed"]["ranking_trace"]
    require(sha256_file(path) == expected["sha256"], "Frozen D1a Top-200 trace hash differs from reproducibility manifest")
    occurrences: list[dict[str, Any]] = []
    case_ids: set[str] = set()
    lines = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            lines += 1
            payload = json.loads(line)
            case_id = str(payload.get("case_id", "")).strip()
            candidates = payload.get("candidate_codes")
            require(case_id, f"Top-200 trace line {line_number} lacks case_id")
            require(isinstance(candidates, list) and len(candidates) == 200, f"Top-200 trace line {line_number} does not contain exactly 200 candidates")
            require(case_id not in case_ids, f"Top-200 trace repeats case_id: {case_id}")
            case_ids.add(case_id)
            for rank, candidate in enumerate(candidates, start=1):
                normalized = normalize_nandina(candidate)
                if normalized in AFFECTED_CODES:
                    occurrences.append({"affected_code": normalized, "case_id": case_id, "rank": rank})
    require(lines == 1056 and len(case_ids) == 1056, f"Top-200 trace must contain 1056 unique cases, found lines={lines}, cases={len(case_ids)}")
    occurrences.sort(key=lambda item: (item["affected_code"], item["case_id"], item["rank"]))
    counts = {code: sum(item["affected_code"] == code for item in occurrences) for code in AFFECTED_CODES}
    ranks = [int(item["rank"]) for item in occurrences]
    return {
        "path": TOP200_PATH,
        "sha256": sha256_file(path),
        "cases_scanned": lines,
        "candidates_per_case": 200,
        "occurrences": occurrences,
        "total_occurrences_87044110": counts["87044110"],
        "total_occurrences_87045110": counts["87045110"],
        "cases_with_affected_code": len({item["case_id"] for item in occurrences}),
        "minimum_rank": min(ranks) if ranks else None,
        "maximum_rank": max(ranks) if ranks else None,
        "D1A_RETRIEVAL_OUTPUT_OVERLAP": "CONFIRMED" if occurrences else "NONE_IDENTIFIED",
    }


def bilingual_record(audit: Mapping[str, Any]) -> str:
    evidence = audit["training_evidence"]
    exposure = audit["training_exposure"]
    overlap = audit["retrieval_output_overlap"]
    policy = audit["prospective_decisions"]
    rows = overlap["occurrences"]
    occurrence_rows = "\n".join(f"| {item['affected_code']} | {item['case_id']} | {item['rank']} |" for item in rows) or "| None / Ninguno | - | - |"
    code_lines = []
    for code in AFFECTED_CODES:
        item = exposure["by_code"][code]
        code_lines.append(
            f"- `{code}`: positives={item['positive_training_occurrences']}; explicit hard negatives={item['explicit_hard_negative_occurrences']}; "
            f"implicit in-batch={item['implicit_in_batch_exposure']['status']} ({item['implicit_in_batch_exposure']['co_batch_negative_opportunities']} co-batch opportunities); "
            f"evidence=`{item['evidence_artifact']}` / `{item['artifact_hash_or_run_metadata']['training_metadata_sha256']}`."
        )
    codes = "\n".join(code_lines)
    sources = "\n".join(
        [
            f"- `{evidence['reproducibility_manifest']['path']}`: SHA256 `{evidence['reproducibility_manifest']['sha256']}`.",
            f"- `{evidence['training_metadata']['path']}`: SHA256 `{evidence['training_metadata']['sha256']}`; command `{evidence['training_metadata']['command']}`; "
            f"started `{evidence['training_metadata']['started_at_utc']}`; finished `{evidence['training_metadata']['finished_at_utc']}`.",
            f"- `{evidence['runner']['path']}` at `{evidence['runner']['commit']}`: Git blob `{evidence['runner']['blob_sha']}`, SHA256 `{evidence['runner']['sha256']}`.",
            f"- `{evidence['selector']['path']}` at `{evidence['selector']['commit']}`: Git blob `{evidence['selector']['blob_sha']}`, SHA256 `{evidence['selector']['sha256']}`.",
            f"- `{evidence['config']['path']}` at `{evidence['config']['commit']}`: Git blob `{evidence['config']['blob_sha']}`, SHA256 `{evidence['config']['sha256']}`.",
            *[
                f"- frozen {key} input `{item['path']}`: SHA256 `{item['sha256']}`."
                for key, item in evidence["frozen_inputs"].items()
            ],
            f"- `{overlap['path']}`: SHA256 `{overlap['sha256']}`; exhaustive scope `{overlap['cases_scanned']}` cases x `{overlap['candidates_per_case']}` candidates.",
        ]
    )
    residual_blockers = (
        "No blocker prevents this forensic audit. The complete execution repository HEAD is `UNKNOWN`; "
        "the documented runner, selector, config, frozen inputs, seed, reconstruction counts, and run metadata provide the required deterministic linkage. "
        "Numerical D1a execution remains prospectively unauthorized."
    )
    return f"""# D1a 0B-05C Pre-execution Audit v0.1 / Auditoria pre-ejecucion D1a 0B-05C v0.1

## Spanish

Este registro resuelve prospectivamente la exposicion efectiva de entrenamiento y el solapamiento exhaustivo Top-200 del D1a congelado. No carga pesos, FAISS ni evaluadores, no genera un corpus correctivo y no calcula metricas nuevas.

- Gate: `0B-05C`.
- Main experimental de entrada: `{audit['input_main']}`.
- Exposicion de indice D1a preservada: `CONFIRMED`.
- Exposicion de entrenamiento: `{exposure['D1A_TRAINING_EXPOSURE']}`.
- Positivos: `{exposure['POSITIVE_EXPOSURE']}`.
- Hard negatives explicitos: `{exposure['EXPLICIT_HARD_NEGATIVE_EXPOSURE']}`.
- Exposicion implicita in-batch: `{exposure['IMPLICIT_IN_BATCH_EXPOSURE']}`.
- Solapamiento en Top-200: `{overlap['D1A_RETRIEVAL_OUTPUT_OVERLAP']}`.
- Politica de pesos: `{exposure['MODEL_POLICY']}`.
- Politica de indice: `{policy['CORRECTED_INDEX_POLICY']}`.
- Control primario: `{policy['PRIMARY_CONTROL']}`.
- Control opcional de reproduccion: `{policy['OPTIONAL_CONTROL_REPRODUCTION']}`.
- Especificacion D1a: `{policy['D1A_EXECUTION_SPECIFICATION']}`.
- Impacto metrico: `{policy['D1A_METRIC_IMPACT']}`.
- Ejecucion numerica D1a: `{policy['D1A_NUMERICAL_EXECUTION']}`.
- Reejecucion downstream: `{policy['DOWNSTREAM_REEXECUTION']}`.
- Cierre 0B-05C: `{policy['0B05C_CLOSURE']}`.

La reconstruccion determinista coincide con el metadata real de entrenamiento: 2,950 instancias, 608 batches, seed 2026 y conteos de nivel negativo. La version D1a queda identificada por los commits del runner, selector y configuracion siguientes. El HEAD completo de ejecucion no fue versionado; la limitacion queda preservada sin inferirla como ausencia de evidencia.

### Fuentes experimentales y trazabilidad criptografica

{sources}

{codes}

Auditoria Top-200 completa: `{overlap['cases_scanned']}` casos x `{overlap['candidates_per_case']}` candidatos. Ocurrencias: `87044110={overlap['total_occurrences_87044110']}`, `87045110={overlap['total_occurrences_87045110']}`, casos afectados=`{overlap['cases_with_affected_code']}`, rango minimo=`{overlap['minimum_rank']}`, rango maximo=`{overlap['maximum_rank']}`.

| affected_code | case_id | rank |
| --- | --- | --- |
{occurrence_rows}

Acciones no ejecutadas: reentrenamiento, reconstruccion de indice, EV-03, EV-04, D1a correctivo, retrieval H150/H200, metricas nuevas, EXP-12 y cambios editoriales.

Bloqueos residuales: Ningun bloqueo impide esta auditoria forense. El HEAD completo del repositorio de ejecucion es `UNKNOWN`; el runner, selector, configuracion, inputs congelados, seed, conteos de reconstruccion y metadatos documentados proporcionan la vinculacion determinista requerida. La ejecucion numerica D1a permanece prospectivamente no autorizada.

## English

This record prospectively resolves effective training exposure and the exhaustive Top-200 overlap for frozen D1a. It does not load weights, FAISS, or evaluators, does not create a corrected corpus, and does not compute new metrics.

- Gate: `0B-05C`.
- Experimental input main: `{audit['input_main']}`.
- Preserved D1a index exposure: `CONFIRMED`.
- Training exposure: `{exposure['D1A_TRAINING_EXPOSURE']}`.
- Positive exposure: `{exposure['POSITIVE_EXPOSURE']}`.
- Explicit hard-negative exposure: `{exposure['EXPLICIT_HARD_NEGATIVE_EXPOSURE']}`.
- Implicit in-batch exposure: `{exposure['IMPLICIT_IN_BATCH_EXPOSURE']}`.
- Top-200 output overlap: `{overlap['D1A_RETRIEVAL_OUTPUT_OVERLAP']}`.
- Weight policy: `{exposure['MODEL_POLICY']}`.
- Index policy: `{policy['CORRECTED_INDEX_POLICY']}`.
- Primary control: `{policy['PRIMARY_CONTROL']}`.
- Optional control reproduction: `{policy['OPTIONAL_CONTROL_REPRODUCTION']}`.
- D1a specification: `{policy['D1A_EXECUTION_SPECIFICATION']}`.
- Metric impact: `{policy['D1A_METRIC_IMPACT']}`.
- D1a numerical execution: `{policy['D1A_NUMERICAL_EXECUTION']}`.
- Downstream re-execution: `{policy['DOWNSTREAM_REEXECUTION']}`.
- 0B-05C closure: `{policy['0B05C_CLOSURE']}`.

The deterministic reconstruction matches the real training metadata: 2,950 instances, 608 batches, seed 2026, and negative-level counts. The D1a version is identified by the following runner, selector, and configuration commits. The complete execution repository HEAD was not versioned; this limitation is preserved and is not treated as missing training evidence.

### Experimental sources and cryptographic traceability

{sources}

{codes}

Complete Top-200 audit: `{overlap['cases_scanned']}` cases x `{overlap['candidates_per_case']}` candidates. Occurrences: `87044110={overlap['total_occurrences_87044110']}`, `87045110={overlap['total_occurrences_87045110']}`, affected cases=`{overlap['cases_with_affected_code']}`, minimum rank=`{overlap['minimum_rank']}`, maximum rank=`{overlap['maximum_rank']}`.

| affected_code | case_id | rank |
| --- | --- | --- |
{occurrence_rows}

Actions not executed: retraining, index rebuild, EV-03, EV-04, corrective D1a, H150/H200 retrieval, new metrics, EXP-12, and editorial changes.

Residual blockers: {residual_blockers}
"""


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_occurrences(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("affected_code", "case_id", "rank"), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def audit(root: Path = ROOT, output_dir: Path | None = None) -> dict[str, Any]:
    config = json.loads(git_bytes(root, CONFIG_COMMIT, CONFIG_PATH).decode("utf-8"))
    require(isinstance(config, dict), "Frozen D1a config is not a JSON object")
    records, batches, levels = reconstruct_training_records(config, root)
    evidence = validate_training_evidence(root, config, records, batches, levels)
    exposure = training_exposure(records, batches, evidence)
    overlap = scan_top200(root)
    prospective_decisions = {
        "MODEL_POLICY": exposure["MODEL_POLICY"],
        "CORRECTED_INDEX_POLICY": "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD",
        "PRIMARY_CONTROL": "FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT",
        "OPTIONAL_CONTROL_REPRODUCTION": "REPRODUCIBILITY_CHECK_ONLY",
        "D1A_EXECUTION_SPECIFICATION": "CLOSED_PROSPECTIVELY",
        "D1A_METRIC_IMPACT": "NOT_DETERMINED",
        "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED",
        "0B05C_CLOSURE": "NOT_AUTHORIZED",
        "EXP11B_RETRIEVAL_GATE": "APPROVED_AND_INTEGRATED",
        "EXP11B_RETRIEVAL_EXECUTION": "NOT_AUTHORIZED",
        "RETRIEVAL_EXECUTED": False,
        "EVALUATION_METRICS_COMPUTED": False,
        "H150_H200_RESULTS_OBSERVED": False,
        "EXP12_AUTHORIZED": False,
    }
    audit_payload: dict[str, Any] = {
        "audit_id": "d1a_0b05c_preexecution_audit_v0.1",
        "gate": "0B-05C",
        "input_main": INPUT_MAIN,
        "scope": "D1a effective optimizer exposure and frozen Top-200 overlap only",
        "D1A_INDEX_EXPOSURE": "CONFIRMED",
        "training_evidence": evidence,
        "training_exposure": exposure,
        "retrieval_output_overlap": overlap,
        "prospective_decisions": prospective_decisions,
        "actions_not_executed": [
            "EV-03 corrective",
            "EV-04 corrective",
            "D1a corrective numerical execution",
            "corrected index rebuild",
            "H150/H200 retrieval",
            "new evaluation metrics",
            "EXP-12",
            "editorial modification",
        ],
    }
    target = output_dir or root / "outputs/audits/d1a_preexecution_0b05c_v0.1"
    require(not target.exists() or not any(target.iterdir()), f"Audit output directory is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)
    audit_path = target / "d1a_0b05c_preexecution_audit_v0.1.json"
    occurrence_path = target / "d1a_0b05c_top200_affected_occurrences_v0.1.csv"
    bilingual_path = target / "d1a_0b05c_bilingual_gate_record_v0.1.md"
    write_json(audit_path, audit_payload)
    write_occurrences(occurrence_path, overlap["occurrences"])
    bilingual_path.write_text(bilingual_record(audit_payload), encoding="utf-8", newline="\n")
    manifest = {
        "audit_id": audit_payload["audit_id"],
        "input_main": INPUT_MAIN,
        "artifacts": [
            {"path": audit_path.name, "sha256": sha256_file(audit_path)},
            {"path": occurrence_path.name, "sha256": sha256_file(occurrence_path)},
            {"path": bilingual_path.name, "sha256": sha256_file(bilingual_path)},
        ],
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "new_d1a_metrics_computed": False,
    }
    write_json(target / "d1a_0b05c_artifact_manifest_v0.1.json", manifest)
    return audit_payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit D1a 0B-05C pre-execution exposure and Top-200 overlap.")
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    result = audit(ROOT, args.output_dir)
    print(f"D1A_TRAINING_EXPOSURE={result['training_exposure']['D1A_TRAINING_EXPOSURE']}")
    print(f"D1A_RETRIEVAL_OUTPUT_OVERLAP={result['retrieval_output_overlap']['D1A_RETRIEVAL_OUTPUT_OVERLAP']}")
    print(f"MODEL_POLICY={result['prospective_decisions']['MODEL_POLICY']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
