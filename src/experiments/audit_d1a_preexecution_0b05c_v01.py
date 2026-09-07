"""Forensic, non-executing audit for the D1a corrective gate 0B-05C."""

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
EXPECTED_NEGATIVE_SOURCE = "historical training codes + frozen normative corpus only"
CONFIG_PATH = "src/configs/text2trade_mnrl_v0.2.json"
TRAINING_RUNNER_PATH = "src/experiments/train_text2trade_mnrl_v02.py"
SELECTOR_PATH = "src/retrieval/text2trade_mnrl_v02.py"
INDEX_BUILDER_PATH = "src/experiments/build_text2trade_mnrl_index_v02.py"
EVALUATOR_PATH = "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py"
CORRECTIVE_RUNNER_PATH = "src/experiments/run_d1a_corrective_0b05c_v01.py"
REPRODUCIBILITY_MANIFEST_PATH = "docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json"
TRAINING_METADATA_PATH = "outputs/training/text2trade_mnrl_v0.2/training_metadata.json"
TOP200_PATH = "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl"
POOL_ARTIFACT = "d1a_0b05c_historical_training_code_pool_v0.1.json"
SPEC_ARTIFACT = "d1a_0b05c_corrective_execution_spec_v0.1.json"
AUDIT_ARTIFACT = "d1a_0b05c_preexecution_audit_v0.1.json"
OCCURRENCES_ARTIFACT = "d1a_0b05c_top200_affected_occurrences_v0.1.csv"
BILINGUAL_ARTIFACT = "d1a_0b05c_bilingual_gate_record_v0.1.md"
MANIFEST_ARTIFACT = "d1a_0b05c_artifact_manifest_v0.1.json"

CANONICAL_MASTER_PLAN = {
    "source_id": "SRC-03",
    "repository": "elVladdi/gci-nandina-rag",
    "branch": "docs/plan-maestro-temporal-2026-08-31",
    "path": "docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md",
    "local_and_github_text_must_match": True,
    "governance": "D-011",
    "canonical_markdown_blob_sha": "b5eaf686c6b0ae7e2dec4639d047d80abe912923",
    "legacy_xlsx_status": "SECONDARY_HISTORICAL_TRACKER_NOT_CANONICAL_MASTER_PLAN",
}


class ContractViolation(ValueError):
    """Frozen evidence does not support the requested gate state."""


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
        return [{str(k): "" if v is None else str(v).strip() for k, v in row.items() if k is not None} for row in reader]


def normalize_nandina(value: object) -> str:
    return re.sub(r"\D", "", "" if value is None else str(value).strip())


def git_command(root: Path, args: Sequence[str], *, text: bool = False) -> subprocess.CompletedProcess[Any]:
    return subprocess.run(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=text,
    )


def git_bytes(root: Path, revision: str, relative_path: str) -> bytes:
    result = git_command(root, ["show", f"{revision}:{relative_path}"])
    require(result.returncode == 0, f"Cannot read Git evidence {revision}:{relative_path}: {result.stderr.decode('utf-8', errors='replace')}")
    return result.stdout


def git_blob_sha(root: Path, revision: str, relative_path: str) -> str:
    result = git_command(root, ["rev-parse", f"{revision}:{relative_path}"], text=True)
    require(result.returncode == 0, f"Cannot resolve Git blob {revision}:{relative_path}: {result.stderr.strip()}")
    return result.stdout.strip()


def git_identity(root: Path, relative_path: str) -> dict[str, str]:
    content = git_bytes(root, INPUT_MAIN, relative_path)
    return {
        "path": relative_path,
        "revision": INPUT_MAIN,
        "git_blob_sha": git_blob_sha(root, INPUT_MAIN, relative_path),
        "sha256": sha256_bytes(content),
    }


def worktree_identity(root: Path, relative_path: str) -> dict[str, str]:
    path = project_path(root, relative_path)
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), "hash-object", relative_path],
        check=False,
        capture_output=True,
        text=True,
    )
    require(result.returncode == 0, f"Cannot hash working-tree code: {relative_path}")
    return {
        "path": relative_path,
        "revision": "MICROCLOSE_WORKTREE_CONTENT",
        "git_blob_sha": result.stdout.strip(),
        "sha256": sha256_file(path),
    }


def project_path(root: Path, relative_path: str) -> Path:
    path = (root / relative_path).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes project root: {relative_path}")
    return path


def choose_hard_negative(case_id: str, positive_code: str, training_codes: Sequence[str]) -> tuple[str, str]:
    same_hs4 = [code for code in training_codes if code != positive_code and code[:4] == positive_code[:4]]
    same_chapter = [code for code in training_codes if code != positive_code and code[:2] == positive_code[:2]]
    other = [code for code in training_codes if code != positive_code]
    for level, pool in (("same_hs4_different_code", same_hs4), ("same_chapter_different_code", same_chapter), ("other_historical_code", other)):
        if pool:
            return pool[int(hashlib.sha256(case_id.encode("utf-8")).hexdigest(), 16) % len(pool)], level
    raise ContractViolation(f"No negative available for {case_id} / {positive_code}")


def build_training_pool(root: Path, config: Mapping[str, Any]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    frozen = config["frozen_inputs"]
    label = str(config["columns"]["label"])
    path = project_path(root, str(frozen["historical_csv"]))
    rows = read_csv(path)
    require(sha256_file(path) == frozen["historical_sha256"], "Historical training input hash differs from frozen D1a config")
    counts = Counter(normalize_nandina(row.get(label, "")) for row in rows)
    counts.pop("", None)
    codes = sorted(counts)
    return rows, {
        "evidence_type": "DIRECT_FROZEN_H100_POOL",
        "source": {"path": str(frozen["historical_csv"]), "sha256": str(frozen["historical_sha256"]), "label_column": label, "row_count": len(rows)},
        "historical_training_code_count": len(codes),
        "historical_training_codes": codes,
        "affected_code_membership": {code: code in counts for code in AFFECTED_CODES},
        "affected_code_positive_row_counts": {code: counts.get(code, 0) for code in AFFECTED_CODES},
        "normalization": "digits-only representation normalization for NANDINA-8 equality",
    }


def reconstruct_training_records(
    config: Mapping[str, Any], historical_rows: Sequence[Mapping[str, str]], training_codes: Sequence[str]
) -> tuple[list[dict[str, str]], list[list[dict[str, str]]], Counter[str]]:
    label = str(config["columns"]["label"])
    records: list[dict[str, str]] = []
    levels: Counter[str] = Counter()
    for row in historical_rows:
        case_id = str(row.get("case_id", "")).strip()
        positive_code = normalize_nandina(row.get(label, ""))
        require(case_id and positive_code, "Historical training row lacks case_id or positive NANDINA")
        negative_code, level = choose_hard_negative(case_id, positive_code, training_codes)
        records.append({"case_id": case_id, "positive_code": positive_code, "negative_code": negative_code, "negative_level": level})
        levels[level] += 1
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sorted(records, key=lambda item: (item["positive_code"], item["case_id"])):
        buckets[row["positive_code"]].append(row)
    codes, batches, cursor = sorted(buckets), [], 0
    while any(buckets.values()):
        batch: list[dict[str, str]] = []
        for offset in range(len(codes)):
            code = codes[(cursor + offset) % len(codes)]
            if buckets[code]:
                batch.append(buckets[code].pop(0))
            if len(batch) == int(config["training"]["batch_size"]):
                break
        require(batch, "Frozen batch reconstruction produced an empty batch")
        batches.append(batch)
        cursor = (cursor + len(batch)) % len(codes)
    require(all(len({row["positive_code"] for row in batch}) == len(batch) for batch in batches), "Reconstructed MNRL batch repeats a positive code")
    return records, batches, levels


def validate_training_evidence(
    root: Path, config: Mapping[str, Any], pool: Mapping[str, Any], records: Sequence[Mapping[str, str]],
    batches: Sequence[Sequence[Mapping[str, str]]], levels: Mapping[str, int],
) -> dict[str, Any]:
    reproducibility = load_json(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))
    metadata_path = project_path(root, TRAINING_METADATA_PATH)
    metadata = load_json(metadata_path)
    require(sha256_file(metadata_path) == reproducibility["small_local_outputs_not_committed"]["training_metadata"]["sha256"], "Training metadata hash differs from reproducibility manifest")
    config_sha = sha256_bytes(git_bytes(root, CONFIG_COMMIT, CONFIG_PATH))
    require(metadata["config"]["sha256"] == config_sha, "Training metadata config hash differs from frozen Git config")
    require(metadata["command"] == "python -B -m src.experiments.train_text2trade_mnrl_v02", "Training metadata command differs")
    require(metadata["training"]["seed"] == config["training"]["seed"], "Training seed differs from frozen config")
    require(metadata["pairs"]["historical_rows"] == pool["source"]["row_count"], "Training metadata historical row count differs")
    require(metadata["pairs"]["historical_unique_codes"] == pool["historical_training_code_count"], "Training metadata unique historical code count differs")
    require(metadata["pairs"]["normative_positive_rows"] == len(records), "Training metadata positive row count differs")
    require(metadata["pairs"]["negative_source"] == EXPECTED_NEGATIVE_SOURCE, "Training metadata negative source is not restricted to the historical training code pool")
    require(metadata["pairs"]["negative_level_counts"] == dict(sorted(levels.items())), "Training metadata negative-level counts differ")
    require(metadata["pairs"]["batch_count"] == len(batches), "Training metadata batch count differs")
    require(metadata["pairs"]["positive_codes_unique_within_every_batch"] is True, "Training metadata does not confirm unique positive codes")
    require(
        metadata["inputs"]["historical"]["path"] == pool["source"]["path"] and metadata["inputs"]["historical"]["sha256"] == pool["source"]["sha256"],
        "Training metadata historical input is not the frozen H100 pool source",
    )
    for key in ("historical", "eval", "corpus"):
        item = metadata["inputs"][key]
        require(sha256_file(project_path(root, item["path"])) == item["sha256"], f"Training metadata input hash differs: {key}")
    snapshots = {}
    for name, commit, path in (
        ("runner", TRAINING_RUNNER_COMMIT, TRAINING_RUNNER_PATH),
        ("selector", SELECTOR_COMMIT, SELECTOR_PATH),
        ("config", CONFIG_COMMIT, CONFIG_PATH),
    ):
        content = git_bytes(root, commit, path)
        snapshots[name] = {"path": path, "commit": commit, "blob_sha": git_blob_sha(root, commit, path), "sha256": sha256_bytes(content)}
    return {
        "TRAINING_EXPOSURE_EVIDENCE": "POOL_EXCLUSION_PROOF_SUPPORTED_BY_FROZEN_RUN_METADATA",
        "RECONSTRUCTION_STATUS": "DETERMINISTIC_RECONSTRUCTION_CONSISTENT_WITH_TRAINING_METADATA",
        "EXECUTION_REPOSITORY_HEAD": "UNKNOWN / HISTORICAL_PROVENANCE_LIMITATION",
        "limitation": "The full historical checkout was not versioned. Runner, selector, and config snapshots are corroborative only, not a cryptographic link to the execution checkout.",
        "reproducibility_manifest": {"path": REPRODUCIBILITY_MANIFEST_PATH, "sha256": sha256_file(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))},
        "training_metadata": {
            "path": TRAINING_METADATA_PATH, "sha256": sha256_file(metadata_path), "started_at_utc": metadata["started_at_utc"],
            "finished_at_utc": metadata["finished_at_utc"], "command": metadata["command"], "negative_source": metadata["pairs"]["negative_source"],
        },
        "historical_code_snapshots": {"scope": "CORROBORATIVE_ONLY_NOT_A_CRYPTOGRAPHIC_EXECUTION_CHECKOUT_LINK", **snapshots},
        "frozen_inputs": {key: {"path": metadata["inputs"][key]["path"], "sha256": metadata["inputs"][key]["sha256"]} for key in ("historical", "eval", "corpus")},
        "reconstruction": {"records": len(records), "batches": len(batches), "seed": config["training"]["seed"], "negative_level_counts": dict(sorted(levels.items()))},
    }


def training_exposure(
    pool: Mapping[str, Any], evidence: Mapping[str, Any], records: Sequence[Mapping[str, str]], batches: Sequence[Sequence[Mapping[str, str]]]
) -> dict[str, Any]:
    require(evidence["training_metadata"]["negative_source"] == EXPECTED_NEGATIVE_SOURCE, "Pool-exclusion conclusion requires the restricted negative-source declaration")
    require(not any(pool["affected_code_membership"].values()), "Affected code appears in the frozen H100 pool; stop and reclassify training exposure")
    by_code: dict[str, Any] = {}
    for code in AFFECTED_CODES:
        positives = sum(row["positive_code"] == code for row in records)
        explicit = sum(row["negative_code"] == code for row in records)
        require(positives == 0 and explicit == 0, "Corroborative reconstruction contradicts frozen H100 pool exclusion")
        by_code[code] = {
            "code": code, "positive_training_occurrences": 0, "explicit_hard_negative_occurrences": 0, "pool_membership": False,
            "positive_exposure_basis": "DIRECT_FROZEN_H100_POOL_EXCLUSION",
            "explicit_hard_negative_basis": "DIRECT_FROZEN_H100_POOL_EXCLUSION_PLUS_METADATA_NEGATIVE_SOURCE_RESTRICTION",
            "implicit_in_batch_exposure": {"status": "NOT_IDENTIFIED", "batches_with_positive_document": 0, "co_batch_negative_opportunities": 0},
            "corroborative_reconstruction": {"positive_training_occurrences": positives, "explicit_hard_negative_occurrences": explicit, "records": len(records), "batches": len(batches)},
            "effective_optimizer_exposure": "NO_EFFECTIVE_EXPOSURE_IDENTIFIED",
            "evidence_artifacts": {"historical_training_code_pool": POOL_ARTIFACT, "training_metadata": evidence["training_metadata"]["path"], "training_metadata_sha256": evidence["training_metadata"]["sha256"]},
            "execution_repository_head_required_for_conclusion": False,
        }
    return {
        "by_code": by_code, "D1A_TRAINING_EXPOSURE": "NO_EFFECTIVE_EXPOSURE_IDENTIFIED", "POSITIVE_EXPOSURE": "NONE_IDENTIFIED",
        "EXPLICIT_HARD_NEGATIVE_EXPOSURE": "NONE_IDENTIFIED", "IMPLICIT_IN_BATCH_EXPOSURE": "NOT_IDENTIFIED",
        "MODEL_POLICY": "FREEZE_ORIGINAL_D1A_WEIGHTS",
        "conclusion_dependency": "FROZEN_H100_POOL_EXCLUSION_AND_RESTRICTED_NEGATIVE_SOURCE_NOT_EXECUTION_REPOSITORY_HEAD",
    }


def scan_top200(root: Path) -> dict[str, Any]:
    manifest = load_json(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))
    path = project_path(root, TOP200_PATH)
    require(sha256_file(path) == manifest["small_local_outputs_not_committed"]["ranking_trace"]["sha256"], "Frozen D1a Top-200 trace hash differs")
    occurrences, case_ids, lines = [], set(), 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            lines += 1
            payload = json.loads(line)
            case_id, candidates = str(payload.get("case_id", "")).strip(), payload.get("candidate_codes")
            require(case_id, f"Top-200 trace line {line_number} lacks case_id")
            require(isinstance(candidates, list) and len(candidates) == 200, f"Top-200 trace line {line_number} does not contain exactly 200 candidates")
            require(case_id not in case_ids, f"Top-200 trace repeats case_id: {case_id}")
            case_ids.add(case_id)
            occurrences.extend({"affected_code": normalize_nandina(candidate), "case_id": case_id, "rank": rank} for rank, candidate in enumerate(candidates, 1) if normalize_nandina(candidate) in AFFECTED_CODES)
    require(lines == 1056 and len(case_ids) == 1056, f"Top-200 trace must contain 1056 unique cases, found lines={lines}, cases={len(case_ids)}")
    occurrences.sort(key=lambda item: (item["affected_code"], item["case_id"], item["rank"]))
    counts = {code: sum(item["affected_code"] == code for item in occurrences) for code in AFFECTED_CODES}
    ranks = [int(item["rank"]) for item in occurrences]
    return {
        "path": TOP200_PATH, "sha256": sha256_file(path), "cases_scanned": lines, "candidates_per_case": 200, "occurrences": occurrences,
        "total_occurrences_87044110": counts["87044110"], "total_occurrences_87045110": counts["87045110"],
        "cases_with_affected_code": len({item["case_id"] for item in occurrences}), "minimum_rank": min(ranks) if ranks else None,
        "maximum_rank": max(ranks) if ranks else None, "D1A_RETRIEVAL_OUTPUT_OVERLAP": "CONFIRMED" if occurrences else "NONE_IDENTIFIED",
    }


def original_affected_documents(root: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    path = project_path(root, str(config["frozen_inputs"]["normative_corpus"]))
    require(sha256_file(path) == config["frozen_inputs"]["normative_corpus_sha256"], "Original normative corpus hash differs from frozen D1a config")
    documents: dict[str, Any] = {}
    for line in path.read_bytes().splitlines():
        if line.strip():
            payload = json.loads(line)
            code = normalize_nandina(payload.get("codigo", ""))
            if code in AFFECTED_CODES:
                require(code not in documents and payload.get("doc_id") == f"NANDINA_{code}" and payload.get("version") == "Decision_885", f"Unexpected original document for {code}")
                documents[code] = {
                    "doc_id": payload["doc_id"], "original_jsonl_line_sha256": sha256_bytes(line),
                    "original_values": {key: payload.get(key) for key in ("codigo", "titulo", "texto", "texto_index", "version", "fuente", "section", "chapter")},
                }
    require(set(documents) == set(AFFECTED_CODES), "Original corpus lacks an affected D1a document")
    return documents


def corrective_execution_spec(root: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    manifest = load_json(project_path(root, REPRODUCIBILITY_MANIFEST_PATH))
    originals = original_affected_documents(root, config)
    corpus = "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.1.jsonl"
    index_root = "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.1"
    output_root = "outputs/evaluation/text2trade_mnrl_d1a_corrective_sensitivity_v0.1"
    runtime_root = "outputs/audits/d1a_corrective_0b05c_runtime_v0.1"
    runtime_config = f"{runtime_root}/text2trade_mnrl_v0.2_0b05c_runtime.json"
    for relative in (corpus, index_root, output_root, runtime_root):
        require(not project_path(root, relative).exists(), f"Prospective D1a path already exists and must remain absent: {relative}")
    patches = []
    for code in AFFECTED_CODES:
        patches.append({
            "code": code,
            "match": {"doc_id": originals[code]["doc_id"], "codigo": code, "version": "Decision_885", "original_jsonl_line_sha256": originals[code]["original_jsonl_line_sha256"]},
            "replacement": {"titulo": "Inferior a 4,537 t", "texto": "Inferior a 4,537 t. Contexto: Sección XVII / Capítulo 87.", "texto_index": "Inferior a 4,537 t.", "version": "Decision_906"},
        })
    return {
        "specification_id": "d1a_corrective_execution_spec_v0.1", "specification_status": "CLOSED_PROSPECTIVELY",
        "authorization": {"D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED", "D1A_CORRECTIVE_CORPUS_CREATED": False, "D1A_CORRECTIVE_INDEX_CREATED": False, "D1A_CORRECTIVE_METRICS_COMPUTED": False},
        "original_normative_corpus": {"path": config["frozen_inputs"]["normative_corpus"], "sha256": config["frozen_inputs"]["normative_corpus_sha256"], "document_count": 7644, "affected_documents": originals},
        "corrected_normative_corpus": {
            "prospective_path": corpus, "must_be_absent_before_authorized_execution": True,
            "definition": {
                "authoritative_normative_source": {
                    "authority": "Comision de la Comunidad Andina", "decision": "Decision 906", "official_gazette": "Gaceta Oficial 5062",
                    "official_url": "https://www.comunidadandina.org/DocOficialesFiles/Gacetas/GACETA%205062.pdf",
                    "published_on": "2022-10-25", "effective_on": "2023-01-01",
                    "annex_entries": {"87044110": {"item": 25, "text": "Inferior a 4,537 t"}, "87045110": {"item": 26, "text": "Inferior a 4,537 t"}},
                },
                "patch_scope": "EXACTLY_TWO_NANDINA8_DOCUMENTS", "patches": patches,
                "preservation_invariants": [
                    "Preserve JSONL row order and corpus cardinality of 7644 documents.",
                    "Change only the two matched documents and declared replacement fields.",
                    "Preserve all unpatched document bytes, fields, and values.",
                    "Serialize UTF-8 JSONL with LF line endings and one terminal newline.",
                ],
            },
        },
        "model_policy": {"MODEL_POLICY": "FREEZE_ORIGINAL_D1A_WEIGHTS", "weights": manifest["large_local_artifacts_not_committed"]["model_safetensors"], "must_not_retrain": True},
        "index_builder": {
            "code_identity": git_identity(root, INDEX_BUILDER_PATH), "policy": "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD",
            "embedding_normalization": config["index"]["normalize_embeddings"], "similarity": config["training"]["similarity"],
            "retrieval_semantics": config["index"]["retrieval"],
            "ranking_unit": config["index"]["ranking_unit"], "hnsw": config["index"]["hnsw"], "prospective_output_root": index_root,
            "prospective_outputs": {
                "vectors": f"{index_root}/index/vectors.npy",
                "id_map": f"{index_root}/index/id_map.json",
                "docstore": f"{index_root}/store/nandina8_docstore.jsonl",
                "retrieval_config": f"{index_root}/retrieval_config.json",
                "vector_integrity_sample": f"{index_root}/vector_integrity_sample_v0.2.csv",
                "vector_integrity_gate": f"{index_root}/vector_integrity_gate_v0.2.json",
                "index_metadata": f"{index_root}/text2trade_mnrl_nandina8_v02_run_metadata.json",
            },
        },
        "evaluation": {
            "code_identity": git_identity(root, EVALUATOR_PATH),
            "eval_input": {"path": config["frozen_inputs"]["eval_csv"], "sha256": config["frozen_inputs"]["eval_sha256"], "N": 1056},
            "query_column": config["columns"]["query"], "label_column": config["columns"]["label"],
            "query_construction": "clean(row[query_column]) using the frozen evaluator", "ranking_depth": 200,
            "metrics_to_compare": ["Top@1", "Top@3", "Top@5", "Top@10", "Top@50", "Recall@100", "Recall@200", "MRR@100", "MRR@200", "Exact@100", "Exact@200", "HS6@100", "HS6@200", "HS4@100", "HS4@200", "Chapter@100", "Chapter@200"],
            "case_level_output_required": True,
            "primary_control": manifest["small_local_outputs_not_committed"]["evaluation_metrics"],
            "primary_control_case_summary": manifest["small_local_outputs_not_committed"]["case_summary"],
            "primary_control_ranking_trace": manifest["small_local_outputs_not_committed"]["ranking_trace"],
            "prospective_output_root": output_root,
            "required_index_contract": {
                "metadata_filename": "text2trade_mnrl_nandina8_v02_run_metadata.json",
                "vector_integrity_filename": "vector_integrity_gate_v0.2.json",
            },
            "prospective_outputs": {
                "metrics": f"{output_root}/d1a_metrics.json",
                "case_summary": f"{output_root}/d1a_case_summary.csv",
                "ranking_trace_top200": f"{output_root}/d1a_ranked_codes_top200.jsonl",
                "strategy_comparison": f"{output_root}/strategy_comparison_a_b_c_d0_d1a_v0.2.csv",
                "summary": f"{output_root}/summary.md",
            },
        },
        "orchestration": {
            "runner": worktree_identity(root, CORRECTIVE_RUNNER_PATH),
            "preflight_command": "python -B -m src.experiments.run_d1a_corrective_0b05c_v01 --preflight",
            "future_authorized_execution_command": "python -B -m src.experiments.run_d1a_corrective_0b05c_v01 --execute-authorized",
            "future_roots": [corpus, index_root, output_root, runtime_root],
            "runtime_root": runtime_root,
            "runtime_config_path": runtime_config,
            "original_config": {
                "path": CONFIG_PATH,
                "sha256": sha256_bytes(git_bytes(root, CONFIG_COMMIT, CONFIG_PATH)),
            },
            "config_derivation": {
                "original_config_path": CONFIG_PATH,
                "corrected_normative_corpus_path": corpus,
                "corrected_index_root": index_root,
                "corrected_evaluation_root": output_root,
                "allowed_changes_only": [
                    "frozen_inputs.normative_corpus",
                    "frozen_inputs.normative_corpus_sha256",
                    "index.output_dir",
                    "outputs.evaluation_dir",
                ],
                "deterministic_sequence": [
                    "Validate frozen original corpus SHA and both original JSONL line SHA values.",
                    "Apply exactly two UTF-8 LF JSONL patches in memory.",
                    "Calculate and record the derived corrected corpus SHA-256.",
                    "Derive the runtime config mechanically and validate its allowed diff before any index build.",
                    "Create the corpus, runtime config, builder outputs, evaluator outputs, comparisons, and ledger only after a separately authorized command.",
                ],
            },
            "runner_outputs": {
                "aggregate_comparison": f"{output_root}/d1a_corrective_vs_original_comparison_v0.1.json",
                "case_level_comparison": f"{output_root}/d1a_corrective_case_level_comparison_v0.1.jsonl",
                "hash_ledger": f"{output_root}/d1a_corrective_output_hash_ledger_v0.1.csv",
                "execution_manifest": f"{output_root}/d1a_corrective_execution_manifest_v0.1.json",
            },
            "comparison_contract": {
                "primary_control_only": "FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT",
                "rank_convention": "0=NOT_FOUND_AT_200",
                "case_fields": [
                    "case_id", "nandina_ref", "original_rank_ref", "corrected_rank_ref",
                    "original_found_at_200", "corrected_found_at_200",
                    "original_hit_1", "corrected_hit_1", "original_hit_3", "corrected_hit_3",
                    "original_hit_5", "corrected_hit_5", "original_hit_10", "corrected_hit_10",
                    "original_hit_50", "corrected_hit_50", "original_hit_100", "corrected_hit_100",
                    "original_hit_200", "corrected_hit_200", "ranking_changed",
                    "original_rank_87044110", "corrected_rank_87044110",
                    "original_rank_87045110", "corrected_rank_87045110",
                ],
                "aggregate_metrics": ["Top@1", "Top@3", "Top@5", "Top@10", "Top@50", "Recall@100", "Recall@200", "MRR@100", "MRR@200", "Exact@100", "Exact@200", "HS6@100", "HS6@200", "HS4@100", "HS4@200", "Chapter@100", "Chapter@200"],
            },
        },
        "fail_closed_execution_rules": [
            "All prospective corpus, index, evaluation, and runtime roots must be absent before execution.",
            "Refuse partial roots, existing files, and overwrite attempts.",
            "Refuse silent resume; preserve a failed run as failed and require a new prospective authorization for a rerun.",
            "Write the output hash ledger only after every required contractual artifact is present.",
            "Do not interpret metrics until all integrity and acceptance criteria pass.",
        ],
        "acceptance_and_integrity_criteria": [
            "Original corpus, model weight, evaluation input, and primary-control hashes match this specification.",
            "The Decision 906 source and both exact annex entries are recorded.",
            "Exactly two targeted documents change; order, cardinality, and every unpatched document are preserved.",
            "Vectors, docstore, and id-map cardinalities are coherent and map all 7644 documents.",
            "Normalized embeddings use exact brute-force dot-product retrieval and unique NANDINA-8 ranking.",
            "Evaluation covers exactly N=1056 cases, emits a unique Top-200 trace and a case-level record for each case.",
            "Runner, index-builder, and evaluator code identities match this specification.",
            "Builder and evaluator fixed filenames exist under the separate corrected roots before comparison.",
            "Aggregate and case-level comparisons use frozen Decision 885 primary controls only.",
            "A complete output hash ledger is emitted without overwrite.",
        ],
    }


def bilingual_record(audit: Mapping[str, Any]) -> str:
    evidence, exposure = audit["training_evidence"], audit["training_exposure"]
    overlap, decisions, specification = audit["retrieval_output_overlap"], audit["prospective_decisions"], audit["corrective_execution_spec"]
    orchestration = specification["orchestration"]
    pool = audit["historical_training_code_pool"]
    return f"""# D1a 0B-05C Pre-execution Audit v0.1

## Spanish

Este microclose no ejecuta retrieval, indice, corpus correctivo ni metricas. La prueba primaria
de exposicion es el pool H100 congelado: {pool['historical_training_code_count']} codigos,
87044110=false y 87045110=false. El metadata real restringe los negativos a:
{evidence['training_metadata']['negative_source']}.

TRAINING_EXPOSURE_EVIDENCE={evidence['TRAINING_EXPOSURE_EVIDENCE']}
RECONSTRUCTION_STATUS={evidence['RECONSTRUCTION_STATUS']}
EXECUTION_REPOSITORY_HEAD={evidence['EXECUTION_REPOSITORY_HEAD']}
D1A_TRAINING_EXPOSURE={exposure['D1A_TRAINING_EXPOSURE']}
D1A_RETRIEVAL_OUTPUT_OVERLAP={overlap['D1A_RETRIEVAL_OUTPUT_OVERLAP']}
MODEL_POLICY={decisions['MODEL_POLICY']}
D1A_EXECUTION_SPECIFICATION={specification['specification_status']}
CORRECTIVE_PREFLIGHT_COMMAND={orchestration['preflight_command']}
D1A_METRIC_IMPACT={decisions['D1A_METRIC_IMPACT']}
D1A_NUMERICAL_EXECUTION={decisions['D1A_NUMERICAL_EXECUTION']}
0B05C_CLOSURE={decisions['0B05C_CLOSURE']}

La reconstruccion de 2950 registros, 608 batches, seed 2026 y conteos negativos es corroborativa.
Los snapshots de runner, selector y configuracion no son una vinculacion criptografica al checkout
historico: el HEAD de ejecucion permanece desconocido.

## English

This microclose does not run retrieval, an index, a corrected corpus, or metrics. The primary
exposure proof is the frozen H100 pool: {pool['historical_training_code_count']} codes,
87044110=false, and 87045110=false. Real run metadata restricts negatives to:
{evidence['training_metadata']['negative_source']}.

TRAINING_EXPOSURE_EVIDENCE={evidence['TRAINING_EXPOSURE_EVIDENCE']}
RECONSTRUCTION_STATUS={evidence['RECONSTRUCTION_STATUS']}
EXECUTION_REPOSITORY_HEAD={evidence['EXECUTION_REPOSITORY_HEAD']}
D1A_TRAINING_EXPOSURE={exposure['D1A_TRAINING_EXPOSURE']}
D1A_RETRIEVAL_OUTPUT_OVERLAP={overlap['D1A_RETRIEVAL_OUTPUT_OVERLAP']}
MODEL_POLICY={decisions['MODEL_POLICY']}
D1A_EXECUTION_SPECIFICATION={specification['specification_status']}
CORRECTIVE_PREFLIGHT_COMMAND={orchestration['preflight_command']}
D1A_METRIC_IMPACT={decisions['D1A_METRIC_IMPACT']}
D1A_NUMERICAL_EXECUTION={decisions['D1A_NUMERICAL_EXECUTION']}
0B05C_CLOSURE={decisions['0B05C_CLOSURE']}

The reconstruction of 2950 records, 608 batches, seed 2026, and negative-level counts is
corroborative. Runner, selector, and configuration snapshots are not a cryptographic link to
the historical checkout: the execution HEAD remains unknown.
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
    rows, pool = build_training_pool(root, config)
    records, batches, levels = reconstruct_training_records(config, rows, pool["historical_training_codes"])
    evidence = validate_training_evidence(root, config, pool, records, batches, levels)
    exposure, overlap = training_exposure(pool, evidence, records, batches), scan_top200(root)
    specification = corrective_execution_spec(root, config)
    decisions = {
        "MODEL_POLICY": exposure["MODEL_POLICY"], "CORRECTED_INDEX_POLICY": specification["index_builder"]["policy"],
        "PRIMARY_CONTROL": "FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT", "OPTIONAL_CONTROL_REPRODUCTION": "REPRODUCIBILITY_CHECK_ONLY",
        "D1A_EXECUTION_SPECIFICATION": specification["specification_status"], "D1A_METRIC_IMPACT": "NOT_DETERMINED",
        "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED", "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED", "0B05C_CLOSURE": "NOT_AUTHORIZED",
        "EXP11B_RETRIEVAL_GATE": "APPROVED_AND_INTEGRATED", "EXP11B_RETRIEVAL_EXECUTION": "NOT_AUTHORIZED",
        "RETRIEVAL_EXECUTED": False, "EVALUATION_METRICS_COMPUTED": False, "H150_H200_RESULTS_OBSERVED": False, "EXP12_AUTHORIZED": False,
    }
    target = output_dir or root / "outputs/audits/d1a_preexecution_0b05c_v0.1"
    require(not target.exists() or not any(target.iterdir()), f"Audit output directory is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)
    pool_path, spec_path = target / POOL_ARTIFACT, target / SPEC_ARTIFACT
    write_json(pool_path, pool)
    write_json(spec_path, specification)
    payload: dict[str, Any] = {
        "audit_id": "d1a_0b05c_preexecution_audit_v0.1", "gate": "0B-05C", "input_main": INPUT_MAIN,
        "scope": "D1a F001 canonical-plan reconciliation, F002 frozen-pool exposure proof, and F003 prospective execution specification",
        "canonical_master_plan": CANONICAL_MASTER_PLAN, "D1A_INDEX_EXPOSURE": "CONFIRMED", "training_evidence": evidence,
        "historical_training_code_pool": pool, "training_exposure": exposure, "retrieval_output_overlap": overlap,
        "corrective_execution_spec": specification, "prospective_decisions": decisions,
        "artifacts": {
            "historical_training_code_pool": {"path": pool_path.name, "sha256": sha256_file(pool_path)},
            "corrective_execution_spec": {"path": spec_path.name, "sha256": sha256_file(spec_path)},
        },
        "actions_not_executed": ["EV-03 corrective", "EV-04 corrective", "D1a corrective numerical execution", "corrected corpus generation", "corrected index rebuild", "H150/H200 retrieval", "new evaluation metrics", "EXP-12", "article modification"],
    }
    audit_path, occurrences_path, bilingual_path = target / AUDIT_ARTIFACT, target / OCCURRENCES_ARTIFACT, target / BILINGUAL_ARTIFACT
    write_json(audit_path, payload)
    write_occurrences(occurrences_path, overlap["occurrences"])
    bilingual_path.write_text(bilingual_record(payload), encoding="utf-8", newline="\n")
    manifest = {
        "audit_id": payload["audit_id"], "input_main": INPUT_MAIN,
        "artifacts": [{"path": path.name, "sha256": sha256_file(path)} for path in (pool_path, spec_path, audit_path, occurrences_path, bilingual_path)],
        "retrieval_executed": False, "evaluation_metrics_computed": False, "new_d1a_metrics_computed": False,
    }
    write_json(target / MANIFEST_ARTIFACT, manifest)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit D1a 0B-05C evidence without execution.")
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    result = audit(ROOT, args.output_dir)
    print(f"D1A_TRAINING_EXPOSURE={result['training_exposure']['D1A_TRAINING_EXPOSURE']}")
    print(f"D1A_RETRIEVAL_OUTPUT_OVERLAP={result['retrieval_output_overlap']['D1A_RETRIEVAL_OUTPUT_OVERLAP']}")
    print(f"D1A_EXECUTION_SPECIFICATION={result['prospective_decisions']['D1A_EXECUTION_SPECIFICATION']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
