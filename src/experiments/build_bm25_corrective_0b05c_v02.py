"""Prospective BM25 builders for the isolated 0B-05C v0.2 gate."""

from __future__ import annotations

import argparse
import json
import pickle
from pathlib import Path
from typing import Any

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from .build_bm25_ev03_historical_recovered_v02 import (
    TOKEN_POLICY,
    build_ev03_recovered_historical_from_corpus,
)
from .prepare_0b05c_corrective_numerical_gate_v02 import ContractViolation, require


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path("src/configs/experiment_config.json")
ARM_SEMANTICS = {
    "EV03": {
        "token_policy": TOKEN_POLICY,
        "builder": "build_ev03_recovered_historical_from_corpus",
        "global_builder_direct_use": False,
        "kwargs": {},
    },
    "EV04": {
        "token_policy": "ORIGINAL_HIERARCHICAL_V0.1",
        "builder": "build_bm25_from_corpus",
        "inherits_ev03_policy": False,
        "kwargs": {
            "type_field": "tipo",
            "code_field": "codigo",
            "title_field": "titulo",
            "text_field": "texto_index_jerarquico",
            "fallback_text_field": "texto_index",
            "target_type": "nandina_8",
            "enforce_8_digits": True,
        },
    },
}


def build(arm: str, corpus_path: Path, output_path: Path, metadata_path: Path, *, root: Path = ROOT) -> dict[str, Any]:
    require(arm in ARM_SEMANTICS, f"Unsupported arm: {arm}")
    corpus_path = corpus_path if corpus_path.is_absolute() else root / corpus_path
    output_path = output_path if output_path.is_absolute() else root / output_path
    metadata_path = metadata_path if metadata_path.is_absolute() else root / metadata_path
    require(corpus_path.is_file(), f"Corpus missing: {corpus_path}")
    require(not output_path.exists() and not metadata_path.exists(), "Builder refuses overwrite or resume")
    config = json.loads((root / CONFIG_PATH).read_text(encoding="utf-8"))
    k1, b = float(config["bm25"]["k1"]), float(config["bm25"]["b"])
    require((k1, b) == (1.5, 0.75), "Frozen BM25 parameters changed")
    rows = read_jsonl(corpus_path)
    if arm == "EV03":
        index, stats = build_ev03_recovered_historical_from_corpus(rows, k1=k1, b=b)
    else:
        index, stats = build_bm25_from_corpus(rows, k1=k1, b=b, stopwords=DEFAULT_STOPWORDS_ES, **ARM_SEMANTICS[arm]["kwargs"])
    output_path.parent.mkdir(parents=True, exist_ok=False)
    with output_path.open("xb") as handle:
        pickle.dump(index, handle)
    metadata = {
        "artifact_id": f"0b05c_{arm.lower()}_corrective_bm25_index_v0.2",
        "arm": arm,
        "semantics": ARM_SEMANTICS[arm],
        "bm25_params": {"k1": k1, "b": b},
        "input_sha256": sha256_file(corpus_path),
        "index_sha256": sha256_file(output_path),
        "index_stats": stats,
        "identity_policy": "DERIVED_ONLY_AT_FUTURE_AUTHORIZED_EXECUTION",
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return metadata


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm", choices=("EV03", "EV04"), required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    args = parser.parse_args(argv)
    print(json.dumps(build(args.arm, args.corpus, args.output, args.metadata), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
