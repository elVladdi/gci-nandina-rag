from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_HYBRID_POOL = Path("outputs/evaluation/hybrid_historical_normative_pool_v0.1/hybrid_pool.csv")
DEFAULT_HYBRID_CASE_SUMMARY = Path("outputs/evaluation/hybrid_historical_normative_pool_v0.1/hybrid_case_summary.csv")
DEFAULT_PROMPT = Path("src/llm/rerank_hybrid_pool_prompt_v0.1.md")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1")

MODEL_NAME = "qwen2.5:7b-instruct"
POOL_STRATEGY = "historical_first_80_normative_20"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
CANDIDATE_LIMIT = 10
SAMPLE_TARGETS = {
    "rank_1": 5,
    "rank_2_10": 5,
    "rank_11_100": 5,
    "singleton": 5,
}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _append_jsonl(path: Path, row: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _rel(path: Path) -> str:
    root = project_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _ollama_json(path: str, payload: Mapping[str, Any] | None = None, timeout: int = 120) -> dict[str, Any]:
    url = f"{OLLAMA_BASE_URL}{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama local unavailable at {OLLAMA_BASE_URL}: {exc}") from exc


def _verify_ollama_model(model: str) -> dict[str, Any]:
    tags = _ollama_json("/api/tags", timeout=10)
    models = tags.get("models", [])
    names = {_clean(item.get("name") or item.get("model")) for item in models}
    if model not in names:
        raise RuntimeError(f"Required local Ollama model not installed: {model}. No download attempted.")
    return {"model": model, "available_models": sorted(names)}


def _case_category(row: Mapping[str, str]) -> str:
    if _clean(row.get("support_bucket")) == "singleton":
        return "singleton"
    rank = int(_clean(row.get("exact_rank")) or "0")
    if rank == 1:
        return "rank_1"
    if 2 <= rank <= 10:
        return "rank_2_10"
    if 11 <= rank <= 100:
        return "rank_11_100"
    return "outside_top_100"


def _select_sample(case_rows: Sequence[Mapping[str, str]]) -> list[dict[str, Any]]:
    selected_ids: set[str] = set()
    selected: list[dict[str, Any]] = []
    by_category: dict[str, list[Mapping[str, str]]] = {category: [] for category in [*SAMPLE_TARGETS, "outside_top_100"]}
    for row in case_rows:
        by_category.setdefault(_case_category(row), []).append(row)
    for rows in by_category.values():
        rows.sort(key=lambda item: (_clean(item.get("case_id")), int(_clean(item.get("exact_rank")) or "999999")))

    fallback_order = {
        "rank_1": ["rank_2_10", "rank_11_100", "singleton", "outside_top_100"],
        "rank_2_10": ["rank_1", "rank_11_100", "singleton", "outside_top_100"],
        "rank_11_100": ["rank_2_10", "rank_1", "singleton", "outside_top_100"],
        "singleton": ["outside_top_100", "rank_11_100", "rank_2_10", "rank_1"],
    }

    for target_category, target_count in SAMPLE_TARGETS.items():
        candidates = [(target_category, row) for row in by_category.get(target_category, [])]
        for category in fallback_order[target_category]:
            candidates.extend((category, row) for row in by_category.get(category, []))
        count = 0
        for source_category, row in candidates:
            case_id = _clean(row.get("case_id"))
            if case_id in selected_ids:
                continue
            selected_ids.add(case_id)
            count += 1
            selected.append(
                {
                    "case_id": case_id,
                    "expected_nandina": _clean(row.get("expected_nandina")),
                    "sample_target_category": target_category,
                    "selection_source_category": source_category,
                    "selection_note": "exact_category" if source_category == target_category else f"fallback_from_{source_category}",
                    "original_exact_rank_pool": int(_clean(row.get("exact_rank")) or "0"),
                    "support_bucket": _clean(row.get("support_bucket")),
                    "historical_support_count": int(_clean(row.get("historical_support_count")) or "0"),
                    "descripcion": _clean(row.get("descripcion")),
                }
            )
            if count >= target_count:
                break
    selected.sort(key=lambda item: (list(SAMPLE_TARGETS).index(item["sample_target_category"]), item["case_id"]))
    return selected


def _load_operational_pool(pool_path: Path) -> tuple[dict[str, list[dict[str, Any]]], int]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    oracle_rows = 0
    for row in _read_csv(pool_path):
        strategy = _clean(row.get("pool_strategy"))
        if "oracle" in strategy:
            oracle_rows += 1
            continue
        if strategy != POOL_STRATEGY:
            continue
        case_id = _clean(row.get("case_id"))
        grouped.setdefault(case_id, []).append(
            {
                "original_rank": int(_clean(row.get("final_rank")) or "0"),
                "nandina": _clean(row.get("candidate_nandina")),
                "source_membership": _clean(row.get("source_membership")),
                "source_rank_history": _clean(row.get("source_rank_history")),
            }
        )
    for rows in grouped.values():
        rows.sort(key=lambda item: int(item["original_rank"]))
    return grouped, oracle_rows


def _build_user_payload(sample: Mapping[str, Any], candidates: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    return {
        "case_id": sample["case_id"],
        "descripcion": sample["descripcion"],
        "candidates": list(candidates[:CANDIDATE_LIMIT]),
    }


def _strip_json(text: str) -> str:
    raw = _clean(text)
    match = re.search(r"```(?:json)?\s*(.*?)```", raw, flags=re.IGNORECASE | re.DOTALL)
    if match:
        raw = match.group(1).strip()
    start = raw.find("{")
    end = raw.rfind("}")
    if start >= 0 and end >= start:
        return raw[start : end + 1]
    return raw


def _normalize_response(case_id: str, raw_text: str, pool_codes: Sequence[str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pool_set = set(pool_codes)
    base_status = {
        "case_id": case_id,
        "json_valid": False,
        "codes_outside_pool": 0,
        "ranking_incomplete": False,
        "duplicates": 0,
        "selected_rank1_outside_pool": False,
        "parse_error": "",
    }
    try:
        payload = json.loads(_strip_json(raw_text))
    except json.JSONDecodeError as exc:
        base_status["parse_error"] = str(exc)
        return [
            {
                **base_status,
                "normalized_rank": "",
                "nandina": "",
                "reason_short": "",
                "confidence": "",
                "in_pool": False,
                "duplicate_code": False,
            }
        ], base_status

    ranking = payload.get("ranking", [])
    warnings = payload.get("warnings", [])
    base_status["json_valid"] = isinstance(ranking, list) and isinstance(warnings, list)
    if not base_status["json_valid"]:
        base_status["parse_error"] = "ranking or warnings has invalid type"
        ranking = []
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    for position, item in enumerate(ranking, start=1):
        if not isinstance(item, dict):
            continue
        code = _clean(item.get("nandina"))
        in_pool = code in pool_set
        duplicate = bool(code and code in seen)
        if code:
            seen.add(code)
        base_status["codes_outside_pool"] += int(bool(code and not in_pool))
        base_status["duplicates"] += int(duplicate)
        rows.append(
            {
                **base_status,
                "normalized_rank": int(item.get("rank") or position),
                "nandina": code,
                "reason_short": _clean(item.get("reason_short")),
                "confidence": _clean(item.get("confidence")),
                "in_pool": str(in_pool).lower(),
                "duplicate_code": str(duplicate).lower(),
            }
        )
    base_status["ranking_incomplete"] = len({row["nandina"] for row in rows if row["nandina"]}) < min(CANDIDATE_LIMIT, len(pool_codes))
    first_code = rows[0]["nandina"] if rows else ""
    base_status["selected_rank1_outside_pool"] = bool(first_code and first_code not in pool_set)
    if not rows:
        rows.append(
            {
                **base_status,
                "normalized_rank": "",
                "nandina": "",
                "reason_short": "",
                "confidence": "",
                "in_pool": False,
                "duplicate_code": False,
            }
        )
    return [{**row, **base_status} for row in rows], base_status


def _generate(prompt: str, payload: Mapping[str, Any], model: str) -> dict[str, Any]:
    full_prompt = f"{prompt}\n\nReordena este caso:\n{json.dumps(payload, ensure_ascii=False, indent=2)}"
    request = {
        "model": model,
        "prompt": full_prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    }
    started = time.perf_counter()
    response = _ollama_json("/api/generate", request, timeout=180)
    response["elapsed_seconds_client"] = time.perf_counter() - started
    return response


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    model_status = _verify_ollama_model(args.model)
    output_dir = resolve_project_path(args.output_dir)
    raw_path = output_dir / "llm_rerank_raw.jsonl"
    if raw_path.exists():
        raw_path.unlink()

    prompt = resolve_project_path(args.prompt).read_text(encoding="utf-8")
    case_rows = [
        row
        for row in _read_csv(resolve_project_path(args.hybrid_case_summary))
        if _clean(row.get("pool_strategy")) == POOL_STRATEGY
    ]
    pool_by_case, oracle_rows_skipped = _load_operational_pool(resolve_project_path(args.hybrid_pool))
    sample = _select_sample(case_rows)
    if len(sample) != sum(SAMPLE_TARGETS.values()):
        raise ValueError(f"Expected 20 sample cases, selected {len(sample)}")

    sample_fieldnames = [
        "case_id",
        "expected_nandina",
        "sample_target_category",
        "selection_source_category",
        "selection_note",
        "original_exact_rank_pool",
        "support_bucket",
        "historical_support_count",
        "descripcion",
    ]
    _write_csv(output_dir / "sample_cases.csv", sample, sample_fieldnames)

    normalized_rows: list[dict[str, Any]] = []
    status_rows: list[dict[str, Any]] = []
    for item in sample:
        case_id = item["case_id"]
        candidates = pool_by_case.get(case_id, [])[:CANDIDATE_LIMIT]
        if len(candidates) != CANDIDATE_LIMIT:
            raise ValueError(f"Case {case_id} has {len(candidates)} candidates, expected {CANDIDATE_LIMIT}")
        request_payload = _build_user_payload(item, candidates)
        response = _generate(prompt, request_payload, args.model)
        raw_text = _clean(response.get("response"))
        pool_codes = [candidate["nandina"] for candidate in candidates]
        rows, status = _normalize_response(case_id, raw_text, pool_codes)
        normalized_rows.extend(rows)
        status_rows.append(status)
        _append_jsonl(
            raw_path,
            {
                "case_id": case_id,
                "model": args.model,
                "pool_strategy": POOL_STRATEGY,
                "candidate_limit": CANDIDATE_LIMIT,
                "request_payload": request_payload,
                "raw_response": raw_text,
                "ollama_metadata": {key: value for key, value in response.items() if key != "response"},
                "normalization_status": status,
                "created_at_utc": datetime.now(timezone.utc).isoformat(),
            },
        )

    normalized_fieldnames = [
        "case_id",
        "json_valid",
        "codes_outside_pool",
        "ranking_incomplete",
        "duplicates",
        "selected_rank1_outside_pool",
        "parse_error",
        "normalized_rank",
        "nandina",
        "reason_short",
        "confidence",
        "in_pool",
        "duplicate_code",
    ]
    _write_csv(output_dir / "llm_rerank_normalized.csv", normalized_rows, normalized_fieldnames)
    return {
        "status": "completed",
        "model_status": model_status,
        "model": args.model,
        "pool_strategy": POOL_STRATEGY,
        "oracle_rows_skipped": oracle_rows_skipped,
        "candidate_limit": CANDIDATE_LIMIT,
        "sample_cases": len(sample),
        "output_dir": _rel(output_dir),
        "json_valid_cases": sum(1 for row in status_rows if row["json_valid"]),
        "pool_violation_cases": sum(1 for row in status_rows if row["codes_outside_pool"] or row["selected_rank1_outside_pool"]),
        "elapsed_seconds": time.perf_counter() - started,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local Ollama re-ranking over a 20-case hybrid pool sample.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--hybrid-pool", default=str(DEFAULT_HYBRID_POOL))
    parser.add_argument("--hybrid-case-summary", default=str(DEFAULT_HYBRID_CASE_SUMMARY))
    parser.add_argument("--prompt", default=str(DEFAULT_PROMPT))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default=MODEL_NAME)
    return parser


def main() -> int:
    result = run(build_parser().parse_args())
    print(f"OK: re-ranking LLM local completado con {result['model']}")
    print(f"Pool: {result['pool_strategy']} candidate_limit={result['candidate_limit']}")
    print(f"Casos: {result['sample_cases']} JSON validos: {result['json_valid_cases']}")
    print(f"Violaciones de pool por caso: {result['pool_violation_cases']}")
    print(f"Outputs: {result['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
