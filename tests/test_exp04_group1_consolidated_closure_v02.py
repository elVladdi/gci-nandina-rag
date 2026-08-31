"""Regression checks for the deterministic Group 1 consolidated closure."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import unittest


REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "outputs" / "evaluation" / "exp04_consolidated_closure_v0.2"


def rows(name: str) -> list[dict[str, str]]:
    with (OUT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def manifest() -> dict:
    return json.loads((OUT / "gate_exp04_consolidated_closure_manifest_v0.2.json").read_text(encoding="utf-8"))


def test_all_ten_group1_cards_are_closed_and_approved() -> None:
    matrix = rows("exp04_group1_card_closure_matrix_v0.2.csv")
    assert [row["card"] for row in matrix] == [f"EXP-{number:02d}" for number in range(1, 11)]
    assert all(row["status"] == "CLOSED" and row["gate"] == "APPROVED" for row in matrix)
    assert all(not row["blocking_issue"] for row in matrix)


def test_split_integrity_and_freeze_contracts_are_closed() -> None:
    value = manifest()
    assert value["dam_overlap_zero"] is True
    assert value["eval_drift"] is False
    assert value["eval_tuning"] is False
    assert value["eval_cases"] == 1056


def test_main_historical_ranking_metrics_are_registered() -> None:
    registry = rows("exp04_final_results_registry_v0.2.csv")
    metrics = {(row["phase"], row["metric"]): row["value"] for row in registry}
    assert metrics[("EXP-04 A", "Top-1")] == "0.509470"
    assert metrics[("EXP-04 A", "Top-3")] == "0.671402"
    assert metrics[("EXP-04 A", "Top-50")] == "0.991477"


def test_normative_and_dense_results_are_preserved_without_reinterpretation() -> None:
    registry = rows("exp04_final_results_registry_v0.2.csv")
    values = {(row["phase"], row["metric"]): row["value"] for row in registry}
    assert values[("EXP-04 B", "Recall@100")] == "0.071023"
    assert values[("EXP-04 C", "Recall@200")] == "0.303977"
    assert values[("EXP-04 D1a", "Top-1")] == "0.071023"


def test_g_h_i_j_k_l_and_exp08_evidence_is_registered() -> None:
    registry = rows("exp04_final_results_registry_v0.2.csv")
    phases = {row["phase"] for row in registry}
    assert {"EXP-04 G", "EXP-04 H", "EXP-04 I", "EXP-04 J", "EXP-04 K", "EXP-04 L", "EXP-08"} <= phases


def test_preserved_hypothesis_statuses_and_no_fabricated_oe1_he1() -> None:
    hypotheses = {row["hypothesis"]: row["status"] for row in rows("exp04_hypothesis_status_registry_v0.2.csv")}
    assert hypotheses == {"HE2": "PARTIALLY_SUPPORTED", "HE3": "SUPPORTED", "HE4": "PARTIALLY_SUPPORTED", "HE5": "PARTIALLY_SUPPORTED"}
    assert manifest()["oe1_he1_formal_status"] == "NOT_FABRICATED_NO_CONSOLIDATED_ASSESSMENT_FOUND"


def test_all_known_limitations_are_preserved() -> None:
    limitations = rows("exp04_consolidated_limitations_v0.2.csv")
    assert len(limitations) == 13
    assert all(row["status"] == "PRESERVED_NOT_RESOLVED" for row in limitations)


def test_provenance_hashes_match_existing_frozen_artifacts() -> None:
    for row in rows("exp04_final_provenance_registry_v0.2.csv"):
        path = REPO / row["artifact"]
        if row["exists"] == "True":
            assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]


def test_gate_declares_no_new_execution_or_merge() -> None:
    value = manifest()
    assert value["no_model_call"] is True
    assert value["no_new_retrieval"] is True
    assert value["no_web"] is True
    assert value["merged_to_main"] is False
    assert value["gate_exp04_consolidated"] == "APPROVED"
    assert value["group1_gate"] == "APPROVED"


def test_generated_registry_hashes_are_current() -> None:
    value = manifest()
    for name, expected in value["generated_file_hashes"].items():
        actual = hashlib.sha256((OUT / name).read_bytes()).hexdigest()
        assert actual == expected


class TestExp04Group1ConsolidatedClosureV02(unittest.TestCase):
    def test_all_cards(self) -> None:
        test_all_ten_group1_cards_are_closed_and_approved()

    def test_split_integrity(self) -> None:
        test_split_integrity_and_freeze_contracts_are_closed()

    def test_historical_metrics(self) -> None:
        test_main_historical_ranking_metrics_are_registered()

    def test_normative_and_dense_metrics(self) -> None:
        test_normative_and_dense_results_are_preserved_without_reinterpretation()

    def test_phase_evidence(self) -> None:
        test_g_h_i_j_k_l_and_exp08_evidence_is_registered()

    def test_hypotheses(self) -> None:
        test_preserved_hypothesis_statuses_and_no_fabricated_oe1_he1()

    def test_limitations(self) -> None:
        test_all_known_limitations_are_preserved()

    def test_provenance(self) -> None:
        test_provenance_hashes_match_existing_frozen_artifacts()

    def test_scope_guards(self) -> None:
        test_gate_declares_no_new_execution_or_merge()

    def test_generated_hashes(self) -> None:
        test_generated_registry_hashes_are_current()
