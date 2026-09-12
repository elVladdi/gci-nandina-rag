from __future__ import annotations

import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np

from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate


ROOT = Path(__file__).resolve().parents[1]


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


class ReplayFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.vectors_path = root / "assets/vectors.npy"
        self.docstore_path = root / "assets/docstore.jsonl"
        self.id_map_path = root / "assets/id_map.json"
        self.sample_path = root / "assets/sample.csv"
        self.gate_path = root / "assets/vector_gate.json"
        self.vectors_path.parent.mkdir(parents=True)
        np.save(self.vectors_path, np.zeros((21, 4), dtype=np.float32))
        self.docs = [
            {"doc_id": f"DOC:{index}", "codigo": f"{index:08d}", "texto_index": f"text {index}"}
            for index in range(21)
        ]
        self.docstore_path.write_text(
            "".join(json.dumps(item) + "\n" for item in self.docs), encoding="utf-8", newline="\n"
        )
        write_json(
            self.id_map_path,
            {str(index): {"doc_id": item["doc_id"], "codigo": item["codigo"]} for index, item in enumerate(self.docs)},
        )
        self.rows = [
            {
                "vector_index": str(index),
                "doc_id": item["doc_id"],
                "nandina": item["codigo"],
                "stored_text_sha256": hashlib.sha256(item["texto_index"].encode()).hexdigest(),
            }
            for index, item in enumerate(self.docs)
        ]
        self.refresh_authority()

    def write_sample(self) -> None:
        with self.sample_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=("vector_index", "doc_id", "nandina", "stored_text_sha256"))
            writer.writeheader()
            writer.writerows(self.rows)

    def refresh_authority(self) -> None:
        self.write_sample()
        replay_gate = {
            "gate": "D1a vector integrity before eval",
            "status": "PASS",
            "criterion": "synthetic fixture",
            "float32_epsilon": float(np.finfo(np.float32).eps),
            "tolerance": float(8 * np.finfo(np.float32).eps),
            "sample_count": 21,
            "byte_exact_count": 21,
            "cosine_min": 1.0,
            "cosine_max": 1.0,
            "max_absolute_difference": 0.0,
            "max_l2_difference": 0.0,
            "sample_csv": "assets/sample.csv",
            "sample_csv_sha256": gate._sha256(self.sample_path),
        }
        write_json(self.gate_path, replay_gate)
        principal = {
            "vectors": {
                "path": "assets/vectors.npy", "sha256": gate._sha256(self.vectors_path),
                "shape": [21, 4], "dtype": "float32",
            },
            "docstore": {"path": "assets/docstore.jsonl", "sha256": gate._sha256(self.docstore_path), "records": 21},
            "id_map": {"path": "assets/id_map.json", "sha256": gate._sha256(self.id_map_path), "records": 21},
        }
        metadata = {
            "artifacts": {
                **principal,
                "vector_integrity_gate": {
                    "path": "assets/vector_gate.json", "sha256": gate._sha256(self.gate_path), **replay_gate,
                },
            }
        }
        write_json(self.root / gate.MODEL_METADATA, metadata)
        write_json(
            self.root / gate.REPRODUCIBILITY_MANIFEST,
            {
                "large_local_artifacts_not_committed": {
                    key: {"path": item["path"], "sha256": item["sha256"], "bytes": (self.root / item["path"]).stat().st_size}
                    for key, item in principal.items()
                }
            },
        )


def pass_replay(_: object) -> dict[str, object]:
    return {
        "status": "PASS", "sample_count": 21, "cosine_min": 1.0,
        "max_absolute_difference": 0.0, "tolerance": float(8 * np.finfo(np.float32).eps),
    }


class HistoricalReplayContractV35ETests(unittest.TestCase):
    def fixture(self, folder: str) -> ReplayFixture:
        return ReplayFixture(Path(folder))

    def assert_asset_failure(self, mutate) -> None:
        with tempfile.TemporaryDirectory() as folder:
            fixture = self.fixture(folder)
            mutate(fixture)
            with self.assertRaises(gate.ContractViolation):
                gate.validate_historical_vector_replay_assets(fixture.root)

    def test_positive_requires_physical_21_of_21_and_has_no_scientific_side_effect(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            fixture = self.fixture(folder)
            before = sorted(path.relative_to(fixture.root).as_posix() for path in fixture.root.rglob("*"))
            result = gate.required_historical_vector_replay(
                fixture.root, Path(sys.executable), replay_executor=pass_replay
            )
            after = sorted(path.relative_to(fixture.root).as_posix() for path in fixture.root.rglob("*"))
            self.assertEqual((result["status"], result["required"], result["sample_count"]), ("PASS", True, 21))
            self.assertEqual(result["classification"], "ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT")
            self.assertEqual(before, after)

    def test_missing_vectors_fails_closed(self) -> None:
        self.assert_asset_failure(lambda value: value.vectors_path.unlink())

    def test_missing_docstore_fails_closed(self) -> None:
        self.assert_asset_failure(lambda value: value.docstore_path.unlink())

    def test_missing_id_map_fails_closed(self) -> None:
        self.assert_asset_failure(lambda value: value.id_map_path.unlink())

    def test_missing_sample_fails_closed(self) -> None:
        self.assert_asset_failure(lambda value: value.sample_path.unlink())

    def test_sample_sha_mismatch_fails_closed(self) -> None:
        self.assert_asset_failure(lambda value: value.sample_path.write_text("changed\n", encoding="utf-8"))

    def test_sample_with_20_rows_fails_closed(self) -> None:
        def mutate(value: ReplayFixture) -> None:
            value.rows.pop()
            value.refresh_authority()
        self.assert_asset_failure(mutate)

    def test_sample_with_22_rows_fails_closed(self) -> None:
        def mutate(value: ReplayFixture) -> None:
            value.rows.append(dict(value.rows[-1], vector_index="20"))
            value.refresh_authority()
        self.assert_asset_failure(mutate)

    def test_duplicate_vector_index_fails_closed(self) -> None:
        def mutate(value: ReplayFixture) -> None:
            value.rows[-1]["vector_index"] = value.rows[0]["vector_index"]
            value.refresh_authority()
        self.assert_asset_failure(mutate)

    def test_out_of_range_vector_index_fails_closed(self) -> None:
        def mutate(value: ReplayFixture) -> None:
            value.rows[-1]["vector_index"] = "21"
            value.refresh_authority()
        self.assert_asset_failure(mutate)

    def test_malformed_stored_text_sha_fails_closed(self) -> None:
        def mutate(value: ReplayFixture) -> None:
            value.rows[-1]["stored_text_sha256"] = ""
            value.refresh_authority()
        self.assert_asset_failure(mutate)

    def test_replay_non_pass_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            fixture = self.fixture(folder)
            with self.assertRaises(gate.ContractViolation):
                gate.required_historical_vector_replay(
                    fixture.root, Path(sys.executable), replay_executor=lambda _: {**pass_replay(None), "status": "FAIL"}
                )

    def test_replay_wrong_sample_count_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            fixture = self.fixture(folder)
            with self.assertRaises(gate.ContractViolation):
                gate.required_historical_vector_replay(
                    fixture.root, Path(sys.executable), replay_executor=lambda _: {**pass_replay(None), "sample_count": 20}
                )

    def test_environment_preflight_rejects_optional_or_unavailable_replay(self) -> None:
        interpreter = Path(__file__).resolve()
        probe = {
            "python": gate.TESTED_ENVIRONMENT["python_version"],
            **{key: gate.TESTED_ENVIRONMENT[key] for key in ("python_implementation", "architecture", "platform_system", "machine")},
            "packages": dict(gate.TESTED_ENVIRONMENT["required_packages"]),
            "distributions": dict(gate.TESTED_ENVIRONMENT["required_distributions"]),
            "project_imports": {"status": "PASS", "count": len(gate.project_local_import_closure(ROOT)), "modules": []},
            "smoke": {"shape": [32, 384], "dtype": "float32", "all_finite": True, "norms_within_tolerance": True},
        }
        usage = type("Usage", (), {"free": gate.DISK_MARGIN_BYTES + 1})()
        optional = {"status": "OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE", "required": False, "sample_count": 0}
        with mock.patch.object(gate, "_sha256", return_value=gate.TESTED_ENVIRONMENT["executable_sha256"]), \
             mock.patch.object(gate, "validate_complete_model_directory", return_value={"status": "PASS_EXACT"}), \
             mock.patch.object(gate, "_interpreter_probe", return_value=probe), \
             mock.patch.object(gate, "required_historical_vector_replay", return_value=optional), \
             mock.patch.object(gate.shutil, "disk_usage", return_value=usage), \
             mock.patch.object(gate, "_available_memory", return_value=(10_000_000_000, gate.MEMORY_MARGIN_BYTES + 1)):
            with self.assertRaises(gate.ContractViolation):
                gate.preauthorization_environment_preflight(ROOT, interpreter)

    def test_environment_preflight_rejects_project_import_and_capacity_drift(self) -> None:
        interpreter = Path(__file__).resolve()
        base_probe = {
            "python": gate.TESTED_ENVIRONMENT["python_version"],
            **{key: gate.TESTED_ENVIRONMENT[key] for key in ("python_implementation", "architecture", "platform_system", "machine")},
            "packages": dict(gate.TESTED_ENVIRONMENT["required_packages"]),
            "distributions": dict(gate.TESTED_ENVIRONMENT["required_distributions"]),
            "project_imports": {"status": "PASS", "count": len(gate.project_local_import_closure(ROOT)), "modules": []},
            "smoke": {"shape": [32, 384], "dtype": "float32", "all_finite": True, "norms_within_tolerance": True},
        }
        replay = {
            "status": "PASS", "required": True, "sample_count": 21,
            "classification": "ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT",
        }
        cases = (
            ("project_import_closure", {**base_probe, "project_imports": {"status": "PASS", "count": len(gate.project_local_import_closure(ROOT)) - 1, "modules": []}}, gate.DISK_MARGIN_BYTES + 1),
            ("capacity", base_probe, gate.DISK_MARGIN_BYTES - 1),
        )
        for label, probe, disk_free in cases:
            usage = type("Usage", (), {"free": disk_free})()
            with self.subTest(label=label), \
                 mock.patch.object(gate, "_sha256", return_value=gate.TESTED_ENVIRONMENT["executable_sha256"]), \
                 mock.patch.object(gate, "validate_complete_model_directory", return_value={"status": "PASS_EXACT"}), \
                 mock.patch.object(gate, "_interpreter_probe", return_value=probe), \
                 mock.patch.object(gate, "required_historical_vector_replay", return_value=replay), \
                 mock.patch.object(gate.shutil, "disk_usage", return_value=usage), \
                 mock.patch.object(gate, "_available_memory", return_value=(10_000_000_000, gate.MEMORY_MARGIN_BYTES + 1)):
                with self.assertRaises(gate.ContractViolation):
                    gate.preauthorization_environment_preflight(ROOT, interpreter)

    def test_gate_readiness_and_manifest_contract_require_replay(self) -> None:
        bundle = gate.build_bundle(ROOT)
        self.assertTrue(bundle["gate"]["historical_vector_replay_required"])
        self.assertTrue(bundle["gate"]["environment_contract"]["historical_vector_replay_required"])
        self.assertTrue(bundle["manifest"]["historical_vector_replay_required"])


if __name__ == "__main__":
    unittest.main()
