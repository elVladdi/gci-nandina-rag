from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_PHASE7A_DEVSET_POOL = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool.csv")
DEFAULT_PHASE7A_EVALSET_POOL = Path("outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/analysis/hierarchical_retrieval_ceiling_v0.1")
PHASE7A_STRATEGY = "hierarchical_80_dual_backfill_20"
K_VALUES = [10, 20, 50, 100]
EXPECTED_ROWS = {"devset": 13, "evalset": 600}


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


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _case_id(dataset: str, row: Mapping[str, Any], position: int) -> str:
    return _clean(row.get("case_id")) or f"{dataset}-{position:02d}"


def _expected_code(row: Mapping[str, Any]) -> str:
    return _clean(row.get("nandina") or row.get("nandina_ref"))


def _rank_exact(hits: Sequence[Mapping[str, Any]], expected_code: str) -> int:
    for rank, hit in enumerate(hits, start=1):
        if _clean(hit.get("code")) == expected_code:
            return rank
    return 0


def _rank_prefix(hits: Sequence[Mapping[str, Any]], expected_code: str, prefix_len: int) -> int:
    prefix = expected_code[:prefix_len]
    for rank, hit in enumerate(hits, start=1):
        if _clean(hit.get("code")).startswith(prefix):
            return rank
    return 0


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _phase7_pool_hits(path: Path) -> dict[str, list[dict[str, Any]]]:
    if not path.exists():
        return {}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return {}
        for row in reader:
            if _clean(row.get("pool_strategy")) != PHASE7A_STRATEGY:
                continue
            case_id = _clean(row.get("case_id"))
            code = _clean(row.get("candidate_code"))
            if not case_id or not code:
                continue
            try:
                rank = int(_clean(row.get("candidate_rank_pool")))
            except ValueError:
                continue
            if rank <= max(K_VALUES):
                grouped[case_id].append({"rank": rank, "code": code, "score": row.get("candidate_score_pool", "")})
    for hits in grouped.values():
        hits.sort(key=lambda item: int(item["rank"]))
    return dict(grouped)


def _hit_metrics(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    metrics: dict[str, Any] = {"cases_total": len(rows)}
    for k in K_VALUES:
        metrics[f"nandina8_at_{k}"] = _mean([float(row[f"nandina8_at_{k}"]) for row in rows])
        metrics[f"hs6_at_{k}"] = _mean([float(row[f"hs6_at_{k}"]) for row in rows])
        metrics[f"hs4_at_{k}"] = _mean([float(row[f"hs4_at_{k}"]) for row in rows])
        metrics[f"hs2_at_{k}"] = _mean([float(row[f"hs2_at_{k}"]) for row in rows])
    metrics["hs2_present_nandina8_absent_at_100"] = sum(int(row["hs2_present_nandina8_absent_at_100"]) for row in rows)
    metrics["hs4_present_nandina8_absent_at_100"] = sum(int(row["hs4_present_nandina8_absent_at_100"]) for row in rows)
    metrics["hs2_absent_at_100"] = sum(int(row["hs2_absent_at_100"]) for row in rows)
    return metrics


def _diagnostic_rows(
    dataset: str,
    input_rows: Sequence[Mapping[str, Any]],
    method: str,
    hits_by_case: Mapping[str, Sequence[Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for position, source_row in enumerate(input_rows, start=1):
        case_id = _case_id(dataset, source_row, position)
        expected = _expected_code(source_row)
        hits = list(hits_by_case.get(case_id, []))
        exact_rank = _rank_exact(hits, expected)
        hs2_rank = _rank_prefix(hits, expected, 2)
        hs4_rank = _rank_prefix(hits, expected, 4)
        hs6_rank = _rank_prefix(hits, expected, 6)
        row: dict[str, Any] = {
            "dataset": dataset,
            "method": method,
            "case_id": case_id,
            "descripcion": _clean(source_row.get("descripcion")),
            "nandina_ref": expected,
            "hs2_ref": expected[:2],
            "hs4_ref": expected[:4],
            "hs6_ref": expected[:6],
            "exact_rank_at_100": exact_rank,
            "hs2_first_rank_at_100": hs2_rank,
            "hs4_first_rank_at_100": hs4_rank,
            "hs6_first_rank_at_100": hs6_rank,
            "top_10_codes": _top_codes(hits, 10),
        }
        for k in K_VALUES:
            row[f"nandina8_at_{k}"] = int(0 < exact_rank <= k)
            row[f"hs2_at_{k}"] = int(0 < hs2_rank <= k)
            row[f"hs4_at_{k}"] = int(0 < hs4_rank <= k)
            row[f"hs6_at_{k}"] = int(0 < hs6_rank <= k)
        row["hs2_present_nandina8_absent_at_100"] = int(row["hs2_at_100"] and not row["nandina8_at_100"])
        row["hs4_present_nandina8_absent_at_100"] = int(row["hs4_at_100"] and not row["nandina8_at_100"])
        row["hs2_absent_at_100"] = int(not row["hs2_at_100"])
        rows.append(row)
    return rows


def _family_error(rows: Sequence[Mapping[str, Any]], field: str) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(_clean(row["method"]), _clean(row[field]))].append(row)
    output: list[dict[str, Any]] = []
    for (method, family), items in sorted(grouped.items()):
        total = len(items)
        output.append(
            {
                "method": method,
                field: family,
                "cases_total": total,
                "nandina8_miss_at_100": sum(1 for row in items if not int(row["nandina8_at_100"])),
                "hs2_miss_at_100": sum(1 for row in items if not int(row["hs2_at_100"])),
                "hs4_miss_at_100": sum(1 for row in items if not int(row["hs4_at_100"])),
                "hs6_miss_at_100": sum(1 for row in items if not int(row["hs6_at_100"])),
                "nandina8_at_100": _mean([float(row["nandina8_at_100"]) for row in items]),
                "hs2_at_100": _mean([float(row["hs2_at_100"]) for row in items]),
                "hs4_at_100": _mean([float(row["hs4_at_100"]) for row in items]),
                "hs6_at_100": _mean([float(row["hs6_at_100"]) for row in items]),
            }
        )
    return output


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Diagnostico techo recuperacion jerarquica v0.1",
        "",
        "## Alcance",
        "",
        "Diagnostico de cobertura por familia arancelaria en devset y evalset. No selecciona estrategia con evalset; solo mide techo observado por HS2, HS4, HS6 y NANDINA8 en Top-K.",
        "",
        "## Metricas principales",
        "",
        "| Dataset | Metodo | NANDINA8@100 | HS6@100 | HS4@100 | HS2@100 | HS2 si, NANDINA8 no | HS4 si, NANDINA8 no | HS2 ausente |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for dataset in ["devset", "evalset"]:
        for method, metrics in payload[dataset]["metrics_by_method"].items():
            lines.append(
                f"| {dataset} | {method} | {metrics['nandina8_at_100']:.4f} | {metrics['hs6_at_100']:.4f} | {metrics['hs4_at_100']:.4f} | {metrics['hs2_at_100']:.4f} | {metrics['hs2_present_nandina8_absent_at_100']} | {metrics['hs4_present_nandina8_absent_at_100']} | {metrics['hs2_absent_at_100']} |"
            )
    lines.extend(
        [
            "",
            "## Lectura",
            "",
            "La brecha entre HS2/HS4/HS6@100 y NANDINA8@100 indica cuanto techo potencial existe si el recuperador acierta la familia pero pierde la subpartida exacta. La Fase 8A usa estos resultados como diagnostico; la seleccion de estrategia se mantiene en devset.",
            "",
        ]
    )
    return "\n".join(lines)


def diagnose(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    evalset_path = resolve_project_path(args.evalset)
    index_path = resolve_project_path(args.hierarchical_index)
    phase7a_devset_path = resolve_project_path(args.phase7a_devset_pool)
    phase7a_evalset_path = resolve_project_path(args.phase7a_evalset_pool)
    output_dir = resolve_project_path(args.output_dir)
    start = time.time()

    datasets = {
        "devset": _read_csv(devset_path),
        "evalset": _read_csv(evalset_path),
    }
    for name, rows in datasets.items():
        if len(rows) != EXPECTED_ROWS[name]:
            raise ValueError(f"{name} row count is {len(rows)}, expected {EXPECTED_ROWS[name]}.")

    index = load_bm25_index(index_path)
    hits_by_dataset: dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = {}
    for dataset, rows in datasets.items():
        method_hits: dict[str, dict[str, list[dict[str, Any]]]] = {"BM25_hierarchical_v0.1": {}}
        for position, row in enumerate(rows, start=1):
            case_id = _case_id(dataset, row, position)
            method_hits["BM25_hierarchical_v0.1"][case_id] = retrieve(index, _clean(row.get("descripcion")), top_n=max(K_VALUES))
        pool_path = phase7a_devset_path if dataset == "devset" else phase7a_evalset_path
        phase7_hits = _phase7_pool_hits(pool_path)
        if phase7_hits:
            method_hits["phase7a_pool_hierarchical_80_dual_backfill_20"] = phase7_hits
        hits_by_dataset[dataset] = method_hits

    output_payload: dict[str, Any] = {
        "script": "src.analysis.diagnose_hierarchical_retrieval_ceiling",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": 0.0,
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "inputs": {
            "devset_path": _rel(devset_path, root),
            "devset_sha256": sha256_file(devset_path),
            "evalset_path": _rel(evalset_path, root),
            "evalset_sha256": sha256_file(evalset_path),
            "hierarchical_index_path": _rel(index_path, root),
            "hierarchical_index_sha256": sha256_file(index_path),
            "phase7a_devset_pool": _rel(phase7a_devset_path, root) if phase7a_devset_path.exists() else "",
            "phase7a_evalset_pool": _rel(phase7a_evalset_path, root) if phase7a_evalset_path.exists() else "",
        },
        "k_values": K_VALUES,
        "policy": {
            "llm_used": False,
            "ollama_used": False,
            "openai_used": False,
            "text2trade_used": False,
            "remote_apis_used": False,
            "evalset_used_for_strategy_selection": False,
        },
    }

    evalset_all_rows: list[dict[str, Any]] = []
    for dataset, rows in datasets.items():
        dataset_rows: list[dict[str, Any]] = []
        metrics_by_method: dict[str, Any] = {}
        error_counts: dict[str, Any] = {}
        for method, hits_by_case in hits_by_dataset[dataset].items():
            diagnostic_rows = _diagnostic_rows(dataset, rows, method, hits_by_case)
            dataset_rows.extend(diagnostic_rows)
            metrics_by_method[method] = _hit_metrics(diagnostic_rows)
            error_counts[method] = {
                "error_by_hs2": dict(Counter(row["hs2_ref"] for row in diagnostic_rows if not int(row["nandina8_at_100"]))),
                "error_by_hs4": dict(Counter(row["hs4_ref"] for row in diagnostic_rows if not int(row["nandina8_at_100"]))),
                "cases_hs2_present_nandina8_absent_at_100": [
                    row["case_id"] for row in diagnostic_rows if int(row["hs2_present_nandina8_absent_at_100"])
                ],
                "cases_hs4_present_nandina8_absent_at_100": [
                    row["case_id"] for row in diagnostic_rows if int(row["hs4_present_nandina8_absent_at_100"])
                ],
                "cases_hs2_absent_at_100": [
                    row["case_id"] for row in diagnostic_rows if int(row["hs2_absent_at_100"])
                ],
            }
        output_payload[dataset] = {
            "cases_total": len(rows),
            "methods": list(hits_by_dataset[dataset].keys()),
            "metrics_by_method": metrics_by_method,
            "error_counts": error_counts,
        }
        if dataset == "evalset":
            evalset_all_rows = dataset_rows
        _write_json(output_dir / f"{dataset}_ceiling.json", output_payload[dataset])

    output_payload["elapsed_seconds"] = time.time() - start
    hs2_rows = _family_error(evalset_all_rows, "hs2_ref")
    hs4_rows = _family_error(evalset_all_rows, "hs4_ref")
    _write_csv(
        output_dir / "evalset_error_by_hs2.csv",
        hs2_rows,
        ["method", "hs2_ref", "cases_total", "nandina8_miss_at_100", "hs2_miss_at_100", "hs4_miss_at_100", "hs6_miss_at_100", "nandina8_at_100", "hs2_at_100", "hs4_at_100", "hs6_at_100"],
    )
    _write_csv(
        output_dir / "evalset_error_by_hs4.csv",
        hs4_rows,
        ["method", "hs4_ref", "cases_total", "nandina8_miss_at_100", "hs2_miss_at_100", "hs4_miss_at_100", "hs6_miss_at_100", "nandina8_at_100", "hs2_at_100", "hs4_at_100", "hs6_at_100"],
    )
    ensure_parent(output_dir / "ceiling_summary.md")
    (output_dir / "ceiling_summary.md").write_text(_summary_markdown(output_payload), encoding="utf-8")
    return output_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Diagnose hierarchical retrieval ceiling on devset and evalset.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--phase7a-devset-pool", type=Path, default=DEFAULT_PHASE7A_DEVSET_POOL)
    parser.add_argument("--phase7a-evalset-pool", type=Path, default=DEFAULT_PHASE7A_EVALSET_POOL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser


def main() -> int:
    payload = diagnose(build_parser().parse_args())
    print("OK: diagnostico de techo jerarquico completado")
    for dataset in ["devset", "evalset"]:
        for method, metrics in payload[dataset]["metrics_by_method"].items():
            print(
                f"{dataset} {method}: "
                f"NANDINA8@100={metrics['nandina8_at_100']:.4f} "
                f"HS4@100={metrics['hs4_at_100']:.4f} "
                f"HS2@100={metrics['hs2_at_100']:.4f}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
