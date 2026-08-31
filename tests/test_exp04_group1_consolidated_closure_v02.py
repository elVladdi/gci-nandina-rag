"""Regression checks for the deterministic Group 1 consolidated closure."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import subprocess
import unittest


REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "outputs" / "evaluation" / "exp04_consolidated_closure_v0.2"
D1A_PATH = "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"
D1A_SHA256 = "620412bc15dbba2edd4e2d195457f0b8b4ce670cd75ff7c6d87835a435b8fb3c"


def rows(name: str) -> list[dict[str, str]]:
    with (OUT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def manifest() -> dict:
    return json.loads((OUT / "gate_exp04_consolidated_closure_manifest_v0.2.json").read_text(encoding="utf-8"))


def corrective_manifest() -> dict:
    return json.loads((OUT / "gate_exp04_consolidated_corrective_microclose_manifest_v0.2.json").read_text(encoding="utf-8"))


def git_tracked(path: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "--error-unmatch", "--", path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def git_content_sha256(path: str) -> str:
    return hashlib.sha256(
        subprocess.check_output(["git", "-C", str(REPO), "show", f":{path}"])
    ).hexdigest()


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


def test_normative_metrics_are_preserved_without_reinterpretation() -> None:
    registry = rows("exp04_final_results_registry_v0.2.csv")
    values = {(row["phase"], row["metric"]): row["value"] for row in registry}
    assert values[("EXP-04 B", "Recall@100")] == "0.071023"
    assert values[("EXP-04 C", "Recall@200")] == "0.303977"


def test_d1a_metrics_reconcile_exactly_with_frozen_source_and_not_d0() -> None:
    source_path = REPO / D1A_PATH
    assert source_path.exists()
    assert git_content_sha256(D1A_PATH) == D1A_SHA256
    assert git_tracked(D1A_PATH)
    source = json.loads(source_path.read_text(encoding="utf-8"))["metrics"]
    expected = {
        "Top-1": "top_1", "Top-3": "top_3", "Top-5": "top_5", "Top-10": "top_10",
        "Top-50": "top_50", "Recall@100": "recall_at_100", "MRR@100": "mrr_at_100",
        "Recall@200": "recall_at_200", "MRR@200": "mrr_at_200",
    }
    registry = [row for row in rows("exp04_final_results_registry_v0.2.csv") if row["phase"] == "EXP-04 D1a"]
    assert {row["metric"] for row in registry} == set(expected)
    for row in registry:
        key = expected[row["metric"]]
        assert row["value"] == f"{source[key]:.15f}"
        assert row["numerator"] == str(source[f"{key}_numerator"])
        assert row["denominator"] == str(source[f"{key}_denominator"])
        assert row["artifact"] == D1A_PATH
        assert row["artifact_sha256"] == D1A_SHA256
        assert "text2trade_dense_data_aduanas" not in row["artifact"]


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
    assert set(limitations[0]) == {"limitation_id", "category", "description", "affected_phase", "scientific_consequence", "mitigation_or_handling", "status"}
    assert all(row["status"] == "PRESERVED_NOT_RESOLVED" for row in limitations)


def test_provenance_hashes_match_existing_frozen_artifacts() -> None:
    for row in rows("exp04_final_provenance_registry_v0.2.csv"):
        path = REPO / row["artifact"]
        if row["exists"] == "True" and row["frozen_evidence"] == "True":
            assert path.exists()
            assert git_content_sha256(row["artifact"]) == row["sha256"]
            assert row["git_tracked"] == "True"
            assert git_tracked(row["artifact"])


def test_benchmark_hashes_exp02_and_exp06_title_are_explicit() -> None:
    value = manifest()
    assert value["historical_sha256"] == "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff"
    assert value["dev_sha256"] == "434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00"
    assert value["eval_sha256"] == "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
    assert "EXP-02" in {row["phase"] for row in rows("exp04_final_provenance_registry_v0.2.csv")}
    matrix = {row["card"]: row for row in rows("exp04_group1_card_closure_matrix_v0.2.csv")}
    assert matrix["EXP-06"]["title"] == "diagnostic reranker final pool"


def test_corrective_gate_closes_group1_only_when_all_contracts_pass() -> None:
    value = manifest()
    corrective = corrective_manifest()
    assert value["d1a_metrics_sha256"] == D1A_SHA256
    assert value["d1a_artifact_git_tracked"] is True
    assert value["all_frozen_evidence_git_tracked"] is True
    assert corrective["provenance_registry_complete"] is True
    assert corrective["gate_exp04_consolidated_corrective_microclose"] == "APPROVED"
    assert corrective["group1_status"] == "CLOSED"
    assert corrective["ready_for_main_merge_review"] is True


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
        actual = git_content_sha256(f"outputs/evaluation/exp04_consolidated_closure_v0.2/{name}")
        assert actual == expected


class TestExp04Group1ConsolidatedClosureV02(unittest.TestCase):
    def test_all_cards(self) -> None:
        test_all_ten_group1_cards_are_closed_and_approved()

    def test_split_integrity(self) -> None:
        test_split_integrity_and_freeze_contracts_are_closed()

    def test_historical_metrics(self) -> None:
        test_main_historical_ranking_metrics_are_registered()

    def test_normative_metrics(self) -> None:
        test_normative_metrics_are_preserved_without_reinterpretation()

    def test_d1a_metrics(self) -> None:
        test_d1a_metrics_reconcile_exactly_with_frozen_source_and_not_d0()

    def test_phase_evidence(self) -> None:
        test_g_h_i_j_k_l_and_exp08_evidence_is_registered()

    def test_hypotheses(self) -> None:
        test_preserved_hypothesis_statuses_and_no_fabricated_oe1_he1()

    def test_limitations(self) -> None:
        test_all_known_limitations_are_preserved()

    def test_provenance(self) -> None:
        test_provenance_hashes_match_existing_frozen_artifacts()

    def test_benchmark_hashes_and_card_metadata(self) -> None:
        test_benchmark_hashes_exp02_and_exp06_title_are_explicit()

    def test_corrective_gate(self) -> None:
        test_corrective_gate_closes_group1_only_when_all_contracts_pass()

    def test_scope_guards(self) -> None:
        test_gate_declares_no_new_execution_or_merge()

    def test_generated_hashes(self) -> None:
        test_generated_registry_hashes_are_current()
