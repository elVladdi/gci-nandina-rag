import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
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
        "preexisting_source_sheets": ["Hoja2", "Hoja1"],
        "historically_processed_sheet": "Hoja2",
        "historically_processed_sheet_index": 0,
        "historical_sheet_selection": "DEFAULT_FIRST_WORKSHEET",
        "historically_processed_second_sheet": False,
        "new_sheet_sets": {
            "NEW_SHEET_SET_1": ["NUEVA_01"],
            "NEW_SHEET_SET_2": ["NUEVA_01", "NUEVA_02"],
        },
        "future_parser": {"module": "src.ingestion.sunat_series_parser"},
        "future_curation": {"eligible_class": "87"},
        "capacity": {
            "H100_rows": 2950,
            "H150_target": 4425,
            "H200_target": 5900,
            "minimum_net_new_eligible_rows_for_H150": 1475,
            "minimum_net_new_eligible_rows_for_H200": 2950,
        },
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


def normalized_row(declaration: str, identifier: str, description: str, sheet_name: str = "NUEVA_01") -> dict[str, str]:
    return {
        "id_unico": identifier,
        "DECLARACION": declaration,
        "SERIE": "1",
        "Clase": "87",
        "Partida": "8701",
        "Sub Partida": "870100",
        "NANDINA": "87010000",
        "NANDINA ORIGINAL": "87.01.00.00",
        "DESCRIPCION DE PARTIDA ARANCELARIA": "PARTIDA SINTETICA",
        "DESCRIPCION DE MERCANCIAS CONCATENADA": description,
        "__sheet_name": sheet_name,
        "__source_file": "fixture.xlsx",
        "__series_row_start": "10",
        "__parse_warnings": "",
    }


def parser_result(rows: list[dict[str, str]]) -> SimpleNamespace:
    columns = []
    for row in rows:
        for column in row:
            if column not in columns:
                columns.append(column)
    return SimpleNamespace(columns=columns, rows=rows)


def write_frozen_csv(path: Path, declaration: str, identifier: str, description: str) -> None:
    path.write_text(
        "case_id,id_unico,DECLARACION,NANDINA,DESCRIPCION DE MERCANCIAS CONCATENADA\n"
        f"FROZEN-1,{identifier},{declaration},87010000,{description}\n",
        encoding="utf-8",
        newline="\n",
    )


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

    def test_05_nueva_02_alone_fails(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["NUEVA_02"], self.contract)

    def test_06_unapproved_new_sheet_fails(self):
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["OTRA_HOJA"], self.contract)

    def test_07_future_workbook_requires_historical_prefix_and_order(self):
        path = self.root / "future.xlsx"
        workbook(path, ["Hoja2", "Hoja1", "NUEVA_01", "NUEVA_02"])
        self.assertEqual(
            MODULE.validate_future_workbook_sheet_order(path, ["NUEVA_01", "NUEVA_02"], self.contract),
            ["NUEVA_01", "NUEVA_02"],
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
        self.assertEqual(config["historically_processed_sheet"], "Hoja2")
        self.assertEqual(config["preexisting_source_sheets"], ["Hoja2", "Hoja1"])


class TestProspectiveIngestionPath(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="new_historical_ingest_")
        self.root = Path(self.tmp.name)
        self.contract = contract_for(self.root)
        for label, filename, dam, identifier, description in (
            ("H100", "h100.csv", "HIST-DAM", "hist-1", "coincidencia exacta"),
            ("DEV", "dev.csv", "DEV-DAM", "dev-1", "descripcion dev"),
            ("EVAL", "eval.csv", "EVAL-DAM", "eval-1", "descripcion eval"),
        ):
            path = self.root / filename
            write_frozen_csv(path, dam, identifier, description)
            self.contract["frozen_datasets"][label]["sha256"] = sha256(path)

    def tearDown(self):
        self.tmp.cleanup()

    def future_workbook(self, names: list[str]) -> Path:
        path = self.root / "future.xlsx"
        workbook(path, ["Hoja2", "Hoja1", *names])
        return path

    def output_dirs(self) -> tuple[Path, Path]:
        return self.root / "interim", self.root / "audits"

    def test_18_nueva_01_and_nueva_02_are_the_only_valid_ordered_sets(self):
        self.assertEqual(MODULE.validate_new_sheet_names(["NUEVA_01"], self.contract), ["NUEVA_01"])
        self.assertEqual(
            MODULE.validate_new_sheet_names(["NUEVA_01", "NUEVA_02"], self.contract),
            ["NUEVA_01", "NUEVA_02"],
        )
        with self.assertRaises(MODULE.ContractViolation):
            MODULE.validate_new_sheet_names(["NUEVA_02", "NUEVA_01"], self.contract)

    def test_19_two_new_sheets_generate_two_explicit_parser_calls(self):
        path = self.future_workbook(["NUEVA_01", "NUEVA_02"])
        first = parser_result([normalized_row("NEW-1", "new-1", "uno", "NUEVA_01")])
        second = parser_result([normalized_row("NEW-2", "new-2", "dos", "NUEVA_02")])
        with patch.object(MODULE.sunat_series_parser, "parse_workbook", side_effect=[first, second]) as parser:
            parsed = MODULE.parse_future_new_sheets(path, ["NUEVA_01", "NUEVA_02"], self.contract)
        self.assertEqual([name for name, _ in parsed], ["NUEVA_01", "NUEVA_02"])
        self.assertEqual(
            parser.call_args_list,
            [
                ((path,), {"sheet_name": "NUEVA_01"}),
                ((path,), {"sheet_name": "NUEVA_02"}),
            ],
        )

    def test_20_classify_rows_receives_the_combined_new_sheet_rows(self):
        path = self.future_workbook(["NUEVA_01", "NUEVA_02"])
        first = parser_result([normalized_row("NEW-1", "new-1", "uno", "NUEVA_01")])
        second = parser_result([normalized_row("NEW-2", "new-2", "dos", "NUEVA_02")])
        interim, audit = self.output_dirs()
        original = MODULE.build_data_aduanas_splits.classify_rows
        with patch.object(MODULE.sunat_series_parser, "parse_workbook", side_effect=[first, second]), patch.object(
            MODULE.build_data_aduanas_splits, "classify_rows", wraps=original
        ) as classifier:
            MODULE.ingest_new_data(path, ["NUEVA_01", "NUEVA_02"], self.contract, interim, audit)
        self.assertEqual(len(classifier.call_args.args[1]), 2)
        self.assertEqual(classifier.call_args.args[2], "87")

    def test_21_dam_and_frozen_id_overlap_are_both_recorded(self):
        result = MODULE.audit_future_rows(
            [{"DECLARACION": "DEV-DAM", "id_unico": "hist-1"}], self.contract
        )
        self.assertEqual(len(result["EXCLUDED_FIXED_DEV_EVAL_DAM"]), 1)
        self.assertEqual(len(result["EXISTING_FROZEN_ID_UNICO_OVERLAP"]), 1)
        self.assertFalse(result["accepted_for_later_curation"])
        self.assertEqual(
            result["audited_rows"][0]["exclusion_reasons"],
            "EXCLUDED_FIXED_DEV_EVAL_DAM|EXISTING_FROZEN_ID_UNICO_OVERLAP",
        )

    def test_22_eligible_pool_only_contains_rows_without_blocking_causes(self):
        rows = [
            {"DECLARACION": "NEW-DAM", "id_unico": "new-1"},
            {"DECLARACION": "DEV-DAM", "id_unico": "hist-1"},
        ]
        result = MODULE.audit_future_rows(rows, self.contract)
        self.assertEqual([row["id_unico"] for row in result["accepted_for_later_curation"]], ["new-1"])

    def test_23_h100_dev_eval_are_never_written_by_synthetic_ingest(self):
        path = self.future_workbook(["NUEVA_01"])
        frozen_paths = [Path(item["path"]) for item in self.contract["frozen_datasets"].values()]
        before = [item.read_bytes() for item in frozen_paths]
        interim, audit = self.output_dirs()
        with patch.object(
            MODULE.sunat_series_parser,
            "parse_workbook",
            return_value=parser_result([normalized_row("NEW-DAM", "new-1", "nueva descripcion")]),
        ):
            MODULE.ingest_new_data(path, ["NUEVA_01"], self.contract, interim, audit)
        self.assertEqual([item.read_bytes() for item in frozen_paths], before)

    def test_24_exact_and_near_duplicate_audit_does_not_exclude_eligible_rows(self):
        path = self.future_workbook(["NUEVA_01"])
        interim, audit = self.output_dirs()
        with patch.object(
            MODULE.sunat_series_parser,
            "parse_workbook",
            return_value=parser_result([normalized_row("NEW-DAM", "new-1", "coincidencia exacta")]),
        ):
            result = MODULE.ingest_new_data(path, ["NUEVA_01"], self.contract, interim, audit)
        self.assertEqual(len(result["eligible_rows"]), 1)
        self.assertIn("exact_summary", result["paths"]["duplicate_nearduplicate"].read_text(encoding="utf-8-sig"))

    def test_25_capacity_thresholds_are_frozen(self):
        below_h150 = MODULE.capacity_descriptor(1474, self.contract)
        h150 = MODULE.capacity_descriptor(1475, self.contract)
        below_h200 = MODULE.capacity_descriptor(2949, self.contract)
        h200 = MODULE.capacity_descriptor(2950, self.contract)
        self.assertFalse(below_h150["H150_FEASIBLE"])
        self.assertTrue(h150["H150_FEASIBLE"])
        self.assertFalse(below_h200["H200_FEASIBLE"])
        self.assertTrue(h200["H200_FEASIBLE"])

    def test_26_synthetic_cli_ingest_generates_only_temporary_prospective_outputs(self):
        path = self.future_workbook(["NUEVA_01"])
        contract_path = self.root / "contract.json"
        contract_path.write_text(json.dumps(self.contract), encoding="utf-8")
        interim, audit = self.output_dirs()
        with patch.object(
            MODULE.sunat_series_parser,
            "parse_workbook",
            return_value=parser_result([normalized_row("NEW-DAM", "new-1", "nueva descripcion")]),
        ):
            exit_code = MODULE.main(
                [
                    "--ingest-new-data",
                    "--future-workbook",
                    str(path),
                    "--new-sheet",
                    "NUEVA_01",
                    "--contract",
                    str(contract_path),
                    "--future-output-dir",
                    str(interim),
                    "--future-audit-dir",
                    str(audit),
                ]
            )
        self.assertEqual(exit_code, 0)
        self.assertTrue((interim / "new_historical_eligible.csv").is_file())
        manifest = json.loads((audit / "new_historical_ingestion_manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["retrieval_executed"])
        self.assertFalse(manifest["creates_H150_or_H200"])

    def test_27_ingest_path_has_no_bm25_execution(self):
        source = MODULE_PATH.read_text(encoding="utf-8").lower()
        self.assertNotIn("bm25", source)


if __name__ == "__main__":
    unittest.main()
