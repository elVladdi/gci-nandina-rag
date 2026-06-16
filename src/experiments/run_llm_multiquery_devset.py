from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_PROMPT = Path("src/llm/multiquery_prompt_v0.1.md")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/multiquery_rrf_devset_v0.1")
DEFAULT_MODEL = "qwen2.5:7b-instruct"
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
EXPECTED_DEVSET_ROWS = 13
QUERY_FIELDS = ("q1_limpia", "q2_expandida", "q3_terminos_clave")

CODE_PATTERN = re.compile(r"(?<![\w.])(?:\d{4}|\d{6}|\d{8}|\d{10})(?![\w.])")
QUANTITY_CONTEXT_PATTERN = re.compile(
    r"^\s*(unidades?|piezas?|pares?|kg|kilogramos?|g|gramos?|mg|toneladas?|litros?|l|ml|metros?|m|cm|mm|gb|tb|mb|"
    r"pulgadas?|envases?|latas?|sacos?|paquetes?|cajas?|botellas?)\b",
    flags=re.IGNORECASE,
)
FORBIDDEN_TERMS = re.compile(
    r"\b(nandina|arancelari[oa]s?|cap[ií]tulos?|partidas?|subpartidas?|c[oó]digos?)\b",
    flags=re.IGNORECASE,
)


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


def _report_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return str(resolved)


def _extract_text_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        values: list[str] = []
        for nested in value.values():
            values.extend(_extract_text_values(nested))
        return values
    if isinstance(value, list):
        values = []
        for nested in value:
            values.extend(_extract_text_values(nested))
        return values
    return []


def _code_like_matches(text: str) -> list[str]:
    matches: list[str] = []
    for match in CODE_PATTERN.finditer(text):
        following = text[match.end() : match.end() + 32]
        if QUANTITY_CONTEXT_PATTERN.match(following):
            continue
        matches.append(match.group(0))
    return matches


def _detect_violations(raw_response: str, parsed_json: Mapping[str, Any] | None) -> tuple[list[str], list[str]]:
    texts = [raw_response]
    if parsed_json is not None:
        texts.extend(_extract_text_values(parsed_json))
    joined = "\n".join(texts)
    codes = sorted(set(_code_like_matches(joined)))
    forbidden = sorted(set(match.group(0).lower() for match in FORBIDDEN_TERMS.finditer(joined)))
    return codes, forbidden


def _parse_json_response(raw_response: str) -> tuple[dict[str, Any] | None, str]:
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        return None, f"json_parse_error: {exc.msg}"
    if not isinstance(parsed, dict):
        return None, "json_parse_error: root is not an object"
    return parsed, ""


def _validate_multiquery(parsed_json: Mapping[str, Any] | None) -> list[str]:
    warnings: list[str] = []
    if parsed_json is None:
        return ["json_invalid"]
    for field in QUERY_FIELDS:
        if not isinstance(parsed_json.get(field), str) or not _clean(parsed_json.get(field)):
            warnings.append(f"empty_or_invalid_{field}")
    if "advertencias" in parsed_json and not isinstance(parsed_json.get("advertencias"), list):
        warnings.append("advertencias_not_list")
    return warnings


def _call_ollama(
    *,
    url: str,
    model: str,
    prompt: str,
    temperature: float,
    top_p: float,
    num_predict: int,
    timeout_seconds: int,
) -> tuple[str, dict[str, Any]]:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": "json",
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        response_payload = json.loads(response.read().decode("utf-8"))
    message = response_payload.get("message", {})
    content = _clean(message.get("content"))
    return content, response_payload


def _summary_markdown(metadata: Mapping[str, Any]) -> str:
    quality = metadata["quality"]
    generation = metadata["generation"]
    lines = [
        "# LLM multi-query devset v0.1",
        "",
        "## Alcance",
        "",
        "Generacion controlada de tres variantes complementarias para los 13 casos del devset. Q0 se conserva desde el devset y no se solicita al LLM. No se ejecuto sobre el evalset final.",
        "",
        "## Modelo",
        "",
        f"- Modelo Ollama: `{generation['model']}`.",
        f"- API: `{generation['ollama_url']}`.",
        f"- Temperature: {generation['temperature']}.",
        f"- Top-p: {generation['top_p']}.",
        f"- Max tokens generados (`num_predict`): {generation['num_predict']}.",
        "",
        "## Calidad automatica",
        "",
        f"- Casos procesados: {quality['cases_total']}.",
        f"- JSON valido: {quality['valid_json_cases']} ({quality['valid_json_rate']:.4f}).",
        f"- Campos Q1-Q3 completos: {quality['complete_query_cases']}.",
        f"- Violaciones por codigos: {quality['code_violation_cases']}.",
        f"- Violaciones por terminos prohibidos: {quality['forbidden_term_cases']}.",
        "",
        "## Advertencias",
        "",
    ]
    warnings = metadata.get("warnings") or []
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- Sin advertencias automaticas globales.")
    lines.append("")
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    prompt_path = resolve_project_path(args.prompt)
    output_dir = resolve_project_path(args.output_dir)

    rows = _read_csv(devset_path)
    if args.max_cases is not None:
        rows = rows[: args.max_cases]
    if len(rows) != EXPECTED_DEVSET_ROWS and args.max_cases is None:
        raise ValueError(f"Devset row count is {len(rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    prompt_template = prompt_path.read_text(encoding="utf-8")
    result_rows: list[dict[str, Any]] = []
    jsonl_rows: list[dict[str, Any]] = []
    start = time.time()

    for position, row in enumerate(rows, start=1):
        descripcion = _clean(row.get("descripcion"))
        nandina_ref = _clean(row.get("nandina"))
        prompt = prompt_template.replace("{{descripcion}}", descripcion)
        attempts = 0
        raw_response = ""
        api_response: dict[str, Any] = {}
        call_error = ""

        while attempts <= args.max_retries:
            attempts += 1
            try:
                raw_response, api_response = _call_ollama(
                    url=args.ollama_url,
                    model=args.model,
                    prompt=prompt,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    num_predict=args.num_predict,
                    timeout_seconds=args.timeout_seconds,
                )
                break
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                call_error = f"{type(exc).__name__}: {exc}"
                if attempts > args.max_retries:
                    raw_response = ""
                    api_response = {}

        parsed_json, parse_warning = _parse_json_response(raw_response) if raw_response else (None, "empty_response")
        validation_warnings = _validate_multiquery(parsed_json)
        code_matches, forbidden_terms = _detect_violations(raw_response, parsed_json)
        q1 = _clean(parsed_json.get("q1_limpia")) if parsed_json else ""
        q2 = _clean(parsed_json.get("q2_expandida")) if parsed_json else ""
        q3 = _clean(parsed_json.get("q3_terminos_clave")) if parsed_json else ""
        llm_warnings = parsed_json.get("advertencias", []) if isinstance(parsed_json, Mapping) else []
        if not isinstance(llm_warnings, list):
            llm_warnings = [str(llm_warnings)]

        warnings = []
        if call_error and not raw_response:
            warnings.append(call_error)
        if parse_warning:
            warnings.append(parse_warning)
        warnings.extend(validation_warnings)
        if code_matches:
            warnings.append("possible_tariff_code_detected")
        if forbidden_terms:
            warnings.append("forbidden_tariff_term_detected")

        record: dict[str, Any] = {
            "case_id": f"dev-{position:02d}",
            "descripcion_original": descripcion,
            "nandina_ref": nandina_ref,
            "q0_original": descripcion,
            "q1_limpia": q1,
            "q2_expandida": q2,
            "q3_terminos_clave": q3,
            "advertencias_llm": llm_warnings,
            "model": args.model,
            "attempts": attempts,
            "raw_response": raw_response,
            "parsed_json": parsed_json,
            "json_valid": int(parsed_json is not None),
            "queries_complete": int(bool(q1 and q2 and q3)),
            "code_violation": int(bool(code_matches)),
            "code_matches": code_matches,
            "forbidden_term_violation": int(bool(forbidden_terms)),
            "forbidden_terms": forbidden_terms,
            "warnings": warnings,
            "ollama_eval_count": api_response.get("eval_count"),
            "ollama_eval_duration": api_response.get("eval_duration"),
        }
        jsonl_rows.append(record)
        result_rows.append(
            {
                "case_id": record["case_id"],
                "descripcion_original": descripcion,
                "nandina_ref": nandina_ref,
                "q0_original": descripcion,
                "q1_limpia": q1,
                "q2_expandida": q2,
                "q3_terminos_clave": q3,
                "advertencias_llm": "; ".join(str(item) for item in llm_warnings),
                "json_valid": record["json_valid"],
                "queries_complete": record["queries_complete"],
                "code_violation": record["code_violation"],
                "code_matches": "; ".join(code_matches),
                "forbidden_term_violation": record["forbidden_term_violation"],
                "forbidden_terms": "; ".join(forbidden_terms),
                "warnings": "; ".join(warnings),
                "raw_response": raw_response,
            }
        )

    quality = {
        "cases_total": len(result_rows),
        "valid_json_cases": sum(int(row["json_valid"]) for row in result_rows),
        "valid_json_rate": sum(int(row["json_valid"]) for row in result_rows) / len(result_rows) if result_rows else 0.0,
        "complete_query_cases": sum(int(row["queries_complete"]) for row in result_rows),
        "code_violation_cases": sum(int(row["code_violation"]) for row in result_rows),
        "forbidden_term_cases": sum(int(row["forbidden_term_violation"]) for row in result_rows),
    }
    warnings: list[str] = []
    if quality["cases_total"] != EXPECTED_DEVSET_ROWS and args.max_cases is None:
        warnings.append(f"Expected {EXPECTED_DEVSET_ROWS} cases, processed {quality['cases_total']}.")
    if quality["valid_json_cases"] != quality["cases_total"]:
        warnings.append("At least one case did not return valid strict JSON.")
    if quality["complete_query_cases"] != quality["cases_total"]:
        warnings.append("At least one case has an empty Q1/Q2/Q3 field.")
    if quality["code_violation_cases"]:
        warnings.append("At least one output contains a possible 4/6/8/10 digit tariff code.")
    if quality["forbidden_term_cases"]:
        warnings.append("At least one output contains forbidden tariff terminology.")

    metadata: dict[str, Any] = {
        "script": "src.experiments.run_llm_multiquery_devset",
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
            "devset_path": _report_path(devset_path, root),
            "devset_abs_path": str(devset_path),
            "devset_sha256": sha256_file(devset_path),
            "prompt_path": _report_path(prompt_path, root),
            "prompt_abs_path": str(prompt_path),
            "prompt_sha256": sha256_file(prompt_path),
        },
        "generation": {
            "model": args.model,
            "ollama_url": args.ollama_url,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "num_predict": args.num_predict,
            "timeout_seconds": args.timeout_seconds,
            "max_retries": args.max_retries,
            "format": "json",
        },
        "quality": quality,
        "warnings": warnings,
        "output": {
            "output_dir": _report_path(output_dir, root),
            "output_abs_dir": str(output_dir),
            "multiqueries_jsonl": _report_path(output_dir / "multiqueries.jsonl", root),
            "multiqueries_csv": _report_path(output_dir / "multiqueries.csv", root),
            "metadata_json": _report_path(output_dir / "metadata.json", root),
            "summary_md": _report_path(output_dir / "summary.md", root),
        },
    }

    ensure_parent(output_dir / "multiqueries.jsonl")
    with (output_dir / "multiqueries.jsonl").open("w", encoding="utf-8") as handle:
        for record in jsonl_rows:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    _write_csv(
        output_dir / "multiqueries.csv",
        result_rows,
        [
            "case_id",
            "descripcion_original",
            "nandina_ref",
            "q0_original",
            "q1_limpia",
            "q2_expandida",
            "q3_terminos_clave",
            "advertencias_llm",
            "json_valid",
            "queries_complete",
            "code_violation",
            "code_matches",
            "forbidden_term_violation",
            "forbidden_terms",
            "warnings",
            "raw_response",
        ],
    )
    _write_json(output_dir / "metadata.json", metadata)
    ensure_parent(output_dir / "summary.md")
    (output_dir / "summary.md").write_text(_summary_markdown(metadata), encoding="utf-8")
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local LLM multi-query generation on the 13-case devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--num-predict", type=int, default=768)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    parser.add_argument("--max-retries", type=int, default=1)
    parser.add_argument("--max-cases", type=int, default=None, help="Debug guard; omit for the full 13-case devset.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    metadata = run(args)
    quality = metadata["quality"]
    print("OK: generacion LLM multi-query devset completada")
    print(f"Casos procesados: {quality['cases_total']}")
    print(f"JSON valido: {quality['valid_json_cases']} ({quality['valid_json_rate']:.4f})")
    print(f"Campos Q1-Q3 completos: {quality['complete_query_cases']}")
    print(f"Violaciones por codigos: {quality['code_violation_cases']}")
    print(f"Violaciones por terminos prohibidos: {quality['forbidden_term_cases']}")
    print(f"Outputs: {metadata['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
