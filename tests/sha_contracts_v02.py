"""Portable SHA assertions for frozen v0.2 artifacts."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import subprocess


REPO = Path(__file__).resolve().parents[1]
MAP = REPO / "outputs" / "evaluation" / "exp04_consolidated_closure_v0.2" / "exp04_sha_artifact_canonicalization_map_v0.2.csv"


def relative_path(path: Path) -> str:
    return path.resolve().relative_to(REPO).as_posix()


def content_bytes(path: Path) -> bytes:
    try:
        spec = f":{relative_path(path)}"
    except ValueError:
        return path.read_bytes()
    result = subprocess.run(
        ["git", "-C", str(REPO), "show", spec], capture_output=True, check=False
    )
    return result.stdout if result.returncode == 0 else path.read_bytes()


def git_content_sha256(path: Path) -> str:
    blob = content_bytes(path)
    return hashlib.sha256(blob).hexdigest()


def assert_frozen_sha(testcase: object, path: Path, expected_sha256: str) -> None:
    blob = content_bytes(path)
    actual = hashlib.sha256(blob).hexdigest()
    if actual == expected_sha256:
        return
    artifact = relative_path(path)
    with MAP.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["artifact"] == artifact and row["legacy_sha256"] == expected_sha256:
                testcase.assertEqual(actual, row["canonical_git_lf_sha256"], artifact)
                return
    if b"\r\n" not in blob:
        testcase.assertEqual(
            hashlib.sha256(blob.replace(b"\n", b"\r\n")).hexdigest(),
            expected_sha256,
            artifact,
        )
        return
    testcase.assertEqual(actual, expected_sha256, artifact)
