from __future__ import annotations

import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"


class He4PhaseKHumanPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads((OUT / "gate_k_pre_scoring_manifest_v0.2.json").read_text(encoding="utf-8"))
        cls.packet = [json.loads(line) for line in (OUT / "he4_qualitative_review_packet_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        with (OUT / "he4_qualitative_scoring_template_v0.2.csv").open(encoding="utf-8", newline="") as handle:
            cls.template = list(csv.DictReader(handle))

    def test_01_fifty_blind_cases_and_exact_dimensions(self) -> None:
        dimensions = ["trazabilidad", "verificabilidad", "separacion_historico_normativo", "prudencia_de_la_conclusion", "consistencia_con_top3_fijo", "deteccion_de_evidencia_normativa_generica", "comparacion_entre_candidatos", "utilidad_para_auditoria_humana"]
        self.assertEqual(len(self.packet), 50)
        self.assertEqual(len(self.template), 50)
        self.assertTrue(all(row["dimensions"] == dimensions for row in self.packet))

    def test_02_packet_hides_labels_and_buckets(self) -> None:
        forbidden = ("expected_nandina", "reference_rank", "exact_rank", "selection_bucket", "selection_target", "correctness")
        self.assertTrue(all(not any(value in json.dumps(row, ensure_ascii=False).lower() for value in forbidden) for row in self.packet))
        self.assertTrue(self.manifest["labels_hidden"])
        self.assertTrue(self.manifest["buckets_hidden"])

    def test_03_pre_scoring_manifest_preserves_the_original_blank_package(self) -> None:
        self.assertTrue(self.manifest["no_scores_assigned"])

    def test_04_frozen_contract_and_status_hold(self) -> None:
        self.assertEqual(self.manifest["rubric"]["sha256"], "175f5405bcdf911fa449cdbbef1fff17284c134970be4a40f8af8a25df25e514")
        self.assertEqual(self.manifest["gate_k"], "PENDING HUMAN SCORING")
        self.assertTrue(self.manifest["ready_for_human_scoring"])
        self.assertFalse(self.manifest["ready_for_phase_l"])
        self.assertFalse(self.manifest["phase_k_executed"])

    def test_05_no_model_or_retrieval_dependency(self) -> None:
        source = (ROOT / "src/experiments/prepare_he4_qualitative_human_scoring_v02.py").read_text(encoding="utf-8").lower()
        for forbidden in ("import urllib", "import requests", "http://", "https://", "ollama", "bm25", "embedding"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
