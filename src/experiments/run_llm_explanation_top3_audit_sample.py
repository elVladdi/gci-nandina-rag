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

DEFAULT_PAYLOADS = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/payloads.jsonl")
DEFAULT_PROMPT = Path("src/llm/explain_top3_nandina_prompt_v0.2.md")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1")

MODEL_NAME = "qwen2.5:7b-instruct"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _rel(path: Path) -> str:
    root = project_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _read_jsonl(path: Path):
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            raw = line.strip()
            if raw:
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc


def _append_jsonl(path: Path, row: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _ollama_json(base_url: str, path: str, payload: Mapping[str, Any] | None = None, timeout: int = 120) -> dict[str, Any]:
    if not base_url.startswith("http://127.0.0.1:") and not base_url.startswith("http://localhost:"):
        raise ValueError("Only local Ollama URLs are allowed")
    url = f"{base_url.rstrip('/')}{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama local unavailable at {base_url}: {exc}") from exc


def _verify_ollama_model(base_url: str, model: str) -> dict[str, Any]:
    tags = _ollama_json(base_url, "/api/tags", timeout=10)
    names = {_clean(item.get("name") or item.get("model")) for item in tags.get("models", [])}
    if model not in names:
        raise RuntimeError(f"Required local Ollama model not installed: {model}. No download attempted.")
    return {"model": model, "available_models": sorted(names)}


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


def _parse_response(raw_text: str) -> tuple[dict[str, Any] | None, str]:
    try:
        parsed = json.loads(_strip_json(raw_text))
    except json.JSONDecodeError as exc:
        return None, str(exc)
    if not isinstance(parsed, dict):
        return None, "top-level JSON is not an object"
    return parsed, ""


def _generate(base_url: str, model: str, prompt: str, payload: Mapping[str, Any]) -> dict[str, Any]:
    full_prompt = (
        f"{prompt}\n\n"
        "Explica este caso respetando estrictamente el Top-3 original y el esquema JSON v0.2:\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )
    request = {
        "model": model,
        "prompt": full_prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0, "num_ctx": 8192},
    }
    started = time.perf_counter()
    response = _ollama_json(base_url, "/api/generate", request, timeout=300)
    response["elapsed_seconds_client"] = time.perf_counter() - started
    return response


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    output_dir = resolve_project_path(args.output_dir)
    raw_path = output_dir / "llm_explanations.jsonl"
    csv_path = output_dir / "llm_explanations.csv"
    existing_records = list(_read_jsonl(raw_path)) if args.resume and raw_path.exists() else []
    done_cases = {_clean(row.get("case_id")) for row in existing_records}
    if raw_path.exists() and not args.resume:
        raw_path.unlink()
    model_status = _verify_ollama_model(args.ollama_url, args.model)
    prompt_path = resolve_project_path(args.prompt)
    prompt = prompt_path.read_text(encoding="utf-8")
    payload_path = resolve_project_path(args.payloads)
    payloads = list(_read_jsonl(payload_path))
    if not payloads:
        raise ValueError("No payloads found")

    rows: list[dict[str, Any]] = [
        {
            "case_id": _clean(row.get("case_id")),
            "id_unico": _clean(row.get("id_unico")),
            "model": _clean(row.get("model")) or args.model,
            "json_valid_on_run": int(bool(row.get("json_valid_on_run"))),
            "parse_error": _clean(row.get("parse_error")),
            "raw_response": _clean(row.get("raw_response")),
            "parsed_response_json": json.dumps(row.get("parsed_response"), ensure_ascii=False, sort_keys=True)
            if isinstance(row.get("parsed_response"), dict)
            else "",
            "elapsed_seconds_client": float((row.get("ollama_metadata") or {}).get("elapsed_seconds_client") or 0.0),
            "created_at_utc": _clean(row.get("created_at_utc")),
        }
        for row in existing_records
    ]
    for position, payload in enumerate(payloads, start=1):
        if _clean(payload.get("case_id")) in done_cases:
            print(f"SKIP {position}/{len(payloads)} {_clean(payload.get('case_id'))} already_present=1")
            continue
        response = _generate(args.ollama_url, args.model, prompt, payload)
        raw_text = _clean(response.get("response"))
        parsed, parse_error = _parse_response(raw_text)
        json_valid = parsed is not None
        created_at = datetime.now(timezone.utc).isoformat()
        row = {
            "case_id": _clean(payload.get("case_id")),
            "id_unico": _clean(payload.get("id_unico")),
            "model": args.model,
            "json_valid_on_run": int(json_valid),
            "parse_error": parse_error,
            "raw_response": raw_text,
            "parsed_response_json": json.dumps(parsed, ensure_ascii=False, sort_keys=True) if parsed else "",
            "elapsed_seconds_client": float(response.get("elapsed_seconds_client") or 0.0),
            "created_at_utc": created_at,
        }
        rows.append(row)
        _append_jsonl(
            raw_path,
            {
                "case_id": row["case_id"],
                "id_unico": row["id_unico"],
                "model": args.model,
                "prompt": _rel(prompt_path),
                "payload": payload,
                "raw_response": raw_text,
                "parsed_response": parsed,
                "json_valid_on_run": json_valid,
                "parse_error": parse_error,
                "ollama_metadata": {key: value for key, value in response.items() if key != "response"},
                "created_at_utc": created_at,
            },
        )
        print(f"OK {position}/{len(payloads)} {row['case_id']} json_valid={int(json_valid)}")

    fieldnames = [
        "case_id",
        "id_unico",
        "model",
        "json_valid_on_run",
        "parse_error",
        "raw_response",
        "parsed_response_json",
        "elapsed_seconds_client",
        "created_at_utc",
    ]
    _write_csv(csv_path, rows, fieldnames)
    return {
        "status": "completed",
        "model_status": model_status,
        "model": args.model,
        "payloads": len(payloads),
        "json_valid_on_run": sum(int(row["json_valid_on_run"]) for row in rows),
        "outputs": {
            "llm_explanations_jsonl": _rel(raw_path),
            "llm_explanations_csv": _rel(csv_path),
        },
        "elapsed_seconds": time.perf_counter() - started,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local Ollama explanations for formal Top-3 NANDINA audit sample.")
    parser.add_argument("--payloads", default=str(DEFAULT_PAYLOADS))
    parser.add_argument("--prompt", default=str(DEFAULT_PROMPT))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--ollama-url", default=OLLAMA_BASE_URL)
    parser.add_argument("--resume", action="store_true", help="Skip cases already present in llm_explanations.jsonl.")
    return parser


def main() -> int:
    result = run(build_parser().parse_args())
    print(f"OK: explicaciones LLM 10B completadas con {result['model']}")
    print(f"Payloads: {result['payloads']} JSON validos iniciales: {result['json_valid_on_run']}")
    print(f"Outputs: {result['outputs']['llm_explanations_jsonl']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
