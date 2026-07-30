from __future__ import annotations

import argparse
import csv
import json
import platform
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_POOL = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool.csv")
DEFAULT_PROMPT = Path("src/llm/rerank_nandina_prompt_v0.1.md")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_rerank_pool_devset_v0.1")
DEFAULT_MODEL = "qwen2.5:7b-instruct"
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
DEFAULT_OLLAMA_TAGS_URL = "http://127.0.0.1:11434/api/tags"
DEFAULT_POOL_STRATEGY = "hierarchical_80_dual_backfill_20"
EXPECTED_DEVSET_CASES = 13


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


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _request_json(url: str, payload: Mapping[str, Any] | None = None, timeout_seconds: int = 30) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    method = "GET" if payload is None else "POST"
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method=method)
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        return json.loads(response.read().decode("utf-8"))


def _model_info(tags_url: str, model: str, timeout_seconds: int) -> dict[str, Any]:
    try:
        payload = _request_json(tags_url, timeout_seconds=timeout_seconds)
    except Exception as exc:  # noqa: BLE001 - metadata should preserve service failures.
        return {"available": False, "error": str(exc), "models": []}
    models = payload.get("models", [])
    match = next((item for item in models if item.get("name") == model or item.get("model") == model), None)
    return {"available": match is not None, "selected_model": match, "models": models}


def _call_ollama(
    *,
    url: str,
    model: str,
    prompt: str,
    response_schema: Mapping[str, Any],
    temperature: float,
    top_p: float,
    num_predict: int,
    timeout_seconds: int,
) -> tuple[str, dict[str, Any]]:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": response_schema,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        },
    }
    response = _request_json(url, payload=payload, timeout_seconds=timeout_seconds)
    message = response.get("message", {})
    return _clean(message.get("content")), response


def _response_schema(allowed_codes: Sequence[str]) -> dict[str, Any]:
    candidate_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["rank", "nandina", "rationale", "evidence_used", "confidence"],
        "properties": {
            "rank": {"type": "integer", "minimum": 1, "maximum": 10},
            "nandina": {"type": "string", "enum": list(allowed_codes)},
            "rationale": {"type": "string"},
            "evidence_used": {"type": "string"},
            "confidence": {"type": "string", "enum": ["alta", "media", "baja"]},
        },
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["ranked_candidates", "selected_nandina", "warnings"],
        "properties": {
            "ranked_candidates": {
                "type": "array",
                "minItems": 1,
                "maxItems": 10,
                "items": candidate_schema,
            },
            "selected_nandina": {"type": "string", "enum": list(allowed_codes)},
            "warnings": {"type": "array", "items": {"type": "string"}},
        },
    }


def _parse_json_response(raw_response: str) -> tuple[dict[str, Any] | None, str]:
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        return None, f"json_parse_error: {exc.msg}"
    if not isinstance(parsed, dict):
        return None, "json_parse_error: root is not an object"
    return parsed, ""


def _validate_response(parsed: Mapping[str, Any] | None, allowed_codes: Sequence[str]) -> list[str]:
    if parsed is None:
        return ["response_is_not_json_object"]
    errors: list[str] = []
    allowed = set(allowed_codes)
    ranked = parsed.get("ranked_candidates")
    selected = _clean(parsed.get("selected_nandina"))
    warnings = parsed.get("warnings")
    if not isinstance(ranked, list) or not ranked:
        errors.append("ranked_candidates_must_be_nonempty_list")
        ranked = []
    if not isinstance(warnings, list):
        errors.append("warnings_must_be_list")
    if selected not in allowed:
        errors.append("selected_nandina_outside_sent_pool")

    codes: list[str] = []
    for position, item in enumerate(ranked, start=1):
        if not isinstance(item, Mapping):
            errors.append(f"ranked_item_{position}_not_object")
            continue
        code = _clean(item.get("nandina"))
        codes.append(code)
        if code not in allowed:
            errors.append(f"ranked_item_{position}_outside_sent_pool")
        if int(item.get("rank", 0)) != position:
            errors.append(f"ranked_item_{position}_rank_mismatch")
        if _clean(item.get("confidence")) not in {"alta", "media", "baja"}:
            errors.append(f"ranked_item_{position}_invalid_confidence")
        for field in ["rationale", "evidence_used"]:
            if not isinstance(item.get(field), str):
                errors.append(f"ranked_item_{position}_{field}_not_string")
    if len(codes) != len(set(codes)):
        errors.append("duplicate_ranked_codes")
    if codes and selected != codes[0]:
        errors.append("selected_nandina_must_match_rank_1")
    return errors


def _normalize_response(parsed: dict[str, Any] | None) -> tuple[dict[str, Any] | None, list[str]]:
    if parsed is None:
        return None, []
    normalized = dict(parsed)
    ranked = parsed.get("ranked_candidates")
    if not isinstance(ranked, list):
        return normalized, []
    deduplicated: list[dict[str, Any]] = []
    seen: set[str] = set()
    actions: list[str] = []
    for item in ranked:
        if not isinstance(item, Mapping):
            deduplicated.append(dict(item) if isinstance(item, dict) else {"value": item})
            continue
        code = _clean(item.get("nandina"))
        if code and code in seen:
            actions.append(f"duplicate_removed:{code}")
            continue
        if code:
            seen.add(code)
        normalized_item = dict(item)
        normalized_item["rank"] = len(deduplicated) + 1
        deduplicated.append(normalized_item)
    normalized["ranked_candidates"] = deduplicated
    return normalized, actions


def _group_cases(rows: Sequence[Mapping[str, str]], strategy: str, candidate_limit: int) -> list[dict[str, Any]]:
    filtered = [row for row in rows if row.get("pool_strategy") == strategy]
    grouped: dict[str, list[Mapping[str, str]]] = {}
    for row in filtered:
        grouped.setdefault(row["case_id"], []).append(row)

    cases: list[dict[str, Any]] = []
    for case_id, items in sorted(grouped.items()):
        ordered = sorted(items, key=lambda row: int(row["candidate_rank_pool"]))
        selected = ordered[:candidate_limit]
        if not selected:
            continue
        cases.append(
            {
                "case_id": case_id,
                "descripcion": selected[0]["descripcion"],
                "nandina_ref": selected[0]["nandina_ref"],
                "candidates": selected,
            }
        )
    return cases


def _format_candidates(candidates: Sequence[Mapping[str, str]]) -> str:
    lines: list[str] = []
    for row in candidates:
        evidence = _clean(row.get("evidence_text"))
        if len(evidence) > 900:
            evidence = evidence[:900].rstrip() + "..."
        lines.append(
            "\n".join(
                [
                    f"- rank_pool: {row['candidate_rank_pool']}",
                    f"  nandina: {row['candidate_code']}",
                    f"  hs4: {row.get('hs4_candidate', '')}",
                    f"  hs2: {row.get('hs2_candidate', '')}",
                    f"  evidencia: {evidence}",
                ]
            )
        )
    return "\n".join(lines)


def _build_prompt(template: str, case: Mapping[str, Any], candidate_limit: int) -> str:
    candidate_codes = [row["candidate_code"] for row in case["candidates"]]
    return "\n\n".join(
        [
            template.strip(),
            "CASO A REORDENAR",
            f"case_id: {case['case_id']}",
            f"descripcion_comercial: {case['descripcion']}",
            f"candidate_limit_enviado: {candidate_limit}",
            "codigos_permitidos:",
            json.dumps(candidate_codes, ensure_ascii=False),
            "candidatos:",
            _format_candidates(case["candidates"]),
            "Recuerda: devuelve solo JSON estricto y solo codigos del listado permitido.",
        ]
    )


def _summary_markdown(metadata: Mapping[str, Any]) -> str:
    quality = metadata["quality"]
    lines = [
        "# LLM rerank pool devset v0.1",
        "",
        "## Alcance",
        "",
        "Ejecucion diagnostica/acotada sobre devset. Usa Ollama local; no usa APIs pagadas/remotas ni Text2Trade.",
        "",
        "## Configuracion",
        "",
        f"- Modelo: `{metadata['generation']['model']}`.",
        f"- Pool strategy: `{metadata['generation']['pool_strategy']}`.",
        f"- Candidate limit enviado al LLM: {metadata['generation']['candidate_limit']}.",
        f"- Temperatura: {metadata['generation']['temperature']}.",
        "",
        "No se envian 100 candidatos porque el contexto crece con evidencia textual por candidato; esta corrida prueba un re-ranking cerrado con un subconjunto auditable del pool final.",
        "",
        "## Calidad de salida",
        "",
        f"- Casos procesados: {quality['cases_total']}.",
        f"- JSON valido: {quality['valid_json_cases']} ({quality['valid_json_rate']:.4f}).",
        f"- Violaciones de pool detectadas por parsing inicial: {quality['pool_violation_cases']}.",
        f"- Errores de ejecucion: {quality['execution_error_cases']}.",
        "",
    ]
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    pool_path = resolve_project_path(args.candidate_pool)
    prompt_path = resolve_project_path(args.prompt)
    output_dir = resolve_project_path(args.output_dir)
    start = time.time()

    prompt_template = prompt_path.read_text(encoding="utf-8")
    rows = _read_csv(pool_path)
    cases = _group_cases(rows, args.pool_strategy, args.candidate_limit)
    if args.limit is not None:
        cases = cases[: args.limit]

    model_info = _model_info(args.ollama_tags_url, args.model, args.timeout_seconds)
    if not model_info.get("available"):
        raise RuntimeError(f"Ollama model not available via local API: {args.model}. Detail: {model_info.get('error', '')}")

    jsonl_rows: list[dict[str, Any]] = []
    result_rows: list[dict[str, Any]] = []
    for case in cases:
        prompt = _build_prompt(prompt_template, case, args.candidate_limit)
        allowed_codes = [row["candidate_code"] for row in case["candidates"]]
        sent_pool_contains_expected = case["nandina_ref"] in set(allowed_codes)
        raw_response = ""
        ollama_response: dict[str, Any] = {}
        error = ""
        started_case = time.time()
        try:
            raw_response, ollama_response = _call_ollama(
                url=args.ollama_url,
                model=args.model,
                prompt=prompt,
                response_schema=_response_schema(allowed_codes),
                temperature=args.temperature,
                top_p=args.top_p,
                num_predict=args.num_predict,
                timeout_seconds=args.timeout_seconds,
            )
        except (urllib.error.URLError, TimeoutError, OSError, RuntimeError) as exc:
            error = f"ollama_error: {exc}"
        raw_parsed, parse_error = _parse_json_response(raw_response) if raw_response else (None, "empty_response")
        if parse_error and not error:
            error = parse_error

        parsed, normalization_actions = _normalize_response(raw_parsed)

        ranked = parsed.get("ranked_candidates", []) if isinstance(parsed, dict) else []
        if not isinstance(ranked, list):
            ranked = []
        selected_nandina = _clean(parsed.get("selected_nandina")) if isinstance(parsed, dict) else ""
        ranked_codes = [_clean(item.get("nandina")) for item in ranked if isinstance(item, Mapping)]
        codes_outside_pool = sorted({code for code in [selected_nandina, *ranked_codes] if code and code not in set(allowed_codes)})
        duplicate_ranked_codes = len(ranked_codes) != len(set(ranked_codes))
        schema_errors = _validate_response(parsed, allowed_codes)
        json_parseable = int(parsed is not None and not parse_error)
        json_valid = int(json_parseable and not schema_errors)
        pool_violation = int(bool(codes_outside_pool))

        record = {
            "case_id": case["case_id"],
            "descripcion": case["descripcion"],
            "nandina_ref": case["nandina_ref"],
            "pool_strategy": args.pool_strategy,
            "candidate_limit": args.candidate_limit,
            "sent_pool_codes": allowed_codes,
            "sent_pool_contains_expected": sent_pool_contains_expected,
            "json_valid": bool(json_valid),
            "json_parseable": bool(json_parseable),
            "pool_violation": bool(pool_violation),
            "codes_outside_pool": codes_outside_pool,
            "duplicate_ranked_codes": duplicate_ranked_codes,
            "schema_errors": schema_errors,
            "selected_nandina": selected_nandina,
            "parsed_response": parsed,
            "raw_parsed_response": raw_parsed,
            "normalization_actions": normalization_actions,
            "raw_response": raw_response,
            "error": error,
            "elapsed_seconds": time.time() - started_case,
            "ollama_response_metadata": {key: value for key, value in ollama_response.items() if key != "message"},
        }
        jsonl_rows.append(record)
        result_rows.append(
            {
                "case_id": case["case_id"],
                "descripcion": case["descripcion"],
                "nandina_ref": case["nandina_ref"],
                "pool_strategy": args.pool_strategy,
                "candidate_limit": args.candidate_limit,
                "sent_pool_contains_expected": int(sent_pool_contains_expected),
                "json_valid": json_valid,
                "json_parseable": json_parseable,
                "pool_violation": pool_violation,
                "codes_outside_pool": " ".join(codes_outside_pool),
                "schema_errors": " | ".join(schema_errors),
                "normalization_actions": " | ".join(normalization_actions),
                "selected_nandina": selected_nandina,
                "ranked_candidates": " ".join(ranked_codes),
                "error": error,
                "elapsed_seconds": f"{record['elapsed_seconds']:.3f}",
            }
        )

    quality = {
        "cases_total": len(result_rows),
        "expected_cases_without_limit": EXPECTED_DEVSET_CASES,
        "valid_json_cases": sum(int(row["json_valid"]) for row in result_rows),
        "valid_json_rate": sum(int(row["json_valid"]) for row in result_rows) / len(result_rows) if result_rows else 0.0,
        "parseable_json_cases": sum(int(row["json_parseable"]) for row in result_rows),
        "pool_violation_cases": sum(int(row["pool_violation"]) for row in result_rows),
        "normalization_cases": sum(1 for row in result_rows if row["normalization_actions"]),
        "execution_error_cases": sum(1 for row in result_rows if row["error"] and not str(row["error"]).startswith("json_parse_error")),
        "sent_pool_contains_expected_cases": sum(int(row["sent_pool_contains_expected"]) for row in result_rows),
        "sent_pool_at_candidate_limit": (
            sum(int(row["sent_pool_contains_expected"]) for row in result_rows) / len(result_rows) if result_rows else 0.0
        ),
    }
    metadata: dict[str, Any] = {
        "script": "src.experiments.run_llm_rerank_pool_devset",
        "execution": {
            "datetime_utc": datetime.now(timezone.utc).isoformat(),
            "timestamp_unix": int(time.time()),
            "elapsed_seconds": time.time() - start,
            "environment": {
                "python_version": platform.python_version(),
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
            },
        },
        "input": {
            "candidate_pool_path": _rel(pool_path, root),
            "candidate_pool_sha256": sha256_file(pool_path),
            "prompt_path": _rel(prompt_path, root),
            "prompt_sha256": sha256_file(prompt_path),
        },
        "generation": {
            "model": args.model,
            "ollama_url": args.ollama_url,
            "ollama_tags_url": args.ollama_tags_url,
            "ollama_cli_available": False,
            "model_info": model_info.get("selected_model"),
            "prompt_version": "rerank_nandina_prompt_v0.1",
            "temperature": args.temperature,
            "top_p": args.top_p,
            "num_predict": args.num_predict,
            "timeout_seconds": args.timeout_seconds,
            "candidate_limit": args.candidate_limit,
            "pool_strategy": args.pool_strategy,
            "limit": args.limit,
        },
        "quality": quality,
        "controls": {
            "local_ollama_api_used": True,
            "paid_or_remote_api_used": False,
            "text2trade_executed": False,
            "llm_may_select_only_sent_pool": True,
        },
        "outputs": {
            "output_dir": _rel(output_dir, root),
            "rerank_responses_jsonl": _rel(output_dir / "rerank_responses.jsonl", root),
            "rerank_results_csv": _rel(output_dir / "rerank_results.csv", root),
            "rerank_metadata_json": _rel(output_dir / "rerank_metadata.json", root),
            "rerank_summary_md": _rel(output_dir / "rerank_summary.md", root),
        },
        "warnings": [
            "Do not compare LLM performance directly against final_pool@100 when candidate_limit is below 100.",
            "Conditioned metrics must use only cases where the expected code was inside the candidates sent to the LLM.",
        ],
    }

    ensure_parent(output_dir / "rerank_responses.jsonl")
    with (output_dir / "rerank_responses.jsonl").open("w", encoding="utf-8") as handle:
        for record in jsonl_rows:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    _write_csv(
        output_dir / "rerank_results.csv",
        result_rows,
        [
            "case_id",
            "descripcion",
            "nandina_ref",
            "pool_strategy",
            "candidate_limit",
            "sent_pool_contains_expected",
            "json_valid",
            "json_parseable",
            "pool_violation",
            "codes_outside_pool",
            "schema_errors",
            "normalization_actions",
            "selected_nandina",
            "ranked_candidates",
            "error",
            "elapsed_seconds",
        ],
    )
    _write_json(output_dir / "rerank_metadata.json", metadata)
    ensure_parent(output_dir / "rerank_summary.md")
    (output_dir / "rerank_summary.md").write_text(_summary_markdown(metadata), encoding="utf-8")
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local Ollama LLM reranking over candidate pool devset.")
    parser.add_argument("--candidate-pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--ollama-tags-url", default=DEFAULT_OLLAMA_TAGS_URL)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--num-predict", type=int, default=900)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    parser.add_argument("--candidate-limit", type=int, default=20)
    parser.add_argument("--pool-strategy", default=DEFAULT_POOL_STRATEGY)
    parser.add_argument("--limit", type=int, default=None, help="Optional technical smoke limit.")
    return parser


def main() -> int:
    metadata = run(build_parser().parse_args())
    quality = metadata["quality"]
    print("OK: reranking LLM devset completado")
    print(f"Casos procesados: {quality['cases_total']}")
    print(f"JSON valido: {quality['valid_json_cases']} ({quality['valid_json_rate']:.4f})")
    print(f"Violaciones de pool: {quality['pool_violation_cases']}")
    print(f"sent_pool_at_candidate_limit: {quality['sent_pool_at_candidate_limit']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
