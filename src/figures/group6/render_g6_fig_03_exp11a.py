from __future__ import annotations

import csv
import html
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "figures/group6"
CANON = ROOT / "outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv"
RUNS = ROOT / "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv"
CONDS = ROOT / "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv"
EXPECTED = {CANON:"cf3aedab5935d6af9b3ac7be7b51b954fcb9c403",RUNS:"9b434d7e09e6db7e9de061953b59c53aac2337ad",CONDS:"535dd377d107ddcbf09ecaa13cd66ca723ee738d"}
METRICS=["Top1","Top3","Top5","Top10","Top50","MRR"]
CONDITIONS=["H25","H50-D1","H50-D2","H75","H100 ref."]
JITTER={10:[-.18,-.14,-.10,-.06,-.02,.02,.06,.10,.14,.18],5:[-.12,-.06,0,.06,.12],1:[0]}


def rows(path):
    with path.open(encoding="utf-8-sig",newline="") as h: return list(csv.DictReader(h))


def verify():
    for path,expected in EXPECTED.items():
        actual=subprocess.check_output(["git","hash-object",str(path.relative_to(ROOT))],cwd=ROOT,text=True).strip()
        if actual!=expected: raise RuntimeError(f"blob mismatch for {path}: {actual}")


def main():
    verify()
    canonical=rows(CANON); run_rows=rows(RUNS); condition_rows=rows(CONDS)
    observed=[r for r in canonical if r["row type"]=="OBSERVED_RUN"]
    summaries=[r for r in canonical if r["row type"]=="FROZEN_CONDITION_SUMMARY"]
    if len(observed)!=31 or len(summaries)!=6: raise RuntimeError("unexpected canonical row inventory")
    run_lookup={r["run_id"]:r for r in run_rows}
    if len(run_lookup)!=31: raise RuntimeError("unexpected run-source inventory")
    expected_scopes={"PRIMARY","FROZEN_REFERENCE","H50_D1_DIAGNOSTIC","H50_D2_DIAGNOSTIC"}
    if {r["aggregation_scope"] for r in condition_rows}!=expected_scopes: raise RuntimeError("unexpected condition aggregation scope")
    grouped={key:[] for key in CONDITIONS}
    for row in observed:
        key=row["row_key"]
        if key=="H100_REEXECUTED_CHECK": condition="H100 ref."
        elif row["condition"]=="H50":
            stratum=run_lookup[key]["dominant_stratum"]
            if stratum not in {"D1","D2"}: raise RuntimeError(f"missing H50 dominant_stratum for {key}")
            condition=f"H50-{stratum}"
        else: condition=row["condition"]
        grouped[condition].append(row)
    counts=[len(grouped[c]) for c in CONDITIONS]
    if counts!=[10,5,5,10,1]: raise RuntimeError(f"unexpected condition counts: {counts}")
    if any(int(r["denominator"])!=1056 for r in observed): raise RuntimeError("unexpected denominator")
    for condition in CONDITIONS: grouped[condition].sort(key=lambda r:r["run/seed"])

    W,H,S=1200,800,2.5
    image=Image.new("RGB",(round(W*S),round(H*S)),"white"); draw=ImageDraw.Draw(image)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<rect width="100%" height="100%" fill="white"/>']
    def font(size,bold=False):
        p=Path("C:/Windows/Fonts")/("arialbd.ttf" if bold else "arial.ttf"); return ImageFont.truetype(str(p),round(size*S)) if p.exists() else ImageFont.load_default()
    def text(x,y,value,size=10,anchor="middle",bold=False,fill="#222222"):
        a={"start":"lm","middle":"mm","end":"rm"}[anchor]; draw.text((x*S,y*S),value,font=font(size,bold),fill=fill,anchor=a)
        svg.append(f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"700" if bold else "400"}" fill="{fill}">{html.escape(value)}</text>')
    def line(x1,y1,x2,y2,color="#888888",width=1,dash=None):
        draw.line((x1*S,y1*S,x2*S,y2*S),fill=color,width=max(1,round(width*S)))
        d=f' stroke-dasharray="{dash}"' if dash else ""; svg.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{width}"{d}/>')
    def marker(x,y,diamond=False,color="#4C78A8"):
        r=4.8
        if not diamond:
            draw.ellipse(((x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S),fill="white",outline=color,width=round(1.5*S)); svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="white" stroke="{color}" stroke-width="1.5"/>'); return
        pts=[(x,y-r-1),(x+r+1,y),(x,y+r+1),(x-r-1,y)]; sp=[(a*S,b*S) for a,b in pts]; draw.polygon(sp,fill="#222222"); svg.append(f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in pts)}" fill="#222222"/>')

    text(35,26,"G6-FIG-03 | EXP11A joint size-composition sensitivity",17,"start",True)
    text(35,48,"Observed runs only; descriptive and noncausal; no summaries, CI, p-values, or fitted trends",9.5,"start",False,"#555555")
    xstarts=[65,430,795]; ystarts=[82,428]
    colors={"H25":"#4C78A8","H50-D1":"#F58518","H50-D2":"#54A24B","H75":"#B279A2","H100 ref.":"#222222"}
    for idx,metric in enumerate(METRICS):
        col,row=idx%3,idx//3; left=xstarts[col]; top=ystarts[row]; right=left+315; bottom=top+235
        text(left,top-18,metric,12,"start",True)
        for tick in [0,.25,.5,.75,1]:
            y=bottom-tick*(bottom-top); line(left,y,right,y,"#E4E4E4",1); text(left-8,y,f"{tick:.2f}",8,"end")
        line(left,top,left,bottom,"#444444",1); line(left,bottom,right,bottom,"#444444",1)
        anchors=[left+28+i*68 for i in range(5)]
        line((anchors[3]+anchors[4])/2,top,(anchors[3]+anchors[4])/2,bottom,"#AAAAAA",1,"4 4")
        for ci,condition in enumerate(CONDITIONS):
            text(anchors[ci],bottom+17,condition,7.5,"middle",condition=="H100 ref.")
            offsets=JITTER[len(grouped[condition])]
            for offset,data in zip(offsets,grouped[condition]):
                y=bottom-float(data[metric])*(bottom-top)
                marker(anchors[ci]+offset*55,y,condition=="H100 ref.",colors[condition])
    text(35,775,"Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly.",9,"start",False,"#555555")
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"g6_fig_03_exp11a.svg").write_text("\n".join(svg+["</svg>"])+"\n",encoding="utf-8",newline="\r\n")
    image.save(OUT/"g6_fig_03_exp11a.png",format="PNG",dpi=(300,300),optimize=False,compress_level=9)


if __name__=="__main__": main()
