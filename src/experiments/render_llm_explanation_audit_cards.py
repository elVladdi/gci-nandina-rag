from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_SAMPLE_CASES = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/sample_cases.csv")
DEFAULT_PAYLOADS = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/payloads.jsonl")
DEFAULT_EXPLANATIONS = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/llm_explanations.jsonl")
DEFAULT_CASE_QUALITY = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/case_audit_quality_summary.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1")


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


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


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _md(value: object) -> str:
    text = _clean(value)
    return text.replace("|", "\\|").replace("\n", " ")


def _slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")
    return slug or "case"


def _parse_response(row: Mapping[str, Any]) -> dict[str, Any] | None:
    parsed = row.get("parsed_response")
    if isinstance(parsed, dict):
        return parsed
    raw = _clean(row.get("raw_response"))
    start = raw.find("{")
    end = raw.rfind("}")
    if start >= 0 and end >= start:
        try:
            parsed = json.loads(raw[start : end + 1])
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, dict) else None
    return None


def _candidate_by_rank(payload: Mapping[str, Any]) -> dict[int, Mapping[str, Any]]:
    return {int(row.get("rank_original") or 0): row for row in payload.get("top3_original", [])}


def _render_list(values: Sequence[Any]) -> str:
    items = [_clean(value if not isinstance(value, dict) else json.dumps(value, ensure_ascii=False)) for value in values]
    items = [item for item in items if item]
    return "; ".join(items) if items else "No registrado."


def _render_bool(value: Any) -> str:
    if isinstance(value, bool):
        return "si" if value else "no"
    text = _clean(value).lower()
    if text in {"true", "1", "si", "yes"}:
        return "si"
    if text in {"false", "0", "no"}:
        return "no"
    return "No registrado."


def _render_card(
    sample: Mapping[str, str],
    payload: Mapping[str, Any],
    response: Mapping[str, Any],
    quality: Mapping[str, str],
) -> str:
    parsed = _parse_response(response)
    case_id = _clean(sample.get("case_id"))
    candidates = _candidate_by_rank(payload)
    lines = [
        f"# Ficha auditable 10B - {case_id}",
        "",
        "## Identificacion",
        "",
        f"- `case_id`: `{case_id}`",
        f"- `id_unico`: `{_clean(sample.get('id_unico'))}`",
        f"- Categoria de muestra: `{_clean(sample.get('sample_target_category'))}`",
        f"- Fuente de seleccion: `{_clean(sample.get('selection_source_category'))}`",
        f"- Soporte historico de etiqueta esperada: `{_clean(sample.get('support_bucket'))}` ({_clean(sample.get('historical_support_count'))} casos)",
        f"- Rank historico de etiqueta esperada: `{_clean(sample.get('expected_rank_historical'))}`",
        "",
        "## Mercancia observada",
        "",
        _clean(payload.get("descripcion_mercancia")),
        "",
        "## Top-3 recibido por el LLM",
        "",
        "| Rank | NANDINA | Score historico | Evidencia historica | Evidencia normativa |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for rank in [1, 2, 3]:
        candidate = candidates.get(rank, {})
        hist = candidate.get("evidencia_historica") if isinstance(candidate.get("evidencia_historica"), dict) else {}
        norm_evidence = _as_list(candidate.get("evidencias_normativas"))
        norm_ids = ", ".join(_clean(item.get("evidence_id")) for item in norm_evidence if isinstance(item, dict))
        lines.append(
            "| "
            f"{rank} | `{_md(candidate.get('nandina'))}` | {_clean(candidate.get('score_historico'))} | "
            f"`{_md(hist.get('candidate_id_unico') if isinstance(hist, dict) else '')}` | `{_md(norm_ids)}` |"
        )

    lines.extend(["", "## Respuesta LLM", ""])
    if not parsed:
        lines.extend(
            [
                "La respuesta no pudo parsearse como JSON valido.",
                "",
                "```text",
                _clean(response.get("raw_response"))[:4000],
                "```",
            ]
        )
    else:
        summary = parsed.get("resumen_observable") if isinstance(parsed.get("resumen_observable"), dict) else {}
        lines.extend(
            [
                "### Resumen observable",
                "",
                f"- Producto: {_clean(summary.get('producto')) or 'No registrado.'}",
                f"- Marca/modelo: {_clean(summary.get('marca_modelo')) or 'No registrado.'}",
                f"- Uso/funcion: {_clean(summary.get('uso_funcion')) or 'No registrado.'}",
                f"- Material/composicion: {_clean(summary.get('material_o_composicion')) or 'No registrado.'}",
                f"- Atributos tecnicos: {_render_list(_as_list(summary.get('atributos_tecnicos')))}",
                f"- Datos faltantes relevantes: {_render_list(_as_list(summary.get('datos_faltantes_relevantes')))}",
                "",
                "### Alertas de revision",
                "",
                f"- Advertencias globales: {_render_list(_as_list(parsed.get('advertencias_globales')))}",
                f"- Requiere revision experta: {_render_bool(parsed.get('requiere_revision_experta'))}",
                f"- Motivo de revision experta: {_clean(parsed.get('motivo_revision_experta')) or 'No registrado.'}",
                "",
                "### Candidatos explicados",
                "",
            ]
        )
        for item in [entry for entry in _as_list(parsed.get("candidatos_explicados")) if isinstance(entry, dict)]:
            rank = int(item.get("rank_original") or 0)
            lines.extend(
                [
                    f"#### Rank {rank} - `{_clean(item.get('nandina'))}`",
                    "",
                    f"- Soporte: `{_clean(item.get('soporte'))}`",
                    f"- Coincidencias: {_render_list(_as_list(item.get('coincidencias')))}",
                    f"- Diferencias o dudas: {_render_list(_as_list(item.get('diferencias_o_dudas')))}",
                    f"- Razon de soporte: {_clean(item.get('razon_de_soporte')) or 'No registrada.'}",
                    f"- Advertencias: {_render_list(_as_list(item.get('advertencias')))}",
                    "",
                    "| Evidencia historica citada | Fragmento usado | Lectura historica |",
                    "| --- | --- | --- |",
                ]
            )
            for evidence in _as_list(item.get("evidencia_historica_usada")):
                if isinstance(evidence, dict):
                    lines.append(
                        f"| `{_md(evidence.get('candidate_id_unico'))}` | {_md(evidence.get('fragmento_usado'))} | "
                        f"{_md(evidence.get('lectura_historica'))} |"
                    )
            if not _as_list(item.get("evidencia_historica_usada")):
                lines.append("| No registrada | No registrado | No registrado |")
            lines.extend(
                [
                    "",
                    "| Evidencia normativa citada | Texto citado | Tipo | Limitaciones |",
                    "| --- | --- | --- | --- |",
                ]
            )
            for evidence in _as_list(item.get("evidencia_normativa_usada")):
                if isinstance(evidence, dict):
                    lines.append(
                        f"| `{_md(evidence.get('evidence_id'))}` | {_md(evidence.get('texto_citado'))} | "
                        f"{_md(evidence.get('tipo_evidencia_normativa')) or 'No registrado'} | "
                        f"{_render_list(_as_list(evidence.get('limitaciones')))} |"
                    )
            if not _as_list(item.get("evidencia_normativa_usada")):
                lines.append("| No registrada | No registrado | No registrado | No registrado |")
            lines.append("")

        comparison = parsed.get("comparacion_top3") if isinstance(parsed.get("comparacion_top3"), dict) else {}
        best = comparison.get("candidato_con_mayor_soporte") if isinstance(comparison.get("candidato_con_mayor_soporte"), dict) else {}
        lines.extend(
            [
                "### Comparacion Top-3",
                "",
                f"- Criterios comparados: {_render_list(_as_list(comparison.get('criterios_comparados')))}",
                f"- Comparacion historica: {_clean(comparison.get('comparacion_historica')) or 'No registrada.'}",
                f"- Comparacion normativa: {_clean(comparison.get('comparacion_normativa')) or 'No registrada.'}",
                f"- Mayor soporte declarado: rank `{_clean(best.get('rank_original'))}`, NANDINA `{_clean(best.get('nandina'))}`.",
                f"- Motivo: {_clean(best.get('motivo')) or 'No registrado.'}",
                f"- Menor soporte de alternativos: {_render_list(_as_list(comparison.get('por_que_los_otros_tienen_menor_soporte')))}",
                "",
                "### Conclusion",
                "",
                _clean(parsed.get("conclusion_auditable")) or "No registrada.",
                "",
                _clean(parsed.get("advertencia_final")) or "Advertencia final no registrada.",
            ]
        )

    lines.extend(
        [
            "",
            "## Calidad auditable",
            "",
            "| Control | Valor |",
            "| --- | ---: |",
            f"| JSON valido | {_clean(quality.get('json_valid'))} |",
            f"| Top-3 completo | {_clean(quality.get('top3_complete'))} |",
            f"| Ranking preservado | {_clean(quality.get('ranking_preserved'))} |",
            f"| Sin codigos fuera del pool | {_clean(quality.get('no_codes_outside_pool'))} |",
            f"| Evidencia historica por candidato | {_clean(quality.get('historical_evidence_cited_all_candidates'))} |",
            f"| Evidencia normativa por candidato | {_clean(quality.get('normative_evidence_cited_all_candidates'))} |",
            f"| Comparacion Top-3 | {_clean(quality.get('comparison_top3_present'))} |",
            f"| Advertencia final | {_clean(quality.get('final_warning_present'))} |",
            f"| Score auditabilidad | {_clean(quality.get('auditability_score'))} |",
            "",
            f"Fallos: `{_clean(quality.get('failure_types')) or 'sin_fallos'}`",
            "",
        ]
    )
    return "\n".join(lines)


def render(args: argparse.Namespace) -> dict[str, Any]:
    sample_rows = _read_csv(resolve_project_path(args.sample_cases))
    payloads = list(_read_jsonl(resolve_project_path(args.payloads)))
    responses = list(_read_jsonl(resolve_project_path(args.explanations)))
    quality_rows = _read_csv(resolve_project_path(args.case_quality))
    output_dir = resolve_project_path(args.output_dir)
    cards_dir = output_dir / "audit_cards"
    cards_dir.mkdir(parents=True, exist_ok=True)

    payload_by_case = {_clean(row.get("case_id")): row for row in payloads}
    response_by_case = {_clean(row.get("case_id")): row for row in responses}
    quality_by_case = {_clean(row.get("case_id")): row for row in quality_rows}

    index_lines = [
        "# Fichas auditables LLM Top-3 10B",
        "",
        "| Caso | Categoria | Rank esperado | Score auditabilidad | Ficha |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    card_count = 0
    for sample in sample_rows:
        case_id = _clean(sample.get("case_id"))
        path = cards_dir / f"{_slug(case_id)}.md"
        text = _render_card(sample, payload_by_case[case_id], response_by_case[case_id], quality_by_case[case_id])
        path.write_text(text, encoding="utf-8")
        card_count += 1
        index_lines.append(
            f"| `{case_id}` | `{_clean(sample.get('sample_target_category'))}` | "
            f"{_clean(sample.get('expected_rank_historical'))} | "
            f"{_clean(quality_by_case[case_id].get('auditability_score'))} | "
            f"[{path.name}]({_rel(path)}) |"
        )
    ensure_parent(output_dir / "audit_cards.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return {
        "cards": card_count,
        "outputs": {
            "audit_cards_md": _rel(output_dir / "audit_cards.md"),
            "audit_cards_dir": _rel(cards_dir),
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render human-readable audit cards for LLM Top-3 explanations.")
    parser.add_argument("--sample-cases", default=str(DEFAULT_SAMPLE_CASES))
    parser.add_argument("--payloads", default=str(DEFAULT_PAYLOADS))
    parser.add_argument("--explanations", default=str(DEFAULT_EXPLANATIONS))
    parser.add_argument("--case-quality", default=str(DEFAULT_CASE_QUALITY))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    return parser


def main() -> int:
    result = render(build_parser().parse_args())
    print("OK: fichas auditables renderizadas")
    print(f"Fichas: {result['cards']}")
    print(f"Indice: {result['outputs']['audit_cards_md']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
