from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import statistics
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def code8(value: object) -> str:
    return "".join(char for char in clean(value) if char.isdigit())[:8]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{clean(key): clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def assert_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256(path)
    if actual != expected:
        raise ValueError(f"{label} SHA-256 mismatch: {actual} != {expected}")


def append_unique(target: list[dict[str, Any]], seen: set[str], candidates: Iterable[str], source: str, stats: dict[str, int]) -> None:
    for candidate in candidates:
        code = code8(candidate)
        if not code:
            continue
        stats["attempted"] += 1
        if code in seen:
            stats["duplicates_discarded"] += 1
            for item in target:
                if item["code"] == code and source not in item["sources"]:
                    item["sources"].append(source)
            continue
        seen.add(code)
        target.append({"code": code, "sources": [source]})


def protected_dual(precision: list[str], recall: list[str], depth: int, protected: int) -> tuple[list[dict[str, Any]], dict[str, int]]:
    out: list[dict[str, Any]] = []
    stats = {"attempted": 0, "duplicates_discarded": 0}
    seen: set[str] = set()
    append_unique(out, seen, precision[:protected], "dual_precision", stats)
    append_unique(out, seen, recall, "dual_recall", stats)
    append_unique(out, seen, precision[protected:], "dual_precision", stats)
    return out[:depth], stats


def build_pool(
    hierarchical: list[str], dual: list[str], depth: int, config: Mapping[str, Any]
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    out: list[dict[str, Any]] = []
    stats = {"attempted": 0, "duplicates_discarded": 0}
    seen: set[str] = set()
    if config["kind"] == "single_source":
        append_unique(out, seen, hierarchical if config["source"] == "hierarchical" else dual, config["source"], stats)
        return out[:depth], stats

    first_block = min(100, depth)
    hierarchical_slots = min(int(config["hierarchical_slots_in_first_100"]), first_block)
    dual_slots = first_block - hierarchical_slots
    append_unique(out, seen, hierarchical[:hierarchical_slots], "hierarchical", stats)
    append_unique(out, seen, dual[:dual_slots], "dual", stats)
    if len(out) < first_block:
        append_unique(out, seen, hierarchical[hierarchical_slots:], "hierarchical", stats)
        append_unique(out, seen, dual[dual_slots:], "dual", stats)
    if depth > 100:
        append_unique(out, seen, dual[dual_slots:], "dual", stats)
        append_unique(out, seen, hierarchical[hierarchical_slots:], "hierarchical", stats)
    return out[:depth], stats


def build_union(hierarchical: list[str], dual: list[str], depth: int) -> tuple[list[dict[str, Any]], dict[str, int]]:
    out: list[dict[str, Any]] = []
    stats = {"attempted": 0, "duplicates_discarded": 0}
    seen: set[str] = set()
    append_unique(out, seen, hierarchical[:depth], "hierarchical", stats)
    append_unique(out, seen, dual[:depth], "dual", stats)
    return out, stats


def hit_flags(codes: list[str], reference: str) -> dict[str, int]:
    return {
        "exact": int(reference in codes),
        "hs6": int(any(code[:6] == reference[:6] for code in codes)),
        "hs4": int(any(code[:4] == reference[:4] for code in codes)),
        "chapter": int(any(code[:2] == reference[:2] for code in codes)),
    }


def ranking_from_results(rows: list[dict[str, str]], expected_cases: set[str]) -> dict[str, list[str]]:
    grouped: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for row in rows:
        case_id = clean(row["case_id"])
        grouped[case_id].append((int(row["candidate_rank"]), code8(row["candidate_code"])))
    if set(grouped) != expected_cases:
        raise ValueError("Hierarchical result case IDs do not match evalset")
    rankings: dict[str, list[str]] = {}
    for case_id, hits in grouped.items():
        codes = [code for _, code in sorted(hits) if code]
        if len(codes) != len(set(codes)):
            raise ValueError(f"Hierarchical source has repeated effective codes: {case_id}")
        rankings[case_id] = codes
    return rankings


def metric_row(pool_id: str, classification: str, depth: int, cases: list[dict[str, Any]]) -> dict[str, Any]:
    counts = [int(row["effective_size"]) for row in cases]
    result: dict[str, Any] = {
        "pool_id": pool_id,
        "classification": classification,
        "depth": depth,
        "cases": len(cases),
        "nominal_size": depth,
        "effective_size_mean": sum(counts) / len(counts),
        "effective_size_min": min(counts),
        "effective_size_max": max(counts),
        "effective_size_median": statistics.median(counts),
    }
    for family in ("exact", "hs6", "hs4", "chapter"):
        numerator = sum(int(row[f"{family}_at_depth"]) for row in cases)
        result[f"{family}_numerator"] = numerator
        result[f"{family}_denominator"] = len(cases)
        result[f"{family}_at_depth"] = numerator / len(cases)
    return result


def source_metrics(case_rows: list[dict[str, Any]], field: str, depth: int) -> dict[str, Any]:
    ranks = [int(row[field]) for row in case_rows]
    return {
        "top_1": sum(0 < rank <= 1 for rank in ranks) / len(ranks),
        "top_3": sum(0 < rank <= 3 for rank in ranks) / len(ranks),
        "top_5": sum(0 < rank <= 5 for rank in ranks) / len(ranks),
        "top_10": sum(0 < rank <= 10 for rank in ranks) / len(ranks),
        "top_50": sum(0 < rank <= 50 for rank in ranks) / len(ranks),
        "recall_at_100": sum(0 < rank <= 100 for rank in ranks) / len(ranks),
        "mrr_at_100": sum((1 / rank) for rank in ranks if 0 < rank <= 100) / len(ranks),
        "recall_at_200": sum(0 < rank <= 200 for rank in ranks) / len(ranks),
        "mrr_at_200": sum((1 / rank) for rank in ranks if 0 < rank <= 200) / len(ranks),
        "not_found_at_depth": sum(rank <= 0 or rank > depth for rank in ranks),
    }


def git_value(root: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}", *args], cwd=root, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def main() -> int:
    parser = argparse.ArgumentParser(description="EXP-04 Fase E normative candidate pools from frozen v0.2 inputs.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/normative_candidate_pools_v0.2.json"))
    args = parser.parse_args()
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    output_dir = resolve_project_path(config["outputs"]["directory"])
    if output_dir.exists():
        raise FileExistsError(f"Refusing to overwrite Fase E output: {output_dir}")

    eval_cfg = config["eval"]
    eval_path = resolve_project_path(eval_cfg["path"])
    assert_hash(eval_path, eval_cfg["sha256"], "evalset")
    eval_rows = read_csv(eval_path)
    if len(eval_rows) != int(eval_cfg["cases"]):
        raise ValueError("Unexpected evalset row count")
    case_ids = [clean(row["case_id"]) for row in eval_rows]
    if len(case_ids) != len(set(case_ids)) or not all(case_id.startswith("DA-EVAL-V02-") for case_id in case_ids):
        raise ValueError("Invalid evalset case IDs")
    expected_cases = set(case_ids)
    references = {clean(row["case_id"]): code8(row[eval_cfg["label_column"]]) for row in eval_rows}
    queries = {clean(row["case_id"]): clean(row[eval_cfg["query_column"]]) for row in eval_rows}
    if any(not reference or not query for reference, query in zip(references.values(), queries.values())):
        raise ValueError("Empty reference or query")

    frozen = config["frozen_input_rankings"]
    hist_cases = read_csv(resolve_project_path(frozen["historical"]["path"]))
    assert_hash(resolve_project_path(frozen["historical"]["path"]), frozen["historical"]["sha256"], "historical case summary")
    flat_summary_path = resolve_project_path(frozen["flat"]["case_summary"])
    flat_results_path = resolve_project_path(frozen["flat"]["results"])
    hier_summary_path = resolve_project_path(frozen["hierarchical"]["case_summary"])
    hier_results_path = resolve_project_path(frozen["hierarchical"]["results"])
    d1_summary_path = resolve_project_path(frozen["d1a"]["case_summary"])
    d1_trace_path = resolve_project_path(frozen["d1a"]["ranking_trace"])
    for path, expected, label in [
        (flat_summary_path, frozen["flat"]["case_summary_sha256"], "flat case summary"),
        (flat_results_path, frozen["flat"]["results_sha256"], "flat results"),
        (hier_summary_path, frozen["hierarchical"]["case_summary_sha256"], "hierarchical case summary"),
        (hier_results_path, frozen["hierarchical"]["results_sha256"], "hierarchical results"),
        (d1_summary_path, frozen["d1a"]["case_summary_sha256"], "D1a case summary"),
        (d1_trace_path, frozen["d1a"]["ranking_trace_sha256"], "D1a trace"),
    ]:
        assert_hash(path, expected, label)

    flat_cases = read_csv(flat_summary_path)
    hier_cases = read_csv(hier_summary_path)
    d1_cases = read_csv(d1_summary_path)
    for name, rows, label in [
        ("historical", hist_cases, "expected_nandina"),
        ("flat", flat_cases, "nandina_ref"),
        ("hierarchical", hier_cases, "nandina_ref"),
        ("d1a", d1_cases, "nandina_ref"),
    ]:
        by_case = {clean(row["case_id"]): code8(row[label]) for row in rows}
        if set(by_case) != expected_cases or by_case != references:
            raise ValueError(f"{name} is incompatible with the frozen evalset")

    hierarchical_rankings = ranking_from_results(read_csv(hier_results_path), expected_cases)
    dual_cfg = config["dual_protected"]
    precision_path = resolve_project_path(dual_cfg["precision_index"]["path"])
    recall_path = resolve_project_path(dual_cfg["recall_index"]["path"])
    assert_hash(precision_path, dual_cfg["precision_index"]["sha256"], "dual precision index")
    assert_hash(recall_path, dual_cfg["recall_index"]["sha256"], "dual recall index")
    precision_index = load_bm25_index(precision_path)
    recall_index = load_bm25_index(recall_path)
    max_depth = max(int(value) for value in config["depths"])
    dual_rankings: dict[str, list[str]] = {}
    dual_detail: dict[str, dict[str, int]] = {}
    for case_id in case_ids:
        precision = [code8(hit["code"]) for hit in retrieve(precision_index, queries[case_id], top_n=max_depth)]
        recall = [code8(hit["code"]) for hit in retrieve(recall_index, queries[case_id], top_n=max_depth)]
        dual_items, stats = protected_dual(precision, recall, max_depth, int(dual_cfg["protected_precision_top_n"]))
        dual_rankings[case_id] = [item["code"] for item in dual_items]
        dual_detail[case_id] = stats

    output_dir.mkdir(parents=True)
    depths = [int(value) for value in config["depths"]]
    case_summary: list[dict[str, Any]] = []
    result_rows: list[dict[str, Any]] = []
    all_metrics: list[dict[str, Any]] = []
    candidate_by_key: dict[tuple[str, int, str], list[dict[str, Any]]] = {}
    for pool_id, pool_cfg in config["candidate_pool_variants"].items():
        for depth in depths:
            rows_for_metric: list[dict[str, Any]] = []
            for case_id in case_ids:
                items, stats = build_pool(hierarchical_rankings[case_id], dual_rankings[case_id], depth, pool_cfg)
                codes = [item["code"] for item in items]
                if len(codes) != len(set(codes)):
                    raise ValueError(f"Pool contains duplicate codes: {pool_id}/{case_id}/{depth}")
                flags = hit_flags(codes, references[case_id])
                row = {"pool_id": pool_id, "classification": "candidate_pool", "case_id": case_id, "nandina_ref": references[case_id], "depth": depth, "effective_size": len(codes), "duplicates_discarded": stats["duplicates_discarded"], **{f"{key}_at_depth": value for key, value in flags.items()}}
                case_summary.append(row)
                rows_for_metric.append(row)
                candidate_by_key[(pool_id, depth, case_id)] = items
                result_rows.append({"pool_id": pool_id, "classification": "candidate_pool", "case_id": case_id, "nandina_ref": references[case_id], "depth": depth, "candidate_codes": "|".join(codes), "effective_size": len(codes)})
            all_metrics.append(metric_row(pool_id, "candidate_pool", depth, rows_for_metric))

    union_id = config["diagnostic_union"]["pool_id"]
    for depth in depths:
        rows_for_metric = []
        for case_id in case_ids:
            items, stats = build_union(hierarchical_rankings[case_id], dual_rankings[case_id], depth)
            codes = [item["code"] for item in items]
            flags = hit_flags(codes, references[case_id])
            row = {"pool_id": union_id, "classification": "diagnostic_union", "case_id": case_id, "nandina_ref": references[case_id], "depth": depth, "effective_size": len(codes), "duplicates_discarded": stats["duplicates_discarded"], **{f"{key}_at_depth": value for key, value in flags.items()}}
            case_summary.append(row)
            rows_for_metric.append(row)
            candidate_by_key[(union_id, depth, case_id)] = items
            result_rows.append({"pool_id": union_id, "classification": "diagnostic_union", "case_id": case_id, "nandina_ref": references[case_id], "depth": depth, "candidate_codes": "|".join(codes), "effective_size": len(codes)})
        all_metrics.append(metric_row(union_id, "diagnostic_union", depth, rows_for_metric))

    overlap_rows: list[dict[str, Any]] = []
    complementarity: dict[str, Any] = {"pair": "hierarchical_vs_dual", "depths": {}}
    for depth in depths:
        both = only_hierarchical = only_dual = neither = 0
        for case_id in case_ids:
            reference = references[case_id]
            h = reference in hierarchical_rankings[case_id][:depth]
            d = reference in dual_rankings[case_id][:depth]
            both += int(h and d)
            only_hierarchical += int(h and not d)
            only_dual += int(d and not h)
            neither += int(not h and not d)
        row = {"strategy_a": "hierarchical", "strategy_b": "dual_protected", "depth": depth, "both": both, "only_a": only_hierarchical, "only_b": only_dual, "neither": neither, "cases": len(case_ids)}
        overlap_rows.append(row)
        complementarity["depths"][str(depth)] = row

    backfill: dict[str, Any] = {"base": "hierarchical", "variants": {}}
    for pool_id, pool_cfg in config["candidate_pool_variants"].items():
        if pool_cfg["kind"] != "hybrid":
            continue
        values: dict[str, Any] = {}
        for depth in depths:
            base = added = lost = duplicate_discarded = 0
            dual_added_counts: list[int] = []
            for case_id in case_ids:
                reference = references[case_id]
                h = reference in hierarchical_rankings[case_id][:depth]
                items = candidate_by_key[(pool_id, depth, case_id)]
                codes = [item["code"] for item in items]
                final = reference in codes
                base += int(h)
                added += int(final and not h)
                lost += int(h and not final)
                dual_added_counts.append(sum("dual" in item["sources"] and "hierarchical" not in item["sources"] for item in items))
                duplicate_discarded += next(row["duplicates_discarded"] for row in case_summary if row["pool_id"] == pool_id and row["depth"] == depth and row["case_id"] == case_id)
            values[str(depth)] = {"hierarchical_covered_cases": base, "new_cases_from_backfill": added, "lost_vs_hierarchical": lost, "absolute_gain": added, "relative_gain_vs_hierarchical": added / base if base else None, "average_dual_only_candidates_added": sum(dual_added_counts) / len(dual_added_counts), "duplicates_discarded": duplicate_discarded}
        backfill["variants"][pool_id] = values

    hist_by_case = {clean(row["case_id"]): row for row in hist_cases}
    flat_by_case = {clean(row["case_id"]): row for row in flat_cases}
    d1_by_case = {clean(row["case_id"]): row for row in d1_cases}
    unrecovered: list[dict[str, Any]] = []
    for case_id in case_ids:
        reference = references[case_id]
        flat = 0 < int(flat_by_case[case_id]["rank_ref"]) <= 100
        hierarchical = reference in hierarchical_rankings[case_id][:200]
        dual = reference in dual_rankings[case_id][:200]
        dense = 0 < int(d1_by_case[case_id]["rank_ref"]) <= 200
        pool = reference in [item["code"] for item in candidate_by_key[(union_id, 200, case_id)]]
        if not pool:
            historical = hist_by_case[case_id]
            unrecovered.append({"case_id": case_id, "reference_nandina": reference, "hs6": reference[:6], "hs4": reference[:4], "chapter": reference[:2], "reference_code_in_normative_corpus": True, "flat_recovered_at_100": flat, "hierarchical_recovered_at_200": hierarchical, "dual_recovered_at_200": dual, "d1a_recovered_at_200": dense, "pool_recovered_at_200": pool, "exact_duplicate_historical_flag": historical["exact_duplicate_cross_split"], "near_duplicate_historical_flag": historical["near_duplicate_095"]})

    dual_case_rows = []
    for case_id in case_ids:
        reference = references[case_id]
        rank = next((index for index, code in enumerate(dual_rankings[case_id], 1) if code == reference), 0)
        dual_case_rows.append({"case_id": case_id, "rank": rank})
    dual_metrics = source_metrics(dual_case_rows, "rank", max_depth)
    historical_metrics = json.loads((resolve_project_path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json")).read_text(encoding="utf-8"))["metrics"]
    flat_metrics = json.loads((resolve_project_path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json")).read_text(encoding="utf-8"))["metrics"]
    hierarchical_metrics = json.loads((resolve_project_path("outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json")).read_text(encoding="utf-8"))["metrics"]
    d1_metrics = json.loads((resolve_project_path("outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json")).read_text(encoding="utf-8"))["metrics"]
    ranking_comparison = [
        {"strategy": "Historical BM25", "classification": "ranking", "top_1": historical_metrics["top_1"], "top_3": historical_metrics["top_3"], "top_5": historical_metrics["top_5"], "top_10": historical_metrics["top_10"], "top_50": historical_metrics["top_50"], "recall_at_100": historical_metrics["recall_at_100"], "mrr_at_100": historical_metrics["mrr"]},
        {"strategy": "Normative BM25 flat", "classification": "ranking", "top_1": flat_metrics["top_1"], "top_3": flat_metrics["top_3"], "top_5": flat_metrics["top_5"], "top_10": flat_metrics["top_10"], "top_50": flat_metrics["top_50"], "recall_at_100": flat_metrics["recall_at_100"], "mrr_at_100": flat_metrics["mrr"]},
        {"strategy": "Normative BM25 hierarchical", "classification": "ranking", "top_1": hierarchical_metrics["top_1"], "top_3": hierarchical_metrics["top_3"], "top_5": hierarchical_metrics["top_5"], "top_10": hierarchical_metrics["top_10"], "top_50": hierarchical_metrics["top_50"], "recall_at_100": hierarchical_metrics["recall_at_100"], "mrr_at_100": hierarchical_metrics["mrr_at_100"]},
        {"strategy": "D1a Text2Trade-inspired MNRL", "classification": "ranking", "top_1": d1_metrics["top_1"], "top_3": d1_metrics["top_3"], "top_5": d1_metrics["top_5"], "top_10": d1_metrics["top_10"], "top_50": d1_metrics["top_50"], "recall_at_100": d1_metrics["recall_at_100"], "mrr_at_100": d1_metrics["mrr_at_100"]},
        {"strategy": "Dual protected historical", "classification": "ranking", **{key: dual_metrics[key] for key in ("top_1", "top_3", "top_5", "top_10", "top_50", "recall_at_100", "mrr_at_100")}},
    ]
    pool_comparison = [{"pool_id": row["pool_id"], "classification": row["classification"], "nominal_size": row["nominal_size"], "effective_size_mean": row["effective_size_mean"], "effective_size_min": row["effective_size_min"], "effective_size_max": row["effective_size_max"], "effective_size_median": row["effective_size_median"], "pool_recall": row["exact_at_depth"], "pool_recall_numerator": row["exact_numerator"], "pool_recall_denominator": row["exact_denominator"], "hs6_at_depth": row["hs6_at_depth"], "hs4_at_depth": row["hs4_at_depth"], "chapter_at_depth": row["chapter_at_depth"], "depth": row["depth"]} for row in all_metrics]
    compatibility = {"compatible": True, "eval_hash": eval_cfg["sha256"], "cases": len(case_ids), "strategies": {"historical": True, "flat": True, "hierarchical": True, "d1a": True, "dual": True, "phase_e": True}, "identical_case_id_sets": True, "identical_labels": True, "d0_excluded_from_confirmatory_comparison": True}

    outputs = {
        "candidate_pool_results": output_dir / "candidate_pool_results.csv",
        "candidate_pool_case_summary": output_dir / "candidate_pool_case_summary.csv",
        "candidate_pool_metrics": output_dir / "candidate_pool_metrics.json",
        "candidate_pool_overlap": output_dir / "candidate_pool_overlap.csv",
        "candidate_pool_complementarity": output_dir / "candidate_pool_complementarity.json",
        "candidate_pool_backfill_analysis": output_dir / "candidate_pool_backfill_analysis.json",
        "candidate_pool_coverage_ceiling": output_dir / "candidate_pool_coverage_ceiling.json",
        "candidate_pool_unrecovered_cases": output_dir / "candidate_pool_unrecovered_cases.csv",
        "candidate_pool_strategy_comparison": output_dir / "candidate_pool_strategy_comparison.csv",
        "candidate_pool_compatibility": output_dir / "candidate_pool_compatibility.json",
        "candidate_pool_run_metadata": output_dir / "candidate_pool_run_metadata.json",
        "summary": output_dir / "summary.md",
    }
    write_csv(outputs["candidate_pool_results"], result_rows, ["pool_id", "classification", "case_id", "nandina_ref", "depth", "candidate_codes", "effective_size"])
    write_csv(outputs["candidate_pool_case_summary"], case_summary, ["pool_id", "classification", "case_id", "nandina_ref", "depth", "effective_size", "duplicates_discarded", "exact_at_depth", "hs6_at_depth", "hs4_at_depth", "chapter_at_depth"])
    write_json(outputs["candidate_pool_metrics"], {"experiment_id": config["experiment_id"], "phase": config["phase"], "metrics": all_metrics, "no_mrr_for_candidate_pools": True, "diagnostic_union_not_a_ranking": True})
    write_csv(outputs["candidate_pool_overlap"], overlap_rows, ["strategy_a", "strategy_b", "depth", "both", "only_a", "only_b", "neither", "cases"])
    write_json(outputs["candidate_pool_complementarity"], complementarity)
    write_json(outputs["candidate_pool_backfill_analysis"], backfill)
    ceiling = {"label": config["diagnostic_union"]["label"], "not_a_ranking": True, "depths": {str(row["depth"]): row for row in all_metrics if row["pool_id"] == union_id}, "uncovered_at_200": len(unrecovered), "exclusive_source_distribution": {str(depth): {"hierarchical_only": row["only_a"], "dual_only": row["only_b"], "both": row["both"], "neither": row["neither"]} for depth, row in complementarity["depths"].items()}}
    write_json(outputs["candidate_pool_coverage_ceiling"], ceiling)
    write_csv(outputs["candidate_pool_unrecovered_cases"], unrecovered, ["case_id", "reference_nandina", "hs6", "hs4", "chapter", "reference_code_in_normative_corpus", "flat_recovered_at_100", "hierarchical_recovered_at_200", "dual_recovered_at_200", "d1a_recovered_at_200", "pool_recovered_at_200", "exact_duplicate_historical_flag", "near_duplicate_historical_flag"])
    write_csv(outputs["candidate_pool_strategy_comparison"], ranking_comparison + pool_comparison, ["strategy", "pool_id", "classification", "depth", "top_1", "top_3", "top_5", "top_10", "top_50", "recall_at_100", "mrr_at_100", "nominal_size", "effective_size_mean", "effective_size_min", "effective_size_max", "effective_size_median", "pool_recall", "pool_recall_numerator", "pool_recall_denominator", "hs6_at_depth", "hs4_at_depth", "chapter_at_depth"])
    write_json(outputs["candidate_pool_compatibility"], compatibility)

    lines = ["# EXP-04 Fase E: candidate pools normativos v0.2", "", "- La unión diagnóstica no es ranking y no reporta MRR.", "- D0 excluido: INVALID AS FINAL COMPARATOR - LEGACY VECTOR INDEX NOT REPRODUCIBLE.", "", "## PoolRecall", "", "| Pool | Tipo | N | Exact | HS6 | HS4 | Chapter |", "|---|---|---:|---:|---:|---:|---:|"]
    for row in all_metrics:
        lines.append(f"| {row['pool_id']} | {row['classification']} | {row['depth']} | {row['exact_numerator']}/{row['exact_denominator']} ({row['exact_at_depth']:.12f}) | {row['hs6_at_depth']:.12f} | {row['hs4_at_depth']:.12f} | {row['chapter_at_depth']:.12f} |")
    lines.extend(["", "## HE2", "", "- HE2-A ranking temprano: se determina desde la tabla de rankings sin convertir pools en rankings.", "- HE2-B cobertura profunda: se determina desde PoolRecall y la unión diagnóstica a 100/200, sin selección posterior de variantes.", ""])
    outputs["summary"].write_text("\n".join(lines), encoding="utf-8", newline="\n")
    large_outputs = [{"name": name, "path": relative(path, root), "bytes": path.stat().st_size} for name, path in outputs.items() if name != "candidate_pool_run_metadata" and path.stat().st_size > 25 * 1024 * 1024]
    too_large = [item for item in large_outputs if item["bytes"] > 50 * 1024 * 1024]
    if too_large:
        raise ValueError(f"Outputs exceed the 50 MB commit guard: {too_large}")
    metadata = {"experiment_id": config["experiment_id"], "phase": config["phase"], "dataset_version": config["dataset_version"], "created_at_utc": datetime.now(timezone.utc).isoformat(), "command": "python -B -m src.experiments.evaluate_normative_candidate_pools_data_aduanas_v02", "config": {"path": relative(config_path, root), "sha256": sha256(config_path)}, "eval": eval_cfg, "input_hashes": {"hierarchical_results": sha256(hier_results_path), "flat_results": sha256(flat_results_path), "historical_case_summary": sha256(resolve_project_path(frozen["historical"]["path"])), "d1a_trace": sha256(d1_trace_path), "dual_precision_index": sha256(precision_path), "dual_recall_index": sha256(recall_path)}, "dual_definition": dual_cfg, "candidate_pool_variants": config["candidate_pool_variants"], "diagnostic_union": config["diagnostic_union"], "exclusions": config["exclusions"], "compatibility": compatibility, "runtime": {"python": sys.version, "platform": platform.platform()}, "git": {"branch": git_value(root, "rev-parse", "--abbrev-ref", "HEAD"), "commit": git_value(root, "rev-parse", "HEAD")}, "outputs": {name: relative(path, root) for name, path in outputs.items()}, "large_outputs_over_25_mb": large_outputs, "output_sha256_excludes_self_referential_metadata": True}
    metadata["output_sha256"] = {name: sha256(path) for name, path in outputs.items() if name != "candidate_pool_run_metadata"}
    write_json(outputs["candidate_pool_run_metadata"], metadata)
    print(f"OK: Fase E candidate pools completed at {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
