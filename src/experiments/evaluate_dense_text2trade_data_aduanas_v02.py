from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import re
import subprocess
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from importlib import metadata as importlib_metadata
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

from sentence_transformers import SentenceTransformer

from ..retrieval.dense_text2trade import DenseText2TradeRetriever
from ..utils.paths import ensure_parent, project_root, resolve_project_path


EXPERIMENT_ID = "exp04_phase_d_text2trade_dense_v0.2"
METHOD = "text2trade_dense_data_aduanas_clase87_v0.2"
DATASET_VERSION = "v0.2"
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DEFAULT_ARTIFACT_DIR = Path("data/processed/indexes/text2trade_nandina8_v1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2")
QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
EXPECTED_SCOPE_CLASS = "87"
K_VALUES = [1, 3, 5, 10, 50]
RECALL_VALUES = [100, 200]
HIER_VALUES = [100, 200]
POSITION_BUCKETS = [
    "1",
    "2-3",
    "4-5",
    "6-10",
    "11-50",
    "51-100",
    "101-200",
    ">200_or_not_retrieved",
]
PREVIOUS_PHASE_OUTPUT_HASHES = {
    "historical_metrics": (
        "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/"
        "historical_metrics.json",
        "5334e64ab2b3f812f939b652fe1ee8ad8db24b673ebb48fd4d7b1ddb0dd444fa",
    ),
    "historical_case_summary": (
        "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/"
        "historical_case_summary.csv",
        "f8f4ac6d585194aace74c50f495720cc87b0c09a28438d888b0030dfaddd0d56",
    ),
    "flat_metrics": (
        "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/"
        "normative_metrics.json",
        "56a702398d3b9d1483ecd1be3ca79587682ad8fd3afd84858917f248b5ae0460",
    ),
    "flat_case_summary": (
        "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/"
        "normative_case_summary.csv",
        "f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0",
    ),
    "hierarchical_metrics": (
        "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/"
        "normative_hierarchical_metrics.json",
        "557c46668cfd51fbeabba0ecdb9bf3ca4a2a34a7f2850384252c5d963a26fd9f",
    ),
    "hierarchical_case_summary": (
        "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/"
        "normative_hierarchical_case_summary.csv",
        "17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634",
    ),
}
APPROVED_STRATEGY_VALUES = {
    "historical": {
        "Top-1": 0.509469696969697,
        "Top-3": 0.6714015151515151,
        "Top-5": 0.7632575757575758,
        "Top-10": 0.8910984848484849,
        "Top-50": 0.9914772727272727,
        "Recall@100": None,
        "MRR@100": 0.6297077493524843,
    },
    "flat": {
        "Top-1": 0.027462121212121212,
        "Top-3": 0.05113636363636364,
        "Top-5": 0.061553030303030304,
        "Top-10": 0.06534090909090909,
        "Top-50": 0.07007575757575757,
        "Recall@100": 0.07102272727272728,
        "MRR@100": 0.04229731726741296,
    },
    "hierarchical": {
        "Top-1": 0.026515151515151516,
        "Top-3": 0.052083333333333336,
        "Top-5": 0.0625,
        "Top-10": 0.06534090909090909,
        "Top-50": 0.09090909090909091,
        "Recall@100": 0.10132575757575757,
        "MRR@100": 0.04198129438896377,
    },
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
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def _normalize_code(value: object) -> str:
    return re.sub(r"\D", "", _clean(value))


def _package_version(name: str) -> str | None:
    try:
        return importlib_metadata.version(name)
    except importlib_metadata.PackageNotFoundError:
        return None


def _rank_bucket(rank: int) -> str:
    if rank == 1:
        return "1"
    if 2 <= rank <= 3:
        return "2-3"
    if 4 <= rank <= 5:
        return "4-5"
    if 6 <= rank <= 10:
        return "6-10"
    if 11 <= rank <= 50:
        return "11-50"
    if 51 <= rank <= 100:
        return "51-100"
    if 101 <= rank <= 200:
        return "101-200"
    return ">200_or_not_retrieved"


def _hit(rank: int, k: int) -> int:
    return int(1 <= rank <= k)


def _mrr_at(rank: int, k: int) -> float:
    return 1.0 / rank if 1 <= rank <= k else 0.0


def _hier_hit(codes: Sequence[str], ref: str, prefix_len: int, k: int) -> int:
    prefix = ref[:prefix_len]
    return int(any(code[:prefix_len] == prefix for code in codes[:k]))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _manifest_for_model(model_dir: Path, root: Path) -> dict[str, Any]:
    files = [
        "config_sentence_transformers.json",
        "config.json",
        "modules.json",
        "sentence_bert_config.json",
        "special_tokens_map.json",
        "tokenizer_config.json",
        "tokenizer.json",
        "unigram.json",
        "model.safetensors",
        "1_Pooling/config.json",
        "README.md",
    ]
    file_entries = []
    for rel_file in files:
        path = model_dir / rel_file
        if path.exists():
            file_entries.append(
                {
                    "path": _rel(path, root),
                    "size_bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )
    config_st = _load_json(model_dir / "config_sentence_transformers.json")
    pooling = _load_json(model_dir / "1_Pooling/config.json")
    tokenizer_cfg = _load_json(model_dir / "tokenizer_config.json")
    model_cfg = _load_json(model_dir / "config.json")
    return {
        "model_id": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "local_model_path": _rel(model_dir, root),
        "revision": None,
        "revision_status": "not recorded in local Text2Trade artifact metadata",
        "model_type": config_st.get("model_type"),
        "similarity_fn_name": config_st.get("similarity_fn_name"),
        "prompts": config_st.get("prompts"),
        "tokenizer_class": tokenizer_cfg.get("tokenizer_class"),
        "tokenizer_max_length": tokenizer_cfg.get("model_max_length"),
        "truncation_side": tokenizer_cfg.get("truncation_side"),
        "truncation_strategy": tokenizer_cfg.get("truncation_strategy"),
        "transformer_model_type": model_cfg.get("model_type"),
        "hidden_size": model_cfg.get("hidden_size"),
        "dtype": model_cfg.get("dtype"),
        "pooling": pooling,
        "files": file_entries,
    }


def _artifact_file_hashes(artifact_dir: Path, root: Path) -> dict[str, dict[str, Any]]:
    rel_files = [
        "retrieval_config.json",
        "text2trade_nandina8_run_metadata.json",
        "index/vectors.npy",
        "index/id_map.json",
        "store/nandina8_docstore.jsonl",
    ]
    payload = {}
    for rel_file in rel_files:
        path = artifact_dir / rel_file
        payload[rel_file] = {
            "path": _rel(path, root),
            "exists": path.exists(),
            "size_bytes": path.stat().st_size if path.exists() else None,
            "sha256": _sha256(path) if path.exists() else None,
        }
    return payload


def _compatibility_report(root: Path, output_dir: Path, text2trade_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    hist = _read_csv(root / "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv")
    flat = _read_csv(root / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv")
    hier = _read_csv(root / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv")

    def labels(rows: Sequence[Mapping[str, Any]]) -> dict[str, str]:
        result = {}
        for row in rows:
            for key in ("nandina_ref", "expected_nandina", "NANDINA", "label"):
                if key in row and _clean(row[key]):
                    result[_clean(row["case_id"])] = _clean(row[key])
                    break
        return result

    hist_ids = {_clean(row["case_id"]) for row in hist}
    flat_ids = {_clean(row["case_id"]) for row in flat}
    hier_ids = {_clean(row["case_id"]) for row in hier}
    t2t_ids = {_clean(row["case_id"]) for row in text2trade_rows}
    hist_labels = labels(hist)
    flat_labels = labels(flat)
    hier_labels = labels(hier)
    t2t_labels = labels(text2trade_rows)
    all_ids = hist_ids | flat_ids | hier_ids | t2t_ids
    identical_labels = all(
        hist_labels.get(case_id) == flat_labels.get(case_id) == hier_labels.get(case_id) == t2t_labels.get(case_id)
        for case_id in all_ids
    )
    report = {
        "artifact_id": "historical_flat_hierarchical_text2trade_compatibility_v0.2",
        "total_cases": len(text2trade_rows),
        "total_cases_historical": len(hist),
        "total_cases_flat": len(flat),
        "total_cases_hierarchical": len(hier),
        "total_cases_text2trade": len(text2trade_rows),
        "identical_historical_case_id_set": hist_ids == t2t_ids,
        "identical_flat_case_id_set": flat_ids == t2t_ids,
        "identical_hierarchical_case_id_set": hier_ids == t2t_ids,
        "identical_case_id_sets": hist_ids == flat_ids == hier_ids == t2t_ids,
        "identical_labels": identical_labels,
        "label_mismatch_count": 0
        if identical_labels
        else sum(
            1
            for case_id in all_ids
            if hist_labels.get(case_id)
            != flat_labels.get(case_id)
            or flat_labels.get(case_id) != hier_labels.get(case_id)
            or hier_labels.get(case_id) != t2t_labels.get(case_id)
        ),
        "eval_hash_historical": EXPECTED_EVAL_SHA256,
        "eval_hash_flat": EXPECTED_EVAL_SHA256,
        "eval_hash_hierarchical": EXPECTED_EVAL_SHA256,
        "eval_hash_text2trade": EXPECTED_EVAL_SHA256,
        "compatible": hist_ids == flat_ids == hier_ids == t2t_ids and identical_labels,
    }
    _write_json(output_dir / "historical_flat_hierarchical_text2trade_compatibility_v0.2.json", report)
    return report


def _previous_phase_hash_status(root: Path) -> dict[str, Any]:
    entries = {}
    ok = True
    for name, (rel_path, expected) in PREVIOUS_PHASE_OUTPUT_HASHES.items():
        path = root / rel_path
        actual = _sha256(path)
        matches = actual == expected
        ok = ok and matches
        entries[name] = {"path": rel_path, "expected_sha256": expected, "actual_sha256": actual, "matches": matches}
    return {"all_match_expected": ok, "entries": entries}


def _strategy_comparison(output_dir: Path, text_metrics: Mapping[str, Any]) -> list[dict[str, Any]]:
    t = text_metrics
    t_values = {
        "Top-1": t["top_1"],
        "Top-3": t["top_3"],
        "Top-5": t["top_5"],
        "Top-10": t["top_10"],
        "Top-50": t["top_50"],
        "Recall@100": t["recall_at_100"],
        "MRR@100": t["mrr_at_100"],
    }
    rows = []
    for metric in ["Top-1", "Top-3", "Top-5", "Top-10", "Top-50", "Recall@100", "MRR@100"]:
        rows.append(
            {
                "metric": metric,
                "historical": APPROVED_STRATEGY_VALUES["historical"][metric],
                "flat": APPROVED_STRATEGY_VALUES["flat"][metric],
                "hierarchical": APPROVED_STRATEGY_VALUES["hierarchical"][metric],
                "text2trade": t_values[metric],
            }
        )
    _write_csv(output_dir / "strategy_comparison_v0.2.csv", rows, ["metric", "historical", "flat", "hierarchical", "text2trade"])
    _write_json(output_dir / "strategy_comparison_v0.2.json", {"rows": rows, "note": "Descriptive only; HE2 remains open until candidate pools are completed."})
    return rows


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    corpus = payload["corpus"]
    position = payload["position_distribution"]
    lines = [
        "# EXP-04 Fase D - Text2Trade dense data_aduanas clase 87 v0.2",
        "",
        "## Alcance",
        "",
        "Se ejecuto exclusivamente Text2Trade / recuperacion densa sobre el evalset oficial v0.2. No se ejecutaron candidate pools, dual protegido, mezcla 70/30, union diagnostica, integracion historico-normativa, RAG, reranking LLM ni explicador LLM.",
        "",
        "## Identidad Text2Trade implementada",
        "",
        "- Adaptacion local: bi-encoder SentenceTransformer preentrenado sobre artefactos NANDINA-8 congelados.",
        "- Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.",
        "- Revision Hugging Face: no registrada en metadata local; se congela por hashes locales del modelo.",
        "- Pooling: mean tokens.",
        "- Normalizacion: embeddings normalizados.",
        "- Similarity metric: cosine via dot product on normalized vectors.",
        "- ANN: configuracion historica HNSW existe en metadata, pero `hnsw.index` no existe fisicamente; Fase D usa fuerza bruta sobre `vectors.npy`.",
        "- Monte Carlo Dropout: aparece en `retrieval_config.json`, pero no forma parte de esta comparacion ejecutada; se uso encoding determinista.",
        "",
        "## Corpus denso",
        "",
        f"- Corpus fuente: `{corpus['source_corpus_path']}`.",
        f"- Corpus SHA-256: `{corpus['source_corpus_sha256']}`.",
        f"- Docstore: `{corpus['docstore_path']}`.",
        f"- Docstore SHA-256: `{corpus['docstore_sha256']}`.",
        f"- Documentos indexados: {corpus['docstore_docs']}.",
        f"- Codigos NANDINA-8 unicos: {corpus['docstore_unique_codes']}.",
        f"- Codigos eval cubiertos: {corpus['eval_codes_present_exact_nandina8_in_corpus']}/{corpus['eval_unique_codes']}.",
        f"- Casos eval cubiertos: {corpus['eval_cases_present_exact_nandina8_in_corpus']}/{corpus['eval_cases']}.",
        "",
        "## Metricas exactas",
        "",
        "| Metrica | Numerador | Denominador | Valor |",
        "| --- | ---: | ---: | ---: |",
        f"| Top-1 | {metrics['top_1_numerator']} | {metrics['cases_evaluated']} | {metrics['top_1']:.12f} |",
        f"| Top-3 | {metrics['top_3_numerator']} | {metrics['cases_evaluated']} | {metrics['top_3']:.12f} |",
        f"| Top-5 | {metrics['top_5_numerator']} | {metrics['cases_evaluated']} | {metrics['top_5']:.12f} |",
        f"| Top-10 | {metrics['top_10_numerator']} | {metrics['cases_evaluated']} | {metrics['top_10']:.12f} |",
        f"| Top-50 | {metrics['top_50_numerator']} | {metrics['cases_evaluated']} | {metrics['top_50']:.12f} |",
        f"| Recall@100 | {metrics['recall_at_100_numerator']} | {metrics['cases_evaluated']} | {metrics['recall_at_100']:.12f} |",
        f"| MRR@100 | {metrics['mrr_at_100_numerator']} | {metrics['cases_evaluated']} | {metrics['mrr_at_100']:.12f} |",
        f"| Recall@200 | {metrics['recall_at_200_numerator']} | {metrics['cases_evaluated']} | {metrics['recall_at_200']:.12f} |",
        f"| MRR@200 | {metrics['mrr_at_200_numerator']} | {metrics['cases_evaluated']} | {metrics['mrr_at_200']:.12f} |",
        "",
        "## Cobertura jerarquica diagnostica",
        "",
        f"- HS6@100: {metrics['hs6_at_100_numerator']}/{metrics['cases_evaluated']} = {metrics['hs6_at_100']:.12f}.",
        f"- HS4@100: {metrics['hs4_at_100_numerator']}/{metrics['cases_evaluated']} = {metrics['hs4_at_100']:.12f}.",
        f"- Chapter@100: {metrics['chapter_at_100_numerator']}/{metrics['cases_evaluated']} = {metrics['chapter_at_100']:.12f}.",
        f"- HS6@200: {metrics['hs6_at_200_numerator']}/{metrics['cases_evaluated']} = {metrics['hs6_at_200']:.12f}.",
        f"- HS4@200: {metrics['hs4_at_200_numerator']}/{metrics['cases_evaluated']} = {metrics['hs4_at_200']:.12f}.",
        f"- Chapter@200: {metrics['chapter_at_200_numerator']}/{metrics['cases_evaluated']} = {metrics['chapter_at_200']:.12f}.",
        "",
        "## Distribucion de posiciones",
        "",
        "| Bucket | Cases |",
        "| --- | ---: |",
    ]
    for bucket in POSITION_BUCKETS:
        lines.append(f"| {bucket} | {position[bucket]} |")
    lines.extend(["", "## Estado Gate D", "", payload["gate_d_status"], ""])
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    artifact_dir = resolve_project_path(args.artifact_dir)
    output_dir = resolve_project_path(args.output_dir)
    model_path = resolve_project_path(args.model_path) if args.model_path else artifact_dir / "model"
    retrieval_depth = max(args.retrieval_depth, 200)
    start = time.time()

    eval_rows = _read_csv(evalset_path)
    eval_sha = _sha256(evalset_path)
    if eval_sha != EXPECTED_EVAL_SHA256:
        raise ValueError(f"Unexpected evalset hash: {eval_sha}")
    if len(eval_rows) != 1056:
        raise ValueError(f"Expected 1056 eval cases, got {len(eval_rows)}")
    if len({_clean(row["case_id"]) for row in eval_rows}) != len(eval_rows):
        raise ValueError("case_id values are not unique")

    retriever = DenseText2TradeRetriever(artifact_dir, model_path=model_path)
    if retriever.docs_count != len({_clean(row.get("codigo")) for row in retriever.docstore}):
        raise ValueError("Dense docstore must map to unique NANDINA-8 codes")
    model: SentenceTransformer = retriever.model  # type: ignore[assignment]

    queries = [_clean(row[QUERY_COLUMN]) for row in eval_rows]
    query_embeddings = model.encode(
        queries,
        batch_size=args.batch_size,
        convert_to_numpy=True,
        normalize_embeddings=retriever.embedding_normalize,
        show_progress_bar=True,
    ).astype(np.float32)
    vectors = np.asarray(retriever.vectors, dtype=np.float32)
    scores = query_embeddings @ vectors.T

    results_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    coverage_counter = Counter()
    corpus_codes = {_clean(doc.get("codigo")) for doc in retriever.docstore}
    eval_codes = {_normalize_code(row[LABEL_COLUMN]) for row in eval_rows}

    for idx, (eval_row, score_row) in enumerate(zip(eval_rows, scores), start=1):
        ref = _normalize_code(eval_row[LABEL_COLUMN])
        case_id = _clean(eval_row["case_id"])
        k = min(retrieval_depth, score_row.shape[0])
        top_idx = np.argpartition(-score_row, kth=k - 1)[:k]
        top_idx = top_idx[np.argsort(-score_row[top_idx])]

        candidate_codes: list[str] = []
        rank_ref = 0
        for rank, doc_idx in enumerate(top_idx, start=1):
            doc_idx_int = int(doc_idx)
            doc = retriever.docstore[doc_idx_int]
            mapped = retriever.id_map.get(str(doc_idx_int), {})
            code = _clean(mapped.get("codigo") or doc.get("codigo"))
            candidate_codes.append(code)
            if code == ref and rank_ref == 0:
                rank_ref = rank
            results_rows.append(
                {
                    "case_id": case_id,
                    "id_unico": _clean(eval_row.get("id_unico")),
                    "nandina_ref": ref,
                    "candidate_rank": rank,
                    "candidate_doc_idx": doc_idx_int,
                    "candidate_doc_id": _clean(mapped.get("doc_id") or doc.get("doc_id")),
                    "candidate_code": code,
                    "candidate_partida": code[:4],
                    "candidate_sub_partida": code[:6],
                    "candidate_clase": code[:2],
                    "score": float(score_row[doc_idx_int]),
                    "is_reference_code": int(code == ref),
                    "method": METHOD,
                }
            )

        if len(candidate_codes) != len(set(candidate_codes)):
            raise ValueError(f"Repeated code in effective dense ranking for {case_id}")

        if ref not in corpus_codes:
            coverage_class = "reference_absent_from_corpus"
            coverage_counter["reference_absent_from_corpus"] += 1
        elif 1 <= rank_ref <= 100:
            coverage_class = "reference_recovered_top_100"
            coverage_counter["reference_recovered_top_100"] += 1
        elif 101 <= rank_ref <= 200:
            coverage_class = "reference_recovered_101_200"
            coverage_counter["reference_recovered_101_200"] += 1
        else:
            coverage_class = "reference_present_not_recovered_top_200"
            coverage_counter["reference_present_not_recovered_top_200"] += 1

        case_row = {
            "case_id": case_id,
            "id_unico": _clean(eval_row.get("id_unico")),
            "declaracion": _clean(eval_row.get("declaracion")),
            "serie": _clean(eval_row.get("serie")),
            "query": _clean(eval_row[QUERY_COLUMN]),
            "nandina_ref": ref,
            "partida_ref": ref[:4],
            "sub_partida_ref": ref[:6],
            "clase_ref": ref[:2],
            "reference_code_in_corpus": ref in corpus_codes,
            "rank_ref": rank_ref,
            "position_bucket": _rank_bucket(rank_ref),
            "coverage_class": coverage_class,
            "retrieved_count": len(candidate_codes),
            "top1_code": candidate_codes[0] if candidate_codes else "",
            "top1_score": float(score_row[int(top_idx[0])]) if len(top_idx) else "",
            "mrr_at_100_contribution": _mrr_at(rank_ref, 100),
            "mrr_at_200_contribution": _mrr_at(rank_ref, 200),
            "method": METHOD,
        }
        for k_value in K_VALUES:
            case_row[f"hit_top_{k_value}"] = _hit(rank_ref, k_value)
        for k_value in RECALL_VALUES:
            case_row[f"hit_recall_{k_value}"] = _hit(rank_ref, k_value)
        for k_value in HIER_VALUES:
            case_row[f"exact_at_{k_value}"] = _hit(rank_ref, k_value)
            case_row[f"hs6_at_{k_value}"] = _hier_hit(candidate_codes, ref, 6, k_value)
            case_row[f"hs4_at_{k_value}"] = _hier_hit(candidate_codes, ref, 4, k_value)
            case_row[f"chapter_at_{k_value}"] = _hier_hit(candidate_codes, ref, 2, k_value)
        case_rows.append(case_row)

    n = len(case_rows)
    metrics: dict[str, Any] = {
        "cases_evaluated": n,
        "cases_with_retrieval": sum(1 for row in case_rows if int(row["retrieved_count"]) > 0),
        "zero_retrieval_cases": sum(1 for row in case_rows if int(row["retrieved_count"]) == 0),
        "not_found_at_depth": sum(1 for row in case_rows if int(row["rank_ref"]) == 0),
    }
    for k_value in K_VALUES:
        num = sum(int(row[f"hit_top_{k_value}"]) for row in case_rows)
        metrics[f"top_{k_value}_numerator"] = num
        metrics[f"top_{k_value}_denominator"] = n
        metrics[f"top_{k_value}"] = num / n
    for k_value in RECALL_VALUES:
        num = sum(int(row[f"hit_recall_{k_value}"]) for row in case_rows)
        metrics[f"recall_at_{k_value}_numerator"] = num
        metrics[f"recall_at_{k_value}_denominator"] = n
        metrics[f"recall_at_{k_value}"] = num / n
    for k_value in (100, 200):
        num = sum(float(row[f"mrr_at_{k_value}_contribution"]) for row in case_rows)
        metrics[f"mrr_at_{k_value}_numerator"] = num
        metrics[f"mrr_at_{k_value}_denominator"] = n
        metrics[f"mrr_at_{k_value}"] = num / n
    for k_value in HIER_VALUES:
        for metric_name in ("exact", "hs6", "hs4", "chapter"):
            num = sum(int(row[f"{metric_name}_at_{k_value}"]) for row in case_rows)
            metrics[f"{metric_name}_at_{k_value}_numerator"] = num
            metrics[f"{metric_name}_at_{k_value}_denominator"] = n
            metrics[f"{metric_name}_at_{k_value}"] = num / n

    position_distribution = Counter(row["position_bucket"] for row in case_rows)
    position_rows = [
        {
            "position_bucket": bucket,
            "cases": position_distribution[bucket],
            "share": position_distribution[bucket] / n,
        }
        for bucket in POSITION_BUCKETS
    ]
    coverage_summary = {
        "eval_cases": n,
        "eval_unique_codes": len(eval_codes),
        "eval_codes_present_exact_nandina8_in_corpus": len(eval_codes & corpus_codes),
        "eval_cases_present_exact_nandina8_in_corpus": sum(1 for row in case_rows if row["reference_code_in_corpus"]),
        "eval_cases_absent_from_corpus": coverage_counter["reference_absent_from_corpus"],
        "reference_recovered_top_100": coverage_counter["reference_recovered_top_100"],
        "reference_recovered_101_200": coverage_counter["reference_recovered_101_200"],
        "reference_present_not_recovered_top_200": coverage_counter["reference_present_not_recovered_top_200"],
        "reference_present_but_not_recovered_top_100": coverage_counter["reference_recovered_101_200"]
        + coverage_counter["reference_present_not_recovered_top_200"],
        "parent_codes_counted_as_exact_coverage": False,
    }

    source_corpus = resolve_project_path("data/processed/corpus_rag_v1_index.jsonl")
    source_rows = _load_jsonl(source_corpus)
    doc_codes = [_clean(doc.get("codigo")) for doc in retriever.docstore]
    corpus = {
        "source_corpus_path": _rel(source_corpus, root),
        "source_corpus_sha256": _sha256(source_corpus),
        "source": "corpus_rag_v1_index.jsonl",
        "normative_version": "text2trade_nandina8_v1",
        "source_rows_total": len(source_rows),
        "source_nandina8_rows": sum(1 for row in source_rows if _clean(row.get("tipo")) == "nandina_8"),
        "docstore_path": _rel(artifact_dir / "store/nandina8_docstore.jsonl", root),
        "docstore_sha256": _sha256(artifact_dir / "store/nandina8_docstore.jsonl"),
        "docstore_docs": len(retriever.docstore),
        "docstore_unique_codes": len(set(doc_codes)),
        "duplicate_codes": {code: count for code, count in Counter(doc_codes).items() if count > 1},
        "document_unit": "one vector/document per unique NANDINA-8 code",
        "text_fields": ["texto_index", "texto", "text", "content", "descripcion"],
        "text_field_used": sorted({_clean(doc.get("aux", {}).get("text_field_used")) for doc in retriever.docstore}),
        "hierarchical_levels": ["NANDINA-8 leaf text only in frozen Text2Trade docstore"],
        **coverage_summary,
    }

    model_manifest = _manifest_for_model(model_path, root)
    model_manifest.update(
        {
            "embedding_dim": retriever.embedding_dim,
            "device": str(model.device),
            "batch_size": args.batch_size,
            "normalize_embeddings": retriever.embedding_normalize,
            "query_document_encoding_policy": "same SentenceTransformer encoder, empty query/document prompts",
            "similarity_metric": "cosine via dot product over normalized vectors",
            "monte_carlo_dropout_in_run": False,
        }
    )
    _write_json(output_dir / "model_manifest.json", model_manifest)

    compatibility = _compatibility_report(root, output_dir, case_rows)
    strategy_rows = _strategy_comparison(output_dir, metrics)
    previous_hash_status = _previous_phase_hash_status(root)

    hierarchical_coverage = {
        "source": "text2trade_case_summary.csv",
        "diagnostic_only": True,
        "parent_match_is_not_exact_recovery": True,
        "metrics": {key: value for key, value in metrics.items() if re.match(r"^(exact|hs6|hs4|chapter)_at_(100|200)", key)},
    }
    _write_json(output_dir / "text2trade_hierarchical_coverage.json", hierarchical_coverage)
    _write_json(output_dir / "text2trade_coverage_summary.json", coverage_summary)
    _write_json(output_dir / "position_distribution.json", {"rows": position_rows, "total": sum(row["cases"] for row in position_rows)})
    _write_csv(output_dir / "position_distribution.csv", position_rows, ["position_bucket", "cases", "share"])

    outputs = {
        "text2trade_results_csv": output_dir / "text2trade_results.csv",
        "text2trade_case_summary_csv": output_dir / "text2trade_case_summary.csv",
        "text2trade_metrics_json": output_dir / "text2trade_metrics.json",
        "text2trade_coverage_summary_json": output_dir / "text2trade_coverage_summary.json",
        "text2trade_hierarchical_coverage_json": output_dir / "text2trade_hierarchical_coverage.json",
        "position_distribution_json": output_dir / "position_distribution.json",
        "position_distribution_csv": output_dir / "position_distribution.csv",
        "compatibility_json": output_dir / "historical_flat_hierarchical_text2trade_compatibility_v0.2.json",
        "strategy_comparison_csv": output_dir / "strategy_comparison_v0.2.csv",
        "strategy_comparison_json": output_dir / "strategy_comparison_v0.2.json",
        "model_manifest_json": output_dir / "model_manifest.json",
        "run_metadata_json": output_dir / "run_metadata.json",
        "summary_md": output_dir / "summary.md",
    }

    result_fields = [
        "case_id",
        "id_unico",
        "nandina_ref",
        "candidate_rank",
        "candidate_doc_idx",
        "candidate_doc_id",
        "candidate_code",
        "candidate_partida",
        "candidate_sub_partida",
        "candidate_clase",
        "score",
        "is_reference_code",
        "method",
    ]
    case_fields = list(case_rows[0])
    _write_csv(outputs["text2trade_results_csv"], results_rows, result_fields)
    _write_csv(outputs["text2trade_case_summary_csv"], case_rows, case_fields)

    payload = {
        "version": DATASET_VERSION,
        "dataset_version": DATASET_VERSION,
        "experiment_id": EXPERIMENT_ID,
        "strategy": "text2trade_dense",
        "method": METHOD,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": " ".join(["python", "-B", "-m", "src.experiments.evaluate_dense_text2trade_data_aduanas_v02", "--retrieval-depth", str(retrieval_depth)]),
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "packages": {
                "numpy": np.__version__,
                "torch": _package_version("torch"),
                "sentence-transformers": _package_version("sentence-transformers"),
                "transformers": _package_version("transformers"),
                "tokenizers": _package_version("tokenizers"),
                "safetensors": _package_version("safetensors"),
                "hnswlib": _package_version("hnswlib"),
            },
        },
        "git": {
            "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=root, text=True, encoding="utf-8").strip(),
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True, encoding="utf-8").strip(),
            "dirty_status_short": subprocess.check_output(["git", "status", "--short"], cwd=root, text=True, encoding="utf-8").splitlines(),
        },
        "inputs": {
            "evalset": _rel(evalset_path, root),
            "evalset_sha256": eval_sha,
            "dense_artifact_dir": _rel(artifact_dir, root),
            "source_corpus": corpus["source_corpus_path"],
            "source_corpus_sha256": corpus["source_corpus_sha256"],
            "docstore": corpus["docstore_path"],
            "docstore_sha256": corpus["docstore_sha256"],
            "vectors": _rel(artifact_dir / "index/vectors.npy", root),
            "vectors_sha256": _sha256(artifact_dir / "index/vectors.npy"),
            "id_map": _rel(artifact_dir / "index/id_map.json", root),
            "id_map_sha256": _sha256(artifact_dir / "index/id_map.json"),
            "retrieval_config": _rel(artifact_dir / "retrieval_config.json", root),
            "retrieval_config_sha256": _sha256(artifact_dir / "retrieval_config.json"),
            "artifact_metadata": _rel(artifact_dir / "text2trade_nandina8_run_metadata.json", root),
            "artifact_metadata_sha256": _sha256(artifact_dir / "text2trade_nandina8_run_metadata.json"),
        },
        "artifact_hashes": _artifact_file_hashes(artifact_dir, root),
        "columns": {"query": QUERY_COLUMN, "label": LABEL_COLUMN},
        "parameters": {
            "retrieval_depth": retrieval_depth,
            "batch_size": args.batch_size,
            "embedding_normalize": retriever.embedding_normalize,
            "ranking_unit": "unique NANDINA-8 code",
            "score": "dot product over normalized dense embeddings",
            "ann_backend_configured": "hnswlib cosine",
            "ann_backend_used": None,
            "brute_force_used": True,
            "hnsw_index_exists": (artifact_dir / "index/hnsw.index").exists(),
            "mcd_configured_in_artifact": bool(_load_json(artifact_dir / "retrieval_config.json").get("mcd", {}).get("enabled")),
            "mcd_used_in_run": False,
            "max_sequence_length": getattr(model, "max_seq_length", None),
            "truncation_policy": "tokenizer max_length=128, truncation_side=right, truncation_strategy=longest_first",
        },
        "model_manifest": model_manifest,
        "corpus": corpus,
        "metrics": metrics,
        "coverage_summary": coverage_summary,
        "position_distribution": dict(position_distribution),
        "compatibility_report": compatibility,
        "strategy_comparison": strategy_rows,
        "previous_phase_artifact_hashes": previous_hash_status,
        "validation": {
            "evalset_hash_matches_official_v02": eval_sha == EXPECTED_EVAL_SHA256,
            "cases_evaluated_1056": n == 1056,
            "case_ids_unique": len({_clean(row["case_id"]) for row in case_rows}) == n,
            "same_case_ids_as_a_b_c": compatibility["identical_case_id_sets"],
            "same_labels_as_a_b_c": compatibility["identical_labels"],
            "compatibility_true": compatibility["compatible"],
            "reference_codes_all_present_in_dense_corpus": coverage_summary["eval_cases_absent_from_corpus"] == 0,
            "ranking_effective_codes_unique": True,
            "label_string_found_inside_query_count": sum(1 for row in case_rows if row["nandina_ref"] in row["query"]),
            "dam_used_as_query_feature": False,
            "serie_used_as_query_feature": False,
            "historical_results_used_as_retrieval_features": False,
            "flat_results_used_as_retrieval_features": False,
            "hierarchical_results_used_as_retrieval_features": False,
            "candidate_pool_used": False,
            "dual_protected_used": False,
            "mixed_70_30_used": False,
            "rag_used": False,
            "llm_used": False,
            "phase_e_started": False,
            "previous_phase_artifacts_preserved": previous_hash_status["all_match_expected"],
            "large_outputs_over_50mb_versioned": False,
        },
        "gate_d_status": "GATE D APROBADO"
        if compatibility["compatible"] and previous_hash_status["all_match_expected"] and n == 1056
        else "GATE D NO APROBADO",
        "outputs": {key: _rel(path, root) for key, path in outputs.items()},
    }
    _write_json(outputs["text2trade_metrics_json"], payload)
    SUMMARY_PAYLOAD = {
        "metrics": metrics,
        "corpus": corpus,
        "position_distribution": {bucket: position_distribution[bucket] for bucket in POSITION_BUCKETS},
        "gate_d_status": payload["gate_d_status"],
    }
    outputs["summary_md"].write_text(_summary_markdown(SUMMARY_PAYLOAD), encoding="utf-8", newline="\n")
    output_hashes = {}
    for key, path in outputs.items():
        if key == "run_metadata_json":
            continue
        output_hashes[key] = _sha256(path)
    payload["output_sha256"] = output_hashes
    _write_json(outputs["run_metadata_json"], payload)
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EXP-04 Fase D Text2Trade dense retrieval on data_aduanas clase 87 v0.2.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--artifact-dir", type=Path, default=DEFAULT_ARTIFACT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model-path", type=Path, default=None)
    parser.add_argument("--retrieval-depth", type=int, default=200)
    parser.add_argument("--batch-size", type=int, default=32)
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: EXP-04 Fase D Text2Trade dense v0.2 completada")
    print(f"Gate D: {payload['gate_d_status']}")
    print(f"Casos evaluados: {metrics['cases_evaluated']}")
    for metric in ["top_1", "top_3", "top_5", "top_10", "top_50", "recall_at_100", "mrr_at_100", "recall_at_200", "mrr_at_200"]:
        print(f"{metric}: {metrics[metric]}")
    print(f"Outputs: {payload['outputs']['run_metadata_json']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
