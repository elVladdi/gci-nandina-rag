import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import openpyxl


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "ingestion" / "prepare_new_historical_multisheet_v0.1.py"
SPEC = importlib.util.spec_from_file_location("new_historical_multisheet_contract_v01", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contract_for(root: Path) -> dict:
    return {
        "current_source": {"sha256": "", "size_bytes": 0, "sheet_order": ["Hoja2", "Hoja1"]},
        "historical_sheets": ["Hoja2", "Hoja1"],
        "allowed_new_sheets": ["NUEVA_01", "NUEVA_02"],
        "frozen_datasets": {
            "H100": {"path": str(root / "h100.csv"), "sha256": "", "rows": 1},
            "DEV": {"path": str(root / "dev.csv"), "sha256": "", "rows": 1},
            "EVAL": {"path": str(root / "eval.csv"), "sha256": "", "rows": 1},
        },
    }


def write_csv(path: Path, declaration: str, identifier: str) -> None:
    path.write_text(f"DECLARACION,id_unico\n{declaration},{identifier}\n", encoding="utf-8", newline="\n")


def workbook(path: Path, sheets: list[str]) -> None:
    book = openpyxl.Workbook()
    book.active.title = sheets[0]
    for name in sheets[1:]:
        book.create_sheet(name)
    book.save(path)


class TestNewHistoricalMultisheetContractV01(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="new_historical_contract_")
        self.root = Path(self.tmp.name)
        self.contract = contract_for(self.root)
        for label, filename, dam, identifier in (
            ("H100", "h100.csv", "HIST-DAM", "hist-1"),
            ("DEV", "dev.csv", "DEV-DAM", "dev-1"),
            ("EVAL", "eval.csv", "EVAL-DAM", "eval-1"),
        ):
            path = self.root / filename
            write_csv(path, dam, identifier)
            self.contract["frozen_datasets"][label]["sha256"] = sha256(path)

    def tearDown(self):
        self.tmp.cleanup()

    def test_01_explicit_new_sheet_is_required(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names([], self.contract)

    def test_02_historical_hoja2_cannot_be_new(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["Hoja2"], self.contract)

    def test_03_historical_hoja1_cannot_be_new(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["Hoja1"], self.contract)

    def test_04_nueva_01_is_accepted(self):
        self.assertEqual(MODULE.validate_new_sheet_names(["NUEVA_01"], self.contract), ["NUEVA_01"])

    def test_05_nueva_02_is_optionally_accepted(self):
        self.assertEqual(MODULE.validate_new_sheet_names(["NUEVA_02"], self.contract), ["NUEVA_02"])

    def test_06_unapproved_new_sheet_fails(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["OTRA_HOJA"], self.contract)

    def test_07_future_workbook_requires_historical_prefix_and_order(self):
        path = self.root / "future.xlsx"
        workbook(path, ["Hoja2", "Hoja1", "NUEVA_01", "NUEVA_02"])
        self.assertEqual(
            MODULE.validate_future_workbook_sheet_order(path, ["NUEVA_01"], self.contract),
            ["NUEVA_01"],
        )
        wrong = self.root / "wrong.xlsx"
        workbook(wrong, ["Hoja1", "Hoja2", "NUEVA_01"])
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_future_workbook_sheet_order(wrong, ["NUEVA_01"], self.contract)

    def test_08_future_parser_receives_explicit_sheet_name(self):
        path = self.root / "future.xlsx"
        workbook(path, ["Hoja2", "Hoja1", "NUEVA_01"])
        with patch.object(MODULE.sunat_series_parser, "parse_workbook", return_value="parsed") as parser:
            self.assertEqual(MODULE.parse_future_new_sheet(path, "NUEVA_01", self.contract), "parsed")
        parser.assert_called_once_with(path, sheet_name="NUEVA_01")

    def test_09_current_source_hash_mismatch_fails(self):
        path = self.root / "current.xlsx"
        workbook(path, ["Hoja2", "Hoja1"])
        self.contract["current_source"].update({"sha256": "0" * 64, "size_bytes": path.stat().st_size})
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_current_source(path, self.contract)

    def test_10_frozen_h100_hash_mismatch_fails(self):
        self.contract["frozen_datasets"]["H100"]["sha256"] = "0" * 64
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_frozen_datasets(self.contract)

    def test_11_frozen_dev_and_eval_hash_mismatches_fail(self):
        for label in ("DEV", "EVAL"):
            with self.subTest(label=label):
                changed = json.loads(json.dumps(self.contract))
                changed["frozen_datasets"][label]["sha256"] = "0" * 64
                with self.assertRaises(MODULE.ContractViolation):
                    MODULE.validate_frozen_datasets(changed)

    def test_12_dev_eval_dam_is_excluded_from_future_history(self):
        result = MODULE.audit_future_rows([{"DECLARACION": "DEV-DAM", "id_unico": "new-1"}], self.contract)
        self.assertEqual(len(result["EXCLUDED_FIXED_DEV_EVAL_DAM"]), 1)
        self.assertFalse(result["accepted_for_later_curation"])

    def test_13_existing_id_unico_overlap_is_detected(self):
        result = MODULE.audit_future_rows([{"DECLARACION": "NEW-DAM", "id_unico": "hist-1"}], self.contract)
        self.assertEqual(len(result["EXISTING_FROZEN_ID_UNICO_OVERLAP"]), 1)

    def test_14_h100_processed_directory_cannot_be_a_future_output(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_future_output_dir(ROOT / "data" / "processed")
        self.assertEqual(MODULE.validate_future_output_dir(self.root / "future_outputs"), self.root / "future_outputs")

    def test_15_source_freeze_is_binary_identical_and_source_is_unchanged(self):
        source = self.root / "source.xlsx"
        source.write_bytes(b"PK\x03\x04binary-xlsx-payload")
        expected = sha256(source)
        before = source.read_bytes()
        archive = self.root / "archive" / "source.xlsx"
        result = MODULE.freeze_source_bytes(source, archive, expected)
        self.assertEqual(archive.read_bytes(), before)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(result["source_sha256_after"], result["archive_sha256"])
        self.assertEqual(result["copy_method"], "Python shutil.copy2 binary copy")

    def test_16_no_first_worksheet_selection_for_future_new_sheets(self):
        source = MODULE_PATH.read_text(encoding="utf-8")
        self.assertIn("parse_workbook(workbook_path, sheet_name=sheet_name)", source)
        self.assertNotIn("worksheets[0]", source)

    def test_17_build_evalset_pipeline_is_absent_from_expansion_contract(self):
        config = json.loads(
            (ROOT / "src" / "configs" / "new_historical_multisheet_contract_v0.1.json").read_text(encoding="utf-8")
        )
        self.assertEqual(config["future_parser"]["forbidden_pipeline"], "src.evaluation.build_evalset_from_sunat_excel")
        self.assertEqual(config["future_parser"]["entrypoint"], "parse_workbook")


if __name__ == "__main__":
    unittest.main()
