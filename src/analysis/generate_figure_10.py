#!/usr/bin/env python3
"""Genera la Figura 10 del Capítulo 4 sin modificar las Figuras 3 a 9.

La figura resume categorías de error y advertencias por etapa del piloto. Cada
barra usa el denominador de su propio instrumento, porque las categorías no son
mutuamente excluyentes ni proceden del mismo universo de casos.

Uso recomendado desde la raíz del repositorio:

    python src/analysis/generate_figure_10.py \
        --repo-root . \
        --output-dir outputs/figures/chapter4 \
        --formats png svg \
        --dpi 300
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import seaborn as sns

SCRIPT_VERSION = "1.0.0"

COLORS = {
    "blue": "#1F4E79",
    "teal": "#168C8C",
    "green": "#4F8A5B",
    "orange": "#D97706",
    "red": "#B5473C",
    "purple": "#6B5CA5",
    "gray": "#5F6B73",
    "black": "#222222",
}


class FigureInputError(RuntimeError):
    """Error de insumo requerido para generar la figura."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera la Figura 10 del Capítulo 4."
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
        "--include-title",
        action="store_true",
        help="Incluye el título completo dentro de la imagen.",
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
        path = Path(item)
        search_paths = [path] if path.is_absolute() else [root / path, root.parent / path]
        for candidate in search_paths:
            candidate = candidate.resolve()
            tried.append(candidate)
            if candidate.exists():
                return candidate
    raise FigureInputError(
        "No se encontró un insumo requerido. Rutas examinadas:\n- "
        + "\n- ".join(str(path) for path in tried)
    )


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise FigureInputError(f"El archivo no contiene un objeto JSON: {path}")
    return data


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pct(value: float, digits: int = 1) -> str:
    return f"{100 * value:.{digits}f}%".replace(".", ",")


def fmt_int(value: int) -> str:
    return f"{int(value):,}".replace(",", " ")


def failures_from_rate(total: int, success_rate: float) -> int:
    return max(0, int(total) - int(round(float(success_rate) * int(total))))


def save_figure(
    fig: plt.Figure,
    output_dir: Path,
    formats: Iterable[str],
    dpi: int,
) -> list[Path]:
    generated: list[Path] = []
    output_dir.mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        path = output_dir / f"figura_10_distribucion_errores_advertencias.{fmt}"
        fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.08)
        generated.append(path)
    plt.close(fig)
    return generated


def build_figure(
    splits_metadata: dict[str, Any],
    corpus_audit: dict[str, Any],
    candidate_pool: dict[str, Any],
    historical: dict[str, Any],
    rerank: dict[str, Any],
    auditability: dict[str, Any],
    include_title: bool,
) -> plt.Figure:
    curation = splits_metadata["curation"]
    scope_rows = int(curation["source_rows_scope_class"])
    excluded_rows = int(curation["excluded_duplicate_rows"])

    historical_metrics = historical["metrics"]
    eval_cases = int(
        historical_metrics.get("cases_evaluated", historical_metrics.get("cases", 0))
    )
    outside_top1 = failures_from_rate(eval_cases, historical_metrics["exact_at_1"])
    outside_top3 = failures_from_rate(eval_cases, historical_metrics["exact_at_3"])
    outside_top10 = failures_from_rate(eval_cases, historical_metrics["exact_at_10"])
    absent_history = int(
        historical_metrics.get("cases_nandina_absent_in_history", 0)
    )
    support_buckets = historical_metrics["by_support_bucket"]
    low_support_cases = sum(
        int(support_buckets[bucket]["cases"]) for bucket in ("1", "2-4", "5-9")
    )

    corpus_counts = corpus_audit["counts"]
    corpus_hierarchy = corpus_audit["hierarchy"]
    corpus_nandina8 = int(
        corpus_counts.get(
            "nandina_8d",
            corpus_counts.get("by_level", {}).get("nandina_8d", 0),
        )
    )
    missing_parent_hs6 = int(corpus_hierarchy["nandina8_missing_parent_hs6"])
    missing_parent_4d = int(corpus_hierarchy["nandina8_missing_parent_4d"])
    conflicting_groups = int(
        corpus_hierarchy.get("conflicting_parent_duplicates", 0)
    )

    pool_metrics = candidate_pool["metrics_by_strategy"]["hierarchical_only"]
    pool_cases = int(pool_metrics["cases_total"])
    neither_top100 = int(pool_metrics["neither_recovers_at_100"])

    rerank_metrics = rerank["metrics"]
    rerank_cases = int(rerank_metrics["cases_evaluated"])
    rerank_lost = int(rerank_metrics["lost_cases"])
    rerank_incomplete = int(rerank_metrics["ranking_incomplete_cases"])

    audit_metrics = auditability["metrics"]
    explanation_cases = int(audit_metrics["casos_procesados"])
    failures = auditability.get("fallos_por_tipo", {})
    no_matches = int(
        failures.get(
            "observable_matches_missing",
            failures_from_rate(
                explanation_cases,
                audit_metrics["coincidencias_observables_rate"],
            ),
        )
    )
    no_generic_warning = int(
        failures.get(
            "generic_normative_warning_missing",
            failures_from_rate(
                explanation_cases,
                audit_metrics["advertencia_normativa_generica_rate"],
            ),
        )
    )
    no_missing_data_warning = int(
        failures.get(
            "missing_data_warning_absent",
            failures_from_rate(
                explanation_cases,
                audit_metrics["advertencia_datos_faltantes_rate"],
            ),
        )
    )
    no_conclusion = int(
        failures.get(
            "conclusion_auditable_missing",
            failures_from_rate(
                explanation_cases,
                audit_metrics["conclusion_auditable_presente_rate"],
            ),
        )
    )

    main_rows = [
        ("Curación: filas excluidas", excluded_rows, scope_rows, COLORS["blue"]),
        ("Histórico: fuera de Top-1", outside_top1, eval_cases, COLORS["green"]),
        ("Histórico: fuera de Top-3", outside_top3, eval_cases, COLORS["green"]),
        ("Histórico: fuera de Top-10", outside_top10, eval_cases, COLORS["green"]),
        ("Histórico: soporte < 10", low_support_cases, eval_cases, COLORS["green"]),
        (
            "Normativo: sin padre HS-6",
            missing_parent_hs6,
            corpus_nandina8,
            COLORS["teal"],
        ),
        (
            "Normativo: sin padre 4D",
            missing_parent_4d,
            corpus_nandina8,
            COLORS["teal"],
        ),
        (
            "Pool normativo: no recuperado a Top-100",
            neither_top100,
            pool_cases,
            COLORS["orange"],
        ),
    ]
    llm_rows = [
        (
            "Reordenamiento: casos perdidos",
            rerank_lost,
            rerank_cases,
            COLORS["red"],
        ),
        (
            "Reordenamiento: ranking incompleto",
            rerank_incomplete,
            rerank_cases,
            COLORS["red"],
        ),
        (
            "Explicación: sin coincidencias observables",
            no_matches,
            explanation_cases,
            COLORS["purple"],
        ),
        (
            "Explicación: sin advertencia normativa genérica",
            no_generic_warning,
            explanation_cases,
            COLORS["purple"],
        ),
        (
            "Explicación: sin advertencia de datos",
            no_missing_data_warning,
            explanation_cases,
            COLORS["purple"],
        ),
        (
            "Explicación: sin conclusión auditable",
            no_conclusion,
            explanation_cases,
            COLORS["purple"],
        ),
    ]

    fig, (ax1, ax2) = plt.subplots(
        2,
        1,
        figsize=(7.2, 7.0),
        gridspec_kw={"height_ratios": [1.35, 1.0]},
    )
    if include_title:
        fig.suptitle(
            "Distribución de categorías de error y advertencias por etapa del piloto",
            y=0.995,
            fontsize=11,
            fontweight="bold",
            color=COLORS["black"],
        )

    def draw_panel(
        ax: plt.Axes,
        rows: list[tuple[str, int, int, str]],
        title: str,
    ) -> None:
        labels = [row[0] for row in rows][::-1]
        counts = [int(row[1]) for row in rows][::-1]
        denominators = [int(row[2]) for row in rows][::-1]
        colors = [row[3] for row in rows][::-1]
        proportions = [
            count / denominator if denominator > 0 else 0.0
            for count, denominator in zip(counts, denominators)
        ]
        y = np.arange(len(rows))
        ax.barh(
            y,
            proportions,
            color=colors,
            height=0.64,
            edgecolor="white",
            linewidth=0.5,
        )
        ax.set_yticks(y, labels)
        ax.set_xlim(0, 0.72)
        ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
        ax.set_xlabel("Proporción dentro de la etapa")
        ax.set_title(
            title,
            loc="left",
            fontsize=9,
            fontweight="bold",
            color=COLORS["black"],
        )
        ax.grid(axis="y", visible=False)
        for yi, count, denominator, proportion in zip(
            y,
            counts,
            denominators,
            proportions,
        ):
            ax.text(
                min(proportion + 0.012, 0.665),
                yi,
                f"{fmt_int(count)}/{fmt_int(denominator)} ({pct(proportion, 1)})",
                ha="left",
                va="center",
                fontsize=7.5,
                color=COLORS["black"],
            )

    draw_panel(ax1, main_rows, "Datos, corpus y recuperación")
    draw_panel(ax2, llm_rows, "Pruebas diagnósticas y explicación con LLM")

    note = (
        f"Cobertura histórica: {absent_history} casos con código ausente del banco.  |  "
        f"Corpus normativo: {fmt_int(conflicting_groups)} grupos código–nivel "
        "con descripciones conflictivas.  |  "
        "Validez externa: una clase, una aduana y un periodo.  |  "
        "Las categorías pueden superponerse y cada barra utiliza su propio denominador."
    )
    fig.text(
        0.01,
        0.005,
        note,
        ha="left",
        va="bottom",
        fontsize=7.2,
        color=COLORS["gray"],
        wrap=True,
    )
    fig.subplots_adjust(left=0.40, right=0.98, bottom=0.14, hspace=0.42)
    return fig


def main() -> int:
    args = parse_args()
    configure_style()
    root = args.repo_root.resolve()
    output_dir = (
        args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
    ).resolve()

    paths = {
        "splits_metadata": resolve_first(
            root,
            ["data/processed/data_aduanas_splits_clase87_v0.1_metadata.json"],
        ),
        "corpus_audit": resolve_first(
            root,
            ["outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.json"],
        ),
        "candidate_pool": resolve_first(
            root,
            [
                "outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/"
                "candidate_pool_metrics.json"
            ],
        ),
        "historical": resolve_first(
            root,
            [
                "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/"
                "historical_metrics.json"
            ],
        ),
        "rerank": resolve_first(
            root,
            [
                "outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/"
                "llm_rerank_metrics.json"
            ],
        ),
        "auditability": resolve_first(
            root,
            [
                "outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/"
                "audit_quality_metrics.json"
            ],
        ),
    }
    data = {name: load_json(path) for name, path in paths.items()}

    fig = build_figure(
        data["splits_metadata"],
        data["corpus_audit"],
        data["candidate_pool"],
        data["historical"],
        data["rerank"],
        data["auditability"],
        args.include_title,
    )
    generated = save_figure(fig, output_dir, args.formats, args.dpi)

    manifest = {
        "script_version": SCRIPT_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(root),
        "output_dir": str(output_dir),
        "formats": list(args.formats),
        "dpi": args.dpi,
        "inputs": {
            name: {"path": str(path), "sha256": sha256(path)}
            for name, path in paths.items()
        },
        "outputs": [str(path) for path in generated],
        "notes": [
            "La figura normaliza cada categoría por el denominador de su etapa.",
            "Las categorías no son mutuamente excluyentes.",
            "La revisión experta y la validez jurídica permanecen fuera del piloto.",
        ],
    }
    manifest_path = output_dir / "manifest_figura_10.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Figura 10 generada en: {output_dir}")
    for path in generated:
        print(f"- {path}")
    print(f"- manifiesto: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
