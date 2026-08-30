from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import random
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..utils.paths import project_root, resolve_project_path


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256(path)
    if actual != expected:
        raise ValueError(f"{label} SHA-256 mismatch: {actual} != {expected}")


def read_selected_csv(path: Path, fields: Sequence[str]) -> list[dict[str, str]]:
    """Read only named columns, so labels in source CSVs never enter pre-LLM memory."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        if not header:
            raise ValueError(f"CSV without header: {path}")
        positions = {field: header.index(field) for field in fields if field in header}
        missing = sorted(set(fields) - set(positions))
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")
        return [{field: clean(row[positions[field]]) if positions[field] < len(row) else "" for field in fields} for row in reader]


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{number}") from exc
    return rows


def relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def git_value(root: Path, *args: str) -> str:
    try:
        return subprocess.run(
            ["git", "-c", f"safe.directory={root.as_posix()}", *args], cwd=root, check=True,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def paths(config: Mapping[str, Any], root: Path) -> dict[str, Path]:
    directory = resolve_project_path(config["outputs"]["directory"])
    return {
        "directory": directory,
        "pool": directory / "reranker_candidate_pool_v0.2.csv",
        "sample": directory / "reranker_diagnostic_sample_v0.2.csv",
        "inputs": directory / "reranker_inputs_v0.2.jsonl",
        "outputs": directory / "reranker_outputs_v0.2.jsonl",
        "case_results": directory / "reranker_case_results_v0.2.csv",
        "metrics": directory / "reranker_metrics_v0.2.json",
        "win_tie_loss": directory / "reranker_win_tie_loss_v0.2.json",
        "position_changes": directory / "reranker_position_changes_v0.2.csv",
        "closure": directory / "reranker_candidate_closure_audit_v0.2.json",
        "label_audit": directory / "reranker_label_leakage_audit_v0.2.json",
        "compatibility": directory / "reranker_compatibility_v0.2.json",
        "metadata": directory / "reranker_run_metadata_v0.2.json",
        "gate_json": directory / "gate_g_pre_llm_freeze_v0.2.json",
        "gate_md": directory / "gate_g_pre_llm_freeze_v0.2.md",
        "summary": directory / "summary.md",
    }


def source_paths(config: Mapping[str, Any]) -> list[tuple[Path, str, str]]:
    values = [
        (resolve_project_path(config["eval"]["path"]), config["eval"]["sha256"], "evalset"),
        (resolve_project_path(config["pool"]["historical_results"]["path"]), config["pool"]["historical_results"]["sha256"], "historical results"),
        (resolve_project_path(config["pool"]["normative_pool"]["path"]), config["pool"]["normative_pool"]["sha256"], "approved normative pool"),
    ]
    for name, item in config["frozen_phase_artifacts"].items():
        values.append((resolve_project_path(item["path"]), item["sha256"], name))
    return values


def verify_sources(config: Mapping[str, Any]) -> None:
    for path, expected, label in source_paths(config):
        assert_hash(path, expected, label)


def load_pool_without_labels(config: Mapping[str, Any]) -> tuple[dict[str, list[dict[str, Any]]], dict[str, str]]:
    """Build the historic 80 -> normative -> remaining historic construction."""
    historical_cfg = config["pool"]["historical_results"]
    norm_cfg = config["pool"]["normative_pool"]
    hist_rows = read_selected_csv(
        resolve_project_path(historical_cfg["path"]),
        ["case_id", "candidate_rank", "candidate_nandina", "score", "method"],
    )
    norm_rows = read_selected_csv(
        resolve_project_path(norm_cfg["path"]),
        ["pool_id", "classification", "case_id", "depth", "candidate_codes", "effective_size"],
    )
    historical: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in hist_rows:
        if row["method"] != historical_cfg["method"]:
            continue
        code = row["candidate_nandina"]
        if len(code) == 8 and code.isdigit():
            historical[row["case_id"]].append({"code": code, "rank": int(row["candidate_rank"]), "score": row["score"]})
    for candidates in historical.values():
        candidates.sort(key=lambda item: int(item["rank"]))
    normative: dict[str, list[str]] = {}
    for row in norm_rows:
        if row["pool_id"] != norm_cfg["pool_id"] or row["classification"] != "candidate_pool" or int(row["depth"]) != int(norm_cfg["depth"]):
            continue
        codes = [code for code in row["candidate_codes"].split("|") if len(code) == 8 and code.isdigit()]
        if len(codes) != len(set(codes)):
            raise ValueError(f"Duplicate normative candidate code for {row['case_id']}")
        normative[row["case_id"]] = codes
    if set(historical) != set(normative):
        raise ValueError("Historical and normative pool case ID sets differ")
    protected = int(config["pool"]["protected_historical_candidates"])
    depth = int(config["pool"]["depth"])
    output: dict[str, list[dict[str, Any]]] = {}
    descriptions: dict[str, str] = {}
    for case_id in sorted(historical):
        hist = historical[case_id]
        norm = normative[case_id]
        hist_by_code = {item["code"]: item for item in hist}
        norm_rank = {code: position for position, code in enumerate(norm, 1)}
        ordered = [item["code"] for item in hist[:protected]] + norm + [item["code"] for item in hist[protected:]]
        seen: set[str] = set()
        candidates: list[dict[str, Any]] = []
        for code in ordered:
            if code in seen:
                continue
            seen.add(code)
            sources: list[str] = []
            ranks: list[str] = []
            if code in hist_by_code:
                sources.append("historical")
                ranks.append(f"historical:{hist_by_code[code]['rank']}")
            if code in norm_rank:
                sources.append("normative_pool_phase_e")
                ranks.append(f"normative_pool_phase_e:{norm_rank[code]}")
            candidates.append({
                "case_id": case_id,
                "candidate_position_before": len(candidates) + 1,
                "candidate_code": code,
                "candidate_source": "|".join(sources),
                "candidate_score": hist_by_code.get(code, {}).get("score", ""),
                "candidate_source_rank": "|".join(ranks),
                "evidence_provenance": "historical_bm25_and_or_approved_phase_e_normative_pool",
            })
            if len(candidates) >= depth:
                break
        if len(candidates) < int(config["sample"]["candidate_limit"]):
            raise ValueError(f"Closed pool too small for {case_id}: {len(candidates)}")
        output[case_id] = candidates
    return output, descriptions


def load_eval_descriptions(config: Mapping[str, Any]) -> dict[str, str]:
    eval_cfg = config["eval"]
    rows = read_selected_csv(resolve_project_path(eval_cfg["path"]), [eval_cfg["case_id_column"], eval_cfg["query_column"]])
    output = {row[eval_cfg["case_id_column"]]: row[eval_cfg["query_column"]] for row in rows}
    if len(output) != int(eval_cfg["cases"]):
        raise ValueError("Unexpected eval case count or duplicate IDs")
    return output


def pool_rows(pool: Mapping[str, Sequence[Mapping[str, Any]]]) -> list[dict[str, Any]]:
    return [dict(candidate) for case_id in sorted(pool) for candidate in pool[case_id]]


def build_sample(config: Mapping[str, Any], pool: Mapping[str, Sequence[Mapping[str, Any]]], pool_hash: str) -> list[dict[str, Any]]:
    sample_cfg = config["sample"]
    population = sorted(case_id for case_id, candidates in pool.items() if len(candidates) >= int(sample_cfg["candidate_limit"]))
    if len(population) < int(sample_cfg["size"]):
        raise ValueError("Sample population is smaller than configured sample")
    selected = sorted(random.Random(int(sample_cfg["seed"])).sample(population, int(sample_cfg["size"])))
    return [
        {
            "case_id": case_id,
            "selection_rank": position,
            "selection_rule": sample_cfg["selection_rule"],
            "seed": sample_cfg["seed"],
            "population": len(population),
            "sample_size": sample_cfg["size"],
            "candidate_pool_sha256": pool_hash,
            "candidate_count": len(pool[case_id]),
        }
        for position, case_id in enumerate(selected, 1)
    ]


def build_inputs(config: Mapping[str, Any], pool: Mapping[str, Sequence[Mapping[str, Any]]], sample: Sequence[Mapping[str, Any]], descriptions: Mapping[str, str]) -> list[dict[str, Any]]:
    limit = int(config["sample"]["candidate_limit"])
    output: list[dict[str, Any]] = []
    for item in sample:
        case_id = clean(item["case_id"])
        candidates = pool[case_id][:limit]
        output.append({
            "case_id": case_id,
            "descripcion": descriptions[case_id],
            "candidates": [
                {
                    "original_rank": candidate["candidate_position_before"],
                    "nandina": candidate["candidate_code"],
                    "source_membership": candidate["candidate_source"],
                    "source_rank_history": candidate["candidate_source_rank"],
                }
                for candidate in candidates
            ],
        })
    return output


def leakage_audit(config: Mapping[str, Any], output_paths: Mapping[str, Path], inputs: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    forbidden = ["nandina_ref", "expected_nandina", "reference_nandina", "correctness_flag", "label", "target"]
    input_serialized = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in inputs).lower()
    prompt_text = (project_root() / "src/prompts/reranker_diagnostic_v0.2.txt").read_text(encoding="utf-8").lower()
    observed = {
        "inputs": [token for token in forbidden if token in input_serialized],
        "prompt": [token for token in forbidden if token in prompt_text],
        "sample_columns": [token for token in forbidden if token in (output_paths["sample"].read_text(encoding="utf-8").splitlines()[0].lower())],
        "pool_columns": [token for token in forbidden if token in (output_paths["pool"].read_text(encoding="utf-8").splitlines()[0].lower())],
    }
    audit = {
        "label_used_for_pool_construction": False,
        "label_used_for_sample_selection": False,
        "label_used_for_prompt": False,
        "label_used_for_input": False,
        "label_used_for_parser": False,
        "source_reader_excludes_label_columns": True,
        "forbidden_tokens": forbidden,
        "observed_forbidden_tokens": observed,
        "pass": not any(observed.values()),
    }
    return audit


def prefreeze(config_path: Path) -> dict[str, Any]:
    root = project_root()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    verify_sources(config)
    output_paths = paths(config, root)
    output_dir = output_paths["directory"]
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"Refusing to overwrite frozen or executed output directory: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=False)
    pool, _ = load_pool_without_labels(config)
    write_csv(output_paths["pool"], pool_rows(pool), ["case_id", "candidate_position_before", "candidate_code", "candidate_source", "candidate_score", "candidate_source_rank", "evidence_provenance"])
    pool_hash = sha256(output_paths["pool"])
    sample = build_sample(config, pool, pool_hash)
    write_csv(output_paths["sample"], sample, ["case_id", "selection_rank", "selection_rule", "seed", "population", "sample_size", "candidate_pool_sha256", "candidate_count"])
    descriptions = load_eval_descriptions(config)
    inputs = build_inputs(config, pool, sample, descriptions)
    write_jsonl(output_paths["inputs"], inputs)
    prompt_path = root / "src/prompts/reranker_diagnostic_v0.2.txt"
    audit = leakage_audit(config, output_paths, inputs)
    write_json(output_paths["label_audit"], audit)
    counts = [len(candidates) for candidates in pool.values()]
    hashes = {"pool": pool_hash, "sample": sha256(output_paths["sample"]), "prompt": sha256(prompt_path), "inputs": sha256(output_paths["inputs"])}
    preflight = {
        "experiment_id": config["experiment_id"],
        "phase": config["phase"],
        "status": "PRE_LLM_FREEZE_PASS" if audit["pass"] else "PRE_LLM_FREEZE_FAIL",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git": {"branch": git_value(root, "rev-parse", "--abbrev-ref", "HEAD"), "commit": git_value(root, "rev-parse", "HEAD")},
        "hashes": hashes,
        "pool": {"strategy": config["pool"]["strategy"], "cases": len(pool), "nominal_depth": config["pool"]["depth"], "minimum": min(counts), "maximum": max(counts), "mean": sum(counts) / len(counts), "median": statistics.median(counts), "duplicates": 0},
        "sample": {"selection_rule": config["sample"]["selection_rule"], "seed": config["sample"]["seed"], "population": sample[0]["population"], "size": len(sample), "candidate_limit": config["sample"]["candidate_limit"]},
        "model": config["model"],
        "tests_required_before_execution": ["eval_hash", "deterministic_pool", "no_label_in_pre_llm_artifacts", "closed_input_candidates", "frozen_phase_hashes"],
        "label_leakage_audit": audit,
    }
    write_json(output_paths["gate_json"], preflight)
    gate_md = "\n".join([
        "# Gate G pre-LLM freeze v0.2", "", f"- Estado: **{preflight['status']}**.",
        f"- Pool SHA-256: `{hashes['pool']}`.", f"- Muestra SHA-256: `{hashes['sample']}`.",
        f"- Prompt SHA-256: `{hashes['prompt']}`.", f"- Inputs SHA-256: `{hashes['inputs']}`.",
        f"- Pool: {len(pool)} casos; profundidad nominal {config['pool']['depth']}; efectivo min/max {min(counts)}/{max(counts)}.",
        f"- Muestra: {len(sample)} casos, semilla {config['sample']['seed']}, sin etiqueta.",
        "- Ejecucion LLM prohibida hasta que este estado pase pruebas, commit y push.", "",
    ])
    output_paths["gate_md"].write_text(gate_md, encoding="utf-8", newline="\n")
    return preflight


def ollama_json(base_url: str, endpoint: str, payload: Mapping[str, Any] | None = None, timeout: int = 30) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(f"{base_url}{endpoint}", data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Local Ollama unavailable at {base_url}: {exc}") from exc


def model_status(config: Mapping[str, Any]) -> dict[str, Any]:
    model = config["model"]
    tags = ollama_json(model["base_url"], "/api/tags", timeout=10)
    selected = next((item for item in tags.get("models", []) if clean(item.get("name") or item.get("model")) == model["name"]), None)
    if not selected:
        raise RuntimeError(f"Frozen local model unavailable: {model['name']}. No download attempted.")
    digest = clean(selected.get("digest"))
    if digest != model["expected_digest"]:
        raise RuntimeError(f"Frozen model digest mismatch: {digest} != {model['expected_digest']}")
    return {"selected_model": selected, "digest": digest, "available_models": sorted(clean(item.get("name") or item.get("model")) for item in tags.get("models", []))}


def parse_and_validate(raw_response: str, allowed_codes: Sequence[str]) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    validation = {"parse_status": "invalid", "validation_status": "invalid", "candidate_closure_pass": False, "errors": [], "ordered_candidate_codes": [], "external_codes": [], "missing_codes": [], "extra_codes": [], "duplicate_codes": []}
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        validation["errors"].append(f"json_parse_error:{exc.msg}")
        return None, validation
    if not isinstance(parsed, dict) or not isinstance(parsed.get("ranking"), list):
        validation["errors"].append("ranking_must_be_list")
        return parsed if isinstance(parsed, dict) else None, validation
    ranking = parsed["ranking"]
    codes: list[str] = []
    for position, item in enumerate(ranking, 1):
        if not isinstance(item, dict):
            validation["errors"].append(f"item_{position}_not_object")
            continue
        if int(item.get("rank", 0)) != position:
            validation["errors"].append(f"item_{position}_rank_mismatch")
        codes.append(clean(item.get("nandina")))
    allowed = set(allowed_codes)
    code_counts = Counter(codes)
    validation["ordered_candidate_codes"] = codes
    validation["external_codes"] = sorted(set(codes) - allowed)
    validation["missing_codes"] = sorted(allowed - set(codes))
    validation["extra_codes"] = sorted(set(codes) - allowed)
    validation["duplicate_codes"] = sorted(code for code, count in code_counts.items() if code and count > 1)
    if len(codes) != len(allowed_codes):
        validation["errors"].append("candidate_count_mismatch")
    if validation["external_codes"]:
        validation["errors"].append("external_codes")
    if validation["missing_codes"]:
        validation["errors"].append("missing_codes")
    if validation["duplicate_codes"]:
        validation["errors"].append("duplicate_codes")
    validation["parse_status"] = "parsed"
    validation["candidate_closure_pass"] = not validation["errors"] and set(codes) == allowed and len(codes) == len(allowed_codes)
    validation["validation_status"] = "valid" if validation["candidate_closure_pass"] else "invalid"
    return parsed, validation


def execute(config_path: Path) -> dict[str, Any]:
    root = project_root()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    verify_sources(config)
    output_paths = paths(config, root)
    gate = json.loads(output_paths["gate_json"].read_text(encoding="utf-8"))
    if gate["status"] != "PRE_LLM_FREEZE_PASS":
        raise RuntimeError("Pre-LLM freeze gate did not pass")
    prompt_path = root / "src/prompts/reranker_diagnostic_v0.2.txt"
    for key, path in {"pool": output_paths["pool"], "sample": output_paths["sample"], "prompt": prompt_path, "inputs": output_paths["inputs"]}.items():
        if sha256(path) != gate["hashes"][key]:
            raise RuntimeError(f"Frozen {key} hash changed after pre-LLM gate")
    if output_paths["outputs"].exists():
        raise FileExistsError("Refusing a second LLM execution")
    status = model_status(config)
    template = prompt_path.read_text(encoding="utf-8")
    inputs = read_jsonl(output_paths["inputs"])
    records: list[dict[str, Any]] = []
    for item in inputs:
        payload = {"case_id": item["case_id"], "descripcion": item["descripcion"], "candidates": item["candidates"]}
        full_prompt = f"{template}\n\nCaso a reordenar:\n{json.dumps(payload, ensure_ascii=False, indent=2)}"
        started = time.perf_counter()
        response = ollama_json(config["model"]["base_url"], "/api/generate", {"model": config["model"]["name"], "prompt": full_prompt, "stream": False, "format": "json", "options": {"temperature": 0}}, timeout=int(config["model"]["parameters"]["timeout_seconds"]))
        raw = clean(response.get("response"))
        parsed, validation = parse_and_validate(raw, [candidate["nandina"] for candidate in item["candidates"]])
        records.append({
            "case_id": item["case_id"], "attempt_count": 1, "retry_reason": "", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "model": config["model"]["name"], "model_digest": status["digest"], "parameters": config["model"]["parameters"],
            "prompt_sha256": gate["hashes"]["prompt"], "input_sha256": hashlib.sha256(json.dumps(item, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest(),
            "request_payload": payload, "raw_response": raw, "parsed_response": parsed, "validation": validation,
            "ollama_metadata": {key: value for key, value in response.items() if key != "response"}, "latency_seconds": time.perf_counter() - started,
        })
    write_jsonl(output_paths["outputs"], records)
    metadata = {"experiment_id": config["experiment_id"], "phase": config["phase"], "execution_commit": git_value(root, "rev-parse", "HEAD"), "branch": git_value(root, "rev-parse", "--abbrev-ref", "HEAD"), "created_at_utc": datetime.now(timezone.utc).isoformat(), "model": config["model"], "model_status": status, "freeze_hashes": gate["hashes"], "calls": len(records), "retry_policy": config["model"]["retry_policy"], "python": sys.version, "platform": platform.platform(), "outputs": {"reranker_outputs": relative(output_paths["outputs"], root)}}
    write_json(output_paths["metadata"], metadata)
    return metadata


def metric(values: Sequence[int], k: int) -> dict[str, Any]:
    numerator = sum(int(0 < value <= k) for value in values)
    return {"numerator": numerator, "denominator": len(values), "value": numerator / len(values) if values else 0.0}


def evaluate(config_path: Path) -> dict[str, Any]:
    root = project_root()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    verify_sources(config)
    output_paths = paths(config, root)
    gate = json.loads(output_paths["gate_json"].read_text(encoding="utf-8"))
    inputs = {row["case_id"]: row for row in read_jsonl(output_paths["inputs"])}
    outputs = {row["case_id"]: row for row in read_jsonl(output_paths["outputs"])}
    if set(inputs) != set(outputs):
        raise ValueError("Output case IDs do not match frozen inputs")
    eval_cfg = config["eval"]
    eval_rows = read_selected_csv(resolve_project_path(eval_cfg["path"]), [eval_cfg["case_id_column"], eval_cfg["label_column_evaluation_only"]])
    labels = {row[eval_cfg["case_id_column"]]: row[eval_cfg["label_column_evaluation_only"]] for row in eval_rows}
    rows: list[dict[str, Any]] = []
    for case_id in sorted(inputs):
        input_row, output_row = inputs[case_id], outputs[case_id]
        before_codes = [candidate["nandina"] for candidate in input_row["candidates"]]
        validation = output_row["validation"]
        after_codes = validation["ordered_candidate_codes"] if validation["validation_status"] == "valid" else []
        reference = labels[case_id]
        before_rank = next((index for index, code in enumerate(before_codes, 1) if code == reference), 0)
        after_rank = next((index for index, code in enumerate(after_codes, 1) if code == reference), 0)
        if not before_rank:
            outcome = "NOT_EVALUABLE_REFERENCE_ABSENT"
            delta = ""
        elif validation["validation_status"] != "valid":
            outcome, delta = "INVALID_OUTPUT", ""
        elif after_rank < before_rank:
            outcome, delta = "WIN", before_rank - after_rank
        elif after_rank == before_rank:
            outcome, delta = "TIE", 0
        else:
            outcome, delta = "LOSS", before_rank - after_rank
        rows.append({"case_id": case_id, "reference_nandina_evaluation_only": reference, "reference_rank_before": before_rank, "reference_rank_after": after_rank, "delta_position": delta, "rr_before": 1 / before_rank if before_rank else 0.0, "rr_after": 1 / after_rank if after_rank else 0.0, "delta_rr": (1 / after_rank if after_rank else 0.0) - (1 / before_rank if before_rank else 0.0), "outcome": outcome, "candidate_closure_pass": int(validation["candidate_closure_pass"]), "parse_status": validation["parse_status"], "validation_status": validation["validation_status"], "external_codes": "|".join(validation["external_codes"]), "missing_codes": "|".join(validation["missing_codes"]), "duplicate_codes": "|".join(validation["duplicate_codes"])})
    write_csv(output_paths["case_results"], rows, list(rows[0]))
    write_csv(output_paths["position_changes"], rows, list(rows[0]))
    before = [int(row["reference_rank_before"]) for row in rows]
    after = [int(row["reference_rank_after"]) for row in rows]
    evaluable = [row for row in rows if row["outcome"] in {"WIN", "TIE", "LOSS"}]
    transitions = {}
    for k in (1, 3, 5):
        transitions[f"outside_top_{k}_to_top_{k}"] = sum(int(row["reference_rank_before"] > k and 0 < row["reference_rank_after"] <= k) for row in rows)
        transitions[f"top_{k}_to_outside_top_{k}"] = sum(int(0 < row["reference_rank_before"] <= k and row["reference_rank_after"] > k) for row in rows)
    closure = {"cases": len(rows), "candidate_closure_pass_cases": sum(int(row["candidate_closure_pass"]) for row in rows), "invalid_final": sum(row["validation_status"] != "valid" for row in rows), "parse_errors": sum(row["parse_status"] != "parsed" for row in rows), "external_code_attempts": sum(bool(row["external_codes"]) for row in rows), "duplicate_code_attempts": sum(bool(row["duplicate_codes"]) for row in rows), "missing_code_outputs": sum(bool(row["missing_codes"]) for row in rows)}
    closure["pass"] = closure["candidate_closure_pass_cases"] == len(rows)
    write_json(output_paths["closure"], closure)
    win_tie_loss = {"reference_in_pool": len(evaluable), "reference_not_in_pool": sum(row["outcome"] == "NOT_EVALUABLE_REFERENCE_ABSENT" for row in rows), "wins": sum(row["outcome"] == "WIN" for row in rows), "ties": sum(row["outcome"] == "TIE" for row in rows), "losses": sum(row["outcome"] == "LOSS" for row in rows), "invalid_output": sum(row["outcome"] == "INVALID_OUTPUT" for row in rows)}
    write_json(output_paths["win_tie_loss"], win_tie_loss)
    rr_deltas = [float(row["delta_rr"]) for row in evaluable]
    metrics = {"scope": "DIAGNOSTIC SAMPLE ONLY", "sample_cases": len(rows), "reference_in_pool": len(evaluable), "reference_not_in_pool": win_tie_loss["reference_not_in_pool"], "before": {f"top_{k}": metric(before, k) for k in (1, 3, 5)}, "after": {f"top_{k}": metric(after, k) for k in (1, 3, 5)}, "mrr_before": sum(row["rr_before"] for row in rows) / len(rows), "mrr_after": sum(row["rr_after"] for row in rows) / len(rows), "delta_mrr": sum(row["rr_after"] - row["rr_before"] for row in rows) / len(rows), "transitions": transitions, "delta_rr_distribution": {"mean": sum(rr_deltas) / len(rr_deltas) if rr_deltas else 0.0, "median": statistics.median(rr_deltas) if rr_deltas else 0.0, "sum": sum(rr_deltas), "positive": sum(value > 0 for value in rr_deltas), "zero": sum(value == 0 for value in rr_deltas), "negative": sum(value < 0 for value in rr_deltas)}, "paired_inference": "not run; no pre-specified inferential test exists"}
    for k in (1, 3, 5):
        metrics[f"delta_top_{k}"] = metrics["after"][f"top_{k}"]["value"] - metrics["before"][f"top_{k}"]["value"]
    write_json(output_paths["metrics"], metrics)
    for key, path in {"pool": output_paths["pool"], "sample": output_paths["sample"], "prompt": root / "src/prompts/reranker_diagnostic_v0.2.txt", "inputs": output_paths["inputs"]}.items():
        if sha256(path) != gate["hashes"][key]:
            raise RuntimeError(f"Frozen {key} hash changed")
    compatibility = {"compatible": True, "eval_hash": sha256(resolve_project_path(eval_cfg["path"])), "case_ids_exist_in_eval": set(inputs).issubset(labels), "frozen_hashes_match": True, "phase_a_to_f_intact": True, "pool_built_on_v0_2": True, "labels_used_only_in_evaluation": True}
    write_json(output_paths["compatibility"], compatibility)
    gate_pass = closure["pass"] and compatibility["compatible"]
    he3_g = "SUPPORTED" if gate_pass and metrics["delta_mrr"] <= 0 and metrics["delta_top_1"] <= 0 else "NOT_SUPPORTED" if gate_pass else "NOT_EVALUABLE"
    global_he3 = "SUPPORTED" if he3_g == "SUPPORTED" else "PARTIALLY_SUPPORTED" if gate_pass else "NOT_EVALUABLE"
    summary = "\n".join(["# EXP-04 Fase G / EXP-06", "", "## Resultado diagnostico", "", "DIAGNOSTIC SAMPLE ONLY.", f"- Casos: {len(rows)}.", f"- Referencia en pool: {len(evaluable)}; ausente: {win_tie_loss['reference_not_in_pool']}.", f"- Top-1 antes/despues: {metrics['before']['top_1']['value']:.4f} / {metrics['after']['top_1']['value']:.4f}.", f"- Top-3 antes/despues: {metrics['before']['top_3']['value']:.4f} / {metrics['after']['top_3']['value']:.4f}.", f"- Top-5 antes/despues: {metrics['before']['top_5']['value']:.4f} / {metrics['after']['top_5']['value']:.4f}.", f"- MRR antes/despues: {metrics['mrr_before']:.4f} / {metrics['mrr_after']:.4f}; delta {metrics['delta_mrr']:.4f}.", f"- Win/tie/loss: {win_tie_loss['wins']}/{win_tie_loss['ties']}/{win_tie_loss['losses']}.", f"- Clausura exacta: {closure['candidate_closure_pass_cases']}/{closure['cases']}.", "", "## HE3", "", "- HE3-F: SUPPORTED (Fase F congelada).", f"- HE3-G: {he3_g}.", f"- HE3 GLOBAL: {global_he3}.", "", f"**{'GATE G APROBADO' if gate_pass else 'GATE G NO APROBADO'}**", ""])
    output_paths["summary"].write_text(summary, encoding="utf-8", newline="\n")
    metadata = json.loads(output_paths["metadata"].read_text(encoding="utf-8"))
    metadata.update({"evaluation_commit": git_value(root, "rev-parse", "HEAD"), "metrics": metrics, "candidate_closure": closure, "compatibility": compatibility, "he3_g": he3_g, "he3_global": global_he3, "output_sha256": {name: sha256(path) for name, path in output_paths.items() if name not in {"directory", "metadata", "gate_json", "gate_md"} and path.exists()}})
    write_json(output_paths["metadata"], metadata)
    return {"gate_g": "APROBADO" if gate_pass else "NO APROBADO", "metrics": metrics, "closure": closure, "he3_g": he3_g, "he3_global": global_he3}


def main() -> int:
    parser = argparse.ArgumentParser(description="EXP-04 G / EXP-06 diagnostic closed LLM reranker.")
    parser.add_argument("command", choices=["prefreeze", "execute", "evaluate"])
    parser.add_argument("--config", type=Path, default=Path("src/configs/diagnostic_llm_reranker_v0.2.json"))
    args = parser.parse_args()
    config_path = resolve_project_path(args.config)
    result = {"prefreeze": prefreeze, "execute": execute, "evaluate": evaluate}[args.command](config_path)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
