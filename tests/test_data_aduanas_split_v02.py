import csv
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
AUDIT = ROOT / "outputs" / "audits" / "data_aduanas_splits_clase87_v0.2"
SCRIPT = ROOT / "src" / "evaluation" / "group_split_by_dam.py"
CONFIG = ROOT / "src" / "configs" / "data_aduanas_split_clase87_v0.2.json"
PYTHON = os.environ.get("PYTHON", sys.executable)

SPLITS = {
    "historico": DATA / "data_aduanas_historico_clase87_v0.2.csv",
    "desarrollo": DATA / "data_aduanas_devset_clase87_v0.2.csv",
    "evaluacion": DATA / "data_aduanas_evalset_clase87_v0.2.csv",
}
V01_HASHES = {
    DATA / "data_aduanas_historico_clase87_v0.1.csv": "ea3286063fc890d2569a8cd3704ab18d82970e3b41973153957e27486c28f2f0",
    DATA / "data_aduanas_devset_clase87_v0.1.csv": "19eeb607cb1586f3eb459a95d267844bcb068daf93f05e4055ce1183dd698a50",
    DATA / "data_aduanas_evalset_clase87_v0.1.csv": "ae642d01c0e941ab94a187fb2a820fbc8dcd6259c90d9decb70408b9dea344bb",
    DATA / "data_aduanas_splits_clase87_v0.1_metadata.json": "71a42f793ae7e7cb02ec5b97723c74ac7b60d67f9f7b542ebfa43bb77834189a",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class TestDataAduanasSplitV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_json(CONFIG)
        cls.metadata = load_json(DATA / "data_aduanas_splits_clase87_v0.2_metadata.json")
        cls.parts = {name: rows(path) for name, path in SPLITS.items()}
        cls.all_rows = [row for part in cls.parts.values() for row in part]
        cls.audit_summary = load_json(AUDIT / "audit_summary_v0.2.json")
        cls.support_summary = load_json(AUDIT / "historical_support_summary_v0.2.json")
        cls.concentration = load_json(AUDIT / "concentration_summary_v0.2.json")
        cls.exact_summary = rows(AUDIT / "exact_duplicates_cross_split_summary_v0.2.csv")
        cls.near_summary = rows(AUDIT / "near_duplicates_hist_eval_summary_v0.2.csv")

    def test_01_expected_files_exist(self):
        for path in [SCRIPT, CONFIG, *SPLITS.values(), DATA / "data_aduanas_splits_clase87_v0.2_metadata.json"]:
            self.assertTrue(path.exists(), path)

    def test_02_approved_split_sizes(self):
        self.assertEqual({k: len(v) for k, v in self.parts.items()}, {"historico": 2950, "desarrollo": 100, "evaluacion": 1056})

    def test_03_approved_dam_counts(self):
        self.assertEqual({k: len({r["DECLARACION"] for r in v}) for k, v in self.parts.items()}, {"historico": 28, "desarrollo": 6, "evaluacion": 67})

    def test_04_approved_code_counts(self):
        self.assertEqual({k: len({r["NANDINA"] for r in v}) for k, v in self.parts.items()}, {"historico": 66, "desarrollo": 9, "evaluacion": 42})

    def test_05_zero_dam_overlap(self):
        dams = {k: {r["DECLARACION"] for r in v} for k, v in self.parts.items()}
        self.assertFalse(dams["historico"] & dams["desarrollo"])
        self.assertFalse(dams["historico"] & dams["evaluacion"])
        self.assertFalse(dams["desarrollo"] & dams["evaluacion"])

    def test_06_zero_id_unico_overlap(self):
        ids = {k: {r["id_unico"] for r in v} for k, v in self.parts.items()}
        self.assertFalse(ids["historico"] & ids["desarrollo"])
        self.assertFalse(ids["historico"] & ids["evaluacion"])
        self.assertFalse(ids["desarrollo"] & ids["evaluacion"])

    def test_07_full_assignment_once(self):
        ids = [r["id_unico"] for r in self.all_rows]
        self.assertEqual(len(ids), 4106)
        self.assertEqual(len(set(ids)), 4106)

    def test_08_split_labels_and_case_prefixes(self):
        prefixes = {"historico": "DA-HIST-V02-", "desarrollo": "DA-DEV-V02-", "evaluacion": "DA-EVAL-V02-"}
        for split, part in self.parts.items():
            self.assertTrue(all(r["split"] == split for r in part))
            self.assertTrue(all(r["case_id"].startswith(prefixes[split]) for r in part))

    def test_09_schema_is_v01_compatible(self):
        required = {"case_id", "id_unico", "split", "DECLARACION", "SERIE", "NANDINA", "DESCRIPCION DE MERCANCIAS CONCATENADA"}
        for part in self.parts.values():
            self.assertTrue(required.issubset(part[0].keys()))

    def test_10_all_rows_are_class_87(self):
        self.assertTrue(all(r["NANDINA"].startswith("87") for r in self.all_rows))

    def test_11_descriptions_are_nonempty(self):
        self.assertTrue(all(r["DESCRIPCION DE MERCANCIAS CONCATENADA"].strip() for r in self.all_rows))

    def test_12_eval_has_full_historical_support(self):
        hist_codes = {r["NANDINA"] for r in self.parts["historico"]}
        self.assertTrue(all(r["NANDINA"] in hist_codes for r in self.parts["evaluacion"]))

    def test_13_eval_concentration_is_under_gate(self):
        self.assertLessEqual(self.concentration["evaluacion"]["max_dam_pct"], 15.0)
        self.assertAlmostEqual(self.concentration["evaluacion"]["max_dam_pct"], 14.109848484848486)

    def test_14_metadata_matches_config_and_counts(self):
        self.assertEqual(self.metadata["version"], "v0.2")
        self.assertEqual(self.metadata["strategy"], "T5-safe-159")
        self.assertEqual(self.metadata["seed"], 2026)
        self.assertEqual(self.metadata["validation"]["eval_cases_without_historical_support"], 0)

    def test_15_v01_hashes_are_unchanged(self):
        for path, expected in V01_HASHES.items():
            self.assertEqual(sha256(path), expected, path)

    def test_16_v02_hashes_match_metadata(self):
        for rel, expected in self.metadata["output_sha256"].items():
            self.assertEqual(sha256(ROOT / rel), expected, rel)
        for rel, expected in self.metadata["audit_sha256"].items():
            self.assertEqual(sha256(ROOT / rel), expected, rel)

    def test_17_exact_duplicate_audit_hist_eval(self):
        row = next(r for r in self.exact_summary if r["comparison"] == "historico-evaluacion")
        self.assertEqual(int(row["affected_rows"]), 35)
        self.assertEqual(int(row["same_nandina_rows"]), 34)
        self.assertEqual(int(row["different_nandina_rows"]), 1)
        self.assertEqual(int(row["same_dam_rows"]), 0)

    def test_18_near_duplicate_audit_hist_eval(self):
        by_threshold = {float(r["threshold"]): r for r in self.near_summary}
        self.assertEqual(int(by_threshold[0.90]["affected_rows"]), 55)
        self.assertEqual(int(by_threshold[0.95]["affected_rows"]), 44)
        self.assertEqual(int(by_threshold[0.98]["affected_rows"]), 37)
        self.assertEqual(int(by_threshold[0.95]["pairs"]), 46)

    def test_19_support_bucket_counts(self):
        self.assertEqual(self.support_summary["bucket_cases"]["A. 1 DAM historica"], 27)
        self.assertEqual(self.support_summary["bucket_cases"]["B. 2 DAM historicas"], 21)
        self.assertEqual(self.support_summary["bucket_cases"]["C. 3-4 DAM historicas"], 425)
        self.assertEqual(self.support_summary["bucket_cases"]["D. 5+ DAM historicas"], 583)

    def test_20_config_freezes_explicit_dam_assignments(self):
        assignments = self.config["dam_assignments"]
        self.assertEqual(len(assignments["historico"]), 28)
        self.assertEqual(len(assignments["desarrollo"]), 6)
        self.assertEqual(len(assignments["evaluacion"]), 67)
        self.assertTrue(self.config["requirements"]["no_model_metric_selection"])

    def test_21_rerun_reproduces_dataset_hashes(self):
        with tempfile.TemporaryDirectory(prefix="split_v02_") as tmp:
            out_dir = Path(tmp) / "processed"
            audit_dir = Path(tmp) / "audits"
            env = os.environ.copy()
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            subprocess.run(
                [PYTHON, str(SCRIPT), "--output-dir", str(out_dir), "--audit-dir", str(audit_dir), "--overwrite"],
                cwd=ROOT,
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for split, source_path in SPLITS.items():
                self.assertEqual(sha256(out_dir / source_path.name), self.metadata["output_sha256"][str(source_path.relative_to(ROOT)).replace("\\", "/")])


if __name__ == "__main__":
    unittest.main()
