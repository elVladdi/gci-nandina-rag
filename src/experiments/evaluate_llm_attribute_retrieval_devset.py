from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_EXTRACTIONS = Path("outputs/evaluation/llm_attribute_retrieval_devset_v0.1/attribute_extractions.jsonl")
DEFAULT_PROMPT = Path("src/llm/attribute_extraction_prompt_v0.1.md")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_attribute_retrieval_devset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_llm_attribute_retrieval_devset_v0.1.md")

EXPECTED_DEVSET_ROWS = 13
K_LIST = [1, 3, 5, 10]
QUERY_WEIGHTS = {"Q0": 3.0, "Q1": 1.5, "Q2": 1.0, "Q3": 0.75}
PROTECTED_TOP_N = 10
PHASE7A_HIERARCHICAL_BASE = 80
PHASE7A_STRATEGY = "hierarchical_80_dual_backfill_20"
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_PROTECTED_TOP_N = 5
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
QUERY_LABELS = ("Q0", "Q1", "Q2", "Q3")
METHODS = (
    "BM25_hierarchical_Q0",
    "BM25_hierarchical_attribute_weighted_rrf",
    "BM25_hierarchical_attribute_q0_protected",
    "phase7a_pool_hierarchical_80_dual_backfill_20",
)
GENERIC_TERMS = {
    "accesorios",
    "articulos",
    "componentes",
    "cosas",
    "demas",
    "las demas",
    "los demas",
    "mercancia",
    "otros",
    "partes",
    "producto",
    "productos",
}
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


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_number}") from exc
            if not isinstance(payload, dict):
                raise ValueError(f"Invalid JSON object in {path} at line {line_number}")
            rows.append(payload)
    return rows


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


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _case_outcome(q0_rank: int, method_rank: int, depth: int) -> str:
    q0_metric = _rank_metric(q0_rank, depth)
    method_metric = _rank_metric(method_rank, depth)
    if method_metric < q0_metric:
        return "ganado"
    if method_metric > q0_metric:
        return "perdido"
    return "sin_cambio"


def _code_from_hit(hit: Mapping[str, Any]) -> str:
    return _clean(hit.get("code"))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        ranked.append(item)
    return ranked


def _dedupe_append(
    target: list[dict[str, Any]],
    seen: set[str],
    hits: Sequence[Mapping[str, Any]],
    limit: int | None = None,
) -> None:
    iterable = hits if limit is None else hits[:limit]
    for hit in iterable:
        code = _code_from_hit(hit)
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _protected_top_5_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=DUAL_PROTECTED_TOP_N)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[DUAL_PROTECTED_TOP_N:])
    return _renumber(fused, depth)


def _phase7a_pool(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    pool: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(pool, seen, hierarchical_hits, limit=min(PHASE7A_HIERARCHICAL_BASE, depth))
    _dedupe_append(pool, seen, dual_hits, limit=depth)
    if len(pool) < depth:
        _dedupe_append(pool, seen, hierarchical_hits[PHASE7A_HIERARCHICAL_BASE:])
    return _renumber(pool, depth)


def _hit_by_code(hits: Sequence[Mapping[str, Any]]) -> dict[str, dict[str, Any]]:
    return {_code_from_hit(hit): dict(hit) for hit in hits if _code_from_hit(hit)}


def _weighted_rrf_fuse(
    source_hits: Mapping[str, Sequence[Mapping[str, Any]]],
    *,
    rrf_k: int,
    weights: Mapping[str, float],
    depth: int,
) -> list[dict[str, Any]]:
    fused: dict[str, dict[str, Any]] = {}
    for label, hits in source_hits.items():
        weight = float(weights.get(label, 1.0))
        best_seen_in_source: set[str] = set()
        for hit in hits:
            code = _code_from_hit(hit)
            if not code or code in best_seen_in_source:
                continue
            best_seen_in_source.add(code)
            rank = int(hit.get("rank", 0))
            if rank <= 0:
                continue
            entry = fused.setdefault(
                code,
                {
                    "code": code,
                    "rrf_score": 0.0,
                    "text": _clean(hit.get("text")),
                    "doc_idx": hit.get("doc_idx", ""),
                    "sources": [],
                    "source_ranks": {},
                },
            )
            entry["rrf_score"] += weight / float(rrf_k + rank)
            entry["sources"].append(f"{label}:{rank}:w{weight:g}")
            entry["source_ranks"][label] = rank
            if not entry.get("text"):
                entry["text"] = _clean(hit.get("text"))
    ordered = sorted(fused.values(), key=lambda item: (-float(item["rrf_score"]), _clean(item["code"])))
    for rank, item in enumerate(ordered, start=1):
        item["rank"] = rank
        item["score"] = float(item["rrf_score"])
        item["sources"] = sorted(item["sources"])
    return ordered[:depth]


def _q0_protected_fusion(
    q0_hits: Sequence[Mapping[str, Any]],
    fused_hits: Sequence[Mapping[str, Any]],
    *,
    protected_top_n: int,
    depth: int,
) -> list[dict[str, Any]]:
    by_code = _hit_by_code(fused_hits)
    protected_block: list[dict[str, Any]] = []
    seen: set[str] = set()
    for q0_hit in q0_hits[:protected_top_n]:
        code = _code_from_hit(q0_hit)
        if not code or code in seen:
            continue
        seen.add(code)
        item = dict(by_code.get(code, q0_hit))
        item["q0_protected"] = True
        protected_block.append(item)
    for hit in fused_hits:
        code = _code_from_hit(hit)
        if code and code not in seen:
            seen.add(code)
            protected_block.append(dict(hit))
    return _renumber(protected_block, depth)


def _strip_code_like(text: str) -> str:
    pieces: list[str] = []
    last = 0
    for match in CODE_PATTERN.finditer(text):
        following = text[match.end() : match.end() + 32]
        if QUANTITY_CONTEXT_PATTERN.match(following):
            continue
        pieces.append(text[last : match.start()])
        last = match.end()
    pieces.append(text[last:])
    return re.sub(r"\s+", " ", " ".join(pieces)).strip()


def _safe_text(value: object) -> str:
    text = _strip_code_like(_clean(value))
    if FORBIDDEN_NORMALIZED_PATTERN.search(_norm(text)):
        return ""
    return text


def _list_values(value: Any) -> list[str]:
    if isinstance(value, list):
        return [_safe_text(item) for item in value if _safe_text(item)]
    if _clean(value):
        return [_safe_text(value)]
    return []


def _query_text(parts: Sequence[Any]) -> str:
    values: list[str] = []
    seen_norm: set[str] = set()
    for part in parts:
        if isinstance(part, list):
            candidates = part
        else:
            candidates = [part]
        for candidate in candidates:
            text = _safe_text(candidate)
            normed = _norm(text)
            if text and normed and normed not in seen_norm:
                seen_norm.add(normed)
                values.append(text)
    return " ".join(values).strip()


def _too_generic(query: str) -> bool:
    normed = _norm(query)
    tokens = normed.split()
    if not normed:
        return True
    if normed in GENERIC_TERMS:
        return True
    return len([token for token in tokens if len(token) >= 4]) < 2


def _extraction_from_record(record: Mapping[str, Any]) -> dict[str, Any]:
    extraction = record.get("extraction")
    if not isinstance(extraction, Mapping):
        extraction = record.get("parsed_json")
    output: dict[str, Any] = {field: "" for field in STRING_FIELDS}
    output.update({field: [] for field in LIST_FIELDS})
    if isinstance(extraction, Mapping):
        for field in STRING_FIELDS:
            output[field] = _clean(extraction.get(field))
        for field in LIST_FIELDS:
            output[field] = _list_values(extraction.get(field))
    return output


def _build_queries(descripcion: str, extraction: Mapping[str, Any]) -> dict[str, str]:
    q1 = _query_text(
        [
            extraction.get("producto"),
            extraction.get("material"),
            extraction.get("composicion"),
            extraction.get("estado"),
        ]
    )
    q2 = _query_text(
        [
            extraction.get("producto"),
            extraction.get("uso_funcion"),
            extraction.get("presentacion"),
            extraction.get("tecnologia"),
            extraction.get("medidas"),
        ]
    )
    q3 = _query_text(
        [
            extraction.get("producto"),
            _list_values(extraction.get("atributos_discriminantes")),
            _list_values(extraction.get("terminos_busqueda")),
        ]
    )
    queries = {"Q0": descripcion, "Q1": q1, "Q2": q2, "Q3": q3}
    for label in ("Q1", "Q2", "Q3"):
        if _too_generic(queries[label]):
            queries[label] = ""
    return queries


def _rank_from_candidates(candidates: Sequence[Mapping[str, Any]], true_code: str) -> int:
    return rank_of_true(candidates, true_code)


def _family_hit(candidates: Sequence[Mapping[str, Any]], true_code: str, family_len: int, k: int) -> int:
    prefix = _clean(true_code)[:family_len]
    if not prefix:
        return 0
    return int(any(_code_from_hit(hit).startswith(prefix) for hit in candidates[:k]))


def _compact_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for hit in candidates[:limit]:
        compact.append(
            {
                "rank": int(hit.get("rank", len(compact) + 1)),
                "code": _code_from_hit(hit),
                "score": float(hit.get("rrf_score", hit.get("score", 0.0))),
                "sources": list(hit.get("sources", [])),
                "text": _clean(hit.get("text")),
            }
        )
    return compact


def _top_codes(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_code_from_hit(hit) for hit in candidates[:limit])


def _metrics_for_method(
    rows: Sequence[Mapping[str, Any]],
    method: str,
    *,
    k_list: Sequence[int],
    depth: int,
) -> dict[str, Any]:
    ranks = [int(row[f"rank_{method}"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "top_10_hs4": _mean([int(row[f"{method}_top10_hs4"]) for row in rows]),
        "top_10_hs2": _mean([int(row[f"{method}_top10_hs2"]) for row in rows]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
        "depth": depth,
    }
    for k in k_list:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _comparison_vs_q0(rows: Sequence[Mapping[str, Any]], method: str, depth: int) -> dict[str, int]:
    outcomes = [_case_outcome(int(row["rank_BM25_hierarchical_Q0"]), int(row[f"rank_{method}"]), depth) for row in rows]
    return {
        "ganados": sum(1 for outcome in outcomes if outcome == "ganado"),
        "perdidos": sum(1 for outcome in outcomes if outcome == "perdido"),
        "sin_cambio": sum(1 for outcome in outcomes if outcome == "sin_cambio"),
        "new_cases_q0_not_found_method_found": sum(
            1
            for row in rows
            if int(row["rank_BM25_hierarchical_Q0"]) <= 0 and int(row[f"rank_{method}"]) > 0
        ),
        "degraded_cases": sum(
            1
            for row in rows
            if _rank_metric(int(row[f"rank_{method}"]), depth) > _rank_metric(int(row["rank_BM25_hierarchical_Q0"]), depth)
        ),
    }


def _json_quality(extraction_rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    return {
        "cases_total": len(extraction_rows),
        "valid_json_cases": sum(int(row.get("json_valid", 0)) for row in extraction_rows),
        "invalid_json_cases": sum(1 for row in extraction_rows if not int(row.get("json_valid", 0))),
        "code_violation_cases": sum(int(row.get("code_violation", 0)) for row in extraction_rows),
        "forbidden_term_violation_cases": sum(int(row.get("forbidden_term_violation", 0)) for row in extraction_rows),
        "possible_invented_attribute_cases": sum(
            int(row.get("possible_invented_attribute_violation", 0)) for row in extraction_rows
        ),
    }


def _json_summary(extraction: Mapping[str, Any]) -> str:
    parts = []
    for field in ("producto", "material", "composicion", "uso_funcion", "estado"):
        value = _clean(extraction.get(field))
        if value:
            parts.append(f"{field}={value}")
    attrs = _list_values(extraction.get("atributos_discriminantes"))
    terms = _list_values(extraction.get("terminos_busqueda"))
    if attrs:
        parts.append("atributos=" + ", ".join(attrs[:3]))
    if terms:
        parts.append("terminos=" + ", ".join(terms[:3]))
    return "; ".join(parts)


def _short(text: str, limit: int = 90) -> str:
    value = _clean(text).replace("|", "/")
    return value if len(value) <= limit else value[: limit - 3].rstrip() + "..."


def _markdown_table_row(cells: Sequence[Any]) -> str:
    return "| " + " | ".join(_short(str(cell), 120) for cell in cells) + " |"


def _summary_markdown(metrics: Mapping[str, Any], case_rows: Sequence[Mapping[str, Any]], prompt_text: str) -> str:
    methods = metrics["methods"]
    comparison = metrics["comparison_vs_q0"]
    quality = metrics["json_quality"]
    decision = metrics["decision"]
    lines = [
        "# Evaluacion LLM attribute retrieval devset v0.1",
        "",
        "## Objetivo",
        "",
        "Evaluar una capa exploratoria pre-retrieval donde el LLM solo extrae atributos estructurados explicitos de la descripcion comercial. La fase usa exclusivamente el devset de 13 casos y no clasifica, no sugiere codigos NANDINA y no reemplaza la descripcion original.",
        "",
        "## Modelo usado",
        "",
        f"- Modelo local Ollama: `{metrics['generation']['model']}`.",
        f"- Endpoint local: `{metrics['generation']['ollama_url']}`.",
        f"- Temperature: {metrics['generation']['temperature']}.",
        "- APIs remotas: no usadas.",
        "- Text2Trade: no usado.",
        "- Evalset: no ejecutado.",
        "",
        "## Prompt usado",
        "",
        "```text",
        prompt_text.strip(),
        "```",
        "",
        "## Generacion de consultas",
        "",
        "- Q0: descripcion original, siempre conservada.",
        "- Q1: producto + material + composicion + estado.",
        "- Q2: producto + uso_funcion + presentacion + tecnologia + medidas.",
        "- Q3: producto + atributos_discriminantes + terminos_busqueda.",
        "- Marca/modelo se conserva como metadata y no entra en Q1-Q3.",
        "- Consultas vacias, genericas o con terminos de codigo arancelario se descartan.",
        "",
        "## Formula de fusion",
        "",
        "Se usa RRF ponderado por consulta:",
        "",
        "`score(d) = sum_q peso(q) / (k_rrf + rank_q(d))`, con `k_rrf = "
        f"{metrics['retrieval']['rrf_k']}`.",
        "",
        f"Pesos: Q0={QUERY_WEIGHTS['Q0']}, Q1={QUERY_WEIGHTS['Q1']}, Q2={QUERY_WEIGHTS['Q2']}, Q3={QUERY_WEIGHTS['Q3']}.",
        "",
        "La variante protegida fija los Top-10 de Q0 como bloque inicial y usa las consultas LLM solo como backfill despues de esos candidatos.",
        "",
        "## Metricas comparativas",
        "",
        "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in METHODS:
        data = methods[method]
        lines.append(
            f"| {method} | {data['top_1']:.4f} | {data['top_3']:.4f} | {data['top_5']:.4f} | "
            f"{data['top_10']:.4f} | {data['mrr']:.4f} | {data['recall_at_50']:.4f} | "
            f"{data['recall_at_100']:.4f} | {data['top_10_hs4']:.4f} | {data['top_10_hs2']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Comparacion contra Q0",
            "",
            "| Metodo | Ganados | Perdidos | Sin cambio | Nuevos Q0 no recuperaba | Degradados |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for method, data in comparison.items():
        lines.append(
            f"| {method} | {data['ganados']} | {data['perdidos']} | {data['sin_cambio']} | "
            f"{data['new_cases_q0_not_found_method_found']} | {data['degraded_cases']} |"
        )
    lines.extend(
        [
            "",
            "## Calidad JSON y violaciones",
            "",
            f"- JSON valido: {quality['valid_json_cases']}/{quality['cases_total']}.",
            f"- JSON invalido: {quality['invalid_json_cases']}.",
            f"- Codigos sugeridos o detectados: {quality['code_violation_cases']}.",
            f"- Terminos prohibidos detectados: {quality['forbidden_term_violation_cases']}.",
            f"- Posibles atributos inventados por heuristica: {quality['possible_invented_attribute_cases']}.",
            "",
            "## Tabla de los 13 casos",
            "",
            "| Caso | Descripcion original | JSON resumido | Q1 | Q2 | Q3 | Rank Q0 | Rank LLM protegido | Resultado |",
            "|---|---|---|---|---|---|---:|---:|---|",
        ]
    )
    for row in case_rows:
        lines.append(
            _markdown_table_row(
                [
                    row["case_id"],
                    row["descripcion_original"],
                    row["json_resumido"],
                    row["Q1"],
                    row["Q2"],
                    row["Q3"],
                    row["rank_BM25_hierarchical_Q0"],
                    row["rank_BM25_hierarchical_attribute_q0_protected"],
                    row["outcome_BM25_hierarchical_attribute_q0_protected"],
                ]
            )
        )
    lines.extend(
        [
            "",
            "## Decision metodologica",
            "",
            decision["recommendation"],
            "",
            f"- Mejora Recall@50 protegido: {decision['protected_recall50_delta']:+.4f}.",
            f"- Mejora Recall@100 protegido: {decision['protected_recall100_delta']:+.4f}.",
            f"- Delta Top-10 protegido: {decision['protected_top10_delta']:+.4f}.",
            f"- Delta MRR protegido: {decision['protected_mrr_delta']:+.4f}.",
            "",
            "## Limitaciones",
            "",
            "- Devset pequeno de 13 casos; sirve solo como diagnostico temprano.",
            "- La deteccion de atributos inventados es heuristica y debe revisarse manualmente.",
            "- La proteccion Q0 prioriza no degradar Top-10, por lo que la mejora esperada debe aparecer sobre todo como recall/backfill.",
            "- No valida fundamento legal ni clasificacion oficial; mide recuperacion documental.",
            "",
            "## Validaciones declaradas",
            "",
            "- Devset/evalset/Excel fuente no se modifican por estos scripts.",
            "- No se ejecuto evalset.",
            "- No se uso Text2Trade.",
            "- No se usaron APIs remotas.",
            "- Los artefactos JSONL/CSV son regenerables bajo `outputs/evaluation/llm_attribute_retrieval_devset_v0.1/`.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    extractions_path = resolve_project_path(args.extractions)
    prompt_path = resolve_project_path(args.prompt)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = args.retrieval_depth
    rrf_k = args.rrf_k

    dev_rows = _read_csv(devset_path)
    extraction_rows = _read_jsonl(extractions_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")
    if len(extraction_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Extraction row count is {len(extraction_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = load_bm25_index(ablation_index_dir / f"{PRECISION_VARIANT}.pkl")
    recall_index = load_bm25_index(ablation_index_dir / f"{RECALL_VARIANT}.pkl")
    prompt_text = prompt_path.read_text(encoding="utf-8")

    start = time.time()
    case_rows: list[dict[str, Any]] = []
    query_rows: list[dict[str, Any]] = []
    retrieval_rows: list[dict[str, Any]] = []

    for position, (dev_row, extraction_record) in enumerate(zip(dev_rows, extraction_rows), start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        true_code = _clean(dev_row.get("nandina") or dev_row.get("nandina_ref"))
        case_id = _clean(extraction_record.get("case_id")) or f"dev-{position:02d}"
        extraction = _extraction_from_record(extraction_record)
        queries = _build_queries(descripcion, extraction)

        source_hits: dict[str, list[dict[str, Any]]] = {}
        for label in QUERY_LABELS:
            query_text = queries[label]
            source_hits[label] = retrieve(hierarchical_index, query_text, top_n=depth) if query_text else []

        q0_hits = source_hits["Q0"]
        fused_hits = _weighted_rrf_fuse(source_hits, rrf_k=rrf_k, weights=QUERY_WEIGHTS, depth=depth)
        protected_hits = _q0_protected_fusion(q0_hits, fused_hits, protected_top_n=PROTECTED_TOP_N, depth=depth)

        precision_hits = retrieve(precision_index, descripcion, top_n=depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth=depth)
        phase7a_hits = _phase7a_pool(q0_hits, dual_hits, depth=depth)

        method_candidates = {
            "BM25_hierarchical_Q0": q0_hits,
            "BM25_hierarchical_attribute_weighted_rrf": fused_hits,
            "BM25_hierarchical_attribute_q0_protected": protected_hits,
            "phase7a_pool_hierarchical_80_dual_backfill_20": phase7a_hits,
        }
        ranks = {method: _rank_from_candidates(candidates, true_code) for method, candidates in method_candidates.items()}

        json_resumido = _json_summary(extraction)
        base_case: dict[str, Any] = {
            "case_id": case_id,
            "descripcion_original": descripcion,
            "nandina_ref": true_code,
            "json_resumido": json_resumido,
            "marca_modelo_metadata": _clean(extraction.get("marca_modelo")),
            "Q0": queries["Q0"],
            "Q1": queries["Q1"],
            "Q2": queries["Q2"],
            "Q3": queries["Q3"],
            "Q1_used": int(bool(queries["Q1"])),
            "Q2_used": int(bool(queries["Q2"])),
            "Q3_used": int(bool(queries["Q3"])),
            "json_valid": int(extraction_record.get("json_valid", 0)),
            "code_violation": int(extraction_record.get("code_violation", 0)),
            "forbidden_term_violation": int(extraction_record.get("forbidden_term_violation", 0)),
            "possible_invented_attribute_violation": int(extraction_record.get("possible_invented_attribute_violation", 0)),
        }
        for method in METHODS:
            candidates = method_candidates[method]
            base_case[f"rank_{method}"] = ranks[method]
            base_case[f"{method}_top10_hs4"] = _family_hit(candidates, true_code, 4, 10)
            base_case[f"{method}_top10_hs2"] = _family_hit(candidates, true_code, 2, 10)
            base_case[f"top10_codes_{method}"] = _top_codes(candidates)
            base_case[f"top10_json_{method}"] = json.dumps(_compact_top(candidates), ensure_ascii=False)
        for method in METHODS:
            if method == "BM25_hierarchical_Q0":
                continue
            base_case[f"outcome_{method}"] = _case_outcome(ranks["BM25_hierarchical_Q0"], ranks[method], depth)
        case_rows.append(base_case)

        query_rows.append(
            {
                "case_id": case_id,
                "descripcion_original": descripcion,
                "nandina_ref": true_code,
                "producto": _clean(extraction.get("producto")),
                "material": _clean(extraction.get("material")),
                "composicion": _clean(extraction.get("composicion")),
                "uso_funcion": _clean(extraction.get("uso_funcion")),
                "presentacion": _clean(extraction.get("presentacion")),
                "estado": _clean(extraction.get("estado")),
                "tecnologia": _clean(extraction.get("tecnologia")),
                "medidas": _clean(extraction.get("medidas")),
                "marca_modelo_metadata": _clean(extraction.get("marca_modelo")),
                "atributos_discriminantes": "; ".join(_list_values(extraction.get("atributos_discriminantes"))),
                "terminos_busqueda": "; ".join(_list_values(extraction.get("terminos_busqueda"))),
                "Q0": queries["Q0"],
                "Q1": queries["Q1"],
                "Q2": queries["Q2"],
                "Q3": queries["Q3"],
                "Q1_used": int(bool(queries["Q1"])),
                "Q2_used": int(bool(queries["Q2"])),
                "Q3_used": int(bool(queries["Q3"])),
            }
        )

        for method, candidates in method_candidates.items():
            retrieval_rows.append(
                {
                    "case_id": case_id,
                    "method": method,
                    "descripcion_original": descripcion,
                    "nandina_ref": true_code,
                    "rank": ranks[method],
                    "hit_top_1": int(acc_at_k(ranks[method], 1)),
                    "hit_top_3": int(acc_at_k(ranks[method], 3)),
                    "hit_top_5": int(acc_at_k(ranks[method], 5)),
                    "hit_top_10": int(acc_at_k(ranks[method], 10)),
                    "recall_at_50": int(acc_at_k(ranks[method], 50)),
                    "recall_at_100": int(acc_at_k(ranks[method], 100)),
                    "top10_hs4": _family_hit(candidates, true_code, 4, 10),
                    "top10_hs2": _family_hit(candidates, true_code, 2, 10),
                    "top10_codes": _top_codes(candidates),
                    "top10_json": json.dumps(_compact_top(candidates), ensure_ascii=False),
                }
            )

    methods_metrics = {
        method: _metrics_for_method(case_rows, method, k_list=K_LIST, depth=depth) for method in METHODS
    }
    comparison = {
        method: _comparison_vs_q0(case_rows, method, depth)
        for method in METHODS
        if method != "BM25_hierarchical_Q0"
    }
    q0_metrics = methods_metrics["BM25_hierarchical_Q0"]
    protected_metrics = methods_metrics["BM25_hierarchical_attribute_q0_protected"]
    recall50_delta = protected_metrics["recall_at_50"] - q0_metrics["recall_at_50"]
    recall100_delta = protected_metrics["recall_at_100"] - q0_metrics["recall_at_100"]
    top10_delta = protected_metrics["top_10"] - q0_metrics["top_10"]
    mrr_delta = protected_metrics["mrr"] - q0_metrics["mrr"]
    should_scale = (recall50_delta > 0 or recall100_delta > 0) and top10_delta >= -0.0001 and mrr_delta >= -0.0001
    recommendation = (
        "Escalar al evalset en una subfase separada, porque la variante protegida mejora el recall amplio sin deterioro material de Top-10/MRR."
        if should_scale
        else "No escalar al evalset: la capa LLM no mejora claramente Recall@50/Recall@100 frente a Q0 BM25 jerarquico, o no ofrece una ganancia suficiente para justificar el costo. Mantener prioridad en mejorar corpus y recuperacion documental base."
    )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_llm_attribute_retrieval_devset",
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
            "devset_sha256": sha256_file(devset_path),
            "attribute_extractions_path": _rel(extractions_path, root),
            "attribute_extractions_sha256": sha256_file(extractions_path),
            "prompt_path": _rel(prompt_path, root),
            "prompt_sha256": sha256_file(prompt_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "phase7a_precision_index": _rel(ablation_index_dir / f"{PRECISION_VARIANT}.pkl", root),
            "phase7a_recall_index": _rel(ablation_index_dir / f"{RECALL_VARIANT}.pkl", root),
        },
        "generation": {
            "model": _clean(extraction_rows[0].get("model")) if extraction_rows else "unknown",
            "ollama_url": _clean(args.ollama_url_for_report),
            "temperature": 0.0,
            "remote_apis_used": False,
            "text2trade_used": False,
            "evalset_executed": False,
        },
        "retrieval": {
            "retrieval_depth": depth,
            "rrf_k": rrf_k,
            "query_weights": dict(QUERY_WEIGHTS),
            "q0_protected_top_n": PROTECTED_TOP_N,
            "phase7a_strategy": PHASE7A_STRATEGY,
            "phase7a_dual_rule": "protected_top_5_backfill",
        },
        "json_quality": _json_quality(extraction_rows),
        "methods": methods_metrics,
        "comparison_vs_q0": comparison,
        "decision": {
            "should_scale_to_evalset": should_scale,
            "recommendation": recommendation,
            "protected_recall50_delta": recall50_delta,
            "protected_recall100_delta": recall100_delta,
            "protected_top10_delta": top10_delta,
            "protected_mrr_delta": mrr_delta,
        },
        "validations": {
            "devset_only": True,
            "evalset_executed": False,
            "text2trade_used": False,
            "remote_apis_used": False,
            "expected_devset_rows": EXPECTED_DEVSET_ROWS,
            "attribute_extractions_rows": len(extraction_rows),
            "attribute_queries_rows": len(query_rows),
            "case_comparison_rows": len(case_rows),
        },
        "outputs": {
            "attribute_queries_csv": _rel(output_dir / "attribute_queries.csv", root),
            "attribute_retrieval_results_csv": _rel(output_dir / "attribute_retrieval_results.csv", root),
            "attribute_retrieval_metrics_json": _rel(output_dir / "attribute_retrieval_metrics.json", root),
            "attribute_retrieval_summary_md": _rel(output_dir / "attribute_retrieval_summary.md", root),
            "attribute_case_comparison_13_cases_csv": _rel(output_dir / "attribute_case_comparison_13_cases.csv", root),
            "report_md": _rel(report_path, root),
        },
    }

    query_fields = [
        "case_id",
        "descripcion_original",
        "nandina_ref",
        "producto",
        "material",
        "composicion",
        "uso_funcion",
        "presentacion",
        "estado",
        "tecnologia",
        "medidas",
        "marca_modelo_metadata",
        "atributos_discriminantes",
        "terminos_busqueda",
        "Q0",
        "Q1",
        "Q2",
        "Q3",
        "Q1_used",
        "Q2_used",
        "Q3_used",
    ]
    retrieval_fields = [
        "case_id",
        "method",
        "descripcion_original",
        "nandina_ref",
        "rank",
        "hit_top_1",
        "hit_top_3",
        "hit_top_5",
        "hit_top_10",
        "recall_at_50",
        "recall_at_100",
        "top10_hs4",
        "top10_hs2",
        "top10_codes",
        "top10_json",
    ]
    case_fields = [
        "case_id",
        "descripcion_original",
        "nandina_ref",
        "json_resumido",
        "marca_modelo_metadata",
        "Q0",
        "Q1",
        "Q2",
        "Q3",
        "Q1_used",
        "Q2_used",
        "Q3_used",
        "json_valid",
        "code_violation",
        "forbidden_term_violation",
        "possible_invented_attribute_violation",
    ]
    for method in METHODS:
        case_fields.extend(
            [
                f"rank_{method}",
                f"{method}_top10_hs4",
                f"{method}_top10_hs2",
                f"top10_codes_{method}",
                f"top10_json_{method}",
            ]
        )
    for method in METHODS:
        if method != "BM25_hierarchical_Q0":
            case_fields.append(f"outcome_{method}")

    _write_csv(output_dir / "attribute_queries.csv", query_rows, query_fields)
    _write_csv(output_dir / "attribute_retrieval_results.csv", retrieval_rows, retrieval_fields)
    _write_csv(output_dir / "attribute_case_comparison_13_cases.csv", case_rows, case_fields)
    _write_json(output_dir / "attribute_retrieval_metrics.json", metrics)
    summary = _summary_markdown(metrics, case_rows, prompt_text)
    ensure_parent(output_dir / "attribute_retrieval_summary.md")
    (output_dir / "attribute_retrieval_summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate LLM attribute retrieval on devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--extractions", type=Path, default=DEFAULT_EXTRACTIONS)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--ollama-url-for-report", default="http://127.0.0.1:11434/api/chat")
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion LLM attribute retrieval devset completada")
    print(f"Casos evaluados: {metrics['json_quality']['cases_total']}")
    for method in METHODS:
        data = metrics["methods"][method]
        print(
            f"{method}: top10={data['top_10']:.4f} mrr={data['mrr']:.4f} "
            f"recall50={data['recall_at_50']:.4f} recall100={data['recall_at_100']:.4f}"
        )
    print(metrics["decision"]["recommendation"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
