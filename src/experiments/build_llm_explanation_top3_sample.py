from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_HISTORICAL_RESULTS = Path(
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_results.csv"
)
DEFAULT_HISTORICAL_CASE_SUMMARY = Path(
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_case_summary.csv"
)
DEFAULT_NORMATIVE_CORPUS = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_sample_v0.1")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
EXPECTED_SAMPLE_SIZE = 30
TOP3_SIZE = 3
SAMPLE_TARGETS = {
    "rank_1": 10,
    "rank_2_3": 10,
    "rank_4_10": 5,
    "difficult_low_support": 5,
}
SUPPORT_ORDER = {"0": 0, "1": 1, "2-4": 2, "5-9": 3, "10+": 4}


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


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_jsonl(path: Path):
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            raw = line.strip()
            if raw:
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _valid_nandina(code: str) -> bool:
    return bool(re.fullmatch(r"\d{8}", _clean(code)))


def _limit_text(text: str, limit: int = 900) -> str:
    clean = " ".join(_clean(text).split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rstrip() + "..."


def _case_category(row: Mapping[str, str]) -> str:
    rank = int(_clean(row.get("exact_rank")) or "0")
    support_bucket = _clean(row.get("support_bucket"))
    if rank == 1:
        return "rank_1"
    if 2 <= rank <= 3:
        return "rank_2_3"
    if 4 <= rank <= 10:
        return "rank_4_10"
    if support_bucket in {"0", "1", "2-4", "5-9"} or rank == 0 or rank > 10:
        return "difficult_low_support"
    return "other"


def _selection_sort_key(row: Mapping[str, str]) -> tuple[Any, ...]:
    rank = int(_clean(row.get("exact_rank")) or "999999")
    support_bucket = _clean(row.get("support_bucket"))
    support_count = int(_clean(row.get("historical_support_count")) or "999999")
    return (
        SUPPORT_ORDER.get(support_bucket, 99),
        support_count,
        0 if rank == 0 else rank,
        _clean(row.get("case_id")),
    )


def _select_sample(case_rows: Sequence[Mapping[str, str]]) -> list[dict[str, Any]]:
    by_category: dict[str, list[Mapping[str, str]]] = defaultdict(list)
    for row in case_rows:
        by_category[_case_category(row)].append(row)
    for rows in by_category.values():
        rows.sort(key=_selection_sort_key)

    selected_ids: set[str] = set()
    selected: list[dict[str, Any]] = []
    fallback_categories = ["difficult_low_support", "rank_4_10", "rank_2_3", "rank_1", "other"]
    for target_category, target_count in SAMPLE_TARGETS.items():
        candidates = [(target_category, row) for row in by_category.get(target_category, [])]
        for category in fallback_categories:
            if category != target_category:
                candidates.extend((category, row) for row in by_category.get(category, []))
        picked = 0
        for source_category, row in candidates:
            case_id = _clean(row.get("case_id"))
            if not case_id or case_id in selected_ids:
                continue
            selected_ids.add(case_id)
            picked += 1
            selected.append(
                {
                    "case_id": case_id,
                    "id_unico": _clean(row.get("id_unico")),
                    "expected_nandina": _clean(row.get("expected_nandina")),
                    "expected_rank_historical": int(_clean(row.get("exact_rank")) or "0"),
                    "sample_target_category": target_category,
                    "selection_source_category": source_category,
                    "selection_note": "exact_category" if source_category == target_category else f"fallback_from_{source_category}",
                    "support_bucket": _clean(row.get("support_bucket")),
                    "historical_support_count": int(_clean(row.get("historical_support_count")) or "0"),
                    "descripcion_mercancia": _clean(row.get("query")),
                }
            )
            if picked >= target_count:
                break
        if picked < target_count:
            raise ValueError(f"Could not select {target_count} cases for {target_category}; selected {picked}")
    if len(selected) != EXPECTED_SAMPLE_SIZE:
        raise ValueError(f"Expected {EXPECTED_SAMPLE_SIZE} sample cases, selected {len(selected)}")
    return selected


def _load_top3(path: Path) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in _read_csv(path):
        rank = int(_clean(row.get("candidate_rank")) or "0")
        if not 1 <= rank <= TOP3_SIZE:
            continue
        code = _clean(row.get("candidate_nandina"))
        if not _valid_nandina(code):
            raise ValueError(f"Invalid candidate NANDINA in historical results: {code}")
        grouped[_clean(row.get("case_id"))].append(
            {
                "rank_original": rank,
                "nandina": code,
                "score_historico": float(_clean(row.get("score")) or 0.0),
                "candidate_history_rank": int(_clean(row.get("candidate_history_rank")) or "0"),
                "candidate_case_id": _clean(row.get("candidate_case_id")),
                "candidate_id_unico": _clean(row.get("candidate_id_unico")),
                "candidate_clase": _clean(row.get("candidate_clase")),
                "candidate_partida": _clean(row.get("candidate_partida")),
                "candidate_sub_partida": _clean(row.get("candidate_sub_partida")),
                "evidencia_historica": _limit_text(row.get("candidate_description"), 800),
            }
        )
    for case_id, rows in grouped.items():
        rows.sort(key=lambda item: int(item["rank_original"]))
        ranks = [int(item["rank_original"]) for item in rows]
        if ranks != [1, 2, 3]:
            raise ValueError(f"Case {case_id} has incomplete Top-3 ranks: {ranks}")
    return grouped


def _load_normative_index(path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for row in _read_jsonl(path):
        code = _clean(row.get("nandina_8d") or row.get("codigo"))
        if _valid_nandina(code) and code not in index:
            index[code] = row
    return index


def _normative_context(code: str, row: Mapping[str, Any] | None, rank: int) -> dict[str, Any]:
    if not row:
        return {
            "descripcion_normativa": "",
            "contexto_jerarquico": {},
            "evidencias_normativas": [],
            "advertencia_evidencia": "Sin registro normativo encontrado en corpus jerarquico.",
        }
    evidence_id = f"E{rank}-NORM-1"
    return {
        "descripcion_normativa": _clean(row.get("descripcion_nandina_8d") or row.get("titulo")),
        "contexto_jerarquico": {
            "seccion": _clean(row.get("section")),
            "seccion_titulo": _clean(row.get("section_title")),
            "capitulo": _clean(row.get("chapter")),
            "capitulo_titulo": _clean(row.get("chapter_title")),
            "partida": _clean(row.get("partida_4d")),
            "descripcion_partida": _clean(row.get("descripcion_partida_4d")),
            "subpartida": _clean(row.get("hs_6d")),
            "descripcion_subpartida": _clean(row.get("descripcion_hs_6d")),
            "nandina": code,
            "descripcion_nandina": _clean(row.get("descripcion_nandina_8d") or row.get("titulo")),
            "unidad_fisica": _clean(row.get("unidad_fisica")),
        },
        "evidencias_normativas": [
            {
                "evidence_id": evidence_id,
                "fuente": _clean(row.get("fuente") or "NANDINA"),
                "pagina": _clean(row.get("source_page") or row.get("pagina_inicio")),
                "linea": _clean(row.get("source_line_no")),
                "texto": _limit_text(row.get("source_line_text") or row.get("texto"), 500),
            }
        ],
        "advertencia_evidencia": "",
    }


def _observable_series_data(eval_row: Mapping[str, str]) -> dict[str, str]:
    allowed = [
        "SERIE",
        "Clase",
        "FECHA NUMERACION",
        "PAIS ORIGEN",
        "PAIS ADQUISICION",
        "PESO NETO (KG)",
        "PESO BRUTO (KG)",
        "UNIDADES COMERCIALES",
        "UNIDADES FISICAS U.F.",
        "TIPO U.C.",
    ]
    output = {key.lower().replace(" ", "_").replace(".", ""): _clean(eval_row.get(key)) for key in allowed}
    output["nota"] = "No se incluye NANDINA esperada, Partida esperada ni Sub Partida esperada en el payload LLM."
    return output


def _build_payload(
    sample: Mapping[str, Any],
    eval_row: Mapping[str, str],
    top3: Sequence[Mapping[str, Any]],
    normative_index: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for candidate in top3:
        rank = int(candidate["rank_original"])
        code = _clean(candidate["nandina"])
        context = _normative_context(code, normative_index.get(code), rank)
        candidates.append(
            {
                **candidate,
                "descripcion_normativa": context["descripcion_normativa"],
                "contexto_jerarquico": context["contexto_jerarquico"],
                "evidencias_normativas": context["evidencias_normativas"],
                "advertencia_evidencia": context["advertencia_evidencia"],
            }
        )
    return {
        "version": "v0.1",
        "phase": "10A_llm_explanation_top3_sample",
        "case_id": sample["case_id"],
        "id_unico": sample["id_unico"],
        "descripcion_mercancia": _clean(sample["descripcion_mercancia"]),
        "datos_serie_observables": _observable_series_data(eval_row),
        "top3_original": candidates,
        "reglas": {
            "llm_puede_agregar_candidatos": False,
            "llm_puede_reordenar": False,
            "llm_puede_usar_codigos_fuera_top3": False,
            "debe_devolver_json_estricto": True,
        },
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    root = project_root()
    eval_path = resolve_project_path(args.evalset)
    historical_results_path = resolve_project_path(args.historical_results)
    historical_case_summary_path = resolve_project_path(args.historical_case_summary)
    normative_corpus_path = resolve_project_path(args.normative_corpus)
    output_dir = resolve_project_path(args.output_dir)

    eval_rows = _read_csv(eval_path)
    eval_by_case = {_clean(row.get("case_id")): row for row in eval_rows}
    case_rows = _read_csv(historical_case_summary_path)
    top3_by_case = _load_top3(historical_results_path)
    normative_index = _load_normative_index(normative_corpus_path)

    sample = _select_sample(case_rows)
    payloads: list[dict[str, Any]] = []
    for item in sample:
        case_id = item["case_id"]
        if case_id not in eval_by_case:
            raise ValueError(f"Sample case missing from evalset: {case_id}")
        top3 = top3_by_case.get(case_id, [])
        if len(top3) != TOP3_SIZE:
            raise ValueError(f"Sample case {case_id} has {len(top3)} Top-3 candidates")
        payloads.append(_build_payload(item, eval_by_case[case_id], top3, normative_index))

    sample_fieldnames = [
        "case_id",
        "id_unico",
        "expected_nandina",
        "expected_rank_historical",
        "sample_target_category",
        "selection_source_category",
        "selection_note",
        "support_bucket",
        "historical_support_count",
        "descripcion_mercancia",
    ]
    _write_csv(output_dir / "sample_cases.csv", sample, sample_fieldnames)
    _write_jsonl(output_dir / "payloads.jsonl", payloads)

    composition = Counter(row["sample_target_category"] for row in sample)
    source_composition = Counter(row["selection_source_category"] for row in sample)
    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "10A_llm_explanation_top3_sample",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform()},
        "inputs": {
            "evalset": _rel(eval_path, root),
            "historical_results": _rel(historical_results_path, root),
            "historical_case_summary": _rel(historical_case_summary_path, root),
            "normative_corpus": _rel(normative_corpus_path, root),
        },
        "input_sha256": {
            "evalset": _sha256_file(eval_path),
            "historical_results": _sha256_file(historical_results_path),
            "historical_case_summary": _sha256_file(historical_case_summary_path),
            "normative_corpus": _sha256_file(normative_corpus_path),
        },
        "parameters": {
            "sample_size": EXPECTED_SAMPLE_SIZE,
            "top3_size": TOP3_SIZE,
            "sample_targets": SAMPLE_TARGETS,
            "selection_rule": (
                "Deterministic balanced sample by historical exact rank: rank_1, rank_2_3, "
                "rank_4_10, and difficult/low support. Ties sort by lower historical support and case_id."
            ),
        },
        "sample_composition": dict(composition),
        "selection_source_composition": dict(source_composition),
        "validation": {
            "sample_cases": len(sample),
            "payloads": len(payloads),
            "top3_complete": all(len(row["top3_original"]) == TOP3_SIZE for row in payloads),
            "expected_label_excluded_from_llm_payload": True,
            "candidate_order_locked": True,
            "remote_api_used": False,
            "openai_used": False,
        },
        "outputs": {
            "sample_cases_csv": _rel(output_dir / "sample_cases.csv", root),
            "payloads_jsonl": _rel(output_dir / "payloads.jsonl", root),
            "build_metadata_json": _rel(output_dir / "build_metadata.json", root),
        },
        "elapsed_seconds": time.perf_counter() - started,
    }
    _write_json(output_dir / "build_metadata.json", payload)
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Top-3 explanation payloads for local LLM diagnostic sample.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--historical-results", default=str(DEFAULT_HISTORICAL_RESULTS))
    parser.add_argument("--historical-case-summary", default=str(DEFAULT_HISTORICAL_CASE_SUMMARY))
    parser.add_argument("--normative-corpus", default=str(DEFAULT_NORMATIVE_CORPUS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    return parser


def main() -> int:
    payload = build(build_parser().parse_args())
    print("OK: payloads Fase 10A construidos")
    print(f"Casos muestra: {payload['validation']['sample_cases']}")
    print(f"Composicion objetivo: {payload['sample_composition']}")
    print(f"Composicion real por fuente: {payload['selection_source_composition']}")
    print(f"Outputs: {payload['outputs']['payloads_jsonl']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
