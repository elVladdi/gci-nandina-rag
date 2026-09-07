"""Freeze and validate the prospective 0B-05C corrective numerical gate.

The module audits only frozen EV-03/EV-04 outputs.  It records the committed
implementation that a separately authorized future execution must use, but it
does not create a corpus, index, retrieval output, or metric in this state.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping

from .run_d1a_corrective_0b05c_v01 import (
    ContractViolation,
    canonical_frozen_text_bytes,
    git_blob_bytes,
    git_blob_sha256,
    git_head_blob_sha,
    git_path_is_tracked,
    git_worktree_semantically_clean,
    project_path,
    require,
    sha256_bytes,
    sha256_file,
    validate_code_identity,
)


ROOT = Path(__file__).resolve().parents[2]
INTEGRATED_BASE_COMMIT = "7ff504c4a5a763705f198ca41753db75e938a87d"
AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.1")
TARGET_CODES = ("87044110", "87045110")
DECISION_906_TEXT = "Inferior a 4,537 t"
EVAL_PATH = "data/processed/data_aduanas_evalset_clase87_v0.2.csv"
CONFIG_PATH = "src/configs/experiment_config.json"
D1A_SPEC_PATH = "outputs/audits/d1a_preexecution_0b05c_v0.1/d1a_0b05c_corrective_execution_spec_v0.1.json"
PREPARE_PATH = "src/experiments/prepare_0b05c_corrective_numerical_gate_v01.py"
RUNNER_PATH = "src/experiments/run_0b05c_corrective_numerical_v01.py"
EVALUATOR_PATH = "src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py"
BUILDER_PATH = "src/experiments/build_bm25_corrective_0b05c_v01.py"

# These are identities, not an invitation to execute their historical CLIs.
# The new prospective evaluator reuses their versioned helper semantics.
FROZEN_EXECUTION_DEPENDENCIES = (
    PREPARE_PATH,
    RUNNER_PATH,
    EVALUATOR_PATH,
    BUILDER_PATH,
    "src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py",
    "src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py",
    "src/experiments/build_bm25_index.py",
    "src/experiments/build_bm25_hierarchical_index.py",
    "src/bm25_index.py",
    "src/retrieval/bm25.py",
    "src/evaluation/metrics.py",
)

ARMS: dict[str, dict[str, Any]] = {
    "EV03": {
        "name": "EV-03 flat normative BM25 corrective",
        "historical_commit": "df60c77287c8fd5f128b136625dc149bc5aaaeb2",
        "runner": "src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py",
        "corpus": "data/processed/corpus_rag_v1_index.jsonl",
        "metadata": "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json",
        "results_key": "normative_results_csv",
        "summary_key": "normative_case_summary_csv",
        "depth": 100,
        "prospective_corpus": "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.1.jsonl",
        "prospective_index_root": "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.1",
        "prospective_output_root": "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.1",
        "spec_name": "ev03_corrective_execution_spec_v0.1.json",
        "overlap_name": "ev03_original_ranking_overlap_v0.1.json",
        "overlap_csv_name": "ev03_original_ranking_overlap_v0.1.csv",
    },
    "EV04": {
        "name": "EV-04 hierarchical normative BM25 corrective",
        "historical_commit": "e3590cf8ea07d0cbcec97a5a41931220c56a3ce0",
        "runner": "src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py",
        "corpus": "data/processed/corpus_nandina_hierarchical_v0.1.jsonl",
        "metadata": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json",
        "results_key": "normative_hierarchical_results_csv",
        "summary_key": "normative_hierarchical_case_summary_csv",
        "depth": 200,
        "prospective_corpus": "data/processed/corpus_nandina_hierarchical_ev04_corrective_decision906_v0.1.jsonl",
        "prospective_index_root": "data/processed/indexes/bm25_nandina8_hierarchical_ev04_corrective_decision906_v0.1",
        "prospective_output_root": "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.1",
        "spec_name": "ev04_corrective_execution_spec_v0.1.json",
        "overlap_name": "ev04_original_ranking_overlap_v0.1.json",
        "overlap_csv_name": "ev04_original_ranking_overlap_v0.1.csv",
    },
}


def canonical_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def posix_relative(value: str | Path) -> str:
    """Return a repository-relative serialization independent of the host OS."""

    candidate = Path(value)
    require(not candidate.is_absolute(), f"Persistent path must be repository-relative: {value}")
    normalized = candidate.as_posix()
    require("\\" not in normalized, f"Persistent path must use POSIX separators: {value}")
    return normalized


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, f"CSV without header: {path}")
        return [{str(key): (value or "").strip() for key, value in row.items() if key is not None} for row in reader]


def git_revision_blob(root: Path, revision: str, relative: str) -> str | None:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), "rev-parse", f"{revision}:{relative}"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def integrated_base_is_ancestor(root: Path, base_commit: str = INTEGRATED_BASE_COMMIT) -> bool:
    """Return whether the approved integration remains in the candidate ancestry."""

    result = subprocess.run(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), "merge-base", "--is-ancestor", base_commit, "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def head_text_identity(root: Path, relative: str) -> dict[str, str]:
    require(git_path_is_tracked(root, relative), f"Frozen text path is not tracked: {relative}")
    require(git_worktree_semantically_clean(root, relative), f"Frozen text path has local modifications: {relative}")
    blob = git_head_blob_sha(root, relative)
    digest = git_blob_sha256(root, blob)
    return {
        "identity_authority": "COMMITTED_GIT_BLOB",
        "path": relative,
        "git_blob_sha": blob,
        "canonical_blob_sha256": digest,
        "historical_sha256": digest,
    }


def historical_identity(root: Path, revision: str, relative: str) -> dict[str, str] | None:
    blob = git_revision_blob(root, revision, relative)
    if blob is None:
        return None
    return {
        "revision": revision,
        "path": relative,
        "git_blob_sha": blob,
        "canonical_blob_sha256": git_blob_sha256(root, blob),
    }


def validate_current_text_identity(root: Path, identity: Mapping[str, Any], label: str) -> bytes:
    require(identity.get("identity_authority") == "COMMITTED_GIT_BLOB", f"Identity authority changed: {label}")
    return canonical_frozen_text_bytes(root, identity, label)


def validate_run_metadata(root: Path, arm: Mapping[str, Any]) -> dict[str, Any]:
    metadata_path = project_path(root, str(arm["metadata"]))
    require(metadata_path.is_file(), f"Frozen run metadata is missing: {arm['metadata']}")
    require(git_path_is_tracked(root, str(arm["metadata"])), f"Frozen run metadata is not tracked: {arm['metadata']}")
    require(git_worktree_semantically_clean(root, str(arm["metadata"])), f"Frozen run metadata has local modifications: {arm['metadata']}")
    metadata = read_json(metadata_path)
    outputs = metadata.get("outputs", {})
    hashes = metadata.get("output_sha256", {})
    require(isinstance(outputs, dict) and isinstance(hashes, dict), f"Frozen metadata output contract malformed: {arm['metadata']}")
    for key, expected in hashes.items():
        relative = outputs.get(key)
        require(isinstance(relative, str), f"Missing output path for {key} in {arm['metadata']}")
        path = project_path(root, relative)
        require(path.is_file(), f"Frozen output is missing: {relative}")
        require(sha256_file(path) == expected, f"Frozen output SHA changed: {relative}")
    return metadata


def source_provenance(root: Path, arm: Mapping[str, Any]) -> dict[str, Any]:
    revision = str(arm["historical_commit"])
    paths = (str(arm["runner"]), CONFIG_PATH, str(arm["corpus"]), EVAL_PATH)
    historical = {path: historical_identity(root, revision, path) for path in paths}
    missing = [path for path, identity in historical.items() if identity is None]
    current = {path: head_text_identity(root, path) for path in paths}
    for path, identity in current.items():
        validate_current_text_identity(root, identity, f"{arm['name']} current {path}")
    if missing:
        status = "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS"
        reason = "Historical execution commit lacks required tracked source paths; frozen output hashes remain available but do not cryptographically bind the original executable source."
    else:
        status = "FULLY_VERIFIABLE_FROM_FROZEN_ARTIFACTS"
        reason = "Historical metadata, outputs, runner, configuration, corpus, and EVAL resolve to committed Git identities."
    return {
        "status": status,
        "reason": reason,
        "historical_execution_commit": revision,
        "historical_git_identities": historical,
        "historical_missing_tracked_paths": missing,
        "prospective_current_git_identities": current,
    }


def eval_case_ids(root: Path) -> set[str]:
    identity = head_text_identity(root, EVAL_PATH)
    rows = read_csv(project_path(root, EVAL_PATH))
    case_ids = {row.get("case_id", "") for row in rows}
    require(len(rows) == 1056 and len(case_ids) == 1056 and "" not in case_ids, "Frozen EVAL case set changed")
    validate_current_text_identity(root, identity, "EVAL")
    return case_ids


def scan_overlap(root: Path, arm_name: str, arm: Mapping[str, Any], metadata: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    outputs = metadata["outputs"]
    result_path = project_path(root, str(outputs[arm["results_key"]]))
    summary_path = project_path(root, str(outputs[arm["summary_key"]]))
    rows = read_csv(result_path)
    summary_rows = read_csv(summary_path)
    expected_cases = eval_case_ids(root)
    summary_cases = {row.get("case_id", "") for row in summary_rows}
    require(summary_cases == expected_cases, f"{arm_name} case summary no longer matches frozen EVAL")
    by_case: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        case_id = row.get("case_id", "")
        require(case_id in expected_cases, f"{arm_name} ranking references an unknown case: {case_id}")
        rank = int(row.get("candidate_rank", "0"))
        require(1 <= rank <= int(arm["depth"]), f"{arm_name} ranking depth changed for {case_id}")
        by_case.setdefault(case_id, []).append(row)
    for case_id, case_rows in by_case.items():
        ranks = [int(row["candidate_rank"]) for row in case_rows]
        require(len(ranks) == len(set(ranks)), f"{arm_name} duplicate effective rank in {case_id}")
    matched = [row for row in rows if row.get("candidate_code") in TARGET_CODES]
    occurrences = [
        {
            "case_id": row["case_id"],
            "nandina_ref": row.get("nandina_ref", ""),
            "candidate_rank": int(row["candidate_rank"]),
            "candidate_raw_rank": int(row["candidate_raw_rank"]) if row.get("candidate_raw_rank") else None,
            "candidate_code": row["candidate_code"],
            "candidate_doc_id": row.get("candidate_doc_id", ""),
            "score": row.get("score", ""),
        }
        for row in matched
    ]
    per_code: dict[str, Any] = {}
    for code in TARGET_CODES:
        code_rows = [row for row in occurrences if row["candidate_code"] == code]
        ranks = [int(row["candidate_rank"]) for row in code_rows]
        per_code[code] = {
            "occurrences": len(code_rows),
            "distinct_cases": len({row["case_id"] for row in code_rows}),
            "minimum_rank": min(ranks) if ranks else None,
            "maximum_rank": max(ranks) if ranks else None,
        }
    summary = {
        "artifact_id": f"{arm_name.lower()}_original_full_ranking_overlap_v0.1",
        "scan_scope": "FULL_FROZEN_RANKING_ARTIFACT_NO_RERETRIEVAL",
        "ranking_path": posix_relative(str(outputs[arm["results_key"]])),
        "ranking_sha256": sha256_file(result_path),
        "case_summary_path": posix_relative(str(outputs[arm["summary_key"]])),
        "case_summary_sha256": sha256_file(summary_path),
        "ranking_depth": int(arm["depth"]),
        "ranking_rows_scanned": len(rows),
        "cases_scanned": len(expected_cases),
        "cases_with_ranked_rows": len(by_case),
        "cases_without_ranked_rows": len(expected_cases - set(by_case)),
        "complete_case_universe_verified": True,
        "target_codes": list(TARGET_CODES),
        "total_occurrences": len(occurrences),
        "affected_cases": len({row["case_id"] for row in occurrences}),
        "per_code": per_code,
        "occurrences": occurrences,
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
    }
    return summary, occurrences


def line_records(canonical_bytes: bytes) -> dict[str, tuple[bytes, dict[str, Any]]]:
    records: dict[str, tuple[bytes, dict[str, Any]]] = {}
    for raw_line in canonical_bytes.splitlines():
        payload = json.loads(raw_line)
        code = str(payload.get("codigo", "")).strip()
        if code in TARGET_CODES:
            require(code not in records, f"Duplicate target code in canonical corpus: {code}")
            records[code] = (raw_line, payload)
    require(tuple(records) == TARGET_CODES, "Canonical corpus does not contain exactly both target codes")
    return records


def flat_patches(canonical_bytes: bytes) -> list[dict[str, Any]]:
    records = line_records(canonical_bytes)
    patches: list[dict[str, Any]] = []
    for code in TARGET_CODES:
        raw_line, row = records[code]
        require(row.get("version") == "Decision_885", f"EV03 original Decision changed for {code}")
        require(row.get("titulo") == "De peso total con carga máxima inferior a 4,537 t", f"EV03 original title changed for {code}")
        patches.append(
            {
                "code": code,
                "match": {
                    "doc_id": row.get("doc_id"),
                    "codigo": code,
                    "version": "Decision_885",
                    "original_jsonl_line_sha256": sha256_bytes(raw_line),
                },
                "replacement": {
                    "titulo": DECISION_906_TEXT,
                    "texto": f"{DECISION_906_TEXT}. Contexto: Sección XVII / Capítulo 87.",
                    "texto_index": f"{DECISION_906_TEXT}.",
                    "version": "Decision_906",
                },
            }
        )
    return patches


def hierarchical_patches(canonical_bytes: bytes) -> list[dict[str, Any]]:
    records = line_records(canonical_bytes)
    old = "De peso total con carga máxima inferior a 4,537 t"
    patches: list[dict[str, Any]] = []
    for code in TARGET_CODES:
        raw_line, row = records[code]
        require(row.get("version") == "hierarchical_v0.1", f"EV04 hierarchy version changed for {code}")
        derived_fields = ("texto", "texto_index_jerarquico", "texto_index", "source_line_text")
        replacements: dict[str, str] = {
            "titulo": DECISION_906_TEXT,
            "descripcion_nandina_8d": DECISION_906_TEXT,
        }
        for field in derived_fields:
            original = str(row.get(field, ""))
            require(original.count(old) == 1, f"EV04 leaf representation changed for {code}: {field}")
            replacements[field] = original.replace(old, DECISION_906_TEXT)
        patches.append(
            {
                "code": code,
                "match": {
                    "doc_id": row.get("doc_id"),
                    "codigo": code,
                    "version": "hierarchical_v0.1",
                    "original_jsonl_line_sha256": sha256_bytes(raw_line),
                    "preserved_node_fields": {
                        field: row.get(field)
                        for field in ("section", "chapter", "partida_4d", "hs_6d", "nandina_8d", "source_page", "source_line_no", "unidad_fisica")
                    },
                },
                "replacement": replacements,
            }
        )
    return patches


def future_roots(d1a_spec: Mapping[str, Any]) -> list[str]:
    roots = [posix_relative(str(arm["prospective_corpus"])) for arm in ARMS.values()]
    roots += [posix_relative(str(arm["prospective_index_root"])) for arm in ARMS.values()]
    roots += [posix_relative(str(arm["prospective_output_root"])) for arm in ARMS.values()]
    roots += [posix_relative(str(path)) for path in d1a_spec["orchestration"]["future_roots"]]
    require(len(roots) == len(set(roots)), "Prospective root contract contains duplicates")
    return roots


def require_absent(root: Path, relatives: Iterable[str], label: str) -> None:
    for relative in relatives:
        require(not project_path(root, relative).exists(), f"{label} already exists: {relative}")


def validate_d1a_reference(root: Path) -> dict[str, Any]:
    identity = head_text_identity(root, D1A_SPEC_PATH)
    canonical = validate_current_text_identity(root, identity, "Integrated D1a execution specification")
    spec = json.loads(canonical)
    require(spec.get("specification_status") == "CLOSED_PROSPECTIVELY", "D1a execution specification is not prospectively closed")
    require(spec.get("authorization", {}).get("D1A_NUMERICAL_EXECUTION") == "NOT_AUTHORIZED", "D1a numerical execution changed")
    return {
        "reference": {
            **identity,
            "artifact_sha256": sha256_file(project_path(root, D1A_SPEC_PATH)),
        },
        "specification_status": spec["specification_status"],
        "D1A_NUMERICAL_EXECUTION": spec["authorization"]["D1A_NUMERICAL_EXECUTION"],
        "spec": spec,
    }


def execution_commands(arm_name: str, arm: Mapping[str, Any]) -> dict[str, str]:
    """Freeze the exact, already-versioned commands for a future authorization."""

    corpus = posix_relative(str(arm["prospective_corpus"]))
    index_root = posix_relative(str(arm["prospective_index_root"]))
    output_root = posix_relative(str(arm["prospective_output_root"]))
    build = (
        f"python -m src.experiments.build_bm25_corrective_0b05c_v01 --arm {arm_name} "
        f"--corpus {corpus} --output {index_root}/index.json --metadata {index_root}/index_metadata.json"
    )
    evaluate = (
        f"python -m src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 --arm {arm_name} "
        f"--corpus {corpus} --index {index_root}/index.json --index-metadata {index_root}/index_metadata.json "
        f"--output-dir {output_root}"
    )
    commands = {
        f"{arm_name.lower()}_build_command": build,
        f"{arm_name.lower()}_evaluate_command": evaluate,
        "d1a_execute_command": "python -m src.experiments.run_d1a_corrective_0b05c_v01 --execute-authorized",
        "unified_execution_command": "python -m src.experiments.run_0b05c_corrective_numerical_v01 --execute-authorized",
    }
    if arm_name == "EV04":
        control_corpus = posix_relative(str(arm["corpus"]))
        control_index = f"{output_root}/decision885_control_index"
        control_output = f"{output_root}/decision885_control"
        commands.update(
            {
                "ev04_control_reproduction_build_command": f"python -m src.experiments.build_bm25_corrective_0b05c_v01 --arm EV04 --corpus {control_corpus} --output {control_index}/index.json --metadata {control_index}/index_metadata.json",
                "ev04_control_reproduction_evaluate_command": f"python -m src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 --arm EV04 --corpus {control_corpus} --index {control_index}/index.json --index-metadata {control_index}/index_metadata.json --output-dir {control_output}",
                "ev04_corrected_build_command": build,
                "ev04_corrected_evaluate_command": evaluate,
            }
        )
    return commands


def execution_binding(root: Path) -> dict[str, Any]:
    identities = {path: head_text_identity(root, path) for path in FROZEN_EXECUTION_DEPENDENCIES}
    for path, identity in identities.items():
        validate_current_text_identity(root, identity, f"Prospective execution dependency {path}")
    return {
        "identity_authority": "COMMITTED_GIT_BLOB",
        "orchestration_runner": identities[RUNNER_PATH],
        "corrective_builder": identities[BUILDER_PATH],
        "corrective_evaluator": identities[EVALUATOR_PATH],
        "frozen_dependencies": identities,
        "semantic_reuse": {
            "flat": "Versioned helpers are imported from evaluate_normative_bm25_flat_data_aduanas_v02.py; its fixed historical SHA assertions are not used for a derived corrective corpus.",
            "hierarchical": "Versioned helpers are imported from evaluate_normative_bm25_hierarchical_data_aduanas_v02.py, including duplicate-code collapse where the first BM25 occurrence by score order wins.",
            "bm25": "Corrective indexes use build_bm25_from_corpus from src/bm25_index.py with k1=1.5, b=0.75 and the frozen stopword policy.",
        },
    }


def control_reproduction_contract(arm_name: str, arm: Mapping[str, Any], metadata: Mapping[str, Any]) -> dict[str, Any]:
    """Describe the mandatory, future control run without performing it now."""

    outputs = metadata["outputs"]
    if arm_name == "EV04":
        return {
            "gate": "EV04_DECISION885_REPRODUCTION_GATE",
            "requirement": "MANDATORY",
            "current_state": "NOT_EXECUTED",
            "historical_source_status": "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS",
            "comparison": {
                "ranking": {
                    "path": posix_relative(str(outputs[arm["results_key"]])),
                    "sha256": metadata["output_sha256"][arm["results_key"]],
                    "scope": "EXACT_EFFECTIVE_FULL_TOP200_CASE_LEVEL",
                },
                "case_summary": {
                    "path": posix_relative(str(outputs[arm["summary_key"]])),
                    "sha256": metadata["output_sha256"][arm["summary_key"]],
                    "scope": "EXACT_CASE_LEVEL",
                },
                "metrics": "EXACT_NUMERATORS_DENOMINATORS_AND_VALUES; timestamps and runtime metadata are excluded",
            },
            "failure_policy": "A non-PASS reproduction blocks EV04 corrected execution and the unified gate.",
        }
    return {
        "gate": "EV03_CONTROL_REPRODUCTION_GATE",
        "requirement": "MANDATORY_INTEGRITY_CHECK",
        "current_state": "NOT_EXECUTED",
        "comparison": "Verify frozen full TOP100 ranking, case summary, and metric contract before corrected execution.",
        "failure_policy": "A non-PASS reproduction blocks EV03 corrected execution and the unified gate.",
    }


def build_arm_spec(root: Path, arm_name: str, arm: Mapping[str, Any], metadata: Mapping[str, Any], provenance: Mapping[str, Any]) -> dict[str, Any]:
    corpus_identity = provenance["prospective_current_git_identities"][str(arm["corpus"])]
    corpus_bytes = validate_current_text_identity(root, corpus_identity, f"{arm_name} frozen corpus")
    patches = flat_patches(corpus_bytes) if arm_name == "EV03" else hierarchical_patches(corpus_bytes)
    parameters = metadata.get("parameters", {})
    require(parameters.get("k1") == 1.5 and parameters.get("b") == 0.75, f"{arm_name} BM25 parameters changed")
    require(parameters.get("retrieval_depth") == arm["depth"], f"{arm_name} retrieval depth changed")
    outputs = metadata["outputs"]
    return {
        "specification_id": f"{arm_name.lower()}_corrective_execution_spec_v0.1",
        "specification_status": "CLOSED_PROSPECTIVELY/PENDING_EXTERNAL_AUDIT",
        "authorization": {f"{arm_name}_NUMERICAL_EXECUTION": "NOT_AUTHORIZED", "corrective_retrieval_executed": False, "corrective_metrics_computed": False},
        "original_run_identity": provenance,
        "frozen_inputs": {
            "runner": provenance["prospective_current_git_identities"][str(arm["runner"])],
            "config": provenance["prospective_current_git_identities"][CONFIG_PATH],
            "corpus": corpus_identity,
            "eval": provenance["prospective_current_git_identities"][EVAL_PATH],
            "index_identity_from_frozen_run_metadata": {
                "path": metadata["inputs"].get("index", metadata["inputs"].get("hierarchical_index")),
                "sha256": metadata["inputs"].get("index_sha256", metadata["inputs"].get("hierarchical_index_sha256")),
                "current_checkout_presence_required": False,
            },
            "query_column": "DESCRIPCION DE MERCANCIAS CONCATENADA",
            "label_column": "NANDINA",
            "eval_cases": 1056,
            "bm25_parameters": parameters,
        },
        "primary_original_control": {
            "decision": "Decision_885",
            "historical_execution_verification": provenance["status"],
            "run_metadata": {**head_text_identity(root, str(arm["metadata"])), "artifact_sha256": sha256_file(project_path(root, str(arm["metadata"])))},
            "outputs": {
                key: {"path": path, "sha256": metadata["output_sha256"][key]}
                for key, path in outputs.items() if key in metadata["output_sha256"]
            },
            "metric_definitions": metadata.get("metrics", {}).get("metric_table", []),
            "comparison_policy": "Use only frozen original definitions and aligned case_ids; no original result is a target and no prospective metric is calculated by this gate.",
            "control_reproduction": control_reproduction_contract(arm_name, arm, metadata),
        },
        "corrective_corpus": {
            "prospective_path": arm["prospective_corpus"],
            "must_be_absent_before_authorized_execution": True,
            "patch_scope": "EXACTLY_TWO_NANDINA8_DOCUMENTS",
            "authoritative_normative_source": {
                "decision": "Decision 906", "official_gazette": "Gaceta Oficial 5062", "published_on": "2022-10-25", "effective_on": "2023-01-01",
                "annex_entries": {code: DECISION_906_TEXT for code in TARGET_CODES},
            },
            "patches": patches,
            "preservation_invariants": [
                "Preserve cardinality, JSONL row order, doc_id, codigo, and all unpatched bytes.",
                "Apply only the two matched documents using their canonical Git JSONL line SHA-256 identities.",
                "Serialize a future derived corpus in UTF-8 with LF and exactly one terminal newline.",
                "For EV04 preserve hierarchy node identifiers, parent fields, source-page lineage, and deterministic ordering; change only declared leaf/derived representations.",
            ],
        },
        "prospective_execution": {
            "full_rebuild_policy": "FULL_NON_DESTRUCTIVE_REBUILD_NO_OVERWRITE_NO_RESUME",
            "prospective_index_root": posix_relative(str(arm["prospective_index_root"])),
            "prospective_output_root": posix_relative(str(arm["prospective_output_root"])),
            "required_outputs": ["case_level_output", "aggregate_output", "original_vs_corrective_comparison", "execution_manifest", "output_hash_ledger", "summary"],
            "execution_order": ["unified_preflight", "control_reproduction", "corrected_retrieval", "validation", "comparison", "manifest", "ledger", "interpretation"],
            "commands": execution_commands(arm_name, arm),
            "derived_identity_policy": "The future evaluator validates the SHA-256 values derived by its own corrective corpus and corrective index build; it never substitutes historic fixed corpus or index hashes.",
        },
    }


def frozen_artifact_paths(root: Path) -> dict[str, Path]:
    paths = {"gate": project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"))}
    for arm_name, arm in ARMS.items():
        paths[f"{arm_name}_spec"] = project_path(root, str(AUDIT_ROOT / arm["spec_name"]))
        paths[f"{arm_name}_overlap"] = project_path(root, str(AUDIT_ROOT / arm["overlap_name"]))
    paths["manifest"] = project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_gate_artifact_manifest_v0.1.json"))
    return paths


def require_posix_serialization(payload: Any, label: str) -> None:
    """Fail on an OS-dependent separator anywhere in persisted gate payloads."""

    if isinstance(payload, Mapping):
        for key, value in payload.items():
            require_posix_serialization(value, f"{label}.{key}")
    elif isinstance(payload, list):
        for index, value in enumerate(payload):
            require_posix_serialization(value, f"{label}[{index}]")
    elif isinstance(payload, str):
        require("\\" not in payload, f"OS-dependent serialized repository path: {label}")


def require_frozen_bundle_matches(root: Path, bundle: Mapping[str, Any]) -> None:
    """Reject a committed source/control change after the prospective freeze."""

    paths = frozen_artifact_paths(root)
    expected: dict[str, Mapping[str, Any]] = {"gate": bundle["gate"]}
    for arm_name in ARMS:
        expected[f"{arm_name}_spec"] = bundle["specifications"][arm_name]
        expected[f"{arm_name}_overlap"] = bundle["overlaps"][arm_name]
    for key, expected_payload in expected.items():
        path = paths[key]
        require(path.is_file(), f"Frozen gate artifact is missing: {path.relative_to(root).as_posix()}")
        actual_payload = read_json(path)
        require_posix_serialization(actual_payload, path.relative_to(root).as_posix())
        require(
            canonical_json_bytes(actual_payload) == canonical_json_bytes(expected_payload),
            f"Frozen gate artifact no longer matches live canonical inputs: {path.relative_to(root).as_posix()}",
        )
    manifest_path = paths["manifest"]
    require(manifest_path.is_file(), f"Frozen gate artifact manifest is missing: {manifest_path.relative_to(root).as_posix()}")
    require_posix_serialization(read_json(manifest_path), manifest_path.relative_to(root).as_posix())


def preflight(root: Path = ROOT, *, require_frozen_artifacts: bool = True) -> dict[str, Any]:
    require(git_revision_blob(root, "HEAD", "README.md") is not None, "Repository HEAD cannot be resolved")
    require(
        integrated_base_is_ancestor(root),
        "Integrated base commit is not an ancestor of the candidate HEAD for 0B-05C numerical gate",
    )
    for arm_name, arm in ARMS.items():
        metadata = validate_run_metadata(root, arm)
        provenance = source_provenance(root, arm)
        if arm_name == "EV03":
            require(provenance["status"] == "FULLY_VERIFIABLE_FROM_FROZEN_ARTIFACTS", "EV03 original run provenance changed")
        else:
            require(provenance["status"] == "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS", "EV04 historical provenance limitation changed")
        validate_code_identity(root, provenance["prospective_current_git_identities"][str(arm["runner"])])
    d1a = validate_d1a_reference(root)
    roots = future_roots(d1a["spec"])
    require_absent(root, roots, "Prospective numerical root")
    bundle = build_bundle(root, d1a)
    require_posix_serialization(bundle, "live_bundle")
    if require_frozen_artifacts:
        require_frozen_bundle_matches(root, bundle)
    return {"status": "PASS", "mode": "PREFLIGHT_ONLY", "numerical_execution_occurred": False, "bundle": bundle}


def build_bundle(root: Path, d1a: Mapping[str, Any] | None = None) -> dict[str, Any]:
    d1a = d1a or validate_d1a_reference(root)
    arm_specs: dict[str, dict[str, Any]] = {}
    overlaps: dict[str, dict[str, Any]] = {}
    overlap_rows: dict[str, list[dict[str, Any]]] = {}
    for arm_name, arm in ARMS.items():
        metadata = validate_run_metadata(root, arm)
        provenance = source_provenance(root, arm)
        arm_specs[arm_name] = build_arm_spec(root, arm_name, arm, metadata, provenance)
        overlaps[arm_name], overlap_rows[arm_name] = scan_overlap(root, arm_name, arm, metadata)
    gate = {
        "gate_id": "0B05C_CORRECTIVE_NUMERICAL_EXECUTION_GATE_v0.1",
        "gate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "integrated_base_commit": INTEGRATED_BASE_COMMIT,
        "integrated_base_ancestry_requirement": "INTEGRATED_BASE_COMMIT must be an ancestor of candidate HEAD; main is not required to remain byte-identical after approved integrations.",
        "authorization": {
            "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "corrective_retrieval_executed": False,
            "corrective_metrics_computed": False,
        },
        "arms": {
            arm_name: {
                "specification_path": posix_relative(AUDIT_ROOT / ARMS[arm_name]["spec_name"]),
                "specification_sha256": sha256_bytes(canonical_json_bytes(spec)),
                "original_ranking_overlap_path": posix_relative(AUDIT_ROOT / ARMS[arm_name]["overlap_name"]),
                "original_ranking_overlap_sha256": sha256_bytes(canonical_json_bytes(overlaps[arm_name])),
                "original_run_identity": spec["original_run_identity"]["status"],
            }
            for arm_name, spec in arm_specs.items()
        },
        "d1a_existing_specification": {
            key: value for key, value in d1a.items() if key != "spec"
        },
        "corrective_execution_binding": execution_binding(root),
        "future_execution_order": [
            "01_unified_preflight",
            "02_EV03_control_reproduction",
            "03_EV03_control_comparison",
            "04_EV03_corrected_corpus_and_index",
            "05_EV03_corrected_evaluation",
            "06_EV04_Decision885_control_reproduction",
            "07_EV04_control_comparison_must_pass",
            "08_EV04_corrected_corpus_and_index",
            "09_EV04_corrected_evaluation",
            "10_case_level_comparisons",
            "11_aggregate_comparisons",
            "12_unified_sensitivity_summary",
            "13_manifest_and_hash_ledger",
            "14_D1a_execute_only_under_its_own_authorization",
        ],
        "fail_closed_preflight": [
            "reject an unrelated candidate that does not descend from the integrated base", "reject frozen control/output/code/config/EVAL/corpus identity changes", "reject Decision 906 or exactly-two-entry changes",
            "reject an existing prospective root, partial output, overwrite, or resume", "reject D1a specification change", "reject an already-executed arm or pre-existing corrective metric",
            "reject execution while authorization remains NOT_AUTHORIZED", "reject EV04 corrected execution unless mandatory Decision885 reproduction is PASS",
        ],
        "decisions": {
            "D1A_PREEXECUTION": "APPROVED/INTEGRATED",
            "D1A_EXECUTION_SPECIFICATION": "CLOSED_PROSPECTIVELY",
            "0B05C_METRIC_IMPACT": "NOT_DETERMINED",
            "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED",
            "0B05C_CLOSURE": "NOT_AUTHORIZED",
            "EXP11B_PORTABILITY_DEBT": "OPEN",
            "EXP11B_PORTABILITY_DEBT_BLOCKS_D1A": False,
            "EXP11B_PORTABILITY_DEBT_BLOCKS_EXP11B_RETRIEVAL_AUTHORIZATION": True,
            "EV04_ORIGINAL_HISTORICAL_EXECUTION": "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS",
            "EV04_DECISION885_REPRODUCTION_GATE": "MANDATORY/NOT_EXECUTED",
        },
        "future_authorization_transition_contract": {
            "allowed_mutations": ["authorization state fields from NOT_AUTHORIZED to AUTHORIZED", "mechanically-derived runtime hashes", "execution manifests"],
            "forbidden_mutations": ["patches", "queries", "base corpora", "weights", "BM25 semantics", "metric contracts", "reproduction rules", "runners", "builders", "evaluators", "output paths", "execution order", "comparison schema"],
            "d1a_authorization": "D1a remains independently governed by its own authorization contract.",
        },
    }
    return {"specifications": arm_specs, "overlaps": overlaps, "overlap_rows": overlap_rows, "gate": gate}


def write_new(path: Path, data: bytes, *, replace_existing: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "wb" if replace_existing else "xb"
    with path.open(mode) as handle:
        handle.write(data)


def csv_bytes(rows: list[dict[str, Any]]) -> bytes:
    fields = ["case_id", "nandina_ref", "candidate_rank", "candidate_raw_rank", "candidate_code", "candidate_doc_id", "score"]
    lines: list[str] = []
    from io import StringIO

    buffer = StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def write_frozen_artifacts(root: Path = ROOT, *, replace_existing: bool = False) -> dict[str, Any]:
    """Create or deliberately refresh only static audit/freeze artifacts.

    This function never touches prospective corpus, index, or evaluation roots.
    A refresh is needed only after a reviewed contract microclose changes the
    immutable static description of the future execution.
    """

    result = preflight(root, require_frozen_artifacts=False)
    bundle = result["bundle"]
    written: list[Path] = []
    for arm_name, arm in ARMS.items():
        spec_path = project_path(root, str(AUDIT_ROOT / arm["spec_name"]))
        overlap_path = project_path(root, str(AUDIT_ROOT / arm["overlap_name"]))
        csv_path = project_path(root, str(AUDIT_ROOT / arm["overlap_csv_name"]))
        write_new(spec_path, canonical_json_bytes(bundle["specifications"][arm_name]), replace_existing=replace_existing)
        write_new(overlap_path, canonical_json_bytes(bundle["overlaps"][arm_name]), replace_existing=replace_existing)
        write_new(csv_path, csv_bytes(bundle["overlap_rows"][arm_name]), replace_existing=replace_existing)
        written.extend((spec_path, overlap_path, csv_path))
    gate_path = project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"))
    write_new(gate_path, canonical_json_bytes(bundle["gate"]), replace_existing=replace_existing)
    written.append(gate_path)
    manifest = {
        "artifact_id": "0b05c_corrective_numerical_gate_artifact_manifest_v0.1",
        "generation_mode": "STATIC_AUDIT_AND_PROSPECTIVE_FREEZE_ONLY",
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "files": [{"path": path.relative_to(root).as_posix(), "sha256": sha256_file(path)} for path in written],
    }
    manifest_path = project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_gate_artifact_manifest_v0.1.json"))
    write_new(manifest_path, canonical_json_bytes(manifest), replace_existing=replace_existing)
    return {"written": [path.relative_to(root).as_posix() for path in [*written, manifest_path]], **result}


def execute(root: Path = ROOT) -> None:
    """Compatibility guard; the bound runner owns prospective execution."""

    preflight(root)
    raise ContractViolation("Numerical execution is not authorized; use of the bound runner remains fail-closed until a separate authorization.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="0B-05C prospective corrective numerical gate.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--write-frozen-artifacts", action="store_true")
    group.add_argument("--refresh-frozen-artifacts", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if args.execute:
        execute(ROOT)
    elif args.write_frozen_artifacts:
        print(json.dumps(write_frozen_artifacts(ROOT), ensure_ascii=False, indent=2, default=str))
    elif args.refresh_frozen_artifacts:
        print(json.dumps(write_frozen_artifacts(ROOT, replace_existing=True), ensure_ascii=False, indent=2, default=str))
    else:
        print(json.dumps(preflight(ROOT), ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
