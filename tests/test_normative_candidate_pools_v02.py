import csv
import hashlib
import json
import statistics
import unittest
from collections import defaultdict
from pathlib import Path

from src.experiments.evaluate_normative_candidate_pools_data_aduanas_v02 import build_pool, hit_flags


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2"
CONFIG_PATH = ROOT / "src/configs/normative_candidate_pools_v0.2.json"
EVAL_HASH = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class TestNormativeCandidatePoolsV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cls.metadata = json.loads((OUT / "candidate_pool_run_metadata.json").read_text(encoding="utf-8"))
        cls.metrics = json.loads((OUT / "candidate_pool_metrics.json").read_text(encoding="utf-8"))
        cls.compatibility = json.loads((OUT / "candidate_pool_compatibility.json").read_text(encoding="utf-8"))
        cls.complementarity = json.loads((OUT / "candidate_pool_complementarity.json").read_text(encoding="utf-8"))
        cls.backfill = json.loads((OUT / "candidate_pool_backfill_analysis.json").read_text(encoding="utf-8"))
        cls.ceiling = json.loads((OUT / "candidate_pool_coverage_ceiling.json").read_text(encoding="utf-8"))
        cls.results = read_csv(OUT / "candidate_pool_results.csv")
        cls.summary = read_csv(OUT / "candidate_pool_case_summary.csv")
        cls.eval_rows = read_csv(ROOT / cls.config["eval"]["path"])
        cls.results_by_key = {(row["pool_id"], int(row["depth"]), row["case_id"]): row for row in cls.results}
        cls.summary_by_key = {(row["pool_id"], int(row["depth"]), row["case_id"]): row for row in cls.summary}

    def test_01_evalset_is_frozen_v02_with_1056_cases(self) -> None:
        self.assertEqual(sha256(ROOT / self.config["eval"]["path"]), EVAL_HASH)
        self.assertEqual(self.config["eval"]["sha256"], EVAL_HASH)
        self.assertEqual(len(self.eval_rows), 1056)
        self.assertEqual(len({row["case_id"] for row in self.eval_rows}), 1056)
        self.assertTrue(all(row["case_id"].startswith("DA-EVAL-V02-") for row in self.eval_rows))

    def test_02_phase_a_to_e_cases_and_labels_are_compatible(self) -> None:
        expected = {row["case_id"]: row["NANDINA"] for row in self.eval_rows}
        sources = self.config["frozen_input_rankings"]
        source_specs = (
            (sources["historical"]["path"], "expected_nandina"),
            (sources["flat"]["case_summary"], "nandina_ref"),
            (sources["hierarchical"]["case_summary"], "nandina_ref"),
            (sources["d1a"]["case_summary"], "nandina_ref"),
        )
        for path, label in source_specs:
            rows = read_csv(ROOT / path)
            self.assertEqual({row["case_id"] for row in rows}, set(expected), path)
            self.assertEqual({row["case_id"]: row[label] for row in rows}, expected, path)
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["identical_case_id_sets"])
        self.assertTrue(self.compatibility["identical_labels"])

    def test_03_frozen_inputs_and_output_hashes_match(self) -> None:
        frozen = self.config["frozen_input_rankings"]
        expected = {
            frozen["historical"]["path"]: frozen["historical"]["sha256"],
            frozen["flat"]["case_summary"]: frozen["flat"]["case_summary_sha256"],
            frozen["flat"]["results"]: frozen["flat"]["results_sha256"],
            frozen["hierarchical"]["case_summary"]: frozen["hierarchical"]["case_summary_sha256"],
            frozen["hierarchical"]["results"]: frozen["hierarchical"]["results_sha256"],
            frozen["d1a"]["case_summary"]: frozen["d1a"]["case_summary_sha256"],
            frozen["d1a"]["ranking_trace"]: frozen["d1a"]["ranking_trace_sha256"],
        }
        for path, digest in expected.items():
            self.assertEqual(sha256(ROOT / path), digest, path)
        for name, digest in self.metadata["output_sha256"].items():
            self.assertEqual(sha256(ROOT / self.metadata["outputs"][name]), digest, name)
        self.assertTrue(self.metadata["output_sha256_excludes_self_referential_metadata"])

    def test_04_pools_are_unique_and_hierarchical_coverage_is_recalculable(self) -> None:
        for row in self.results:
            codes = [code for code in row["candidate_codes"].split("|") if code]
            self.assertEqual(len(codes), len(set(codes)), row["case_id"])
            self.assertEqual(len(codes), int(row["effective_size"]))
            self.assertTrue(all(len(code) == 8 and code.isdigit() for code in codes))
            summary = self.summary_by_key[(row["pool_id"], int(row["depth"]), row["case_id"])]
            flags = hit_flags(codes, row["nandina_ref"])
            for family, value in flags.items():
                self.assertEqual(value, int(summary[f"{family}_at_depth"]))

    def test_05_historical_pool_order_and_backfill_are_deterministic(self) -> None:
        case_ids = [row["case_id"] for row in self.eval_rows]
        variants = self.config["candidate_pool_variants"]
        for case_id in case_ids:
            hierarchical = self.results_by_key[("hierarchical_only", 200, case_id)]["candidate_codes"].split("|")
            dual = self.results_by_key[("dual_only", 200, case_id)]["candidate_codes"].split("|")
            for pool_id, variant in variants.items():
                for depth in self.config["depths"]:
                    expected, _ = build_pool(hierarchical, dual, int(depth), variant)
                    actual = self.results_by_key[(pool_id, int(depth), case_id)]["candidate_codes"].split("|")
                    self.assertEqual([item["code"] for item in expected], actual, f"{pool_id}/{depth}/{case_id}")

    def test_06_pool_metrics_and_backfill_gain_are_recalculable(self) -> None:
        grouped: dict[tuple[str, int], list[dict[str, str]]] = defaultdict(list)
        for row in self.summary:
            grouped[(row["pool_id"], int(row["depth"]))].append(row)
        for metric in self.metrics["metrics"]:
            rows = grouped[(metric["pool_id"], metric["depth"])]
            sizes = [int(row["effective_size"]) for row in rows]
            self.assertEqual(len(rows), 1056)
            self.assertAlmostEqual(sum(sizes) / len(sizes), metric["effective_size_mean"])
            self.assertEqual(min(sizes), metric["effective_size_min"])
            self.assertEqual(max(sizes), metric["effective_size_max"])
            self.assertEqual(statistics.median(sizes), metric["effective_size_median"])
            for family in ("exact", "hs6", "hs4", "chapter"):
                count = sum(int(row[f"{family}_at_depth"]) for row in rows)
                self.assertEqual(count, metric[f"{family}_numerator"])
                self.assertAlmostEqual(count / 1056, metric[f"{family}_at_depth"])
        for pool_id, values in self.backfill["variants"].items():
            for depth, outcome in values.items():
                depth_int = int(depth)
                hierarchical_rows = {row["case_id"]: row for row in grouped[("hierarchical_only", depth_int)]}
                pool_rows = {row["case_id"]: row for row in grouped[(pool_id, depth_int)]}
                added = sum(int(row["exact_at_depth"]) and not int(hierarchical_rows[case_id]["exact_at_depth"]) for case_id, row in pool_rows.items())
                lost = sum(int(row["exact_at_depth"]) and not int(pool_rows[case_id]["exact_at_depth"]) for case_id, row in hierarchical_rows.items())
                self.assertEqual(added, outcome["new_cases_from_backfill"])
                self.assertEqual(lost, outcome["lost_vs_hierarchical"])

    def test_07_overlap_and_diagnostic_union_are_not_rankings(self) -> None:
        for depth, expected in self.complementarity["depths"].items():
            h_rows = {row["case_id"]: row for row in self.summary if row["pool_id"] == "hierarchical_only" and row["depth"] == depth}
            d_rows = {row["case_id"]: row for row in self.summary if row["pool_id"] == "dual_only" and row["depth"] == depth}
            actual = {"both": 0, "only_a": 0, "only_b": 0, "neither": 0}
            for case_id, h_row in h_rows.items():
                h = int(h_row["exact_at_depth"])
                d = int(d_rows[case_id]["exact_at_depth"])
                actual["both" if h and d else "only_a" if h else "only_b" if d else "neither"] += 1
            for key, value in actual.items():
                self.assertEqual(value, expected[key])
        self.assertTrue(self.ceiling["not_a_ranking"])
        self.assertEqual(self.ceiling["label"], "DIAGNOSTIC ORACLE-LIKE UNION / COVERAGE CEILING")
        self.assertTrue(self.metrics["no_mrr_for_candidate_pools"])
        self.assertTrue(self.metrics["diagnostic_union_not_a_ranking"])

    def test_08_d0_and_v01_eval_are_excluded_from_confirmatory_phase_e(self) -> None:
        self.assertFalse(self.config["exclusions"]["d0_in_comparison"])
        self.assertTrue(self.compatibility["d0_excluded_from_confirmatory_comparison"])
        strategies = read_csv(OUT / "candidate_pool_strategy_comparison.csv")
        self.assertFalse(any("D0" in row["strategy"] for row in strategies))
        self.assertNotIn("v0.1", self.config["eval"]["path"])
        self.assertTrue(all(row["case_id"].startswith("DA-EVAL-V02-") for row in self.results))


if __name__ == "__main__":
    unittest.main()
