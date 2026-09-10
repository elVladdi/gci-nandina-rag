"""Build and validate the fail-closed 0B-05C v0.5 preauthorization gate."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable, Mapping


ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "c873ff1bd10f4e86c6f80f7f34a4dad1126965f1"
AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.5")
READINESS_ROOT = Path("outputs/audits/0b05c_v05_preauthorization_readiness")
AUTHORIZATION_RECORD = AUDIT_ROOT / "0b05c_numerical_authorization_record_v0.5.json"
ARTIFACT_NAMES = (
    "ev03_numerical_execution_spec_v0.5.json",
    "ev04_numerical_execution_spec_v0.5.json",
    "d1a_numerical_execution_spec_v0.5.json",
    "0b05c_corrective_numerical_execution_gate_v0.5.json",
    "0b05c_corrective_numerical_gate_manifest_v0.5.json",
    "0b05c_corrective_numerical_gate_hash_ledger_v0.5.json",
)
PIPELINE_STEPS = (
    "01_unified_preflight", "02_EV03_Decision885_control_reproduction",
    "03_EV03_control_reproduction_verification", "04_EV03_corrected_corpus_materialization",
    "05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS", "06_EV03_corrected_evaluation",
    "07_EV04_Decision885_control_reproduction_ENRICHED_MRR", "08_EV04_control_reproduction_verification_PASS_EXACT",
    "09_EV04_corrected_corpus_materialization", "10_EV04_corrected_index_build",
    "11_EV04_corrected_evaluation_ENRICHED_MRR", "12_D1a_corrected_execution_under_future_v05_authorization",
    "13_integrity_validation", "14_case_level_comparisons", "15_aggregate_comparisons",
    "16_unified_sensitivity_summary", "17_execution_manifest", "18_exact_hash_ledger",
    "19_final_completion_state",
)
FUTURE_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.5",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.5",
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.5.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.5",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5",
    "data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.5",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.5",
    "data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.5.jsonl",
    "data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.5",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5",
    "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.5.jsonl",
    "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.5",
    "outputs/evaluation/d1a_corrective_0b05c_v0.5",
    "outputs/audits/d1a_corrective_0b05c_runtime_v0.5",
    "outputs/evaluation/0b05c_corrective_numerical_v0.5",
    "outputs/audits/0b05c_corrective_numerical_runtime_v0.5",
)
V04_ROOTS = tuple(path.replace("v0.5", "v0.4") for path in FUTURE_ROOTS)
AUTHORIZATION = {
    "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "authorization_record_present": False,
    "runtime_authorization_record_present": False,
    "corrective_retrieval_executed": False,
    "corrective_metrics_computed": False,
}
TESTED_ENVIRONMENT = {
    "classification": "TESTED_EXECUTION_ENVIRONMENT / NOT_HISTORICAL_PROVENANCE",
    "python_version": "3.10.11",
    "executable_sha256": "b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961",
    "required_packages": {
        "numpy": "2.2.6", "sentence_transformers": "5.5.1",
        "torch": "2.12.0+cpu", "tqdm": "4.68.2",
    },
}
MODEL_METADATA = Path("data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json")
OBSERVED_FOOTPRINT_BYTES = 733_372_007
DISK_MARGIN_BYTES = 2 * OBSERVED_FOOTPRINT_BYTES
MEMORY_MARGIN_BYTES = 2 * 477_616_987


class ContractViolation(RuntimeError):
    """Raised before numerical side effects when a v0.5 contract fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(payload, dict), f"JSON object required: {path.as_posix()}")
    return payload


def canonical_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def _replace_runtime_version(value: Any) -> Any:
    if isinstance(value, str):
        for old, new in zip(V04_ROOTS, FUTURE_ROOTS, strict=True):
            value = value.replace(old, new)
        return (value
                .replace("evaluate_normative_bm25_corrective_0b05c_v04", "evaluate_normative_bm25_corrective_0b05c_v05")
                .replace("run_d1a_corrective_0b05c_v04", "run_d1a_corrective_0b05c_v05")
                .replace("run_0b05c_corrective_numerical_v04", "run_0b05c_corrective_numerical_v05"))
    if isinstance(value, list):
        return [_replace_runtime_version(item) for item in value]
    if isinstance(value, dict):
        return {key: _replace_runtime_version(item) for key, item in value.items()}
    return value


def _spec(root: Path, name: str, arm: str) -> dict[str, Any]:
    old = _json(root / "outputs/audits/0b05c_corrective_numerical_gate_v0.4" / name.replace("v0.5", "v0.4"))
    spec = _replace_runtime_version(copy.deepcopy(old))
    spec["specification_status"] = "PREAUTHORIZATION_SPEC_DEFINED / PENDING_EXTERNAL_AUDIT"
    spec["attempt05"] = "FAIL_CLOSED / AUTHORIZATION_CONSUMED"
    spec["attempt06"] = "NOT_AUTHORIZED / NOT_EXECUTED"
    key = f"{arm}_NUMERICAL_EXECUTION" if arm != "d1a" else "D1A_NUMERICAL_EXECUTION"
    spec["authorization"][key] = "NOT_AUTHORIZED"
    spec["v04_partial_roots_policy"] = "NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05"
    if arm == "EV03":
        spec["prospective_execution"]["case_level_comparison_contract"]["rank_convention"] = "0=NOT_FOUND/EMPTY"
        spec["prospective_execution"]["case_level_comparison_contract"]["empty_ranking_contract"] = "VALID_ONLY_WHEN_SUMMARY_RETRIEVED_COUNT_AND_RANK_REF_ARE_ZERO_AND_TOP1_FIELDS_EMPTY"
    return spec


def _runtime_paths_from_v04(root: Path) -> tuple[str, ...]:
    gate = _json(root / "outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json")
    return tuple(sorted(path.replace("v0.4", "v0.5") for path in gate["runtime_hash_ledger_contract"]["expected_paths"]))


def producer_runtime_paths(bundle: Mapping[str, Any]) -> tuple[str, ...]:
    """Derive producer outputs independently from the frozen operation groups."""

    gate_paths = set(bundle["gate"]["runtime_hash_ledger_contract"]["expected_paths"])
    groups = {
        "preflight": {p for p in gate_paths if p.endswith("runtime_authorization_record_v0.5.json")},
        "ev03": {p for p in gate_paths if "ev03" in p or "normative_flat" in p},
        "ev04": {p for p in gate_paths if "ev04" in p or "normative_hierarchical" in p},
        "d1a": {p for p in gate_paths if "d1a" in p or "text2trade_mnrl_nandina8_d1a" in p},
        "unified": {p for p in gate_paths if "0b05c_corrective_numerical_v0.5" in p or "0b05c_corrective_numerical_runtime_v0.5" in p},
    }
    produced = set().union(*groups.values())
    require(produced == gate_paths, "v0.5 producer derivation does not cover the expected runtime set")
    return tuple(sorted(produced))


def _source_binding(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    require(path.is_file(), f"Candidate source is missing: {relative}")
    return {"path": relative, "classification": "CANDIDATE_WORKTREE_BYTES", "sha256": _sha256(path), "size_bytes": path.stat().st_size}


def build_bundle(root: Path = ROOT) -> dict[str, Any]:
    ev03 = _spec(root, ARTIFACT_NAMES[0], "EV03")
    ev04 = _spec(root, ARTIFACT_NAMES[1], "EV04")
    d1a = _spec(root, ARTIFACT_NAMES[2], "d1a")
    expected = _runtime_paths_from_v04(root)
    sources = [
        "src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py",
        "src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py",
        "src/experiments/run_d1a_corrective_0b05c_v05.py",
        "src/experiments/run_0b05c_corrective_numerical_v05.py",
    ]
    gate = {
        "gate_id": "0b05c_corrective_numerical_execution_gate_v0.5",
        "gate_version": "v0.5",
        "gate_status": "CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED",
        "authorization_readiness": "NOT_AUTHORIZED",
        "authorization": dict(AUTHORIZATION),
        "attempt05": "FAIL_CLOSED / AUTHORIZATION_CONSUMED",
        "attempt06": "NOT_AUTHORIZED / NOT_EXECUTED",
        "base_commit": BASE_COMMIT,
        "pipeline_steps": list(PIPELINE_STEPS),
        "future_roots": list(FUTURE_ROOTS),
        "v04_partial_roots": {"policy": "NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05", "paths": list(V04_ROOTS)},
        "methodological_invariants": {
            "mrr_at_100": "EXACT_RATIONAL_SUM_THEN_ONE_FLOAT_CONVERSION",
            "mrr_at_200": "LEGACY_SUM_FLOAT_RECIPROCAL_RANK_IN_FROZEN_ROW_ORDER",
            "mrr_101_200_contribution": "EXACT_RATIONAL_DIFFERENCE",
            "ev04_aggregate_rows": 28,
            "ev03_semantics": "RECOVERED_HISTORICAL_DROP_SINGLE_CHARACTER_TOKENS",
            "decision906_changed_codes": ["87044110", "87045110"],
            "d1a_retraining": "FORBIDDEN",
        },
        "environment_contract": dict(TESTED_ENVIRONMENT),
        "runtime_hash_ledger_contract": {
            "expected_paths": list(expected),
            "excluded_self_path": "outputs/audits/0b05c_corrective_numerical_runtime_v0.5/exact_hash_ledger_v0.5.json",
            "entry_fields": ["path", "sha256", "size_bytes"],
            "missing_or_unexpected_policy": "FAIL_CLOSED",
        },
        "candidate_source_bindings": [_source_binding(root, path) for path in sources],
        "scientific_state": {"0B05C_METRIC_IMPACT": "NOT_DETERMINED", "0B05C_CLOSURE": "NOT_AUTHORIZED"},
    }
    bundle: dict[str, Any] = {"ev03": ev03, "ev04": ev04, "d1a": d1a, "gate": gate}
    producer = producer_runtime_paths(bundle)
    manifest = {
        "artifact_id": "0b05c_corrective_numerical_gate_manifest_v0.5",
        "gate_status": gate["gate_status"], "authorization_readiness": "NOT_AUTHORIZED",
        "attempt05": gate["attempt05"], "attempt06": gate["attempt06"],
        "pipeline_steps": list(PIPELINE_STEPS), "future_roots": list(FUTURE_ROOTS),
        "v04_partial_roots_policy": "NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05",
        "candidate_source_bindings": gate["candidate_source_bindings"],
        "authorization_record_v05_present": False,
    }
    ledger = {
        "artifact_id": "0b05c_corrective_numerical_gate_hash_ledger_v0.5",
        "classification": "PREAUTHORIZATION_CONTRACT / FUTURE_HASHES_NOT_INVENTED",
        "expected_set_count": len(expected), "producer_set_count": len(producer),
        "expected_set": list(expected), "producer_set": list(producer),
        "set_identity": expected == producer, "excluded_self_path": gate["runtime_hash_ledger_contract"]["excluded_self_path"],
        "future_hashes_invented": False,
    }
    bundle.update({"manifest": manifest, "ledger": ledger})
    return bundle


def validate_manifest_payload(payload: Mapping[str, Any]) -> None:
    required = {"artifact_id", "status", "authorization_provenance", "pipeline_steps", "future_roots", "results"}
    require(isinstance(payload, Mapping) and set(payload) == required, "Execution manifest schema is not exact")
    require(payload.get("status") == "PASS", "Execution manifest status is not PASS")
    require(payload.get("pipeline_steps") == list(PIPELINE_STEPS), "Execution manifest 19-step order changed")
    provenance = payload.get("authorization_provenance")
    require(isinstance(provenance, Mapping) and provenance.get("status") == "PASS", "Execution manifest authorization provenance is incomplete")
    roots = payload.get("future_roots")
    require(roots == list(FUTURE_ROOTS), "Execution manifest roots changed")
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True, allow_nan=False)
    require(not any(root in serialized for root in V04_ROOTS), "Execution manifest references a v0.4 partial root")


def write_manifest_new(path: Path, payload: Mapping[str, Any]) -> None:
    require(not path.exists(), "Execution manifest refuses overwrite")
    validate_manifest_payload(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(payload))
    require(_json(path) == dict(payload), "Execution manifest round-trip changed content")


def validate_ledger_sets(expected: set[str], produced: set[str]) -> None:
    require(expected == produced, f"Runtime ledger set mismatch: missing={sorted(expected-produced)}, unexpected={sorted(produced-expected)}")
    require(len(produced) == len(set(produced)), "Runtime producer path collision")
    require(not any(path.endswith("execution_failed.json") for path in expected), "Failure record entered success ledger")


def validate_runtime_ledger(
    root: Path, expected: set[str], produced: set[str], *, snapshot: Mapping[str, str] | None = None,
) -> list[dict[str, Any]]:
    validate_ledger_sets(expected, produced)
    entries = []
    for relative in sorted(produced):
        path = root / relative
        require(path.is_file() and path.stat().st_size > 0, f"Runtime output missing or empty: {relative}")
        digest = _sha256(path)
        if snapshot is not None and relative in snapshot:
            require(snapshot[relative] == digest, f"Runtime output changed after integrity snapshot: {relative}")
        entries.append({"path": relative, "sha256": digest, "size_bytes": path.stat().st_size})
    return entries


def _available_memory() -> tuple[int, int]:
    if os.name == "nt":
        import ctypes
        class MemoryStatus(ctypes.Structure):
            _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong), ("total", ctypes.c_ulonglong),
                        ("available", ctypes.c_ulonglong), ("total_page", ctypes.c_ulonglong), ("available_page", ctypes.c_ulonglong),
                        ("total_virtual", ctypes.c_ulonglong), ("available_virtual", ctypes.c_ulonglong), ("available_extended", ctypes.c_ulonglong)]
        status = MemoryStatus()
        status.length = ctypes.sizeof(status)
        require(bool(ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))), "Unable to query host memory")
        return int(status.total), int(status.available)
    page = os.sysconf("SC_PAGE_SIZE")
    return int(page * os.sysconf("SC_PHYS_PAGES")), int(page * os.sysconf("SC_AVPHYS_PAGES"))


def validate_complete_model_directory(root: Path) -> dict[str, Any]:
    metadata = _json(root / MODEL_METADATA)
    governed = metadata["inputs"]["model"]["files"]
    require(isinstance(governed, list) and len(governed) == 9, "Frozen model manifest must govern exactly nine files")
    expected_paths = {item["path"] for item in governed}
    model_root = root / metadata["inputs"]["model"]["path"]
    require(model_root.is_dir(), "Complete frozen model directory is absent")
    observed = {path.relative_to(root).as_posix() for path in model_root.rglob("*") if path.is_file()}
    require(observed == expected_paths, f"Frozen model directory file set mismatch: missing={sorted(expected_paths-observed)}, extra={sorted(observed-expected_paths)}")
    for item in governed:
        path = root / item["path"]
        require(path.stat().st_size == item["size_bytes"], f"Frozen model size mismatch: {item['path']}")
        require(_sha256(path) == item["sha256"], f"Frozen model SHA mismatch: {item['path']}")
    return {"status": "PASS_EXACT", "governed_file_count": 9, "model_directory": metadata["inputs"]["model"]["path"]}


def _interpreter_probe(root: Path, interpreter: Path) -> dict[str, Any]:
    model = _json(root / MODEL_METADATA)["inputs"]["model"]["path"]
    script = r'''
import importlib, json, os, sys
import numpy as np
from sentence_transformers import SentenceTransformer
packages = {}
for name in ("numpy","sentence_transformers","torch","tqdm","transformers","tokenizers","safetensors","huggingface_hub"):
    module = importlib.import_module(name)
    packages[name] = str(getattr(module, "__version__", "UNKNOWN"))
importlib.import_module("src.experiments.build_text2trade_mnrl_index_v02")
importlib.import_module("src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02")
os.environ["HF_HUB_OFFLINE"] = "1"; os.environ["TRANSFORMERS_OFFLINE"] = "1"
model = SentenceTransformer(sys.argv[1], device="cpu")
model.max_seq_length = 128
vectors = model.encode([f"synthetic readiness probe {i}" for i in range(32)], batch_size=32, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False).astype(np.float32)
norms = np.linalg.norm(vectors, axis=1)
eps = float(8 * np.finfo(np.float32).eps)
print(json.dumps({"python":sys.version.split()[0],"packages":packages,"builder_import":"PASS","evaluator_import":"PASS","smoke":{"shape":list(vectors.shape),"dtype":str(vectors.dtype),"all_finite":bool(np.isfinite(vectors).all()),"norm_min":float(norms.min()),"norm_max":float(norms.max()),"tolerance":eps,"norms_within_tolerance":bool(np.all(np.abs(norms-1.0)<=eps))}}))
'''
    env = dict(os.environ)
    env.update({"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "PYTHONPATH": str(root)})
    result = subprocess.run([str(interpreter), "-c", script, str(root / model)], cwd=root, env=env, capture_output=True, text=True)
    require(result.returncode == 0, f"Candidate interpreter/model smoke failed: {result.stderr.strip().splitlines()[-1:]}")
    return json.loads(result.stdout.strip().splitlines()[-1])


def optional_historical_vector_replay(root: Path, interpreter: Path) -> dict[str, Any]:
    metadata = _json(root / MODEL_METADATA)
    required = [metadata["artifacts"][key] for key in ("vectors", "docstore", "id_map")]
    sample = root / metadata["artifacts"]["vector_integrity_gate"]["sample_csv"]
    if not sample.is_file() or any(not (root / item["path"]).is_file() for item in required):
        return {"status": "OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE", "classification": "ENVIRONMENT_PARITY_EVIDENCE"}
    for item in required:
        require(_sha256(root / item["path"]) == item["sha256"], f"Historical replay input SHA mismatch: {item['path']}")
    script = r'''
import csv, hashlib, json, sys
import numpy as np
from sentence_transformers import SentenceTransformer
root, metadata_path = sys.argv[1], sys.argv[2]
from pathlib import Path
root=Path(root); meta=json.loads((root/metadata_path).read_text(encoding="utf-8"))
rows=list(csv.DictReader((root/meta["artifacts"]["vector_integrity_gate"]["sample_csv"]).open(encoding="utf-8-sig",newline="")))
indices=[int(r["vector_index"]) for r in rows]
docs=[json.loads(line) for line in (root/meta["artifacts"]["docstore"]["path"]).open(encoding="utf-8")]
texts=[str(docs[i]["texto_index"]).strip() for i in indices]
assert all(hashlib.sha256(t.encode()).hexdigest()==r["stored_text_sha256"] for t,r in zip(texts,rows))
model=SentenceTransformer(str(root/meta["inputs"]["model"]["path"]),device="cpu"); model.max_seq_length=128
rebuilt=model.encode(texts,batch_size=32,convert_to_numpy=True,normalize_embeddings=True,show_progress_bar=False).astype(np.float32)
stored=np.load(root/meta["artifacts"]["vectors"]["path"],mmap_mode="r")[indices].astype(np.float32)
eps=float(8*np.finfo(np.float32).eps); diff=np.abs(rebuilt.astype(np.float64)-stored.astype(np.float64))
cos=np.sum(rebuilt.astype(np.float64)*stored.astype(np.float64),axis=1)/(np.linalg.norm(rebuilt,axis=1)*np.linalg.norm(stored,axis=1))
print(json.dumps({"status":"PASS" if bool(np.all(cos>=1-eps) and np.max(diff)<=eps) else "FAIL","sample_count":len(indices),"cosine_min":float(cos.min()),"max_absolute_difference":float(np.max(diff)),"tolerance":eps}))
'''
    env = dict(os.environ); env.update({"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "PYTHONPATH": str(root)})
    result = subprocess.run([str(interpreter), "-c", script, str(root), MODEL_METADATA.as_posix()], cwd=root, env=env, capture_output=True, text=True)
    require(result.returncode == 0, f"Historical vector replay process failed: {result.stderr.strip().splitlines()[-1:]}")
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    require(payload.get("status") == "PASS", "Historical 21-vector replay failed")
    return {**payload, "classification": "ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT"}


def preauthorization_environment_preflight(root: Path = ROOT, interpreter: Path | str | None = None) -> dict[str, Any]:
    executable = Path(interpreter or sys.executable).resolve()
    require(executable.is_file(), "Candidate interpreter does not exist")
    require(_sha256(executable) == TESTED_ENVIRONMENT["executable_sha256"], "Candidate interpreter SHA is not the tested binding")
    model = validate_complete_model_directory(root)
    probe = _interpreter_probe(root, executable)
    require(probe["python"] == TESTED_ENVIRONMENT["python_version"], "Candidate Python version drift")
    for package, version in TESTED_ENVIRONMENT["required_packages"].items():
        require(probe["packages"].get(package) == version, f"Candidate package version drift: {package}")
    smoke = probe["smoke"]
    require(smoke["shape"] == [32, 384] and smoke["dtype"] == "float32", "Offline model smoke shape/dtype mismatch")
    require(smoke["all_finite"] and smoke["norms_within_tolerance"], "Offline model smoke numerical contract failed")
    disk = shutil.disk_usage(root)
    total_memory, available_memory = _available_memory()
    require(disk.free >= DISK_MARGIN_BYTES, "Host disk is below observed two-copy margin")
    require(available_memory >= MEMORY_MARGIN_BYTES, "Host memory is below two-model-footprint margin")
    replay = optional_historical_vector_replay(root, executable)
    return {
        "status": "PASS", "mode": "PREAUTHORIZATION_ENVIRONMENT_READINESS_ONLY",
        "interpreter": {"python_version": probe["python"], "executable_sha256": _sha256(executable), "packages": probe["packages"]},
        "model": model, "offline_smoke": smoke, "historical_vector_replay": replay,
        "capacity": {"disk_free_bytes": disk.free, "disk_required_margin_bytes": DISK_MARGIN_BYTES, "memory_total_bytes": total_memory, "memory_available_bytes": available_memory, "memory_required_margin_bytes": MEMORY_MARGIN_BYTES},
        "numerical_execution_occurred": False,
    }


def preflight(root: Path = ROOT) -> dict[str, Any]:
    require(not (root / AUTHORIZATION_RECORD).exists(), "v0.5 authorization record must not exist")
    require(all(not (root / path).exists() for path in FUTURE_ROOTS), "A prospective v0.5 root already exists")
    require(set(FUTURE_ROOTS).isdisjoint(V04_ROOTS), "v0.5 roots collide with v0.4 roots")
    bundle = build_bundle(root)
    keys = ("ev03", "ev04", "d1a", "gate", "manifest", "ledger")
    for key, name in zip(keys, ARTIFACT_NAMES, strict=True):
        require(_json(root / AUDIT_ROOT / name) == bundle[key], f"v0.5 persisted gate artifact drift: {name}")
    require(bundle["gate"]["authorization"] == AUTHORIZATION, "v0.5 authorization state is not closed")
    require(tuple(bundle["gate"]["pipeline_steps"]) == PIPELINE_STEPS, "v0.5 19-step order changed")
    validate_ledger_sets(set(bundle["ledger"]["expected_set"]), set(bundle["ledger"]["producer_set"]))
    return {"status": "PASS", "mode": "PREAUTHORIZATION_CLOSED_READONLY", "attempt06": "NOT_AUTHORIZED / NOT_EXECUTED", "prospective_roots_present": False, "numerical_execution_occurred": False}


def write_artifacts(root: Path = ROOT) -> list[str]:
    require(not (root / AUDIT_ROOT).exists(), "v0.5 gate artifact root already exists")
    bundle = build_bundle(root)
    target = root / AUDIT_ROOT
    target.mkdir(parents=True)
    payloads = (bundle["ev03"], bundle["ev04"], bundle["d1a"], bundle["gate"], bundle["manifest"], bundle["ledger"])
    created = []
    for name, payload in zip(ARTIFACT_NAMES, payloads, strict=True):
        path = target / name; path.write_bytes(canonical_json_bytes(payload)); created.append(path.relative_to(root).as_posix())
    return created


def write_readiness(root: Path, environment: Mapping[str, Any], shadow: Mapping[str, Any]) -> str:
    path = root / READINESS_ROOT / "preauthorization_readiness_v0.5.json"
    require(not path.exists(), "v0.5 readiness artifact already exists")
    payload = {
        "artifact_id": "0b05c_v05_preauthorization_readiness",
        "classification": "CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI",
        "status": "BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT",
        "closure_matrix": {key: "CLOSED_BY_CODE_TEST_AND_SHADOW" for key in ("R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19")},
        "environment": dict(environment), "shadow": dict(shadow),
        "residual_risks": ["FULL_7644_DOCUMENT_ENCODE", "FULL_1056_QUERY_ENCODE_AND_EVALUATION", "RUNTIME_MEMORY_CPU_IO_PEAK", "FUTURE_OUTPUT_HASHES", "EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS"],
        "mitigations": ["REPEAT_ENVIRONMENT_AND_CAPACITY_PREFLIGHT_BEFORE_AUTHORIZATION", "USE_FINGERPRINTED_INTERPRETER", "REQUIRE_ALL_V05_ROOTS_ABSENT", "SINGLE_FUTURE_INVOCATION_NO_RETRY_NO_RESUME", "PRESERVE_FAIL_CLOSED_EVIDENCE"],
        "attempt05": "FAIL_CLOSED / AUTHORIZATION_CONSUMED", "attempt06": "NOT_AUTHORIZED / NOT_EXECUTED",
        "0B05C_METRIC_IMPACT": "NOT_DETERMINED", "0B05C_CLOSURE": "NOT_AUTHORIZED",
    }
    path.parent.mkdir(parents=True); path.write_bytes(canonical_json_bytes(payload))
    return path.relative_to(root).as_posix()
