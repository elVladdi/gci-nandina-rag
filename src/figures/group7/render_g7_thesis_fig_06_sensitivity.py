from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REF_G6 = "e93b44164a9619dad1f527a3b2d4479265858e39"
RENDERER = "src/figures/group6/render_g6_fig_03_exp11a.py"
SVG_SOURCE = "figures/group6/g6_fig_03_exp11a.svg"
EXPECTED_BLOBS = {
    RENDERER: "1723f139afd308c4966846247ffe4d2f330a0d4e",
    SVG_SOURCE: "1b2aca9aa9c2582cf0b7e16850cd5b22387cc771",
    "figures/group6/g6_fig_03_exp11a.png": "eaf59497ee49ab36d34d23e42cf002111bc9fe3e",
    "outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv": "cf3aedab5935d6af9b3ac7be7b51b954fcb9c403",
    "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv": "9b434d7e09e6db7e9de061953b59c53aac2337ad",
    "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv": "535dd377d107ddcbf09ecaa13cd66ca723ee738d",
}
EXPECTED_SHA256 = {
    RENDERER: "bb73e2ce324500a36053afa52bc25a03af44def36ea2a7c2fd5c2c14a3cf844f",
    SVG_SOURCE: "a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3",
    "figures/group6/g6_fig_03_exp11a.png": "3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de",
}


def frozen_sources() -> dict[str, bytes]:
    sources = {}
    for path, expected in EXPECTED_BLOBS.items():
        data = subprocess.check_output(["git", "show", f"{REF_G6}:{path}"], cwd=ROOT)
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")
        if path in EXPECTED_SHA256 and hashlib.sha256(data).hexdigest() != EXPECTED_SHA256[path]:
            raise RuntimeError(f"frozen source SHA-256 mismatch: {path}")
        sources[path] = data
    return sources


def replace_exact(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        raise RuntimeError(f"expected exactly one frozen renderer occurrence: {old}")
    return source.replace(old, new, 1)


def non_text_geometry(element: ET.Element):
    return (
        element.tag,
        element.attrib,
        [non_text_geometry(child) for child in element if child.tag.rsplit("}", 1)[-1] not in {"text", "tspan"}],
    )


def main() -> None:
    sources = frozen_sources()
    source = sources[RENDERER].decode("utf-8")
    substitutions = [
        ('"EXP11A joint size-composition sensitivity"',
         '"Sensibilidad conjunta del banco histórico a tamaño y composición"'),
        ('"Observed runs only; descriptive and noncausal; no summaries, CI, p-values, or fitted trends"',
         '"Solo corridas observadas; análisis descriptivo y no causal; sin resúmenes como marcas, IC, valores p ni tendencias ajustadas"'),
        ('text(left,top-18,metric,16,"start",True)',
         'text(left,top-18,metric.replace("Top", "Top-"),16,"start",True)'),
        ('text(anchors[ci],bottom+17,condition,7.5,"middle",condition=="H100 ref.")',
         'text(anchors[ci],bottom+17,condition.replace("H100 ref.", "H100 (ref.)"),7.5,"middle",condition=="H100 ref.")'),
        ('"Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly."',
         '"Las condiciones representan bancos observados categóricos; H100 es una única referencia congelada. El tamaño y la composición varían conjuntamente."'),
        ('g6_fig_03_exp11a.svg', 'g7_thesis_fig_06_sensitivity.svg'),
        ('g6_fig_03_exp11a.png', 'g7_thesis_fig_06_sensitivity.png'),
    ]
    for old, new in substitutions:
        source = replace_exact(source, old, new)
    namespace = {"__name__": "g7_frozen_renderer", "__file__": str(Path(__file__))}
    exec(compile(source, f"{REF_G6}:{RENDERER}", "exec"), namespace)

    # Read already verified Git blobs instead of materializing scientific files.
    def rows(path):
        return list(csv.DictReader(io.StringIO(sources[path.relative_to(ROOT).as_posix()].decode("utf-8-sig"))))

    namespace["rows"] = rows
    namespace["verify"] = lambda: None
    namespace["OUT"] = ROOT / "figures/group7"
    namespace["main"]()
    original = ET.fromstring(sources[SVG_SOURCE])
    candidate = ET.parse(ROOT / "figures/group7/g7_thesis_fig_06_sensitivity.svg").getroot()
    if non_text_geometry(original) != non_text_geometry(candidate):
        raise RuntimeError("non-text SVG geometry differs from frozen G6")
    print("PASS: frozen inputs and non-text SVG geometry identity")


if __name__ == "__main__":
    main()
