"""Deterministic prospective orchestration for the D1a 0B-05C correction.

Default and --preflight modes are read-only. They never write a corpus, load a
model, build vectors, run retrieval, or calculate metrics.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = "src/experiments/run_d1a_corrective_0b05c_v01.py"
BUILDER_PATH = "src/experiments/build_text2trade_mnrl_index_v02.py"
EVALUATOR_PATH = "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py"
AUDIT_SPEC_PATH = "outputs/audits/d1a_preexecution_0b05c_v0.1/d1a_0b05c_corrective_execution_spec_v0.1.json"

BUILDER_FILENAMES = (
    "index/vectors.npy",
    "index/id_map.json",
    "store/nandina8_docstore.jsonl",
    "retrieval_config.json",
    "vector_integrity_sample_v0.2.csv",
    "vector_integrity_gate_v0.2.json",
    "text2trade_mnrl_nandina8_v02_run_metadata.json",
)
EVALUATOR_FILENAMES = (
    "d1a_metrics.json",
    "d1a_case_summary.csv",
    "d1a_ranked_codes_top200.jsonl",
    "strategy_comparison_a_b_c_d0_d1a_v0.2.csv",
    "summary.md",
)
RUNNER_FILENAMES = (
    "d1a_corrective_vs_original_comparison_v0.1.json",
    "d1a_corrective_case_level_comparison_v0.1.jsonl",
    "d1a_corrective_output_hash_ledger_v0.1.csv",
    "d1a_corrective_execution_manifest_v0.1.json",
)
METRIC_SPECS = (
    ("Top@1", "top_1"), ("Top@3", "top_3"), ("Top@5", "top_5"), ("Top@10", "top_10"),
    ("Top@50", "top_50"), ("Recall@100", "recall_at_100"), ("Recall@200", "recall_at_200"),
    ("MRR@100", "mrr_at_100"), ("MRR@200", "mrr_at_200"), ("Exact@100", "exact_at_100"),
    ("Exact@200", "exact_at_200"), ("HS6@100", "hs6_at_100"), ("HS6@200", "hs6_at_200"),
    ("HS4@100", "hs4_at_100"), ("HS4@200", "hs4_at_200"), ("Chapter@100", "chapter_at_100"),
    ("Chapter@200", "chapter_at_200"),
)


class ContractViolation(RuntimeError):
    """Raised for fail-closed 0B-05C contract violations."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(payload, dict), f"Expected JSON object: {path}")
    return payload


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    require(not path.exists(), f"Refusing to overwrite contractual artifact: {path}")
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def project_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes project root: {relative}")
    return path


def relative_path(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def git_hash_object(root: Path, relative: str) -> str:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), "hash-object", relative],
        check=False,
        capture_output=True,
        text=True,
    )
    require(result.returncode == 0, f"Cannot hash code identity {relative}: {result.stderr.strip()}")
    return result.stdout.strip()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def future_roots(spec: Mapping[str, Any]) -> tuple[str, ...]:
    roots = spec["orchestration"]["future_roots"]
    require(isinstance(roots, list) and roots, "Execution specification has no prospective roots")
    return tuple(str(item) for item in roots)


def validate_code_identity(root: Path, identity: Mapping[str, Any]) -> None:
    relative = str(identity["path"])
    path = project_path(root, relative)
    require(path.is_file(), f"Required code path is missing: {relative}")
    require(git_hash_object(root, relative) == identity["git_blob_sha"], f"Git blob identity changed: {relative}")
    if identity["revision"] == "MICROCLOSE_WORKTREE_CONTENT":
        require(sha256_file(path) == identity["sha256"], f"Runner worktree SHA changed: {relative}")


def validate_patch_contract(spec: Mapping[str, Any]) -> None:
    definition = spec["corrected_normative_corpus"]["definition"]
    authority = definition["authoritative_normative_source"]
    require(authority["decision"] == "Decision 906", "Normative decision changed")
    require(authority["official_gazette"] == "Gaceta Oficial 5062", "Normative gazette changed")
    require(authority["annex_entries"]["87044110"]["text"] == "Inferior a 4,537 t", "Decision 906 text changed for 87044110")
    require(authority["annex_entries"]["87045110"]["text"] == "Inferior a 4,537 t", "Decision 906 text changed for 87045110")
    patches = definition["patches"]
    require(definition["patch_scope"] == "EXACTLY_TWO_NANDINA8_DOCUMENTS", "Patch scope changed")
    require([item["code"] for item in patches] == ["87044110", "87045110"], "Patched codes changed")
    for patch in patches:
        replacement = patch["replacement"]
        require(replacement["titulo"] == "Inferior a 4,537 t", f"Title changed for {patch['code']}")
        require(replacement["texto_index"] == "Inferior a 4,537 t.", f"Index text changed for {patch['code']}")
        require(replacement["texto"] == "Inferior a 4,537 t. Contexto: Sección XVII / Capítulo 87.", f"Synthetic context changed for {patch['code']}")
        require(replacement["version"] == "Decision_906", f"Version changed for {patch['code']}")


def patched_corpus_bytes(original: bytes, spec: Mapping[str, Any]) -> bytes:
    """Apply the two frozen JSONL patches in memory with deterministic UTF-8 LF."""

    validate_patch_contract(spec)
    patches = {item["code"]: item for item in spec["corrected_normative_corpus"]["definition"]["patches"]}
    seen: set[str] = set()
    output: list[bytes] = []
    for raw_line in original.splitlines():
        payload = json.loads(raw_line)
        code = str(payload.get("codigo", "")).strip()
        patch = patches.get(code)
        if patch is None:
            output.append(raw_line)
            continue
        require(sha256_bytes(raw_line) == patch["match"]["original_jsonl_line_sha256"], f"Original JSONL line SHA changed for {code}")
        require(payload.get("doc_id") == patch["match"]["doc_id"] and payload.get("version") == patch["match"]["version"], f"Original document identity changed for {code}")
        payload.update(patch["replacement"])
        output.append(json.dumps(payload, ensure_ascii=False, separators=(", ", ": ")).encode("utf-8"))
        seen.add(code)
    require(seen == set(patches), "One or more frozen corrective patches did not match")
    return b"\n".join(output) + b"\n"


def diff_paths(left: Any, right: Any, prefix: str = "") -> set[str]:
    if isinstance(left, dict) and isinstance(right, dict):
        result: set[str] = set()
        for key in sorted(set(left) | set(right)):
            name = f"{prefix}.{key}" if prefix else str(key)
            result |= diff_paths(left.get(key), right.get(key), name)
        return result
    return set() if left == right else {prefix}


def derive_runtime_config(original: Mapping[str, Any], spec: Mapping[str, Any], corrected_sha: str) -> dict[str, Any]:
    runtime = copy.deepcopy(original)
    derivation = spec["orchestration"]["config_derivation"]
    runtime["frozen_inputs"]["normative_corpus"] = derivation["corrected_normative_corpus_path"]
    runtime["frozen_inputs"]["normative_corpus_sha256"] = corrected_sha
    runtime["index"]["output_dir"] = derivation["corrected_index_root"]
    runtime["outputs"]["evaluation_dir"] = derivation["corrected_evaluation_root"]
    allowed = {
        "frozen_inputs.normative_corpus",
        "frozen_inputs.normative_corpus_sha256",
        "index.output_dir",
        "outputs.evaluation_dir",
    }
    require(diff_paths(original, runtime) == allowed, "Derived runtime config differs beyond the frozen derivation rule")
    return runtime


def validate_contract_inputs(root: Path, spec: Mapping[str, Any]) -> dict[str, Path]:
    original = spec["original_normative_corpus"]
    corpus_path = project_path(root, str(original["path"]))
    require(sha256_file(corpus_path) == original["sha256"], "Original normative corpus SHA changed")
    model = spec["model_policy"]["weights"]
    model_path = project_path(root, str(model["path"]))
    require(model_path.is_file() and sha256_file(model_path) == model["sha256"], "Frozen D1a model SHA changed")
    evaluation = spec["evaluation"]["eval_input"]
    eval_path = project_path(root, str(evaluation["path"]))
    require(sha256_file(eval_path) == evaluation["sha256"], "Frozen EVAL SHA changed")
    for item in (
        spec["evaluation"]["primary_control"],
        spec["evaluation"]["primary_control_case_summary"],
        spec["evaluation"]["primary_control_ranking_trace"],
    ):
        path = project_path(root, str(item["path"]))
        require(sha256_file(path) == item["sha256"], f"Primary control SHA changed: {item['path']}")
    for identity in (spec["orchestration"]["runner"], spec["index_builder"]["code_identity"], spec["evaluation"]["code_identity"]):
        validate_code_identity(root, identity)
    for prospective_root in future_roots(spec):
        require(not project_path(root, prospective_root).exists(), f"Prospective root already exists: {prospective_root}")
    return {"corpus": corpus_path, "eval": eval_path}


def preflight_provenance(corrected_sha: str, derived_config_sha: str, prospective_roots: Iterable[str]) -> dict[str, Any]:
    """Construct the immutable read-only provenance returned by preflight."""

    return {
        "status": "PASS", "preflight_status": "PASS", "mode": "PREFLIGHT_ONLY",
        "execution_mode": "PREFLIGHT_ONLY", "numerical_execution_occurred": False,
        "corrected_corpus_sha256": corrected_sha,
        "derived_config_sha256": derived_config_sha,
        "prospective_roots_absent": list(prospective_roots), "retrieval_executed": False,
        "corrected_corpus_created": False, "corrected_index_created": False, "new_metrics_computed": False,
    }


def preflight(root: Path = ROOT) -> dict[str, Any]:
    """Validate all bindings without creating any file or loading any model."""

    spec = load_json(project_path(root, AUDIT_SPEC_PATH))
    require(spec["specification_status"] == "CLOSED_PROSPECTIVELY", "Execution specification is not closed prospectively")
    inputs = validate_contract_inputs(root, spec)
    validate_patch_contract(spec)
    corrected_sha = sha256_bytes(patched_corpus_bytes(inputs["corpus"].read_bytes(), spec))
    config_identity = spec["orchestration"]["original_config"]
    config_path = project_path(root, str(config_identity["path"]))
    require(sha256_file(config_path) == config_identity["sha256"], "Original frozen config SHA changed")
    runtime = derive_runtime_config(load_json(config_path), spec, corrected_sha)
    return preflight_provenance(
        corrected_sha,
        sha256_bytes((json.dumps(runtime, ensure_ascii=False, indent=2) + "\n").encode("utf-8")),
        future_roots(spec),
    )


def require_numerical_authorization(spec: Mapping[str, Any]) -> None:
    """Fail closed unless a separately approved future commit authorizes execution."""

    authorization = spec.get("authorization")
    state = authorization.get("D1A_NUMERICAL_EXECUTION") if isinstance(authorization, Mapping) else None
    require(state == "AUTHORIZED", f"Numerical execution is not authorized: {state!r}")


def expected_paths(root: Path, spec: Mapping[str, Any]) -> dict[str, list[Path]]:
    derivation = spec["orchestration"]["config_derivation"]
    index_root = project_path(root, derivation["corrected_index_root"])
    evaluation_root = project_path(root, derivation["corrected_evaluation_root"])
    return {
        "index": [index_root / item for item in BUILDER_FILENAMES],
        "evaluation": [evaluation_root / item for item in EVALUATOR_FILENAMES],
        "runner": [evaluation_root / item for item in RUNNER_FILENAMES],
    }


def require_all(paths: Iterable[Path], label: str) -> None:
    missing = [str(path) for path in paths if not path.is_file()]
    require(not missing, f"Missing {label} contractual outputs: {missing}")


def read_case_csv(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    require(rows and all(row.get("case_id") for row in rows), f"Invalid case-level output: {path}")
    return {str(row["case_id"]): row for row in rows}


def rank_of(codes: list[str], code: str) -> int:
    return next((rank for rank, candidate in enumerate(codes, 1) if candidate == code), 0)


def build_case_comparison(root: Path, spec: Mapping[str, Any]) -> list[dict[str, Any]]:
    original_case = read_case_csv(project_path(root, spec["evaluation"]["primary_control_case_summary"]["path"]))
    corrected_case = read_case_csv(project_path(root, f"{spec['evaluation']['prospective_output_root']}/d1a_case_summary.csv"))
    original_trace = {str(row["case_id"]): list(row["candidate_codes"]) for row in read_jsonl(project_path(root, spec["evaluation"]["primary_control_ranking_trace"]["path"]))}
    corrected_trace = {str(row["case_id"]): list(row["candidate_codes"]) for row in read_jsonl(project_path(root, f"{spec['evaluation']['prospective_output_root']}/d1a_ranked_codes_top200.jsonl"))}
    require(set(original_case) == set(corrected_case) == set(original_trace) == set(corrected_trace), "Case-level comparison inputs are not aligned")
    rows = []
    for case_id in sorted(original_case):
        before, after = original_case[case_id], corrected_case[case_id]
        before_codes, after_codes = original_trace[case_id], corrected_trace[case_id]
        row: dict[str, Any] = {
            "case_id": case_id, "nandina_ref": before["nandina_ref"], "original_rank_ref": int(before["rank_ref"]),
            "corrected_rank_ref": int(after["rank_ref"]), "ranking_changed": before_codes != after_codes,
            "rank_convention": "0=NOT_FOUND_AT_200",
        }
        for k in (1, 3, 5, 10, 50, 100, 200):
            row[f"original_found_at_{k}"] = int(1 <= row["original_rank_ref"] <= k)
            row[f"corrected_found_at_{k}"] = int(1 <= row["corrected_rank_ref"] <= k)
            row[f"original_hit_{k}"] = row[f"original_found_at_{k}"]
            row[f"corrected_hit_{k}"] = row[f"corrected_found_at_{k}"]
        for code in ("87044110", "87045110"):
            row[f"original_rank_{code}"] = rank_of(before_codes, code)
            row[f"corrected_rank_{code}"] = rank_of(after_codes, code)
            row[f"corrected_contains_{code}"] = row[f"corrected_rank_{code}"] > 0
        required_fields = set(spec["orchestration"]["comparison_contract"]["case_fields"])
        require(required_fields <= set(row), f"Case-level producer omitted contractual fields: {sorted(required_fields - set(row))}")
        rows.append(row)
    return rows


def build_aggregate_comparison(root: Path, spec: Mapping[str, Any]) -> dict[str, Any]:
    original = load_json(project_path(root, spec["evaluation"]["primary_control"]["path"]))["metrics"]
    corrected = load_json(project_path(root, f"{spec['evaluation']['prospective_output_root']}/d1a_metrics.json"))["metrics"]
    rows = []
    for label, key in METRIC_SPECS:
        denominator_key, numerator_key = f"{key}_denominator", f"{key}_numerator"
        denominator = original[denominator_key]
        require(corrected[denominator_key] == denominator, f"Metric denominator changed for {label}")
        rows.append({
            "metric": label, "original_numerator": original[numerator_key], "corrected_numerator": corrected[numerator_key],
            "denominator": denominator, "original_value": original[key], "corrected_value": corrected[key],
            "absolute_delta": corrected[key] - original[key],
        })
    return {
        "comparison_id": "d1a_corrective_vs_original_v0.1", "primary_control": spec["evaluation"]["primary_control"],
        "rank_convention": "0=NOT_FOUND_AT_200", "metrics": rows,
    }


def contractual_ledger_paths(root: Path, spec: Mapping[str, Any]) -> list[Path]:
    paths = expected_paths(root, spec)
    expected = [
        project_path(root, spec["corrected_normative_corpus"]["prospective_path"]),
        project_path(root, spec["orchestration"]["runtime_config_path"]),
        *paths["index"], *paths["evaluation"], paths["runner"][0], paths["runner"][1], paths["runner"][3],
    ]
    contract = spec["orchestration"]["hash_ledger_contract"]
    ledger = paths["runner"][2]
    declared = [project_path(root, relative) for relative in contract["included_paths"]]
    require(declared == expected, "Frozen hash-ledger contract differs from actual orchestration paths")
    require(project_path(root, contract["excluded_self_path"]) == ledger, "Hash ledger self-exclusion is not frozen")
    require(ledger not in declared and len(declared) == len(set(declared)), "Hash-ledger contract is not unique or excludes more than itself")
    return declared


def write_hash_ledger(root: Path, spec: Mapping[str, Any]) -> Path:
    paths = expected_paths(root, spec)
    contractual = contractual_ledger_paths(root, spec)
    require_all(contractual, "hash ledger")
    ledger = paths["runner"][2]
    require(not ledger.exists(), f"Refusing to overwrite contractual artifact: {ledger}")
    rows = [{"path": relative_path(root, path), "sha256": sha256_file(path), "size_bytes": path.stat().st_size} for path in contractual]
    write_csv(ledger, rows, ["path", "sha256", "size_bytes"])
    return ledger


def authorized_execution_provenance(preflight_proof: Mapping[str, Any]) -> dict[str, Any]:
    """Return the distinct, future-only state after an authorized numerical run."""

    require(preflight_proof["mode"] == "PREFLIGHT_ONLY", "Authorized execution must start from preflight proof")
    return {
        **preflight_proof,
        "status": "PASS",
        "preflight_status": preflight_proof["status"],
        "mode": "AUTHORIZED_EXECUTION",
        "execution_mode": "AUTHORIZED_EXECUTION",
        "numerical_execution_occurred": True,
        "retrieval_executed": True,
        "corrected_corpus_created": True,
        "corrected_index_created": True,
        "new_metrics_computed": True,
    }


def build_execution_manifest(root: Path, spec: Mapping[str, Any], preflight_proof: Mapping[str, Any]) -> dict[str, Any]:
    """Describe an authorized run without creating a circular ledger hash dependency."""

    execution = authorized_execution_provenance(preflight_proof)
    ledger = expected_paths(root, spec)["runner"][2]
    return {
        "status": execution["status"],
        "preflight_status": execution["preflight_status"],
        "execution_mode": execution["execution_mode"],
        "numerical_execution_occurred": execution["numerical_execution_occurred"],
        "hash_ledger": {"path": relative_path(root, ledger), "sha256": None},
    }


def execute_authorized(root: Path = ROOT) -> dict[str, Any]:
    """Perform the pre-frozen numerical sequence only after separate authorization."""

    spec = load_json(project_path(root, AUDIT_SPEC_PATH))
    require_numerical_authorization(spec)
    proof = preflight(root)
    derivation = spec["orchestration"]["config_derivation"]
    corrected_path = project_path(root, spec["corrected_normative_corpus"]["prospective_path"])
    runtime_root = project_path(root, spec["orchestration"]["runtime_root"])
    runtime_config = project_path(root, spec["orchestration"]["runtime_config_path"])
    try:
        with corrected_path.open("xb") as handle:
            handle.write(patched_corpus_bytes(project_path(root, spec["original_normative_corpus"]["path"]).read_bytes(), spec))
        runtime_root.mkdir(parents=True)
        runtime = derive_runtime_config(load_json(project_path(root, derivation["original_config_path"])), spec, proof["corrected_corpus_sha256"])
        write_json(runtime_config, runtime)
        config_arg = relative_path(root, runtime_config)
        for module in ("src.experiments.build_text2trade_mnrl_index_v02", "src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02"):
            subprocess.run([sys.executable, "-B", "-m", module, "--config", config_arg], cwd=root, check=True)
        paths = expected_paths(root, spec)
        require_all(paths["index"], "builder")
        require_all(paths["evaluation"], "evaluator")
        write_json(paths["runner"][0], build_aggregate_comparison(root, spec))
        write_jsonl(paths["runner"][1], build_case_comparison(root, spec))
        write_json(paths["runner"][3], build_execution_manifest(root, spec, proof))
        ledger = write_hash_ledger(root, spec)
        require(ledger.is_file(), "Hash ledger was not materialized")
        return authorized_execution_provenance(proof)
    except Exception as error:
        if runtime_root.exists():
            (runtime_root / "execution_failed.json").write_text(json.dumps({"status": "FAILED", "error": str(error)}, ensure_ascii=False) + "\n", encoding="utf-8")
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description="0B-05C D1a corrective orchestration.")
    parser.add_argument("--preflight", action="store_true", help="Read-only contract validation.")
    parser.add_argument("--execute-authorized", action="store_true", help="Numerical execution; requires separate authorization.")
    args = parser.parse_args()
    require(not (args.preflight and args.execute_authorized), "Choose one execution mode")
    result = execute_authorized(ROOT) if args.execute_authorized else preflight(ROOT)
    print(f"STATUS={result['status']}")
    print(f"MODE={result['mode'] if 'mode' in result else 'AUTHORIZED_EXECUTION'}")
    print(f"CORRECTED_CORPUS_SHA256={result['corrected_corpus_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
