from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np


TEXT_FIELDS = ("texto_index", "texto", "text", "content", "descripcion")
CONTEXT_RE = re.compile(r"\bcontexto\s*:\s.*$", flags=re.IGNORECASE | re.DOTALL)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def normalize_code(value: object) -> str:
    return re.sub(r"\D", "", clean(value))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [{clean(key): clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def build_texto_index(texto: object) -> str:
    text = clean(texto)
    text = CONTEXT_RE.sub("", text).strip()
    return re.sub(r"\s+", " ", text).strip()


def pick_text_field(row: Mapping[str, Any]) -> tuple[str, str]:
    for field in TEXT_FIELDS:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return field, value
    return "fallback", "\n".join(value for value in row.values() if isinstance(value, str) and len(value) > 20)


def build_document_text(row: Mapping[str, Any]) -> tuple[str, dict[str, Any]]:
    title = row.get("titulo") if isinstance(row.get("titulo"), str) else ""
    used_field, main_text = pick_text_field(row)
    text = (title.strip() + "\n" + main_text.strip()).strip() if title.strip() else main_text.strip()
    return text, {"text_field_used": used_field, "has_title": bool(title.strip())}


def build_normative_documents(corpus_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source_index, row in enumerate(corpus_rows):
        code = clean(row.get("codigo"))
        if clean(row.get("tipo")) != "nandina_8" or not re.fullmatch(r"\d{8}", code) or code in seen:
            continue
        seen.add(code)
        text, aux = build_document_text(row)
        documents.append(
            {
                "doc_id": f"NANDINA:{code}",
                "tipo": "nandina_8",
                "codigo": code,
                "titulo": clean(row.get("titulo")),
                "texto_index": text,
                "fuente": "corpus_rag_v1_index.jsonl",
                "offsets": {"source_row": source_index, "document_index": len(documents)},
                "aux": aux,
            }
        )
    return documents


def historical_code_pools(historical_rows: Sequence[Mapping[str, str]], label_column: str) -> list[str]:
    return sorted({normalize_code(row[label_column]) for row in historical_rows if normalize_code(row[label_column])})


def choose_hard_negative(case_id: str, positive_code: str, training_codes: Sequence[str]) -> tuple[str, str]:
    same_hs4 = [code for code in training_codes if code != positive_code and code[:4] == positive_code[:4]]
    same_chapter = [code for code in training_codes if code != positive_code and code[:2] == positive_code[:2]]
    other = [code for code in training_codes if code != positive_code]
    pools = (("same_hs4_different_code", same_hs4), ("same_chapter_different_code", same_chapter), ("other_historical_code", other))
    for level, pool in pools:
        if pool:
            index = int(hashlib.sha256(case_id.encode("utf-8")).hexdigest(), 16) % len(pool)
            return pool[index], level
    raise ValueError(f"No negative available for {case_id} / {positive_code}")


def order_rows_for_unique_positive_batches(rows: Sequence[dict[str, Any]], batch_size: int) -> list[dict[str, Any]]:
    """Round-robin labels so explicit MNRL positives do not repeat in a batch."""
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in sorted(rows, key=lambda item: (item["positive_code"], item["case_id"])):
        buckets[row["positive_code"]].append(row)
    codes = sorted(buckets)
    ordered: list[dict[str, Any]] = []
    cursor = 0
    while any(buckets.values()):
        batch: list[dict[str, Any]] = []
        for offset in range(len(codes)):
            code = codes[(cursor + offset) % len(codes)]
            if buckets[code]:
                batch.append(buckets[code].pop(0))
            if len(batch) == batch_size:
                break
        if not batch:
            break
        ordered.extend(batch)
        cursor = (cursor + len(batch)) % len(codes)
    return ordered


def sample_indices(documents: Sequence[Mapping[str, Any]], eval_rows: Sequence[Mapping[str, str]], label_column: str) -> dict[int, list[str]]:
    reasons: dict[int, list[str]] = defaultdict(list)

    def add(index: int, reason: str) -> None:
        reasons[index].append(reason)

    for index in (0, 1, 2, len(documents) - 3, len(documents) - 2, len(documents) - 1):
        add(index, "first_or_last_3")
    for i in range(10):
        add(((i + 1) * len(documents)) // 11, "distributed_10")
    by_code = {clean(doc.get("codigo")): index for index, doc in enumerate(documents)}
    for code in sorted({normalize_code(row[label_column]) for row in eval_rows})[:5]:
        if code in by_code:
            add(by_code[code], f"evalset_reference_code:{code}")
    return {index: sorted(set(values)) for index, values in sorted(reasons.items())}


def vector_integrity_rows(
    model: Any,
    vectors: np.ndarray,
    documents: Sequence[Mapping[str, Any]],
    id_map: Mapping[str, Mapping[str, Any]],
    eval_rows: Sequence[Mapping[str, str]],
    label_column: str,
) -> list[dict[str, Any]]:
    selected = sample_indices(documents, eval_rows, label_column)
    indices = list(selected)
    texts = [clean(documents[index].get("texto_index")) for index in indices]
    rebuilt = model.encode(texts, batch_size=32, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False).astype(np.float32)
    stored = np.asarray(vectors[indices], dtype=np.float32)
    rows = []
    for offset, index in enumerate(indices):
        current = rebuilt[offset]
        original = stored[offset]
        diff = current.astype(np.float64) - original.astype(np.float64)
        current_norm = float(np.linalg.norm(current))
        original_norm = float(np.linalg.norm(original))
        cosine = float(np.dot(current.astype(np.float64), original.astype(np.float64)) / (current_norm * original_norm))
        mapped = id_map[str(index)]
        rows.append(
            {
                "vector_index": index,
                "doc_id": clean(mapped.get("doc_id")),
                "nandina": clean(mapped.get("codigo")),
                "selection_reasons": "|".join(selected[index]),
                "stored_text_sha256": hashlib.sha256(texts[offset].encode("utf-8")).hexdigest(),
                "cosine_similarity_reconstructed_stored": cosine,
                "max_absolute_difference": float(np.max(np.abs(diff))),
                "l2_difference": float(np.linalg.norm(diff)),
                "byte_exact_float32": bool(np.array_equal(current, original)),
            }
        )
    return rows


def model_file_manifest(model_dir: Path, root: Path) -> list[dict[str, Any]]:
    return [
        {"path": relative(path, root), "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in sorted(model_dir.rglob("*"))
        if path.is_file()
    ]
