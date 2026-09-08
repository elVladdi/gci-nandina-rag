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
import subprocess
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from ..bm25_index import sha256_file
from .build_bm25_ev03_historical_recovered_v02 import TOKEN_POLICY, build
from .evaluate_normative_bm25_corrective_0b05c_v01 import (
    EV03_CANDIDATE_FIELDS,
    EV03_CASE_FIELDS,
    compare_control_reproduction,
    evaluate_arm,
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


def _git(*args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True)
    return result.stdout if binary else result.stdout.decode("utf-8").strip()


def _git_blob(path: str, revision: str = "HEAD") -> str:
    return str(_git("rev-parse", f"{revision}:{path}"))


def _path_at_revision(path: str, revision: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{revision}:{path}"], cwd=ROOT, capture_output=True).returncode == 0


def _row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def _identity(path: Path) -> dict[str, Any]:
    return {"path": path.as_posix(), "size_bytes": (ROOT / path).stat().st_size, "sha256": sha256_file(ROOT / path)}


def verify_control(root: Path = ROOT) -> dict[str, Any]:
    require(root.resolve() == ROOT.resolve(), "Verification must run from the repository checkout")
    require(str(_git("rev-parse", "HEAD")) == BASE_COMMIT, "Candidate must begin at the frozen base commit")
    for relative in FUTURE_EXECUTION_ROOTS:
        require(not (root / relative).exists(), f"Future numerical root already exists: {relative}")
    for relative in (PREEXEC_INDEX_ROOT, PREEXEC_OUTPUT_ROOT, AUDIT_ROOT):
        require(not (root / relative).exists(), f"Preexecution verification refuses overwrite: {relative.as_posix()}")

    corpus_sha = sha256_file(root / CORPUS)
    eval_sha = sha256_file(root / EVALSET)
    config_sha = sha256_file(root / CONFIG)
    historical_index_sha = sha256_file(root / HISTORICAL_INDEX)
    require(corpus_sha == "83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0", "Corpus identity drift")
    require(eval_sha == "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941", "EVAL identity drift")
    require(historical_index_sha == "fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b", "Historical index identity drift")

    build(CORPUS, PREEXEC_INDEX, PREEXEC_INDEX_METADATA, root=root)
    with (root / HISTORICAL_INDEX).open("rb") as handle:
        historical_index = pickle.load(handle)
    with (root / PREEXEC_INDEX).open("rb") as handle:
        recovered_index = pickle.load(handle)
    logical = logical_identity(historical_index, recovered_index)
    require(logical["LOGICAL_INDEX_IDENTITY"] == "EXACT", "Recovered EV03 index is not logically exact")

    evaluation = evaluate_arm(
        "EV03",
        root / CORPUS,
        root / PREEXEC_INDEX,
        root / PREEXEC_INDEX_METADATA,
        root / PREEXEC_OUTPUT_ROOT,
        evalset=root / EVALSET,
        config_path=root / CONFIG,
        root=root,
    )
    frozen_metadata = json.loads((root / FROZEN_OUTPUT_ROOT / "run_metadata.json").read_text(encoding="utf-8"))
    comparison = compare_control_reproduction(
        root / FROZEN_OUTPUT_ROOT / "normative_results.csv",
        root / PREEXEC_OUTPUT_ROOT / "normative_flat_results.csv",
        root / FROZEN_OUTPUT_ROOT / "normative_case_summary.csv",
        root / PREEXEC_OUTPUT_ROOT / "normative_flat_case_summary.csv",
        frozen_metadata["metrics"],
        evaluation["metrics"],
        expected_candidate_schema=EV03_CANDIDATE_FIELDS,
        expected_case_schema=EV03_CASE_FIELDS,
    )

    ranking = PREEXEC_OUTPUT_ROOT / "normative_flat_results.csv"
    case_summary = PREEXEC_OUTPUT_ROOT / "normative_flat_case_summary.csv"
    metrics_file = PREEXEC_OUTPUT_ROOT / "normative_flat_metrics.json"
    frozen_ranking = FROZEN_OUTPUT_ROOT / "normative_results.csv"
    frozen_summary = FROZEN_OUTPUT_ROOT / "normative_case_summary.csv"
    ranking_bytes_exact = (root / ranking).read_bytes() == (root / frozen_ranking).read_bytes()
    summary_bytes_exact = (root / case_summary).read_bytes() == (root / frozen_summary).read_bytes()
    require(ranking_bytes_exact and summary_bytes_exact, "Logical rows match but frozen CSV bytes differ")

    with (root / case_summary).open("r", encoding="utf-8-sig", newline="") as handle:
        witness = next(row for row in csv.DictReader(handle) if row["case_id"] == "DA-EVAL-V02-00001")
    reproduction = {
        "artifact_id": "ev03_decision885_control_reproduction_v0.2",
        "status": "PASS_EXACT",
        "EV03_DECISION885_CONTROL_REPRODUCTION": "PASS_EXACT",
        "comparison": comparison,
        "ranking": {**_identity(ranking), "rows": _row_count(root / ranking), "frozen_sha256": sha256_file(root / frozen_ranking), "bytes_exact": ranking_bytes_exact},
        "case_summary": {**_identity(case_summary), "rows": _row_count(root / case_summary), "frozen_sha256": sha256_file(root / frozen_summary), "bytes_exact": summary_bytes_exact},
        "metrics": {**_identity(metrics_file), "metric_table_exact": frozen_metadata["metrics"]["metric_table"] == evaluation["metrics"]["metric_table"], "full_metrics_exact": frozen_metadata["metrics"] == evaluation["metrics"]},
        "witness_DA-EVAL-V02-00001": {"top1_code": witness["top1_code"], "top1_score": witness["top1_score"], "retrieved_count": int(witness["retrieved_count"])},
    }
    require(reproduction["metrics"]["full_metrics_exact"], "Full frozen EV03 metrics do not match")

    pyc_path = "src/__pycache__/bm25_index.cpython-311.pyc"
    pyc_bytes = _git("show", f"{BYTECODE_INTRO_COMMIT}:{pyc_path}", binary=True)
    provenance = {
        "artifact_id": "ev03_historical_builder_provenance_v0.2",
        "policy": "RECOVERED_HISTORICAL_EV03_SEMANTICS_WITH_EXACT_CONTROL_GATE",
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
        "versioned_bytecode": {"path": pyc_path, "git_blob_sha1": _git_blob(pyc_path, BYTECODE_INTRO_COMMIT), "sha256": sha256_bytes(bytes(pyc_bytes)), "classification": "DERIVED_BYTECODE_EVIDENCE_NOT_AUTHENTIC_SOURCE_PY"},
        "historical_index": {**_identity(HISTORICAL_INDEX), "git_blob_sha1": _git_blob(HISTORICAL_INDEX.as_posix(), INDEX_INTRO_COMMIT)},
        "historical_metadata": {**_identity(HISTORICAL_METADATA), "git_blob_sha1": _git_blob(HISTORICAL_METADATA.as_posix(), INDEX_INTRO_COMMIT)},
        "frozen_inputs": {"corpus_sha256": corpus_sha, "eval_sha256": eval_sha, "config_sha256": config_sha},
        "current_divergent_source": {"path": "src/bm25_index.py", "git_blob_sha1": _git_blob("src/bm25_index.py"), "keeps_single_character_tokens": True},
        "recovered_rule": TOKEN_POLICY,
        "AUTHENTIC_HISTORICAL_SOURCE_PY": "NOT_VERSIONED_AT_INDEX_CREATION",
        "conclusion": "HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED",
    }

    spec = {
        "specification_id": "ev03_corrective_execution_spec_v0.2",
        "methodology": "RECOVERED_HISTORICAL_EV03_SEMANTICS_WITH_EXACT_CONTROL_GATE",
        "authorization": {"EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED", "corrective_retrieval_executed": False, "corrective_metrics_computed": False},
        "historical_control": {"index": _identity(HISTORICAL_INDEX), "corpus": _identity(CORPUS), "eval": _identity(EVALSET)},
        "recovered_builder": {"path": "src/experiments/build_bm25_ev03_historical_recovered_v02.py", "token_policy": TOKEN_POLICY, "scope": "EV03_ONLY", "k1": 1.5, "b": 0.75},
        "precondition": {"LOGICAL_INDEX_IDENTITY": "EXACT", "EV03_DECISION885_CONTROL_REPRODUCTION": "PASS_EXACT"},
        "future_roots": list(FUTURE_EXECUTION_ROOTS),
        "v01_evidence_roots_excluded": list(V01_EVIDENCE_ROOTS),
        "corrected_arm_executed": False,
    }
    gate = {
        "gate_id": "0b05c_corrective_numerical_gate_v0.2",
        "base_commit": BASE_COMMIT,
        "gate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "authorization": {
            "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
            "corrective_retrieval_executed": False,
            "corrective_metrics_computed": False,
            "runtime_authorization_record_present": False,
        },
        "scientific_state": {"0B05C_METRIC_IMPACT": "NOT_DETERMINED", "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED", "0B05C_CLOSURE": "NOT_AUTHORIZED"},
        "ev03_recovery": {"logical_index_identity": "EXACT", "control_reproduction": "PASS_EXACT", "token_policy": TOKEN_POLICY},
        "ev04_policy": "UNCHANGED_AND_NOT_ASSUMED_TO_USE_EV03_RECOVERED_TOKEN_POLICY",
        "future_roots": list(FUTURE_EXECUTION_ROOTS),
    }

    audit_paths = {
        "provenance": AUDIT_ROOT / "ev03_historical_builder_provenance_v0.2.json",
        "logical_identity": AUDIT_ROOT / "ev03_logical_index_identity_v0.2.json",
        "control_reproduction": AUDIT_ROOT / "ev03_decision885_control_reproduction_v0.2.json",
        "ev03_spec": AUDIT_ROOT / "ev03_corrective_execution_spec_v0.2.json",
        "unified_gate": AUDIT_ROOT / "0b05c_corrective_numerical_gate_v0.2.json",
        "manifest": AUDIT_ROOT / "0b05c_ev03_historical_builder_recovery_manifest_v0.2.json",
        "ledger": AUDIT_ROOT / "0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json",
    }
    _write_json(root / audit_paths["provenance"], provenance)
    _write_json(root / audit_paths["logical_identity"], logical)
    _write_json(root / audit_paths["control_reproduction"], reproduction)
    _write_json(root / audit_paths["ev03_spec"], spec)
    _write_json(root / audit_paths["unified_gate"], gate)
    manifest = {
        "artifact_id": "0b05c_ev03_historical_builder_recovery_manifest_v0.2",
        "base_commit": BASE_COMMIT,
        "versioned_contract_paths": [path.as_posix() for path in audit_paths.values()],
        "preexecution_generated_paths": [PREEXEC_INDEX.as_posix(), PREEXEC_INDEX_METADATA.as_posix(), ranking.as_posix(), case_summary.as_posix(), metrics_file.as_posix()],
        "future_roots_absent": list(FUTURE_EXECUTION_ROOTS),
        "v01_evidence_roots_not_outputs_of_v02": list(V01_EVIDENCE_ROOTS),
    }
    _write_json(root / audit_paths["manifest"], manifest)

    ledger_inputs = [
        Path("src/experiments/build_bm25_ev03_historical_recovered_v02.py"),
        Path("src/experiments/verify_ev03_historical_builder_recovery_v02.py"),
        Path("tests/test_0b05c_ev03_historical_builder_recovery_v02.py"),
        Path("docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md"),
        CORPUS, EVALSET, CONFIG, HISTORICAL_INDEX, HISTORICAL_METADATA,
        PREEXEC_INDEX, PREEXEC_INDEX_METADATA, ranking, case_summary, metrics_file,
        *[path for key, path in audit_paths.items() if key != "ledger"],
    ]
    ledger = {
        "artifact_id": "0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2",
        "hash_algorithm": "SHA-256",
        "self_excluded": audit_paths["ledger"].as_posix(),
        "files": [_identity(path) for path in ledger_inputs],
    }
    _write_json(root / audit_paths["ledger"], ledger)
    return {"logical_identity": logical, "reproduction": reproduction, "gate": gate, "audit_paths": {key: path.as_posix() for key, path in audit_paths.items()}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify recovered historical EV03 control semantics v0.2")
    parser.add_argument("--verify-control", action="store_true", required=True)
    parser.parse_args(argv)
    print(json.dumps(verify_control(), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
