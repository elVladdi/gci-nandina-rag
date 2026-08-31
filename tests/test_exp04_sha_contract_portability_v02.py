"""Regression tests for the Group 1 SHA contract portability microclose."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

from src.analysis.build_exp04_sha_contract_portability_v02 import (
    ACTIVE_SOURCES,
    FORENSIC_BASELINE,
    source_values,
)


REPO = Path(__file__).resolve().parents[1]
OUT_REL = "outputs/evaluation/exp04_consolidated_closure_v0.2"
OUT = REPO / OUT_REL


def rows(name: str) -> list[dict[str, str]]:
    with (OUT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO), "show", spec])


def git_sha(path: str) -> str:
    return hashlib.sha256(git_bytes(f":{path}")).hexdigest()


def baseline_sha(path: str) -> str:
    return hashlib.sha256(git_bytes(f"{FORENSIC_BASELINE}:{path}")).hexdigest()


def canonical_map() -> dict[str, dict[str, str]]:
    return {row["legacy_sha256"]: row for row in rows("exp04_sha_artifact_canonicalization_map_v0.2.csv")}


def test_forensic_inventory_reconciles_exactly() -> None:
    occurrences = rows("exp04_sha_contract_occurrence_inventory_v0.2.csv")
    references = rows("exp04_sha_contract_reference_inventory_v0.2.csv")
    mapping = rows("exp04_sha_artifact_canonicalization_map_v0.2.csv")
    assert len(occurrences) == 106
    assert len(references) == 101
    assert len(mapping) == 55
    assert len({row["legacy_expected_sha256"] for row in occurrences}) == 55
    assert len({row["target_artifact"] for row in occurrences}) == 55
    assert sum(row["contract_lifecycle"] == "ACTIVE_CANONICAL_CONTRACT" for row in occurrences) == 19
    assert sum(row["contract_lifecycle"] == "HISTORICAL_LEGACY_CONTRACT" for row in occurrences) == 87
    assert sum(row["contract_lifecycle"] == "NON_ACTIVE_DOCUMENTARY_REFERENCE" for row in occurrences) == 0
    assert all(row["classification"] == "EXPECTED_MATCHES_LEGACY_CRLF_REPRESENTATION" for row in occurrences)
    assert all(row["migration_action"] for row in occurrences)


def test_artifact_map_proves_crlf_legacy_equivalence() -> None:
    mapping = rows("exp04_sha_artifact_canonicalization_map_v0.2.csv")
    assert len({row["legacy_sha256"] for row in mapping}) == len(mapping)
    for row in mapping:
        blob = git_bytes(f"{FORENSIC_BASELINE}:{row['artifact']}")
        assert hashlib.sha256(blob).hexdigest() == row["canonical_git_lf_sha256"]
        assert hashlib.sha256(blob.replace(b"\n", b"\r\n")).hexdigest() == row["legacy_sha256"]
        assert row["legacy_sha256"] != row["canonical_git_lf_sha256"]
        assert row["scientific_content_changed"] == "false"
        assert row["git_tracked"] == "true"
        assert row["index_eol"] == "lf"
        assert "eol=lf" in row["eol_attribute"]


def test_historical_contract_sources_are_not_rewritten() -> None:
    historical_sources = {
        row["source_artifact"]
        for row in rows("exp04_sha_contract_occurrence_inventory_v0.2.csv")
        if row["contract_lifecycle"] == "HISTORICAL_LEGACY_CONTRACT"
    }
    for source in historical_sources:
        assert git_bytes(f":{source}") == git_bytes(f"{FORENSIC_BASELINE}:{source}")


def test_active_provenance_and_manifest_use_canonical_contracts() -> None:
    mapping = canonical_map()
    provenance = rows("exp04_final_provenance_registry_v0.2.csv")
    affected = [row for row in provenance if row["legacy_sha256"]]
    assert len(affected) == 7
    for row in affected:
        mapped = mapping[row["legacy_sha256"]]
        assert row["artifact"] == mapped["artifact"]
        assert row["sha256"] == mapped["canonical_git_lf_sha256"]
        assert row["hash_basis"] == "CANONICAL_GIT_LF_CONTENT_BYTES"
        assert row["hash_migration_reason"] == "WORKTREE_EOL_DEPENDENT_HASH"
    value = json.loads((OUT / "gate_exp04_consolidated_closure_manifest_v0.2.json").read_text(encoding="utf-8"))
    active_inputs = [item for item in value["inputs"] if "legacy_sha256" in item]
    assert len(active_inputs) == 7
    for item in active_inputs:
        mapped = mapping[item["legacy_sha256"]]
        assert item["artifact"] == mapped["artifact"]
        assert item["sha256"] == mapped["canonical_git_lf_sha256"]
        assert item["hash_basis"] == "CANONICAL_GIT_LF_CONTENT_BYTES"
        assert item["hash_migration_reason"] == "WORKTREE_EOL_DEPENDENT_HASH"
    for name, legacy in value["generated_file_hashes_legacy"].items():
        expected = git_sha(f"{OUT_REL}/{name}") if name == "exp04_final_provenance_registry_v0.2.csv" else mapping[legacy]["canonical_git_lf_sha256"]
        assert value["generated_file_hashes"][name] == expected


def test_final_scan_has_no_active_or_unmapped_crlf_contract() -> None:
    mapping = canonical_map()
    original_sources = sorted(
        {row["source_artifact"] for row in rows("exp04_sha_contract_occurrence_inventory_v0.2.csv")}
    )
    active_crlf = []
    unmapped = []
    documentary = 0
    historical = 0
    for source in original_sources:
        blob = git_bytes(f":{source}")
        for locator, legacy, _ in source_values(source, blob):
            if legacy not in mapping:
                continue
            is_documentary = source in ACTIVE_SOURCES and (
                "legacy_sha256" in locator or "generated_file_hashes_legacy" in locator
            )
            if is_documentary:
                documentary += 1
            elif source in ACTIVE_SOURCES:
                active_crlf.append((source, locator, legacy))
            else:
                historical += 1
            if legacy not in mapping:
                unmapped.append((source, locator, legacy))
    assert active_crlf == []
    assert unmapped == []
    assert historical == 87
    assert documentary == 19


def test_active_dependency_graph_is_acyclic() -> None:
    graph = rows("exp04_active_sha_contract_dependency_graph_v0.2.csv")
    assert len(graph) == 17
    adjacency: dict[str, set[str]] = {}
    for edge in graph:
        adjacency.setdefault(edge["source"], set()).add(edge["target"])
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        assert node not in visiting
        if node in visited:
            return
        visiting.add(node)
        for target in adjacency.get(node, set()):
            visit(target)
        visiting.remove(node)
        visited.add(node)

    for source in adjacency:
        visit(source)


class TestExp04ShaContractPortabilityV02(unittest.TestCase):
    def test_inventory(self) -> None:
        test_forensic_inventory_reconciles_exactly()

    def test_mapping(self) -> None:
        test_artifact_map_proves_crlf_legacy_equivalence()

    def test_historical_sources(self) -> None:
        test_historical_contract_sources_are_not_rewritten()

    def test_active_contracts(self) -> None:
        test_active_provenance_and_manifest_use_canonical_contracts()

    def test_final_scan(self) -> None:
        test_final_scan_has_no_active_or_unmapped_crlf_contract()

    def test_graph(self) -> None:
        test_active_dependency_graph_is_acyclic()


if __name__ == "__main__":
    unittest.main()
