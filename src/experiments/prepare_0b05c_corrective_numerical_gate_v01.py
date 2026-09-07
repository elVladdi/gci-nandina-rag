"""Freeze the non-executing 0B-05C corrective numerical sensitivity gate.

This module audits frozen EV-03/EV-04 outputs and links the already-integrated
D1a specification.  It deliberately contains no retrieval, indexing, or metric
calculation path.  ``--execute`` is an explicit fail-closed guard.
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
BASE_MAIN = "7ff504c4a5a763705f198ca41753db75e938a87d"
AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.1")
TARGET_CODES = ("87044110", "87045110")
DECISION_906_TEXT = "Inferior a 4,537 t"
EVAL_PATH = "data/processed/data_aduanas_evalset_clase87_v0.2.csv"
CONFIG_PATH = "src/configs/experiment_config.json"
D1A_SPEC_PATH = "outputs/audits/d1a_preexecution_0b05c_v0.1/d1a_0b05c_corrective_execution_spec_v0.1.json"

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
        "ranking_path": str(outputs[arm["results_key"]]),
        "ranking_sha256": sha256_file(result_path),
        "case_summary_path": str(outputs[arm["summary_key"]]),
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
    roots = [str(arm["prospective_corpus"]) for arm in ARMS.values()]
    roots += [str(arm["prospective_index_root"]) for arm in ARMS.values()]
    roots += [str(arm["prospective_output_root"]) for arm in ARMS.values()]
    roots += [str(path) for path in d1a_spec["orchestration"]["future_roots"]]
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
            "run_metadata": {**head_text_identity(root, str(arm["metadata"])), "artifact_sha256": sha256_file(project_path(root, str(arm["metadata"])))},
            "outputs": {
                key: {"path": path, "sha256": metadata["output_sha256"][key]}
                for key, path in outputs.items() if key in metadata["output_sha256"]
            },
            "metric_definitions": metadata.get("metrics", {}).get("metric_table", []),
            "comparison_policy": "Use only frozen original definitions and aligned case_ids; no original result is a target and no prospective metric is calculated by this gate.",
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
            "prospective_index_root": arm["prospective_index_root"],
            "prospective_output_root": arm["prospective_output_root"],
            "required_outputs": ["case_level_output", "original_vs_corrective_comparison", "execution_manifest", "output_hash_ledger", "summary"],
            "execution_order": ["unified_preflight", "corrected_retrieval", "validation", "comparison", "manifest", "ledger", "interpretation"],
        },
    }


def frozen_artifact_paths(root: Path) -> dict[str, Path]:
    paths = {"gate": project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"))}
    for arm_name, arm in ARMS.items():
        paths[f"{arm_name}_spec"] = project_path(root, str(AUDIT_ROOT / arm["spec_name"]))
        paths[f"{arm_name}_overlap"] = project_path(root, str(AUDIT_ROOT / arm["overlap_name"]))
    return paths


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
        require(
            canonical_json_bytes(actual_payload) == canonical_json_bytes(expected_payload),
            f"Frozen gate artifact no longer matches live canonical inputs: {path.relative_to(root).as_posix()}",
        )


def preflight(root: Path = ROOT, *, require_frozen_artifacts: bool = True) -> dict[str, Any]:
    require(git_revision_blob(root, "HEAD", "README.md") is not None, "Repository HEAD cannot be resolved")
    main = subprocess.run(["git", "-c", f"safe.directory={root}", "-C", str(root), "rev-parse", "main"], check=False, capture_output=True, text=True)
    require(main.returncode == 0 and main.stdout.strip() == BASE_MAIN, "main unexpected for 0B-05C numerical gate")
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
        "base_main": BASE_MAIN,
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
                "specification_path": str(AUDIT_ROOT / ARMS[arm_name]["spec_name"]),
                "specification_sha256": sha256_bytes(canonical_json_bytes(spec)),
                "original_ranking_overlap_path": str(AUDIT_ROOT / ARMS[arm_name]["overlap_name"]),
                "original_ranking_overlap_sha256": sha256_bytes(canonical_json_bytes(overlaps[arm_name])),
                "original_run_identity": spec["original_run_identity"]["status"],
            }
            for arm_name, spec in arm_specs.items()
        },
        "d1a_existing_specification": {
            key: value for key, value in d1a.items() if key != "spec"
        },
        "future_execution_order": [
            "unified_preflight", "EV03_corrected_flat_normative_BM25", "EV04_corrected_hierarchical_normative_BM25", "D1a_corrected_dense_retrieval",
            "validation", "comparisons", "manifest", "ledger", "interpretation",
        ],
        "fail_closed_preflight": [
            "reject unexpected main", "reject frozen control/output/code/config/EVAL/corpus identity changes", "reject Decision 906 or exactly-two-entry changes",
            "reject an existing prospective root, partial output, overwrite, or resume", "reject D1a specification change", "reject an already-executed arm or pre-existing corrective metric",
            "reject --execute while authorization remains NOT_AUTHORIZED",
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
        },
    }
    return {"specifications": arm_specs, "overlaps": overlaps, "overlap_rows": overlap_rows, "gate": gate}


def write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
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


def write_frozen_artifacts(root: Path = ROOT) -> dict[str, Any]:
    result = preflight(root, require_frozen_artifacts=False)
    bundle = result["bundle"]
    written: list[Path] = []
    for arm_name, arm in ARMS.items():
        spec_path = project_path(root, str(AUDIT_ROOT / arm["spec_name"]))
        overlap_path = project_path(root, str(AUDIT_ROOT / arm["overlap_name"]))
        csv_path = project_path(root, str(AUDIT_ROOT / arm["overlap_csv_name"]))
        write_new(spec_path, canonical_json_bytes(bundle["specifications"][arm_name]))
        write_new(overlap_path, canonical_json_bytes(bundle["overlaps"][arm_name]))
        write_new(csv_path, csv_bytes(bundle["overlap_rows"][arm_name]))
        written.extend((spec_path, overlap_path, csv_path))
    gate_path = project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"))
    write_new(gate_path, canonical_json_bytes(bundle["gate"]))
    written.append(gate_path)
    manifest = {
        "artifact_id": "0b05c_corrective_numerical_gate_artifact_manifest_v0.1",
        "generation_mode": "STATIC_AUDIT_AND_PROSPECTIVE_FREEZE_ONLY",
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "files": [{"path": path.relative_to(root).as_posix(), "sha256": sha256_file(path)} for path in written],
    }
    manifest_path = project_path(root, str(AUDIT_ROOT / "0b05c_corrective_numerical_gate_artifact_manifest_v0.1.json"))
    write_new(manifest_path, canonical_json_bytes(manifest))
    return {"written": [path.relative_to(root).as_posix() for path in [*written, manifest_path]], **result}


def execute(root: Path = ROOT) -> None:
    preflight(root)
    raise ContractViolation("Numerical execution is not authorized; this prospective gate has no executable numerical path and requires a separately authorized commit.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="0B-05C prospective corrective numerical gate.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--write-frozen-artifacts", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if args.execute:
        execute(ROOT)
    elif args.write_frozen_artifacts:
        print(json.dumps(write_frozen_artifacts(ROOT), ensure_ascii=False, indent=2, default=str))
    else:
        print(json.dumps(preflight(ROOT), ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
