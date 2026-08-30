from __future__ import annotations

import argparse
import csv
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

from ..retrieval.text2trade_mnrl_v02 import clean, load_json, normalize_code, read_csv, relative, sha256_file, write_csv, write_json
from ..utils.paths import project_root, resolve_project_path


K_VALUES = (1, 3, 5, 10, 50)
DEPTH = 200


def assert_hash(path: Path, expected: str) -> None:
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"Frozen input hash mismatch for {path}: {actual} != {expected}")


def hit(rank: int, k: int) -> int:
    return int(1 <= rank <= k)


def hierarchical(codes: list[str], reference: str, length: int, k: int) -> int:
    return int(any(code[:length] == reference[:length] for code in codes[:k]))


def baseline_values(root: Path) -> list[dict[str, Any]]:
    sources = {
        "Historical BM25": root / "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json",
        "Normative BM25 flat": root / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json",
        "Normative BM25 hierarchical": root / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json",
        "D0 pretrained dense SBERT baseline": root / "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json",
    }
    fields = ("Top-1", "Top-3", "Top-5", "Top-10", "Top-50", "Recall@100", "MRR@100", "Recall@200", "MRR@200")
    keys = {
        "Historical BM25": {"Top-1": "exact_at_1", "Top-3": "exact_at_3", "Top-5": "exact_at_5", "Top-10": "exact_at_10", "Top-50": "exact_at_50", "MRR@100": "mrr"},
        "Normative BM25 flat": {"Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10", "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr"},
        "Normative BM25 hierarchical": {"Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10", "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr", "Recall@200": "recall_at_200", "MRR@200": "mrr_at_200"},
        "D0 pretrained dense SBERT baseline": {"Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10", "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr_at_100", "Recall@200": "recall_at_200", "MRR@200": "mrr_at_200"},
    }
    rows = []
    for name, path in sources.items():
        payload = load_json(path)
        metrics = payload.get("metrics", payload)
        for label in fields:
            key = keys[name].get(label)
            rows.append({"strategy": name, "metric": label, "value": metrics.get(key) if key else None, "source": relative(path, root)})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate D1a MNRL on frozen data_aduanas evalset v0.2 after vector integrity passes.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/text2trade_mnrl_v0.2.json"))
    parser.add_argument("--refresh-comparison-only", action="store_true")
    args = parser.parse_args()
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    frozen = config["frozen_inputs"]
    columns = config["columns"]
    eval_path = resolve_project_path(frozen["eval_csv"])
    index_dir = resolve_project_path(config["index"]["output_dir"])
    model_dir = resolve_project_path(config["outputs"]["model_dir"])
    output_dir = resolve_project_path(config["outputs"]["evaluation_dir"])
    if args.refresh_comparison_only:
        payload = load_json(output_dir / "d1a_metrics.json")
        comparison = baseline_values(root)
        d1_fields = {"Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10", "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr_at_100", "Recall@200": "recall_at_200", "MRR@200": "mrr_at_200"}
        comparison.extend({"strategy": "D1a Text2Trade-inspired MNRL", "metric": label, "value": payload["metrics"][key], "source": "D1a"} for label, key in d1_fields.items())
        write_csv(output_dir / "strategy_comparison_a_b_c_d0_d1a_v0.2.csv", comparison, ["strategy", "metric", "value", "source"])
        print("OK: D1a comparison refreshed from existing metrics only")
        return 0
    if output_dir.exists():
        raise FileExistsError(f"Refusing to overwrite D1a evaluation output: {output_dir}")
    assert_hash(eval_path, frozen["eval_sha256"])
    index_metadata = load_json(index_dir / "text2trade_mnrl_nandina8_v02_run_metadata.json")
    integrity = load_json(index_dir / "vector_integrity_gate_v0.2.json")
    if integrity["status"] != "PASS" or not index_metadata["validation"]["vector_integrity_pass"]:
        raise RuntimeError("D1a vector integrity gate did not pass; evaluation is forbidden")

    eval_rows = read_csv(eval_path)
    if len(eval_rows) != 1056 or len({clean(row["case_id"]) for row in eval_rows}) != 1056:
        raise ValueError("Expected 1056 unique v0.2 eval cases")
    docstore = [json.loads(line) for line in (index_dir / "store/nandina8_docstore.jsonl").read_text(encoding="utf-8").splitlines() if line]
    id_map = load_json(index_dir / "index/id_map.json")
    vectors = np.load(index_dir / "index/vectors.npy", mmap_mode="r")
    if vectors.shape[0] != len(docstore) or len(id_map) != len(docstore):
        raise ValueError("D1a index cardinality mismatch")
    model = SentenceTransformer(str(model_dir), device=config["training"]["device"])
    model.max_seq_length = int(config["training"]["max_sequence_length"])
    queries = [clean(row[columns["query"]]) for row in eval_rows]
    query_vectors = model.encode(queries, batch_size=32, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=True).astype(np.float32)
    corpus_codes = {clean(doc["codigo"]) for doc in docstore}
    if not all(normalize_code(row[columns["label"]]) in corpus_codes for row in eval_rows):
        raise ValueError("Evaluation reference code absent from D1a corpus")

    output_dir.mkdir(parents=True)
    case_rows: list[dict[str, Any]] = []
    trace_path = output_dir / "d1a_ranked_codes_top200.jsonl"
    with trace_path.open("w", encoding="utf-8", newline="\n") as trace:
        for eval_row, query_vector in zip(eval_rows, query_vectors):
            scores = np.asarray(vectors @ query_vector, dtype=np.float32)
            top_indices = np.argpartition(-scores, kth=DEPTH - 1)[:DEPTH]
            top_indices = top_indices[np.argsort(-scores[top_indices])]
            codes = [clean(id_map[str(int(index))]["codigo"]) for index in top_indices]
            reference = normalize_code(eval_row[columns["label"]])
            rank = next((position for position, code in enumerate(codes, start=1) if code == reference), 0)
            row = {
                "case_id": clean(eval_row["case_id"]),
                "id_unico": clean(eval_row[columns["id"]]),
                "nandina_ref": reference,
                "rank_ref": rank,
                "retrieved_count": len(codes),
                "top1_code": codes[0],
                "top1_score": float(scores[int(top_indices[0])]),
            }
            for k in K_VALUES:
                row[f"hit_top_{k}"] = hit(rank, k)
            for k in (100, 200):
                row[f"hit_recall_{k}"] = hit(rank, k)
                row[f"mrr_at_{k}_contribution"] = 1.0 / rank if hit(rank, k) else 0.0
                for name, length in (("exact", 8), ("hs6", 6), ("hs4", 4), ("chapter", 2)):
                    row[f"{name}_at_{k}"] = hit(rank, k) if name == "exact" else hierarchical(codes, reference, length, k)
            case_rows.append(row)
            trace.write(json.dumps({"case_id": row["case_id"], "nandina_ref": reference, "candidate_codes": codes}, ensure_ascii=False) + "\n")

    metrics: dict[str, Any] = {"cases_evaluated": len(case_rows), "cases_with_retrieval": len(case_rows), "zero_retrieval_cases": 0, "not_found_at_depth": sum(not row["rank_ref"] for row in case_rows)}
    for k in K_VALUES:
        numerator = sum(row[f"hit_top_{k}"] for row in case_rows)
        metrics.update({f"top_{k}_numerator": numerator, f"top_{k}_denominator": len(case_rows), f"top_{k}": numerator / len(case_rows)})
    for k in (100, 200):
        numerator = sum(row[f"hit_recall_{k}"] for row in case_rows)
        mrr_numerator = sum(row[f"mrr_at_{k}_contribution"] for row in case_rows)
        metrics.update({f"recall_at_{k}_numerator": numerator, f"recall_at_{k}_denominator": len(case_rows), f"recall_at_{k}": numerator / len(case_rows), f"mrr_at_{k}_numerator": mrr_numerator, f"mrr_at_{k}_denominator": len(case_rows), f"mrr_at_{k}": mrr_numerator / len(case_rows)})
        for name in ("exact", "hs6", "hs4", "chapter"):
            numerator = sum(row[f"{name}_at_{k}"] for row in case_rows)
            metrics.update({f"{name}_at_{k}_numerator": numerator, f"{name}_at_{k}_denominator": len(case_rows), f"{name}_at_{k}": numerator / len(case_rows)})

    comparison = baseline_values(root)
    d1_fields = {"Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10", "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr_at_100", "Recall@200": "recall_at_200", "MRR@200": "mrr_at_200"}
    comparison.extend({"strategy": "D1a Text2Trade-inspired MNRL", "metric": label, "value": metrics[key], "source": "D1a"} for label, key in d1_fields.items())
    case_path = output_dir / "d1a_case_summary.csv"
    metrics_path = output_dir / "d1a_metrics.json"
    comparison_path = output_dir / "strategy_comparison_a_b_c_d0_d1a_v0.2.csv"
    write_csv(case_path, case_rows, list(case_rows[0]))
    write_csv(comparison_path, comparison, ["strategy", "metric", "value", "source"])
    payload = {
        "experiment_id": config["experiment_id"],
        "variant": "D1a",
        "method": "Text2Trade-inspired MNRL dense retriever without MCD",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python -B -m src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02",
        "inputs": {"evalset": {"path": relative(eval_path, root), "sha256": sha256_file(eval_path), "cases": len(eval_rows)}, "index_metadata": {"path": relative(index_dir / "text2trade_mnrl_nandina8_v02_run_metadata.json", root), "sha256": sha256_file(index_dir / "text2trade_mnrl_nandina8_v02_run_metadata.json")}, "vector_integrity": integrity},
        "metrics": metrics,
        "validation": {"vector_integrity_passed_before_eval": True, "evalset_used_for_training_or_selection": False, "mcd_used": False, "candidate_pool_used": False, "phase_e_started": False, "ranking_codes_unique": all(len(set(json.loads(line)["candidate_codes"])) == DEPTH for line in trace_path.read_text(encoding="utf-8").splitlines())},
        "outputs": {"case_summary": relative(case_path, root), "ranking_trace": relative(trace_path, root), "comparison": relative(comparison_path, root)},
    }
    write_json(metrics_path, payload)
    (output_dir / "summary.md").write_text("# D1a Text2Trade-inspired MNRL v0.2\n\n" + "\n".join(f"- `{key}`: `{value}`" for key, value in metrics.items()) + "\n", encoding="utf-8", newline="\n")
    print("OK: D1a evaluated after vector integrity pass")
    print(f"Top-1: {metrics['top_1']}; Recall@100: {metrics['recall_at_100']}; MRR@100: {metrics['mrr_at_100']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
