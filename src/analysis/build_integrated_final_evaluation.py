"""Build the integrated final evaluation for the offline NANDINA pilot.

This script consolidates metrics and methodological evidence already produced
by previous phases of the project. It does not retrain models, does not execute
LLM/Ollama, does not call remote APIs, and does not modify source data, splits,
the original Excel file, or previous phase outputs.

Outputs are written to:
    outputs/evaluation/integrated_final_evaluation_v0.1/

The final methodological document is also regenerated at:
    docs/evaluacion_final_integrada_v0.1.md
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "evaluation" / "integrated_final_evaluation_v0.1"
FINAL_DOC_PATH = PROJECT_ROOT / "docs" / "evaluacion_final_integrada_v0.1.md"

NOT_EVALUATED = "no evaluado"
NOT_COMPARABLE = "no comparable"

METRIC_COLUMNS = [
    "method_id",
    "method_name",
    "method_type",
    "phase",
    "n_evaluated",
    "data_source",
    "metric_source",
    "top_1",
    "top_3",
    "top_5",
    "top_10",
    "top_20",
    "top_50",
    "recall_at_100",
    "recall_at_200",
    "mrr",
    "partida_at_100",
    "sub_partida_at_100",
    "clase_at_100",
    "json_valid",
    "ranking_preserved",
    "historical_evidence_cited",
    "normative_evidence_cited",
    "auditability_score",
    "methodological_decision",
    "limitations",
]


@dataclass(frozen=True)
class MethodSpec:
    method_id: str
    method_name: str
    method_type: str
    phase: str
    data_source: str
    metric_path: str | None
    report_path: str
    decision: str
    limitations: str


METHOD_SPECS = [
    MethodSpec(
        "bm25_flat_class87",
        "BM25 normativo plano clase 87",
        "normativo",
        "Fase 4 actualizada",
        "data_aduanas evalset clase 87",
        "outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/metrics.json",
        "docs/evaluacion_bm25_data_aduanas_clase87_v0.1.md",
        "Baseline auditable de referencia; no se adopta como recuperador principal.",
        "Baja exactitud NANDINA8; comparacion no pareada contra fases historicas.",
    ),
    MethodSpec(
        "dense_text2trade_class87",
        "Dense Text2Trade clase 87",
        "denso",
        "Fase 5 actualizada",
        "data_aduanas evalset clase 87",
        "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/metrics.json",
        "docs/evaluacion_text2trade_dense_data_aduanas_clase87_v0.1.md",
        "No se incorpora al pipeline de recuperacion exacta.",
        "No mejora BM25 en exactitud; solo mejora Partida@100 y degrada Sub Partida/Clase.",
    ),
    MethodSpec(
        "bm25_hierarchical_class87",
        "BM25 jerarquico v0.1 clase 87",
        "normativo",
        "Fase 6B/6C actualizada",
        "data_aduanas evalset clase 87",
        "outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1/metrics.json",
        "docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md",
        "Se conserva como recuperador normativo auxiliar de trazabilidad.",
        "Mejora cobertura amplia frente al plano, pero mantiene baja precision temprana.",
    ),
    MethodSpec(
        "bm25_dual_protected_class87",
        "BM25 dual protegido clase 87",
        "normativo",
        "Fase 6B/6C actualizada",
        "data_aduanas evalset clase 87",
        "outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1/metrics.json",
        "docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md",
        "Se conserva solo como fuente auxiliar de cobertura profunda.",
        "No supera al jerarquico como ranking principal; baja exactitud temprana.",
    ),
    MethodSpec(
        "candidate_pool_normative_class87",
        "Candidate pool normativo clase 87",
        "normativo",
        "Fase 7A actualizada",
        "data_aduanas evalset clase 87",
        "outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_metrics.json",
        "docs/evaluacion_candidate_pool_data_aduanas_clase87_v0.1.md",
        "Queda como respaldo documental y trazabilidad, no como fuente principal.",
        "Union oracle no es pool ordenado; el pool operativo sigue lejos del historico.",
    ),
    MethodSpec(
        "historical_retrieval_class87",
        "Recuperacion historica real clase 87",
        "historico",
        "Fase 9A actualizada",
        "historico data_aduanas clase 87 separado del evalset",
        "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_metrics.json",
        "docs/evaluacion_recuperacion_historica_data_aduanas_clase87_v0.1.md",
        "Debe dominar como recuperador cuando existe soporte historico.",
        "Todos los codigos del evalset tienen soporte historico; falta validar codigos ausentes/temporalidad.",
    ),
    MethodSpec(
        "hybrid_pool_class87",
        "Pool hibrido historico + normativo clase 87",
        "hibrido",
        "Fase 9B actualizada",
        "historico real + candidate pool normativo clase 87",
        "outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/hybrid_metrics.json",
        "docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md",
        "Estrategia recomendada: historico primero con backfill normativo si falta codigo.",
        "El backfill no mejora Top-100 en este evalset porque todo tiene soporte historico.",
    ),
    MethodSpec(
        "llm_rerank_hybrid_sample",
        "LLM re-ranker sobre pool hibrido",
        "LLM re-ranking",
        "Fase 9C-A",
        "muestra deterministica de 20 casos",
        "outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/llm_rerank_metrics.json",
        "docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md",
        "Resultado negativo; no escalar a Fase 9C-B.",
        "Muestra diagnostica pequena; se compara solo contra candidatos enviados.",
    ),
    MethodSpec(
        "llm_explanation_top3_audit",
        "LLM explicacion Top-3 auditable",
        "LLM explicacion",
        "Fase 10B",
        "muestra deterministica de 50 casos",
        "outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_quality_metrics.json",
        "docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md",
        "Pasa como explicador auditable del Top-3 fijo, no como recuperador ni re-ranker.",
        "No mide exactitud de recuperacion; depende de candidatos ya recuperados.",
    ),
    MethodSpec(
        "qualitative_review_10c",
        "Revision cualitativa 10C",
        "LLM explicacion",
        "Fase 10C",
        "10 fichas auditables de Fase 10B",
        "docs/revision_cualitativa_fichas_auditables_v0.1.csv",
        "docs/revision_cualitativa_fichas_auditables_v0.1.md",
        "Confirma trazabilidad formal y utilidad humana con cautelas de tono/evidencia.",
        "Revision cualitativa de 10 fichas; no produce metricas de recuperacion.",
    ),
    MethodSpec(
        "audit_card_improvement_10d",
        "Mejora de ficha 10D",
        "LLM explicacion",
        "Fase 10D",
        "diseno de prompt/rubrica/ficha",
        "docs/mejora_ficha_auditable_llm_top3_v0.1.md",
        "docs/mejora_ficha_auditable_llm_top3_v0.1.md",
        "Mejora el diseno auditable sin regenerar fichas ni cambiar metricas.",
        "No ejecuta LLM ni genera metricas nuevas; queda pendiente validacion 10E.",
    ),
]


def read_json(relative_path: str) -> dict[str, Any] | None:
    path = PROJECT_ROOT / relative_path
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def read_csv_rows(relative_path: str) -> list[dict[str, str]]:
    path = PROJECT_ROOT / relative_path
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def file_exists(relative_path: str | None) -> bool:
    return bool(relative_path) and (PROJECT_ROOT / relative_path).exists()


def fmt(value: Any) -> Any:
    if value is None:
        return NOT_EVALUATED
    if isinstance(value, float):
        return round(value, 4)
    return value


def get_nested(data: dict[str, Any] | None, *keys: str) -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def base_row(spec: MethodSpec, metric_source: str) -> dict[str, Any]:
    return {
        "method_id": spec.method_id,
        "method_name": spec.method_name,
        "method_type": spec.method_type,
        "phase": spec.phase,
        "n_evaluated": NOT_EVALUATED,
        "data_source": spec.data_source,
        "metric_source": metric_source,
        "top_1": NOT_EVALUATED,
        "top_3": NOT_EVALUATED,
        "top_5": NOT_EVALUATED,
        "top_10": NOT_EVALUATED,
        "top_20": NOT_EVALUATED,
        "top_50": NOT_EVALUATED,
        "recall_at_100": NOT_EVALUATED,
        "recall_at_200": NOT_EVALUATED,
        "mrr": NOT_EVALUATED,
        "partida_at_100": NOT_EVALUATED,
        "sub_partida_at_100": NOT_EVALUATED,
        "clase_at_100": NOT_EVALUATED,
        "json_valid": NOT_EVALUATED,
        "ranking_preserved": NOT_EVALUATED,
        "historical_evidence_cited": NOT_EVALUATED,
        "normative_evidence_cited": NOT_EVALUATED,
        "auditability_score": NOT_EVALUATED,
        "methodological_decision": spec.decision,
        "limitations": spec.limitations,
    }


def fill_retrieval_metrics(row: dict[str, Any], metrics: dict[str, Any]) -> None:
    row.update(
        {
            "n_evaluated": fmt(first_present(metrics.get("cases_total"), metrics.get("cases"), metrics.get("cases_evaluated"))),
            "top_1": fmt(first_present(metrics.get("top_1"), metrics.get("top_1_accuracy"), metrics.get("exact_at_1"), metrics.get("final_pool_at_1"))),
            "top_3": fmt(first_present(metrics.get("top_3"), metrics.get("top_3_accuracy"), metrics.get("exact_at_3"), metrics.get("final_pool_at_3"))),
            "top_5": fmt(first_present(metrics.get("top_5"), metrics.get("top_5_accuracy"), metrics.get("exact_at_5"), metrics.get("final_pool_at_5"))),
            "top_10": fmt(first_present(metrics.get("top_10"), metrics.get("top_10_accuracy"), metrics.get("exact_at_10"), metrics.get("final_pool_at_10"))),
            "top_20": fmt(first_present(metrics.get("exact_at_20"), metrics.get("final_pool_at_20"))),
            "top_50": fmt(first_present(metrics.get("recall_at_50"), metrics.get("exact_at_50"), metrics.get("final_pool_at_50"))),
            "recall_at_100": fmt(first_present(metrics.get("recall_at_100"), metrics.get("exact_at_100"), metrics.get("final_pool_at_100"))),
            "recall_at_200": fmt(first_present(metrics.get("recall_at_200"), metrics.get("exact_at_200"), metrics.get("final_pool_at_200"))),
            "mrr": fmt(metrics.get("mrr")),
            "partida_at_100": fmt(first_present(metrics.get("partida_at_100"), metrics.get("final_pool_partida_at_100"))),
            "sub_partida_at_100": fmt(first_present(metrics.get("sub_partida_at_100"), metrics.get("final_pool_sub_partida_at_100"))),
            "clase_at_100": fmt(first_present(metrics.get("clase_at_100"), metrics.get("final_pool_clase_at_100"))),
        }
    )


def build_method_row(spec: MethodSpec) -> dict[str, Any]:
    metric_source = spec.metric_path if file_exists(spec.metric_path) else spec.report_path
    row = base_row(spec, metric_source)
    data = read_json(spec.metric_path) if spec.metric_path and spec.metric_path.endswith(".json") else None

    if spec.method_id in {"bm25_flat_class87", "dense_text2trade_class87"}:
        fill_retrieval_metrics(row, get_nested(data, "global_metrics") or {})
        hierarchical = get_nested(data, "hierarchical_metrics") or {}
        row["partida_at_100"] = fmt(hierarchical.get("partida_at_100"))
        row["sub_partida_at_100"] = fmt(hierarchical.get("sub_partida_at_100"))
        row["clase_at_100"] = fmt(hierarchical.get("clase_at_100"))
    elif spec.method_id == "bm25_hierarchical_class87":
        fill_retrieval_metrics(row, get_nested(data, "metrics_by_method", "BM25_hierarchical_v0.1") or {})
    elif spec.method_id == "bm25_dual_protected_class87":
        fill_retrieval_metrics(row, get_nested(data, "metrics_by_method", "BM25_dual_protected_top_5_backfill") or {})
    elif spec.method_id == "candidate_pool_normative_class87":
        fill_retrieval_metrics(row, get_nested(data, "metrics_by_strategy", "hierarchical_70_dual_backfill_30") or {})
        row["mrr"] = NOT_COMPARABLE
    elif spec.method_id == "historical_retrieval_class87":
        fill_retrieval_metrics(row, get_nested(data, "metrics") or {})
    elif spec.method_id == "hybrid_pool_class87":
        fill_retrieval_metrics(row, get_nested(data, "selected_strategy") or {})
    elif spec.method_id == "llm_rerank_hybrid_sample":
        metrics = get_nested(data, "metrics") or {}
        row.update(
            {
                "n_evaluated": fmt(metrics.get("cases_evaluated")),
                "top_1": fmt(metrics.get("llm_top_1")),
                "top_3": fmt(metrics.get("llm_top_3")),
                "top_5": fmt(metrics.get("llm_top_5")),
                "top_10": fmt(metrics.get("llm_top_10")),
                "mrr": fmt(metrics.get("llm_mrr")),
                "json_valid": fmt(metrics.get("json_valid_rate")),
                "ranking_preserved": "no; MRR y Top-1 degradan frente al ranking original",
                "limitations": f"{spec.limitations} Original MRR={fmt(metrics.get('original_mrr'))}, LLM MRR={fmt(metrics.get('llm_mrr'))}.",
            }
        )
    elif spec.method_id == "llm_explanation_top3_audit":
        metrics = get_nested(data, "metrics") or {}
        row.update(
            {
                "n_evaluated": fmt(metrics.get("casos_procesados")),
                "json_valid": fmt(metrics.get("json_valido_rate")),
                "ranking_preserved": fmt(metrics.get("ranking_preservado_rate")),
                "historical_evidence_cited": fmt(metrics.get("evidencia_historica_citada_por_candidato_rate")),
                "normative_evidence_cited": fmt(metrics.get("evidencia_normativa_citada_por_candidato_rate")),
                "auditability_score": fmt(metrics.get("score_promedio_auditabilidad_por_caso")),
            }
        )
    elif spec.method_id == "qualitative_review_10c":
        rows = read_csv_rows(spec.metric_path or "")
        scores = [float(r["audit_score"]) for r in rows if r.get("audit_score")]
        row.update(
            {
                "n_evaluated": len(rows),
                "auditability_score": fmt(sum(scores) / len(scores) if scores else None),
                "json_valid": NOT_COMPARABLE,
                "ranking_preserved": NOT_COMPARABLE,
                "historical_evidence_cited": "confirmado cualitativamente",
                "normative_evidence_cited": "confirmado con cautelas",
            }
        )
    elif spec.method_id == "audit_card_improvement_10d":
        row.update(
            {
                "n_evaluated": NOT_COMPARABLE,
                "json_valid": NOT_COMPARABLE,
                "ranking_preserved": NOT_COMPARABLE,
                "historical_evidence_cited": "diseno reforzado",
                "normative_evidence_cited": "diseno reforzado con alerta de norma generica",
                "auditability_score": NOT_EVALUATED,
            }
        )
    return row


def build_hypothesis_matrix(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    by_id = {row["method_id"]: row for row in rows}
    historical = by_id["historical_retrieval_class87"]
    hybrid = by_id["hybrid_pool_class87"]
    normative = by_id["candidate_pool_normative_class87"]
    rerank = by_id["llm_rerank_hybrid_sample"]
    explanation = by_id["llm_explanation_top3_audit"]

    return [
        {
            "hypothesis": "Mejora de recuperacion",
            "status": "respaldada",
            "quantitative_evidence": (
                f"Historico Recall@100={historical['recall_at_100']} y Top-1={historical['top_1']}; "
                f"hibrido Recall@100={hybrid['recall_at_100']} frente a pool normativo Recall@100={normative['recall_at_100']}."
            ),
            "qualitative_evidence": "Los documentos 9A/9B concluyen que el historico debe dominar el ranking operativo.",
            "evidence_phase": "Fases 7A, 9A y 9B",
            "limitations": "La mejora depende de soporte historico disponible; falta validacion temporal/codigos ausentes.",
        },
        {
            "hypothesis": "Utilidad del banco historico",
            "status": "respaldada",
            "quantitative_evidence": f"Historico real: Top-10={historical['top_10']}, Recall@100={historical['recall_at_100']}, MRR={historical['mrr']}.",
            "qualitative_evidence": "La evidencia historica es la fuente principal de ranking y tambien alimenta fichas auditables.",
            "evidence_phase": "Fase 9A y Fase 10B",
            "limitations": "No prueba aun desempeno para NANDINAS sin precedentes historicos.",
        },
        {
            "hypothesis": "Utilidad del corpus normativo jerarquico",
            "status": "parcialmente respaldada",
            "quantitative_evidence": f"Pool normativo: Recall@100={normative['recall_at_100']} y Clase@100={normative['clase_at_100']}; bajo Top-10={normative['top_10']}.",
            "qualitative_evidence": "Aporta trazabilidad, respaldo documental y evidencia normativa para explicaciones.",
            "evidence_phase": "Fases 6B/6C, 7A, 9B y 10B",
            "limitations": "No alcanza exactitud/ranking suficiente como recuperador principal.",
        },
        {
            "hypothesis": "LLM como re-ranker",
            "status": "no respaldada",
            "quantitative_evidence": f"LLM re-ranker: Top-1={rerank['top_1']} y MRR={rerank['mrr']}; degrada frente al ranking original.",
            "qualitative_evidence": "Decision explicita: no escalar a 9C-B.",
            "evidence_phase": "Fase 9C-A",
            "limitations": "Muestra diagnostica de 20 casos; suficiente como resultado negativo local, no como estudio exhaustivo.",
        },
        {
            "hypothesis": "LLM como generador de explicacion auditable",
            "status": "respaldada",
            "quantitative_evidence": f"JSON valido={explanation['json_valid']}, ranking preservado={explanation['ranking_preserved']}, score auditabilidad={explanation['auditability_score']}.",
            "qualitative_evidence": "10C confirma utilidad humana y 10D corrige debilidades de prudencia/formato.",
            "evidence_phase": "Fases 10B, 10C y 10D",
            "limitations": "La explicacion depende del Top-3 recuperado y requiere revision experta.",
        },
        {
            "hypothesis": "Trazabilidad/auditabilidad del enfoque RAG",
            "status": "respaldada",
            "quantitative_evidence": (
                f"Evidencia historica citada={explanation['historical_evidence_cited']}; "
                f"evidencia normativa citada={explanation['normative_evidence_cited']}."
            ),
            "qualitative_evidence": "Fichas 10B, revision 10C y mejora 10D separan fuentes historicas/normativas y advierten limites.",
            "evidence_phase": "Fases 9B, 10B, 10C y 10D",
            "limitations": "No equivale a clasificacion oficial ni sustituye revision experta.",
        },
    ]


def build_timeline() -> list[dict[str, str]]:
    return [
        {
            "order": "1",
            "phase": "Fase 4",
            "tested": "BM25 normativo plano clase 87",
            "result": "Top-10 bajo y Recall@100=0.0626.",
            "methodological_decision": "Usarlo como baseline auditable, no como recuperador principal.",
            "supporting_document": "docs/evaluacion_bm25_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "2",
            "phase": "Fase 5",
            "tested": "Dense Text2Trade clase 87",
            "result": "Exactitud NANDINA8 practicamente nula; Recall@100=0.0010.",
            "methodological_decision": "Descartar como componente exacto en esta fase.",
            "supporting_document": "docs/evaluacion_text2trade_dense_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "3",
            "phase": "Fase 6B/6C",
            "tested": "BM25 jerarquico y dual protegido",
            "result": "Mejoran cobertura normativa amplia, pero no ranking temprano suficiente.",
            "methodological_decision": "Conservar como trazabilidad/backfill normativo.",
            "supporting_document": "docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "4",
            "phase": "Fase 7A",
            "tested": "Candidate pool normativo",
            "result": "Mejor pool normativo alcanza Recall@100=0.3489 y Recall@200=0.6292.",
            "methodological_decision": "Mantener como respaldo documental frente al futuro bloque historico.",
            "supporting_document": "docs/evaluacion_candidate_pool_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "5",
            "phase": "Fase 9A",
            "tested": "Recuperacion historica real",
            "result": "Top-1=0.8628, Top-10=0.9801, Recall@100=1.0000.",
            "methodological_decision": "Promover historico como fuente dominante.",
            "supporting_document": "docs/evaluacion_recuperacion_historica_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "6",
            "phase": "Fase 9B",
            "tested": "Pool hibrido historico + normativo",
            "result": "Conserva metricas historicas y agrega backfill normativo sin degradar.",
            "methodological_decision": "Recomendar historico primero con backfill normativo si falta codigo.",
            "supporting_document": "docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md",
        },
        {
            "order": "7",
            "phase": "Fase 9C-A",
            "tested": "LLM como re-ranker",
            "result": "Top-1 y MRR degradan; ganados=0, perdidos=4.",
            "methodological_decision": "No escalar re-ranking; usar LLM despues solo para explicacion.",
            "supporting_document": "docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md",
        },
        {
            "order": "8",
            "phase": "Fase 10B",
            "tested": "LLM como explicador Top-3 auditable",
            "result": "JSON valido, ranking preservado y citas de evidencia en 50/50.",
            "methodological_decision": "Aceptar rol de explicador auditable controlado.",
            "supporting_document": "docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md",
        },
        {
            "order": "9",
            "phase": "Fases 10C/10D",
            "tested": "Revision cualitativa y mejora de ficha",
            "result": "Utilidad confirmada con cautelas sobre norma generica, predominio historico y tono.",
            "methodological_decision": "Reforzar prompt, rubrica, formato y necesidad de revision experta.",
            "supporting_document": "docs/revision_cualitativa_fichas_auditables_v0.1.md; docs/mejora_ficha_auditable_llm_top3_v0.1.md",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return "\n".join(lines)


def build_integrated_summary(rows: list[dict[str, Any]], hypotheses: list[dict[str, str]], timeline: list[dict[str, str]]) -> str:
    compact_columns = [
        "method_name",
        "method_type",
        "n_evaluated",
        "top_1",
        "top_10",
        "recall_at_100",
        "recall_at_200",
        "mrr",
        "auditability_score",
        "methodological_decision",
    ]
    hypothesis_columns = ["hypothesis", "status", "quantitative_evidence", "evidence_phase"]
    timeline_columns = ["order", "phase", "tested", "result", "methodological_decision"]
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")

    return f"""# Evaluacion final integrada v0.1

Generado por `src/analysis/build_integrated_final_evaluation.py` en `{generated}`.

## Resumen ejecutivo

La evidencia integrada respalda una arquitectura offline donde el recuperador historico real domina el ranking operativo para `data_aduanas` clase 87, mientras el corpus normativo jerarquico queda como respaldo documental, trazabilidad y backfill. El LLM no queda respaldado como re-ranker porque degrada Top-1/MRR en la prueba diagnostica. Si se usa LLM, el rol defendible es explicar de forma auditable un Top-3 fijo ya recuperado, con revision experta.

## Tabla comparativa integrada

{markdown_table(rows, compact_columns)}

## Validacion de hipotesis

{markdown_table(hypotheses, hypothesis_columns)}

## Decisiones experimentales

{markdown_table(timeline, timeline_columns)}

## Controles de alcance

- No se reentrenan modelos.
- No se ejecuta LLM, Ollama, OpenAI ni APIs remotas.
- No se modifican datos fuente, splits, Excel original ni outputs historicos.
- Las metricas ausentes o no comparables se marcan como `{NOT_EVALUATED}` o `{NOT_COMPARABLE}`.
"""


def build_final_document(rows: list[dict[str, Any]], hypotheses: list[dict[str, str]], timeline: list[dict[str, str]]) -> str:
    summary = build_integrated_summary(rows, hypotheses, timeline)
    limitations = [
        "La evaluacion principal clase 87 no es comparable de forma pareada con el evalset historico de 600 casos.",
        "El desempeno historico presupone soporte en el banco de precedentes; faltan particiones temporales y codigos ausentes.",
        "La evidencia normativa aporta trazabilidad, pero no reemplaza revision juridica ni clasificacion oficial.",
        "La prueba de LLM re-ranker es diagnostica y pequena, aunque suficiente para no escalar dentro de este piloto.",
        "La explicacion LLM se evalua como auditabilidad del Top-3 fijo, no como exactitud de clasificacion.",
    ]
    pending = [
        "Lockfile o contenedor reproducible de dependencias.",
        "Registro externo versionado por checksum para artefactos pesados.",
        "Validacion temporal o externa para medir generalizacion del banco historico.",
        "Eventual corrida 10E con prompt v0.3 si se decide validar la ficha mejorada.",
        "Politica final de preservacion de outputs regenerables fuera de Git.",
    ]

    return (
        summary
        + "\n## Principales hallazgos\n\n"
        + "- El historico real clase 87 alcanza `Recall@100 = 1.0000`, `Top-1 = 0.8628` y `MRR = 0.9062`.\n"
        + "- El hibrido recomendado conserva las metricas historicas y agrega respaldo normativo sin desplazar el ranking temprano.\n"
        + "- El pool normativo mejora la trazabilidad, pero no compite con el historico como fuente principal.\n"
        + "- Dense Text2Trade no aporta exactitud exacta NANDINA8 en este alcance.\n"
        + "- El LLM como re-ranker queda descartado; como explicador Top-3 auditable queda respaldado.\n\n"
        + "## Limites del experimento\n\n"
        + "\n".join(f"- {item}" for item in limitations)
        + "\n\n## Pendiente para cierre de reproducibilidad\n\n"
        + "\n".join(f"- {item}" for item in pending)
        + "\n"
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rows = [build_method_row(spec) for spec in METHOD_SPECS]
    hypotheses = build_hypothesis_matrix(rows)
    timeline = build_timeline()

    payload = {
        "version": "v0.1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "script": "src.analysis.build_integrated_final_evaluation",
        "controls": {
            "llm_executed": False,
            "ollama_executed": False,
            "openai_used": False,
            "remote_api_used": False,
            "models_retrained": False,
            "source_data_modified": False,
            "previous_outputs_modified": False,
        },
        "metrics": rows,
        "hypothesis_validation": hypotheses,
        "experimental_decisions_timeline": timeline,
    }

    with (OUTPUT_DIR / "integrated_metrics.json").open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    write_csv(OUTPUT_DIR / "integrated_metrics.csv", rows, METRIC_COLUMNS)
    write_csv(
        OUTPUT_DIR / "hypothesis_validation_matrix.csv",
        hypotheses,
        ["hypothesis", "status", "quantitative_evidence", "qualitative_evidence", "evidence_phase", "limitations"],
    )
    write_csv(
        OUTPUT_DIR / "experimental_decisions_timeline.csv",
        timeline,
        ["order", "phase", "tested", "result", "methodological_decision", "supporting_document"],
    )

    summary = build_integrated_summary(rows, hypotheses, timeline)
    (OUTPUT_DIR / "integrated_summary.md").write_text(summary, encoding="utf-8")
    (OUTPUT_DIR / "hypothesis_validation_matrix.md").write_text(
        "# Matriz de validacion de hipotesis v0.1\n\n"
        + markdown_table(
            hypotheses,
            ["hypothesis", "status", "quantitative_evidence", "qualitative_evidence", "evidence_phase", "limitations"],
        )
        + "\n",
        encoding="utf-8",
    )
    FINAL_DOC_PATH.write_text(build_final_document(rows, hypotheses, timeline), encoding="utf-8")


if __name__ == "__main__":
    main()
