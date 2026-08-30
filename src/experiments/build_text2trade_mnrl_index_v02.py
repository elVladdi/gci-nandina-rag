from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

from ..retrieval.text2trade_mnrl_v02 import (
    build_normative_documents,
    load_json,
    load_jsonl,
    model_file_manifest,
    read_csv,
    relative,
    sha256_file,
    vector_integrity_rows,
    write_csv,
    write_json,
)
from ..utils.paths import project_root, resolve_project_path


def assert_hash(path: Path, expected: str) -> None:
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"Frozen input hash mismatch for {path}: {actual} != {expected}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild D1a normalized NANDINA-8 dense vectors from the final MNRL model.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/text2trade_mnrl_v0.2.json"))
    args = parser.parse_args()
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    frozen = config["frozen_inputs"]
    index_config = config["index"]
    columns = config["columns"]
    corpus_path = resolve_project_path(frozen["normative_corpus"])
    eval_path = resolve_project_path(frozen["eval_csv"])
    model_dir = resolve_project_path(config["outputs"]["model_dir"])
    artifact_dir = resolve_project_path(index_config["output_dir"])
    if artifact_dir.exists():
        raise FileExistsError(f"Refusing to overwrite D1a index artifact: {artifact_dir}")
    if not model_dir.exists():
        raise FileNotFoundError(f"Final D1a model missing: {model_dir}")
    assert_hash(corpus_path, frozen["normative_corpus_sha256"])
    assert_hash(eval_path, frozen["eval_sha256"])

    corpus_rows = load_jsonl(corpus_path)
    documents = build_normative_documents(corpus_rows)
    if len(documents) != 7644 or len({document["codigo"] for document in documents}) != 7644:
        raise ValueError("Expected exactly 7644 unique NANDINA-8 normative documents")
    model = SentenceTransformer(str(model_dir), device=config["training"]["device"])
    model.max_seq_length = int(config["training"]["max_sequence_length"])
    texts = [document["texto_index"] for document in documents]
    vectors = model.encode(
        texts,
        batch_size=32,
        convert_to_numpy=True,
        normalize_embeddings=bool(index_config["normalize_embeddings"]),
        show_progress_bar=True,
    ).astype(np.float32)
    if vectors.shape != (7644, 384) or vectors.dtype != np.float32:
        raise ValueError(f"Unexpected D1a vectors shape/dtype: {vectors.shape} / {vectors.dtype}")

    index_dir = artifact_dir / "index"
    store_dir = artifact_dir / "store"
    index_dir.mkdir(parents=True)
    store_dir.mkdir(parents=True)
    vectors_path = index_dir / "vectors.npy"
    docstore_path = store_dir / "nandina8_docstore.jsonl"
    id_map_path = index_dir / "id_map.json"
    np.save(vectors_path, vectors)
    with docstore_path.open("w", encoding="utf-8", newline="\n") as handle:
        for document in documents:
            handle.write(json.dumps(document, ensure_ascii=False) + "\n")
    id_map = {str(index): {"doc_id": document["doc_id"], "codigo": document["codigo"]} for index, document in enumerate(documents)}
    write_json(id_map_path, id_map)

    eval_rows = read_csv(eval_path)
    integrity_rows = vector_integrity_rows(model, vectors, documents, id_map, eval_rows, columns["label"])
    epsilon = float(8 * np.finfo(np.float32).eps)
    integrity_pass = all(
        row["cosine_similarity_reconstructed_stored"] >= 1.0 - epsilon
        and row["max_absolute_difference"] <= epsilon
        for row in integrity_rows
    )
    integrity_csv = artifact_dir / "vector_integrity_sample_v0.2.csv"
    write_csv(integrity_csv, integrity_rows, list(integrity_rows[0]))

    retrieval_config_path = artifact_dir / "retrieval_config.json"
    artifact_metadata_path = artifact_dir / "text2trade_mnrl_nandina8_v02_run_metadata.json"
    retrieval_config = {
        "artifact_name": "text2trade_mnrl_nandina8_v0.2",
        "variant": "D1a",
        "retriever": {
            "family": "Text2Trade-inspired MNRL dense retrieval",
            "model": config["base_model"]["model_id"],
            "fine_tuned_model_path": relative(model_dir, root),
            "embedding_normalize": bool(index_config["normalize_embeddings"]),
            "batch_size": 32,
            "max_sequence_length": model.max_seq_length,
        },
        "index": {"backend": "exact", "score": "dot product over normalized float32 vectors", "hnsw": False},
        "mcd": {"enabled": False, "variant": "D1b not executed"},
        "document_text": config["document_text"],
    }
    write_json(retrieval_config_path, retrieval_config)
    integrity = {
        "gate": "D1a vector integrity before eval",
        "status": "PASS" if integrity_pass else "FAIL",
        "criterion": "cosine within 8 float32 machine epsilons of identity and maximum component difference within 8 float32 machine epsilons",
        "float32_epsilon": float(np.finfo(np.float32).eps),
        "tolerance": epsilon,
        "sample_count": len(integrity_rows),
        "byte_exact_count": sum(row["byte_exact_float32"] for row in integrity_rows),
        "cosine_min": min(row["cosine_similarity_reconstructed_stored"] for row in integrity_rows),
        "cosine_max": max(row["cosine_similarity_reconstructed_stored"] for row in integrity_rows),
        "max_absolute_difference": max(row["max_absolute_difference"] for row in integrity_rows),
        "max_l2_difference": max(row["l2_difference"] for row in integrity_rows),
        "sample_csv": relative(integrity_csv, root),
        "sample_csv_sha256": sha256_file(integrity_csv),
    }
    integrity_path = artifact_dir / "vector_integrity_gate_v0.2.json"
    write_json(integrity_path, integrity)
    metadata = {
        "experiment_id": config["experiment_id"],
        "variant": "D1a",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python -B -m src.experiments.build_text2trade_mnrl_index_v02",
        "config": {"path": relative(config_path, root), "sha256": sha256_file(config_path)},
        "inputs": {
            "corpus": {"path": relative(corpus_path, root), "sha256": sha256_file(corpus_path), "rows": len(corpus_rows)},
            "model": {"path": relative(model_dir, root), "files": model_file_manifest(model_dir, root)},
            "evalset_for_integrity_sampling_only": {"path": relative(eval_path, root), "sha256": sha256_file(eval_path), "used_for_training": False},
        },
        "artifacts": {
            "vectors": {"path": relative(vectors_path, root), "sha256": sha256_file(vectors_path), "shape": list(vectors.shape), "dtype": str(vectors.dtype)},
            "docstore": {"path": relative(docstore_path, root), "sha256": sha256_file(docstore_path), "records": len(documents)},
            "id_map": {"path": relative(id_map_path, root), "sha256": sha256_file(id_map_path), "records": len(id_map)},
            "retrieval_config": {"path": relative(retrieval_config_path, root), "sha256": sha256_file(retrieval_config_path)},
            "vector_integrity_gate": {"path": relative(integrity_path, root), "sha256": sha256_file(integrity_path), **integrity},
        },
        "mapping": {
            "vectors_documents_codes": [len(vectors), len(documents), len({document["codigo"] for document in documents})],
            "id_map_matches_docstore": all(id_map[str(index)]["codigo"] == document["codigo"] and id_map[str(index)]["doc_id"] == document["doc_id"] for index, document in enumerate(documents)),
            "source_order": "corpus_rag_v1_index.jsonl filtered in file order to nandina_8, first-code deduplication",
        },
        "validation": {"vector_integrity_pass": integrity_pass, "hnsw_built": False, "mcd_used": False, "phase_e_started": False},
    }
    write_json(artifact_metadata_path, metadata)
    print(f"D1a vector integrity: {integrity['status']}")
    print(f"Index: {relative(artifact_dir, root)}")
    return 0 if integrity_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
