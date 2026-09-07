"""Contract tests for the non-executing 0B-05C corrective orchestration."""

from __future__ import annotations

import copy
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

from src.experiments.run_d1a_corrective_0b05c_v01 import (
    AUDIT_SPEC_PATH,
    BUILDER_FILENAMES,
    EVALUATOR_FILENAMES,
    RUNNER_FILENAMES,
    ContractViolation,
    authorized_execution_provenance,
    build_case_comparison,
    build_execution_manifest,
    contractual_ledger_paths,
    derive_runtime_config,
    diff_paths,
    expected_paths,
    git_hash_object,
    load_json,
    patched_corpus_bytes,
    preflight,
    project_path,
    preflight_provenance,
    relative_path,
    sha256_file,
    validate_contract_inputs,
    write_hash_ledger,
    write_json,
)


ROOT = Path(__file__).resolve().parents[1]


class D1aCorrective0B05cRunnerV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = load_json(project_path(ROOT, AUDIT_SPEC_PATH))

    def test_01_preflight_is_read_only_and_fails_closed_when_the_frozen_model_is_unavailable(self) -> None:
        for relative in self.spec["orchestration"]["future_roots"]:
            self.assertFalse(project_path(ROOT, relative).exists())
        with self.assertRaisesRegex(ContractViolation, "Frozen D1a model SHA changed"):
            preflight(ROOT)
        self.assertNotIn("sentence_transformers", sys.modules)
        for relative in self.spec["orchestration"]["future_roots"]:
            self.assertFalse(project_path(ROOT, relative).exists())

    def test_02_patch_is_exactly_two_codes_and_preserves_official_context(self) -> None:
        definition = self.spec["corrected_normative_corpus"]["definition"]
        self.assertEqual(definition["patch_scope"], "EXACTLY_TWO_NANDINA8_DOCUMENTS")
        self.assertEqual([patch["code"] for patch in definition["patches"]], ["87044110", "87045110"])
        for patch in definition["patches"]:
            self.assertEqual(patch["replacement"]["texto"], "Inferior a 4,537 t. Contexto: Sección XVII / Capítulo 87.")
            self.assertEqual(patch["replacement"]["version"], "Decision_906")

    def test_03_patch_derivation_is_in_memory_and_does_not_create_the_corrected_corpus(self) -> None:
        original = project_path(ROOT, self.spec["original_normative_corpus"]["path"])
        before = original.read_bytes()
        corrected = patched_corpus_bytes(before, self.spec)
        self.assertEqual(original.read_bytes(), before)
        self.assertNotEqual(corrected, before)
        self.assertFalse(project_path(ROOT, self.spec["corrected_normative_corpus"]["prospective_path"]).exists())

    def test_04_runtime_config_derivation_is_deterministic_and_limited(self) -> None:
        original_config = load_json(project_path(ROOT, self.spec["orchestration"]["original_config"]["path"]))
        first = derive_runtime_config(original_config, self.spec, "a" * 64)
        second = derive_runtime_config(original_config, self.spec, "a" * 64)
        self.assertEqual(first, second)
        self.assertEqual(
            diff_paths(original_config, first),
            {
                "frozen_inputs.normative_corpus",
                "frozen_inputs.normative_corpus_sha256",
                "index.output_dir",
                "outputs.evaluation_dir",
            },
        )

    def test_05_builder_filenames_in_spec_bind_to_the_real_builder_contract(self) -> None:
        paths = expected_paths(ROOT, self.spec)["index"]
        self.assertEqual([path.relative_to(paths[0].parents[1]).as_posix() for path in paths], list(BUILDER_FILENAMES))
        self.assertEqual(
            self.spec["evaluation"]["required_index_contract"]["metadata_filename"],
            "text2trade_mnrl_nandina8_v02_run_metadata.json",
        )

    def test_06_evaluator_filenames_in_spec_bind_to_the_real_evaluator_contract(self) -> None:
        paths = expected_paths(ROOT, self.spec)["evaluation"]
        self.assertEqual([path.name for path in paths], list(EVALUATOR_FILENAMES))
        self.assertEqual(
            self.spec["evaluation"]["required_index_contract"]["vector_integrity_filename"],
            "vector_integrity_gate_v0.2.json",
        )

    def test_07_runner_has_versioned_producers_for_comparison_and_hash_ledger(self) -> None:
        paths = expected_paths(ROOT, self.spec)["runner"]
        self.assertEqual([path.name for path in paths], list(RUNNER_FILENAMES))
        outputs = self.spec["orchestration"]["runner_outputs"]
        self.assertTrue(outputs["aggregate_comparison"].endswith(paths[0].name))
        self.assertTrue(outputs["case_level_comparison"].endswith(paths[1].name))
        self.assertTrue(outputs["hash_ledger"].endswith(paths[2].name))

    def test_08_preflight_binds_runner_builder_and_evaluator_code_identities(self) -> None:
        identities = (
            self.spec["orchestration"]["runner"],
            self.spec["index_builder"]["code_identity"],
            self.spec["evaluation"]["code_identity"],
        )
        for identity in identities:
            path = project_path(ROOT, identity["path"])
            self.assertEqual(git_hash_object(ROOT, identity["path"]), identity["git_blob_sha"])
            if identity["revision"] == "MICROCLOSE_WORKTREE_CONTENT":
                self.assertEqual(sha256_file(path), identity["sha256"])

    def test_09_existing_prospective_root_fails_closed(self) -> None:
        modified = copy.deepcopy(self.spec)
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            modified["orchestration"]["future_roots"] = [str(root)]
            with self.assertRaises(ContractViolation):
                validate_contract_inputs(ROOT, modified)

    def test_10_contractual_json_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "artifact.json"
            write_json(path, {"value": 1})
            with self.assertRaises(ContractViolation):
                write_json(path, {"value": 2})

    def test_11_case_level_contract_freezes_rank_zero_convention_and_all_required_fields(self) -> None:
        contract = self.spec["orchestration"]["comparison_contract"]
        self.assertEqual(contract["rank_convention"], "0=NOT_FOUND_AT_200")
        for field in (
            "case_id",
            "original_rank_ref",
            "corrected_rank_ref",
            "original_hit_200",
            "corrected_hit_200",
            "original_rank_87044110",
            "corrected_rank_87045110",
        ):
            self.assertIn(field, contract["case_fields"])

    def test_12_numerical_execution_remains_not_authorized(self) -> None:
        self.assertEqual(self.spec["authorization"]["D1A_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")

    def test_13_case_level_producer_materializes_every_contractual_field_and_rank_zero(self) -> None:
        spec = copy.deepcopy(self.spec)
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            original_case = root / "fixture/original_case.csv"
            original_trace = root / "fixture/original_trace.jsonl"
            corrected_root = root / "fixture/corrected"
            original_case.parent.mkdir(parents=True)
            corrected_root.mkdir(parents=True)
            original_case.write_text("case_id,nandina_ref,rank_ref\ncase-1,87044110,101\n", encoding="utf-8", newline="\n")
            (corrected_root / "d1a_case_summary.csv").write_text(
                "case_id,nandina_ref,rank_ref\ncase-1,87044110,100\n", encoding="utf-8", newline="\n"
            )
            original_codes = [f"8704{i:04d}" for i in range(1, 201)]
            corrected_codes = list(reversed(original_codes))
            original_trace.write_text(
                json.dumps({"case_id": "case-1", "candidate_codes": original_codes}) + "\n", encoding="utf-8", newline="\n"
            )
            (corrected_root / "d1a_ranked_codes_top200.jsonl").write_text(
                json.dumps({"case_id": "case-1", "candidate_codes": corrected_codes}) + "\n", encoding="utf-8", newline="\n"
            )
            spec["evaluation"]["primary_control_case_summary"]["path"] = "fixture/original_case.csv"
            spec["evaluation"]["primary_control_ranking_trace"]["path"] = "fixture/original_trace.jsonl"
            spec["evaluation"]["prospective_output_root"] = "fixture/corrected"
            row = build_case_comparison(root, spec)[0]
        required_case_fields = set(spec["orchestration"]["comparison_contract"]["case_fields"])
        self.assertLessEqual(required_case_fields, set(row))
        self.assertEqual(row["original_hit_100"], 0)
        self.assertEqual(row["corrected_hit_100"], 1)
        self.assertEqual(row["original_hit_200"], 1)
        self.assertEqual(row["corrected_hit_200"], 1)
        self.assertEqual(row["original_rank_87045110"], 0)
        self.assertEqual(row["corrected_rank_87045110"], 0)
        self.assertEqual(row["rank_convention"], "0=NOT_FOUND_AT_200")

    def test_14_hash_ledger_covers_exactly_the_frozen_contract_excluding_only_itself(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            contractual = contractual_ledger_paths(root, self.spec)
            paths = expected_paths(root, self.spec)
            expected_contractual_paths = [
                project_path(root, self.spec["corrected_normative_corpus"]["prospective_path"]),
                project_path(root, self.spec["orchestration"]["runtime_config_path"]),
                *paths["index"],
                *paths["evaluation"],
                paths["runner"][0],
                paths["runner"][1],
                paths["runner"][3],
            ]
            self.assertEqual(contractual, expected_contractual_paths)
            for index, path in enumerate(expected_contractual_paths):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"contractual-{index}\n", encoding="utf-8", newline="\n")
            ledger = write_hash_ledger(root, self.spec)
            with ledger.open("r", encoding="utf-8", newline="") as handle:
                ledger_paths = [row["path"] for row in csv.DictReader(handle)]
            expected = [relative_path(root, path) for path in expected_contractual_paths]
            self.assertEqual(ledger_paths, expected)
            self.assertEqual(len(ledger_paths), 17)
            self.assertNotIn(relative_path(root, ledger), ledger_paths)
            self.assertIn(self.spec["orchestration"]["runtime_config_path"], ledger_paths)
            self.assertIn(self.spec["orchestration"]["runner_outputs"]["execution_manifest"], ledger_paths)

    def test_15_preflight_and_authorized_execution_provenance_are_distinct_without_execution(self) -> None:
        proof = preflight_provenance("a" * 64, "b" * 64, ["future/root"])
        self.assertEqual(proof["mode"], "PREFLIGHT_ONLY")
        self.assertEqual(proof["execution_mode"], "PREFLIGHT_ONLY")
        self.assertFalse(proof["numerical_execution_occurred"])
        future = authorized_execution_provenance(proof)
        self.assertEqual(future["mode"], "AUTHORIZED_EXECUTION")
        self.assertEqual(future["execution_mode"], "AUTHORIZED_EXECUTION")
        self.assertTrue(future["numerical_execution_occurred"])
        manifest = build_execution_manifest(ROOT, self.spec, proof)
        self.assertEqual(manifest["preflight_status"], "PASS")
        self.assertEqual(manifest["execution_mode"], "AUTHORIZED_EXECUTION")
        self.assertTrue(manifest["numerical_execution_occurred"])
        self.assertIsNone(manifest["hash_ledger"]["sha256"])


if __name__ == "__main__":
    unittest.main()
