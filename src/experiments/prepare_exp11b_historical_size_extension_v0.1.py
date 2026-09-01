"""Freeze the expanded eligible pool and prospectively plan EXP-11B sizes.

This module is deliberately limited to pool integrity, complete-DAM planning,
and text-overlap sensitivity masks. It does not construct H150/H200 banks or
run any retrieval or model evaluation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
GATE_DIR = Path("outputs/audits/new_historical_gate_v0.1")
INTERIM_DIR = Path("data/interim/new_historical_gate_v0.1")
H100_PATH = Path("data/processed/data_aduanas_historico_clase87_v0.2.csv")
EVAL_PATH = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DESCRIPTION = "DESCRIPCION DE MERCANCIAS CONCATENADA"
DAM = "DECLARACION"
NANDINA = "NANDINA"
CASE_ID = "case_id"

REAL_INGEST_ARTIFACTS = (
    INTERIM_DIR / "new_historical_normalized_all.csv",
    INTERIM_DIR / "new_historical_curated.csv",
    INTERIM_DIR / "new_historical_eligible.csv",
    GATE_DIR / "new_historical_exclusions.csv",
    GATE_DIR / "new_historical_frozen_overlap_audit.csv",
    GATE_DIR / "new_historical_duplicate_nearduplicate_audit.csv",
    GATE_DIR / "new_historical_ingestion_manifest.json",
    GATE_DIR / "new_historical_artifact_hashes.csv",
)
FREEZE_MANIFEST = GATE_DIR / "real_ingest_01_freeze_manifest_v0.1.json"
FREEZE_HASHES = GATE_DIR / "real_ingest_01_freeze_hashes_v0.1.csv"
FEASIBILITY = GATE_DIR / "exp11b_h150_h200_feasibility_v0.1.json"
COMMON_MASKS = GATE_DIR / "eval_common_clean_masks_v0.1.csv"
NEW_ELIGIBLE_PATH = INTERIM_DIR / "new_historical_eligible.csv"
SELECTION_BASELINE_COMMIT = "b3806190cb645d35c2a121c0f1d0c07fbfe21605"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def count_rows(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def relative(path: Path) -> str:
    return path.as_posix()


def artifact_inventory(root: Path, artifacts: Iterable[Path]) -> list[dict[str, Any]]:
    inventory = []
    for relative_path in artifacts:
        path = root / relative_path
        if not path.is_file():
            raise RuntimeError(f"Required Real Ingest 01 artifact is missing: {relative_path}")
        inventory.append(
            {
                "path": relative(relative_path),
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return inventory


def write_csv_bytes(fieldnames: list[str], rows: Iterable[dict[str, Any]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return buffer.getvalue().encode("utf-8")


def seeded_dam_order(dam_counts: dict[str, int], seed: int, namespace: str) -> list[str]:
    return sorted(
        dam_counts,
        key=lambda dam: (sha256_text(f"{seed}:{namespace}:{dam}"), dam),
    )


def composition_sha256(dams: Iterable[str]) -> str:
    return sha256_text(json.dumps(sorted(dams), ensure_ascii=True, separators=(",", ":")))


def choose_complete_dam_prefix(
    ordered_dams: list[str], dam_counts: dict[str, int], target_rows: int
) -> dict[str, Any]:
    if not ordered_dams:
        raise ValueError("Cannot choose a DAM prefix from an empty eligible pool")
    running_rows = 0
    candidates: list[dict[str, Any]] = []
    for prefix_length, dam in enumerate(ordered_dams, start=1):
        running_rows += dam_counts[dam]
        dams = ordered_dams[:prefix_length]
        candidates.append(
            {
                "dams": dams,
                "prefix_length": prefix_length,
                "realized_new_rows": running_rows,
                "absolute_deviation": abs(running_rows - target_rows),
                "composition_sha256": composition_sha256(dams),
            }
        )
    return min(
        candidates,
        key=lambda candidate: (
            candidate["absolute_deviation"],
            candidate["prefix_length"],
            candidate["composition_sha256"],
        ),
    )


def select_nested_prefixes(
    dam_counts: dict[str, int],
    seed: int,
    namespace: str,
    h150_target_increment: int,
    h200_target_increment: int,
) -> dict[str, Any]:
    """Select only from DAM identifiers and their row counts.

    Downstream descriptive summaries are intentionally outside this function.
    """
    if any(not dam or count <= 0 for dam, count in dam_counts.items()):
        raise ValueError("DAM identifiers and counts must be non-empty and positive")
    ordered_dams = seeded_dam_order(dam_counts, seed, namespace)
    h150 = choose_complete_dam_prefix(ordered_dams, dam_counts, h150_target_increment)
    h200 = choose_complete_dam_prefix(ordered_dams, dam_counts, h200_target_increment)
    h150_dams = set(h150["dams"])
    h200_dams = set(h200["dams"])
    return {
        "seed": seed,
        "namespace": namespace,
        "ordered_dams": ordered_dams,
        "H150": h150,
        "H200": h200,
        "h150_is_strict_subset_h200": h150_dams < h200_dams,
    }


def dam_counts_from_rows(rows: Iterable[dict[str, str]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        dam = row[DAM].strip()
        if not dam:
            raise ValueError("Eligible pool contains an empty DAM identifier")
        counts[dam] += 1
    return dict(counts)


def rows_for_dams(rows: list[dict[str, str]], dams: Iterable[str]) -> list[dict[str, str]]:
    selected_dams = set(dams)
    return [row for row in rows if row[DAM] in selected_dams]


def distribution_descriptor(rows: list[dict[str, str]]) -> dict[str, Any]:
    counts = Counter(row[DAM] for row in rows)
    total = len(rows)
    hhi = sum((count / total) ** 2 for count in counts.values()) if total else 0.0
    return {
        "rows": total,
        "dam_count": len(counts),
        "dam_hhi": hhi,
        "effective_dam_count": (1 / hhi) if hhi else 0.0,
        "largest_dam_rows": max(counts.values(), default=0),
        "largest_dam_share": (max(counts.values()) / total) if total else 0.0,
    }


def increment_descriptor(
    new_rows: list[dict[str, str]], dams: Iterable[str], h100_nandina: set[str]
) -> dict[str, Any]:
    selected_rows = rows_for_dams(new_rows, dams)
    selected_nandina = {row[NANDINA].strip() for row in selected_rows if row[NANDINA].strip()}
    return {
        **distribution_descriptor(selected_rows),
        "nandina_count": len(selected_nandina),
        "nandina_shared_with_h100_count": len(selected_nandina & h100_nandina),
        "nandina_new_vs_h100_count": len(selected_nandina - h100_nandina),
    }


def total_bank_descriptor(
    h100_rows: list[dict[str, str]],
    new_rows: list[dict[str, str]],
    dams: Iterable[str],
    h100_nandina: set[str],
) -> dict[str, Any]:
    total_rows = [*h100_rows, *rows_for_dams(new_rows, dams)]
    total_nandina = {row[NANDINA].strip() for row in total_rows if row[NANDINA].strip()}
    h100_covered = total_nandina & h100_nandina
    h100_denominator = 66
    if len(h100_nandina) != h100_denominator:
        raise RuntimeError("H100 NANDINA coverage denominator no longer matches the frozen contract")
    return {
        **distribution_descriptor(total_rows),
        "nandina_count": len(total_nandina),
        "H100_nandina_coverage_n": len(h100_covered),
        "H100_nandina_coverage_denominator": h100_denominator,
        "H100_nandina_coverage_pct": len(h100_covered) / h100_denominator * 100,
        "new_nandina_count": len(total_nandina - h100_nandina),
    }


def selection_identity(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "accepted_seed_schedule": payload["accepted_seed_schedule"],
        "accepted_replicates": [
            {
                "replicate_id": replicate["replicate_id"],
                "H150": {
                    field: replicate["H150"][field]
                    for field in ("composition_sha256", "dams", "realized_new_rows", "realized_total_rows")
                },
                "H200": {
                    field: replicate["H200"][field]
                    for field in ("composition_sha256", "dams", "realized_new_rows", "realized_total_rows")
                },
            }
            for replicate in payload["accepted_replicates"]
        ],
    }


def verify_selection_identity_against_baseline(root: Path, payload: dict[str, Any]) -> dict[str, Any]:
    try:
        baseline_bytes = subprocess.check_output(
            ["git", "show", f"{SELECTION_BASELINE_COMMIT}:{relative(FEASIBILITY)}"],
            cwd=root,
        )
    except subprocess.CalledProcessError as error:
        raise RuntimeError("Cannot read the frozen Gate 03 selection baseline") from error
    baseline = json.loads(baseline_bytes.decode("utf-8"))
    baseline_identity = selection_identity(baseline)
    current_identity = selection_identity(payload)
    if current_identity != baseline_identity:
        raise RuntimeError("EXP-11B selection identity differs from the approved Gate 03 baseline")
    return {
        "baseline_candidate_commit": SELECTION_BASELINE_COMMIT,
        "accepted_seed_schedule_identical": True,
        "replicate_fields_identical": {
            "H150_dams": True,
            "H150_composition_sha256": True,
            "H150_realized_rows": True,
            "H200_dams": True,
            "H200_composition_sha256": True,
            "H200_realized_rows": True,
        },
    }


def build_feasibility_evidence(
    config: dict[str, Any], new_rows: list[dict[str, str]], h100_rows: list[dict[str, str]]
) -> dict[str, Any]:
    selection = config["selection"]
    policy = config["replicate_policy"]
    h150_target = config["conditions"]["H150"]["target_new_rows"]
    h200_target = config["conditions"]["H200"]["target_new_rows"]
    tolerance = config["feasibility_contract"]["max_abs_new_row_deviation"]
    dam_counts = dam_counts_from_rows(new_rows)
    h100_nandina = {row[NANDINA].strip() for row in h100_rows if row[NANDINA].strip()}
    h100_dams = {row[DAM].strip() for row in h100_rows}
    new_dams = set(dam_counts)
    direct_dam_overlap = sorted(h100_dams & new_dams)
    if direct_dam_overlap:
        raise RuntimeError("Expanded eligible pool overlaps H100 DAM identifiers")
    accepted: list[dict[str, Any]] = []
    seen_h150: set[str] = set()
    seen_h200: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    rejection_counts: Counter[str] = Counter()
    evaluated = 0

    for seed in range(policy["seed_stream_start"], policy["seed_stream_start"] + policy["max_seed_candidates"]):
        evaluated += 1
        candidate = select_nested_prefixes(
            dam_counts,
            seed,
            selection["namespace"],
            h150_target,
            h200_target,
        )
        h150 = candidate["H150"]
        h200 = candidate["H200"]
        if h150["absolute_deviation"] > tolerance:
            rejection_counts["H150_tolerance"] += 1
            continue
        if h200["absolute_deviation"] > tolerance:
            rejection_counts["H200_tolerance"] += 1
            continue
        if not candidate["h150_is_strict_subset_h200"]:
            rejection_counts["strict_nesting"] += 1
            continue
        pair = (h150["composition_sha256"], h200["composition_sha256"])
        if h150["composition_sha256"] in seen_h150:
            rejection_counts["duplicate_H150_composition"] += 1
            continue
        if h200["composition_sha256"] in seen_h200:
            rejection_counts["duplicate_H200_composition"] += 1
            continue
        if pair in seen_pairs:
            rejection_counts["duplicate_nested_pair"] += 1
            continue
        seen_h150.add(h150["composition_sha256"])
        seen_h200.add(h200["composition_sha256"])
        seen_pairs.add(pair)
        accepted.append(
            {
                "replicate_id": f"R{len(accepted) + 1:02d}",
                "seed": seed,
                "H150": {
                    **h150,
                    "realized_total_rows": len(h100_rows) + h150["realized_new_rows"],
                    "increment_descriptor": increment_descriptor(new_rows, h150["dams"], h100_nandina),
                    "total_bank_descriptor": total_bank_descriptor(
                        h100_rows, new_rows, h150["dams"], h100_nandina
                    ),
                },
                "H200": {
                    **h200,
                    "realized_total_rows": len(h100_rows) + h200["realized_new_rows"],
                    "increment_descriptor": increment_descriptor(new_rows, h200["dams"], h100_nandina),
                    "total_bank_descriptor": total_bank_descriptor(
                        h100_rows, new_rows, h200["dams"], h100_nandina
                    ),
                },
            }
        )
        if len(accepted) == policy["accepted_replicates"]:
            break

    if len(accepted) != policy["accepted_replicates"]:
        raise RuntimeError(
            "EXP-11B feasibility failed closed: insufficient valid unique nested DAM compositions"
        )
    return {
        "gate": "NEW_HISTORICAL_GATE_03",
        "experiment_id": config["experiment_id"],
        "version": config["version"],
        "status": "PROSPECTIVE_DESIGN_FEASIBLE_NOT_EXECUTED",
        "execution_authorized": False,
        "retrieval_executed": False,
        "banks_materialized": False,
        "selection_contract": config["selection"],
        "feasibility_contract": config["feasibility_contract"],
        "pool": {
            "H100_frozen_rows": len(h100_rows),
            "H100_frozen_dam_count": len(h100_dams),
            "new_eligible_rows": len(new_rows),
            "maximum_pool_rows": len(h100_rows) + len(new_rows),
            "new_eligible_dam_count": len(dam_counts),
            "direct_h100_new_dam_overlap_count": len(direct_dam_overlap),
            "new_eligible_composition_sha256": composition_sha256(dam_counts),
        },
        "seeds_evaluated": evaluated,
        "accepted_seed_schedule": [entry["seed"] for entry in accepted],
        "rejection_counts": dict(sorted(rejection_counts.items())),
        "accepted_replicates": accepted,
    }


def prepare_duplicate_frames(root: Path):
    import pandas as pd

    h100 = pd.read_csv(root / H100_PATH, dtype=str, keep_default_na=False)
    new_pool = pd.read_csv(root / NEW_ELIGIBLE_PATH, dtype=str, keep_default_na=False)
    evaluation = pd.read_csv(root / EVAL_PATH, dtype=str, keep_default_na=False)
    maximum_pool = pd.concat([h100, new_pool], ignore_index=True)
    return maximum_pool, evaluation


def build_common_clean_masks(root: Path) -> tuple[bytes, dict[str, Any]]:
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    from src.evaluation import group_split_by_dam

    maximum_pool, evaluation = prepare_duplicate_frames(root)
    exact_summary, exact_details = group_split_by_dam.exact_duplicate_audit(
        maximum_pool, evaluation, "maximum_historical_pool-evaluation"
    )
    near_summary, near_details = group_split_by_dam.near_duplicate_audit(
        maximum_pool, evaluation, "maximum_historical_pool-evaluation"
    )
    mask_by_case = {
        str(case_id): {
            "case_id": str(case_id),
            "exact_match_in_max_pool": False,
            "near_090_in_max_pool": False,
            "near_095_in_max_pool": False,
            "near_098_in_max_pool": False,
        }
        for case_id in evaluation[CASE_ID].astype(str)
    }
    for row in exact_details:
        mask_by_case[str(row["right_case_id"])]["exact_match_in_max_pool"] = True
    threshold_fields = {0.9: "near_090_in_max_pool", 0.95: "near_095_in_max_pool", 0.98: "near_098_in_max_pool"}
    for row in near_details:
        threshold = float(row["threshold"])
        mask_by_case[str(row["right_case_id"])][threshold_fields[threshold]] = True
    rows = [mask_by_case[str(case_id)] for case_id in evaluation[CASE_ID].astype(str)]
    fieldnames = [
        "case_id",
        "exact_match_in_max_pool",
        "near_090_in_max_pool",
        "near_095_in_max_pool",
        "near_098_in_max_pool",
    ]
    masked_case_counts = {
        "exact": sum(bool(row["exact_match_in_max_pool"]) for row in rows),
        "near090": sum(bool(row["near_090_in_max_pool"]) for row in rows),
        "near095": sum(bool(row["near_095_in_max_pool"]) for row in rows),
        "near098": sum(bool(row["near_098_in_max_pool"]) for row in rows),
    }
    summary = {
        "primary_eval_denominator": len(rows),
        "maximum_pool_rows": len(maximum_pool),
        "masked_case_counts": masked_case_counts,
        "clean_denominators": {
            key: len(rows) - value for key, value in masked_case_counts.items()
        },
        "primary_denominator_affected": False,
        "selection_affected": False,
        "duplicate_audit_summary": {"exact": exact_summary, "near": near_summary},
    }
    return write_csv_bytes(fieldnames, rows), summary


def build_freeze_manifest(
    config: dict[str, Any], inventory: list[dict[str, Any]], root: Path
) -> dict[str, Any]:
    ingest_manifest = read_json(root / GATE_DIR / "new_historical_ingestion_manifest.json")
    frozen_datasets = ingest_manifest["frozen_datasets"]
    expected_frozen = config["frozen_datasets"]
    for name, expected in expected_frozen.items():
        actual = frozen_datasets.get(name, {})
        if actual.get("sha256") != expected["sha256"]:
            raise RuntimeError(f"Frozen {name} hash does not match the Gate 03 contract")
        dataset_path = root / Path(expected["path"])
        if sha256_file(dataset_path) != expected["sha256"]:
            raise RuntimeError(f"Frozen {name} file hash does not match the Gate 03 contract")
    new_rows = read_csv_rows(root / NEW_ELIGIBLE_PATH)
    eligible_contract = config["real_ingest_01"]
    if sha256_file(root / NEW_ELIGIBLE_PATH) != eligible_contract["eligible_sha256"]:
        raise RuntimeError("Expanded eligible pool hash does not match the Gate 03 contract")
    if len(new_rows) != eligible_contract["eligible_rows"]:
        raise RuntimeError("Expanded eligible pool row count does not match the Gate 03 contract")
    h100_rows = read_csv_rows(root / H100_PATH)
    h100_dams = {row[DAM].strip() for row in h100_rows}
    new_dams = {row[DAM].strip() for row in new_rows}
    overlap = sorted(h100_dams & new_dams)
    if overlap:
        raise RuntimeError("Expanded eligible pool overlaps H100 DAM identifiers")
    return {
        "gate": "NEW_HISTORICAL_GATE_03",
        "version": "v0.1",
        "status": "REAL_INGEST_01_FROZEN_FOR_PROSPECTIVE_EXP11B_DESIGN",
        "source_execution_commit": ingest_manifest["execution_commit"],
        "workbook": ingest_manifest["workbook"],
        "real_ingest_artifacts": inventory,
        "real_ingest_counts": ingest_manifest["counts"],
        "frozen_datasets": frozen_datasets,
        "direct_h100_new_dam_overlap_count": len(overlap),
        "direct_h100_new_dam_overlap": overlap,
        "frozen_data_changed": False,
        "real_ingest_regenerated": False,
        "retrieval_executed": False,
        "H150_materialized": False,
        "H200_materialized": False,
    }


def build_freeze_hashes(root: Path, inventory: list[dict[str, Any]]) -> bytes:
    manifest_path = root / FREEZE_MANIFEST
    manifest_row = {
        "path": relative(FREEZE_MANIFEST),
        "size_bytes": manifest_path.stat().st_size,
        "sha256": sha256_file(manifest_path),
    }
    return write_csv_bytes(["path", "size_bytes", "sha256"], [*inventory, manifest_row])


def no_overwrite(root: Path) -> None:
    existing = [path for path in (FREEZE_MANIFEST, FREEZE_HASHES, FEASIBILITY, COMMON_MASKS) if (root / path).exists()]
    if existing:
        joined = ", ".join(relative(path) for path in existing)
        raise RuntimeError(f"Gate 03 refuses to overwrite existing frozen evidence: {joined}")


def expected_outputs(root: Path, config: dict[str, Any]) -> dict[Path, bytes]:
    inventory = artifact_inventory(root, REAL_INGEST_ARTIFACTS)
    freeze_manifest = build_freeze_manifest(config, inventory, root)
    h100_rows = read_csv_rows(root / H100_PATH)
    new_rows = read_csv_rows(root / NEW_ELIGIBLE_PATH)
    feasibility = build_feasibility_evidence(config, new_rows, h100_rows)
    feasibility["selection_identity_comparison"] = verify_selection_identity_against_baseline(root, feasibility)
    masks, mask_summary = build_common_clean_masks(root)
    feasibility["common_clean_mask_summary"] = mask_summary
    return {
        FREEZE_MANIFEST: canonical_json(freeze_manifest).encode("utf-8"),
        FEASIBILITY: canonical_json(feasibility).encode("utf-8"),
        COMMON_MASKS: masks,
    }


def run(root: Path, config_path: Path, verify_only: bool, refresh_derived_evidence: bool) -> None:
    config = read_json(config_path)
    if config["execution_authorized"] or config["retrieval_executed"]:
        raise RuntimeError("EXP-11B Gate 03 config must remain prospective and non-executing")
    outputs = expected_outputs(root, config)
    if verify_only:
        for path, expected in outputs.items():
            actual_path = root / path
            if not actual_path.is_file() or actual_path.read_bytes() != expected:
                raise RuntimeError(f"Gate 03 verification mismatch: {relative(path)}")
        inventory = artifact_inventory(root, REAL_INGEST_ARTIFACTS)
        expected_hashes = build_freeze_hashes(root, inventory)
        if (root / FREEZE_HASHES).read_bytes() != expected_hashes:
            raise RuntimeError(f"Gate 03 verification mismatch: {relative(FREEZE_HASHES)}")
        print("RESULT: PASS")
        print("MODE: VERIFY_ONLY")
        print("RETRIEVAL_EXECUTED: false")
        return
    if refresh_derived_evidence:
        for path in (FREEZE_MANIFEST, COMMON_MASKS):
            actual_path = root / path
            if not actual_path.is_file() or actual_path.read_bytes() != outputs[path]:
                raise RuntimeError(f"Gate 03 refresh requires unchanged frozen artifact: {relative(path)}")
        if not (root / FEASIBILITY).is_file():
            raise RuntimeError("Gate 03 refresh requires the existing feasibility evidence")
        (root / FEASIBILITY).write_bytes(outputs[FEASIBILITY])
        print("RESULT: PASS")
        print("MODE: REFRESH_DERIVED_FEASIBILITY_ONLY")
        print("RETRIEVAL_EXECUTED: false")
        return
    no_overwrite(root)
    for path, payload in outputs.items():
        destination = root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
    inventory = artifact_inventory(root, REAL_INGEST_ARTIFACTS)
    (root / FREEZE_HASHES).write_bytes(build_freeze_hashes(root, inventory))
    feasibility = read_json(root / FEASIBILITY)
    print("RESULT: PASS")
    print(f"ACCEPTED_REPLICATES: {len(feasibility['accepted_replicates'])}")
    print(f"MAXIMUM_POOL_ROWS: {feasibility['pool']['maximum_pool_rows']}")
    print("RETRIEVAL_EXECUTED: false")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "src/configs/exp11b_historical_size_extension_v0.1.json",
    )
    parser.add_argument("--verify", action="store_true", help="Recompute and compare frozen Gate 03 evidence.")
    parser.add_argument(
        "--refresh-derived-evidence",
        action="store_true",
        help="Rewrite only the approved derived feasibility evidence after baseline identity verification.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    try:
        if arguments.verify and arguments.refresh_derived_evidence:
            raise ValueError("--verify and --refresh-derived-evidence are mutually exclusive")
        run(ROOT, arguments.config, arguments.verify, arguments.refresh_derived_evidence)
    except Exception as error:
        print(f"RESULT: FAIL\n{error}", file=sys.stderr)
        raise
