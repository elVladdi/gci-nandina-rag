from __future__ import annotations

import argparse
import json
import os
import platform
import random
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch
from sentence_transformers import InputExample, SentenceTransformer
from sentence_transformers.sentence_transformer import losses
from torch.utils.data import DataLoader, Sampler
from transformers import get_linear_schedule_with_warmup

from ..retrieval.text2trade_mnrl_v02 import (
    build_normative_documents,
    choose_hard_negative,
    clean,
    historical_code_pools,
    load_json,
    load_jsonl,
    model_file_manifest,
    normalize_code,
    rows_by_unique_positive_batches,
    read_csv,
    relative,
    sha256_file,
    write_json,
)
from ..utils.paths import project_root, resolve_project_path


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


def assert_hash(path: Path, expected: str) -> None:
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"Frozen input hash mismatch for {path}: {actual} != {expected}")


class StaticBatchSampler(Sampler[list[int]]):
    def __init__(self, batches: list[list[int]]) -> None:
        self.batches = batches

    def __iter__(self):
        return iter(self.batches)

    def __len__(self) -> int:
        return len(self.batches)


def main() -> int:
    parser = argparse.ArgumentParser(description="Train D1a Text2Trade-inspired MNRL retriever from approved historical v0.2 only.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/text2trade_mnrl_v0.2.json"))
    args = parser.parse_args()
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    frozen = config["frozen_inputs"]
    training = config["training"]
    columns = config["columns"]
    historical_path = resolve_project_path(frozen["historical_csv"])
    eval_path = resolve_project_path(frozen["eval_csv"])
    corpus_path = resolve_project_path(frozen["normative_corpus"])
    base_model_path = resolve_project_path(config["base_model"]["local_path"])
    model_dir = resolve_project_path(config["outputs"]["model_dir"])
    training_dir = resolve_project_path(config["outputs"]["training_dir"])
    if model_dir.exists():
        raise FileExistsError(f"Refusing to overwrite model artifact: {model_dir}")
    assert_hash(historical_path, frozen["historical_sha256"])
    assert_hash(eval_path, frozen["eval_sha256"])
    assert_hash(corpus_path, frozen["normative_corpus_sha256"])
    assert_hash(base_model_path / "model.safetensors", config["base_model"]["model_safetensors_sha256"])

    historical_rows = read_csv(historical_path)
    eval_rows = read_csv(eval_path)
    corpus_rows = load_jsonl(corpus_path)
    documents = build_normative_documents(corpus_rows)
    docs_by_code = {clean(document["codigo"]): document for document in documents}
    training_codes = historical_code_pools(historical_rows, columns["label"])
    eval_codes = {normalize_code(row[columns["label"]]) for row in eval_rows}
    historical_dams = {clean(row[columns["dam"]]) for row in historical_rows}
    eval_dams = {clean(row[columns["dam"]]) for row in eval_rows}
    historical_ids = {clean(row[columns["id"]]) for row in historical_rows}
    eval_ids = {clean(row[columns["id"]]) for row in eval_rows}
    historical_cases = {clean(row["case_id"]) for row in historical_rows}
    eval_cases = {clean(row["case_id"]) for row in eval_rows}
    if historical_dams & eval_dams or historical_ids & eval_ids or historical_cases & eval_cases:
        raise ValueError("Leakage guard failed: historical and eval split overlap")

    records: list[dict[str, Any]] = []
    negative_levels: Counter[str] = Counter()
    duplicate_descriptions = Counter(clean(row[columns["query"]]).casefold() for row in historical_rows)
    for row in historical_rows:
        case_id = clean(row["case_id"])
        query = clean(row[columns["query"]])
        positive_code = normalize_code(row[columns["label"]])
        if not query:
            raise ValueError(f"Empty historical query: {case_id}")
        if positive_code not in docs_by_code:
            raise ValueError(f"Missing normative positive for {case_id}: {positive_code}")
        negative_code, level = choose_hard_negative(case_id, positive_code, training_codes)
        if negative_code not in docs_by_code:
            raise ValueError(f"Missing normative negative for {case_id}: {negative_code}")
        records.append(
            {
                "case_id": case_id,
                "query": query,
                "positive_code": positive_code,
                "positive_text": clean(docs_by_code[positive_code]["texto_index"]),
                "negative_code": negative_code,
                "negative_text": clean(docs_by_code[negative_code]["texto_index"]),
                "negative_level": level,
            }
        )
        negative_levels[level] += 1
    batches = rows_by_unique_positive_batches(records, int(training["batch_size"]))
    if any(len({row["positive_code"] for row in batch}) != len(batch) for batch in batches):
        raise ValueError("MNRL batch construction repeated a positive code")

    set_seed(int(training["seed"]))
    model = SentenceTransformer(str(base_model_path), device=training["device"])
    model.max_seq_length = int(training["max_sequence_length"])
    ordered_records = [row for batch in batches for row in batch]
    examples = [InputExample(texts=[row["query"], row["positive_text"], row["negative_text"]]) for row in ordered_records]
    batch_indices: list[list[int]] = []
    offset = 0
    for batch in batches:
        batch_indices.append(list(range(offset, offset + len(batch))))
        offset += len(batch)
    loader = DataLoader(examples, batch_sampler=StaticBatchSampler(batch_indices), collate_fn=model.smart_batching_collate)
    loss = losses.MultipleNegativesRankingLoss(model, scale=float(training["mnrl_scale"]))
    total_steps = len(loader) * int(training["epochs"])
    warmup_steps = int(total_steps * float(training["warmup_ratio"]))
    if training_dir.exists() and any(training_dir.iterdir()):
        raise FileExistsError(f"Refusing to overwrite training metadata: {training_dir}")
    training_dir.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(training["learning_rate"]), weight_decay=float(training["weight_decay"]))
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)
    loss_values: list[float] = []
    model.train()
    for epoch in range(int(training["epochs"])):
        for sentence_features, labels in loader:
            sentence_features = [{key: value.to(model.device) for key, value in features.items()} for features in sentence_features]
            labels = labels.to(model.device)
            optimizer.zero_grad(set_to_none=True)
            value = loss(sentence_features, labels)
            value.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), float(training["max_grad_norm"]))
            optimizer.step()
            scheduler.step()
            loss_values.append(float(value.detach().cpu()))
        print(f"epoch={epoch + 1} mean_mnrl_loss={sum(loss_values) / len(loss_values):.8f}")
    model.save(str(model_dir))
    finished = datetime.now(timezone.utc)
    metadata = {
        "experiment_id": config["experiment_id"],
        "variant": "D1a",
        "method_label": config["method_label"],
        "command": "python -B -m src.experiments.train_text2trade_mnrl_v02",
        "started_at_utc": started.isoformat(),
        "finished_at_utc": finished.isoformat(),
        "config": {"path": relative(config_path, root), "sha256": sha256_file(config_path)},
        "inputs": {
            "historical": {"path": relative(historical_path, root), "sha256": sha256_file(historical_path), "rows": len(historical_rows)},
            "eval": {"path": relative(eval_path, root), "sha256": sha256_file(eval_path), "rows": len(eval_rows), "used_for_training": False},
            "corpus": {"path": relative(corpus_path, root), "sha256": sha256_file(corpus_path), "normative_documents": len(documents)},
            "base_model": {"path": relative(base_model_path, root), "files": model_file_manifest(base_model_path, root)},
        },
        "leakage_audit": {
            "dam_overlap_historical_eval": len(historical_dams & eval_dams),
            "id_overlap_historical_eval": len(historical_ids & eval_ids),
            "case_overlap_historical_eval": len(historical_cases & eval_cases),
            "eval_labels_used_for_training": False,
            "eval_metric_used_for_selection": False,
            "eval_codes_not_used_to_generate_negatives": True,
        },
        "pairs": {
            "historical_rows": len(records),
            "historical_unique_codes": len(training_codes),
            "normative_positive_rows": len(records),
            "missing_normative_positive_rows": 0,
            "duplicate_normalized_description_groups": sum(count > 1 for count in duplicate_descriptions.values()),
            "duplicate_normalized_description_extra_rows": sum(count - 1 for count in duplicate_descriptions.values() if count > 1),
            "negative_level_counts": dict(sorted(negative_levels.items())),
            "negative_source": "historical training codes + frozen normative corpus only",
            "batch_count": len(batches),
            "positive_codes_unique_within_every_batch": True,
        },
        "training": {**training, "warmup_steps": warmup_steps, "total_steps": total_steps, "loss_first": loss_values[0], "loss_last": loss_values[-1], "loss_mean": sum(loss_values) / len(loss_values)},
        "runtime": {"python": platform.python_version(), "platform": platform.platform(), "torch": torch.__version__},
        "outputs": {"model_dir": relative(model_dir, root), "model_files": model_file_manifest(model_dir, root)},
        "mcd_used": False,
        "phase_e_started": False,
    }
    write_json(training_dir / "training_metadata.json", metadata)
    print("OK: D1a MNRL training completed")
    print(f"Model: {metadata['outputs']['model_dir']}")
    print(f"Pairs: {len(records)}; steps: {total_steps}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
