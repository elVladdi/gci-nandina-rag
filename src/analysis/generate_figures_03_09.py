#!/usr/bin/env python3
"""Genera las Figuras 3 a 9 del Capítulo 4 de la tesis NANDINA-RAG-LLM.

El script lee los artefactos JSON/CSV del repositorio y produce figuras en PNG,
SVG y/o PDF, además de un manifiesto de procedencia con las huellas SHA-256 de
los insumos utilizados.

Uso recomendado desde la raíz del repositorio:

    python src/analysis/generate_figures_03_09.py \
        --repo-root . \
        --output-dir outputs/figures/chapter4 \
        --formats png svg \
        --dpi 300

Para la versión final de la tesis, puede activarse el control estricto:

    python src/analysis/generate_figures_03_09.py ... --fail-on-provisional

Ese modo detiene la ejecución cuando detecta resultados normativos calculados con
una huella distinta del evalset congelado o la corrida anterior del reordenador.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd
import seaborn as sns

SCRIPT_VERSION = "1.0.0"
EXPECTED_EVALSET_SHA256 = (
    "ae642d01c0e941ab94a187fb2a820fbc8dcd6259c90d9decb70408b9dea344bb"
)

# Paleta sobria y consistente con el documento.
COLORS = {
    "blue": "#1F4E79",
    "blue_light": "#D9EAF7",
    "teal": "#168C8C",
    "teal_light": "#D9F0EF",
    "green": "#4F8A5B",
    "green_light": "#E3F0E6",
    "orange": "#D97706",
    "orange_light": "#FCE8CC",
    "red": "#B5473C",
    "red_light": "#F5DDDA",
    "purple": "#6B5CA5",
    "gray": "#5F6B73",
    "gray_light": "#EEF1F3",
    "black": "#222222",
}


@dataclass
class Inputs:
    bm25_flat: Path
    dense: Path
    hierarchical: Path
    candidate_pool: Path
    historical: Path
    hybrid: Path
    hybrid_source_contribution: Path
    rerank: Path
    auditability: Path


class FigureInputError(RuntimeError):
    """Error de insumo requerido para generar una figura."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera las Figuras 3 a 9 del Capítulo 4."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Raíz del repositorio. Predeterminado: directorio actual.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/figures/chapter4"),
        help="Directorio de salida, relativo a --repo-root o absoluto.",
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=("png", "svg", "pdf"),
        default=("png", "svg"),
        help="Formatos de salida.",
    )
    parser.add_argument("--dpi", type=int, default=300, help="Resolución PNG/PDF.")
    parser.add_argument(
        "--include-titles",
        action="store_true",
        help="Incluye el título completo dentro de cada imagen. Por defecto se omite porque Word ya usa pie de figura.",
    )
    parser.add_argument(
        "--fail-on-provisional",
        action="store_true",
        help="Falla si detecta resultados provisionales pendientes de reejecución.",
    )
    return parser.parse_args()


def configure_style() -> None:
    sns.set_theme(style="whitegrid")
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#808080",
            "grid.color": "#D9DEE2",
            "grid.linewidth": 0.6,
            "axes.linewidth": 0.7,
            "savefig.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def resolve_first(root: Path, candidates: Iterable[str]) -> Path:
    tried: list[Path] = []
    for item in candidates:
        p = Path(item)
        search_paths = [p] if p.is_absolute() else [root / p, root.parent / p]
        for candidate in search_paths:
            candidate = candidate.resolve()
            tried.append(candidate)
            if candidate.exists():
                return candidate
    raise FigureInputError(
        "No se encontró un insumo requerido. Rutas examinadas:\n- "
        + "\n- ".join(str(p) for p in tried)
    )


def discover_inputs(root: Path) -> Inputs:
    return Inputs(
        bm25_flat=resolve_first(
            root,
            [
                "outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/metrics.json",
            ],
        ),
        dense=resolve_first(
            root,
            [
                "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/metrics.json",
            ],
        ),
        hierarchical=resolve_first(
            root,
            [
                "outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1/metrics.json",
            ],
        ),
        candidate_pool=resolve_first(
            root,
            [
                "outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_metrics.json",
            ],
        ),
        historical=resolve_first(
            root,
            [
                "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_metrics.json",
            ],
        ),
        hybrid=resolve_first(
            root,
            [
                "outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/hybrid_metrics.json",
            ],
        ),
        hybrid_source_contribution=resolve_first(
            root,
            [
                "outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/hybrid_source_contribution.csv",
            ],
        ),
        rerank=resolve_first(
            root,
            [
                "outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/llm_rerank_metrics.json",
            ],
        ),
        auditability=resolve_first(
            root,
            [
                "outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_quality_metrics.json",
            ],
        ),
    )


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise FigureInputError(f"El archivo no contiene un objeto JSON: {path}")
    return data


def load_input(path: Path) -> Any:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    return load_json(path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decimal_comma(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def pct(value: float, digits: int = 1) -> str:
    return f"{100 * value:.{digits}f}%".replace(".", ",")


def get_output_dir(root: Path, configured: Path) -> Path:
    output = configured if configured.is_absolute() else root / configured
    output.mkdir(parents=True, exist_ok=True)
    return output.resolve()


def add_full_title(fig: plt.Figure, title: str, enabled: bool) -> None:
    if enabled:
        fig.suptitle(title, y=0.995, fontsize=11, fontweight="bold", color=COLORS["black"])


def add_note(fig: plt.Figure, text: str, *, y: float = 0.005, color: str | None = None) -> None:
    fig.text(
        0.01,
        y,
        text,
        ha="left",
        va="bottom",
        fontsize=7.2,
        color=color or COLORS["gray"],
        wrap=True,
    )


def save_figure(
    fig: plt.Figure,
    output_dir: Path,
    stem: str,
    formats: Iterable[str],
    dpi: int,
) -> list[Path]:
    generated: list[Path] = []
    for fmt in formats:
        path = output_dir / f"{stem}.{fmt}"
        fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.08)
        generated.append(path)
    plt.close(fig)
    return generated


def draw_box(
    ax: plt.Axes,
    xy: tuple[float, float],
    width: float,
    height: float,
    text: str,
    edge: str,
    face: str,
    fontsize: float = 8.5,
) -> None:
    rect = Rectangle(xy, width, height, linewidth=1.2, edgecolor=edge, facecolor=face)
    ax.add_patch(rect)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=COLORS["black"],
        wrap=True,
    )


def draw_arrow(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float], color: str) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=1.1,
            color=color,
            connectionstyle="arc3,rad=0",
        )
    )


def fig03_information_flow(include_titles: bool) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7.2, 4.65))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.2)
    ax.axis("off")
    add_full_title(
        fig,
        "Flujo de transformación de datos aduaneros y fuentes normativas en información auditable",
        include_titles,
    )

    # Carril histórico.
    ax.add_patch(Rectangle((0.15, 3.9), 7.75, 2.8, facecolor="#F7FBF7", edgecolor=COLORS["green"], linewidth=0.9))
    ax.text(0.35, 6.45, "Información histórica", color=COLORS["green"], fontweight="bold", fontsize=9)
    boxes_hist = [
        ((0.45, 5.0), 1.35, 0.85, "Series de DAM"),
        ((2.05, 5.0), 1.45, 0.85, "Normalización\ny curación"),
        ((3.75, 5.0), 1.45, 0.85, "Banco histórico\netiquetado"),
        ((5.45, 5.0), 1.45, 0.85, "Recuperación\nBM25"),
        ((7.15, 5.0), 1.15, 0.85, "Top-3\nfijo"),
    ]
    for xy, w, h, label in boxes_hist:
        draw_box(ax, xy, w, h, label, COLORS["green"], COLORS["green_light"])
    for x1, x2 in [(1.80, 2.05), (3.50, 3.75), (5.20, 5.45), (6.90, 7.15)]:
        draw_arrow(ax, (x1, 5.425), (x2, 5.425), COLORS["green"])

    # Carril normativo.
    ax.add_patch(Rectangle((0.15, 0.55), 7.75, 2.8, facecolor="#F7FBFC", edgecolor=COLORS["teal"], linewidth=0.9))
    ax.text(0.35, 3.10, "Información normativa", color=COLORS["teal"], fontweight="bold", fontsize=9)
    boxes_norm = [
        ((0.45, 1.65), 1.35, 0.85, "Fuentes\nnormativas"),
        ((2.05, 1.65), 1.45, 0.85, "Estructuración\ny auditoría"),
        ((3.75, 1.65), 1.45, 0.85, "Corpus\njerárquico"),
        ((5.45, 1.65), 1.45, 0.85, "Recuperación\npor candidato"),
        ((7.15, 1.65), 1.15, 0.85, "Evidencia\nnormativa"),
    ]
    for xy, w, h, label in boxes_norm:
        draw_box(ax, xy, w, h, label, COLORS["teal"], COLORS["teal_light"])
    for x1, x2 in [(1.80, 2.05), (3.50, 3.75), (5.20, 5.45), (6.90, 7.15)]:
        draw_arrow(ax, (x1, 2.075), (x2, 2.075), COLORS["teal"])

    # Convergencia y salida.
    draw_box(ax, (8.75, 3.83), 1.25, 1.0, "Contexto\nRAG", COLORS["blue"], COLORS["blue_light"], 8.5)
    draw_box(ax, (10.35, 3.83), 1.25, 1.0, "Explicación\nLLM", COLORS["purple"], "#ECE8F7", 8.5)
    draw_box(ax, (9.55, 1.95), 1.25, 0.95, "Ficha\nauditable", COLORS["orange"], COLORS["orange_light"], 8.5)
    draw_box(ax, (9.55, 0.55), 1.25, 0.95, "Revisión\nexperta", COLORS["gray"], COLORS["gray_light"], 8.5)

    draw_arrow(ax, (8.30, 5.425), (9.05, 4.83), COLORS["green"])
    draw_arrow(ax, (8.30, 2.075), (9.05, 3.83), COLORS["teal"])
    draw_arrow(ax, (10.00, 4.33), (10.35, 4.33), COLORS["blue"])
    draw_arrow(ax, (10.98, 3.83), (10.35, 2.90), COLORS["purple"])
    draw_arrow(ax, (10.18, 1.95), (10.18, 1.50), COLORS["gray"])

    ax.text(
        6.2,
        0.18,
        "La salida organiza información y evidencia para revisión; no constituye una clasificación oficial.",
        ha="center",
        va="center",
        fontsize=7.5,
        color=COLORS["gray"],
    )
    return fig


def _normative_methods(flat: dict[str, Any], dense: dict[str, Any], hier: dict[str, Any]) -> tuple[list[str], np.ndarray]:
    f = flat["global_metrics"]
    d = dense["global_metrics"]
    h = hier["metrics_by_method"]["BM25_hierarchical_v0.1"]
    dual = hier["metrics_by_method"]["BM25_dual_protected_top_5_backfill"]
    labels = ["BM25 plano*", "Text2Trade*", "BM25 jerárquico*", "BM25 dual"]
    rows = [
        [f["top_1_accuracy"], f["top_3_accuracy"], f["top_10_accuracy"], f["mrr"], f["recall_at_100"]],
        [d["top_1_accuracy"], d["top_3_accuracy"], d["top_10_accuracy"], d["mrr"], d["recall_at_100"]],
        [h["top_1"], h["top_3"], h["top_10"], h["mrr"], h["recall_at_100"]],
        [dual["top_1"], dual["top_3"], dual["top_10"], dual["mrr"], dual["recall_at_100"]],
    ]
    return labels, np.array(rows, dtype=float)


def fig04_retrieval_performance(
    flat: dict[str, Any],
    dense: dict[str, Any],
    hier: dict[str, Any],
    historical: dict[str, Any],
    include_titles: bool,
    provisional: bool,
) -> plt.Figure:
    labels, normative = _normative_methods(flat, dense, hier)
    hm = historical["metrics"]
    historical_row = np.array(
        [[hm["exact_at_1"], hm["exact_at_3"], hm["exact_at_10"], hm["mrr"], hm["exact_at_100"]]],
        dtype=float,
    )
    data = np.vstack([normative, historical_row])
    row_labels = labels + ["BM25 histórico"]
    columns = ["Top-1", "Top-3", "Top-10", "MRR", "Recall@100"]

    fig, ax = plt.subplots(figsize=(7.2, 4.35))
    add_full_title(fig, "Comparación del desempeño temprano y la cobertura profunda de los métodos de recuperación", include_titles)
    sns.heatmap(
        data,
        ax=ax,
        cmap=sns.light_palette(COLORS["blue"], as_cmap=True),
        vmin=0,
        vmax=1,
        cbar_kws={"label": "Proporción", "shrink": 0.78},
        linewidths=0.7,
        linecolor="white",
        annot=False,
    )
    ax.set_xticklabels(columns, rotation=0)
    ax.set_yticklabels(row_labels, rotation=0)
    ax.set_xlabel("")
    ax.set_ylabel("")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            value = data[i, j]
            color = "white" if value >= 0.58 else COLORS["black"]
            ax.text(j + 0.5, i + 0.5, decimal_comma(value), ha="center", va="center", fontsize=8, color=color)
    if provisional:
        add_note(
            fig,
            "* BM25 plano, Text2Trade y BM25 jerárquico corresponden a corridas provisionales pendientes de reejecución con el evalset congelado.",
            color=COLORS["red"],
        )
        fig.subplots_adjust(bottom=0.12)
    return fig


def fig05_normative_pool(pool: dict[str, Any], include_titles: bool) -> plt.Figure:
    depths = [10, 20, 50, 100, 200]
    metrics = pool["metrics_by_strategy"]
    series = {
        "Solo jerárquico": [metrics["hierarchical_only"][f"final_pool_at_{k}"] for k in depths],
        "Solo dual": [metrics["dual_only"][f"final_pool_at_{k}"] for k in depths],
        "Jerárquico 70 + dual 30": [metrics["hierarchical_70_dual_backfill_30"][f"final_pool_at_{k}"] for k in depths],
        "Unión diagnóstica": [metrics["hierarchical_only"][f"union_oracle_at_{k}"] for k in depths],
    }
    colors = [COLORS["teal"], COLORS["orange"], COLORS["blue"], COLORS["gray"]]
    styles = ["-", "-", "-", "--"]

    fig, ax = plt.subplots(figsize=(7.2, 4.25))
    add_full_title(fig, "Cobertura del pool normativo según estrategia y profundidad de recuperación", include_titles)
    for (name, values), color, style in zip(series.items(), colors, styles):
        ax.plot(depths, values, marker="o", markersize=4.5, linewidth=1.8, linestyle=style, label=name, color=color)
        ax.text(depths[-1] + 3, values[-1], pct(values[-1], 1), va="center", fontsize=7.5, color=color)
    ax.set_xlim(5, 220)
    ax.set_ylim(0, 0.70)
    ax.set_xticks(depths)
    ax.set_xlabel("Profundidad del pool")
    ax.set_ylabel("Cobertura exacta")
    ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.legend(loc="upper left", frameon=True, ncol=2)
    ax.grid(axis="x", visible=False)
    add_note(fig, "La unión diagnóstica representa un techo de cobertura y no un ranking entregable.")
    fig.subplots_adjust(bottom=0.13, right=0.91)
    return fig


def fig06_historical_support(historical: dict[str, Any], include_titles: bool) -> plt.Figure:
    buckets = ["1", "2-4", "5-9", "10+"]
    bdata = historical["metrics"]["by_support_bucket"]
    metrics = [
        ("Top-1", "exact_at_1", COLORS["blue"]),
        ("Top-3", "exact_at_3", COLORS["teal"]),
        ("Top-10", "exact_at_10", COLORS["green"]),
        ("MRR", "mrr", COLORS["orange"]),
    ]
    x = np.arange(len(buckets))
    width = 0.19

    fig, ax = plt.subplots(figsize=(7.2, 4.35))
    add_full_title(fig, "Desempeño de la recuperación histórica según disponibilidad de precedentes", include_titles)
    for idx, (label, key, color) in enumerate(metrics):
        values = [bdata[b][key] for b in buckets]
        ax.bar(x + (idx - 1.5) * width, values, width, label=label, color=color, edgecolor="white", linewidth=0.5)
    labels = [f"{b}\n(n={bdata[b]['cases']})" for b in buckets]
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("Proporción / MRR")
    ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Cantidad de precedentes históricos del código")
    ax.legend(loc="lower right", ncol=4, frameon=True)
    ax.grid(axis="x", visible=False)
    add_note(fig, "Los grupos con 1 y 2–4 precedentes contienen pocos casos; se muestran como diagnóstico interno y no como estimación poblacional.")
    fig.subplots_adjust(bottom=0.16)
    return fig


def fig07_source_contribution(
    hybrid: dict[str, Any], source_df: pd.DataFrame, include_titles: bool
) -> plt.Figure:
    selected = hybrid["selected_strategy"]
    strategy = selected["pool_strategy"]
    subset = source_df[source_df["pool_strategy"] == strategy].copy()
    by_source = {
        str(row["source_membership"]): int(row["cases_where_expected_source_at_100"])
        for _, row in subset.iterrows()
    }
    counts = np.array(
        [by_source.get("historical", 0), by_source.get("both", 0), by_source.get("normative", 0)],
        dtype=int,
    )
    labels = ["Solo histórico", "Histórico y normativo", "Solo normativo"]
    colors = [COLORS["green"], COLORS["teal"], COLORS["orange"]]
    total = counts.sum()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 4.05), gridspec_kw={"width_ratios": [1.08, 1.0]})
    add_full_title(fig, "Contribución diferenciada de la recuperación histórica y la evidencia normativa en el pool híbrido", include_titles)

    left = 0
    for count, label, color in zip(counts, labels, colors):
        proportion = count / total if total else 0
        ax1.barh([0], [proportion], left=left, color=color, height=0.42, label=label)
        if proportion > 0.06:
            ax1.text(left + proportion / 2, 0, f"{count}\n{pct(proportion, 1)}", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        left += proportion
    ax1.set_xlim(0, 1)
    ax1.set_yticks([])
    ax1.set_xlabel("Distribución de los 1 006 códigos de referencia")
    ax1.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax1.legend(loc="upper center", bbox_to_anchor=(0.5, 1.20), ncol=1, frameon=False)
    ax1.grid(axis="y", visible=False)

    metric_items = [
        ("Top-1", selected["exact_at_1"], COLORS["blue"]),
        ("Top-3", selected["exact_at_3"], COLORS["teal"]),
        ("Top-10", selected["exact_at_10"], COLORS["green"]),
        ("MRR", selected["mrr"], COLORS["orange"]),
    ]
    y_positions = np.arange(len(metric_items))[::-1]
    for y, (name, value, color) in zip(y_positions, metric_items):
        ax2.plot([0, 1], [y, y], color=color, linewidth=2)
        ax2.scatter([0, 1], [y, y], color=color, s=38, zorder=3)
        ax2.text(1.07, y, decimal_comma(value), ha="left", va="center", fontsize=8, color=color)
    ax2.set_xlim(-0.15, 1.28)
    ax2.set_ylim(-0.55, len(metric_items) - 0.45)
    ax2.set_xticks([0, 1], ["Histórico", "Híbrido"])
    ax2.set_yticks(y_positions, [item[0] for item in metric_items])
    ax2.set_ylabel("")
    ax2.text(0.5, -0.42, "Sin cambio en las métricas", ha="center", va="bottom", fontsize=8, color=COLORS["gray"])
    ax2.grid(axis="x", visible=False)
    add_note(fig, "El bloque normativo aportó evidencia concurrente; no produjo rescates adicionales porque el histórico ya cubría todas las etiquetas a Top-100.")
    fig.subplots_adjust(bottom=0.16, wspace=0.35)
    return fig


def fig08_reranking(rerank: dict[str, Any], include_titles: bool, provisional: bool) -> plt.Figure:
    m = rerank["metrics"]
    metric_names = ["Top-1", "Top-3", "Top-5", "Top-10", "MRR"]
    original = [m["original_top_1"], m["original_top_3"], m["original_top_5"], m["original_top_10"], m["original_mrr"]]
    llm = [m["llm_top_1"], m["llm_top_3"], m["llm_top_5"], m["llm_top_10"], m["llm_mrr"]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 4.25), gridspec_kw={"width_ratios": [1.4, 0.9]})
    add_full_title(fig, "Variación del ranking antes y después del reordenamiento diagnóstico con LLM", include_titles)

    x = np.arange(len(metric_names))
    width = 0.36
    ax1.bar(x - width / 2, original, width, label="Ranking original", color=COLORS["blue"])
    ax1.bar(x + width / 2, llm, width, label="LLM", color=COLORS["purple"])
    ax1.set_xticks(x, metric_names)
    ax1.set_ylim(0, 0.58)
    ax1.set_ylabel("Proporción / MRR")
    ax1.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax1.legend(loc="upper right", frameon=True)
    ax1.grid(axis="x", visible=False)
    for i, (a, b) in enumerate(zip(original, llm)):
        ax1.text(i - width / 2, a + 0.012, decimal_comma(a), ha="center", va="bottom", fontsize=7)
        ax1.text(i + width / 2, b + 0.012, decimal_comma(b), ha="center", va="bottom", fontsize=7)

    outcomes = [m["won_cases"], m["lost_cases"], m["unchanged_cases"]]
    outcome_labels = ["Ganados", "Perdidos", "Sin cambio"]
    outcome_colors = [COLORS["green"], COLORS["red"], COLORS["gray"]]
    left = 0
    for count, label, color in zip(outcomes, outcome_labels, outcome_colors):
        prop = count / m["cases_evaluated"]
        ax2.barh([0], [prop], left=left, height=0.40, color=color, label=label)
        if prop > 0.09:
            ax2.text(left + prop / 2, 0, str(count), ha="center", va="center", color="white", fontweight="bold", fontsize=8)
        left += prop
    ax2.set_xlim(0, 1)
    ax2.set_yticks([])
    ax2.set_xlabel("Resultado por caso")
    ax2.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax2.legend(loc="upper center", bbox_to_anchor=(0.5, 1.20), frameon=False)
    ax2.set_title(f"Rankings incompletos: {m['ranking_incomplete_cases']} de {m['cases_evaluated']}", loc="left", fontsize=8.5, color=COLORS["red"], pad=10)
    ax2.grid(axis="y", visible=False)

    if provisional:
        add_note(fig, "Resultado provisional: la corrida disponible utilizó un conjunto anterior y debe repetirse con el pool final de clase 87.", color=COLORS["red"])
        fig.subplots_adjust(bottom=0.15, wspace=0.32)
    return fig


def fig09_auditability(audit: dict[str, Any], include_titles: bool) -> plt.Figure:
    m = audit["metrics"]
    hard = [
        ("JSON válido", m["json_valido_rate"]),
        ("Top-3 completo", m["top3_completo_rate"]),
        ("Ranking preservado", m["ranking_preservado_rate"]),
        ("Sin códigos fuera del pool", m["sin_codigos_fuera_pool_rate"]),
        ("Sin códigos inventados", m["sin_codigos_inventados_rate"]),
        ("Evidencia histórica citada", m["evidencia_historica_citada_por_candidato_rate"]),
        ("Evidencia normativa citada", m["evidencia_normativa_citada_por_candidato_rate"]),
        ("Comparación Top-3", m["comparacion_top3_presente_rate"]),
        ("Conclusión auditable", m["conclusion_auditable_presente_rate"]),
        ("Advertencia final", m["advertencia_final_presente_rate"]),
        ("Sin clasificación oficial", m["sin_clasificacion_oficial_rate"]),
        ("Sin señales de reordenamiento", m["sin_senales_reranking_rate"]),
    ]
    secondary = [
        ("Coincidencias observables", m["coincidencias_observables_rate"]),
        ("Diferencias observables", m["diferencias_observables_rate"]),
        ("Advertencia normativa genérica", m["advertencia_normativa_generica_rate"]),
        ("Advertencia de datos faltantes", m["advertencia_datos_faltantes_rate"]),
    ]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 7.45), gridspec_kw={"height_ratios": [2.35, 1.0]})
    add_full_title(fig, "Cumplimiento de los controles de auditabilidad de las explicaciones Top-3", include_titles)

    def bar_panel(ax: plt.Axes, rows: list[tuple[str, float]], title: str, show_threshold: bool) -> None:
        labels = [r[0] for r in rows][::-1]
        values = [r[1] for r in rows][::-1]
        colors = [COLORS["green"] if v >= 0.95 else COLORS["orange"] if v >= 0.70 else COLORS["red"] for v in values]
        y = np.arange(len(labels))
        ax.barh(y, values, color=colors, height=0.62)
        ax.set_yticks(y, labels)
        ax.set_xlim(0, 1.06)
        ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
        ax.set_title(title, loc="left", fontweight="bold")
        ax.grid(axis="y", visible=False)
        if show_threshold:
            ax.axvline(0.95, color=COLORS["gray"], linestyle="--", linewidth=1, label="Umbral 95 %")
            ax.legend(loc="lower right", frameon=False)
        for yi, v in zip(y, values):
            ax.text(min(v + 0.012, 1.01), yi, pct(v, 0), va="center", fontsize=7.5, color=COLORS["black"])

    bar_panel(ax1, hard, "Controles estructurales y de trazabilidad", True)
    bar_panel(ax2, secondary, "Controles secundarios de contenido y prudencia", False)
    ax2.text(0.99, -0.30, f"Puntaje medio: {pct(m['score_promedio_auditabilidad_por_caso'], 1)}", transform=ax2.transAxes, ha="right", fontsize=8.5, fontweight="bold", color=COLORS["blue"])
    add_note(fig, "Los porcentajes miden cumplimiento estructural y documental; no representan corrección jurídica de la subpartida.")
    fig.subplots_adjust(left=0.34, right=0.97, bottom=0.10, hspace=0.38)
    return fig


def assess_provisional(flat: dict[str, Any], dense: dict[str, Any], hier: dict[str, Any], rerank: dict[str, Any]) -> dict[str, Any]:
    flat_sha = flat.get("input", {}).get("evalset_sha256")
    dense_sha = dense.get("input", {}).get("evalset_sha256")
    hier_sha = hier.get("input", {}).get("evalset_sha256")
    normative_provisional = any(
        sha and sha != EXPECTED_EVALSET_SHA256 for sha in (flat_sha, dense_sha, hier_sha)
    )
    rerank_input = str(rerank.get("inputs", {}).get("hybrid_pool", ""))
    rerank_provisional = "hybrid_pool_data_aduanas_clase87_v0.1" not in rerank_input
    return {
        "normative_provisional": normative_provisional,
        "normative_evalset_sha256": {
            "bm25_flat": flat_sha,
            "text2trade": dense_sha,
            "hierarchical": hier_sha,
            "expected": EXPECTED_EVALSET_SHA256,
        },
        "rerank_provisional": rerank_provisional,
        "rerank_input": rerank_input,
    }


def main() -> int:
    args = parse_args()
    configure_style()
    root = args.repo_root.resolve()
    output_dir = get_output_dir(root, args.output_dir)

    try:
        inputs = discover_inputs(root)
        data = {name: load_input(getattr(inputs, name)) for name in inputs.__dataclass_fields__}
    except FigureInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    provisional = assess_provisional(data["bm25_flat"], data["dense"], data["hierarchical"], data["rerank"])
    if args.fail_on_provisional and (provisional["normative_provisional"] or provisional["rerank_provisional"]):
        print("ERROR: se detectaron resultados provisionales pendientes de reejecución.", file=sys.stderr)
        print(json.dumps(provisional, ensure_ascii=False, indent=2), file=sys.stderr)
        return 3

    figures: list[tuple[str, plt.Figure]] = [
        ("figura_03_flujo_transformacion_informacion", fig03_information_flow(args.include_titles)),
        (
            "figura_04_desempeno_recuperacion",
            fig04_retrieval_performance(
                data["bm25_flat"],
                data["dense"],
                data["hierarchical"],
                data["historical"],
                args.include_titles,
                provisional["normative_provisional"],
            ),
        ),
        ("figura_05_cobertura_pool_normativo", fig05_normative_pool(data["candidate_pool"], args.include_titles)),
        ("figura_06_desempeno_soporte_historico", fig06_historical_support(data["historical"], args.include_titles)),
        ("figura_07_contribucion_historica_normativa", fig07_source_contribution(data["hybrid"], data["hybrid_source_contribution"], args.include_titles)),
        (
            "figura_08_reordenamiento_llm",
            fig08_reranking(data["rerank"], args.include_titles, provisional["rerank_provisional"]),
        ),
        ("figura_09_controles_auditabilidad", fig09_auditability(data["auditability"], args.include_titles))
    ]

    output_files: dict[str, list[str]] = {}
    for stem, fig in figures:
        paths = save_figure(fig, output_dir, stem, args.formats, args.dpi)
        output_files[stem] = [str(p.relative_to(root)) if p.is_relative_to(root) else str(p) for p in paths]

    input_manifest = {
        name: {
            "path": str(getattr(inputs, name)),
            "sha256": sha256(getattr(inputs, name)),
        }
        for name in inputs.__dataclass_fields__
    }
    manifest = {
        "script_version": SCRIPT_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(root),
        "output_dir": str(output_dir),
        "formats": list(args.formats),
        "dpi": args.dpi,
        "provisional_status": provisional,
        "inputs": input_manifest,
        "outputs": output_files,
        "notes": [
            "Las Figuras 4 y 8 incorporan avisos automáticos mientras sus corridas permanezcan provisionales.",
            "Los títulos completos pueden incluirse con --include-titles; por defecto se asume que el documento Word contiene el pie de figura.",
        ],
    }
    manifest_path = output_dir / "manifest_figuras_03_09.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Figuras generadas en: {output_dir}")
    for stem, paths in output_files.items():
        print(f"- {stem}: {', '.join(paths)}")
    print(f"- manifiesto: {manifest_path}")
    if provisional["normative_provisional"] or provisional["rerank_provisional"]:
        print("ADVERTENCIA: se detectaron resultados provisionales. Consulte el manifiesto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
