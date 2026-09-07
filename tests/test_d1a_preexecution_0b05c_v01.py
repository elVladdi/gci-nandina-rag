"""Contract tests for the D1a 0B-05C pre-execution audit."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.experiments.audit_d1a_preexecution_0b05c_v01 import (
    EXPECTED_NEGATIVE_SOURCE,
    audit,
    bilingual_record,
    normalize_nandina,
)


ROOT = Path(__file__).resolve().parents[1]


class D1aPreexecution0B05cV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            cls.result = audit(ROOT, Path(temporary_directory))

    def test_01_frozen_h100_pool_contains_all_66_codes_and_excludes_affected_codes(self) -> None:
        pool = self.result["historical_training_code_pool"]
        self.assertEqual(pool["source"]["row_count"], 2950)
        self.assertEqual(pool["historical_training_code_count"], 66)
        self.assertEqual(len(pool["historical_training_codes"]), 66)
        self.assertFalse(pool["affected_code_membership"]["87044110"])
        self.assertFalse(pool["affected_code_membership"]["87045110"])
        self.assertNotIn("87044110", pool["historical_training_codes"])
        self.assertNotIn("87045110", pool["historical_training_codes"])

    def test_02_pool_exclusion_conclusion_depends_on_restricted_negative_source_not_execution_head(self) -> None:
        evidence = self.result["training_evidence"]
        exposure = self.result["training_exposure"]
        self.assertEqual(evidence["training_metadata"]["negative_source"], EXPECTED_NEGATIVE_SOURCE)
        self.assertEqual(evidence["TRAINING_EXPOSURE_EVIDENCE"], "POOL_EXCLUSION_PROOF_SUPPORTED_BY_FROZEN_RUN_METADATA")
        self.assertEqual(evidence["EXECUTION_REPOSITORY_HEAD"], "UNKNOWN / HISTORICAL_PROVENANCE_LIMITATION")
        self.assertEqual(
            exposure["conclusion_dependency"],
            "FROZEN_H100_POOL_EXCLUSION_AND_RESTRICTED_NEGATIVE_SOURCE_NOT_EXECUTION_REPOSITORY_HEAD",
        )

    def test_03_each_affected_code_has_zero_primary_exposure_from_the_pool_contract(self) -> None:
        for code in ("87044110", "87045110"):
            exposure = self.result["training_exposure"]["by_code"][code]
            self.assertEqual(exposure["positive_training_occurrences"], 0)
            self.assertEqual(exposure["explicit_hard_negative_occurrences"], 0)
            self.assertEqual(exposure["positive_exposure_basis"], "DIRECT_FROZEN_H100_POOL_EXCLUSION")
            self.assertIn("METADATA_NEGATIVE_SOURCE_RESTRICTION", exposure["explicit_hard_negative_basis"])
            self.assertFalse(exposure["execution_repository_head_required_for_conclusion"])

    def test_04_reconstruction_is_corroborative_and_matches_real_metadata(self) -> None:
        evidence = self.result["training_evidence"]
        self.assertEqual(evidence["RECONSTRUCTION_STATUS"], "DETERMINISTIC_RECONSTRUCTION_CONSISTENT_WITH_TRAINING_METADATA")
        self.assertEqual(evidence["reconstruction"]["records"], 2950)
        self.assertEqual(evidence["reconstruction"]["batches"], 608)
        self.assertEqual(evidence["reconstruction"]["seed"], 2026)
        self.assertEqual(
            evidence["historical_code_snapshots"]["scope"],
            "CORROBORATIVE_ONLY_NOT_A_CRYPTOGRAPHIC_EXECUTION_CHECKOUT_LINK",
        )

    def test_05_corrective_execution_specification_is_closed_only_prospectively(self) -> None:
        specification = self.result["corrective_execution_spec"]
        self.assertEqual(specification["specification_status"], "CLOSED_PROSPECTIVELY")
        self.assertEqual(specification["authorization"]["D1A_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")
        self.assertEqual(specification["corrected_normative_corpus"]["definition"]["patch_scope"], "EXACTLY_TWO_NANDINA8_DOCUMENTS")
        self.assertEqual(specification["index_builder"]["policy"], "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD")
        self.assertEqual(specification["evaluation"]["eval_input"]["N"], 1056)
        self.assertEqual(specification["evaluation"]["ranking_depth"], 200)

    def test_06_top200_scan_is_complete_and_not_a_metric_run(self) -> None:
        overlap = self.result["retrieval_output_overlap"]
        decisions = self.result["prospective_decisions"]
        self.assertEqual(overlap["cases_scanned"], 1056)
        self.assertEqual(overlap["candidates_per_case"], 200)
        self.assertEqual(overlap["total_occurrences_87044110"], 0)
        self.assertEqual(overlap["total_occurrences_87045110"], 0)
        self.assertFalse(decisions["RETRIEVAL_EXECUTED"])
        self.assertFalse(decisions["EVALUATION_METRICS_COMPUTED"])

    def test_07_nandina_search_normalizes_representation_only(self) -> None:
        self.assertEqual(normalize_nandina("87.0441.10"), "87044110")
        self.assertEqual(normalize_nandina(" 8704-5110 "), "87045110")

    def test_08_bilingual_record_preserves_the_provenance_limitation_and_prospective_controls(self) -> None:
        record = bilingual_record(self.result)
        self.assertIn("POOL_EXCLUSION_PROOF_SUPPORTED_BY_FROZEN_RUN_METADATA", record)
        self.assertIn("UNKNOWN / HISTORICAL_PROVENANCE_LIMITATION", record)
        self.assertIn("D1A_EXECUTION_SPECIFICATION=CLOSED_PROSPECTIVELY", record)
        self.assertIn("not a cryptographic link", record)


if __name__ == "__main__":
    unittest.main()
