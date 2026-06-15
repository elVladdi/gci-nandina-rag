from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass(frozen=True)
class DenseText2TradeArtifacts:
    artifact_dir: Path
    vectors_path: Path
    id_map_path: Path
    docstore_path: Path
    config_path: Path
    metadata_path: Path
    model_path: Path


def default_artifacts(artifact_dir: str | Path) -> DenseText2TradeArtifacts:
    base = Path(artifact_dir)
    return DenseText2TradeArtifacts(
        artifact_dir=base,
        vectors_path=base / "index" / "vectors.npy",
        id_map_path=base / "index" / "id_map.json",
        docstore_path=base / "store" / "nandina8_docstore.jsonl",
        config_path=base / "retrieval_config.json",
        metadata_path=base / "text2trade_nandina8_run_metadata.json",
        model_path=base / "model",
    )


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _normalize_rows(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0.0] = 1.0
    return matrix / norms


class DenseText2TradeRetriever:
    """Brute-force dense retriever over frozen Text2Trade vectors."""

    def __init__(
        self,
        artifact_dir: str | Path,
        model_path: str | Path | None = None,
        *,
        load_model: bool = True,
        mmap_vectors: bool = True,
    ) -> None:
        self.artifacts = default_artifacts(artifact_dir)
        self.config: dict[str, Any] = _load_json(self.artifacts.config_path)
        self.metadata: dict[str, Any] = _load_json(self.artifacts.metadata_path)
        self.id_map: dict[str, dict[str, Any]] = _load_json(self.artifacts.id_map_path)
        self.docstore: list[dict[str, Any]] = _load_jsonl(self.artifacts.docstore_path)

        mmap_mode = "r" if mmap_vectors else None
        self.vectors = np.load(self.artifacts.vectors_path, mmap_mode=mmap_mode)
        if self.vectors.ndim != 2:
            raise ValueError(f"Expected 2D vectors matrix, got shape={self.vectors.shape}")
        if len(self.id_map) != self.vectors.shape[0] or len(self.docstore) != self.vectors.shape[0]:
            raise ValueError(
                "Inconsistent dense artifacts: "
                f"vectors={self.vectors.shape[0]}, id_map={len(self.id_map)}, docstore={len(self.docstore)}"
            )

        retriever_cfg = self.config.get("retriever", {})
        self.embedding_normalize = bool(retriever_cfg.get("embedding_normalize", True))
        self.model_path = Path(model_path) if model_path else self.artifacts.model_path
        self.model: SentenceTransformer | None = None
        if load_model:
            self.model = SentenceTransformer(str(self.model_path))

    @property
    def docs_count(self) -> int:
        return int(self.vectors.shape[0])

    @property
    def embedding_dim(self) -> int:
        return int(self.vectors.shape[1])

    def artifact_summary(self) -> dict[str, Any]:
        return {
            "artifact_dir": str(self.artifacts.artifact_dir),
            "vectors_path": str(self.artifacts.vectors_path),
            "id_map_path": str(self.artifacts.id_map_path),
            "docstore_path": str(self.artifacts.docstore_path),
            "model_path": str(self.model_path),
            "docs_count": self.docs_count,
            "embedding_dim": self.embedding_dim,
            "embedding_normalize": self.embedding_normalize,
            "retrieval_mode": "brute_force_dot_product_cosine_on_normalized_vectors",
            "uses_hnsw": False,
            "uses_llm": False,
        }

    def encode_query(self, query: str) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("Model was not loaded; initialize with load_model=True to encode queries.")
        embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=self.embedding_normalize,
            show_progress_bar=False,
        )[0]
        return np.asarray(embedding, dtype=np.float32)

    def retrieve(self, query: str, top_k: int = 10, *, query_embedding: np.ndarray | None = None) -> list[dict[str, Any]]:
        if top_k <= 0:
            raise ValueError("top_k must be positive")
        q = query_embedding if query_embedding is not None else self.encode_query(query)
        q = np.asarray(q, dtype=np.float32)
        if q.ndim != 1 or q.shape[0] != self.embedding_dim:
            raise ValueError(f"Expected query embedding shape ({self.embedding_dim},), got {q.shape}")
        if not self.embedding_normalize:
            q = _normalize_rows(q.reshape(1, -1))[0].astype(np.float32)

        scores = np.asarray(self.vectors @ q, dtype=np.float32)
        k = min(top_k, scores.shape[0])
        candidate_idx = np.argpartition(-scores, kth=k - 1)[:k]
        ordered_idx = candidate_idx[np.argsort(-scores[candidate_idx])]

        hits: list[dict[str, Any]] = []
        for rank, idx in enumerate(ordered_idx, start=1):
            doc = self.docstore[int(idx)]
            mapped = self.id_map.get(str(int(idx)), {})
            code = str(mapped.get("codigo") or doc.get("codigo") or "")
            text = str(doc.get("texto_index") or doc.get("texto") or doc.get("text") or "")
            hits.append(
                {
                    "rank": rank,
                    "doc_idx": int(idx),
                    "doc_id": str(mapped.get("doc_id") or doc.get("doc_id") or ""),
                    "code": code,
                    "score": float(scores[int(idx)]),
                    "text": text,
                    "title": str(doc.get("titulo") or ""),
                    "metadata": {
                        "tipo": doc.get("tipo"),
                        "fuente": doc.get("fuente"),
                        "offsets": doc.get("offsets"),
                        "aux": doc.get("aux"),
                    },
                }
            )
        return hits


def retrieve(
    retriever: DenseText2TradeRetriever,
    query: str,
    top_n: int = 10,
    *,
    query_embedding: np.ndarray | None = None,
) -> list[dict[str, Any]]:
    return retriever.retrieve(query, top_k=top_n, query_embedding=query_embedding)
