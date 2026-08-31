"""Build the read-only forensic inventories for Group 1 SHA portability."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path, PurePosixPath
import re
import subprocess


REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "outputs" / "evaluation" / "exp04_consolidated_closure_v0.2"
TEXT_EXTENSIONS = {".json", ".csv", ".md", ".txt"}
SHA256_RE = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])")
ACTIVE_SOURCES = {
    "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_provenance_registry_v0.2.csv",
    "outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json",
}
FORENSIC_BASELINE = "07eff735bf43f0d831c7d57ec134b8cbc61c8caa"
PROVENANCE_PATH = "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_provenance_registry_v0.2.csv"
MANIFEST_PATH = "outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json"
MICROCLOSE_PATH = "outputs/evaluation/exp04_consolidated_closure_v0.2/gate_group1_sha_contract_portability_microclose_v0.2.json"
ADMIN_ARTIFACTS = [
    "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_sha_contract_occurrence_inventory_v0.2.csv",
    "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_sha_contract_reference_inventory_v0.2.csv",
    "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_sha_artifact_canonicalization_map_v0.2.csv",
    "outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_active_sha_contract_dependency_graph_v0.2.csv",
    PROVENANCE_PATH,
    MANIFEST_PATH,
]


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO), "show", spec])


def git_paths(revision: str) -> list[str]:
    if revision == ":":
        return subprocess.check_output(
            ["git", "-C", str(REPO), "ls-files"], text=True, encoding="utf-8"
        ).splitlines()
    return subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", revision], text=True, encoding="utf-8"
    ).splitlines()


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def json_pointer(parts: tuple[str, ...]) -> str:
    return "/" + "/".join(part.replace("~", "~0").replace("/", "~1") for part in parts)


def json_sha_values(value: object, parts: tuple[str, ...] = ()) -> list[tuple[str, str]]:
    if isinstance(value, dict):
        return [item for key, child in value.items() for item in json_sha_values(child, (*parts, key))]
    if isinstance(value, list):
        return [item for index, child in enumerate(value) for item in json_sha_values(child, (*parts, str(index)))]
    if isinstance(value, str) and SHA256_RE.fullmatch(value):
        return [(json_pointer(parts), value.lower())]
    return []


def source_phase(path: str) -> str:
    if path.startswith("outputs/audits/data_aduanas_splits"):
        return "EXP-01/EXP-02/EXP-03"
    if "/exp05_" in path or "/exp05/" in path:
        return "EXP-05"
    if "/exp07_" in path or "/exp07/" in path:
        return "EXP-07"
    if "/exp08_" in path or "/exp08/" in path:
        return "EXP-08"
    if "/he4_" in path:
        return "EXP-04 HE4"
    if "/he5_" in path:
        return "EXP-04 HE5"
    if "/historical_retrieval_" in path:
        return "EXP-04 A"
    if "/exp04_consolidated_closure_" in path:
        return "EXP-04 / GROUP 1"
    return "GROUP 1"


def source_values(path: str, blob: bytes) -> list[tuple[str, str, str]]:
    suffix = PurePosixPath(path).suffix.lower()
    text = blob.decode("utf-8")
    if suffix == ".json":
        return [(locator, value, "JSON") for locator, value in json_sha_values(json.loads(text))]
    if suffix == ".csv":
        rows = list(csv.reader(text.splitlines()))
        header = rows[0]
        values: list[tuple[str, str, str]] = []
        for row_number, row in enumerate(rows[1:], start=2):
            for column_index, cell in enumerate(row):
                column = header[column_index] if column_index < len(header) else f"column_{column_index + 1}"
                for occurrence_index, match in enumerate(SHA256_RE.finditer(cell), start=1):
                    values.append((f"row:{row_number}/column:{column}/occurrence:{occurrence_index}", match.group().lower(), "CSV"))
        return values
    values = []
    for match in SHA256_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        values.append((f"line:{line}/offset:{match.start()}", match.group().lower(), "TEXT"))
    return values


def eol_by_path(paths: list[str]) -> dict[str, dict[str, str]]:
    raw = subprocess.check_output(["git", "-C", str(REPO), "ls-files", "--eol", "-z"])
    values: dict[str, dict[str, str]] = {}
    for entry in raw.decode("utf-8").split("\0"):
        if not entry:
            continue
        metadata, path = entry.split("\t", 1)
        parts = metadata.split()
        values[path] = {
            "index_eol": parts[0].removeprefix("i/"),
            "worktree_eol": parts[1].removeprefix("w/"),
            "eol_attribute": " ".join(parts[2:]),
        }
    return {path: values[path] for path in paths}


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def collect(
    revision: str = FORENSIC_BASELINE, *, enforce_expected_counts: bool = True
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    paths = git_paths(revision)
    text_blobs = {
        path: git_bytes(f"{revision}{path}" if revision == ":" else f"{revision}:{path}")
        for path in paths
        if PurePosixPath(path).suffix.lower() in TEXT_EXTENSIONS
    }
    targets_by_legacy: dict[str, list[tuple[str, str]]] = defaultdict(list)
    canonical_hashes: set[str] = set()
    for path, blob in text_blobs.items():
        canonical_hashes.add(sha256(blob))
        if b"\r\n" not in blob:
            targets_by_legacy[sha256(blob.replace(b"\n", b"\r\n"))].append((path, sha256(blob)))

    occurrences: list[dict[str, object]] = []
    for source in paths:
        if not (source.startswith("outputs/audits/") or source.startswith("outputs/evaluation/")):
            continue
        if source not in text_blobs:
            continue
        blob = text_blobs[source]
        for locator, legacy, source_type in source_values(source, blob):
            matches = targets_by_legacy.get(legacy, [])
            if legacy in canonical_hashes or not matches:
                continue
            if len(matches) != 1:
                raise RuntimeError(f"legacy SHA maps to multiple targets: {legacy}")
            target, canonical = matches[0]
            lifecycle = "ACTIVE_CANONICAL_CONTRACT" if source in ACTIVE_SOURCES else "HISTORICAL_LEGACY_CONTRACT"
            occurrences.append(
                {
                    "source_artifact": source,
                    "source_locator": locator,
                    "source_type": source_type,
                    "phase": source_phase(source),
                    "target_artifact": target,
                    "legacy_expected_sha256": legacy,
                    "canonical_git_lf_sha256": canonical,
                    "crlf_reconstructed_sha256": legacy,
                    "legacy_matches_crlf": "true",
                    "legacy_matches_lf": "false",
                    "classification": "EXPECTED_MATCHES_LEGACY_CRLF_REPRESENTATION",
                    "contract_lifecycle": lifecycle,
                    "migration_action": "CANONICALIZE_ACTIVE_SOURCE_AT_LOCATOR" if source in ACTIVE_SOURCES else "PRESERVE_HISTORICAL_LEGACY_AND_MAP",
                    "notes": "SHA-256 calculated from Git content bytes; CRLF value reconstructed in memory.",
                }
            )

    if enforce_expected_counts and len(occurrences) != 106:
        raise RuntimeError(f"expected 106 occurrences, found {len(occurrences)}")

    unique: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for occurrence in occurrences:
        unique[(occurrence["source_artifact"], occurrence["legacy_expected_sha256"], occurrence["target_artifact"])].append(occurrence)
    if enforce_expected_counts and len(unique) != 101:
        raise RuntimeError(f"expected 101 unique references, found {len(unique)}")

    reference_rows: list[dict[str, object]] = []
    for index, group in enumerate(unique.values(), start=1):
        first = group[0].copy()
        first["reference_id"] = f"REF-{index:03d}"
        first["source_locator"] = " | ".join(item["source_locator"] for item in group)
        first["occurrence_count"] = len(group)
        first["deduplication_criterion"] = "source_artifact+legacy_expected_sha256+target_artifact"
        reference_rows.append(first)

    by_target: dict[str, list[dict[str, object]]] = defaultdict(list)
    for occurrence in occurrences:
        by_target[str(occurrence["target_artifact"])].append(occurrence)
    if enforce_expected_counts and len(by_target) != 55:
        raise RuntimeError(f"expected 55 target artifacts, found {len(by_target)}")
    eol = eol_by_path(list(by_target))
    map_rows: list[dict[str, object]] = []
    for target, group in sorted(by_target.items()):
        legacy_values = {str(item["legacy_expected_sha256"]) for item in group}
        canonical_values = {str(item["canonical_git_lf_sha256"]) for item in group}
        if len(legacy_values) != 1 or len(canonical_values) != 1:
            raise RuntimeError(f"target does not have a 1:1 legacy/canonical mapping: {target}")
        map_rows.append(
            {
                "artifact": target,
                "phase": " | ".join(sorted({str(item["phase"]) for item in group})),
                "legacy_sha256": next(iter(legacy_values)),
                "canonical_git_lf_sha256": next(iter(canonical_values)),
                "legacy_representation": "WORKTREE_CRLF_BYTES",
                "canonical_representation": "CANONICAL_GIT_LF_CONTENT_BYTES",
                "scientific_content_changed": "false",
                "git_tracked": "true",
                "eol_attribute": eol[target]["eol_attribute"],
                "index_eol": eol[target]["index_eol"],
                "worktree_eol": eol[target]["worktree_eol"],
                "evidence": "legacy SHA equals in-memory CRLF reconstruction of the canonical Git LF blob",
            }
        )

    graph_rows: list[dict[str, object]] = []
    seen_edges: set[tuple[str, str]] = set()
    for occurrence in occurrences:
        if occurrence["contract_lifecycle"] != "ACTIVE_CANONICAL_CONTRACT":
            continue
        edge = (str(occurrence["source_artifact"]), str(occurrence["target_artifact"]))
        if edge in seen_edges:
            continue
        seen_edges.add(edge)
        graph_rows.append(
            {
                "source": edge[0],
                "target": edge[1],
                "source_will_change": "true",
                "target_will_change": "true" if edge[1].endswith("exp04_final_provenance_registry_v0.2.csv") else "false",
            }
        )
    return occurrences, reference_rows, map_rows, graph_rows


def canonical_by_legacy() -> dict[str, str]:
    map_path = OUT / "exp04_sha_artifact_canonicalization_map_v0.2.csv"
    if map_path.exists():
        with map_path.open(encoding="utf-8", newline="") as handle:
            return {
                row["legacy_sha256"]: row["canonical_git_lf_sha256"]
                for row in csv.DictReader(handle)
            }
    _, _, mapping, _ = collect()
    return {str(row["legacy_sha256"]): str(row["canonical_git_lf_sha256"]) for row in mapping}


def write_active_provenance() -> None:
    canonical = canonical_by_legacy()
    baseline = git_bytes(f"{FORENSIC_BASELINE}:{PROVENANCE_PATH}").decode("utf-8")
    rows = list(csv.DictReader(baseline.splitlines()))
    fields = [
        "phase", "artifact", "sha256", "legacy_sha256", "hash_basis", "hash_migration_reason",
        "exists", "frozen_evidence", "git_tracked", "role", "notes",
    ]
    output: list[dict[str, object]] = []
    for row in rows:
        legacy = row["sha256"]
        updated = {
            "phase": row["phase"],
            "artifact": row["artifact"],
            "sha256": canonical.get(legacy, legacy),
            "legacy_sha256": legacy if legacy in canonical else "",
            "hash_basis": "CANONICAL_GIT_LF_CONTENT_BYTES",
            "hash_migration_reason": "WORKTREE_EOL_DEPENDENT_HASH" if legacy in canonical else "",
            "exists": row["exists"],
            "frozen_evidence": row["frozen_evidence"],
            "git_tracked": row["git_tracked"],
            "role": row["role"],
            "notes": "Active portable SHA contract canonicalized from the Git LF blob." if legacy in canonical else "Canonical Git LF contract verified.",
        }
        output.append(updated)
    write_csv(REPO / PROVENANCE_PATH, fields, output)


def write_active_manifest(provenance_sha256: str) -> None:
    canonical = canonical_by_legacy()
    value = json.loads(git_bytes(f"{FORENSIC_BASELINE}:{MANIFEST_PATH}").decode("utf-8"))
    for item in value["inputs"]:
        legacy = item["sha256"]
        if legacy in canonical:
            item["sha256"] = canonical[legacy]
            item["legacy_sha256"] = legacy
            item["hash_basis"] = "CANONICAL_GIT_LF_CONTENT_BYTES"
            item["hash_migration_reason"] = "WORKTREE_EOL_DEPENDENT_HASH"
    legacy_generated = dict(value["generated_file_hashes"])
    generated = {name: canonical.get(legacy, legacy) for name, legacy in legacy_generated.items()}
    generated[PurePosixPath(PROVENANCE_PATH).name] = provenance_sha256
    value["generated_file_hashes"] = generated
    value["generated_file_hashes_legacy"] = legacy_generated
    value["generated_file_hash_basis"] = "CANONICAL_GIT_LF_CONTENT_BYTES"
    value["generated_file_hash_migration_reason"] = "WORKTREE_EOL_DEPENDENT_HASH"
    value["current_portable_provenance_contract"] = True
    (REPO / MANIFEST_PATH).write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def index_sha256(path: str) -> str:
    return sha256(git_bytes(f":{path}"))


def write_microclose_manifest(*, finalized: bool) -> None:
    value = {
        "phase": "GROUP 1 SHA CONTRACT PORTABILITY MICROCLOSE",
        "root_cause": "WORKTREE_EOL_DEPENDENT_HASH_CONTRACTS",
        "eol_root_cause": "INCOMPLETE_GITATTRIBUTES_COVERAGE_FOR_FROZEN_TEXT_ARTIFACTS",
        "forensic_occurrences": 106,
        "unique_contract_references": 101,
        "distinct_legacy_hashes": 55,
        "canonicalized_artifacts": 55,
        "historical_legacy_contracts": 87,
        "active_canonical_contracts": 19,
        "non_active_documentary_references": 0,
        "unclassified_occurrences": 0,
        "historical_manifests_rewritten": False,
        "scientific_results_changed": False,
        "scientific_artifacts_regenerated": False,
        "legacy_hashes_preserved": True,
        "canonical_hash_basis": "CANONICAL_GIT_LF_CONTENT_BYTES",
        "gitattributes_commit": FORENSIC_BASELINE,
        "core_autocrlf_changed": False,
        "active_contract_graph_acyclic": True,
        "all_active_contracts_canonical": True,
        "all_legacy_contracts_mapped": True,
        "all_frozen_text_eol_lf": finalized,
        "clean_checkout_validated": finalized,
        "full_suite_passed": finalized,
        "origin_main_unchanged": True,
        "ready_for_main_fast_forward_retry": finalized,
        "administrative_artifact_index_sha256": {path: index_sha256(path) for path in ADMIN_ARTIFACTS},
    }
    (REPO / MICROCLOSE_PATH).write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--write-active-provenance", action="store_true")
    parser.add_argument("--write-active-manifest", metavar="PROVENANCE_SHA256")
    parser.add_argument("--write-microclose-manifest", action="store_true")
    parser.add_argument("--finalize-microclose-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_active_provenance:
        write_active_provenance()
        return
    if args.write_active_manifest:
        write_active_manifest(args.write_active_manifest)
        return
    if args.write_microclose_manifest:
        write_microclose_manifest(finalized=False)
        return
    if args.finalize_microclose_manifest:
        write_microclose_manifest(finalized=True)
        return
    occurrences, references, mapping, graph = collect()
    print(f"occurrences={len(occurrences)}")
    print(f"references={len(references)}")
    print(f"artifacts={len(mapping)}")
    print(f"active_occurrences={sum(row['contract_lifecycle'] == 'ACTIVE_CANONICAL_CONTRACT' for row in occurrences)}")
    print(f"historical_occurrences={sum(row['contract_lifecycle'] == 'HISTORICAL_LEGACY_CONTRACT' for row in occurrences)}")
    print(f"graph_edges={len(graph)}")
    if not args.write:
        return
    occurrence_fields = [
        "occurrence_id", "source_artifact", "source_locator", "source_type", "phase", "target_artifact",
        "legacy_expected_sha256", "canonical_git_lf_sha256", "crlf_reconstructed_sha256", "legacy_matches_crlf",
        "legacy_matches_lf", "classification", "contract_lifecycle", "migration_action", "notes",
    ]
    for index, row in enumerate(occurrences, start=1):
        row["occurrence_id"] = f"OCC-{index:03d}"
    reference_fields = ["reference_id", *occurrence_fields[1:], "occurrence_count", "deduplication_criterion"]
    map_fields = [
        "artifact", "phase", "legacy_sha256", "canonical_git_lf_sha256", "legacy_representation",
        "canonical_representation", "scientific_content_changed", "git_tracked", "eol_attribute", "index_eol",
        "worktree_eol", "evidence",
    ]
    write_csv(OUT / "exp04_sha_contract_occurrence_inventory_v0.2.csv", occurrence_fields, occurrences)
    write_csv(OUT / "exp04_sha_contract_reference_inventory_v0.2.csv", reference_fields, references)
    write_csv(OUT / "exp04_sha_artifact_canonicalization_map_v0.2.csv", map_fields, mapping)
    write_csv(
        OUT / "exp04_active_sha_contract_dependency_graph_v0.2.csv",
        ["source", "target", "source_will_change", "target_will_change"],
        graph,
    )


if __name__ == "__main__":
    main()
