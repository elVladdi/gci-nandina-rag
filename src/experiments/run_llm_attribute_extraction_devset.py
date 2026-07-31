from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_PROMPT = Path("src/llm/attribute_extraction_prompt_v0.1.md")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_attribute_retrieval_devset_v0.1")
DEFAULT_MODEL = "qwen2.5:7b-instruct"
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
EXPECTED_DEVSET_ROWS = 13

STRING_FIELDS = (
    "producto",
    "material",
    "composicion",
    "uso_funcion",
    "presentacion",
    "estado",
    "tecnologia",
    "medidas",
    "marca_modelo",
)
LIST_FIELDS = ("atributos_discriminantes", "terminos_busqueda", "advertencias")
SCHEMA_FIELDS = STRING_FIELDS + LIST_FIELDS

CODE_PATTERN = re.compile(r"(?<![\w.])(?:\d{4}|\d{6}|\d{8}|\d{10})(?![\w.])")
QUANTITY_CONTEXT_PATTERN = re.compile(
    r"^\s*(unidades?|piezas?|pares?|kg|kilogramos?|g|gramos?|mg|toneladas?|litros?|l|ml|metros?|m|cm|mm|gb|tb|mb|"
    r"pulgadas?|envases?|latas?|sacos?|paquetes?|cajas?|botellas?)\b",
    flags=re.IGNORECASE,
)
FORBIDDEN_NORMALIZED_PATTERN = re.compile(
    r"\b(nandina|arancelari[oa]s?|capitulos?|partidas?|subpartidas?|codigos?)\b",
    flags=re.IGNORECASE,
)


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(text: object) -> str:
    raw = unicodedata.normalize("NFKD", _clean(text).lower())
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


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
    forbidden = sorted(set(match.group(0).lower() for match in FORBIDDEN_NORMALIZED_PATTERN.finditer(_norm(joined))))
    return codes, forbidden


def _parse_json_response(raw_response: str) -> tuple[dict[str, Any] | None, str]:
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        return None, f"json_parse_error: {exc.msg}"
    if not isinstance(parsed, dict):
        return None, "json_parse_error: root is not an object"
    return parsed, ""


def _normalize_extraction(parsed_json: Mapping[str, Any] | None) -> dict[str, Any]:
    normalized: dict[str, Any] = {field: "" for field in STRING_FIELDS}
    normalized.update({field: [] for field in LIST_FIELDS})
    if parsed_json is None:
        return normalized
    for field in STRING_FIELDS:
        value = parsed_json.get(field, "")
        normalized[field] = _clean(value) if isinstance(value, str) else _clean(value)
    for field in LIST_FIELDS:
        value = parsed_json.get(field, [])
        if isinstance(value, list):
            normalized[field] = [_clean(item) for item in value if _clean(item)]
        elif _clean(value):
            normalized[field] = [_clean(value)]
        else:
            normalized[field] = []
    return normalized


def _validate_schema(parsed_json: Mapping[str, Any] | None) -> list[str]:
    if parsed_json is None:
        return ["json_invalid"]
    warnings: list[str] = []
    for field in SCHEMA_FIELDS:
        if field not in parsed_json:
            warnings.append(f"missing_{field}")
    for field in STRING_FIELDS:
        if field in parsed_json and not isinstance(parsed_json.get(field), str):
            warnings.append(f"non_string_{field}")
    for field in LIST_FIELDS:
        if field in parsed_json and not isinstance(parsed_json.get(field), list):
            warnings.append(f"non_list_{field}")
    extra_fields = sorted(set(parsed_json.keys()) - set(SCHEMA_FIELDS))
    if extra_fields:
        warnings.append("extra_fields:" + ",".join(extra_fields))
    return warnings


def _possible_invented_fields(descripcion: str, extraction: Mapping[str, Any]) -> list[str]:
    source_tokens = {token for token in _norm(descripcion).split() if len(token) >= 4}
    findings: list[str] = []
    for field in STRING_FIELDS:
        if field == "marca_modelo":
            continue
        value = _clean(extraction.get(field))
        if not value:
            continue
        value_tokens = {token for token in _norm(value).split() if len(token) >= 4}
        if value_tokens and not (value_tokens & source_tokens):
            findings.append(field)
    return findings


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
        nandina_ref = _clean(row.get("nandina") or row.get("nandina_ref"))
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
        extraction = _normalize_extraction(parsed_json)
        schema_warnings = _validate_schema(parsed_json)
        code_matches, forbidden_terms = _detect_violations(raw_response, parsed_json)
        possible_invented = _possible_invented_fields(descripcion, extraction)

        warnings = []
        if call_error and not raw_response:
            warnings.append(call_error)
        if parse_warning:
            warnings.append(parse_warning)
        warnings.extend(schema_warnings)
        if code_matches:
            warnings.append("possible_tariff_code_detected")
        if forbidden_terms:
            warnings.append("forbidden_tariff_term_detected")
        if possible_invented:
            warnings.append("possible_invented_attributes:" + ",".join(possible_invented))

        record: dict[str, Any] = {
            "case_id": f"dev-{position:02d}",
            "descripcion_original": descripcion,
            "nandina_ref": nandina_ref,
            "model": args.model,
            "attempts": attempts,
            "raw_response": raw_response,
            "parsed_json": parsed_json,
            "extraction": extraction,
            "json_valid": int(parsed_json is not None),
            "schema_valid": int(parsed_json is not None and not schema_warnings),
            "code_violation": int(bool(code_matches)),
            "code_matches": code_matches,
            "forbidden_term_violation": int(bool(forbidden_terms)),
            "forbidden_terms": forbidden_terms,
            "possible_invented_attribute_violation": int(bool(possible_invented)),
            "possible_invented_fields": possible_invented,
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
                **{field: extraction[field] for field in STRING_FIELDS},
                "atributos_discriminantes": "; ".join(extraction["atributos_discriminantes"]),
                "terminos_busqueda": "; ".join(extraction["terminos_busqueda"]),
                "advertencias": "; ".join(extraction["advertencias"]),
                "json_valid": record["json_valid"],
                "schema_valid": record["schema_valid"],
                "code_violation": record["code_violation"],
                "code_matches": "; ".join(code_matches),
                "forbidden_term_violation": record["forbidden_term_violation"],
                "forbidden_terms": "; ".join(forbidden_terms),
                "possible_invented_attribute_violation": record["possible_invented_attribute_violation"],
                "possible_invented_fields": "; ".join(possible_invented),
                "warnings": "; ".join(warnings),
                "raw_response": raw_response,
            }
        )

    quality = {
        "cases_total": len(result_rows),
        "valid_json_cases": sum(int(row["json_valid"]) for row in result_rows),
        "schema_valid_cases": sum(int(row["schema_valid"]) for row in result_rows),
        "valid_json_rate": sum(int(row["json_valid"]) for row in result_rows) / len(result_rows) if result_rows else 0.0,
        "code_violation_cases": sum(int(row["code_violation"]) for row in result_rows),
        "forbidden_term_cases": sum(int(row["forbidden_term_violation"]) for row in result_rows),
        "possible_invented_attribute_cases": sum(int(row["possible_invented_attribute_violation"]) for row in result_rows),
    }
    warnings: list[str] = []
    if quality["cases_total"] != EXPECTED_DEVSET_ROWS and args.max_cases is None:
        warnings.append(f"Expected {EXPECTED_DEVSET_ROWS} cases, processed {quality['cases_total']}.")
    if quality["valid_json_cases"] != quality["cases_total"]:
        warnings.append("At least one case did not return valid strict JSON.")
    if quality["schema_valid_cases"] != quality["cases_total"]:
        warnings.append("At least one case did not match the requested schema exactly.")
    if quality["code_violation_cases"]:
        warnings.append("At least one output contains a possible 4/6/8/10 digit tariff code.")
    if quality["forbidden_term_cases"]:
        warnings.append("At least one output contains forbidden tariff terminology.")
    if quality["possible_invented_attribute_cases"]:
        warnings.append("Heuristic found possible invented attributes; review case CSV.")

    metadata: dict[str, Any] = {
        "script": "src.experiments.run_llm_attribute_extraction_devset",
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
            "devset_path": _rel(devset_path, root),
            "devset_abs_path": str(devset_path),
            "devset_sha256": sha256_file(devset_path),
            "prompt_path": _rel(prompt_path, root),
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
            "remote_apis_used": False,
            "text2trade_used": False,
            "evalset_executed": False,
        },
        "quality": quality,
        "warnings": warnings,
        "output": {
            "output_dir": _rel(output_dir, root),
            "attribute_extractions_jsonl": _rel(output_dir / "attribute_extractions.jsonl", root),
            "attribute_extractions_csv": _rel(output_dir / "attribute_extractions.csv", root),
            "attribute_metadata_json": _rel(output_dir / "attribute_metadata.json", root),
        },
    }

    ensure_parent(output_dir / "attribute_extractions.jsonl")
    with (output_dir / "attribute_extractions.jsonl").open("w", encoding="utf-8") as handle:
        for record in jsonl_rows:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    _write_csv(
        output_dir / "attribute_extractions.csv",
        result_rows,
        [
            "case_id",
            "descripcion_original",
            "nandina_ref",
            *STRING_FIELDS,
            "atributos_discriminantes",
            "terminos_busqueda",
            "advertencias",
            "json_valid",
            "schema_valid",
            "code_violation",
            "code_matches",
            "forbidden_term_violation",
            "forbidden_terms",
            "possible_invented_attribute_violation",
            "possible_invented_fields",
            "warnings",
            "raw_response",
        ],
    )
    _write_json(output_dir / "attribute_metadata.json", metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local LLM attribute extraction on the 13-case devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--num-predict", type=int, default=1024)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    parser.add_argument("--max-retries", type=int, default=1)
    parser.add_argument("--max-cases", type=int, default=None, help="Debug guard; omit for the full 13-case devset.")
    return parser


def main() -> int:
    metadata = run(build_parser().parse_args())
    quality = metadata["quality"]
    print("OK: extraccion LLM de atributos devset completada")
    print(f"Casos procesados: {quality['cases_total']}")
    print(f"JSON valido: {quality['valid_json_cases']} ({quality['valid_json_rate']:.4f})")
    print(f"Schema valido: {quality['schema_valid_cases']}")
    print(f"Violaciones por codigos: {quality['code_violation_cases']}")
    print(f"Violaciones por terminos prohibidos: {quality['forbidden_term_cases']}")
    print(f"Posibles atributos inventados: {quality['possible_invented_attribute_cases']}")
    print(f"Outputs: {metadata['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
