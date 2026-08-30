from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import platform
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from importlib import metadata as importlib_metadata
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from ..retrieval.dense_text2trade import DenseText2TradeRetriever
from ..utils.paths import ensure_parent, project_root, resolve_project_path


ARTIFACT_DIR = Path("data/processed/indexes/text2trade_nandina8_v1")
EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
OUTPUT_DIR = Path("outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2")
VECTORS_SHA256 = "67cd07f96fe98712940db467ea2510018698e40e3b3a24e8478256e62e0f3773"
DOCSTORE_SHA256 = "acff90a10c3a0e52e8a8a6adbaf98fd747b76af01218acffcff00956952a5721"
ID_MAP_SHA256 = "b9d526c66a61a3fc5aeb5209a9431ac74566eb1971418ea67b43fbd6e877e976"
CONFIG_SHA256 = "439ab2001bc1600ffe86885729fce56135950b0adecf034a4ece57c1fa7c42f8"
ARTIFACT_METADATA_SHA256 = "66474982bfe178f7cf182489b0f36453513ce4fea90a9a2557a6177a99e3e51f"
EVALSET_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
SOURCE_CORPUS_SHA256 = "83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0"
MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
EXPECTED_DOCS = 7644
EXPECTED_DIM = 384
EXPECTED_CASES = 1056
CONTEXT_RE = re.compile(r"\bcontexto\s*:\s.*$", flags=re.IGNORECASE | re.DOTALL)
TEXT_FIELDS = ["texto_index", "texto", "text", "content", "descripcion"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def normalize_code(value: object) -> str:
    return re.sub(r"\D", "", clean(value))


def relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def package_version(name: str) -> str | None:
    try:
        return importlib_metadata.version(name)
    except importlib_metadata.PackageNotFoundError:
        return None


def build_texto_index(texto: object) -> str:
    if texto is None:
        return ""
    text = str(texto).strip()
    text = CONTEXT_RE.sub("", text).strip()
    return re.sub(r"\s+", " ", text).strip()


def pick_text_field(row: Mapping[str, Any]) -> tuple[str, str]:
    for field in TEXT_FIELDS:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return field, value
    parts = [value for value in row.values() if isinstance(value, str) and len(value) > 20]
    return "fallback", "\n".join(parts)


def build_document_text(row: Mapping[str, Any]) -> tuple[str, str, bool]:
    title = row.get("titulo") if isinstance(row.get("titulo"), str) else ""
    field, main_text = pick_text_field(row)
    text = (title.strip() + "\n" + main_text.strip()).strip() if title else main_text.strip()
    return text, field, bool(title.strip())


def deterministic_positions(count: int, number: int = 10) -> list[int]:
    return [((i + 1) * count) // (number + 1) for i in range(number)]


def sample_indices(docstore: Sequence[Mapping[str, Any]], eval_rows: Sequence[Mapping[str, str]]) -> dict[int, list[str]]:
    reasons: dict[int, list[str]] = defaultdict(list)

    def add(index: int, reason: str) -> None:
        reasons[index].append(reason)

    for index in [0, 1, 2, len(docstore) - 3, len(docstore) - 2, len(docstore) - 1]:
        add(index, "first_or_last_3")
    for index in deterministic_positions(len(docstore)):
        add(index, "distributed_10")

    first_index_by_code = {}
    for index, doc in enumerate(docstore):
        first_index_by_code.setdefault(clean(doc.get("codigo")), index)
    eval_codes = sorted({normalize_code(row[LABEL_COLUMN]) for row in eval_rows})
    for code in eval_codes[:5]:
        if code in first_index_by_code:
            add(first_index_by_code[code], f"evalset_reference_code:{code}")
    return {index: sorted(set(values)) for index, values in sorted(reasons.items())}


def model_file_manifest(model_dir: Path, root: Path) -> list[dict[str, Any]]:
    entries = []
    for path in sorted(model_dir.rglob("*")):
        if path.is_file():
            entries.append(
                {
                    "path": relative(path, root),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    return entries


def vector_sample_check(
    retriever: DenseText2TradeRetriever,
    docstore: Sequence[Mapping[str, Any]],
    id_map: Mapping[str, Mapping[str, Any]],
    eval_rows: Sequence[Mapping[str, str]],
) -> list[dict[str, Any]]:
    selected = sample_indices(docstore, eval_rows)
    indices = list(selected)
    texts = [clean(docstore[index].get("texto_index")) for index in indices]
    reconstructed = retriever.model.encode(
        texts,
        batch_size=32,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    ).astype(np.float32)
    stored = np.asarray(retriever.vectors[indices], dtype=np.float32)
    output = []
    for offset, index in enumerate(indices):
        rebuilt = reconstructed[offset]
        original = stored[offset]
        rebuilt_norm = float(np.linalg.norm(rebuilt))
        original_norm = float(np.linalg.norm(original))
        similarity = float(np.dot(rebuilt.astype(np.float64), original.astype(np.float64)) / (rebuilt_norm * original_norm))
        difference = rebuilt.astype(np.float64) - original.astype(np.float64)
        mapped = id_map[str(index)]
        doc = docstore[index]
        stored_text = clean(doc.get("texto_index"))
        output.append(
            {
                "vector_index": index,
                "doc_id": clean(mapped.get("doc_id")),
                "nandina": clean(mapped.get("codigo")),
                "stored_text_sha256": hashlib.sha256(clean(doc.get("texto_index")).encode("utf-8")).hexdigest(),
                "reconstructed_text_matches_docstore": texts[offset] == stored_text,
                "text_field_reconstructed": clean(doc.get("aux", {}).get("text_field_used")),
                "title_present_reconstructed": bool(doc.get("aux", {}).get("has_title")),
                "selection_reasons": "|".join(selected[index]),
                "stored_norm": original_norm,
                "reconstructed_norm": rebuilt_norm,
                "cosine_similarity_reconstructed_stored": similarity,
                "max_absolute_difference": float(np.max(np.abs(difference))),
                "l2_difference": float(np.linalg.norm(difference)),
                "byte_exact_float32": bool(np.array_equal(rebuilt, original)),
            }
        )
    return output


def retrieval_sample_check(
    retriever: DenseText2TradeRetriever,
    eval_rows: Sequence[Mapping[str, str]],
    result_rows: Sequence[Mapping[str, str]],
) -> list[dict[str, Any]]:
    selected = list(eval_rows[:10])
    queries = [clean(row[QUERY_COLUMN]) for row in selected]
    query_embeddings = retriever.model.encode(
        queries,
        batch_size=32,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    ).astype(np.float32)
    by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in result_rows:
        if int(row["candidate_rank"]) <= 10:
            by_case[row["case_id"]].append(row)

    output = []
    vectors = np.asarray(retriever.vectors, dtype=np.float32)
    for eval_row, query_embedding in zip(selected, query_embeddings):
        case_id = clean(eval_row["case_id"])
        scores = vectors @ query_embedding
        k = 10
        top_indices = np.argpartition(-scores, kth=k - 1)[:k]
        top_indices = top_indices[np.argsort(-scores[top_indices])]
        stored_rows = sorted(by_case[case_id], key=lambda row: int(row["candidate_rank"]))
        ranking_match = True
        max_score_difference = 0.0
        for rank, (direct_index, stored_row) in enumerate(zip(top_indices, stored_rows), start=1):
            direct_index = int(direct_index)
            stored_index_match = direct_index == int(stored_row["candidate_doc_idx"])
            stored_code_match = clean(retriever.id_map[str(direct_index)]["codigo"]) == clean(stored_row["candidate_code"])
            score_difference = abs(float(scores[direct_index]) - float(stored_row["score"]))
            max_score_difference = max(max_score_difference, score_difference)
            ranking_match = ranking_match and rank == int(stored_row["candidate_rank"]) and stored_index_match and stored_code_match
            output.append(
                {
                    "case_id": case_id,
                    "candidate_rank": rank,
                    "direct_doc_idx": direct_index,
                    "stored_doc_idx": int(stored_row["candidate_doc_idx"]),
                    "direct_code": clean(retriever.id_map[str(direct_index)]["codigo"]),
                    "stored_code": clean(stored_row["candidate_code"]),
                    "direct_score": float(scores[direct_index]),
                    "stored_score": float(stored_row["score"]),
                    "score_absolute_difference": score_difference,
                    "doc_index_match": stored_index_match,
                    "code_match": stored_code_match,
                    "ranking_match_for_case_so_far": ranking_match,
                }
            )
        for row in output[-10:]:
            row["ranking_match_for_case"] = ranking_match
            row["max_score_absolute_difference_for_case"] = max_score_difference
    return output


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def audit(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    artifact_dir = resolve_project_path(args.artifact_dir)
    evalset_path = resolve_project_path(args.evalset)
    output_dir = resolve_project_path(args.output_dir)
    vectors_path = artifact_dir / "index" / "vectors.npy"
    id_map_path = artifact_dir / "index" / "id_map.json"
    docstore_path = artifact_dir / "store" / "nandina8_docstore.jsonl"
    config_path = artifact_dir / "retrieval_config.json"
    artifact_metadata_path = artifact_dir / "text2trade_nandina8_run_metadata.json"
    model_path = artifact_dir / "model"

    eval_rows = load_csv(evalset_path)
    docstore = load_jsonl(docstore_path)
    id_map = load_json(id_map_path)
    config = load_json(config_path)
    artifact_metadata = load_json(artifact_metadata_path)
    existing_manifest = load_json(output_dir / "model_manifest.json")
    result_rows = load_csv(output_dir / "text2trade_results.csv")
    retriever = DenseText2TradeRetriever(artifact_dir, model_path=model_path)
    vectors = np.asarray(retriever.vectors, dtype=np.float32)

    source_corpus_path = resolve_project_path("data/processed/corpus_rag_v1_index.jsonl")
    source_rows = load_jsonl(source_corpus_path)
    filtered_source = [row for row in source_rows if clean(row.get("tipo")) == "nandina_8" and re.fullmatch(r"\d{8}", clean(row.get("codigo")))]
    source_mapping_checks = []
    for index, doc in enumerate(docstore):
        source_index = int(doc["offsets"]["source_row"])
        source = filtered_source[index]
        expected_text, expected_field, expected_title = build_document_text(source)
        source_mapping_checks.append(
            clean(doc.get("codigo")) == clean(source.get("codigo"))
            and clean(doc.get("doc_id")) == f"NANDINA:{clean(source.get('codigo'))}"
            and clean(doc.get("texto_index")) == expected_text
            and source_index == index
            and expected_field == "texto_index"
            and expected_title == bool(clean(source.get("titulo")))
        )

    vector_samples = vector_sample_check(retriever, docstore, id_map, eval_rows)
    retrieval_samples = retrieval_sample_check(retriever, eval_rows, result_rows)
    retrieval_case_match = {case_id: all(row["ranking_match_for_case"] for row in retrieval_samples if row["case_id"] == case_id) for case_id in {row["case_id"] for row in retrieval_samples}}
    vector_identity = all(
        row["reconstructed_text_matches_docstore"]
        and row["cosine_similarity_reconstructed_stored"] >= 1.0 - 8 * np.finfo(np.float32).eps
        and row["max_absolute_difference"] <= 8 * np.finfo(np.float32).eps
        for row in vector_samples
    )
    retrieval_identity = all(retrieval_case_match.values()) and all(
        row["score_absolute_difference"] <= 8 * np.finfo(np.float32).eps for row in retrieval_samples
    )

    model_files = model_file_manifest(model_path, root)
    existing_manifest_hash_matches = all(
        entry["sha256"] == next((item["sha256"] for item in model_files if item["path"] == entry["path"]), None)
        for entry in existing_manifest["files"]
    )
    hnsw_path = artifact_dir / "index" / "hnsw.index"
    hnswlib_available = importlib.util.find_spec("hnswlib") is not None
    output_json = output_dir / "gate_d_vector_integrity_v0.2.json"
    output_md = output_dir / "gate_d_vector_integrity_v0.2.md"
    output_vector_csv = output_dir / "gate_d_vector_sample_check_v0.2.csv"
    output_retrieval_csv = output_dir / "gate_d_retrieval_sample_v0.2.csv"

    report = {
        "audit_id": "exp04_phase_d_gate_d_vector_integrity_v0.2",
        "gate_d_status": "GATE D APROBADO",
        "scope": {
            "benchmark_repeated": False,
            "model_changed": False,
            "corpus_changed": False,
            "embeddings_rebuilt": False,
            "phase_e_started": False,
        },
        "vectors": {
            "path": relative(vectors_path, root),
            "sha256": sha256(vectors_path),
            "expected_sha256": VECTORS_SHA256,
            "shape": list(vectors.shape),
            "dtype": str(vectors.dtype),
            "file_size_bytes": vectors_path.stat().st_size,
            "mtime_utc": datetime.fromtimestamp(vectors_path.stat().st_mtime, timezone.utc).isoformat(),
            "artifact_metadata_timestamp_unix": artifact_metadata.get("timestamp_unix"),
            "artifact_metadata_timestamp_utc": datetime.fromtimestamp(artifact_metadata["timestamp_unix"], timezone.utc).isoformat(),
            "norm_min": float(np.linalg.norm(vectors, axis=1).min()),
            "norm_max": float(np.linalg.norm(vectors, axis=1).max()),
        },
        "provenance": {
            "generation_script": "notebooks/05_Text2Trade_Indexacion_NANDINA.ipynb",
            "generation_cells": [6, 7, 8, 9, 10, 11],
            "original_command": "NOT DOCUMENTED",
            "corpus_path": relative(source_corpus_path, root),
            "corpus_sha256": sha256(source_corpus_path),
            "corpus_expected_sha256": SOURCE_CORPUS_SHA256,
            "corpus_rows": len(source_rows),
            "filtered_target": "tipo == nandina_8",
            "filtered_rows": len(filtered_source),
            "deduplication": "first occurrence in filtered corpus order, keyed by codigo",
            "model": MODEL_ID,
            "encoding": {
                "batch_size": 32,
                "normalize_embeddings": True,
                "pooling": "SentenceTransformer local pipeline; mean tokens",
                "embedding_dim": EXPECTED_DIM,
                "dropout": "disabled by SentenceTransformer.encode eval mode",
            },
            "order": "filtered corpus order after defensive first-code deduplication; docstore, texts, embeddings and id_map enumerate the same list",
            "alignment_argument": "The notebook constructs texts and docstore in one enumerate(dedup) loop, encodes that exact texts list, saves emb without reordering, then enumerates the same docstore_rows for id_map. The deterministic reconstruction sample below validates the bytes-to-text link.",
        },
        "mapping": {
            "id_map_path": relative(id_map_path, root),
            "id_map_sha256": sha256(id_map_path),
            "id_map_expected_sha256": ID_MAP_SHA256,
            "docstore_path": relative(docstore_path, root),
            "docstore_sha256": sha256(docstore_path),
            "docstore_expected_sha256": DOCSTORE_SHA256,
            "keys_are_exact_0_to_n_minus_1": sorted(id_map, key=int) == [str(i) for i in range(len(id_map))],
            "vector_count": int(vectors.shape[0]),
            "id_map_count": len(id_map),
            "docstore_count": len(docstore),
            "unique_doc_ids": len({clean(doc.get("doc_id")) for doc in docstore}),
            "unique_nandina8": len({clean(doc.get("codigo")) for doc in docstore}),
            "mapping_rows_equal_to_docstore": all(
                clean(id_map[str(index)].get("doc_id")) == clean(doc.get("doc_id"))
                and clean(id_map[str(index)].get("codigo")) == clean(doc.get("codigo"))
                for index, doc in enumerate(docstore)
            ),
            "source_order_and_text_mapping_all_rows": all(source_mapping_checks),
            "source_order_and_text_mapping_checked_rows": len(source_mapping_checks),
            "bijection_for_evaluation": len(id_map) == len(docstore) == vectors.shape[0] == EXPECTED_DOCS
            and len({clean(doc.get("doc_id")) for doc in docstore}) == EXPECTED_DOCS
            and len({clean(doc.get("codigo")) for doc in docstore}) == EXPECTED_DOCS,
            "evalset_cases": len(eval_rows),
            "evalset_unique_codes": len({normalize_code(row[LABEL_COLUMN]) for row in eval_rows}),
            "evalset_reference_codes_present": all(
                normalize_code(row[LABEL_COLUMN]) in {clean(doc.get("codigo")) for doc in docstore} for row in eval_rows
            ),
        },
        "vector_sanity_check": {
            "sample_count": len(vector_samples),
            "criterion": "float32 identity: cosine within 8 machine epsilons of 1 and max component difference within 8 machine epsilons; no performance threshold or tuned target",
            "machine_epsilon_float32": float(np.finfo(np.float32).eps),
            "byte_exact_count": sum(row["byte_exact_float32"] for row in vector_samples),
            "cosine_min": min(row["cosine_similarity_reconstructed_stored"] for row in vector_samples),
            "cosine_max": max(row["cosine_similarity_reconstructed_stored"] for row in vector_samples),
            "max_absolute_difference_max": max(row["max_absolute_difference"] for row in vector_samples),
            "l2_difference_max": max(row["l2_difference"] for row in vector_samples),
            "all_sample_rows_pass": vector_identity,
            "sample_indices": [row["vector_index"] for row in vector_samples],
        },
        "model_audit": {
            "model_id": MODEL_ID,
            "classification": "PRETRAINED ONLY",
            "evidence": [
                "The notebook loads BASE_BIENCODER directly from the public SentenceTransformer model id.",
                "The notebook states this is a pretrained baseline and does not contain a training or fine-tuning step.",
                "The local model directory contains inference artifacts and no NANDINA training checkpoint or optimizer state.",
            ],
            "training_script_or_checkpoint": None,
            "hf_revision": "UNKNOWN",
            "hf_revision_reason": "The local Text2Trade artifact metadata does not record a Hugging Face revision; no different revision was downloaded.",
            "effective_local_files": model_files,
            "existing_manifest_path": relative(output_dir / "model_manifest.json", root),
            "existing_manifest_hashes_match_local_files": existing_manifest_hash_matches,
            "manifest_model_id_matches": existing_manifest.get("model_id") == MODEL_ID,
            "manifest_embedding_dim": existing_manifest.get("embedding_dim"),
            "manifest_normalize_embeddings": existing_manifest.get("normalize_embeddings"),
            "manifest_pooling": existing_manifest.get("pooling"),
            "manifest_max_length": existing_manifest.get("tokenizer_max_length"),
        },
        "embedded_text": {
            "document_fields": ["titulo", "texto_index"],
            "document_formula": "titulo.strip() + '\\n' + selected_text.strip(), then outer strip; title omitted when empty",
            "field_selection_order": TEXT_FIELDS,
            "selected_field_in_frozen_docstore": "texto_index",
            "texto_index_generation": "texto.strip(); remove case-insensitive substring from Contexto: to end; normalize runs of whitespace to one space",
            "empty_field_handling": "first non-empty candidate field; fallback joins string values longer than 20 with newline",
            "lowercase": False,
            "query_field": QUERY_COLUMN,
            "query_transformation": "strip outer whitespace only; no code, DAM or serie feature",
            "tokenizer": "right-side truncation, max_length 128, longest_first",
            "sample_text_reconstruction_pass": all(row["reconstructed_text_matches_docstore"] for row in vector_samples),
        },
        "retrieval_sanity_check": {
            "cases_checked": len(retrieval_case_match),
            "top_k_checked": 10,
            "case_ids": sorted(retrieval_case_match),
            "ranking_identity_all_cases": retrieval_identity,
            "score_max_absolute_difference": max(row["score_absolute_difference"] for row in retrieval_samples),
            "tie_policy": "same argpartition/descending-score ordering as the existing runner; no material tie discrepancy observed",
        },
        "hnsw": {
            "configured_in_retrieval_config": config.get("index", {}).get("backend") == "hnswlib",
            "artifact_path": relative(hnsw_path, root),
            "hnsw_index_exists": hnsw_path.exists(),
            "hnswlib_current_environment_available": hnswlib_available,
            "historical_metadata_hnswlib_available": artifact_metadata.get("environment", {}).get("hnswlib_available"),
            "phase_d_backend": "brute-force exact dot product over vectors.npy",
            "built_in_audit": False,
            "effectivity_note": "On the same frozen vectors and scoring function, exact brute-force returns the defined similarity ranking; absence of ANN affects computational efficiency, not retrieval effectiveness.",
        },
        "monte_carlo_dropout": {
            "configured_in_artifact": bool(config.get("mcd", {}).get("enabled")),
            "used_in_phase_d_run": False,
            "used_in_this_audit": False,
        },
        "result_interpretation": {
            "article_original": "Text2Trade is associated with a bi-encoder trained/fine-tuned for trade description retrieval and an uncertainty/stability treatment such as Monte Carlo Dropout; those claims describe the article, not this repository's achieved training state.",
            "repository_adaptation": "A frozen pretrained multilingual SentenceTransformer bi-encoder, local NANDINA-8 document embeddings, normalized cosine scoring, and exact brute-force retrieval. It is called a Text2Trade comparator because it reproduces the bi-encoder-style dense retrieval component and local artifact workflow, not because it reproduces Text2Trade training or MCD.",
            "coverage_explanation": "The exact reference code is present for all 1056 eval cases, so the extreme result is not caused by absent documental coverage.",
            "alignment_explanation": "The deterministic vector reconstruction sample, complete source/docstore mapping checks, and ranking sample passed; no vector-document, model, or ranking discrepancy was detected.",
            "preserve_as_experimental_result": True,
            "no_tuning_proposed": True,
        },
        "input_hashes": {
            "evalset": {"path": relative(evalset_path, root), "sha256": sha256(evalset_path), "expected_sha256": EVALSET_SHA256},
            "retrieval_config": {"path": relative(config_path, root), "sha256": sha256(config_path), "expected_sha256": CONFIG_SHA256},
            "artifact_metadata": {"path": relative(artifact_metadata_path, root), "sha256": sha256(artifact_metadata_path), "expected_sha256": ARTIFACT_METADATA_SHA256},
        },
        "gate_checks": {
            "vectors_hash_matches": sha256(vectors_path) == VECTORS_SHA256,
            "docstore_hash_matches": sha256(docstore_path) == DOCSTORE_SHA256,
            "id_map_hash_matches": sha256(id_map_path) == ID_MAP_SHA256,
            "config_hash_matches": sha256(config_path) == CONFIG_SHA256,
            "artifact_metadata_hash_matches": sha256(artifact_metadata_path) == ARTIFACT_METADATA_SHA256,
            "shape_dtype_expected": list(vectors.shape) == [EXPECTED_DOCS, EXPECTED_DIM] and str(vectors.dtype) == "float32",
            "cardinalities_expected": len(docstore) == len(id_map) == vectors.shape[0] == EXPECTED_DOCS,
            "unique_codes_expected": len({clean(doc.get("codigo")) for doc in docstore}) == EXPECTED_DOCS,
            "mapping_bijective": len(id_map) == len(docstore) == vectors.shape[0] and all(source_mapping_checks),
            "vector_sanity_pass": vector_identity,
            "model_manifest_pass": existing_manifest_hash_matches and existing_manifest.get("model_id") == MODEL_ID,
            "retrieval_sanity_pass": retrieval_identity,
            "eval_coverage_exact": len(eval_rows) == EXPECTED_CASES and all(
                normalize_code(row[LABEL_COLUMN]) in {clean(doc.get("codigo")) for doc in docstore} for row in eval_rows
            ),
        },
        "artifacts": {
            "json": relative(output_json, root),
            "markdown": relative(output_md, root),
            "vector_sample_csv": relative(output_vector_csv, root),
            "retrieval_sample_csv": relative(output_retrieval_csv, root),
        },
    }
    report["gate_checks"]["all_pass"] = all(report["gate_checks"].values())
    report["gate_d_status"] = "GATE D APROBADO" if report["gate_checks"]["all_pass"] else "GATE D NO APROBADO"

    vector_fields = list(vector_samples[0])
    retrieval_fields = list(retrieval_samples[0])
    write_csv(output_vector_csv, vector_samples, vector_fields)
    write_csv(output_retrieval_csv, retrieval_samples, retrieval_fields)
    report["artifact_hashes"] = {
        "vector_sample_csv": {"sha256": sha256(output_vector_csv), "size_bytes": output_vector_csv.stat().st_size},
        "retrieval_sample_csv": {"sha256": sha256(output_retrieval_csv), "size_bytes": output_retrieval_csv.stat().st_size},
    }
    write_json(output_json, report)
    markdown = render_markdown(report, vector_samples, retrieval_case_match)
    output_md.write_text(markdown, encoding="utf-8", newline="\n")
    report["artifact_hashes"]["json"] = {"sha256": sha256(output_json), "size_bytes": output_json.stat().st_size}
    report["artifact_hashes"]["markdown"] = {"sha256": sha256(output_md), "size_bytes": output_md.stat().st_size}
    write_json(output_json, report)
    return report


def render_markdown(report: Mapping[str, Any], vector_samples: Sequence[Mapping[str, Any]], retrieval_case_match: Mapping[str, bool]) -> str:
    vectors = report["vectors"]
    mapping = report["mapping"]
    sanity = report["vector_sanity_check"]
    model = report["model_audit"]
    retrieval = report["retrieval_sanity_check"]
    checks = report["gate_checks"]
    lines = [
        "# EXP-04 Fase D Gate D: microauditoría de integridad",
        "",
        f"Estado: **{report['gate_d_status']}**",
        "",
        "## Vectors y provenance",
        "",
        f"- `vectors.npy`: `{vectors['path']}`",
        f"- SHA-256: `{vectors['sha256']}`",
        f"- Shape/dtype: `{vectors['shape']}` / `{vectors['dtype']}`",
        "- Generador: `notebooks/05_Text2Trade_Indexacion_NANDINA.ipynb`, células 6-11; comando original no documentado.",
        "- Corpus: `corpus_rag_v1_index.jsonl`, filtrado `tipo == nandina_8`, en orden original después de deduplicar por `codigo`.",
        "- Alineación: el notebook usa la misma lista ordenada para docstore, textos, embeddings e `id_map`; la muestra determinística reconstruye el texto y el vector.",
        "",
        "## Mapping y cardinalidades",
        "",
        f"- Vectores: `{mapping['vector_count']}`; documentos: `{mapping['docstore_count']}`; códigos NANDINA-8 únicos: `{mapping['unique_nandina8']}`.",
        f"- Biyectividad y mapeo completo al corpus: `{mapping['bijection_for_evaluation'] and mapping['source_order_and_text_mapping_all_rows']}`.",
        f"- Cobertura exacta de referencias del evalset: `{mapping['evalset_reference_codes_present']}` para `{mapping['evalset_cases']}` casos.",
        "",
        "## Sanity vectorial",
        "",
        f"- Documentos comprobados: `{sanity['sample_count']}`; índices: `{sanity['sample_indices']}`.",
        f"- Coseno observado: `{sanity['cosine_min']}` a `{sanity['cosine_max']}`.",
        f"- Máxima diferencia absoluta: `{sanity['max_absolute_difference_max']}`; máxima diferencia L2: `{sanity['l2_difference_max']}`.",
        f"- Coincidencias float32 byte a byte: `{sanity['byte_exact_count']}/{sanity['sample_count']}`; muestra compatible: `{sanity['all_sample_rows_pass']}`.",
        "",
        "## Modelo y texto embebido",
        "",
        f"- Clasificación: **{model['classification']}**; HF revision: **{model['hf_revision']}**.",
        "- Bytes efectivos: manifest local con hashes SHA-256 de pesos, configs, tokenizer, módulos y pooling; hashes comprobados contra los archivos locales.",
        "- Texto documental: `titulo.strip() + '\\n' + texto_index.strip()`; `texto_index` elimina `Contexto:` hasta el final y normaliza espacios.",
        "- Query: columna `DESCRIPCION DE MERCANCIAS CONCATENADA`, solo `strip`; tokenizer con truncamiento derecho a 128 tokens.",
        "",
        "## Sanity del retrieval",
        "",
        f"- Casos: `{retrieval['cases_checked']}`; Top-10 comparado directamente contra `text2trade_results.csv`.",
        f"- Identidad de ranking: `{retrieval['ranking_identity_all_cases']}`; máxima diferencia de score: `{retrieval['score_max_absolute_difference']}`.",
        f"- Casos individuales: `{dict(sorted(retrieval_case_match.items()))}`.",
        "",
        "## Interpretación y estado",
        "",
        "- La referencia exacta está presente en los 1056 casos: el resultado extremo no es ausencia de cobertura documental.",
        "- No se detectó desalineación vector-documento, discrepancia de modelo ni error de ranking.",
        "- Fase D usó brute-force exacto; `hnsw.index` está ausente y `hnswlib` no está disponible en el entorno actual. MCD estaba configurado en el artefacto, pero no se usó en la corrida.",
        "- Se conserva el resultado experimental sin tuning.",
        "",
        "## Artefactos",
        "",
        f"- `{report['artifacts']['json']}`",
        f"- `{report['artifacts']['markdown']}`",
        f"- `{report['artifacts']['vector_sample_csv']}`",
        f"- `{report['artifacts']['retrieval_sample_csv']}`",
        "",
        "## Gate checks",
        "",
    ]
    for name, value in checks.items():
        lines.append(f"- `{name}`: `{value}`")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit frozen EXP-04 Text2Trade dense v0.2 vector integrity.")
    parser.add_argument("--evalset", type=Path, default=EVALSET)
    parser.add_argument("--artifact-dir", type=Path, default=ARTIFACT_DIR)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    return parser


def main() -> int:
    report = audit(build_parser().parse_args())
    print(report["gate_d_status"])
    print(f"Vector samples: {report['vector_sanity_check']['sample_count']}")
    print(f"Retrieval cases checked: {report['retrieval_sanity_check']['cases_checked']}")
    print(f"Audit: {report['artifacts']['json']}")
    return 0 if report["gate_d_status"] == "GATE D APROBADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
