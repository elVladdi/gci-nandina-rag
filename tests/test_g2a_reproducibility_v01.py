"""Regression checks for the G2A reproducibility microclose artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "outputs" / "audits" / "g2a_reproducibility_v0.1"


def csv_rows(name: str) -> list[dict[str, str]]:
    with (AUDIT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


class TestG2AReproducibilityV01(unittest.TestCase):
    def test_inventory_has_required_components_and_columns(self) -> None:
        rows = csv_rows("g2a_reproducibility_inventory_v0.1.csv")
        expected = {
            "SPLIT_V02", "EXP04_A", "EXP04_B", "EXP04_C", "EXP04_D1A", "EXP04_E", "EXP04_F", "EXP04_G",
            "EXP04_H", "EXP04_I", "EXP04_J", "EXP04_K", "EXP04_L", "EXP05", "EXP06", "EXP07", "EXP08", "EXP09", "EXP10",
            "G2A_EXP11_PREEXECUTION_DESIGN", "G2A_EXP11_H50_STRATIFICATION", "G2A_EXTERNAL_TESIS_GOVERNANCE",
        }
        self.assertEqual({row["component_id"] for row in rows}, expected)
        required = {"input_sha256", "script_commit_or_provenance", "config_sha256", "seed", "output_sha256", "manifest_path", "reproducibility_level"}
        self.assertTrue(required.issubset(rows[0]))

    def test_traceability_covers_required_result_chains(self) -> None:
        rows = csv_rows("g2a_end_to_end_traceability_v0.1.csv")
        self.assertEqual(
            {row["chain_id"] for row in rows},
            {"HISTORICAL_TOP3_MRR", "NORMATIVE_FLAT", "NORMATIVE_HIERARCHICAL", "D1A", "INTEGRATION_F", "DIAGNOSTIC_RERANKER_G", "HE4", "HE5", "EXP08", "G2A_EXP11_CONTRACT", "G2A_EXP12_CONTRACT"},
        )

    def test_f003_preserves_partial_d1a_provenance(self) -> None:
        finding = next(row for row in csv_rows("g2a_findings_v0.1.csv") if row["finding_id"] == "G2A-F003")
        self.assertEqual(finding["status"], "PARTIALLY_RESOLVED")
        self.assertEqual(finding["resolution"], "SCRIPT_AND_CONFIG_PROVENANCE_RECOVERED_EXECUTION_HEAD_UNKNOWN")
        self.assertEqual(finding["execution_repository_head"], "UNKNOWN")
        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        self.assertEqual(gate["f003"]["execution_repository_head"], "UNKNOWN")
        self.assertEqual(gate["f003"]["training_script_last_modifying_commit_before_execution"], "a91269ed3b5c52d08511063465be130adf185f0a")
        self.assertEqual(gate["f003"]["config_last_modifying_commit_before_execution"], "c82e6232ef5f0678c3b10fbdb9c3850910aacee0")

    def test_f007_is_future_dependency_with_scoped_blocking(self) -> None:
        finding = next(row for row in csv_rows("g2a_findings_v0.1.csv") if row["finding_id"] == "G2A-F007")
        self.assertEqual(finding["status"], "OPEN")
        self.assertEqual(finding["dependency_type"], "FUTURE_DEPENDENCY")
        self.assertEqual(finding["severity"], "S3_SCOPED_FUTURE")
        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        self.assertEqual(gate["f007"]["status"], "OPEN")
        self.assertEqual(gate["f007"]["dependency_type"], "FUTURE_DEPENDENCY")
        self.assertFalse(gate["f007"]["blocks_g2a_contractual_closure"])
        self.assertFalse(gate["f007"]["blocks_exp11a_h25_h50_h75_h100"])
        self.assertTrue(gate["f007"]["blocks_exp11b_h150_h200"])
        self.assertTrue(gate["f007"]["blocks_all_exp12_execution"])

    def test_environment_and_assets_keep_historical_and_current_separate(self) -> None:
        environment = json.loads((AUDIT / "g2a_environment_inventory_v0.1.json").read_text(encoding="utf-8"))
        self.assertTrue(all(item["classification"] == "CURRENT_ENV_ONLY" for item in environment["current_env_only"]))
        asset_classes = {row["asset_class"] for row in csv_rows("g2a_asset_classification_v0.1.csv")}
        self.assertEqual(
            asset_classes,
            {"VERSIONED_FROZEN_EVIDENCE", "RECONSTRUCTABLE_ARTIFACT", "RESTRICTED_LOCAL_SOURCE", "RUNTIME_ONLY_DEPENDENCY", "OPTIONAL_DIAGNOSTIC_ASSET", "NOT_REQUIRED_FOR_FROZEN_CONCLUSION", "EXTERNAL_TESIS_GOVERNANCE_DOCUMENT"},
        )

    def test_final_gate_authorizes_only_exp11a_and_records_no_scientific_change(self) -> None:
        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        self.assertEqual(gate["status"], "APPROVED_WITH_NONBLOCKING_LIMITATIONS")
        self.assertEqual(gate["recommended_gate"], "APPROVED_WITH_NONBLOCKING_LIMITATIONS")
        self.assertEqual(gate["closure_state"], "CLOSED")
        self.assertEqual(gate["external_final_audit"], "APPROVED")
        self.assertEqual(gate["external_audit_date"], "2026-08-31")
        self.assertEqual(gate["audited_candidate_commit"], "c9751f67165b0bf6e06b54e4e979e7258481ded6")
        self.assertTrue(gate["G2A_CLOSED"])
        self.assertFalse(gate["group1_reopen_required"])
        self.assertEqual(gate["blocking_findings_for_exp11a"], [])
        self.assertFalse(gate["scientific_results_changed"])
        self.assertFalse(gate["scientific_artifacts_regenerated"])
        self.assertTrue(gate["execution_authorization"]["exp11"])
        self.assertTrue(gate["execution_authorization"]["exp11a"])
        self.assertEqual(gate["execution_authorization"]["exp11a_execution_scope"], "EXP11A_H25_H50_H75_H100_ONLY")
        self.assertEqual(gate["execution_authorization"]["authorized_conditions"], ["H25", "H50", "H75", "H100"])
        self.assertFalse(gate["execution_authorization"]["exp11b"])
        self.assertFalse(gate["execution_authorization"]["expanded_historical_conditions"])
        self.assertFalse(gate["execution_authorization"]["exp12"])
        self.assertFalse(gate["NEW_HISTORICAL_DATA_REQUIRED_NOW"])
        self.assertEqual(gate["NEXT_NEW_DATA_TRIGGER"], "AFTER_EXP11A_EXTERNAL_AUDIT")

    def test_microclose_1b_records_exp11_fail_closed_evidence(self) -> None:
        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        evidence = json.loads((AUDIT / gate["microclose_1b"]["exp11_h100_planning_evidence"]).read_text(encoding="utf-8"))
        self.assertEqual(gate["microclose_1b"]["exp11_seed_acceptance"], "DESIGN_INFEASIBLE")
        self.assertEqual(gate["microclose_1b"]["exp11_final_candidate_seeds"], [])
        self.assertFalse(gate["microclose_1b"]["exp11_retrieval_started"])
        self.assertFalse(gate["microclose_1b"]["exp12_real_data_planning_started"])
        self.assertEqual(evidence["seed_acceptance"]["status"], "DESIGN_INFEASIBLE")
        self.assertEqual(evidence["seed_acceptance"]["candidates_evaluated"], 100000)
        self.assertEqual(len(evidence["original_seed_evidence"]), 10)
        self.assertTrue(all(item["nesting_valid"] and not item["valid_seed"] for item in evidence["original_seed_evidence"]))
        self.assertFalse(evidence["retrieval_executed"])
        self.assertFalse(evidence["eval_descriptions_read"])
        self.assertFalse(evidence["eval_labels_read"])

    def test_microclose_1c_freezes_f008_f009_and_independent_compositions(self) -> None:
        findings = {row["finding_id"]: row for row in csv_rows("g2a_findings_v0.1.csv")}
        self.assertEqual(findings["G2A-F008"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(findings["G2A-F008"]["resolution"], "FROZEN_PRE_EXECUTION_CORRECTION")
        self.assertEqual(findings["G2A-F008"]["severity"], "S3_SCOPED_TO_EXP11A_DESIGN")
        self.assertEqual(findings["G2A-F008"]["classification"], "PRE_EXECUTION_DESIGN_INFEASIBILITY")
        self.assertEqual(findings["G2A-F009"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(findings["G2A-F009"]["resolution"], "DECLARED_LIMITATION")
        self.assertEqual(findings["G2A-F009"]["classification"], "STRUCTURAL_SIZE_COMPOSITION_COUPLING")
        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        close = gate["microclose_1c"]
        evidence = json.loads((AUDIT / close["exp11_independent_condition_evidence"]).read_text(encoding="utf-8"))
        self.assertEqual(close["f008"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(close["f008"]["structural_design_status"], "STRUCTURALLY_INFEASIBLE_UNDER_FROZEN_GROUP_AND_VOLUME_CONSTRAINTS")
        self.assertEqual(close["f009"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(close["f009"]["resolution"], "DECLARED_LIMITATION")
        self.assertFalse(close["exp11_retrieval_started"])
        self.assertFalse(close["exp12_started"])
        self.assertEqual(evidence["seed_acceptance"]["status"], "ACCEPTED")
        self.assertFalse(evidence["retrieval_executed"])
        self.assertFalse(evidence["eval_descriptions_read"])
        self.assertFalse(evidence["eval_labels_read"])
        self.assertFalse(evidence["selection_uses_nandina"])
        self.assertFalse(evidence["selection_uses_eval"])
        self.assertEqual(evidence["f008_structural_infeasibility"]["minimum_h75_rows_if_h25_were_nested"], 2575)
        self.assertEqual(evidence["f008_structural_infeasibility"]["h75_upper_band"], 2361)
        all_compositions = []
        for condition, dominant_count in {"H25": 0, "H50": 1, "H75": 2}.items():
            records = evidence["conditions"][condition]
            self.assertEqual(len(records), 10)
            self.assertEqual(len({record["composition_sha256"] for record in records}), 10)
            self.assertTrue(all(record["dominant_count"] == dominant_count for record in records))
            self.assertTrue(all(record["complete_dams_valid"] for record in records))
            self.assertTrue(all(record["nandina_coverage"]["reference_codes"] == 66 for record in records))
            all_compositions.extend(record["composition_sha256"] for record in records)
        self.assertEqual(len(set(all_compositions)), 30)

    def test_microclose_1d_preserves_h25_h75_and_stratifies_h50_pairs(self) -> None:
        findings = {row["finding_id"]: row for row in csv_rows("g2a_findings_v0.1.csv")}
        f010 = findings["G2A-F010"]
        self.assertEqual(f010["status"], "VERIFIED_IN_G2")
        self.assertEqual(f010["severity"], "S2")
        self.assertEqual(f010["resolution"], "RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION")
        self.assertEqual(f010["previous_state"], "2_D1_8_D2")
        self.assertEqual(f010["final_state"], "5_D1_5_D2")
        self.assertEqual(f010["classification"], "H50_DOMINANT_STRATUM_IMBALANCE")

        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        close = gate["microclose_1d"]
        self.assertEqual(close["status"], "PENDING_EXTERNAL_AUDIT")
        self.assertEqual(close["f010"]["classification"], "H50_DOMINANT_STRATUM_IMBALANCE")
        self.assertEqual(close["f010"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(close["f010"]["resolution"], "RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION")
        self.assertFalse(close["f010"]["scientific_results_affected"])
        self.assertFalse(close["f010"]["group1_reopen_required"])
        self.assertTrue(close["h25_sha_preserved_from_v0_1"])
        self.assertTrue(close["h75_sha_preserved_from_v0_1"])
        self.assertEqual(close["h50_paired_seeds"], [20261001, 20261002, 20261003, 20261004, 20261005])
        self.assertEqual(close["h50_replicates"], {"D1": 5, "D2": 5, "total": 10})
        self.assertFalse(close["exp11_retrieval_started"])
        self.assertFalse(close["exp12_started"])
        self.assertFalse(close["group3_started"])

        previous = json.loads((AUDIT / "exp11_independent_condition_feasibility_v0.1.json").read_text(encoding="utf-8"))
        evidence = json.loads((AUDIT / close["exp11_independent_condition_evidence"]).read_text(encoding="utf-8"))
        self.assertEqual(evidence["artifact_type"], "G2A_EXP11_INDEPENDENT_CONDITION_FEASIBILITY_V0_2_ONLY")
        self.assertEqual(evidence["supersedes_planning_evidence"], "exp11_independent_condition_feasibility_v0.1.json")
        self.assertFalse(evidence["retrieval_executed"])
        self.assertFalse(evidence["eval_descriptions_read"])
        self.assertFalse(evidence["eval_labels_read"])
        self.assertFalse(evidence["selection_uses_nandina"])
        self.assertFalse(evidence["selection_uses_eval"])
        for condition in ("H25", "H75"):
            previous_sha = [record["composition_sha256"] for record in previous["conditions"][condition]]
            current_sha = [record["composition_sha256"] for record in evidence["conditions"][condition]]
            self.assertEqual(current_sha, previous_sha)
            self.assertEqual(len(current_sha), 10)

        h50 = evidence["conditions"]["H50"]
        self.assertEqual(len(h50), 10)
        by_pair: dict[str, list[dict[str, object]]] = {}
        by_stratum = {"D1": [], "D2": []}
        for record in h50:
            self.assertTrue(record["complete_dams_valid"])
            self.assertTrue(record["valid_seed"])
            self.assertEqual(record["dominant_count"], 1)
            self.assertLessEqual(record["absolute_row_deviation"], 148)
            by_pair.setdefault(record["pair_id"], []).append(record)
            by_stratum[record["dominant_stratum"]].append(record)
        self.assertEqual({stratum: len(records) for stratum, records in by_stratum.items()}, {"D1": 5, "D2": 5})
        self.assertEqual(len(by_pair), 5)
        self.assertEqual(len({record["composition_sha256"] for record in by_stratum["D1"]}), 5)
        self.assertEqual(len({record["composition_sha256"] for record in by_stratum["D2"]}), 5)
        for pair_id, records in by_pair.items():
            self.assertEqual(len(records), 2, pair_id)
            self.assertEqual({record["dominant_stratum"] for record in records}, {"D1", "D2"})
            self.assertEqual(len({record["seed"] for record in records}), 1)
        self.assertEqual(evidence["h50_interpretation"]["primary_analysis"], "POOLED_EQUAL_WEIGHT_5_D1_5_D2")
        self.assertEqual(evidence["h50_interpretation"]["secondary_diagnostic"], "DOMINANT_STRATUM_COMPARISON")
        self.assertFalse(evidence["h50_interpretation"]["causal_dominant_identity_claim_allowed"])

    def test_microclose_1e_normalizes_findings_and_records_external_governance(self) -> None:
        findings = {row["finding_id"]: row for row in csv_rows("g2a_findings_v0.1.csv")}
        expected = {
            "G2A-F001": ("PARTIALLY_RESOLVED", "HISTORICAL_ENVIRONMENT_INCOMPLETE_BUT_EXPLICITLY_DELIMITED"),
            "G2A-F002": ("NOT_RECOVERABLE", "EXP04_C_HISTORICAL_RUNNER_NOT_VERSIONED_AT_EXECUTION"),
            "G2A-F003": ("PARTIALLY_RESOLVED", "SCRIPT_AND_CONFIG_PROVENANCE_RECOVERED_EXECUTION_HEAD_UNKNOWN"),
            "G2A-F004": ("PARTIALLY_RESOLVED", "LLM_AND_AI_EVALUATION_NOT_BYTE_EXACTLY_REPRODUCIBLE"),
            "G2A-F005": ("NOT_RECOVERABLE", "EXP08_V01_METADATA_NOT_RECOVERABLE_NO_RETROSPECTIVE_RECONSTRUCTION"),
            "G2A-F006": ("VERIFIED_IN_G2", "EXP11_EXP12_REPRODUCIBILITY_CONTRACTS_IMPLEMENTED_AND_TESTED"),
            "G2A-F007": ("OPEN", "FUTURE_DEPENDENCY_UNRESOLVED"),
            "G2A-F008": ("VERIFIED_IN_G2", "FROZEN_PRE_EXECUTION_CORRECTION"),
            "G2A-F009": ("VERIFIED_IN_G2", "DECLARED_LIMITATION"),
            "G2A-F010": ("VERIFIED_IN_G2", "RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION"),
        }
        self.assertEqual({finding_id: (findings[finding_id]["status"], findings[finding_id]["resolution"]) for finding_id in expected}, expected)
        for finding_id in ("G2A-F001", "G2A-F002", "G2A-F004", "G2A-F005"):
            self.assertNotEqual(findings[finding_id]["status"], "CLOSED_BY_GROUP1")
        self.assertEqual(findings["G2A-F002"]["r1_r2_preserved"], "true")
        self.assertEqual(findings["G2A-F004"]["r5"], "PARTIAL")
        self.assertEqual(findings["G2A-F006"]["original_diagnostic_status"], "OPEN")
        self.assertEqual(findings["G2A-F006"]["original_severity"], "S3")

        gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        self.assertEqual(gate["status"], "APPROVED_WITH_NONBLOCKING_LIMITATIONS")
        self.assertEqual(gate["recommended_gate"], "APPROVED_WITH_NONBLOCKING_LIMITATIONS")
        self.assertEqual(gate["resolved_in_g2"], ["F006", "F008", "F010"])
        self.assertEqual(gate["future_dependencies"], ["F007"])
        close = gate["microclose_1e"]
        self.assertEqual(close["exp11_v3_design"], "ACCEPTED_PENDING_VERSIONED_FREEZE")
        self.assertEqual(close["exp12_v3_method"], "CONDITIONAL_ACCEPTED_PENDING_NEW_HISTORICAL_GATE")
        self.assertFalse(close["exp11a_execution_authorized"])
        self.assertFalse(close["exp12_execution_authorized"])
        documents = close["external_tesis_governance_documents"]
        self.assertEqual(len(documents), 2)
        self.assertTrue(all(item["role"] == "EXTERNAL_TESIS_GOVERNANCE_DOCUMENT" for item in documents))
        self.assertTrue(all(not item["required_for_clean_checkout_execution"] for item in documents))


if __name__ == "__main__":
    unittest.main()
