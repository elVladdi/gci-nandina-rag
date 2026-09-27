from __future__ import annotations

import csv
import hashlib
import io
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE_COMMIT = "db0d0ad0d8435921a7838db6720eaea86a263763"
RENDERER_PATH = "src/figures/group6/render_g6_fig_02_phase_e.py"
CSV_PATH = "outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv"
EXPECTED_BLOBS = {
    RENDERER_PATH: "e9dafe41e3b22cb1c8d09da08a723925cd300b7d",
    "figures/group6/g6_fig_02_phase_e.svg": "ec164ea41ab8605edf198c03785db63c442c1b64",
    "figures/group6/g6_fig_02_phase_e.png": "7917314c8fc54dd96dd9ddfb28c9927c9a577c76",
    CSV_PATH: "fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61",
}
EXPECTED_SHA256 = {
    "figures/group6/g6_fig_02_phase_e.png": "867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f",
    CSV_PATH: "77a9b3cf27881396162fa25464d9fcaa1c8c557b6140e1e48bdbe93858aa523e",
}


def frozen_blob(path: str) -> bytes:
    actual = subprocess.check_output(
        ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"], cwd=ROOT, text=True
    ).strip()
    if actual != EXPECTED_BLOBS[path]:
        raise RuntimeError(f"frozen source blob mismatch: {path}: {actual}")
    data = subprocess.check_output(["git", "show", f"{SOURCE_COMMIT}:{path}"], cwd=ROOT)
    expected_sha = EXPECTED_SHA256.get(path)
    if expected_sha and hashlib.sha256(data).hexdigest() != expected_sha:
        raise RuntimeError(f"frozen source SHA-256 mismatch: {path}")
    return data


def replace_exact(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        raise RuntimeError(f"expected exactly one frozen renderer occurrence: {old}")
    return source.replace(old, new, 1)


def main() -> None:
    frozen = {path: frozen_blob(path) for path in EXPECTED_BLOBS}
    rows = list(csv.DictReader(io.StringIO(frozen[CSV_PATH].decode("utf-8-sig"))))
    if len(rows) != 15:
        raise RuntimeError("frozen scientific source must contain 15 marks")
    source = frozen[RENDERER_PATH].decode("utf-8")
    substitutions = [
        ('OUT = ROOT / "figures/group6"', 'OUT = ROOT / "figures/group7"'),
        (
            '    verify_blob()\n    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:\n        rows = list(csv.DictReader(handle))',
            '    rows = frozen_rows',
        ),
        ('"Phase E exact-NANDINA coverage"', '"Cobertura exacta NANDINA según profundidad y variante"'),
        ('"Descriptive only; no CI, p-values, fitted trends, or connecting lines"',
         '"Resultados descriptivos; sin IC, valores p, tendencias ajustadas ni líneas de conexión"'),
        ('label = "Exact-NANDINA coverage"', 'label = "Cobertura exacta NANDINA"'),
        ('"Recovery depth (ordered categories)"', '"Profundidad de recuperación"'),
        ('text(865,105,"Formal claim variants",11,"start",True)',
         'text(865,105,"Variantes descriptivas predefinidas",11,"start",True)'),
        (
            '    for i,(variant,shape,color,formal) in enumerate(VARIANTS[:4]):\n'
            '        y=137+i*49; marker(878,y,shape,color,formal,6); text(896,y,variant,15,"start")',
            '    labels = [\n'
            '        ("Solo jerárquico",),\n'
            '        ("Solo dual",),\n'
            '        ("Jerárquico con prioridad para", "los primeros 100 candidatos"),\n'
            '        ("Jerárquico 80 + backfill", "dual 20"),\n'
            '    ]\n'
            '    for i,(variant,shape,color,formal) in enumerate(VARIANTS[:4]):\n'
            '        y=137+i*49; marker(878,y,shape,color,formal,6)\n'
            '        for j,label_line in enumerate(labels[i]):\n'
            '            text(896,y+(j-(len(labels[i])-1)/2)*19,label_line,13.5,"start")',
        ),
        ('text(865,350,"Context only",11,"start",True)',
         'text(865,350,"Contexto descriptivo adicional",11,"start",True)'),
        ('text(896,383,"hierarchical_70_",15,"start"); text(896,403,"dual_backfill_30",15,"start")',
         'text(896,373,"Jerárquico 70 + backfill",13.5,"start"); text(896,393,"dual 30",13.5,"start")'),
        ('"15 marks = 5 variants x 3 depths"', '"15 puntos = 5 variantes × 3 profundidades"'),
        ('"N = 1,056 series"', '"N = 1 056 series"'),
        (
            'text(45,648,"The diagnostic union is excluded from ordinary performance. Context and formal variants retain equal visual weight.",13.5,"start",False,"#555555")',
            'text(45,637,"La unión diagnóstica se excluye del rendimiento ordinario.",13.5,"start",False,"#555555")\n'
            '    text(45,659,"Las variantes predefinidas y la variante contextual conservan igual peso visual.",13.5,"start",False,"#555555")',
        ),
        ('g6_fig_02_phase_e.svg', 'g7_thesis_fig_05_coverage.svg'),
        ('g6_fig_02_phase_e.png', 'g7_thesis_fig_05_coverage.png'),
    ]
    for old, new in substitutions:
        source = replace_exact(source, old, new)
    namespace = {"__name__": "g7_frozen_renderer", "__file__": str(Path(__file__)), "frozen_rows": rows}
    exec(compile(source, f"{SOURCE_COMMIT}:{RENDERER_PATH}", "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
