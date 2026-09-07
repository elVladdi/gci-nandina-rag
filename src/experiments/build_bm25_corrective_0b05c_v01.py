"""Prospective BM25 builder bound to the 0B-05C corrective gate.

It deliberately shares ``build_bm25_from_corpus`` and the frozen Spanish
stopword policy with the versioned production builders.  The runner is the
only supported entry point for a real execution; this module has no implicit
or resume mode and refuses to overwrite an artifact.
"""

from __future__ import annotations

import argparse
import json
import pickle
from pathlib import Path
from typing import Any, Mapping

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from .run_d1a_corrective_0b05c_v01 import ContractViolation, require


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path("src/configs/experiment_config.json")

ARM_SEMANTICS: dict[str, Mapping[str, Any]] = {
    "EV03": {
        "builder_source": "src/experiments/build_bm25_index.py",
        "kwargs": {},
        "ranking_unit": "NANDINA-8 document",
    },
    "EV04": {
        "builder_source": "src/experiments/build_bm25_hierarchical_index.py",
        "kwargs": {
            "type_field": "tipo",
            "code_field": "codigo",
            "title_field": "titulo",
            "text_field": "texto_index_jerarquico",
            "fallback_text_field": "texto_index",
            "target_type": "nandina_8",
            "enforce_8_digits": True,
        },
        "ranking_unit": "unique NANDINA-8 code after the frozen hierarchical collapse rule",
    },
}


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ContractViolation(f"Corrective builder path escapes repository: {path}") from exc


def _read_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build(
    arm: str,
    corpus_path: Path,
    output_path: Path,
    metadata_path: Path,
    *,
    config_path: Path = CONFIG_PATH,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Build one derived index with frozen BM25 semantics and POSIX metadata."""

    require(arm in ARM_SEMANTICS, f"Unsupported corrective arm: {arm}")
    corpus_path = (root / corpus_path).resolve() if not corpus_path.is_absolute() else corpus_path.resolve()
    output_path = (root / output_path).resolve() if not output_path.is_absolute() else output_path.resolve()
    metadata_path = (root / metadata_path).resolve() if not metadata_path.is_absolute() else metadata_path.resolve()
    config_path = (root / config_path).resolve() if not config_path.is_absolute() else config_path.resolve()
    for path in (corpus_path, config_path):
        require(path.is_file(), f"Corrective builder input is missing: {_relative(path, root)}")
    for path in (output_path, metadata_path):
        require(not path.exists(), f"Corrective builder refuses overwrite or resume: {_relative(path, root)}")

    config = _read_config(config_path)
    bm25_config = config.get("bm25", {})
    k1 = float(bm25_config.get("k1", 1.5))
    b = float(bm25_config.get("b", 0.75))
    require((k1, b) == (1.5, 0.75), "Corrective builder rejects a change to frozen BM25 k1/b")
    rows = read_jsonl(corpus_path)
    index, stats = build_bm25_from_corpus(
        rows,
        k1=k1,
        b=b,
        stopwords=DEFAULT_STOPWORDS_ES,
        **dict(ARM_SEMANTICS[arm]["kwargs"]),
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("xb") as handle:
        pickle.dump(index, handle)
    metadata: dict[str, Any] = {
        "artifact_id": f"0b05c_{arm.lower()}_corrective_bm25_index_v0.1",
        "identity_policy": "DERIVED_AT_AUTHORIZED_EXECUTION",
        "script": "src/experiments/build_bm25_corrective_0b05c_v01.py",
        "frozen_semantics_source": ARM_SEMANTICS[arm]["builder_source"],
        "arm": arm,
        "input": {"corpus_path": _relative(corpus_path, root), "corpus_sha256": sha256_file(corpus_path), "config_path": _relative(config_path, root), "config_sha256": sha256_file(config_path)},
        "bm25_params": {"k1": index.k1, "b": index.b, "use_stopwords": True, "stopwords_source": "src.bm25_index.DEFAULT_STOPWORDS_ES", "ranking_unit": ARM_SEMANTICS[arm]["ranking_unit"]},
        "index_stats": stats,
        "output": {"bm25_index_path": _relative(output_path, root), "bm25_index_sha256": sha256_file(output_path), "metadata_path": _relative(metadata_path, root)},
    }
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    with metadata_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a prospective 0B-05C corrective BM25 index.")
    parser.add_argument("--arm", choices=sorted(ARM_SEMANTICS), required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=CONFIG_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    metadata = build(args.arm, args.corpus, args.output, args.metadata, config_path=args.config)
    print(json.dumps(metadata, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
