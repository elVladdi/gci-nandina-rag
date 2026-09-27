from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = "db0d0ad0d8435921a7838db6720eaea86a263763"
STEM = "g7_thesis_fig_04_he2"
FROZEN_BLOBS = {
    "src/figures/group6/render_g6_fig_01_he2.py": "678d5fd49b3bd090c7d7729702741e6dcfe293fa",
    "figures/group6/g6_fig_01_he2.svg": "f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3",
    "figures/group6/g6_fig_01_he2.png": "1860898f13cdefb311489dd1ec3d8fb28bf24538",
    "outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv": "cb68583ee2260e4455796bac99ad90995ca7ef92",
    "outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv": "359e4e19b5ef1d44983c03039162209293b2a44c",
}
FROZEN_PNG_SHA256 = "3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f"
LABELS = {
    "Primary HE2 evidence": "Evidencia primaria de HE2",
    "Offline internal benchmark: 1,056 series / 67 DAM / 42 NANDINA":
        "Evaluación interna fuera de línea: 1 056 series / 67 DAM / 42 NANDINA",
    "Observed values (no arm-level CI)": "Valores observados (sin IC por brazo)",
    "Observed metric value": "Valor observado de la métrica",
    "Historical": "Recuperación histórica",
    "Flat (Attempt06)": "BM25 normativo plano",
    "Hierarchical (Attempt06)": "BM25 normativo jerárquico",
    "D1a (Attempt06)": "Recuperador denso entrenado con MNRL",
    "Historical - comparator (frozen 99% CI)":
        "Recuperación histórica − comparador (IC del 99 %)",
    "Flat": "BM25 normativo plano",
    "Hierarchical": "BM25 normativo jerárquico",
    "D1a": "Recuperador denso entrenado con MNRL",
    "Paired difference": "Diferencia pareada",
    "Recall@200 - Recall@100 (frozen 95% CI)":
        "Recall@200 − Recall@100 (IC del 95 %)",
    "Paired recall difference": "Diferencia pareada de recall",
    "Context: Recall@100=0.101; Recall@200=0.304; delta=0.203 [0.067, 0.342]":
        "Contexto: Recall@100 = 0,101; Recall@200 = 0,304; diferencia = 0,203; IC 95 % [0,067; 0,342]",
}


def git_bytes(path: str) -> bytes:
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", "show", f"{BASE}:{path}"],
        cwd=ROOT,
    )


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def frozen_inputs() -> dict[str, bytes]:
    blobs = {}
    for path, expected in FROZEN_BLOBS.items():
        data = git_bytes(path)
        actual = blob_id(data)
        if actual != expected:
            raise RuntimeError(f"frozen blob mismatch: {path}: {actual} != {expected}")
        blobs[path] = data
    png_sha = hashlib.sha256(blobs["figures/group6/g6_fig_01_he2.png"]).hexdigest()
    if png_sha != FROZEN_PNG_SHA256:
        raise RuntimeError(f"frozen PNG SHA-256 mismatch: {png_sha}")
    return blobs


def main() -> None:
    blobs = frozen_inputs()
    source = blobs["src/figures/group6/render_g6_fig_01_he2.py"].decode("utf-8")
    g6 = types.ModuleType("frozen_g6_fig_01")
    g6.__file__ = str(Path(__file__).resolve())
    exec(compile(source, f"{BASE}:render_g6_fig_01_he2.py", "exec"), g6.__dict__)

    def verify_blob(path: Path, expected: str) -> None:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in blobs or blob_id(blobs[rel]) != expected:
            raise RuntimeError(f"unexpected scientific input: {rel}")

    def read_rows(path: Path) -> list[dict[str, str]]:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in blobs or not rel.endswith(".csv"):
            raise RuntimeError(f"unexpected table: {rel}")
        return list(csv.DictReader(io.StringIO(blobs[rel].decode("utf-8-sig"))))

    original_text = g6.Canvas.text

    def thesis_text(self, x, y, value, size=12, anchor="middle", bold=False, fill="#222222"):
        # Text-only reflow keeps every G6 data mark, axis, tick, and reference line untouched.
        if x == 120 and value in g6.METRICS:
            return original_text(self, 290, y - 15, value, size, "start", bold, fill)
        if x == 195 and value == "D1a":
            original_text(self, x, y - 7, "Recuperador denso", size, anchor, bold, fill)
            return original_text(self, x, y + 7, "entrenado con MNRL", size, anchor, bold, fill)
        if x > 800 and value == "D1a (Attempt06)":
            original_text(self, x, y - 8, "Recuperador denso", size, anchor, bold, fill)
            return original_text(self, x, y + 8, "entrenado con MNRL", size, anchor, bold, fill)
        if value not in LABELS and ("Context:" in value or "Attempt06" in value):
            raise RuntimeError(f"unmapped thesis-visible source label: {value}")
        return original_text(self, x, y, LABELS.get(value, value), size, anchor, bold, fill)

    original_save = g6.Canvas.save

    def thesis_save(self, _source_stem: str) -> None:
        original_save(self, STEM)

    g6.verify_blob = verify_blob
    g6.read_rows = read_rows
    g6.Canvas.text = thesis_text
    g6.Canvas.save = thesis_save
    g6.OUT = ROOT / "figures/group7"
    g6.main()


if __name__ == "__main__":
    main()
