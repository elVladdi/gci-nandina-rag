"""Contract tests for the D1a 0B-05C pre-execution audit."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.experiments.audit_d1a_preexecution_0b05c_v01 import audit, bilingual_record, normalize_nandina


ROOT = Path(__file__).resolve().parents[1]


class D1aPreexecution0B05cV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            cls.result = audit(ROOT, Path(temporary_directory))

    def test_01_training_reconstruction_matches_real_metadata(self) -> None:
        evidence = self.result["training_evidence"]
        self.assertEqual(evidence["status"], "DETERMINISTIC_RECONSTRUCTION_MATCHES_TRAINING_METADATA")
        self.assertEqual(evidence["reconstruction"]["records"], 2950)
        self.assertEqual(evidence["reconstruction"]["batches"], 608)
        self.assertEqual(evidence["reconstruction"]["seed"], 2026)

    def test_02_top200_scan_is_complete_and_not_a_metric_run(self) -> None:
        overlap = self.result["retrieval_output_overlap"]
        self.assertEqual(overlap["cases_scanned"], 1056)
        self.assertEqual(overlap["candidates_per_case"], 200)
        self.assertFalse(self.result["prospective_decisions"]["RETRIEVAL_EXECUTED"])
        self.assertFalse(self.result["prospective_decisions"]["EVALUATION_METRICS_COMPUTED"])

    def test_03_nandina_search_normalizes_representation_only(self) -> None:
        self.assertEqual(normalize_nandina("87.0441.10"), "87044110")
        self.assertEqual(normalize_nandina(" 8704-5110 "), "87045110")

    def test_04_prospective_decisions_remain_closed(self) -> None:
        decisions = self.result["prospective_decisions"]
        self.assertEqual(decisions["CORRECTED_INDEX_POLICY"], "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD")
        self.assertEqual(decisions["PRIMARY_CONTROL"], "FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT")
        self.assertEqual(decisions["D1A_EXECUTION_SPECIFICATION"], "CLOSED_PROSPECTIVELY")
        self.assertEqual(decisions["D1A_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")

    def test_05_each_affected_code_has_linked_training_evidence(self) -> None:
        for code in ("87044110", "87045110"):
            exposure = self.result["training_exposure"]["by_code"][code]
            evidence = exposure["artifact_hash_or_run_metadata"]
            self.assertEqual(exposure["evidence_artifact"], "outputs/training/text2trade_mnrl_v0.2/training_metadata.json")
            self.assertEqual(len(evidence["training_metadata_sha256"]), 64)
            self.assertEqual(len(evidence["runner_blob_sha"]), 40)
            self.assertEqual(len(evidence["selector_blob_sha"]), 40)
            self.assertEqual(len(evidence["config_blob_sha"]), 40)

    def test_06_bilingual_record_preserves_the_prospective_controls(self) -> None:
        record = bilingual_record(self.result)
        self.assertIn("Control opcional de reproduccion: `REPRODUCIBILITY_CHECK_ONLY`", record)
        self.assertIn("Optional control reproduction: `REPRODUCIBILITY_CHECK_ONLY`", record)
        self.assertIn("Bloqueos residuales: Ningun bloqueo impide esta auditoria forense.", record)
        self.assertIn("Residual blockers: No blocker prevents this forensic audit.", record)


if __name__ == "__main__":
    unittest.main()
