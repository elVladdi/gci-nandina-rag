from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import time
from collections import Counter
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
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_explanation_top3_audit_sample_v0.1")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
EXPECTED_SAMPLE_SIZE = 50
TOP3_SIZE = 3
SEED = 2026
SAMPLE_TARGETS = {
    "rank_1": 15,
    "rank_2_3": 15,
    "rank_4_10": 10,
    "difficult_low_support": 10,
}
SUPPORT_ORDER = {"0": 0, "1": 1, "2-4": 2, "5-9": 3, "10+": 4, "": 99}
FORBIDDEN_LLM_PAYLOAD_KEYS = {
    "expected_nandina",
    "nandina_esperada",
    "expected_rank_historical",
    "exact_rank",
    "acierto",
    "error",
}


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


def _read_jsonl(path: Path):
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            raw = line.strip()
            if raw:
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _rel(path: Path, root: Path | None = None) -> str:
    root = root or project_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _valid_nandina(code: str) -> bool:
    return bool(re.fullmatch(r"\d{8}", _clean(code)))


def _limit_text(text: object, limit: int = 900) -> str:
    clean = " ".join(_clean(text).split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rstrip() + "..."


def _as_int(value: object, default: int = 0) -> int:
    try:
        return int(float(_clean(value)))
    except ValueError:
        return default


def _target_match(row: Mapping[str, str], target: str) -> bool:
    rank = _as_int(row.get("exact_rank"))
    support_bucket = _clean(row.get("support_bucket"))
    if target == "rank_1":
        return rank == 1
    if target == "rank_2_3":
        return 2 <= rank <= 3
    if target == "rank_4_10":
        return 4 <= rank <= 10
    if target == "difficult_low_support":
        return rank == 0 or rank > 10 or support_bucket in {"0", "1", "2-4", "5-9"}
    return False


def _primary_category(row: Mapping[str, str]) -> str:
    for category in SAMPLE_TARGETS:
        if _target_match(row, category):
            return category
    return "other"


def _selection_sort_key(row: Mapping[str, str]) -> tuple[Any, ...]:
    rank = _as_int(row.get("exact_rank"), 999999)
    support_bucket = _clean(row.get("support_bucket"))
    support_count = _as_int(row.get("historical_support_count"), 999999)
    difficult_rank = 999999 if rank == 0 else rank
    return (
        SUPPORT_ORDER.get(support_bucket, 99),
        support_count,
        difficult_rank,
        _clean(row.get("case_id")),
    )


def _select_sample(case_rows: Sequence[Mapping[str, str]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected_ids: set[str] = set()
    selected: list[dict[str, Any]] = []
    target_availability = {
        target: sum(1 for row in case_rows if _target_match(row, target)) for target in SAMPLE_TARGETS
    }
    balance_notes: list[str] = []

    def add_row(row: Mapping[str, str], target: str, source: str, note: str) -> None:
        selected_ids.add(_clean(row.get("case_id")))
        selected.append(
            {
                "case_id": _clean(row.get("case_id")),
                "id_unico": _clean(row.get("id_unico")),
                "expected_nandina": _clean(row.get("expected_nandina")),
                "expected_rank_historical": _as_int(row.get("exact_rank")),
                "sample_target_category": target,
                "selection_source_category": source,
                "selection_note": note,
                "support_bucket": _clean(row.get("support_bucket")),
                "historical_support_count": _as_int(row.get("historical_support_count")),
                "descripcion_mercancia": _clean(row.get("query")),
            }
        )

    all_sorted = sorted(case_rows, key=_selection_sort_key)
    for target, target_count in SAMPLE_TARGETS.items():
        exact_candidates = [row for row in all_sorted if _target_match(row, target)]
        picked = 0
        for row in exact_candidates:
            case_id = _clean(row.get("case_id"))
            if not case_id or case_id in selected_ids:
                continue
            add_row(row, target, target, "exact_category")
            picked += 1
            if picked >= target_count:
                break
        if picked < target_count:
            balance_notes.append(
                f"{target}: target={target_count}, exact_available={target_availability[target]}, exact_picked={picked}; deterministic fallback used."
            )
            for row in all_sorted:
                case_id = _clean(row.get("case_id"))
                if not case_id or case_id in selected_ids:
                    continue
                source = _primary_category(row)
                add_row(row, target, source, f"fallback_from_{source}")
                picked += 1
                if picked >= target_count:
                    break
        if picked < target_count:
            raise ValueError(f"Could not select {target_count} cases for {target}; selected {picked}")

    if len(selected) != EXPECTED_SAMPLE_SIZE:
        raise ValueError(f"Expected {EXPECTED_SAMPLE_SIZE} sample cases, selected {len(selected)}")
    metadata = {
        "seed": SEED,
        "selection_rule": (
            "Deterministic stratified sample over historical exact rank and low-support signals. "
            "Rows are sorted by support bucket, historical support count, exact rank and case_id; "
            "fallback is only used if a target stratum cannot be filled exactly."
        ),
        "target_availability": target_availability,
        "target_composition": dict(Counter(row["sample_target_category"] for row in selected)),
        "source_composition": dict(Counter(row["selection_source_category"] for row in selected)),
        "balance_notes": balance_notes or ["Exact target balance achieved without fallback."],
    }
    return selected, metadata


def _load_top3(path: Path) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in _read_csv(path):
        rank = _as_int(row.get("candidate_rank"))
        if not 1 <= rank <= TOP3_SIZE:
            continue
        code = _clean(row.get("candidate_nandina"))
        if not _valid_nandina(code):
            raise ValueError(f"Invalid candidate NANDINA in historical results: {code}")
        case_id = _clean(row.get("case_id"))
        grouped.setdefault(case_id, []).append(
            {
                "rank_original": rank,
                "nandina": code,
                "score_historico": float(_clean(row.get("score")) or 0.0),
                "candidate_id_unico": _clean(row.get("candidate_id_unico")),
                "candidate_case_id": _clean(row.get("candidate_case_id")),
                "candidate_history_rank": _as_int(row.get("candidate_history_rank")),
                "evidencia_historica": {
                    "candidate_id_unico": _clean(row.get("candidate_id_unico")),
                    "candidate_case_id": _clean(row.get("candidate_case_id")),
                    "texto": _limit_text(row.get("candidate_description"), 1000),
                    "fuente": "data_aduanas_historico_clase87_v0.1",
                },
                "ruta_jerarquica": {
                    "clase": _clean(row.get("candidate_clase")),
                    "partida": _clean(row.get("candidate_partida")),
                    "sub_partida": _clean(row.get("candidate_sub_partida")),
                    "nandina": code,
                },
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
            "evidencias_normativas": [
                {
                    "evidence_id": f"R{rank}-NORM-MISSING",
                    "fuente": "NANDINA",
                    "pagina": "",
                    "linea": "",
                    "texto": "Sin registro normativo encontrado en corpus jerarquico.",
                }
            ],
        }
    text = _limit_text(row.get("source_line_text") or row.get("texto") or row.get("texto_index"), 700)
    if not text:
        text = _limit_text(row.get("descripcion_nandina_8d") or row.get("titulo"), 700)
    return {
        "descripcion_normativa": _clean(row.get("descripcion_nandina_8d") or row.get("titulo")),
        "evidencias_normativas": [
            {
                "evidence_id": f"R{rank}-NORM-1",
                "fuente": _clean(row.get("fuente") or "NANDINA"),
                "pagina": _clean(row.get("source_page") or row.get("pagina_inicio")),
                "linea": _clean(row.get("source_line_no")),
                "texto": text,
            }
        ],
    }


def _observable_eval_data(eval_row: Mapping[str, str]) -> dict[str, str]:
    allowed = [
        "SERIE",
        "Clase",
        "PAIS ORIGEN",
        "PAIS ADQUISICION",
        "PESO NETO (KG)",
        "PESO BRUTO (KG)",
        "UNIDADES COMERCIALES",
        "UNIDADES FISICAS U.F.",
        "TIPO U.C.",
    ]
    output = {key.lower().replace(" ", "_").replace(".", "").replace("-", "_"): _clean(eval_row.get(key)) for key in allowed}
    output["descripcion_fuente"] = QUERY_COLUMN
    output["nota"] = "Payload limitado a datos observables, candidatos Top-3 y evidencias recuperadas."
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
        normative = _normative_context(code, normative_index.get(code), rank)
        candidates.append(
            {
                **candidate,
                "descripcion_normativa": normative["descripcion_normativa"],
                "evidencias_normativas": normative["evidencias_normativas"],
            }
        )
    return {
        "version": "v0.1",
        "phase": "10B_llm_explanation_top3_audit_sample",
        "id_unico": sample["id_unico"],
        "case_id": sample["case_id"],
        "descripcion_mercancia": _clean(sample["descripcion_mercancia"]),
        "resumen_payload": _observable_eval_data(eval_row),
        "top3_original": candidates,
        "reglas": {
            "llm_puede_agregar_candidatos": False,
            "llm_puede_reordenar": False,
            "llm_puede_usar_codigos_fuera_top3": False,
            "llm_emite_clasificacion_oficial": False,
            "debe_devolver_json_estricto": True,
        },
    }


def _assert_expected_label_not_in_payloads(payloads: Sequence[Mapping[str, Any]]) -> None:
    """Validate forbidden structural field names without scanning explanatory text values."""
    def walk(value: Any, path: str = "") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                lowered = _clean(key).lower()
                if lowered in FORBIDDEN_LLM_PAYLOAD_KEYS:
                    raise ValueError(f"Forbidden key sent to LLM payload: {path}/{key}")
                walk(child, f"{path}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")

    for payload in payloads:
        walk(payload)


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

    sample, sample_metadata = _select_sample(case_rows)
    payloads: list[dict[str, Any]] = []
    for item in sample:
        case_id = item["case_id"]
        if case_id not in eval_by_case:
            raise ValueError(f"Sample case missing from evalset: {case_id}")
        top3 = top3_by_case.get(case_id, [])
        if len(top3) != TOP3_SIZE:
            raise ValueError(f"Sample case {case_id} has {len(top3)} Top-3 candidates")
        payloads.append(_build_payload(item, eval_by_case[case_id], top3, normative_index))
    _assert_expected_label_not_in_payloads(payloads)

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

    metadata: dict[str, Any] = {
        "version": "v0.1",
        "phase": "10B_llm_explanation_top3_audit_sample",
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
            "seed": SEED,
            "query_column": QUERY_COLUMN,
        },
        "sample": sample_metadata,
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
    _write_json(output_dir / "build_metadata.json", metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build formal Top-3 audit explanation payloads for local LLM.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--historical-results", default=str(DEFAULT_HISTORICAL_RESULTS))
    parser.add_argument("--historical-case-summary", default=str(DEFAULT_HISTORICAL_CASE_SUMMARY))
    parser.add_argument("--normative-corpus", default=str(DEFAULT_NORMATIVE_CORPUS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: payloads Fase 10B construidos")
    print(f"Casos muestra: {metadata['validation']['sample_cases']}")
    print(f"Composicion objetivo: {metadata['sample']['target_composition']}")
    print(f"Composicion real por fuente: {metadata['sample']['source_composition']}")
    print(f"Outputs: {metadata['outputs']['payloads_jsonl']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
