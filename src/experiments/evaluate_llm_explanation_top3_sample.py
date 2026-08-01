from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_SAMPLE_CASES = Path("outputs/evaluation/llm_explanation_top3_sample_v0.1/sample_cases.csv")
DEFAULT_PAYLOADS = Path("outputs/evaluation/llm_explanation_top3_sample_v0.1/payloads.jsonl")
DEFAULT_EXPLANATIONS = Path("outputs/evaluation/llm_explanation_top3_sample_v0.1/llm_explanations.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_sample_v0.1")

EXPECTED_CASES = 30
EXPECTED_RANKS = [1, 2, 3]
SUPPORT_VALUES = {"alto", "medio", "bajo"}


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


def _read_jsonl(path: Path):
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            raw = line.strip()
            if raw:
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc


def _rel(path: Path) -> str:
    root = project_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


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


def _parse_response(row: Mapping[str, Any]) -> tuple[dict[str, Any] | None, str]:
    parsed = row.get("parsed_response")
    if isinstance(parsed, dict):
        return parsed, ""
    try:
        payload = json.loads(_strip_json(_clean(row.get("raw_response"))))
    except json.JSONDecodeError as exc:
        return None, str(exc)
    if not isinstance(payload, dict):
        return None, "top-level JSON is not an object"
    return payload, ""


def _candidate_codes(payload: Mapping[str, Any]) -> list[str]:
    return [_clean(row.get("nandina")) for row in payload.get("top3_original", [])]


def _candidate_ranks(payload: Mapping[str, Any]) -> list[int]:
    return [int(row.get("rank_original") or 0) for row in payload.get("top3_original", [])]


def _allowed_evidence_ids(payload: Mapping[str, Any]) -> set[str]:
    output: set[str] = set()
    for candidate in payload.get("top3_original", []):
        for evidence in candidate.get("evidencias_normativas", []):
            evidence_id = _clean(evidence.get("evidence_id"))
            if evidence_id:
                output.add(evidence_id)
    return output


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _supports_from(explained: Sequence[Mapping[str, Any]]) -> Counter[str]:
    return Counter(_clean(item.get("soporte")).lower() for item in explained)


def _has_evidence(item: Mapping[str, Any], allowed_ids: set[str]) -> bool:
    used = item.get("evidencias_usadas")
    if not isinstance(used, list) or not used:
        return False
    if not allowed_ids:
        return True
    for value in used:
        text = _clean(value)
        if text in allowed_ids or any(evidence_id in text for evidence_id in allowed_ids):
            return True
    return False


def _evaluate_case(
    sample: Mapping[str, str],
    payload: Mapping[str, Any],
    response_row: Mapping[str, Any] | None,
) -> dict[str, Any]:
    case_id = _clean(sample.get("case_id"))
    pool_codes = _candidate_codes(payload)
    pool_ranks = _candidate_ranks(payload)
    allowed_ids = _allowed_evidence_ids(payload)
    row: dict[str, Any] = {
        "case_id": case_id,
        "id_unico": _clean(sample.get("id_unico")),
        "expected_nandina": _clean(sample.get("expected_nandina")),
        "expected_rank_historical": int(_clean(sample.get("expected_rank_historical")) or "0"),
        "sample_target_category": _clean(sample.get("sample_target_category")),
        "selection_source_category": _clean(sample.get("selection_source_category")),
        "support_bucket": _clean(sample.get("support_bucket")),
        "historical_support_count": int(_clean(sample.get("historical_support_count")) or "0"),
        "json_valid": 0,
        "candidatos_explicados_completos": 0,
        "respeta_top3_original": 0,
        "no_agrega_candidatos_fuera_pool": 0,
        "no_cambia_ranking": 0,
        "no_inventa_codigos": 0,
        "evidencia_citada_por_candidato": 0,
        "advertencias_emitidas": 0,
        "comparacion_top3": 0,
        "diferencias_o_dudas": 0,
        "support_alto": 0,
        "support_medio": 0,
        "support_bajo": 0,
        "failure_types": "",
        "parse_error": "",
    }
    failures: list[str] = []
    if not response_row:
        row["parse_error"] = "missing_response"
        failures.append("missing_response")
        row["failure_types"] = "|".join(failures)
        return row

    parsed, parse_error = _parse_response(response_row)
    if parsed is None:
        row["parse_error"] = parse_error
        failures.append("json_invalid")
        row["failure_types"] = "|".join(failures)
        return row
    row["json_valid"] = 1

    explained = parsed.get("candidatos_explicados")
    if not isinstance(explained, list):
        explained = []
        failures.append("candidatos_explicados_missing_or_invalid")
    explained_dicts = [item for item in explained if isinstance(item, dict)]
    returned_codes = [_clean(item.get("nandina")) for item in explained_dicts]
    returned_ranks = [int(item.get("rank_original") or 0) for item in explained_dicts]

    complete_candidates = (
        len(explained_dicts) == 3
        and returned_ranks == EXPECTED_RANKS
        and all(code for code in returned_codes)
        and all(_clean(item.get("justificacion")) for item in explained_dicts)
        and all(_clean(item.get("soporte")).lower() in SUPPORT_VALUES for item in explained_dicts)
    )
    row["candidatos_explicados_completos"] = int(complete_candidates)
    if not complete_candidates:
        failures.append("candidatos_explicados_incompletos")

    row["respeta_top3_original"] = int(returned_codes == pool_codes and returned_ranks == pool_ranks)
    if not row["respeta_top3_original"]:
        failures.append("top3_original_no_respetado")

    outside_count = sum(1 for code in returned_codes if code and code not in set(pool_codes))
    row["no_agrega_candidatos_fuera_pool"] = int(outside_count == 0)
    row["no_inventa_codigos"] = int(outside_count == 0 and all(re.fullmatch(r"\d{8}", code or "") for code in returned_codes))
    if outside_count:
        failures.append("candidatos_fuera_pool")
    if not row["no_inventa_codigos"]:
        failures.append("codigos_inventados_o_invalidos")

    row["no_cambia_ranking"] = int(returned_ranks == pool_ranks and returned_codes == pool_codes)
    if not row["no_cambia_ranking"]:
        failures.append("ranking_modificado")

    evidence_flags = [_has_evidence(item, allowed_ids) for item in explained_dicts]
    row["evidencia_citada_por_candidato"] = int(len(evidence_flags) == 3 and all(evidence_flags))
    if not row["evidencia_citada_por_candidato"]:
        failures.append("evidencia_no_citada_por_candidato")

    warnings = parsed.get("advertencias")
    row["advertencias_emitidas"] = int(isinstance(warnings, list) and len(warnings) > 0)
    row["comparacion_top3"] = int(bool(_clean(parsed.get("comparacion_top3"))))
    if not row["comparacion_top3"]:
        failures.append("comparacion_top3_ausente")

    row["diferencias_o_dudas"] = int(
        any(isinstance(item.get("diferencias_o_dudas"), list) and item.get("diferencias_o_dudas") for item in explained_dicts)
    )
    support_counts = _supports_from(explained_dicts)
    row["support_alto"] = support_counts["alto"]
    row["support_medio"] = support_counts["medio"]
    row["support_bajo"] = support_counts["bajo"]
    row["failure_types"] = "|".join(dict.fromkeys(failures))
    return row


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    lines = [
        "# Evaluacion LLM explicacion Top-3 sample v0.1",
        "",
        "## Resultado",
        "",
        f"- Modelo: `{payload['model']}`.",
        f"- Casos esperados: {payload['expected_cases']}.",
        f"- Casos procesados: {metrics['casos_procesados']}.",
        f"- JSON valido: {metrics['json_valido_rate']:.4f}.",
        f"- Candidatos explicados completos: {metrics['candidatos_explicados_completos_rate']:.4f}.",
        f"- Respeta Top-3 original: {metrics['respeta_top3_original_rate']:.4f}.",
        f"- No cambia ranking: {metrics['no_cambia_ranking_rate']:.4f}.",
        f"- Evidencia citada por candidato: {metrics['evidencia_citada_por_candidato_rate']:.4f}.",
        f"- Comparacion Top-3 presente: {metrics['comparacion_top3_rate']:.4f}.",
        "",
        "## Decision",
        "",
        payload["decision"],
        "",
        "## Fallos por tipo",
        "",
        "| Tipo | Casos |",
        "| --- | ---: |",
    ]
    for failure_type, count in payload["fallos_por_tipo"].items():
        lines.append(f"| `{failure_type}` | {count} |")
    if not payload["fallos_por_tipo"]:
        lines.append("| sin_fallos | 0 |")
    lines.append("")
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    sample_path = resolve_project_path(args.sample_cases)
    payloads_path = resolve_project_path(args.payloads)
    explanations_path = resolve_project_path(args.explanations)
    output_dir = resolve_project_path(args.output_dir)

    sample_rows = _read_csv(sample_path)
    payloads = list(_read_jsonl(payloads_path))
    responses = list(_read_jsonl(explanations_path))
    if len(sample_rows) != EXPECTED_CASES:
        raise ValueError(f"Expected {EXPECTED_CASES} sample cases, found {len(sample_rows)}")
    if len(payloads) != EXPECTED_CASES:
        raise ValueError(f"Expected {EXPECTED_CASES} payloads, found {len(payloads)}")
    if len(responses) != EXPECTED_CASES:
        raise ValueError(f"Expected {EXPECTED_CASES} LLM responses, found {len(responses)}")

    payload_by_case = {_clean(row.get("case_id")): row for row in payloads}
    response_by_case = {_clean(row.get("case_id")): row for row in responses}
    case_rows = [_evaluate_case(row, payload_by_case[_clean(row.get("case_id"))], response_by_case.get(_clean(row.get("case_id")))) for row in sample_rows]

    metrics = {
        "casos_procesados": len(case_rows),
        "json_valido": sum(row["json_valid"] for row in case_rows),
        "json_valido_rate": _mean([row["json_valid"] for row in case_rows]),
        "candidatos_explicados_completos": sum(row["candidatos_explicados_completos"] for row in case_rows),
        "candidatos_explicados_completos_rate": _mean([row["candidatos_explicados_completos"] for row in case_rows]),
        "respeta_top3_original": sum(row["respeta_top3_original"] for row in case_rows),
        "respeta_top3_original_rate": _mean([row["respeta_top3_original"] for row in case_rows]),
        "no_agrega_candidatos_fuera_pool": sum(row["no_agrega_candidatos_fuera_pool"] for row in case_rows),
        "no_agrega_candidatos_fuera_pool_rate": _mean([row["no_agrega_candidatos_fuera_pool"] for row in case_rows]),
        "no_cambia_ranking": sum(row["no_cambia_ranking"] for row in case_rows),
        "no_cambia_ranking_rate": _mean([row["no_cambia_ranking"] for row in case_rows]),
        "no_inventa_codigos": sum(row["no_inventa_codigos"] for row in case_rows),
        "no_inventa_codigos_rate": _mean([row["no_inventa_codigos"] for row in case_rows]),
        "evidencia_citada_por_candidato": sum(row["evidencia_citada_por_candidato"] for row in case_rows),
        "evidencia_citada_por_candidato_rate": _mean([row["evidencia_citada_por_candidato"] for row in case_rows]),
        "advertencias_emitidas": sum(row["advertencias_emitidas"] for row in case_rows),
        "advertencias_emitidas_rate": _mean([row["advertencias_emitidas"] for row in case_rows]),
        "proporcion_diferencias_o_dudas": _mean([row["diferencias_o_dudas"] for row in case_rows]),
        "comparacion_top3": sum(row["comparacion_top3"] for row in case_rows),
        "comparacion_top3_rate": _mean([row["comparacion_top3"] for row in case_rows]),
        "support_alto_candidatos": sum(row["support_alto"] for row in case_rows),
        "support_medio_candidatos": sum(row["support_medio"] for row in case_rows),
        "support_bajo_candidatos": sum(row["support_bajo"] for row in case_rows),
        "median_historical_expected_rank": _median([row["expected_rank_historical"] for row in case_rows if row["expected_rank_historical"]]),
    }
    failure_counter: Counter[str] = Counter()
    for row in case_rows:
        for failure in _clean(row.get("failure_types")).split("|"):
            if failure:
                failure_counter[failure] += 1

    passes = (
        metrics["casos_procesados"] == EXPECTED_CASES
        and metrics["json_valido_rate"] >= 0.95
        and metrics["candidatos_explicados_completos_rate"] >= 0.95
        and metrics["respeta_top3_original_rate"] == 1.0
        and metrics["no_agrega_candidatos_fuera_pool_rate"] == 1.0
        and metrics["no_cambia_ranking_rate"] == 1.0
        and metrics["no_inventa_codigos_rate"] == 1.0
        and metrics["evidencia_citada_por_candidato_rate"] >= 0.90
        and metrics["comparacion_top3_rate"] >= 0.90
    )
    decision = (
        "Pasa a Fase 10B como explicacion controlada: la muestra diagnostica cumple controles estructurales y de auditabilidad basica."
        if passes
        else "No pasa aun a Fase 10B: requiere ajustar prompt, payload o controles antes de escalar la explicacion."
    )

    model = _clean(responses[0].get("model")) if responses else args.model
    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "10A_llm_explanation_top3_sample",
        "model": model,
        "expected_cases": EXPECTED_CASES,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "sample_cases": _rel(sample_path),
            "payloads": _rel(payloads_path),
            "llm_explanations": _rel(explanations_path),
        },
        "metrics": metrics,
        "fallos_por_tipo": dict(sorted(failure_counter.items())),
        "decision": decision,
        "policy": {
            "llm_role": "explanation_only",
            "retrieval_used_by_llm": False,
            "reranking_allowed": False,
            "openai_used": False,
            "remote_api_used": False,
            "ollama_local_only": True,
        },
        "outputs": {
            "explanation_quality_metrics_json": _rel(output_dir / "explanation_quality_metrics.json"),
            "explanation_quality_summary_md": _rel(output_dir / "explanation_quality_summary.md"),
            "case_quality_summary_csv": _rel(output_dir / "case_quality_summary.csv"),
        },
    }
    fieldnames = [
        "case_id",
        "id_unico",
        "expected_nandina",
        "expected_rank_historical",
        "sample_target_category",
        "selection_source_category",
        "support_bucket",
        "historical_support_count",
        "json_valid",
        "candidatos_explicados_completos",
        "respeta_top3_original",
        "no_agrega_candidatos_fuera_pool",
        "no_cambia_ranking",
        "no_inventa_codigos",
        "evidencia_citada_por_candidato",
        "advertencias_emitidas",
        "comparacion_top3",
        "diferencias_o_dudas",
        "support_alto",
        "support_medio",
        "support_bajo",
        "failure_types",
        "parse_error",
    ]
    _write_csv(output_dir / "case_quality_summary.csv", case_rows, fieldnames)
    _write_json(output_dir / "explanation_quality_metrics.json", payload)
    ensure_parent(output_dir / "explanation_quality_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate structural quality and auditability of Top-3 LLM explanations.")
    parser.add_argument("--sample-cases", default=str(DEFAULT_SAMPLE_CASES))
    parser.add_argument("--payloads", default=str(DEFAULT_PAYLOADS))
    parser.add_argument("--explanations", default=str(DEFAULT_EXPLANATIONS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default="qwen2.5:7b-instruct")
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: evaluacion estructural LLM explicacion Top-3 completada")
    print(
        f"casos={metrics['casos_procesados']} json={metrics['json_valido_rate']:.4f} "
        f"top3={metrics['respeta_top3_original_rate']:.4f} evidencia={metrics['evidencia_citada_por_candidato_rate']:.4f}"
    )
    print(payload["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
