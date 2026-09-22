from __future__ import annotations

import csv
import html
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "figures/group6"
SOURCE_A = ROOT / "outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv"
SOURCE_C = ROOT / "outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv"
EXPECTED_BLOBS = {
    SOURCE_A: "cb68583ee2260e4455796bac99ad90995ca7ef92",
    SOURCE_C: "359e4e19b5ef1d44983c03039162209293b2a44c",
}
METRICS = ["Top-1", "Top-3", "Top-5", "Top-10", "MRR@100"]
SERIES = [
    ("Historical", "circle", "#222222"),
    ("Flat (Attempt06)", "square", "#4C78A8"),
    ("Hierarchical (Attempt06)", "triangle", "#F58518"),
    ("D1a (Attempt06)", "diamond", "#54A24B"),
]
COMPARATORS = {
    "HISTORICAL_MINUS_FLAT": "Flat",
    "HISTORICAL_MINUS_HIERARCHICAL": "Hierarchical",
    "HISTORICAL_MINUS_D1A": "D1a",
}


def verify_blob(path: Path, expected: str) -> None:
    actual = subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True
    ).strip()
    if actual != expected:
        raise RuntimeError(f"blob mismatch for {path}: {actual} != {expected}")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class Canvas:
    def __init__(self, width: int, height: int, scale: float = 2.5) -> None:
        self.w, self.h, self.s = width, height, scale
        self.image = Image.new("RGB", (round(width * scale), round(height * scale)), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            '<rect width="100%" height="100%" fill="white"/>',
        ]

    def font(self, size: float, bold: bool = False):
        name = "arialbd.ttf" if bold else "arial.ttf"
        path = Path("C:/Windows/Fonts") / name
        return ImageFont.truetype(str(path), round(size * self.s)) if path.exists() else ImageFont.load_default()

    def text(self, x, y, value, size=12, anchor="middle", bold=False, fill="#222222"):
        pil_anchor = {"start": "lm", "middle": "mm", "end": "rm"}[anchor]
        self.draw.text((x * self.s, y * self.s), value, font=self.font(size, bold), fill=fill, anchor=pil_anchor)
        self.svg.append(
            f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'font-family="Arial, sans-serif" font-size="{size}" font-weight="{"700" if bold else "400"}" fill="{fill}">{html.escape(value)}</text>'
        )

    def line(self, x1, y1, x2, y2, fill="#888888", width=1):
        self.draw.line((x1 * self.s, y1 * self.s, x2 * self.s, y2 * self.s), fill=fill, width=max(1, round(width * self.s)))
        self.svg.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{fill}" stroke-width="{width}"/>')

    def marker(self, x, y, shape, color, size=6, filled=False):
        r, s = size, self.s
        fill = color if filled else "white"
        if shape == "circle":
            self.draw.ellipse(((x-r)*s, (y-r)*s, (x+r)*s, (y+r)*s), fill=fill, outline=color, width=round(1.6*s))
            self.svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="1.6"/>')
            return
        if shape == "square":
            pts = [(x-r,y-r),(x+r,y-r),(x+r,y+r),(x-r,y+r)]
        elif shape == "triangle":
            pts = [(x,y-r-1),(x+r+1,y+r),(x-r-1,y+r)]
        else:
            pts = [(x,y-r-1),(x+r+1,y),(x,y+r+1),(x-r-1,y)]
        scaled = [(a*s,b*s) for a,b in pts]
        self.draw.polygon(scaled, fill=fill)
        self.draw.line(scaled+[scaled[0]], fill=color, width=round(1.6*s), joint="curve")
        points = " ".join(f"{a:.2f},{b:.2f}" for a,b in pts)
        self.svg.append(f'<polygon points="{points}" fill="{fill}" stroke="{color}" stroke-width="1.6"/>')

    def save(self, stem: str):
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{stem}.svg").write_text("\n".join(self.svg + ["</svg>"]) + "\n", encoding="utf-8", newline="\r\n")
        self.image.save(OUT / f"{stem}.png", format="PNG", dpi=(300, 300), optimize=False, compress_level=9)


def xmap(value: float, lo: float, hi: float, left=205, right=950) -> float:
    return left + (value - lo) * (right - left) / (hi - lo)


def axes(c: Canvas, top: float, bottom: float, lo: float, hi: float, ticks: list[float], label: str):
    for tick in ticks:
        x = xmap(tick, lo, hi)
        c.line(x, top, x, bottom, "#E2E2E2", 1)
        c.text(x, bottom + 18, f"{tick:.1f}", 10)
    c.line(205, bottom, 950, bottom, "#444444", 1.2)
    c.text((205 + 950) / 2, bottom + 40, label, 11)


def main() -> None:
    for path, blob in EXPECTED_BLOBS.items():
        verify_blob(path, blob)
    rows = read_rows(SOURCE_A)
    deep = read_rows(SOURCE_C)
    if len(rows) != 15 or len(deep) != 1:
        raise RuntimeError("unexpected HE2 row inventory")
    if {r["metric"] for r in rows} != set(METRICS) or set(COMPARATORS) != {r["comparison"] for r in rows}:
        raise RuntimeError("unexpected HE2 metric/comparator inventory")
    for metric in METRICS:
        values = {r["historical_observed_value"] for r in rows if r["metric"] == metric}
        if len(values) != 1:
            raise RuntimeError(f"Historical repetitions differ for {metric}")
    if any(int(r["EVAL_N"]) != 1056 or int(r["DAM_N"]) != 67 for r in rows + deep):
        raise RuntimeError("unexpected HE2 denominator")

    lookup = {(r["metric"], r["comparison"]): r for r in rows}
    c = Canvas(1000, 1250)
    c.text(40, 28, "G6-FIG-01 | Primary HE2 evidence", 18, "start", True)
    c.text(40, 51, "Offline internal benchmark: 1,056 series / 67 DAM / 42 NANDINA", 10, "start", False, "#555555")

    c.text(40, 82, "A", 16, "start", True)
    c.text(70, 82, "Observed values (no arm-level CI)", 13, "start", True)
    axes(c, 105, 390, 0, 1, [0, .2, .4, .6, .8, 1], "Observed metric value")
    y_positions = {m: 135 + i * 53 for i, m in enumerate(METRICS)}
    offsets = [-12, -4, 4, 12]
    for metric, y in y_positions.items():
        c.text(190, y, metric, 10, "end", True)
        hist = float(next(r["historical_observed_value"] for r in rows if r["metric"] == metric))
        values = [hist] + [float(lookup[(metric, key)]["comparator_observed_value"]) for key in COMPARATORS]
        for (name, shape, color), value, dy in zip(SERIES, values, offsets):
            c.marker(xmap(value, 0, 1), y + dy, shape, color, 5.2, name == "Historical")
    for i, (name, shape, color) in enumerate(SERIES):
        x = 145 + i * 215
        c.marker(x, 452, shape, color, 5, name == "Historical")
        c.text(x + 12, 452, name, 9, "start")

    c.text(40, 495, "B", 16, "start", True)
    c.text(70, 495, "Historical - comparator (frozen 99% CI)", 13, "start", True)
    axes(c, 525, 985, -.1, 1, [-.1, 0, .2, .4, .6, .8, 1], "Paired difference")
    c.line(xmap(0, -.1, 1), 525, xmap(0, -.1, 1), 985, "#333333", 1.4)
    shapes = {"Flat": ("square", "#4C78A8"), "Hierarchical": ("triangle", "#F58518"), "D1a": ("diamond", "#54A24B")}
    row_y = 545
    for metric in METRICS:
        for key, short in COMPARATORS.items():
            r = lookup[(metric, key)]
            y = row_y
            row_y += 27
            c.text(120, y, metric if short == "Flat" else "", 9, "end", short == "Flat")
            c.text(195, y, short, 8.5, "end")
            lo = float(r["frozen_99pct_ci_lower_for_paired_difference"])
            hi = float(r["frozen_99pct_ci_upper_for_paired_difference"])
            est = float(r["paired_difference_historical_minus_comparator"])
            c.line(xmap(lo, -.1, 1), y, xmap(hi, -.1, 1), y, "#555555", 2)
            c.line(xmap(lo, -.1, 1), y-4, xmap(lo, -.1, 1), y+4, "#555555", 1)
            c.line(xmap(hi, -.1, 1), y-4, xmap(hi, -.1, 1), y+4, "#555555", 1)
            shape, color = shapes[short]
            c.marker(xmap(est, -.1, 1), y, shape, color, 4.7)
        row_y += 8

    c.text(40, 1040, "C", 16, "start", True)
    c.text(70, 1040, "Recall@200 - Recall@100 (frozen 95% CI)", 13, "start", True)
    axes(c, 1065, 1150, -.1, 1, [-.1, 0, .2, .4, .6, .8, 1], "Paired recall difference")
    c.line(xmap(0, -.1, 1), 1065, xmap(0, -.1, 1), 1150, "#333333", 1.4)
    r = deep[0]
    lo, est, hi = map(float, (r["frozen CI lower"], r["paired difference"], r["frozen CI upper"]))
    y = 1096
    c.text(195, y, "Hierarchical", 9, "end", True)
    c.line(xmap(lo, -.1, 1), y, xmap(hi, -.1, 1), y, "#555555", 2)
    c.line(xmap(lo, -.1, 1), y-5, xmap(lo, -.1, 1), y+5, "#555555", 1)
    c.line(xmap(hi, -.1, 1), y-5, xmap(hi, -.1, 1), y+5, "#555555", 1)
    c.marker(xmap(est, -.1, 1), y, "triangle", "#F58518", 6)
    c.text(205, 1220, f"Context: Recall@100={float(r['Recall@100']):.3f}; Recall@200={float(r['Recall@200']):.3f}; delta={est:.3f} [{lo:.3f}, {hi:.3f}]", 10, "start", False, "#444444")
    c.save("g6_fig_01_he2")


if __name__ == "__main__":
    main()
