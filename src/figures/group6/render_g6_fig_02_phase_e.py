from __future__ import annotations

import csv
import html
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv"
EXPECTED_BLOB = "fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61"
OUT = ROOT / "figures/group6"
VARIANTS = [
    ("hierarchical_only", "circle", "#222222", True),
    ("dual_only", "square", "#4C78A8", True),
    ("hierarchical_first_100", "triangle", "#F58518", True),
    ("hierarchical_80_dual_backfill_20", "diamond", "#54A24B", True),
    ("hierarchical_70_dual_backfill_30", "hexagon", "#B279A2", False),
]
DEPTHS = [50, 100, 200]


def verify_blob() -> None:
    actual = subprocess.check_output(["git", "hash-object", str(SOURCE.relative_to(ROOT))], cwd=ROOT, text=True).strip()
    if actual != EXPECTED_BLOB:
        raise RuntimeError(f"source blob mismatch: {actual}")


def font(size, bold=False, scale=2.5):
    path = Path("C:/Windows/Fonts") / ("arialbd.ttf" if bold else "arial.ttf")
    return ImageFont.truetype(str(path), round(size * scale)) if path.exists() else ImageFont.load_default()


def main() -> None:
    verify_blob()
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    allowed = {v[0] for v in VARIANTS}
    if len(rows) != 15 or {r["variant"] for r in rows} != allowed or {int(r["depth"]) for r in rows} != set(DEPTHS):
        raise RuntimeError("unexpected Phase E inventory")
    if any(int(r["denominator"]) != 1056 for r in rows):
        raise RuntimeError("unexpected Phase E denominator")
    if any(r["variant"] == "diagnostic_union_hierarchical_dual" for r in rows):
        raise RuntimeError("diagnostic union cannot be plotted")

    W, H, S = 1200, 675, 2.5
    image = Image.new("RGB", (round(W*S), round(H*S)), "white")
    draw = ImageDraw.Draw(image)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W/120}in" height="{H/120}in" viewBox="0 0 {W} {H}">', '<rect width="100%" height="100%" fill="white"/>']

    def text(x, y, value, size=12, anchor="middle", bold=False, fill="#222222"):
        size = max(size, 13.5)
        a = {"start":"lm","middle":"mm","end":"rm"}[anchor]
        draw.text((x*S,y*S), value, font=font(size,bold,S), fill=fill, anchor=a)
        svg.append(f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"700" if bold else "400"}" fill="{fill}">{html.escape(value)}</text>')

    def line(x1,y1,x2,y2,color="#888888",width=1):
        draw.line((x1*S,y1*S,x2*S,y2*S),fill=color,width=max(1,round(width*S)))
        svg.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{width}"/>')

    def marker(x,y,shape,color,filled=True,r=7):
        fill=color if filled else "white"
        if shape=="circle":
            draw.ellipse(((x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S),fill=fill,outline=color,width=round(1.8*S)); svg.append(f'<circle cx="{x}" cy="{y:.2f}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="1.8"/>'); return
        if shape=="square": pts=[(x-r,y-r),(x+r,y-r),(x+r,y+r),(x-r,y+r)]
        elif shape=="triangle": pts=[(x,y-r-1),(x+r+1,y+r),(x-r-1,y+r)]
        elif shape=="diamond": pts=[(x,y-r-1),(x+r+1,y),(x,y+r+1),(x-r-1,y)]
        else: pts=[(x-r,y),(x-r/2,y-r),(x+r/2,y-r),(x+r,y),(x+r/2,y+r),(x-r/2,y+r)]
        scaled=[(a*S,b*S) for a,b in pts]; draw.polygon(scaled,fill=fill); draw.line(scaled+[scaled[0]],fill=color,width=round(1.8*S),joint="curve")
        svg.append(f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in pts)}" fill="{fill}" stroke="{color}" stroke-width="1.8"/>')

    text(45,32,"Phase E exact-NANDINA coverage",18,"start",True)
    text(45,57,"Descriptive only; no CI, p-values, fitted trends, or connecting lines",10,"start",False,"#555555")
    left,right,top,bottom=100,815,95,565
    def ymap(v): return bottom-v/.35*(bottom-top)
    for tick in [0,.05,.10,.15,.20,.25,.30,.35]:
        y=ymap(tick); line(left,y,right,y,"#E1E1E1",1); text(left-12,y,f"{tick:.2f}",15,"end")
    line(left,top,left,bottom,"#444444",1.2); line(left,bottom,right,bottom,"#444444",1.2)
    # Match the external vertical label in both formats; 17 units = 10.2 pt in PNG.
    label = "Exact-NANDINA coverage"
    label_font = font(17, True, S)
    bbox = label_font.getbbox(label)
    label_image = Image.new("RGBA", (bbox[2]-bbox[0]+8, bbox[3]-bbox[1]+8))
    ImageDraw.Draw(label_image).text((4-bbox[0],4-bbox[1]),label,font=label_font,fill="#222222")
    label_image = label_image.transpose(Image.Transpose.ROTATE_90)
    image.paste(label_image,(round(30*S-label_image.width/2),round((top+bottom)/2*S-label_image.height/2)),label_image)
    svg.append(f'<text x="30" y="{(top+bottom)/2}" transform="rotate(-90 30 {(top+bottom)/2})" text-anchor="middle" dominant-baseline="middle" font-family="Arial, sans-serif" font-size="17" font-weight="700" fill="#222222">{label}</text>')
    anchors={50:200,100:455,200:710}; dodge=[-28,-14,0,14,28]
    lookup={(r["variant"],int(r["depth"])):float(r["exact-NANDINA coverage"]) for r in rows}
    for depth in DEPTHS:
        text(anchors[depth],bottom+23,str(depth),15,"middle",True)
        for i,(variant,shape,color,formal) in enumerate(VARIANTS):
            marker(anchors[depth]+dodge[i],ymap(lookup[(variant,depth)]),shape,color,formal)
    text((left+right)/2,bottom+50,"Recovery depth (ordered categories)",17,"middle")
    text(865,105,"Formal claim variants",11,"start",True)
    for i,(variant,shape,color,formal) in enumerate(VARIANTS[:4]):
        y=137+i*49; marker(878,y,shape,color,formal,6); text(896,y,variant,15,"start")
    text(865,350,"Context only",11,"start",True)
    variant,shape,color,formal=VARIANTS[4]; marker(878,383,shape,color,formal,6); text(896,383,"hierarchical_70_",15,"start"); text(896,403,"dual_backfill_30",15,"start")
    text(865,458,"15 marks = 5 variants x 3 depths",9,"start",False,"#555555")
    text(865,480,"N = 1,056 series",9,"start",False,"#555555")
    text(865,500,"67 DAM / 42 NANDINA",9,"start",False,"#555555")
    text(45,648,"The diagnostic union is excluded from ordinary performance. Context and formal variants retain equal visual weight.",13.5,"start",False,"#555555")
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"g6_fig_02_phase_e.svg").write_text("\n".join(svg+["</svg>"])+"\n",encoding="utf-8",newline="\r\n")
    image.save(OUT/"g6_fig_02_phase_e.png",format="PNG",dpi=(300,300),optimize=False,compress_level=9)


if __name__ == "__main__":
    main()
