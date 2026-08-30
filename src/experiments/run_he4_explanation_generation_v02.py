from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import ensure_parent, project_root, resolve_project_path


CONFIG_PATH = Path("src/configs/he4_pre_explainer_v0.2.json")
OUT_DIR = Path("outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2")
OLLAMA_URL = "http://127.0.0.1:11434"
PHASE_I_FILES = (
    "he4_responses_raw_v0.2.jsonl",
    "he4_responses_parsed_v0.2.jsonl",
    "he4_generation_execution_v0.2.csv",
    "he4_generation_status_v0.2.json",
    "he4_generation_metadata_v0.2.json",
    "gate_i_generation_manifest_v0.2.json",
    "summary_phase_i.md",
)
FORBIDDEN_PAYLOAD_KEYS = {
    "expected_nandina",
    "reference_code",
    "reference_rank",
    "exact_rank",
    "selection_target",
    "selection_bucket",
    "ground_truth",
    "correct_candidate",
    "correctness",
    "target",
}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _append_jsonl(path: Path, value: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def _read_jsonl_raw(path: Path) -> list[tuple[str, dict[str, Any]]]:
    rows: list[tuple[str, dict[str, Any]]] = []
    with path.open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            raw = line.rstrip("\r\n")
            if not raw:
                continue
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid generation input at line {line_number}: {exc}") from exc
            if not isinstance(parsed, dict):
                raise ValueError(f"Generation input at line {line_number} is not an object")
            rows.append((raw, parsed))
    return rows


def _walk_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield _clean(key).lower()
            yield from _walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_keys(child)


def _local_ollama_json(path: str, payload: Mapping[str, Any] | None = None, timeout: int = 300) -> dict[str, Any]:
    url = f"{OLLAMA_URL}{path}"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Local Ollama unavailable at {OLLAMA_URL}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"Unexpected local Ollama response at {path}")
    return value


def _git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *args],
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout.strip()


def _model_state(expected: Mapping[str, Any]) -> dict[str, Any]:
    tags = _local_ollama_json("/api/tags", timeout=15)
    model_name = _clean(expected["name"])
    candidates = [item for item in tags.get("models", []) if _clean(item.get("name") or item.get("model")) == model_name]
    if len(candidates) != 1:
        raise RuntimeError(f"Required local Ollama model unavailable: {model_name}. No download attempted.")
    item = candidates[0]
    details = item.get("details") if isinstance(item.get("details"), dict) else {}
    actual = {
        "name": _clean(item.get("name") or item.get("model")),
        "digest": _clean(item.get("digest")),
        "quantization": _clean(details.get("quantization_level")),
        "size_bytes": int(item.get("size") or 0),
        "context_length_available": int(details.get("context_length") or 0),
        "parameter_size": _clean(details.get("parameter_size")),
        "format": _clean(details.get("format")),
    }
    if actual["name"] != model_name:
        raise RuntimeError("Ollama model name mismatch")
    if actual["digest"] != _clean(expected["digest"]):
        raise RuntimeError("Ollama model digest mismatch")
    if actual["quantization"] != _clean(expected["quantization"]):
        raise RuntimeError("Ollama model quantization mismatch")
    version = _local_ollama_json("/api/version", timeout=15).get("version", "")
    return {"backend": "Ollama local", "ollama_url": OLLAMA_URL, "ollama_version": _clean(version), **actual}


def _top3_invariance(config: Mapping[str, Any], inputs: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]:
    root = project_root()
    historical_rows = _read_csv(resolve_project_path(config["historical_results"]["path"]))
    scores = {
        (row["case_id"], int(row["candidate_rank"])): (row["candidate_nandina"], row["score"])
        for row in historical_rows
        if row["method"] == config["historical_results"]["method"] and int(row["candidate_rank"]) <= 3
    }
    f_slots = _read_csv(resolve_project_path(config["phase_f_slots"]["path"]))
    by_case: dict[str, list[dict[str, str]]] = {}
    for row in f_slots:
        by_case.setdefault(row["case_id"], []).append(row)
    checked = 0
    for _, payload in inputs:
        case_id = _clean(payload.get("case_id"))
        candidates = payload.get("top3_original")
        if not isinstance(candidates, list) or len(candidates) != 3:
            raise ValueError(f"Invalid Top-3 for {case_id}")
        slots = sorted(by_case.get(case_id, []), key=lambda row: int(row["historical_rank"]))
        if len(slots) != 3:
            raise ValueError(f"Missing Phase F Top-3 for {case_id}")
        for candidate, slot in zip(candidates, slots, strict=True):
            rank = int(candidate.get("rank_original") or 0)
            expected = scores.get((case_id, rank))
            actual = (_clean(candidate.get("nandina")), _clean(candidate.get("score_historico")))
            phase_f = (_clean(slot["historical_candidate_code"]), _clean(slot["historical_score"]))
            if rank != int(slot["historical_rank"]) or actual != expected or actual != phase_f:
                raise ValueError(f"Phase A/F/HE4 Top-3 divergence at {case_id}/{rank}")
            if _clean(slot.get("has_exact_nandina8_evidence")) != "1":
                raise ValueError(f"Missing exact normative evidence at {case_id}/{rank}")
            checked += 1
    return {"cases": len(inputs), "slots": checked, "pass": checked == 150}


def _precheck() -> dict[str, Any]:
    root = project_root()
    config = json.loads(resolve_project_path(CONFIG_PATH).read_text(encoding="utf-8"))
    out = resolve_project_path(config["outputs"]["directory"])
    gate_h = json.loads((out / "gate_h_pre_explainer_freeze_v0.2.json").read_text(encoding="utf-8"))
    initial_head = "12acbee8d796a28df8f7b6b7a04370f65b3b8fdd"
    initial_head_is_ancestor = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", "merge-base", "--is-ancestor", initial_head, "HEAD"],
        cwd=root,
        check=False,
    ).returncode == 0
    checks: dict[str, Any] = {
        "head": _git(root, "rev-parse", "HEAD"),
        "branch": _git(root, "branch", "--show-current"),
        "initial_head_expected": initial_head,
        "initial_head_is_ancestor": initial_head_is_ancestor,
    }
    expected_hashes = gate_h["hashes"]
    paths = {
        "sample": out / "he4_explainer_sample_v0.2.csv",
        "contexts": out / "he4_contexts_v0.2.jsonl",
        "generation_inputs": out / "he4_generation_inputs_v0.2.jsonl",
        "prompt": resolve_project_path(config["prompt"]["path"]),
        "schema": resolve_project_path(config["schema"]["path"]),
        "rubric": resolve_project_path(config["rubric"]["path"]),
    }
    checks["hashes"] = {name: {"expected": expected_hashes[name], "actual": _sha256(path), "pass": expected_hashes[name] == _sha256(path)} for name, path in paths.items()}
    sample = _read_csv(paths["sample"])
    inputs = _read_jsonl_raw(paths["generation_inputs"])
    checks["sample_cases"] = len(sample)
    checks["generation_inputs"] = len(inputs)
    checks["unique_case_ids"] = len({_clean(payload.get("case_id")) for _, payload in inputs})
    checks["contexts_inputs_byte_identical"] = paths["contexts"].read_bytes() == paths["generation_inputs"].read_bytes()
    forbidden = sorted({key for _, payload in inputs for key in _walk_keys(payload) if key in FORBIDDEN_PAYLOAD_KEYS})
    checks["forbidden_payload_keys"] = forbidden
    checks["top3_invariance"] = _top3_invariance(config, inputs)
    checks["model"] = _model_state(config["model"])
    checks["parameters"] = {
        "explicit": {key: value for key, value in config["model"]["parameters"].items() if value is not None},
        "backend_default_or_unspecified": [key for key, value in config["model"]["parameters"].items() if value is None],
        "retry_policy": config["model"]["parameters"]["retry_policy"],
    }
    checks["phase_g_or_evaluation_only_loaded"] = False
    checks["retrieval_performed"] = False
    passed = (
        checks["branch"] == "codex/exp04-rerun-v02"
        and checks["initial_head_is_ancestor"]
        and all(item["pass"] for item in checks["hashes"].values())
        and checks["sample_cases"] == 50
        and checks["generation_inputs"] == 50
        and checks["unique_case_ids"] == 50
        and checks["contexts_inputs_byte_identical"]
        and not forbidden
        and checks["top3_invariance"]["pass"]
        and checks["top3_invariance"]["slots"] == 150
        and checks["model"]["context_length_available"] >= int(config["model"]["parameters"]["num_ctx"])
    )
    return {"version": "gate_i_pre_generation_check_v0.2", "created_at_utc": datetime.now(timezone.utc).isoformat(), "passed": passed, "checks": checks}


def _write_precheck(precheck: Mapping[str, Any]) -> Path:
    path = resolve_project_path(OUT_DIR) / "gate_i_pre_generation_check_v0.2.json"
    _write_json(path, precheck)
    return path


def _assert_no_phase_i_overwrite(out: Path) -> None:
    existing = [name for name in PHASE_I_FILES if (out / name).exists()]
    if existing:
        raise FileExistsError(f"Refusing to overwrite Phase I artifacts: {', '.join(existing)}")


def _parse_json_object(raw: str) -> tuple[dict[str, Any] | None, str]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, str(exc)
    return (value, "") if isinstance(value, dict) else (None, "top-level JSON is not an object")


def _generate(prompt: str, raw_payload: str, config: Mapping[str, Any]) -> tuple[dict[str, Any], float]:
    parameters = config["model"]["parameters"]
    request = {
        "model": config["model"]["name"],
        "prompt": prompt + "\n\n" + raw_payload,
        "stream": parameters["stream"],
        "format": parameters["format"],
        "options": {"temperature": parameters["temperature"], "num_ctx": parameters["num_ctx"]},
    }
    started = time.perf_counter()
    response = _local_ollama_json("/api/generate", request, timeout=int(parameters["timeout_seconds"]))
    return response, time.perf_counter() - started


def _runtime_environment(model: Mapping[str, Any]) -> dict[str, Any]:
    try:
        loaded = _local_ollama_json("/api/ps", timeout=15).get("models", [])
    except RuntimeError:
        loaded = []
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "os_name": os.name,
        "machine": platform.machine(),
        "processor": platform.processor(),
        "device": loaded,
        "model": model,
    }


def _output_hashes(out: Path) -> dict[str, str]:
    return {name: _sha256(out / name) for name in PHASE_I_FILES if name != "gate_i_generation_manifest_v0.2.json" and (out / name).is_file()}


def _summary(metadata: Mapping[str, Any], status: Mapping[str, Any], hashes: Mapping[str, str]) -> str:
    lines = [
        "# EXP-04 Fase I - Generacion controlada Top-3 HE4 v0.2",
        "",
        "## Freeze y modelo",
        "",
        f"- Freeze H: `{metadata['freeze_hashes']['generation_inputs']}`.",
        f"- Prompt: `{metadata['prompt']['path']}` (`{metadata['prompt']['sha256']}`).",
        f"- Modelo: `{metadata['model']['name']}` (`{metadata['model']['digest']}`, `{metadata['model']['quantization']}`).",
        f"- Backend: `{metadata['model']['backend']}`; Ollama `{metadata['model']['ollama_version']}`.",
        "",
        "## Ejecucion",
        "",
        f"- Inputs: {status['inputs']}.",
        f"- Llamadas intentadas/completadas: {status['calls_attempted']}/{status['calls_completed']}.",
        f"- Fallos tecnicos: {status['technical_failures']}; retries: {status['retries']}.",
        f"- Raw preservadas: {status['raw_responses_stored']}.",
        f"- JSON parseable/no parseable: {status['parseable_json']}/{status['non_parseable_json']}.",
        f"- Latencia total: {status['latency_total_seconds']:.3f}s.",
        "",
        "## Provenance",
        "",
        "- Una ejecucion primaria por input en el orden congelado; sin recuperacion, etiquetas, evaluation-only ni Fase G.",
        "- El parseo es tecnico y no reparo respuestas ni aplico controles HE4, rubrica o evaluacion cualitativa.",
        "- Hashes de outputs (el manifiesto excluye su propio hash):",
    ]
    lines.extend(f"  - `{name}`: `{value}`." for name, value in sorted(hashes.items()))
    lines.extend(["", "## Limitaciones", "", "- HE4 permanece pendiente de validacion automatica y evaluacion cualitativa.", "- Fase J/K no fue ejecutada.", ""])
    return "\n".join(lines)


def run(precheck_only: bool) -> int:
    precheck = _precheck()
    precheck_path = _write_precheck(precheck)
    if not precheck["passed"]:
        raise RuntimeError(f"Gate I pre-generation not approved: {precheck_path}")
    if precheck_only:
        print(json.dumps({"gate": str(precheck_path), "passed": True}, ensure_ascii=False))
        return 0

    root = project_root()
    config = json.loads(resolve_project_path(CONFIG_PATH).read_text(encoding="utf-8"))
    out = resolve_project_path(config["outputs"]["directory"])
    _assert_no_phase_i_overwrite(out)
    prompt_path = resolve_project_path(config["prompt"]["path"])
    prompt = prompt_path.read_text(encoding="utf-8")
    inputs = _read_jsonl_raw(out / "he4_generation_inputs_v0.2.jsonl")
    raw_path = out / "he4_responses_raw_v0.2.jsonl"
    parsed_path = out / "he4_responses_parsed_v0.2.jsonl"
    executions: list[dict[str, Any]] = []
    started = time.perf_counter()
    technical_failure = ""
    for sequence, (raw_payload, payload) in enumerate(inputs, start=1):
        case_id = _clean(payload.get("case_id"))
        timestamp = datetime.now(timezone.utc).isoformat()
        input_hash = _sha256_text(raw_payload)
        try:
            response, latency = _generate(prompt, raw_payload, config)
            raw_response = response.get("response")
            if not isinstance(raw_response, str):
                raise RuntimeError("Ollama response has no string response field")
            parsed, parse_error = _parse_json_object(raw_response)
            parse_status = "parsed_json_object" if parsed is not None else "non_parseable_json"
            completed = True
        except Exception as exc:  # Preserve the technical failure as the campaign stopping point.
            response, latency, raw_response, parsed = {}, 0.0, None, None
            parse_error, parse_status, completed = f"{type(exc).__name__}: {exc}", "technical_failure", False
            technical_failure = f"{case_id}: {parse_error}"
        raw_record = {
            "case_id": case_id,
            "generation_sequence": sequence,
            "timestamp_utc": timestamp,
            "model": config["model"]["name"],
            "model_digest": config["model"]["digest"],
            "prompt_hash": _sha256(prompt_path),
            "input_hash": input_hash,
            "parameters": config["model"]["parameters"],
            "latency_seconds": latency,
            "raw_response": raw_response,
            "ollama_metadata": {key: value for key, value in response.items() if key != "response"},
        }
        _append_jsonl(raw_path, raw_record)
        _append_jsonl(parsed_path, {**{key: raw_record[key] for key in ("case_id", "generation_sequence", "timestamp_utc", "model", "model_digest", "prompt_hash", "input_hash")}, "parse_status": parse_status, "parse_error": parse_error, "parsed_response": parsed})
        executions.append({
            "case_id": case_id,
            "generation_sequence": sequence,
            "attempt_count": 1,
            "retry_reason": "",
            "timestamp_utc": timestamp,
            "model": config["model"]["name"],
            "model_digest": config["model"]["digest"],
            "prompt_hash": _sha256(prompt_path),
            "input_hash": input_hash,
            "status": "completed" if completed else "technical_failure",
            "parse_status": parse_status,
            "parse_error": parse_error,
            "latency_seconds": latency,
            "prompt_eval_count": response.get("prompt_eval_count", ""),
            "eval_count": response.get("eval_count", ""),
        })
        print(f"{sequence}/50 {case_id} {executions[-1]['status']} {parse_status}", flush=True)
        if not completed:
            break

    _write_csv(out / "he4_generation_execution_v0.2.csv", executions, list(executions[0]) if executions else [])
    completed = sum(row["status"] == "completed" for row in executions)
    parseable = sum(row["parse_status"] == "parsed_json_object" for row in executions)
    latencies = [float(row["latency_seconds"]) for row in executions if row["status"] == "completed"]
    status = {
        "version": "he4_generation_status_v0.2",
        "status": "completed" if completed == 50 else "interrupted_technical_failure",
        "inputs": 50,
        "calls_attempted": len(executions),
        "calls_completed": completed,
        "technical_failures": len(executions) - completed,
        "raw_responses_stored": completed,
        "parseable_json": parseable,
        "non_parseable_json": completed - parseable,
        "retries": 0,
        "latency_total_seconds": sum(latencies),
        "latency_mean_seconds": statistics.mean(latencies) if latencies else 0.0,
        "latency_median_seconds": statistics.median(latencies) if latencies else 0.0,
        "prompt_tokens_reported": sum(int(row["prompt_eval_count"] or 0) for row in executions),
        "completion_tokens_reported": sum(int(row["eval_count"] or 0) for row in executions),
        "technical_failure_detail": technical_failure,
    }
    _write_json(out / "he4_generation_status_v0.2.json", status)
    metadata = {
        "version": "he4_generation_metadata_v0.2",
        "phase": "EXP-04 FASE I",
        "branch": _git(root, "branch", "--show-current"),
        "head": _git(root, "rev-parse", "HEAD"),
        "freeze_hashes": precheck["checks"]["hashes"],
        "prompt": {"path": config["prompt"]["path"], "sha256": _sha256(prompt_path)},
        "model": precheck["checks"]["model"],
        "parameters": precheck["checks"]["parameters"],
        "runtime": _runtime_environment(precheck["checks"]["model"]),
        "generation_order": "he4_generation_inputs_v0.2.jsonl source order",
        "no_label_or_evaluation_only_loaded": True,
        "no_phase_g_loaded": True,
        "no_retrieval_performed": True,
        "status": status,
    }
    _write_json(out / "he4_generation_metadata_v0.2.json", metadata)
    hashes = _output_hashes(out)
    large = [{"path": name, "size_bytes": (out / name).stat().st_size} for name in hashes if (out / name).stat().st_size > 25 * 1024 * 1024]
    over_50 = [item for item in large if item["size_bytes"] > 50 * 1024 * 1024]
    (out / "summary_phase_i.md").write_text(_summary(metadata, status, hashes), encoding="utf-8", newline="\n")
    hashes = _output_hashes(out)
    manifest = {
        "version": "gate_i_generation_manifest_v0.2",
        "gate_i": "APPROVED" if completed == 50 and not over_50 else "NOT_APPROVED",
        "he4_status": "PENDING AUTOMATIC VALIDATION / QUALITATIVE EVALUATION",
        "pre_generation_gate": precheck,
        "generation_status": status,
        "output_sha256": hashes,
        "outputs_over_25_mib": large,
        "outputs_over_50_mib": over_50,
        "manifest_self_hash_excluded": True,
        "phase_j_or_k_executed": False,
    }
    _write_json(out / "gate_i_generation_manifest_v0.2.json", manifest)
    print(json.dumps({"gate_i": manifest["gate_i"], "status": status["status"], "completed": completed}, ensure_ascii=False))
    return 0 if manifest["gate_i"] == "APPROVED" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="EXP-04 Fase I controlled HE4 Top-3 explanation generation.")
    parser.add_argument("--precheck-only", action="store_true")
    args = parser.parse_args()
    return run(args.precheck_only)


if __name__ == "__main__":
    raise SystemExit(main())
