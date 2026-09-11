"""Build and validate the fail-closed 0B-05C v0.5 preauthorization gate."""

from __future__ import annotations

import ast
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
AUTHORIZATION_RECORD_ID = "0b05c_numerical_authorization_record_v0.5"
AUTHORIZATION_RECORD_SCHEMA_VERSION = 1
AUTHORIZED_GATE_STATUS = "APPROVED / INTEGRATED"
AUTHORIZED_READINESS = "AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION"
AUTHORIZED_ATTEMPT06 = "AUTHORIZED / NOT_EXECUTED"
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
GATE_PATH = AUDIT_ROOT / ARTIFACT_NAMES[3]
AUTHORIZATION_BASELINE_ARTIFACTS = {
    "unified_gate": GATE_PATH.as_posix(),
    "ev03_spec": (AUDIT_ROOT / ARTIFACT_NAMES[0]).as_posix(),
    "ev04_spec": (AUDIT_ROOT / ARTIFACT_NAMES[1]).as_posix(),
    "d1a_spec": (AUDIT_ROOT / ARTIFACT_NAMES[2]).as_posix(),
}
AUTHORIZATION_SPEC_KEYS = {
    "ev03_spec": "EV03_NUMERICAL_EXECUTION",
    "ev04_spec": "EV04_NUMERICAL_EXECUTION",
    "d1a_spec": "D1A_NUMERICAL_EXECUTION",
}
AUTHORIZATION_COMMIT_PATH_STATUS = {
    AUTHORIZATION_BASELINE_ARTIFACTS["unified_gate"]: "M",
    AUTHORIZATION_BASELINE_ARTIFACTS["ev03_spec"]: "M",
    AUTHORIZATION_BASELINE_ARTIFACTS["ev04_spec"]: "M",
    AUTHORIZATION_BASELINE_ARTIFACTS["d1a_spec"]: "M",
    AUTHORIZATION_RECORD.as_posix(): "A",
}
D1A_RUNNER_OUTPUTS = {
    "aggregate_comparison": "d1a_corrective_vs_original_comparison_v0.5.json",
    "case_level_comparison": "d1a_corrective_case_level_comparison_v0.5.jsonl",
    "hash_ledger": "d1a_corrective_output_hash_ledger_v0.5.csv",
    "execution_manifest": "d1a_corrective_execution_manifest_v0.5.json",
}
BM25_INDEX_FILENAMES = ("index.pkl", "index_metadata.json")
EV03_OUTPUT_FILENAMES = ("normative_flat_results.csv", "normative_flat_case_summary.csv", "normative_flat_metrics.json")
EV04_OUTPUT_FILENAMES = ("normative_hierarchical_results.csv", "normative_hierarchical_case_summary.csv", "normative_hierarchical_metrics.json")
D1A_INDEX_FILENAMES = (
    "index/vectors.npy", "index/id_map.json", "store/nandina8_docstore.jsonl", "retrieval_config.json",
    "vector_integrity_sample_v0.2.csv", "vector_integrity_gate_v0.2.json", "text2trade_mnrl_nandina8_v02_run_metadata.json",
)
D1A_EVALUATION_FILENAMES = (
    "d1a_metrics.json", "d1a_case_summary.csv", "d1a_ranked_codes_top200.jsonl",
    "strategy_comparison_a_b_c_d0_d1a_v0.2.csv", "summary.md",
)
UNIFIED_OUTPUT_FILENAMES = (
    "ev03_case_level_comparison_v0.5.json", "ev04_case_level_comparison_v0.5.json",
    "ev03_aggregate_comparison_v0.5.json", "ev04_aggregate_comparison_v0.5.json",
    "unified_sensitivity_summary_v0.5.json",
)
ATTEMPT06_ENTRYPOINTS = (
    "src/experiments/run_0b05c_corrective_numerical_v05.py",
    "src/experiments/run_d1a_corrective_0b05c_v05.py",
    "src/experiments/build_text2trade_mnrl_index_v02.py",
    "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py",
)
RUNTIME_DATA_DEPENDENCY_PATHS = (
    "src/configs/experiment_config.json", "src/configs/text2trade_mnrl_v0.2.json",
    "data/processed/corpus_rag_v1_index.jsonl", "data/processed/corpus_nandina_hierarchical_v0.1.jsonl",
    "data/processed/data_aduanas_evalset_clase87_v0.2.csv",
    "data/processed/indexes/bm25_nandina8_run_metadata.json",
    "data/processed/indexes/text2trade_mnrl_nandina8_v0.2/retrieval_config.json",
    "data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_results.csv",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_case_summary.csv",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl",
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json",
    "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json",
    "data/processed/indexes/bm25_nandina8.pkl",
)
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
    "classification": "CURRENT_EXECUTION_ENVIRONMENT_CONTRACT",
    "python_version": "3.10.11",
    "python_implementation": "CPython",
    "architecture": "64bit",
    "platform_system": "Windows",
    "machine": "AMD64",
    "executable_sha256": "b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961",
    "required_packages": {
        "numpy": "2.2.6", "sentence_transformers": "5.5.1",
        "torch": "2.12.0+cpu", "tqdm": "4.68.2",
        "transformers": "5.12.1", "tokenizers": "0.22.2",
        "safetensors": "0.8.0", "huggingface_hub": "1.19.0",
    },
    "required_distributions": {
        "annotated-doc": "0.0.4", "anyio": "4.13.0", "certifi": "2026.5.20",
        "click": "8.4.1", "colorama": "0.4.6", "exceptiongroup": "1.3.1",
        "filelock": "3.29.4", "fsspec": "2026.4.0", "h11": "0.16.0",
        "hf-xet": "1.5.1", "httpcore": "1.0.9", "httpx": "0.28.1",
        "huggingface_hub": "1.19.0", "idna": "3.18", "Jinja2": "3.1.6",
        "joblib": "1.5.3", "markdown-it-py": "4.2.0", "MarkupSafe": "3.0.3",
        "mdurl": "0.1.2", "mpmath": "1.3.0", "networkx": "3.4.2",
        "numpy": "2.2.6", "packaging": "26.2", "Pygments": "2.20.0",
        "Pillow": "12.3.0", "PyYAML": "6.0.3", "regex": "2026.5.9",
        "rich": "15.0.0", "safetensors": "0.8.0", "scikit-learn": "1.7.2",
        "scipy": "1.15.3", "sentence-transformers": "5.5.1",
        "setuptools": "65.5.0", "shellingham": "1.5.4", "sympy": "1.14.0",
        "threadpoolctl": "3.6.0", "tokenizers": "0.22.2", "torch": "2.12.0",
        "tqdm": "4.68.2", "transformers": "5.12.1", "typer": "0.25.1",
        "typing_extensions": "4.15.0",
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
    spec["specification_id"] = f"{arm.lower()}_numerical_execution_spec_v0.5"
    if arm == "EV03":
        spec["prospective_execution"]["case_level_comparison_contract"]["rank_convention"] = "0=NOT_FOUND/EMPTY"
        spec["prospective_execution"]["case_level_comparison_contract"]["empty_ranking_contract"] = "VALID_ONLY_WHEN_SUMMARY_RETRIEVED_COUNT_AND_RANK_REF_ARE_ZERO_AND_TOP1_FIELDS_EMPTY"
    if arm == "d1a":
        output_root = spec["evaluation"]["prospective_output_root"]
        spec["orchestration"]["runner_outputs"] = {
            key: f"{output_root}/{filename}" for key, filename in D1A_RUNNER_OUTPUTS.items()
        }
        included = _d1a_declared_nonledger_paths(spec)
        spec["orchestration"]["hash_ledger_contract"] = {
            "included_paths": list(included),
            "excluded_self_path": spec["orchestration"]["runner_outputs"]["hash_ledger"],
        }
        spec["orchestration"]["runner"] = git_binding(
            root, "src/experiments/run_d1a_corrective_0b05c_v05.py", candidate_revision(root),
            "CANDIDATE_GIT_CANONICAL_BLOB",
        )
    return spec


def _join(root: str, names: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(f"{root}/{name}" for name in names)


def _d1a_declared_nonledger_paths(spec: Mapping[str, Any]) -> tuple[str, ...]:
    derivation = spec["orchestration"]["config_derivation"]
    output_root = spec["evaluation"]["prospective_output_root"]
    runner = spec["orchestration"]["runner_outputs"]
    return (
        spec["corrected_normative_corpus"]["prospective_path"],
        spec["orchestration"]["runtime_config_path"],
        *_join(derivation["corrected_index_root"], D1A_INDEX_FILENAMES),
        *_join(output_root, D1A_EVALUATION_FILENAMES),
        runner["aggregate_comparison"], runner["case_level_comparison"], runner["execution_manifest"],
    )


def expected_runtime_paths_from_specs(ev03: Mapping[str, Any], ev04: Mapping[str, Any], d1a: Mapping[str, Any]) -> tuple[str, ...]:
    """Derive EXPECTED_SET only from declarative v0.5 contracts."""

    paths: list[str] = []
    for spec, names in ((ev03, EV03_OUTPUT_FILENAMES), (ev04, EV04_OUTPUT_FILENAMES)):
        execution = spec["prospective_execution"]
        paths.extend(_join(execution["control_reproduction_index_root"], BM25_INDEX_FILENAMES))
        paths.extend(_join(execution["control_reproduction_output_root"], names))
        paths.append(spec["corrective_corpus"]["prospective_path"])
        paths.extend(_join(execution["corrected_index_root"], BM25_INDEX_FILENAMES))
        paths.extend(_join(execution["corrected_output_root"], names))
    d1a_contract = d1a["orchestration"]["hash_ledger_contract"]
    paths.extend(d1a_contract["included_paths"])
    paths.append(d1a_contract["excluded_self_path"])
    paths.append(f"{FUTURE_ROOTS[15]}/runtime_authorization_record_v0.5.json")
    paths.extend(_join(FUTURE_ROOTS[14], UNIFIED_OUTPUT_FILENAMES))
    paths.append(f"{FUTURE_ROOTS[15]}/execution_manifest_v0.5.json")
    require(len(paths) == len(set(paths)), "Declarative EXPECTED_SET contains a collision")
    return tuple(sorted(paths))


def producer_runtime_paths(_: Mapping[str, Any] | None = None) -> tuple[str, ...]:
    """Derive PRODUCER_SET from the concrete step 1-17 path builders only."""

    paths = [f"{FUTURE_ROOTS[15]}/runtime_authorization_record_v0.5.json"]
    for roots, names in (((FUTURE_ROOTS[0], FUTURE_ROOTS[1], FUTURE_ROOTS[2], FUTURE_ROOTS[3], FUTURE_ROOTS[4]), EV03_OUTPUT_FILENAMES),
                         ((FUTURE_ROOTS[5], FUTURE_ROOTS[6], FUTURE_ROOTS[7], FUTURE_ROOTS[8], FUTURE_ROOTS[9]), EV04_OUTPUT_FILENAMES)):
        control_index, control_output, corpus, corrected_index, corrected_output = roots
        paths.extend(_join(control_index, BM25_INDEX_FILENAMES))
        paths.extend(_join(control_output, names))
        paths.append(corpus)
        paths.extend(_join(corrected_index, BM25_INDEX_FILENAMES))
        paths.extend(_join(corrected_output, names))
    paths.append(FUTURE_ROOTS[10])
    paths.append(f"{FUTURE_ROOTS[13]}/text2trade_mnrl_v0.2_0b05c_runtime.json")
    paths.extend(_join(FUTURE_ROOTS[11], D1A_INDEX_FILENAMES))
    paths.extend(_join(FUTURE_ROOTS[12], D1A_EVALUATION_FILENAMES))
    paths.extend(_join(FUTURE_ROOTS[12], tuple(D1A_RUNNER_OUTPUTS.values())))
    paths.extend(_join(FUTURE_ROOTS[14], UNIFIED_OUTPUT_FILENAMES))
    paths.append(f"{FUTURE_ROOTS[15]}/execution_manifest_v0.5.json")
    require(len(paths) == len(set(paths)), "Concrete PRODUCER_SET contains a path collision")
    return tuple(sorted(paths))


def _git(root: Path, *args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=not binary)
    return result.stdout if binary else result.stdout.strip()


def candidate_revision(root: Path) -> str:
    for revision in ("INDEX", "HEAD"):
        spec = ":src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py" if revision == "INDEX" else "HEAD:src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py"
        if subprocess.run(["git", "cat-file", "-e", spec], cwd=root, capture_output=True).returncode == 0:
            return revision
    raise ContractViolation("Candidate v0.5 sources are not staged or committed")


def git_binding(root: Path, path: str, revision: str = "HEAD", classification: str = "VERSIONED_GIT_BLOB") -> dict[str, Any]:
    spec = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
    raw = _git(root, "show", spec, binary=True)
    assert isinstance(raw, bytes)
    return {
        "path": path, "classification": classification,
        "git_blob_sha1": str(_git(root, "rev-parse", spec)),
        "canonical_git_blob_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_size_bytes": len(raw),
    }


def authorization_artifact_binding(root: Path, path: str, revision: str) -> dict[str, Any]:
    binding = git_binding(root, path, revision)
    return {key: binding[key] for key in ("path", "git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes")}


def _git_path_exists(root: Path, path: str, revision: str) -> bool:
    spec = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
    return subprocess.run(["git", "cat-file", "-e", spec], cwd=root, capture_output=True).returncode == 0


def _module_path(root: Path, module: str, revision: str) -> str | None:
    if not module.startswith("src"):
        return None
    base = module.replace(".", "/")
    for candidate in (f"{base}.py", f"{base}/__init__.py"):
        if _git_path_exists(root, candidate, revision):
            return candidate
    return None


def _module_name(path: str) -> str:
    module = path[:-3].replace("/", ".")
    return module[:-9] if module.endswith(".__init__") else module


def _package_initializers(root: Path, module: str, revision: str) -> set[str]:
    parts = module.split(".")
    paths: set[str] = set()
    for length in range(1, len(parts)):
        candidate = "/".join(parts[:length]) + "/__init__.py"
        if _git_path_exists(root, candidate, revision):
            paths.add(candidate)
    return paths


def project_local_import_closure(
    root: Path,
    revision: str | None = None,
    entrypoints: tuple[str, ...] = ATTEMPT06_ENTRYPOINTS,
) -> tuple[str, ...]:
    """Resolve the recursive project-local import closure from canonical Git bytes."""

    revision = revision or candidate_revision(root)
    pending = list(entrypoints)
    closure: set[str] = set()
    while pending:
        path = pending.pop()
        require(_git_path_exists(root, path, revision), f"Project import entry/dependency is absent: {path}")
        if path in closure:
            continue
        closure.add(path)
        module = _module_name(path)
        for initializer in _package_initializers(root, module, revision):
            if initializer not in closure:
                pending.append(initializer)
        spec = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
        raw = _git(root, "show", spec, binary=True)
        assert isinstance(raw, bytes)
        tree = ast.parse(raw.decode("utf-8"), filename=path)
        imported: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names if alias.name.startswith("src"))
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    package = module.split(".")[:-1]
                    keep = len(package) - (node.level - 1)
                    require(keep >= 0, f"Invalid relative import in {path}")
                    prefix = package[:keep]
                    if node.module:
                        prefix += node.module.split(".")
                    base = ".".join(prefix)
                else:
                    base = node.module or ""
                if base.startswith("src"):
                    imported.add(base)
                    imported.update(f"{base}.{alias.name}" for alias in node.names if alias.name != "*")
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "import_module"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)
                and node.args[0].value.startswith("src")
            ):
                imported.add(node.args[0].value)
        for imported_module in sorted(imported):
            resolved = _module_path(root, imported_module, revision)
            if resolved and resolved not in closure:
                pending.append(resolved)
    return tuple(sorted(closure))


def project_import_bindings(root: Path, revision: str | None = None) -> list[dict[str, Any]]:
    revision = revision or candidate_revision(root)
    return [git_binding(root, path, revision, "PROJECT_LOCAL_IMPORT_CLOSURE") for path in project_local_import_closure(root, revision)]


def runtime_data_dependency_bindings(root: Path, revision: str = "HEAD") -> list[dict[str, Any]]:
    return [git_binding(root, path, revision, "VERSIONED_RUNTIME_DATA_DEPENDENCY") for path in RUNTIME_DATA_DEPENDENCY_PATHS]


def validate_project_import_bindings(
    root: Path,
    bindings: Any,
    revision: str = "HEAD",
    entrypoints: tuple[str, ...] = ATTEMPT06_ENTRYPOINTS,
) -> None:
    expected_paths = set(project_local_import_closure(root, revision, entrypoints))
    require(isinstance(bindings, list) and len(bindings) == len(expected_paths), "Project import binding count is not exact")
    require({item.get("path") for item in bindings} == expected_paths, "Project import closure binding path set is not exact")
    for binding in bindings:
        require(binding.get("classification") == "PROJECT_LOCAL_IMPORT_CLOSURE", f"Project import binding classification changed: {binding.get('path')}")
        require(binding == git_binding(root, binding["path"], revision, "PROJECT_LOCAL_IMPORT_CLOSURE"), f"Project import binding drift: {binding['path']}")


def dependency_bindings(root: Path) -> list[dict[str, Any]]:
    candidate = candidate_revision(root)
    return [*project_import_bindings(root, candidate), *runtime_data_dependency_bindings(root, candidate)]


def build_bundle(root: Path = ROOT) -> dict[str, Any]:
    ev03 = _spec(root, ARTIFACT_NAMES[0], "EV03")
    ev04 = _spec(root, ARTIFACT_NAMES[1], "EV04")
    d1a = _spec(root, ARTIFACT_NAMES[2], "d1a")
    expected = expected_runtime_paths_from_specs(ev03, ev04, d1a)
    sources = dependency_bindings(root)
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
        "project_local_import_closure": list(project_local_import_closure(root, candidate_revision(root))),
        "runtime_data_dependency_paths": list(RUNTIME_DATA_DEPENDENCY_PATHS),
        "runtime_hash_ledger_contract": {
            "expected_paths": list(expected),
            "excluded_self_path": "outputs/audits/0b05c_corrective_numerical_runtime_v0.5/exact_hash_ledger_v0.5.json",
            "entry_fields": ["path", "sha256", "size_bytes"],
            "missing_or_unexpected_policy": "FAIL_CLOSED",
        },
        "candidate_source_bindings": sources,
        "authorization_record_contract": authorization_record_contract(),
        "scientific_state": {"0B05C_METRIC_IMPACT": "NOT_DETERMINED", "0B05C_CLOSURE": "NOT_AUTHORIZED"},
    }
    bundle: dict[str, Any] = {"ev03": ev03, "ev04": ev04, "d1a": d1a, "gate": gate}
    producer = producer_runtime_paths()
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
    audit_stale_current_identities(bundle)
    return bundle


def validate_manifest_payload(payload: Mapping[str, Any]) -> None:
    required = {"artifact_id", "status", "authorization_provenance", "environment_fingerprint", "pipeline_steps", "future_roots", "results"}
    require(isinstance(payload, Mapping) and set(payload) == required, "Execution manifest schema is not exact")
    require(payload.get("status") == "PASS", "Execution manifest status is not PASS")
    require(payload.get("pipeline_steps") == list(PIPELINE_STEPS), "Execution manifest 19-step order changed")
    provenance = payload.get("authorization_provenance")
    provenance_fields = {
        "status", "execution_authorization_commit", "authorization_baseline_commit", "authorization_transition_proof",
        "authorization_commit_shape", "current_dependency_bindings_equal_baseline",
        "authorization_flags", "authorization_record_binding", "authorized_artifact_bindings",
    }
    require(isinstance(provenance, Mapping) and set(provenance) == provenance_fields and provenance.get("status") == "PASS", "Execution manifest authorization provenance is incomplete")
    for key in ("execution_authorization_commit", "authorization_baseline_commit"):
        value = provenance.get(key)
        require(isinstance(value, str) and len(value) == 40, f"Execution manifest {key} is malformed")
    require(provenance.get("authorization_flags") == {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}, "Execution manifest authorization flags are inconsistent")
    binding_fields = {"path", "git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes"}
    require(isinstance(provenance.get("authorization_record_binding"), Mapping) and set(provenance["authorization_record_binding"]) == binding_fields, "Execution manifest authorization record binding is incomplete")
    require(isinstance(provenance.get("authorized_artifact_bindings"), Mapping) and set(provenance["authorized_artifact_bindings"]) == set(AUTHORIZATION_BASELINE_ARTIFACTS), "Execution manifest authorized artifacts are incomplete")
    require(isinstance(provenance.get("authorization_transition_proof"), Mapping) and provenance["authorization_transition_proof"].get("status") == "PASS", "Execution manifest transition proof is incomplete")
    require(isinstance(provenance.get("authorization_commit_shape"), Mapping) and provenance["authorization_commit_shape"].get("mode") == "DIRECT_PARENT_EXACT_FIVE_PATH_AUTHORIZATION_DIFF", "Execution manifest authorization commit shape is incomplete")
    require(provenance.get("current_dependency_bindings_equal_baseline") is True, "Execution manifest current dependency bindings are not proven equal")
    environment = payload.get("environment_fingerprint")
    require(isinstance(environment, Mapping), "Execution manifest environment fingerprint is malformed")
    for key in ("python_version", "python_implementation", "architecture", "platform_system", "machine", "executable_sha256"):
        require(environment.get(key) == TESTED_ENVIRONMENT[key], f"Execution manifest environment fingerprint drift: {key}")
    require(environment.get("packages") == TESTED_ENVIRONMENT["required_packages"], "Execution manifest critical package stack drift")
    require(environment.get("distributions") == TESTED_ENVIRONMENT["required_distributions"], "Execution manifest transitive distribution stack drift")
    require(environment.get("project_imports", {}).get("status") == "PASS" and environment["project_imports"].get("count") == len(project_local_import_closure(ROOT)), "Execution manifest project import closure evidence is incomplete")
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
    discovery_roots: tuple[str, ...] = FUTURE_ROOTS,
    excluded_self_path: str = "outputs/audits/0b05c_corrective_numerical_runtime_v0.5/exact_hash_ledger_v0.5.json",
) -> list[dict[str, Any]]:
    validate_ledger_sets(expected, produced)
    observed = observed_runtime_paths(root, discovery_roots, excluded_self_path)
    require(observed == expected, f"Runtime observed set mismatch: missing={sorted(expected-observed)}, unexpected={sorted(observed-expected)}")
    entries = []
    for relative in sorted(observed):
        path = root / relative
        require(path.is_file() and path.stat().st_size > 0, f"Runtime output missing or empty: {relative}")
        digest = _sha256(path)
        if snapshot is not None and relative in snapshot:
            require(snapshot[relative] == digest, f"Runtime output changed after integrity snapshot: {relative}")
        entries.append({"path": relative, "sha256": digest, "size_bytes": path.stat().st_size})
    return entries


def observed_runtime_paths(root: Path, discovery_roots: tuple[str, ...], excluded_self_path: str) -> set[str]:
    observed: set[str] = set()
    for relative in discovery_roots:
        path = root / relative
        if path.is_file():
            observed.add(relative)
        elif path.is_dir():
            observed.update(item.relative_to(root).as_posix() for item in path.rglob("*") if item.is_file())
    observed.discard(excluded_self_path)
    return observed


def authorization_record_contract() -> dict[str, Any]:
    return {
        "artifact_id": AUTHORIZATION_RECORD_ID,
        "schema_version": AUTHORIZATION_RECORD_SCHEMA_VERSION,
        "path": AUTHORIZATION_RECORD.as_posix(),
        "required_fields": ["artifact_id", "schema_version", "authorization_baseline_commit", "baseline_external_audit", "baseline_artifacts"],
        "baseline_external_audit": "PASS / APPROVED_FOR_INTEGRATION",
        "baseline_artifacts": dict(AUTHORIZATION_BASELINE_ARTIFACTS),
        "baseline_relationship": "DIRECT_PARENT_OF_SINGLE_AUTHORIZATION_COMMIT",
        "authorization_commit_path_status": dict(AUTHORIZATION_COMMIT_PATH_STATUS),
        "binding_fields": ["path", "git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes"],
    }


def validate_authorization_record_schema(record: Mapping[str, Any]) -> None:
    contract = authorization_record_contract()
    require(set(record) == set(contract["required_fields"]), "Authorization record v0.5 fields are not exact")
    require(record.get("artifact_id") == AUTHORIZATION_RECORD_ID, "Authorization record v0.5 artifact_id is invalid")
    require(record.get("schema_version") == AUTHORIZATION_RECORD_SCHEMA_VERSION, "Authorization record v0.5 schema_version is invalid")
    baseline = record.get("authorization_baseline_commit")
    require(isinstance(baseline, str) and len(baseline) == 40 and all(char in "0123456789abcdef" for char in baseline), "Authorization baseline commit is malformed")
    require(record.get("baseline_external_audit") == contract["baseline_external_audit"], "Authorization baseline external audit is invalid")
    artifacts = record.get("baseline_artifacts")
    require(isinstance(artifacts, Mapping) and set(artifacts) == set(AUTHORIZATION_BASELINE_ARTIFACTS), "Authorization baseline artifact set is not exact")
    fields = set(contract["binding_fields"])
    for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items():
        binding = artifacts[key]
        require(isinstance(binding, Mapping) and set(binding) == fields and binding.get("path") == path, f"Authorization baseline binding is invalid: {key}")


def validate_authorization_baseline_ancestry(root: Path, baseline: str, revision: str = "HEAD") -> str:
    current = str(_git(root, "rev-parse", revision))
    require(baseline != current, "Authorization baseline must be a proper ancestor")
    commit_line = str(_git(root, "rev-list", "--parents", "-n", "1", current)).split()
    require(len(commit_line) == 2 and commit_line[1] == baseline, "Authorization baseline is not the direct parent")
    return current


def validate_authorization_commit_shape(root: Path, baseline: str, revision: str = "HEAD") -> dict[str, Any]:
    current = validate_authorization_baseline_ancestry(root, baseline, revision)
    raw = str(_git(root, "diff", "--name-status", "--no-renames", baseline, current))
    observed: dict[str, str] = {}
    for line in raw.splitlines():
        status, path = line.split("\t", 1)
        require(status in {"A", "M", "D"}, f"Unsupported authorization diff status: {status}")
        observed[path] = status
    require(observed == AUTHORIZATION_COMMIT_PATH_STATUS, f"Authorization commit path/status set is not exact: {observed}")
    return {"status": "PASS", "mode": "DIRECT_PARENT_EXACT_FIVE_PATH_AUTHORIZATION_DIFF", "baseline": baseline, "authorization_commit": current, "path_status": observed}


def validate_authorization_record_bindings(root: Path, record: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    baseline = str(record["authorization_baseline_commit"])
    expected = {key: authorization_artifact_binding(root, path, baseline) for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()}
    require(record["baseline_artifacts"] == expected, "Authorization baseline artifact binding mismatch")
    return expected


def _git_json(root: Path, path: str, revision: str) -> dict[str, Any]:
    raw = _git(root, "show", f"{revision}:{path}", binary=True)
    assert isinstance(raw, bytes)
    payload = json.loads(raw.decode("utf-8"))
    require(isinstance(payload, dict), f"Authorization artifact is not a JSON object: {path}")
    return payload


def _authorization_projection(payload: Mapping[str, Any], artifact: str) -> dict[str, Any]:
    projected = copy.deepcopy(dict(payload))
    projected["attempt06"] = "<AUTHORIZED_TRANSITION_FIELD>"
    if artifact == "unified_gate":
        projected["gate_status"] = "<AUTHORIZED_TRANSITION_FIELD>"
        projected["authorization_readiness"] = "<AUTHORIZED_TRANSITION_FIELD>"
        for key in (*[name for name in AUTHORIZATION if name.endswith("NUMERICAL_EXECUTION")], "authorization_record_present"):
            projected["authorization"][key] = "<AUTHORIZED_TRANSITION_FIELD>"
    else:
        projected["authorization"][AUTHORIZATION_SPEC_KEYS[artifact]] = "<AUTHORIZED_TRANSITION_FIELD>"
    return projected


def validate_authorization_transition(baseline_artifacts: Mapping[str, Mapping[str, Any]], authorized_artifacts: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    keys = set(AUTHORIZATION_BASELINE_ARTIFACTS)
    require(set(baseline_artifacts) == keys and set(authorized_artifacts) == keys, "Authorization transition artifact set is not exact")
    baseline_gate, authorized_gate = baseline_artifacts["unified_gate"], authorized_artifacts["unified_gate"]
    require(baseline_gate.get("gate_status") == "CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED", "Authorization baseline gate status is invalid")
    require(baseline_gate.get("authorization_readiness") == "NOT_AUTHORIZED" and baseline_gate.get("authorization") == AUTHORIZATION, "Authorization baseline gate is not closed")
    require(baseline_gate.get("attempt06") == "NOT_AUTHORIZED / NOT_EXECUTED", "Authorization baseline Attempt06 is invalid")
    require(authorized_gate.get("gate_status") == AUTHORIZED_GATE_STATUS and authorized_gate.get("authorization_readiness") == AUTHORIZED_READINESS, "Authorized gate status/readiness is invalid")
    four = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    require({key: authorized_gate.get("authorization", {}).get(key) for key in four} == four, "Authorized gate flags are incomplete")
    require(authorized_gate.get("authorization", {}).get("authorization_record_present") is True, "Authorized gate record flag is false")
    for key in ("corrective_retrieval_executed", "corrective_metrics_computed", "runtime_authorization_record_present"):
        require(authorized_gate.get("authorization", {}).get(key) is False, f"Authorization transition changed {key}")
    require(authorized_gate.get("attempt06") == AUTHORIZED_ATTEMPT06, "Authorized Attempt06 state is invalid")
    require(authorized_gate.get("attempt05") == "FAIL_CLOSED / AUTHORIZATION_CONSUMED", "Attempt05 historical state drift")
    for artifact, key in AUTHORIZATION_SPEC_KEYS.items():
        before, after = baseline_artifacts[artifact], authorized_artifacts[artifact]
        require(before.get("authorization", {}).get(key) == "NOT_AUTHORIZED" and before.get("attempt06") == "NOT_AUTHORIZED / NOT_EXECUTED", f"Baseline {artifact} is not closed")
        require(after.get("authorization", {}).get(key) == "AUTHORIZED" and after.get("attempt06") == AUTHORIZED_ATTEMPT06, f"Authorized {artifact} is invalid")
    before_projection = {key: _authorization_projection(value, key) for key, value in baseline_artifacts.items()}
    after_projection = {key: _authorization_projection(value, key) for key, value in authorized_artifacts.items()}
    require(before_projection == after_projection, "Authorization transition changed immutable scientific or technical content")
    digest = hashlib.sha256(canonical_json_bytes(before_projection)).hexdigest()
    return {"status": "PASS", "mode": "BASELINE_TO_AUTHORIZED_IMMUTABLE_PROJECTION", "allowed_fields_only": True, "projection_sha256": digest}


def validate_dependency_bindings(root: Path, bindings: Any, revision: str = "HEAD") -> None:
    source_paths = set(project_local_import_closure(root, revision))
    expected_paths = source_paths | set(RUNTIME_DATA_DEPENDENCY_PATHS)
    require(isinstance(bindings, list) and len(bindings) == len(expected_paths) and {item.get("path") for item in bindings} == expected_paths, "Dependency binding path set is not exact")
    source_bindings = [item for item in bindings if item.get("path") in source_paths]
    validate_project_import_bindings(root, source_bindings, revision)
    data_bindings = [item for item in bindings if item.get("path") in RUNTIME_DATA_DEPENDENCY_PATHS]
    require(len(data_bindings) == len(RUNTIME_DATA_DEPENDENCY_PATHS), "Runtime data dependency binding count is not exact")
    for binding in data_bindings:
        require(binding.get("classification") == "VERSIONED_RUNTIME_DATA_DEPENDENCY", f"Runtime data binding classification changed: {binding.get('path')}")
        require(binding == git_binding(root, binding["path"], revision, "VERSIONED_RUNTIME_DATA_DEPENDENCY"), f"Runtime data Git binding drift: {binding['path']}")


def load_authorization_transition_from_git(root: Path, current_gate: Mapping[str, Any]) -> dict[str, Any]:
    record = _json(root / AUTHORIZATION_RECORD)
    validate_authorization_record_schema(record)
    baseline = str(record["authorization_baseline_commit"])
    current = validate_authorization_baseline_ancestry(root, baseline)
    shape = validate_authorization_commit_shape(root, baseline, current)
    baseline_bindings = validate_authorization_record_bindings(root, record)
    baseline_artifacts = {key: _git_json(root, path, baseline) for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()}
    authorized_artifacts = {key: _git_json(root, path, current) for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()}
    filesystem = {key: _json(root / path) for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()}
    validate_filesystem_authorization_artifacts(authorized_artifacts, filesystem)
    require(authorized_artifacts["unified_gate"] == dict(current_gate), "Filesystem gate differs from committed authorization gate")
    transition = validate_authorization_transition(baseline_artifacts, authorized_artifacts)
    frozen_dependencies = baseline_artifacts["unified_gate"]["candidate_source_bindings"]
    validate_dependency_bindings(root, frozen_dependencies, baseline)
    validate_dependency_bindings(root, frozen_dependencies, current)
    return {
        "status": "PASS", "authorization_baseline_commit": baseline, "execution_authorization_commit": current,
        "baseline_external_audit": record["baseline_external_audit"], "baseline_artifact_bindings": baseline_bindings,
        "authorized_artifact_bindings": {key: authorization_artifact_binding(root, path, current) for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()},
        "authorization_record_binding": authorization_artifact_binding(root, AUTHORIZATION_RECORD.as_posix(), current),
        "record": record, "transition": transition, "authorization_commit_shape": shape,
        "current_dependency_bindings_equal_baseline": True, "artifacts": authorized_artifacts,
    }


def validate_filesystem_authorization_artifacts(committed: Mapping[str, Mapping[str, Any]], filesystem: Mapping[str, Mapping[str, Any]]) -> None:
    require(set(committed) == set(AUTHORIZATION_BASELINE_ARTIFACTS) and set(filesystem) == set(AUTHORIZATION_BASELINE_ARTIFACTS), "Authorization filesystem artifact set is not exact")
    require(filesystem == committed, "Filesystem gate/specs differ from committed authorization artifacts")


STALE_V04_ALLOWLIST = {
    "attempt05", "v04_partial_roots", "v04_partial_roots_policy", "v01_classification",
    "v02_attempt03_provenance", "v03_attempt04_provenance",
}
STALE_SOURCE_TOKEN_ALLOWLIST = {
    "src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py": (
        "audited v0.4 code", "corrective_0b05c_v01 as legacy", "corrective_0b05c_v04 as v04",
    ),
    "src/experiments/run_d1a_corrective_0b05c_v05.py": (
        "corrective_0b05c_v01 as legacy", "D1a execution manifest references stale current output",
    ),
    "src/experiments/run_0b05c_corrective_numerical_v05.py": (
        "prepare_0b05c_corrective_numerical_gate_v01 as v01_gate", "evaluator.v04.compare_complete_ev04_control_v04",
    ),
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py": (
        "V04_ROOTS =", "corrective_numerical_gate_v0.4", "name.replace(\"v0.5\", \"v0.4\")",
        "corrective_0b05c_v04.py", "corrective_0b05c_v01.py", "corpus_nandina_hierarchical_v0.1.jsonl",
        ".replace(\"evaluate_normative_bm25_corrective_0b05c_v04\"", ".replace(\"run_d1a_corrective_0b05c_v04\"",
        ".replace(\"run_0b05c_corrective_numerical_v04\"", "v0.4 partial root", "\"v0.4\" in value",
        "corrective_0b05c_v01\" in value", "historical_v0.4", "v0.5 roots collide with v0.4 roots",
        "Non-allowlisted v0.4 occurrence", "\"v0.4\", \"_v04\", \"v0.1\", \"_v01\"",
        "Non-allowlisted stale source token",
    ),
}


def audit_stale_current_identities(bundle: Mapping[str, Any]) -> dict[str, Any]:
    for name in ("ev03", "ev04", "d1a"):
        require(bundle[name].get("specification_id") == f"{name}_numerical_execution_spec_v0.5", f"Stale specification_id: {name}")
    d1a = bundle["d1a"]
    runner_outputs = d1a["orchestration"]["runner_outputs"]
    require(tuple(Path(runner_outputs[key]).name for key in D1A_RUNNER_OUTPUTS) == tuple(D1A_RUNNER_OUTPUTS.values()), "D1a current runner output identity is stale")
    require(d1a["orchestration"]["runner"]["path"] == "src/experiments/run_d1a_corrective_0b05c_v05.py", "D1a current runner binding is stale")
    current_fields = [d1a["specification_id"], d1a["orchestration"]["runner"]["path"], *runner_outputs.values(), d1a["orchestration"]["hash_ledger_contract"]["excluded_self_path"]]
    require(not any("v0.4" in value or "corrective_0b05c_v01" in value for value in current_fields), "Stale current v0.4/v0.1 D1a identity")
    historical: list[str] = []

    def walk(value: Any, trail: tuple[str, ...] = ()) -> None:
        if isinstance(value, Mapping):
            for key, item in value.items():
                walk(item, (*trail, str(key)))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, (*trail, str(index)))
        elif isinstance(value, str) and "v0.4" in value:
            joined = ".".join(trail)
            allowed = any(token in joined for token in STALE_V04_ALLOWLIST) or "v04_partial" in value or "attempt04" in joined
            require(allowed, f"Non-allowlisted v0.4 occurrence: {joined}={value}")
            historical.append(joined)

    walk(bundle)
    return {"status": "PASS", "historical_v0.4_allowlist": sorted(STALE_V04_ALLOWLIST), "historical_occurrences": sorted(historical), "stale_current_identity_count": 0}


def audit_stale_source_tokens(root: Path) -> dict[str, Any]:
    occurrences: list[dict[str, Any]] = []
    for relative, allowlist in STALE_SOURCE_TOKEN_ALLOWLIST.items():
        in_allowlist_declaration = False
        for number, line in enumerate((root / relative).read_text(encoding="utf-8").splitlines(), 1):
            if relative.endswith("prepare_0b05c_corrective_numerical_gate_v05.py") and line.startswith("STALE_SOURCE_TOKEN_ALLOWLIST ="):
                in_allowlist_declaration = True
            if in_allowlist_declaration:
                if line == "}":
                    in_allowlist_declaration = False
                continue
            if any(token in line for token in ("v0.4", "_v04", "v0.1", "_v01")):
                require(any(allowed in line for allowed in allowlist), f"Non-allowlisted stale source token: {relative}:{number}")
                occurrences.append({"path": relative, "line": number, "classification": "EXPLICIT_HISTORICAL_OR_REUSED_COMPONENT_ALLOWLIST"})
    return {"status": "PASS", "allowlist": {key: list(value) for key, value in STALE_SOURCE_TOKEN_ALLOWLIST.items()}, "occurrences": occurrences, "stale_current_identity_count": 0}


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


def validate_complete_model_directory(root: Path, asset_root: Path | None = None) -> dict[str, Any]:
    asset_root = (asset_root or root).resolve()
    metadata = _json(root / MODEL_METADATA)
    governed = metadata["inputs"]["model"]["files"]
    require(isinstance(governed, list) and len(governed) == 9, "Frozen model manifest must govern exactly nine files")
    expected_paths = {item["path"] for item in governed}
    model_root = asset_root / metadata["inputs"]["model"]["path"]
    require(model_root.is_dir(), "Complete frozen model directory is absent")
    observed = {path.relative_to(asset_root).as_posix() for path in model_root.rglob("*") if path.is_file()}
    require(observed == expected_paths, f"Frozen model directory file set mismatch: missing={sorted(expected_paths-observed)}, extra={sorted(observed-expected_paths)}")
    for item in governed:
        path = asset_root / item["path"]
        require(path.stat().st_size == item["size_bytes"], f"Frozen model size mismatch: {item['path']}")
        require(_sha256(path) == item["sha256"], f"Frozen model SHA mismatch: {item['path']}")
    return {"status": "PASS_EXACT", "governed_file_count": 9, "model_directory": metadata["inputs"]["model"]["path"]}


def _interpreter_probe(root: Path, interpreter: Path, asset_root: Path | None = None) -> dict[str, Any]:
    asset_root = (asset_root or root).resolve()
    model = _json(root / MODEL_METADATA)["inputs"]["model"]["path"]
    modules = sorted({_module_name(path) for path in project_local_import_closure(root)})
    distributions = sorted(TESTED_ENVIRONMENT["required_distributions"])
    script = r'''
import importlib, importlib.metadata, json, os, platform, sys
import numpy as np
from sentence_transformers import SentenceTransformer
packages = {}
for name in ("numpy","sentence_transformers","torch","tqdm","transformers","tokenizers","safetensors","huggingface_hub"):
    module = importlib.import_module(name)
    packages[name] = str(getattr(module, "__version__", "UNKNOWN"))
modules=json.loads(sys.argv[2]); distributions=json.loads(sys.argv[3])
for module in modules: importlib.import_module(module)
distribution_versions={name:importlib.metadata.version(name) for name in distributions}
os.environ["HF_HUB_OFFLINE"] = "1"; os.environ["TRANSFORMERS_OFFLINE"] = "1"
model = SentenceTransformer(sys.argv[1], device="cpu")
model.max_seq_length = 128
vectors = model.encode([f"synthetic readiness probe {i}" for i in range(32)], batch_size=32, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False).astype(np.float32)
norms = np.linalg.norm(vectors, axis=1)
eps = float(8 * np.finfo(np.float32).eps)
print(json.dumps({"python":sys.version.split()[0],"python_implementation":platform.python_implementation(),"architecture":platform.architecture()[0],"platform_system":platform.system(),"machine":platform.machine(),"packages":packages,"distributions":distribution_versions,"project_imports":{"status":"PASS","count":len(modules),"modules":modules},"smoke":{"shape":list(vectors.shape),"dtype":str(vectors.dtype),"all_finite":bool(np.isfinite(vectors).all()),"norm_min":float(norms.min()),"norm_max":float(norms.max()),"tolerance":eps,"norms_within_tolerance":bool(np.all(np.abs(norms-1.0)<=eps))}}))
'''
    env = dict(os.environ)
    env.update({"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "PYTHONPATH": str(root)})
    result = subprocess.run([str(interpreter), "-c", script, str(asset_root / model), json.dumps(modules), json.dumps(distributions)], cwd=root, env=env, capture_output=True, text=True)
    require(result.returncode == 0, f"Candidate interpreter/model smoke failed: {result.stderr.strip().splitlines()[-1:]}")
    return json.loads(result.stdout.strip().splitlines()[-1])


def optional_historical_vector_replay(root: Path, interpreter: Path, asset_root: Path | None = None) -> dict[str, Any]:
    asset_root = (asset_root or root).resolve()
    metadata = _json(root / MODEL_METADATA)
    required = [metadata["artifacts"][key] for key in ("vectors", "docstore", "id_map")]
    sample = asset_root / metadata["artifacts"]["vector_integrity_gate"]["sample_csv"]
    if not sample.is_file() or any(not (asset_root / item["path"]).is_file() for item in required):
        return {"status": "OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE", "classification": "ENVIRONMENT_PARITY_EVIDENCE"}
    for item in required:
        require(_sha256(asset_root / item["path"]) == item["sha256"], f"Historical replay input SHA mismatch: {item['path']}")
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
    if asset_root != root.resolve():
        require((asset_root / MODEL_METADATA).is_file() and _sha256(asset_root / MODEL_METADATA) == _sha256(root / MODEL_METADATA), "Historical replay metadata differs between candidate and local asset root")
    result = subprocess.run([str(interpreter), "-c", script, str(asset_root), MODEL_METADATA.as_posix()], cwd=root, env=env, capture_output=True, text=True)
    require(result.returncode == 0, f"Historical vector replay process failed: {result.stderr.strip().splitlines()[-1:]}")
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    require(payload.get("status") == "PASS", "Historical 21-vector replay failed")
    return {**payload, "classification": "ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT"}


def preauthorization_environment_preflight(
    root: Path = ROOT,
    interpreter: Path | str | None = None,
    *,
    asset_root: Path | None = None,
) -> dict[str, Any]:
    executable = Path(interpreter or sys.executable).resolve()
    require(executable.is_file(), "Candidate interpreter does not exist")
    require(_sha256(executable) == TESTED_ENVIRONMENT["executable_sha256"], "Candidate interpreter SHA is not the tested binding")
    model = validate_complete_model_directory(root, asset_root)
    probe = _interpreter_probe(root, executable, asset_root)
    require(probe["python"] == TESTED_ENVIRONMENT["python_version"], "Candidate Python version drift")
    for key in ("python_implementation", "architecture", "platform_system", "machine"):
        require(probe.get(key) == TESTED_ENVIRONMENT[key], f"Candidate interpreter platform drift: {key}")
    for package, version in TESTED_ENVIRONMENT["required_packages"].items():
        require(probe["packages"].get(package) == version, f"Candidate package version drift: {package}")
    require(probe.get("distributions") == TESTED_ENVIRONMENT["required_distributions"], "Candidate transitive distribution stack drift")
    require(probe.get("project_imports", {}).get("status") == "PASS" and probe["project_imports"].get("count") == len(project_local_import_closure(root)), "Candidate project import closure did not import exactly")
    smoke = probe["smoke"]
    require(smoke["shape"] == [32, 384] and smoke["dtype"] == "float32", "Offline model smoke shape/dtype mismatch")
    require(smoke["all_finite"] and smoke["norms_within_tolerance"], "Offline model smoke numerical contract failed")
    disk = shutil.disk_usage(root)
    total_memory, available_memory = _available_memory()
    require(disk.free >= DISK_MARGIN_BYTES, "Host disk is below observed two-copy margin")
    require(available_memory >= MEMORY_MARGIN_BYTES, "Host memory is below two-model-footprint margin")
    replay = optional_historical_vector_replay(root, executable, asset_root)
    return {
        "status": "PASS", "mode": "PREAUTHORIZATION_ENVIRONMENT_READINESS_ONLY",
        "interpreter": {
            "python_version": probe["python"], "python_implementation": probe["python_implementation"],
            "architecture": probe["architecture"], "platform_system": probe["platform_system"],
            "machine": probe["machine"], "executable_sha256": _sha256(executable),
            "packages": probe["packages"], "distributions": probe["distributions"],
            "project_imports": probe["project_imports"],
        },
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
        "status": "BUILT / CURRENT_ENVIRONMENT_VERIFIED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT",
        "closure_matrix": {key: "CLOSED_BY_CODE_TEST_AND_SHADOW" for key in ("R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19")},
        "external_audit_findings": {f"F35D-0{index}": "CLOSED_BY_CODE_TEST_AND_SHADOW" for index in range(1, 6)},
        "environment": {
            "LAST_KNOWN_TESTED_ENVIRONMENT": {
                "classification": "PROMPT35B_CODEX_LOCAL_EVIDENCE / NOT_CURRENT_REPROBE",
                "python_version": "3.10.11",
                "executable_sha256": "b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961",
                "model_manifest": "9/9 PASS_EXACT",
                "offline_smoke": "PASS / 32x384 / FLOAT32 / FINITE / NORMALIZED",
                "historical_vector_replay": "PASS / 21_VECTORS",
            },
            "CURRENT_EXECUTION_ENVIRONMENT_READINESS": {**dict(environment), "readiness": "PASS"},
        },
        "shadow": dict(shadow),
        "residual_risks": ["FULL_7644_DOCUMENT_ENCODE", "FULL_1056_QUERY_ENCODE_AND_EVALUATION", "RUNTIME_MEMORY_CPU_IO_PEAK", "FUTURE_OUTPUT_HASHES", "EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS"],
        "mitigations": ["REPEAT_ENVIRONMENT_AND_CAPACITY_PREFLIGHT_BEFORE_AUTHORIZATION", "USE_FINGERPRINTED_INTERPRETER", "REQUIRE_ALL_V05_ROOTS_ABSENT", "SINGLE_FUTURE_INVOCATION_NO_RETRY_NO_RESUME", "PRESERVE_FAIL_CLOSED_EVIDENCE"],
        "attempt05": "FAIL_CLOSED / AUTHORIZATION_CONSUMED", "attempt06": "NOT_AUTHORIZED / NOT_EXECUTED",
        "0B05C_METRIC_IMPACT": "NOT_DETERMINED", "0B05C_CLOSURE": "NOT_AUTHORIZED",
    }
    path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(canonical_json_bytes(payload))
    return path.relative_to(root).as_posix()
