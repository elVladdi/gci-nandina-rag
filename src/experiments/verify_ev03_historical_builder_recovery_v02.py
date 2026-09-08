"""Build-only preexecution verification for recovered EV03 semantics v0.2.

This command can reconstruct and evaluate only the frozen Decision885 control.
It has no corrected-arm or numerical-authorization mode.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pickle
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from ..bm25_index import sha256_file
from .build_bm25_ev03_historical_recovered_v02 import TOKEN_POLICY, build
from .evaluate_normative_bm25_corrective_0b05c_v01 import (
    EV03_CANDIDATE_FIELDS,
    EV03_CASE_FIELDS,
    _flat_rows,
    _normalize_rows,
    compare_control_reproduction,
)


ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "06cc75ec173eb6c4b134a45eeb88fe25999f396e"
INDEX_INTRO_COMMIT = "975bc9879ec89cc945d5432ef0bac3b37598f72c"
BYTECODE_INTRO_COMMIT = "689f7436a8e2011b3399140c90c7eb6e777b2026"
SOURCE_INTRO_COMMIT = "d73ff147b02d69c65218de4b4bd08d501ff9f5d7"
HISTORICAL_RUN_COMMIT = "df60c77287c8fd5f128b136625dc149bc5aaaeb2"

CORPUS = Path("data/processed/corpus_rag_v1_index.jsonl")
EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
CONFIG = Path("src/configs/experiment_config.json")
HISTORICAL_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
HISTORICAL_METADATA = Path("data/processed/indexes/bm25_nandina8_run_metadata.json")
FROZEN_OUTPUT_ROOT = Path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2")

PREEXEC_INDEX_ROOT = Path("data/processed/indexes/bm25_nandina8_ev03_decision885_preexecution_v0.2")
PREEXEC_INDEX = PREEXEC_INDEX_ROOT / "index.pkl"
PREEXEC_INDEX_METADATA = PREEXEC_INDEX_ROOT / "index_metadata.json"
PREEXEC_OUTPUT_ROOT = Path("outputs/evaluation/0b05c_ev03_decision885_preexecution_v0.2")
AUDIT_ROOT = Path("outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2")

FUTURE_EXECUTION_ROOTS = (
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2",
    "data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2",
    "data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.2",
    "outputs/evaluation/0b05c_corrective_numerical_v0.2",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.2",
    "outputs/evaluation/d1a_corrective_0b05c_v0.2",
)

V01_EVIDENCE_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1",
    "outputs/evaluation/0b05c_corrective_numerical_v0.1",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1",
)

AUDIT_FILES = {
    "provenance": AUDIT_ROOT / "ev03_historical_builder_provenance_v0.2.json",
    "logical_identity": AUDIT_ROOT / "ev03_logical_index_identity_v0.2.json",
    "control_reproduction": AUDIT_ROOT / "ev03_decision885_control_reproduction_v0.2.json",
    "ev03_spec": AUDIT_ROOT / "ev03_corrective_execution_spec_v0.2.json",
    "unified_gate": AUDIT_ROOT / "0b05c_corrective_numerical_gate_v0.2.json",
    "manifest": AUDIT_ROOT / "0b05c_ev03_historical_builder_recovery_manifest_v0.2.json",
    "ledger": AUDIT_ROOT / "0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json",
}

FROZEN_RANKING = FROZEN_OUTPUT_ROOT / "normative_results.csv"
FROZEN_CASE_SUMMARY = FROZEN_OUTPUT_ROOT / "normative_case_summary.csv"
FROZEN_RUN_METADATA = FROZEN_OUTPUT_ROOT / "run_metadata.json"

BINDING_SPECS = (
    ("src/experiments/build_bm25_ev03_historical_recovered_v02.py", "VERSIONED_GIT_BLOB"),
    ("src/experiments/verify_ev03_historical_builder_recovery_v02.py", "VERSIONED_GIT_BLOB"),
    ("src/bm25_index.py", "VERSIONED_GIT_BLOB"),
    ("src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py", "VERSIONED_GIT_BLOB"),
    ("src/retrieval/bm25.py", "VERSIONED_GIT_BLOB"),
    (CONFIG.as_posix(), "VERSIONED_GIT_BLOB"),
    (CORPUS.as_posix(), "VERSIONED_GIT_BLOB"),
    (EVALSET.as_posix(), "VERSIONED_GIT_BLOB"),
    (HISTORICAL_INDEX.as_posix(), "FROZEN_BINARY_GIT_BLOB"),
    (HISTORICAL_METADATA.as_posix(), "VERSIONED_GIT_BLOB"),
    (FROZEN_RANKING.as_posix(), "VERSIONED_GIT_BLOB"),
    (FROZEN_CASE_SUMMARY.as_posix(), "VERSIONED_GIT_BLOB"),
    (FROZEN_RUN_METADATA.as_posix(), "VERSIONED_GIT_BLOB"),
)


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sequence_hash(values: list[Any]) -> str:
    return sha256_bytes(canonical_json_bytes(values))


def doc_lens_hash(values: np.ndarray) -> str:
    array = np.ascontiguousarray(values)
    payload = array.dtype.str.encode("ascii") + b"|" + canonical_json_bytes(list(array.shape)) + b"|" + array.tobytes()
    return sha256_bytes(payload)


def idf_hash(values: Mapping[str, float]) -> str:
    return sha256_bytes(canonical_json_bytes([[key, float(value).hex()] for key, value in sorted(values.items())]))


def inverted_index_hash(values: Mapping[str, list[tuple[int, int]]]) -> str:
    payload = [[term, [[int(doc), int(tf)] for doc, tf in postings]] for term, postings in sorted(values.items())]
    return sha256_bytes(canonical_json_bytes(payload))


def logical_projection(index: Any) -> dict[str, Any]:
    return {
        "k1": float(index.k1),
        "b": float(index.b),
        "doc_ids_count": len(index.doc_ids),
        "doc_ids_sha256": sequence_hash(list(index.doc_ids)),
        "doc_texts_count": len(index.doc_texts),
        "doc_texts_sha256": sequence_hash(list(index.doc_texts)),
        "doc_lens_count": len(index.doc_lens),
        "doc_lens_min": float(np.min(index.doc_lens)),
        "doc_lens_max": float(np.max(index.doc_lens)),
        "doc_lens_mean": float(np.mean(index.doc_lens)),
        "doc_lens_sha256": doc_lens_hash(index.doc_lens),
        "avgdl": float(index.avgdl),
        "vocabulary_size": len(index.idf),
        "idf_sha256": idf_hash(index.idf),
        "postings_count": sum(len(postings) for postings in index.inv_index.values()),
        "inverted_index_sha256": inverted_index_hash(index.inv_index),
    }


def logical_identity(historical: Any, recovered: Any) -> dict[str, Any]:
    historical_projection = logical_projection(historical)
    recovered_projection = logical_projection(recovered)
    checks = {
        "k1_exact": historical.k1 == recovered.k1,
        "b_exact": historical.b == recovered.b,
        "doc_ids_and_order_exact": historical.doc_ids == recovered.doc_ids,
        "doc_texts_and_order_exact": historical.doc_texts == recovered.doc_texts,
        "doc_lens_exact": np.array_equal(historical.doc_lens, recovered.doc_lens),
        "avgdl_exact": historical.avgdl == recovered.avgdl,
        "idf_mapping_exact": historical.idf == recovered.idf,
        "inverted_index_exact": historical.inv_index == recovered.inv_index,
    }
    return {
        "artifact_id": "ev03_logical_index_identity_v0.2",
        "canonical_hash_method": "JSON_UTF8_SORTED_FLOAT_HEX; doc_lens=dtype|shape|contiguous_bytes",
        "historical_index": historical_projection,
        "recovered_index": recovered_projection,
        "checks": checks,
        "LOGICAL_INDEX_IDENTITY": "EXACT" if all(checks.values()) else "FAIL",
        "PICKLE_BYTE_IDENTITY": "NOT_REQUIRED",
    }


def _git(*args: str, binary: bool = False, root: Path = ROOT) -> str | bytes:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    return result.stdout if binary else result.stdout.decode("utf-8").strip()


def _git_blob(path: str, revision: str = "HEAD") -> str:
    object_spec = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
    return str(_git("rev-parse", object_spec))


def git_blob_identity(path: str, classification: str, revision: str = "HEAD") -> dict[str, Any]:
    blob_sha1 = _git_blob(path, revision)
    blob_bytes = bytes(_git("cat-file", "blob", blob_sha1, binary=True))
    return {
        "path": path,
        "classification": classification,
        "git_blob_sha1": blob_sha1,
        "canonical_git_blob_sha256": sha256_bytes(blob_bytes),
        "canonical_size_bytes": len(blob_bytes),
    }


def canonical_bindings(revision: str = "HEAD") -> list[dict[str, Any]]:
    return [git_blob_identity(path, classification, revision) for path, classification in BINDING_SPECS]


def verify_canonical_bindings(expected: list[Mapping[str, Any]], revision: str = "HEAD") -> dict[str, Any]:
    mismatches: list[dict[str, Any]] = []
    for item in expected:
        actual = git_blob_identity(str(item["path"]), str(item["classification"]), revision)
        if dict(item) != actual:
            mismatches.append({"path": item["path"], "expected": dict(item), "actual": actual})
    require(not mismatches, f"Canonical Git dependency binding mismatch: {mismatches}")
    return {"status": "PASS", "checked": len(expected), "mismatch_count": 0}


def _path_at_revision(path: str, revision: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{revision}:{path}"], cwd=ROOT, capture_output=True).returncode == 0


def _row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def _write_csv(path: Path, rows: list[Mapping[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(_normalize_rows(rows))


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    require(not temporary.exists(), f"Temporary artifact path already exists: {temporary}")
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    temporary.replace(path)


def _base_is_ancestor(root: Path = ROOT) -> bool:
    return subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD"], cwd=root, capture_output=True
    ).returncode == 0


def _tracked_clean(root: Path = ROOT) -> bool:
    return not str(_git("status", "--porcelain", "--untracked-files=no", root=root))


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _future_roots_absent(root: Path = ROOT) -> bool:
    return all(not (root / relative).exists() for relative in FUTURE_EXECUTION_ROOTS)


def _run_control_replay(root: Path = ROOT) -> dict[str, Any]:
    require(root.resolve() == ROOT.resolve(), "Verification must run from the repository checkout")
    require(_future_roots_absent(root), "A future numerical root already exists")
    temporary_path: Path | None = None
    replay: dict[str, Any]
    with tempfile.TemporaryDirectory(prefix="0b05c_ev03_committed_replay_") as directory:
        temporary_path = Path(directory)
        corpus_copy = temporary_path / "inputs" / CORPUS.name
        corpus_copy.parent.mkdir(parents=True)
        shutil.copyfile(root / CORPUS, corpus_copy)
        index_path = temporary_path / "index" / "index.pkl"
        metadata_path = temporary_path / "index" / "index_metadata.json"
        output_root = temporary_path / "evaluation"
        build(corpus_copy, index_path, metadata_path, root=temporary_path)

        with (root / HISTORICAL_INDEX).open("rb") as handle:
            historical_index = pickle.load(handle)
        with index_path.open("rb") as handle:
            recovered_index = pickle.load(handle)
        logical = logical_identity(historical_index, recovered_index)
        require(logical["LOGICAL_INDEX_IDENTITY"] == "EXACT", "Recovered EV03 index is not logically exact")

        cases, candidates, metrics = _flat_rows(root / EVALSET, corpus_copy, recovered_index, 100)
        output_root.mkdir(parents=True)
        ranking = output_root / "normative_flat_results.csv"
        case_summary = output_root / "normative_flat_case_summary.csv"
        metrics_file = output_root / "normative_flat_metrics.json"
        _write_csv(ranking, candidates, EV03_CANDIDATE_FIELDS)
        _write_csv(case_summary, cases, EV03_CASE_FIELDS)
        with metrics_file.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump({"metrics": metrics}, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        frozen_metadata = _read_json(root / FROZEN_RUN_METADATA)
        comparison = compare_control_reproduction(
            root / FROZEN_RANKING,
            ranking,
            root / FROZEN_CASE_SUMMARY,
            case_summary,
            frozen_metadata["metrics"],
            metrics,
            expected_candidate_schema=EV03_CANDIDATE_FIELDS,
            expected_case_schema=EV03_CASE_FIELDS,
        )
        ranking_bytes_exact = ranking.read_bytes() == (root / FROZEN_RANKING).read_bytes()
        summary_bytes_exact = case_summary.read_bytes() == (root / FROZEN_CASE_SUMMARY).read_bytes()
        require(ranking_bytes_exact and summary_bytes_exact, "Frozen EV03 CSV bytes are not exact")
        require(frozen_metadata["metrics"] == metrics, "Full frozen EV03 metrics do not match")
        with case_summary.open("r", encoding="utf-8-sig", newline="") as handle:
            witness = next(row for row in csv.DictReader(handle) if row["case_id"] == "DA-EVAL-V02-00001")
        reproduction = {
            "artifact_id": "ev03_decision885_control_reproduction_v0.2",
            "status": "PASS_EXACT",
            "EV03_DECISION885_CONTROL_REPRODUCTION": "PASS_EXACT",
            "comparison": comparison,
            "ranking": {
                "classification": "GENERATED_LOCAL_OUTPUT",
                "path": "TEMPORARY_REPLAY/evaluation/normative_flat_results.csv",
                "size_bytes": ranking.stat().st_size,
                "sha256": sha256_file(ranking),
                "rows": _row_count(ranking),
                "frozen_sha256": sha256_file(root / FROZEN_RANKING),
                "bytes_exact": ranking_bytes_exact,
            },
            "case_summary": {
                "classification": "GENERATED_LOCAL_OUTPUT",
                "path": "TEMPORARY_REPLAY/evaluation/normative_flat_case_summary.csv",
                "size_bytes": case_summary.stat().st_size,
                "sha256": sha256_file(case_summary),
                "rows": _row_count(case_summary),
                "frozen_sha256": sha256_file(root / FROZEN_CASE_SUMMARY),
                "bytes_exact": summary_bytes_exact,
            },
            "metrics": {
                "classification": "GENERATED_LOCAL_OUTPUT",
                "identity_scope": "CANONICAL_METRICS_OBJECT_ONLY",
                "canonical_metrics_sha256": sha256_bytes(canonical_json_bytes(metrics)),
                "metric_table_exact": frozen_metadata["metrics"]["metric_table"] == metrics["metric_table"],
                "full_metrics_exact": True,
            },
            "witness_DA-EVAL-V02-00001": {
                "top1_code": witness["top1_code"],
                "top1_score": witness["top1_score"],
                "retrieved_count": int(witness["retrieved_count"]),
            },
        }
        replay = {"logical_identity": logical, "reproduction": reproduction}
    require(temporary_path is not None and not temporary_path.exists(), "Temporary replay directory was not removed")
    return replay


def _contracts(replay: Mapping[str, Any], binding_revision: str) -> dict[str, dict[str, Any]]:
    bindings = canonical_bindings(binding_revision)
    by_path = {item["path"]: item for item in bindings}
    pyc_path = "src/__pycache__/bm25_index.cpython-311.pyc"
    pyc_bytes = bytes(_git("show", f"{BYTECODE_INTRO_COMMIT}:{pyc_path}", binary=True))
    provenance = {
        "artifact_id": "ev03_historical_builder_provenance_v0.2",
        "policy": "RECOVERED_HISTORICAL_EV03_SEMANTICS_WITH_EXACT_CONTROL_GATE",
        "canonical_identity_policy": "GIT_BLOB_SHA1_AND_SHA256_OVER_GIT_CAT_FILE_BLOB",
        "historical_commits": {
            "bytecode_first_observed": BYTECODE_INTRO_COMMIT,
            "index_and_metadata_first_observed": INDEX_INTRO_COMMIT,
            "source_and_notebook_first_observed": SOURCE_INTRO_COMMIT,
            "historical_ev03_run": HISTORICAL_RUN_COMMIT,
        },
        "index_intro_presence": {
            "versioned_bytecode": _path_at_revision(pyc_path, INDEX_INTRO_COMMIT),
            "historical_index": _path_at_revision(HISTORICAL_INDEX.as_posix(), INDEX_INTRO_COMMIT),
            "historical_metadata": _path_at_revision(HISTORICAL_METADATA.as_posix(), INDEX_INTRO_COMMIT),
            "source_py": _path_at_revision("src/bm25_index.py", INDEX_INTRO_COMMIT),
            "notebook": _path_at_revision("notebooks/04_BM25_Indexacion_NANDINA.ipynb", INDEX_INTRO_COMMIT),
        },
        "versioned_bytecode": {
            "path": pyc_path,
            "git_blob_sha1": _git_blob(pyc_path, BYTECODE_INTRO_COMMIT),
            "canonical_git_blob_sha256": sha256_bytes(pyc_bytes),
            "classification": "DERIVED_BYTECODE_EVIDENCE_NOT_AUTHENTIC_SOURCE_PY",
        },
        "frozen_inputs": {
            "corpus": by_path[CORPUS.as_posix()],
            "eval": by_path[EVALSET.as_posix()],
            "config": by_path[CONFIG.as_posix()],
            "historical_index": by_path[HISTORICAL_INDEX.as_posix()],
            "historical_metadata": by_path[HISTORICAL_METADATA.as_posix()],
        },
        "config_worktree_observation": {
            "worktree_sha256": "ee23e112fb553a355d9787403eb7fa8688295737f76c7acaff052cc9d0ecb2d3",
            "classification": "WORKTREE_SHA256_DIAGNOSTIC_ONLY_WINDOWS_CRLF",
            "authoritative": False,
        },
        "current_divergent_source": {**by_path["src/bm25_index.py"], "keeps_single_character_tokens": True},
        "recovered_rule": TOKEN_POLICY,
        "AUTHENTIC_HISTORICAL_SOURCE_PY": "NOT_VERSIONED_AT_INDEX_CREATION",
        "conclusion": "HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED",
    }
    authorization = {
        "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "corrective_retrieval_executed": False,
        "corrective_metrics_computed": False,
        "runtime_authorization_record_present": False,
    }
    scientific_state = {
        "0B05C_METRIC_IMPACT": "NOT_DETERMINED",
        "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED",
        "0B05C_CLOSURE": "NOT_AUTHORIZED",
    }
    spec = {
        "specification_id": "ev03_corrective_execution_spec_v0.2",
        "methodology": "RECOVERED_HISTORICAL_EV03_SEMANTICS_WITH_EXACT_CONTROL_GATE",
        "gate_scope": "EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY",
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "authorization": authorization,
        "dependency_bindings": bindings,
        "recovered_builder": {
            "binding": by_path["src/experiments/build_bm25_ev03_historical_recovered_v02.py"],
            "token_policy": TOKEN_POLICY,
            "scope": "EV03_ONLY",
            "k1": 1.5,
            "b": 0.75,
        },
        "precondition": {
            "LOGICAL_INDEX_IDENTITY": "EXACT",
            "EV03_DECISION885_CONTROL_REPRODUCTION": "PASS_EXACT",
        },
        "future_roots": list(FUTURE_EXECUTION_ROOTS),
        "v01_evidence_roots_excluded": list(V01_EVIDENCE_ROOTS),
        "corrected_arm_executed": False,
        "scientific_state": scientific_state,
    }
    gate = {
        "gate_id": "0b05c_corrective_numerical_gate_v0.2",
        "base_commit": BASE_COMMIT,
        "gate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "gate_scope": "EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY",
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "authorization": authorization,
        "scientific_state": scientific_state,
        "dependency_bindings": bindings,
        "ev03_recovery": {
            "logical_index_identity": "EXACT",
            "control_reproduction": "PASS_EXACT",
            "token_policy": TOKEN_POLICY,
        },
        "ev04_policy": "UNCHANGED_AND_NOT_ASSUMED_TO_USE_EV03_RECOVERED_TOKEN_POLICY",
        "future_roots": list(FUTURE_EXECUTION_ROOTS),
    }
    manifest = {
        "artifact_id": "0b05c_ev03_historical_builder_recovery_manifest_v0.2",
        "base_commit": BASE_COMMIT,
        "gate_scope": "EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY",
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "versioned_contract_paths": [path.as_posix() for path in AUDIT_FILES.values()],
        "committed_replay_mode": "COMMITTED_REPLAY_READONLY",
        "temporary_generated_paths": [
            "TEMPORARY_REPLAY/index/index.pkl",
            "TEMPORARY_REPLAY/index/index_metadata.json",
            "TEMPORARY_REPLAY/evaluation/normative_flat_results.csv",
            "TEMPORARY_REPLAY/evaluation/normative_flat_case_summary.csv",
            "TEMPORARY_REPLAY/evaluation/normative_flat_metrics.json",
        ],
        "repository_generated_paths": [],
        "future_roots_absent": list(FUTURE_EXECUTION_ROOTS),
        "v01_evidence_roots_not_outputs_of_v02": list(V01_EVIDENCE_ROOTS),
    }
    generated = [
        {
            "path": "TEMPORARY_REPLAY/index/index.pkl",
            "classification": "GENERATED_LOCAL_OUTPUT",
            "identity_scope": "LOGICAL_PROJECTION",
            "logical_projection_sha256": sha256_bytes(canonical_json_bytes(replay["logical_identity"]["recovered_index"])),
        },
        replay["reproduction"]["ranking"],
        replay["reproduction"]["case_summary"],
        replay["reproduction"]["metrics"],
    ]
    ledger = {
        "artifact_id": "0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2",
        "canonical_hash_algorithm": "SHA-256_OVER_GIT_CAT_FILE_BLOB",
        "authoritative_categories": ["VERSIONED_GIT_BLOB", "FROZEN_BINARY_GIT_BLOB"],
        "non_authoritative_category": "GENERATED_LOCAL_OUTPUT",
        "files": [*bindings, *generated],
        "mismatch_count": 0,
        "self_excluded": AUDIT_FILES["ledger"].as_posix(),
    }
    return {
        "provenance": provenance,
        "logical_identity": dict(replay["logical_identity"]),
        "control_reproduction": dict(replay["reproduction"]),
        "ev03_spec": spec,
        "unified_gate": gate,
        "manifest": manifest,
        "ledger": ledger,
    }


def prepare_artifacts(root: Path = ROOT, binding_revision: str = "INDEX") -> dict[str, Any]:
    require(root.resolve() == ROOT.resolve(), "Preparation must run from the repository checkout")
    require(_base_is_ancestor(root), "Frozen base commit is not an ancestor of HEAD")
    require(_future_roots_absent(root), "A future numerical root already exists")
    replay = _run_control_replay(root)
    contracts = _contracts(replay, binding_revision)
    for key, path in AUDIT_FILES.items():
        _write_json(root / path, contracts[key])
    return {
        "status": "PASS",
        "mode": "PREPARE_VERSIONED_RECOVERY_ARTIFACTS",
        "LOGICAL_INDEX_IDENTITY": replay["logical_identity"]["LOGICAL_INDEX_IDENTITY"],
        "EV03_DECISION885_CONTROL_REPRODUCTION": replay["reproduction"]["EV03_DECISION885_CONTROL_REPRODUCTION"],
        "artifact_count": len(AUDIT_FILES),
        "future_numerical_roots_present": False,
    }


def verify_committed(root: Path = ROOT) -> dict[str, Any]:
    require(root.resolve() == ROOT.resolve(), "Verification must run from the repository checkout")
    base_commit_ancestor = _base_is_ancestor(root)
    tracked_worktree_clean = _tracked_clean(root)
    require(base_commit_ancestor, "Frozen base commit is not an ancestor of HEAD")
    require(tracked_worktree_clean, "Committed replay requires a clean tracked worktree")
    require(_future_roots_absent(root), "A future numerical root already exists")
    for path in AUDIT_FILES.values():
        require((root / path).is_file(), f"Committed recovery artifact is missing: {path.as_posix()}")

    status_before = str(_git("status", "--porcelain", "--untracked-files=all", root=root))
    audit_hashes_before = {key: sha256_file(root / path) for key, path in AUDIT_FILES.items()}
    committed = {key: _read_json(root / path) for key, path in AUDIT_FILES.items()}
    binding_check = verify_canonical_bindings(committed["ev03_spec"]["dependency_bindings"])
    require(
        next(item for item in committed["ev03_spec"]["dependency_bindings"] if item["path"] == CONFIG.as_posix())[
            "canonical_git_blob_sha256"
        ]
        == "107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d",
        "Canonical config Git blob identity drift",
    )
    replay = _run_control_replay(root)
    expected = _contracts(replay, "HEAD")
    mismatched_artifacts = [key for key in AUDIT_FILES if committed[key] != expected[key]]
    require(not mismatched_artifacts, f"Committed recovery artifacts do not match replay: {mismatched_artifacts}")

    status_after = str(_git("status", "--porcelain", "--untracked-files=all", root=root))
    audit_hashes_after = {key: sha256_file(root / path) for key, path in AUDIT_FILES.items()}
    require(status_after == status_before, "Committed replay changed repository status")
    require(audit_hashes_after == audit_hashes_before, "Committed replay modified versioned audit artifacts")
    return {
        "status": "PASS",
        "mode": "COMMITTED_REPLAY_READONLY",
        "base_commit_ancestor": base_commit_ancestor,
        "tracked_worktree_clean": tracked_worktree_clean,
        "canonical_dependency_bindings": binding_check,
        "LOGICAL_INDEX_IDENTITY": replay["logical_identity"]["LOGICAL_INDEX_IDENTITY"],
        "EV03_DECISION885_CONTROL_REPRODUCTION": replay["reproduction"]["EV03_DECISION885_CONTROL_REPRODUCTION"],
        "ranking_bytes_exact": replay["reproduction"]["ranking"]["bytes_exact"],
        "case_summary_bytes_exact": replay["reproduction"]["case_summary"]["bytes_exact"],
        "full_metrics_exact": replay["reproduction"]["metrics"]["full_metrics_exact"],
        "repo_files_created": 0,
        "repo_files_modified": 0,
        "repo_files_deleted": 0,
        "audit_artifacts_modified": False,
        "future_numerical_roots_present": False,
        "ledger_mismatch_count": committed["ledger"]["mismatch_count"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify recovered historical EV03 control semantics v0.2")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--prepare-artifacts", action="store_true")
    modes.add_argument("--verify-committed", action="store_true")
    args = parser.parse_args(argv)
    result = prepare_artifacts() if args.prepare_artifacts else verify_committed()
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
