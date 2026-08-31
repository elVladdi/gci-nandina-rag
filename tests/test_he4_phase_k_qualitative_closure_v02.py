from __future__ import annotations

import csv
import hashlib
import json
import unittest
from pathlib import Path

from tests.sha_contracts_v02 import assert_frozen_sha, git_content_sha256


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"
DIMENSIONS = [
    "trazabilidad",
    "verificabilidad",
    "separacion_historico_normativo",
    "prudencia_de_la_conclusion",
    "consistencia_con_top3_fijo",
    "deteccion_de_evidencia_normativa_generica",
    "comparacion_entre_candidatos",
    "utilidad_para_auditoria_humana",
]
EXPECTED_TEMPLATE_SHA256 = "5779d6e5f59c8f947a4efa0903da79ff0ec62c8047b79a2eb94ade0518c980c4"


def sha256(path: Path) -> str:
    return git_content_sha256(path)


class He4PhaseKQualitativeClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (OUT / "he4_qualitative_scoring_template_v0.2.csv").open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            cls.columns = reader.fieldnames
            cls.template = list(reader)
        cls.packet = [json.loads(line) for line in (OUT / "he4_qualitative_review_packet_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        cls.metrics = json.loads((OUT / "he4_qualitative_metrics_v0.2.json").read_text(encoding="utf-8"))
        cls.manifest = json.loads((OUT / "gate_k_qualitative_evaluation_manifest_v0.2.json").read_text(encoding="utf-8"))
        cls.joint = json.loads((OUT / "he4_he4_joint_jk_assessment_v0.2.json").read_text(encoding="utf-8"))
        cls.pre_manifest = json.loads((OUT / "gate_k_pre_scoring_manifest_v0.2.json").read_text(encoding="utf-8"))

    def test_01_received_scoring_is_the_authorized_input(self) -> None:
        assert_frozen_sha(self, OUT / "he4_qualitative_scoring_template_v0.2.csv", EXPECTED_TEMPLATE_SHA256)
        self.assertEqual(len(self.template), 50)
        self.assertEqual(len({row["case_id"] for row in self.template}), 50)
        self.assertEqual({row["case_id"] for row in self.template}, {row["case_id"] for row in self.packet})

    def test_02_exact_columns_dimensions_and_scores(self) -> None:
        expected = ["case_id", *[field for dimension in DIMENSIONS for field in (f"{dimension}_score", f"{dimension}_justification")], "hard_violation", "hard_violation_type", "total_score", "auditable", "general_notes"]
        self.assertEqual(self.columns, expected)
        self.assertEqual(sum(1 for row in self.template for dimension in DIMENSIONS if row[f"{dimension}_score"] in {"0", "1", "2"}), 400)
        self.assertEqual(sum(1 for row in self.template for dimension in DIMENSIONS if row[f"{dimension}_justification"].strip()), 400)

    def test_03_totals_auditability_and_hard_violations_are_consistent(self) -> None:
        self.assertTrue(all(row["hard_violation"] in {"SI", "NO"} for row in self.template))
        for row in self.template:
            total = sum(int(row[f"{dimension}_score"]) for dimension in DIMENSIONS)
            self.assertEqual(row["total_score"], str(total))
            expected_auditable = "SI" if total >= 12 and row["hard_violation"] == "NO" else "NO"
            self.assertEqual(row["auditable"], expected_auditable)
        self.assertEqual(self.metrics["validation"]["total_score_consistency"]["numerator"], 50)
        self.assertEqual(self.metrics["validation"]["auditable_consistency"]["numerator"], 50)
        self.assertEqual(self.metrics["auditable"]["numerator"], 28)
        self.assertEqual(self.metrics["hard_violations"]["count"], 0)

    def test_04_provenance_and_historical_pre_scoring_are_preserved(self) -> None:
        self.assertEqual(self.pre_manifest["evaluator_modality"], "A. HUMAN/MANUAL REVIEW")
        self.assertTrue(self.pre_manifest["no_model_judge"])
        self.assertEqual(self.manifest["evaluator_modality"], "AI_EXPERT_ROLE")
        self.assertEqual(self.manifest["evaluator_identifier"], "independent_ai_reviewer_01")
        self.assertFalse(self.manifest["human_scoring"])
        self.assertTrue(self.manifest["llm_as_judge"])
        self.assertTrue(self.manifest["methodological_deviation"])
        self.assertEqual(self.manifest["methodological_deviation_type"], "EVALUATOR_MODALITY_DEVIATION")
        self.assertFalse(self.manifest["ground_truth_exposed"])
        self.assertFalse(self.manifest["reference_rank_exposed"])
        self.assertFalse(self.manifest["bucket_exposed"])
        self.assertFalse(self.manifest["external_evidence_used"])
        self.assertFalse(self.manifest["web_used"])
        self.assertFalse(self.manifest["retrieval_used"])

    def test_05_gate_and_preserved_j_limitations(self) -> None:
        self.assertEqual(self.manifest["gate_k"], "APPROVED WITH EVALUATOR-MODALITY LIMITATION")
        self.assertTrue(self.manifest["ready_for_phase_l"])
        self.assertTrue(self.manifest["advertencias_globales_excluded"])
        self.assertTrue(self.manifest["prompt_schema_limitation_preserved"])
        self.assertEqual(self.joint["he4_j"]["gate"], "APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION")
        self.assertEqual(self.joint["he4_global"], "PARTIALLY SUPPORTED")

    def test_06_post_scoring_comparisons_and_outputs_are_auditable(self) -> None:
        with (OUT / "he4_qualitative_warning_comparison_v0.2.csv").open(encoding="utf-8", newline="") as handle:
            warning_rows = {row["group"]: row for row in csv.DictReader(handle)}
        self.assertEqual(warning_rows["generic_normative_warning_missing"]["cases"], "9")
        self.assertEqual(warning_rows["other_cases"]["cases"], "41")
        for name, expected_hash in self.manifest["outputs_sha256_excluding_manifest_and_summary"].items():
            path = {
                "case_scores": OUT / "he4_qualitative_case_scores_v0.2.csv",
                "dimension_metrics": OUT / "he4_qualitative_dimension_metrics_v0.2.csv",
                "metrics": OUT / "he4_qualitative_metrics_v0.2.json",
                "hard_violations": OUT / "he4_qualitative_hard_violations_v0.2.csv",
                "by_bucket": OUT / "he4_qualitative_by_bucket_v0.2.csv",
                "warning_comparison": OUT / "he4_qualitative_warning_comparison_v0.2.csv",
                "findings": OUT / "he4_qualitative_findings_v0.2.md",
                "joint_assessment": OUT / "he4_he4_joint_jk_assessment_v0.2.json",
            }[name]
            self.assertTrue(path.exists())
            assert_frozen_sha(self, path, expected_hash)

    def test_07_closer_uses_no_external_runtime(self) -> None:
        source = (ROOT / "src/experiments/close_he4_qualitative_ai_scoring_v02.py").read_text(encoding="utf-8").lower()
        for forbidden in ("import requests", "import urllib", "ollama", "http://", "https://", "embedding", "bm25"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
