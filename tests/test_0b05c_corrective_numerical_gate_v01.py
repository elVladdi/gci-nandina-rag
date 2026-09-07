"""Fail-closed contract tests for the prospective 0B-05C numerical gate."""

from __future__ import annotations

import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from src.experiments.prepare_0b05c_corrective_numerical_gate_v01 import (
    ARMS,
    AUDIT_ROOT,
    ContractViolation,
    D1A_SPEC_PATH,
    EVALUATOR_PATH,
    FROZEN_EXECUTION_DEPENDENCIES,
    INTEGRATED_BASE_COMMIT,
    RUNNER_PATH,
    TARGET_CODES,
    build_bundle,
    canonical_json_bytes,
    execute,
    future_roots,
    head_text_identity,
    integrated_base_is_ancestor,
    posix_relative,
    preflight,
    require_posix_serialization,
    require_frozen_bundle_matches,
    require_absent,
    validate_current_text_identity,
)
from src.experiments.run_0b05c_corrective_numerical_v01 import execute_authorized, preflight as runner_preflight
from src.experiments import evaluate_normative_bm25_flat_data_aduanas_v02 as frozen_flat_runner
from src.experiments import evaluate_normative_bm25_hierarchical_data_aduanas_v02 as frozen_hierarchical_runner
from src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 import compare_control_reproduction, ev04_corrected_execution_permitted
from src.experiments.run_d1a_corrective_0b05c_v01 import git_blob_sha256, git_head_blob_sha, sha256_bytes


ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class CorrectiveNumericalGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = preflight(ROOT)["bundle"]
        cls.gate = load_json(str(AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"))
        cls.ev03 = load_json(str(AUDIT_ROOT / ARMS["EV03"]["spec_name"]))
        cls.ev04 = load_json(str(AUDIT_ROOT / ARMS["EV04"]["spec_name"]))
        cls.ev03_overlap = load_json(str(AUDIT_ROOT / ARMS["EV03"]["overlap_name"]))
        cls.ev04_overlap = load_json(str(AUDIT_ROOT / ARMS["EV04"]["overlap_name"]))
        cls.manifest = load_json(str(AUDIT_ROOT / "0b05c_corrective_numerical_gate_artifact_manifest_v0.1.json"))

    def test_01_ev03_original_inputs_and_outputs_are_linked(self) -> None:
        identity = self.ev03["original_run_identity"]
        self.assertEqual(identity["status"], "FULLY_VERIFIABLE_FROM_FROZEN_ARTIFACTS")
        self.assertEqual(self.ev03["frozen_inputs"]["eval"]["canonical_blob_sha256"], "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941")
        self.assertEqual(self.ev03["primary_original_control"]["decision"], "Decision_885")
        self.assertEqual(self.ev03["frozen_inputs"]["bm25_parameters"]["k1"], 1.5)
        self.assertEqual(self.ev03["frozen_inputs"]["bm25_parameters"]["b"], 0.75)

    def test_02_ev04_original_outputs_are_linked_and_historical_source_limitation_is_explicit(self) -> None:
        identity = self.ev04["original_run_identity"]
        self.assertEqual(identity["status"], "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS")
        self.assertIn(ARMS["EV04"]["runner"], identity["historical_missing_tracked_paths"])
        self.assertIn(ARMS["EV04"]["corpus"], identity["historical_missing_tracked_paths"])
        self.assertEqual(self.ev04["frozen_inputs"]["bm25_parameters"]["retrieval_depth"], 200)
        self.assertEqual(self.ev04["frozen_inputs"]["bm25_parameters"]["raw_retrieval_depth"], 7648)

    def test_03_d1a_specification_is_referenced_by_identity_not_reconstructed(self) -> None:
        reference = self.gate["d1a_existing_specification"]["reference"]
        self.assertEqual(reference["path"], D1A_SPEC_PATH)
        self.assertEqual(reference["git_blob_sha"], git_head_blob_sha(ROOT, D1A_SPEC_PATH))
        self.assertEqual(reference["canonical_blob_sha256"], git_blob_sha256(ROOT, reference["git_blob_sha"]))
        self.assertEqual(self.gate["d1a_existing_specification"]["D1A_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")

    def test_04_ev03_patch_scope_is_exactly_two_entries(self) -> None:
        patches = self.ev03["corrective_corpus"]["patches"]
        self.assertEqual([patch["code"] for patch in patches], list(TARGET_CODES))
        self.assertEqual(self.ev03["corrective_corpus"]["patch_scope"], "EXACTLY_TWO_NANDINA8_DOCUMENTS")
        self.assertTrue(all(patch["match"]["version"] == "Decision_885" for patch in patches))

    def test_05_ev04_patch_scope_preserves_hierarchy_nodes_and_changes_declared_leaf_representations(self) -> None:
        patches = self.ev04["corrective_corpus"]["patches"]
        self.assertEqual([patch["code"] for patch in patches], list(TARGET_CODES))
        for patch in patches:
            self.assertEqual(patch["match"]["version"], "hierarchical_v0.1")
            self.assertEqual(patch["replacement"]["titulo"], "Inferior a 4,537 t")
            self.assertEqual(patch["match"]["preserved_node_fields"]["nandina_8d"], patch["code"])

    def test_06_ev03_complete_frozen_ranking_overlap_is_recorded_without_retrieval(self) -> None:
        self.assertEqual(self.ev03_overlap["cases_scanned"], 1056)
        self.assertEqual(self.ev03_overlap["ranking_depth"], 100)
        self.assertEqual(self.ev03_overlap["total_occurrences"], 1)
        self.assertEqual(self.ev03_overlap["per_code"]["87044110"]["minimum_rank"], 100)
        self.assertEqual(self.ev03_overlap["per_code"]["87045110"]["occurrences"], 0)
        self.assertFalse(self.ev03_overlap["retrieval_executed"])

    def test_07_ev04_complete_frozen_ranking_overlap_is_recorded_without_retrieval(self) -> None:
        self.assertEqual(self.ev04_overlap["cases_scanned"], 1056)
        self.assertEqual(self.ev04_overlap["ranking_depth"], 200)
        self.assertEqual(self.ev04_overlap["total_occurrences"], 148)
        self.assertEqual(self.ev04_overlap["affected_cases"], 74)
        self.assertEqual(self.ev04_overlap["per_code"]["87044110"]["occurrences"], 74)
        self.assertEqual(self.ev04_overlap["per_code"]["87045110"]["maximum_rank"], 192)
        self.assertFalse(self.ev04_overlap["evaluation_metrics_computed"])

    def test_08_unified_authorization_is_not_opened(self) -> None:
        authorization = self.gate["authorization"]
        for key in ("EV03_NUMERICAL_EXECUTION", "EV04_NUMERICAL_EXECUTION", "D1A_NUMERICAL_EXECUTION", "UNIFIED_0B05C_NUMERICAL_EXECUTION"):
            self.assertEqual(authorization[key], "NOT_AUTHORIZED")
        self.assertEqual(self.gate["gate_status"], "CANDIDATE_PENDING_EXTERNAL_AUDIT")

    def test_09_all_prospective_roots_remain_absent(self) -> None:
        d1a = self.bundle["gate"]["d1a_existing_specification"]
        spec = load_json(D1A_SPEC_PATH)
        for relative in future_roots(spec):
            self.assertFalse((ROOT / relative).exists(), relative)
        self.assertEqual(d1a["D1A_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")

    def test_10_preflight_is_read_only(self) -> None:
        before = {path: path.stat().st_mtime_ns for path in (ROOT / AUDIT_ROOT).glob("*")}
        result = preflight(ROOT)
        after = {path: path.stat().st_mtime_ns for path in (ROOT / AUDIT_ROOT).glob("*")}
        self.assertEqual(result["mode"], "PREFLIGHT_ONLY")
        self.assertEqual(before, after)

    def test_11_execute_is_fail_closed_without_side_effects(self) -> None:
        spec = load_json(D1A_SPEC_PATH)
        roots = future_roots(spec)
        with self.assertRaisesRegex(ContractViolation, "not authorized"):
            execute(ROOT)
        self.assertTrue(all(not (ROOT / relative).exists() for relative in roots))

    def test_12_no_overwrite_or_resume_is_permitted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            existing = root / "partial"
            existing.mkdir()
            with self.assertRaises(ContractViolation):
                require_absent(root, ["partial"], "Prospective numerical root")

    def test_13_current_text_identity_rejects_semantic_change_but_uses_canonical_git_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / ".git").mkdir()
            # A real Git fixture is used to test the portable identity primitive.
            import subprocess

            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            source = root / "frozen.txt"
            source.write_bytes(b"value=1\n")
            subprocess.run(["git", "add", "frozen.txt"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Codex", "-c", "user.email=codex@example.invalid", "commit", "-m", "fixture"], cwd=root, check=True, capture_output=True)
            identity = head_text_identity(root, "frozen.txt")
            source.write_bytes(b"value=1\r\n")
            self.assertEqual(validate_current_text_identity(root, identity, "fixture"), b"value=1\n")
            source.write_bytes(b"value=2\n")
            with self.assertRaises(ContractViolation):
                validate_current_text_identity(root, identity, "fixture")

    def test_14_metric_contracts_are_frozen_but_no_corrective_metric_is_present(self) -> None:
        self.assertTrue(self.ev03["primary_original_control"]["metric_definitions"])
        self.assertTrue(self.ev04["primary_original_control"]["metric_definitions"])
        for spec in (self.ev03, self.ev04):
            self.assertFalse(spec["authorization"]["corrective_metrics_computed"])
            self.assertEqual(spec["specification_status"], "CLOSED_PROSPECTIVELY/PENDING_EXTERNAL_AUDIT")

    def test_15_bundle_is_deterministic(self) -> None:
        second = build_bundle(ROOT)
        self.assertEqual(sha256_bytes(canonical_json_bytes(self.bundle["gate"])), sha256_bytes(canonical_json_bytes(second["gate"])))
        self.assertEqual(self.gate["integrated_base_commit"], INTEGRATED_BASE_COMMIT)
        self.assertTrue(integrated_base_is_ancestor(ROOT))

    def test_16_frozen_artifacts_reject_post_freeze_identity_drift(self) -> None:
        require_frozen_bundle_matches(ROOT, self.bundle)
        changed = copy.deepcopy(self.bundle)
        changed["specifications"]["EV03"]["frozen_inputs"]["runner"]["git_blob_sha"] = "0" * 40
        with self.assertRaisesRegex(ContractViolation, "no longer matches live canonical inputs"):
            require_frozen_bundle_matches(ROOT, changed)

    def test_17_execution_binding_is_committed_and_commands_are_bound(self) -> None:
        binding = self.gate["corrective_execution_binding"]
        self.assertEqual(binding["orchestration_runner"]["path"], RUNNER_PATH)
        self.assertEqual(binding["corrective_evaluator"]["path"], EVALUATOR_PATH)
        self.assertEqual(set(binding["frozen_dependencies"]), set(FROZEN_EXECUTION_DEPENDENCIES))
        self.assertIn("ev03_build_command", self.ev03["prospective_execution"]["commands"])
        self.assertIn("ev04_control_reproduction_evaluate_command", self.ev04["prospective_execution"]["commands"])

    def test_18_all_static_contract_paths_are_posix(self) -> None:
        for payload in (self.gate, self.ev03, self.ev04, self.ev03_overlap, self.ev04_overlap, self.manifest):
            require_posix_serialization(payload, "fixture")

    def test_19_ev04_reproduction_stays_mandatory_and_original_stays_unverified(self) -> None:
        control = self.ev04["primary_original_control"]["control_reproduction"]
        self.assertEqual(self.ev04["original_run_identity"]["status"], "NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS")
        self.assertEqual(control["gate"], "EV04_DECISION885_REPRODUCTION_GATE")
        self.assertEqual(control["requirement"], "MANDATORY")
        self.assertEqual(control["current_state"], "NOT_EXECUTED")
        self.assertEqual(control["comparison"]["ranking"]["scope"], "EXACT_EFFECTIVE_FULL_TOP200_CASE_LEVEL")

    def test_20_runner_preflight_and_execute_authorized_have_no_side_effects(self) -> None:
        roots = future_roots(load_json(D1A_SPEC_PATH))
        result = runner_preflight(ROOT)
        self.assertEqual(result["mode"], "PREFLIGHT_ONLY")
        with self.assertRaisesRegex(ContractViolation, "not authorized"):
            execute_authorized(ROOT)
        self.assertTrue(all(not (ROOT / relative).exists() for relative in roots))

    def test_21_integrated_base_ancestry_accepts_descendants_and_rejects_unrelated_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            (root / "README.md").write_text("base\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Codex", "-c", "user.email=codex@example.invalid", "commit", "-m", "base"], cwd=root, check=True, capture_output=True)
            base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
            self.assertTrue(integrated_base_is_ancestor(root, base))
            (root / "README.md").write_text("descendant\n", encoding="utf-8")
            subprocess.run(["git", "-c", "user.name=Codex", "-c", "user.email=codex@example.invalid", "commit", "-am", "descendant"], cwd=root, check=True, capture_output=True)
            self.assertTrue(integrated_base_is_ancestor(root, base))
            subprocess.run(["git", "checkout", "--orphan", "unrelated"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "rm", "-f", "README.md"], cwd=root, check=True, capture_output=True)
            (root / "README.md").write_text("unrelated\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Codex", "-c", "user.email=codex@example.invalid", "commit", "-m", "unrelated"], cwd=root, check=True, capture_output=True)
            self.assertFalse(integrated_base_is_ancestor(root, base))

    def test_22_control_reproduction_requires_an_exact_fixture_and_blocks_a_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            expected_ranking = root / "expected_ranking.csv"
            actual_ranking = root / "actual_ranking.csv"
            expected_summary = root / "expected_summary.csv"
            actual_summary = root / "actual_summary.csv"
            for path, text in ((expected_ranking, "case_id,candidate_rank\nA,1\n"), (actual_ranking, "case_id,candidate_rank\nA,1\n"), (expected_summary, "case_id,rank_ref\nA,1\n"), (actual_summary, "case_id,rank_ref\nA,1\n")):
                path.write_text(text, encoding="utf-8", newline="\n")
            self.assertEqual(compare_control_reproduction(expected_ranking, actual_ranking, expected_summary, actual_summary, {"top_1": 1}, {"top_1": 1})["status"], "PASS")
            actual_ranking.write_text("case_id,candidate_rank\nA,2\n", encoding="utf-8", newline="\n")
            with self.assertRaisesRegex(ContractViolation, "not exact"):
                compare_control_reproduction(expected_ranking, actual_ranking, expected_summary, actual_summary, {"top_1": 1}, {"top_1": 1})

    def test_23_posix_serialization_is_stable_for_windows_style_repository_input(self) -> None:
        self.assertEqual(posix_relative("outputs\\audits\\0b05c\\gate.json"), "outputs/audits/0b05c/gate.json")

    def test_24_execution_contract_includes_builders_producers_and_full_ledger(self) -> None:
        commands = self.ev03["prospective_execution"]["commands"]
        self.assertIn("build_bm25_corrective_0b05c_v01", commands["ev03_build_command"])
        self.assertIn("build_bm25_corrective_0b05c_v01", self.ev04["prospective_execution"]["commands"]["ev04_corrected_build_command"])
        self.assertIn("produce_case_level_comparison", self.gate["comparison_producers"]["EV03_case_level"])
        self.assertIn("D1a corrected outputs", self.gate["hash_ledger_contract"]["covers"])
        self.assertEqual(self.gate["hash_ledger_contract"]["self_exclusion"], "Only the ledger file itself is excluded to avoid a circular hash.")

    def test_25_historical_fixed_hash_guards_reject_a_derived_corpus_and_ev04_needs_both_gates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            derived = Path(temporary_directory) / "corrected.jsonl"
            derived.write_text('{"codigo":"87044110"}\n', encoding="utf-8", newline="\n")
            with self.assertRaises(ValueError):
                frozen_flat_runner._validate_hash(derived, "0" * 64, "historical flat corpus")
            with self.assertRaises(ValueError):
                frozen_hierarchical_runner.validate_hash(derived, "0" * 64, "historical hierarchical corpus")
        self.assertFalse(ev04_corrected_execution_permitted(authorized=False, reproduction_status="PASS"))
        self.assertFalse(ev04_corrected_execution_permitted(authorized=True, reproduction_status="FAIL"))
        self.assertTrue(ev04_corrected_execution_permitted(authorized=True, reproduction_status="PASS"))


if __name__ == "__main__":
    unittest.main()
