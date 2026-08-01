from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_SAMPLE_CASES = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/sample_cases.csv")
DEFAULT_PAYLOADS = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/payloads.jsonl")
DEFAULT_EXPLANATIONS = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/llm_explanations.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1")

EXPECTED_CASES = 50
EXPECTED_RANKS = [1, 2, 3]
SUPPORT_VALUES = {"alto", "medio", "bajo"}
FINAL_WARNING_FRAGMENT = "no reemplaza la clasificacion oficial"
OFFICIAL_CLASSIFICATION_PATTERNS = [
    "clasificacion oficial es",
    "clasificación oficial es",
    "debe clasificarse",
    "se clasifica oficialmente",
    "codigo correcto es",
    "código correcto es",
]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(value: object) -> str:
    text = unicodedata.normalize("NFKD", _clean(value)).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text).lower().strip()


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


def _candidate_ids_by_rank(payload: Mapping[str, Any]) -> dict[int, str]:
    return {int(row.get("rank_original") or 0): _clean(row.get("candidate_id_unico")) for row in payload.get("top3_original", [])}


def _evidence_ids_by_rank(payload: Mapping[str, Any]) -> dict[int, set[str]]:
    output: dict[int, set[str]] = {}
    for candidate in payload.get("top3_original", []):
        rank = int(candidate.get("rank_original") or 0)
        output[rank] = {
            _clean(evidence.get("evidence_id"))
            for evidence in candidate.get("evidencias_normativas", [])
            if _clean(evidence.get("evidence_id"))
        }
    return output


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _text_blob(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return _clean(value)


def _has_historical_evidence(item: Mapping[str, Any], expected_id: str) -> bool:
    evidence = _as_list(item.get("evidencia_historica_usada"))
    if not evidence or not expected_id:
        return False
    for entry in evidence:
        if isinstance(entry, dict) and _clean(entry.get("candidate_id_unico")) == expected_id:
            return bool(_clean(entry.get("fragmento_usado")) or _as_list(entry.get("atributos_coincidentes")))
        if expected_id in _text_blob(entry):
            return True
    return False


def _has_normative_evidence(item: Mapping[str, Any], allowed_ids: set[str]) -> bool:
    evidence = _as_list(item.get("evidencia_normativa_usada"))
    if not evidence or not allowed_ids:
        return False
    for entry in evidence:
        if isinstance(entry, dict) and _clean(entry.get("evidence_id")) in allowed_ids:
            return bool(_clean(entry.get("texto_citado")) or _as_list(entry.get("atributos_coincidentes")))
        if any(evidence_id in _text_blob(entry) for evidence_id in allowed_ids):
            return True
    return False


def _generic_normative_warning(item: Mapping[str, Any], payload_candidate: Mapping[str, Any]) -> bool:
    evidence_text = " ".join(_clean(ev.get("texto")) for ev in payload_candidate.get("evidencias_normativas", []))
    if "los demas" not in _norm(evidence_text):
        return True
    warnings = _as_list(item.get("advertencias"))
    limitations = []
    for evidence in _as_list(item.get("evidencia_normativa_usada")):
        if isinstance(evidence, dict):
            limitations.extend(_as_list(evidence.get("limitaciones")))
    warning_text = _norm(" ".join(map(_text_blob, warnings + limitations)))
    return "generica" in warning_text or "los demas" in warning_text or "insuficiente" in warning_text


def _has_missing_data_warning(parsed: Mapping[str, Any]) -> bool:
    summary = parsed.get("resumen_observable") if isinstance(parsed.get("resumen_observable"), dict) else {}
    missing = _as_list(summary.get("datos_faltantes_relevantes"))
    candidate_warnings = []
    for item in _as_list(parsed.get("candidatos_explicados")):
        if isinstance(item, dict):
            candidate_warnings.extend(_as_list(item.get("advertencias")))
            candidate_warnings.extend(_as_list(item.get("diferencias_o_dudas")))
    text = _norm(" ".join(map(_text_blob, missing + candidate_warnings)))
    return bool(missing) or "falt" in text or "no se especifica" in text or "insuficiente" in text


def _no_official_claim(parsed: Mapping[str, Any]) -> bool:
    text = _norm(parsed)
    return not any(_norm(pattern) in text for pattern in OFFICIAL_CLASSIFICATION_PATTERNS)


def _evaluate_case(
    sample: Mapping[str, str],
    payload: Mapping[str, Any],
    response_row: Mapping[str, Any] | None,
) -> dict[str, Any]:
    case_id = _clean(sample.get("case_id"))
    pool_codes = _candidate_codes(payload)
    pool_ranks = _candidate_ranks(payload)
    candidate_ids = _candidate_ids_by_rank(payload)
    evidence_ids = _evidence_ids_by_rank(payload)
    payload_candidates = {int(row.get("rank_original") or 0): row for row in payload.get("top3_original", [])}
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
        "top3_complete": 0,
        "ranking_preserved": 0,
        "no_codes_outside_pool": 0,
        "no_invented_codes": 0,
        "historical_evidence_cited_all_candidates": 0,
        "normative_evidence_cited_all_candidates": 0,
        "candidate_id_preserved_all_candidates": 0,
        "evidence_id_preserved_all_candidates": 0,
        "observable_matches_present": 0,
        "observable_differences_present": 0,
        "comparison_top3_present": 0,
        "alternatives_lower_support_explained": 0,
        "conclusion_auditable_present": 0,
        "final_warning_present": 0,
        "generic_normative_warning_when_needed": 0,
        "missing_data_warning_present": 0,
        "no_official_classification_claim": 0,
        "no_reranking_signal": 0,
        "support_alto": 0,
        "support_medio": 0,
        "support_bajo": 0,
        "candidates_with_warnings": 0,
        "auditability_score": 0.0,
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

    explained = [item for item in _as_list(parsed.get("candidatos_explicados")) if isinstance(item, dict)]
    returned_codes = [_clean(item.get("nandina")) for item in explained]
    returned_ranks = [int(item.get("rank_original") or 0) for item in explained]
    support_counts = Counter(_norm(item.get("soporte")) for item in explained)
    row["support_alto"] = support_counts["alto"]
    row["support_medio"] = support_counts["medio"]
    row["support_bajo"] = support_counts["bajo"]
    row["candidates_with_warnings"] = sum(1 for item in explained if _as_list(item.get("advertencias")))

    complete = (
        len(explained) == 3
        and returned_ranks == EXPECTED_RANKS
        and all(code for code in returned_codes)
        and all(_norm(item.get("soporte")) in SUPPORT_VALUES for item in explained)
        and all(_clean(item.get("razon_de_soporte")) for item in explained)
    )
    row["top3_complete"] = int(complete)
    if not complete:
        failures.append("top3_incomplete_or_schema_invalid")

    row["ranking_preserved"] = int(returned_codes == pool_codes and returned_ranks == pool_ranks)
    row["no_reranking_signal"] = row["ranking_preserved"]
    if not row["ranking_preserved"]:
        failures.append("ranking_not_preserved")

    outside_count = sum(1 for code in returned_codes if code and code not in set(pool_codes))
    row["no_codes_outside_pool"] = int(outside_count == 0)
    row["no_invented_codes"] = int(outside_count == 0 and all(re.fullmatch(r"\d{8}", code or "") for code in returned_codes))
    if outside_count:
        failures.append("codes_outside_pool")
    if not row["no_invented_codes"]:
        failures.append("invented_or_invalid_codes")

    historical_flags = []
    normative_flags = []
    generic_warning_flags = []
    for item in explained:
        rank = int(item.get("rank_original") or 0)
        historical_flags.append(_has_historical_evidence(item, candidate_ids.get(rank, "")))
        normative_flags.append(_has_normative_evidence(item, evidence_ids.get(rank, set())))
        generic_warning_flags.append(_generic_normative_warning(item, payload_candidates.get(rank, {})))
    row["historical_evidence_cited_all_candidates"] = int(len(historical_flags) == 3 and all(historical_flags))
    row["normative_evidence_cited_all_candidates"] = int(len(normative_flags) == 3 and all(normative_flags))
    row["candidate_id_preserved_all_candidates"] = row["historical_evidence_cited_all_candidates"]
    row["evidence_id_preserved_all_candidates"] = row["normative_evidence_cited_all_candidates"]
    row["generic_normative_warning_when_needed"] = int(len(generic_warning_flags) == 3 and all(generic_warning_flags))
    if not row["historical_evidence_cited_all_candidates"]:
        failures.append("historical_evidence_not_cited_all_candidates")
    if not row["normative_evidence_cited_all_candidates"]:
        failures.append("normative_evidence_not_cited_all_candidates")
    if not row["generic_normative_warning_when_needed"]:
        failures.append("generic_normative_warning_missing")

    row["observable_matches_present"] = int(all(_as_list(item.get("coincidencias")) for item in explained))
    row["observable_differences_present"] = int(any(_as_list(item.get("diferencias_o_dudas")) for item in explained))
    if not row["observable_matches_present"]:
        failures.append("observable_matches_missing")
    if not row["observable_differences_present"]:
        failures.append("observable_differences_missing")

    comparison = parsed.get("comparacion_top3")
    if isinstance(comparison, dict):
        criteria = _as_list(comparison.get("criterios_comparados"))
        best = comparison.get("candidato_con_mayor_soporte") if isinstance(comparison.get("candidato_con_mayor_soporte"), dict) else {}
        lower = _as_list(comparison.get("por_que_los_otros_tienen_menor_soporte"))
        best_code = _clean(best.get("nandina"))
        best_rank = int(best.get("rank_original") or 0)
        row["comparison_top3_present"] = int(bool(criteria) and best_code in pool_codes and best_rank in EXPECTED_RANKS)
        row["alternatives_lower_support_explained"] = int(bool(lower))
    if not row["comparison_top3_present"]:
        failures.append("comparison_top3_missing_or_invalid")
    if not row["alternatives_lower_support_explained"]:
        failures.append("alternatives_lower_support_missing")

    row["conclusion_auditable_present"] = int(bool(_clean(parsed.get("conclusion_auditable"))))
    final_warning = _norm(parsed.get("advertencia_final"))
    row["final_warning_present"] = int(FINAL_WARNING_FRAGMENT in final_warning)
    row["missing_data_warning_present"] = int(_has_missing_data_warning(parsed))
    row["no_official_classification_claim"] = int(_no_official_claim(parsed))
    if not row["conclusion_auditable_present"]:
        failures.append("conclusion_auditable_missing")
    if not row["final_warning_present"]:
        failures.append("final_warning_missing")
    if not row["missing_data_warning_present"]:
        failures.append("missing_data_warning_absent")
    if not row["no_official_classification_claim"]:
        failures.append("official_classification_claim")

    scored_fields = [
        "json_valid",
        "top3_complete",
        "ranking_preserved",
        "no_codes_outside_pool",
        "no_invented_codes",
        "historical_evidence_cited_all_candidates",
        "normative_evidence_cited_all_candidates",
        "observable_matches_present",
        "observable_differences_present",
        "comparison_top3_present",
        "alternatives_lower_support_explained",
        "conclusion_auditable_present",
        "final_warning_present",
        "generic_normative_warning_when_needed",
        "no_official_classification_claim",
    ]
    row["auditability_score"] = sum(float(row[field]) for field in scored_fields) / len(scored_fields)
    row["failure_types"] = "|".join(dict.fromkeys(failures))
    return row


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _rate(rows: Sequence[Mapping[str, Any]], field: str) -> float:
    return _mean([float(row[field]) for row in rows])


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    lines = [
        "# Evaluacion LLM explicacion Top-3 auditable v0.1",
        "",
        "## Resultado",
        "",
        f"- Modelo: `{payload['model']}`.",
        f"- Casos esperados: {payload['expected_cases']}.",
        f"- Casos procesados: {metrics['casos_procesados']}.",
        f"- JSON valido: {metrics['json_valido_rate']:.4f}.",
        f"- Top-3 completo: {metrics['top3_completo_rate']:.4f}.",
        f"- Ranking preservado: {metrics['ranking_preservado_rate']:.4f}.",
        f"- Sin codigos fuera del pool: {metrics['sin_codigos_fuera_pool_rate']:.4f}.",
        f"- Evidencia historica citada por candidato: {metrics['evidencia_historica_citada_por_candidato_rate']:.4f}.",
        f"- Evidencia normativa citada por candidato: {metrics['evidencia_normativa_citada_por_candidato_rate']:.4f}.",
        f"- Comparacion Top-3 presente: {metrics['comparacion_top3_presente_rate']:.4f}.",
        f"- Advertencia final presente: {metrics['advertencia_final_presente_rate']:.4f}.",
        f"- Score promedio de auditabilidad: {metrics['score_promedio_auditabilidad_por_caso']:.4f}.",
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
    case_rows = [
        _evaluate_case(row, payload_by_case[_clean(row.get("case_id"))], response_by_case.get(_clean(row.get("case_id"))))
        for row in sample_rows
    ]

    total_candidates = len(case_rows) * 3
    metrics = {
        "casos_procesados": len(case_rows),
        "json_valido": sum(row["json_valid"] for row in case_rows),
        "json_valido_rate": _rate(case_rows, "json_valid"),
        "top3_completo": sum(row["top3_complete"] for row in case_rows),
        "top3_completo_rate": _rate(case_rows, "top3_complete"),
        "ranking_preservado": sum(row["ranking_preserved"] for row in case_rows),
        "ranking_preservado_rate": _rate(case_rows, "ranking_preserved"),
        "sin_codigos_fuera_pool": sum(row["no_codes_outside_pool"] for row in case_rows),
        "sin_codigos_fuera_pool_rate": _rate(case_rows, "no_codes_outside_pool"),
        "sin_codigos_inventados": sum(row["no_invented_codes"] for row in case_rows),
        "sin_codigos_inventados_rate": _rate(case_rows, "no_invented_codes"),
        "evidencia_historica_citada_por_candidato": sum(row["historical_evidence_cited_all_candidates"] for row in case_rows),
        "evidencia_historica_citada_por_candidato_rate": _rate(case_rows, "historical_evidence_cited_all_candidates"),
        "evidencia_normativa_citada_por_candidato": sum(row["normative_evidence_cited_all_candidates"] for row in case_rows),
        "evidencia_normativa_citada_por_candidato_rate": _rate(case_rows, "normative_evidence_cited_all_candidates"),
        "candidate_id_preservado_rate": _rate(case_rows, "candidate_id_preserved_all_candidates"),
        "evidence_id_preservado_rate": _rate(case_rows, "evidence_id_preserved_all_candidates"),
        "coincidencias_observables_rate": _rate(case_rows, "observable_matches_present"),
        "diferencias_observables_rate": _rate(case_rows, "observable_differences_present"),
        "comparacion_top3_presente": sum(row["comparison_top3_present"] for row in case_rows),
        "comparacion_top3_presente_rate": _rate(case_rows, "comparison_top3_present"),
        "conclusion_auditable_presente_rate": _rate(case_rows, "conclusion_auditable_present"),
        "advertencia_final_presente_rate": _rate(case_rows, "final_warning_present"),
        "advertencia_normativa_generica_rate": _rate(case_rows, "generic_normative_warning_when_needed"),
        "advertencia_datos_faltantes_rate": _rate(case_rows, "missing_data_warning_present"),
        "sin_clasificacion_oficial_rate": _rate(case_rows, "no_official_classification_claim"),
        "sin_senales_reranking_rate": _rate(case_rows, "no_reranking_signal"),
        "soporte_alto_candidatos": sum(row["support_alto"] for row in case_rows),
        "soporte_medio_candidatos": sum(row["support_medio"] for row in case_rows),
        "soporte_bajo_candidatos": sum(row["support_bajo"] for row in case_rows),
        "soporte_alto_rate": sum(row["support_alto"] for row in case_rows) / total_candidates,
        "soporte_medio_rate": sum(row["support_medio"] for row in case_rows) / total_candidates,
        "soporte_bajo_rate": sum(row["support_bajo"] for row in case_rows) / total_candidates,
        "candidatos_con_advertencias_rate": sum(row["candidates_with_warnings"] for row in case_rows) / total_candidates,
        "score_promedio_auditabilidad_por_caso": _mean([float(row["auditability_score"]) for row in case_rows]),
        "score_mediano_auditabilidad_por_caso": _median([float(row["auditability_score"]) for row in case_rows]),
        "median_historical_expected_rank": _median([row["expected_rank_historical"] for row in case_rows if row["expected_rank_historical"]]),
    }
    failure_counter: Counter[str] = Counter()
    for row in case_rows:
        for failure in _clean(row.get("failure_types")).split("|"):
            if failure:
                failure_counter[failure] += 1

    passes = (
        metrics["json_valido_rate"] >= 0.95
        and metrics["ranking_preservado_rate"] == 1.0
        and metrics["sin_codigos_fuera_pool_rate"] == 1.0
        and metrics["evidencia_historica_citada_por_candidato_rate"] >= 0.95
        and metrics["evidencia_normativa_citada_por_candidato_rate"] >= 0.95
        and metrics["comparacion_top3_presente_rate"] >= 0.95
        and metrics["advertencia_final_presente_rate"] >= 0.95
        and metrics["sin_senales_reranking_rate"] == 1.0
        and metrics["sin_clasificacion_oficial_rate"] == 1.0
    )
    decision = (
        "Pasa metodologicamente a Fase 10C: cumple los umbrales formales de auditabilidad, preserva Top-3 y no muestra senales de re-ranking ni clasificacion oficial."
        if passes
        else "No pasa aun a Fase 10C: requiere ajustar prompt, payload, runner o controles antes de escalar."
    )

    model = _clean(responses[0].get("model")) if responses else args.model
    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "10B_llm_explanation_top3_audit_sample",
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
        "pass_criteria": {
            "json_valido_rate_min": 0.95,
            "ranking_preservado_rate": 1.0,
            "sin_codigos_fuera_pool_rate": 1.0,
            "evidencia_historica_citada_por_candidato_rate_min": 0.95,
            "evidencia_normativa_citada_por_candidato_rate_min": 0.95,
            "comparacion_top3_presente_rate_min": 0.95,
            "advertencia_final_presente_rate_min": 0.95,
            "sin_senales_reranking_rate": 1.0,
            "sin_clasificacion_oficial_rate": 1.0,
        },
        "policy": {
            "llm_role": "explanation_only",
            "retrieval_used_by_llm": False,
            "reranking_allowed": False,
            "openai_used": False,
            "remote_api_used": False,
            "ollama_local_only": True,
        },
        "outputs": {
            "audit_quality_metrics_json": _rel(output_dir / "audit_quality_metrics.json"),
            "audit_quality_summary_md": _rel(output_dir / "audit_quality_summary.md"),
            "case_audit_quality_summary_csv": _rel(output_dir / "case_audit_quality_summary.csv"),
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
        "top3_complete",
        "ranking_preserved",
        "no_codes_outside_pool",
        "no_invented_codes",
        "historical_evidence_cited_all_candidates",
        "normative_evidence_cited_all_candidates",
        "candidate_id_preserved_all_candidates",
        "evidence_id_preserved_all_candidates",
        "observable_matches_present",
        "observable_differences_present",
        "comparison_top3_present",
        "alternatives_lower_support_explained",
        "conclusion_auditable_present",
        "final_warning_present",
        "generic_normative_warning_when_needed",
        "missing_data_warning_present",
        "no_official_classification_claim",
        "no_reranking_signal",
        "support_alto",
        "support_medio",
        "support_bajo",
        "candidates_with_warnings",
        "auditability_score",
        "failure_types",
        "parse_error",
    ]
    _write_csv(output_dir / "case_audit_quality_summary.csv", case_rows, fieldnames)
    _write_json(output_dir / "audit_quality_metrics.json", payload)
    ensure_parent(output_dir / "audit_quality_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate formal auditability of Top-3 LLM explanations.")
    parser.add_argument("--sample-cases", default=str(DEFAULT_SAMPLE_CASES))
    parser.add_argument("--payloads", default=str(DEFAULT_PAYLOADS))
    parser.add_argument("--explanations", default=str(DEFAULT_EXPLANATIONS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default="qwen2.5:7b-instruct")
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: evaluacion formal LLM explicacion Top-3 auditable completada")
    print(
        f"casos={metrics['casos_procesados']} json={metrics['json_valido_rate']:.4f} "
        f"top3={metrics['ranking_preservado_rate']:.4f} "
        f"hist_ev={metrics['evidencia_historica_citada_por_candidato_rate']:.4f} "
        f"norm_ev={metrics['evidencia_normativa_citada_por_candidato_rate']:.4f}"
    )
    print(payload["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
