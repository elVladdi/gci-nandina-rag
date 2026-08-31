"""Keep the repository entrypoint aligned with the closed Group 1 benchmark."""

from __future__ import annotations

from pathlib import Path
import unittest


README = Path(__file__).resolve().parents[1] / "README.md"


class TestReadmeGroup1StatusV02(unittest.TestCase):
    def test_closed_group1_status_is_present_without_stale_pending_rows(self) -> None:
        content = README.read_text(encoding="utf-8")
        for required in ("Grupo 1", "CLOSED", "EXP-04", "v0.2", "HE2", "HE3", "HE4", "HE5"):
            self.assertIn(required, content)
        for stale in (
            "EXP-04 B Flat normative BM25 | Pending",
            "EXP-04 C Hierarchical normative BM25 | Pending",
            "Text2Trade / dense comparator | Pending",
            "Candidate pools v0.2 | Pending",
            "Diagnostic LLM reranker | Pending",
            "Top-3 explainer v0.2 | Pending",
            "Integrated error analysis | Pending",
        ):
            self.assertNotIn(stale, content)
