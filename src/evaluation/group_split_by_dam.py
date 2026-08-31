"""Generate deterministic Clase 87 DAM-grouped Aduanas split v0.2.

This script materializes the approved T5-safe-159 partition from an explicit
configuration. It does not search, optimize, or use model metrics.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import pandas as pd

DAM = "DECLARACION"
CODE = "NANDINA"
DESC = "DESCRIPCION DE MERCANCIAS CONCATENADA"
CASE_ID = "case_id"
ID_UNICO = "id_unico"
SPLIT = "split"
SOURCE_SPLIT = "source_split_v0_1"

DEFAULT_CONFIG = Path("src/configs/data_aduanas_split_clase87_v0.2.json")
DEFAULT_OUTPUT_DIR = Path("data/processed")
DEFAULT_AUDIT_DIR = Path("outputs/audits/data_aduanas_splits_clase87_v0.2")

SPLIT_OUTPUTS = {
    "historico": "data_aduanas_historico_clase87_v0.2.csv",
    "desarrollo": "data_aduanas_devset_clase87_v0.2.csv",
    "evaluacion": "data_aduanas_evalset_clase87_v0.2.csv",
}
CASE_PREFIX = {
    "historico": "DA-HIST-V02",
    "desarrollo": "DA-DEV-V02",
    "evaluacion": "DA-EVAL-V02",
}
SOURCE_NAMES = {
    "historico": "historico_v0.1",
    "desarrollo": "devset_v0.1",
    "evaluacion": "evalset_v0.1",
}
NEAR_THRESHOLDS = (0.90, 0.95, 0.98)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def frozen_sha256_matches(path: Path, expected: str) -> bool:
    """Accept the historical CRLF digest or its canonical Git LF representation."""
    content = path.read_bytes()
    canonical = content.replace(b"\r\n", b"\n")
    candidates = {
        hashlib.sha256(content).hexdigest(),
        hashlib.sha256(canonical).hexdigest(),
        hashlib.sha256(canonical.replace(b"\n", b"\r\n")).hexdigest(),
    }
    return expected in candidates


def artifact_key(path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root()).as_posix()
    except ValueError:
        return path.as_posix()


def clean_text(value: Any) -> str:
    text = "" if value is None else str(value).replace("\xa0", " ").strip()
    if text.casefold() in {"nan", "nat", "none"}:
        return ""
    return re.sub(r"\s+", " ", text)


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", clean_text(value))).strip().casefold()


def description_tokens(value: str) -> set[str]:
    return {tok for tok in re.findall(r"\w+", value, re.UNICODE) if len(tok) >= 3}


def jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    inter = left & right
    if not inter:
        return 0.0
    return len(inter) / len(left | right)


def read_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        cfg = json.load(fh)
    for split in SPLIT_OUTPUTS:
        if split not in cfg.get("dam_assignments", {}):
            raise ValueError(f"Missing DAM assignments for {split}")
    return cfg


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def verify_source_hashes(root: Path, cfg: dict[str, Any]) -> dict[str, str]:
    actual: dict[str, str] = {}
    for rel, expected in cfg["source_v0_1_sha256_locked"].items():
        path = root / rel
        digest = sha256_file(path)
        actual[rel] = digest
        if not frozen_sha256_matches(path, expected):
            raise RuntimeError(f"v0.1 hash changed for {rel}: {digest} != {expected}")
    return actual


def load_source_union(root: Path, cfg: dict[str, Any]) -> tuple[pd.DataFrame, list[str]]:
    frames = []
    source_cols: list[str] | None = None
    for split, rel in cfg["source_files"].items():
        if split == "metadata":
            continue
        frame = read_csv(root / rel)
        if source_cols is None:
            source_cols = list(frame.columns)
        elif list(frame.columns) != source_cols:
            raise RuntimeError(f"Source schema mismatch in {rel}")
        for col in [DAM, CODE, DESC, CASE_ID, ID_UNICO, SPLIT]:
            if col in frame.columns:
                frame[col] = frame[col].map(clean_text)
        frame[SOURCE_SPLIT] = SOURCE_NAMES[split]
        frames.append(frame)
    if not frames or source_cols is None:
        raise RuntimeError("No source CSV files loaded")
    df = pd.concat(frames, ignore_index=True)
    return df, source_cols


def split_dataframe(df: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, pd.DataFrame]:
    assignments = {k: set(v) for k, v in cfg["dam_assignments"].items()}
    assigned_dams = set().union(*assignments.values())
    observed_dams = set(df[DAM])
    missing = observed_dams - assigned_dams
    extra = assigned_dams - observed_dams
    if missing:
        raise RuntimeError(f"Unassigned observed DAM values: {sorted(missing)[:10]}")
    if extra:
        raise RuntimeError(f"Configured DAM values absent from sources: {sorted(extra)[:10]}")
    overlaps = _pairwise_overlaps(assignments)
    if any(overlaps.values()):
        raise RuntimeError(f"DAM assignment overlaps detected: {overlaps}")
    parts = {split: df[df[DAM].isin(dams)].copy() for split, dams in assignments.items()}
    return parts


def materialize_outputs(parts: dict[str, pd.DataFrame], source_cols: list[str]) -> dict[str, pd.DataFrame]:
    outputs = {}
    for split in SPLIT_OUTPUTS:
        out = parts[split].sort_values([DAM, "SERIE", ID_UNICO], kind="mergesort").reset_index(drop=True)
        out = out[source_cols].copy()
        out[SPLIT] = split
        out[CASE_ID] = [f"{CASE_PREFIX[split]}-{i:05d}" for i in range(1, len(out) + 1)]
        outputs[split] = out
    return outputs


def write_outputs(outputs: dict[str, pd.DataFrame], output_dir: Path, overwrite: bool) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rel_hashes = {}
    for split, filename in SPLIT_OUTPUTS.items():
        path = output_dir / filename
        if path.exists() and not overwrite:
            raise FileExistsError(f"Refusing to overwrite {path}; pass --overwrite")
        outputs[split].to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
        rel_hashes[artifact_key(path)] = sha256_file(path)
    return rel_hashes


def hhi(values: list[int]) -> tuple[float, float, float]:
    total = sum(values)
    if not total:
        return 0.0, 0.0, 0.0
    shares = [v / total for v in values]
    score = sum(s * s for s in shares)
    return max(shares) * 100, score, 1 / score if score else 0.0


def split_stats(outputs: dict[str, pd.DataFrame]) -> dict[str, dict[str, Any]]:
    stats = {}
    for split, df in outputs.items():
        dam_counts = [int(v) for v in df.groupby(DAM).size().tolist()]
        max_pct, hhi_score, effective = hhi(dam_counts)
        stats[split] = {
            "series": int(len(df)),
            "dam": int(df[DAM].nunique()),
            "codes": int(df[CODE].nunique()),
            "max_dam_pct": max_pct,
            "hhi": hhi_score,
            "effective_dam": effective,
        }
    return stats


def _pairwise_overlaps(groups: dict[str, set[str]]) -> dict[str, int]:
    names = sorted(groups)
    out = {}
    for idx, left in enumerate(names):
        for right in names[idx + 1 :]:
            out[f"{left}__{right}"] = len(groups[left] & groups[right])
    return out

def validation_summary(source: pd.DataFrame, outputs: dict[str, pd.DataFrame], cfg: dict[str, Any]) -> dict[str, Any]:
    all_out = pd.concat(outputs.values(), ignore_index=True)
    dams = {split: set(df[DAM]) for split, df in outputs.items()}
    ids = {split: set(df[ID_UNICO]) for split, df in outputs.items()}
    code_hist = set(outputs["historico"][CODE])
    eval_support = outputs["evaluacion"][CODE].isin(code_hist)
    approved = cfg["approved_counts"]
    sizes_match = {
        split: {
            "series": int(len(outputs[split])) == int(approved[split]["series"]),
            "dam": int(outputs[split][DAM].nunique()) == int(approved[split]["dam"]),
            "codes": int(outputs[split][CODE].nunique()) == int(approved[split]["codes"]),
        }
        for split in outputs
    }
    return {
        "total_source_rows": int(len(source)),
        "total_output_rows": int(len(all_out)),
        "full_assignment": int(len(source)) == int(len(all_out)) == int(all_out[ID_UNICO].nunique()),
        "source_unique_id_unico": int(source[ID_UNICO].nunique()),
        "output_unique_id_unico": int(all_out[ID_UNICO].nunique()),
        "dam_overlap": _pairwise_overlaps(dams),
        "id_overlap": _pairwise_overlaps(ids),
        "eval_cases_with_historical_support": int(eval_support.sum()),
        "eval_cases_without_historical_support": int((~eval_support).sum()),
        "eval_support_pct": float(eval_support.mean() * 100) if len(eval_support) else 0.0,
        "sizes_match_approved": sizes_match,
    }


def build_concentration(outputs: dict[str, pd.DataFrame]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    summary = {}
    for split, df in outputs.items():
        counts = df.groupby(DAM).size().sort_values(ascending=False)
        max_pct, hhi_score, effective = hhi([int(v) for v in counts.tolist()])
        summary[split] = {
            "series": int(len(df)),
            "dam": int(counts.size),
            "codes": int(df[CODE].nunique()),
            "max_dam_pct": max_pct,
            "hhi": hhi_score,
            "effective_dam": effective,
        }
        total = len(df)
        acc = 0
        for rank, (dam, n) in enumerate(counts.items(), 1):
            acc += int(n)
            rows.append({
                "split": split,
                "rank": rank,
                "DECLARACION": dam,
                "series": int(n),
                "pct_split": int(n) / total * 100 if total else 0,
                "cum_pct": acc / total * 100 if total else 0,
            })
    return rows, summary


def historical_support(outputs: dict[str, pd.DataFrame]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    hist = outputs["historico"]
    eval_df = outputs["evaluacion"]
    hist_series = hist.groupby(CODE).size().to_dict()
    hist_dams = hist.groupby(CODE)[DAM].nunique().to_dict()
    code_rows = []
    bucket_cases: Counter[str] = Counter()
    bucket_codes: Counter[str] = Counter()
    for code, eval_cases in eval_df.groupby(CODE).size().sort_values(ascending=False).items():
        dam_count = int(hist_dams.get(code, 0))
        bucket = support_bucket(dam_count)
        bucket_cases[bucket] += int(eval_cases)
        bucket_codes[bucket] += 1
        code_rows.append({
            "NANDINA": code,
            "eval_cases": int(eval_cases),
            "support_count_series": int(hist_series.get(code, 0)),
            "support_count_dams": dam_count,
            "support_bucket": bucket,
            "has_historical_support": dam_count > 0,
        })
    row_support = eval_df[[CASE_ID, ID_UNICO, DAM, CODE, DESC]].copy()
    row_support["support_count_series"] = row_support[CODE].map(lambda c: int(hist_series.get(c, 0)))
    row_support["support_count_dams"] = row_support[CODE].map(lambda c: int(hist_dams.get(c, 0)))
    row_support["support_bucket"] = row_support["support_count_dams"].map(support_bucket)
    row_support["has_historical_support"] = row_support["support_count_dams"] > 0
    summary = {
        "eval_total_cases": int(len(eval_df)),
        "eval_cases_with_historical_support": int(row_support["has_historical_support"].sum()),
        "eval_cases_without_historical_support": int((~row_support["has_historical_support"]).sum()),
        "eval_total_codes": int(eval_df[CODE].nunique()),
        "eval_codes_with_historical_support": int(sum(1 for r in code_rows if r["has_historical_support"])),
        "eval_codes_without_historical_support": int(sum(1 for r in code_rows if not r["has_historical_support"])),
        "bucket_cases": dict(bucket_cases),
        "bucket_codes": dict(bucket_codes),
    }
    return code_rows, row_support.to_dict("records"), summary


def support_bucket(dam_count: int) -> str:
    if dam_count <= 0:
        return "Z. sin soporte historico"
    if dam_count == 1:
        return "A. 1 DAM historica"
    if dam_count == 2:
        return "B. 2 DAM historicas"
    if dam_count <= 4:
        return "C. 3-4 DAM historicas"
    return "D. 5+ DAM historicas"


def exact_duplicate_audit(left: pd.DataFrame, right: pd.DataFrame, label: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    index: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    left_rows = left[[CASE_ID, ID_UNICO, DAM, CODE, DESC]].copy()
    left_rows["desc_norm"] = left_rows[DESC].map(normalize_text)
    right_rows = right[[CASE_ID, ID_UNICO, DAM, CODE, DESC]].copy()
    right_rows["desc_norm"] = right_rows[DESC].map(normalize_text)
    for row in left_rows.to_dict("records"):
        if row["desc_norm"]:
            index[row["desc_norm"]].append(row)
    details = []
    affected_rows = same_rows = diff_rows = same_dam_rows = diff_dam_rows = 0
    same_pairs = diff_pairs = 0
    for right_row in right_rows.to_dict("records"):
        matches = index.get(right_row["desc_norm"], []) if right_row["desc_norm"] else []
        if not matches:
            continue
        row_same = row_diff = row_same_dam = row_diff_dam = False
        for left_row in matches:
            same_code = left_row[CODE] == right_row[CODE]
            same_dam = left_row[DAM] == right_row[DAM]
            same_pairs += int(same_code)
            diff_pairs += int(not same_code)
            row_same = row_same or same_code
            row_diff = row_diff or not same_code
            row_same_dam = row_same_dam or same_dam
            row_diff_dam = row_diff_dam or not same_dam
            details.append({
                "comparison": label,
                "left_case_id": left_row[CASE_ID],
                "right_case_id": right_row[CASE_ID],
                "left_id_unico": left_row[ID_UNICO],
                "right_id_unico": right_row[ID_UNICO],
                "left_DECLARACION": left_row[DAM],
                "right_DECLARACION": right_row[DAM],
                "left_NANDINA": left_row[CODE],
                "right_NANDINA": right_row[CODE],
                "same_nandina": same_code,
                "same_dam": same_dam,
                "desc_norm_sha256": hashlib.sha256(right_row["desc_norm"].encode("utf-8")).hexdigest(),
            })
        affected_rows += 1
        same_rows += int(row_same)
        diff_rows += int(row_diff)
        same_dam_rows += int(row_same_dam)
        diff_dam_rows += int(row_diff_dam)
    summary = {
        "comparison": label,
        "method": "exact_normalized_description",
        "right_rows": int(len(right)),
        "affected_rows": affected_rows,
        "affected_pct": affected_rows / len(right) * 100 if len(right) else 0.0,
        "same_nandina_rows": same_rows,
        "different_nandina_rows": diff_rows,
        "same_dam_rows": same_dam_rows,
        "different_dam_rows": diff_dam_rows,
        "same_nandina_pairs": same_pairs,
        "different_nandina_pairs": diff_pairs,
    }
    return summary, details

def near_duplicate_audit(left: pd.DataFrame, right: pd.DataFrame, label: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    left_rows = left[[CASE_ID, ID_UNICO, DAM, CODE, DESC]].copy()
    left_rows["desc_norm"] = left_rows[DESC].map(normalize_text)
    right_rows = right[[CASE_ID, ID_UNICO, DAM, CODE, DESC]].copy()
    right_rows["desc_norm"] = right_rows[DESC].map(normalize_text)
    left_records = left_rows.to_dict("records")
    right_records = right_rows.to_dict("records")
    left_tokens = [description_tokens(row["desc_norm"]) for row in left_records]
    token_df: Counter[str] = Counter()
    for tokens in left_tokens:
        token_df.update(tokens)
    rare_limit = max(20, int(len(left_records) * 0.25))
    rare_tokens = {token for token, freq in token_df.items() if freq <= rare_limit}
    inverted: defaultdict[str, set[int]] = defaultdict(set)
    for idx, tokens in enumerate(left_tokens):
        for token in tokens & rare_tokens:
            inverted[token].add(idx)
    candidate_by_right: list[tuple[dict[str, Any], set[str], set[int]]] = []
    for row in right_records:
        tokens = description_tokens(row["desc_norm"])
        candidates: set[int] = set()
        for token in tokens & rare_tokens:
            candidates.update(inverted.get(token, set()))
        candidate_by_right.append((row, tokens, candidates))
    summary_rows = []
    detail_rows = []
    for threshold in NEAR_THRESHOLDS:
        affected_rows = same_rows = diff_rows = 0
        pairs = same_pairs = diff_pairs = 0
        for right_row, right_tokens, candidates in candidate_by_right:
            row_matches = []
            row_same = row_diff = False
            for left_idx in sorted(candidates):
                score = jaccard(left_tokens[left_idx], right_tokens)
                if score < threshold:
                    continue
                left_row = left_records[left_idx]
                same_code = left_row[CODE] == right_row[CODE]
                row_same = row_same or same_code
                row_diff = row_diff or not same_code
                pairs += 1
                same_pairs += int(same_code)
                diff_pairs += int(not same_code)
                row_matches.append({
                    "comparison": label,
                    "threshold": threshold,
                    "left_case_id": left_row[CASE_ID],
                    "right_case_id": right_row[CASE_ID],
                    "left_id_unico": left_row[ID_UNICO],
                    "right_id_unico": right_row[ID_UNICO],
                    "left_DECLARACION": left_row[DAM],
                    "right_DECLARACION": right_row[DAM],
                    "left_NANDINA": left_row[CODE],
                    "right_NANDINA": right_row[CODE],
                    "same_nandina": same_code,
                    "jaccard": score,
                    "method": "token_jaccard_rare_block",
                })
            if row_matches:
                affected_rows += 1
                same_rows += int(row_same)
                diff_rows += int(row_diff)
                detail_rows.extend(row_matches)
        summary_rows.append({
            "comparison": label,
            "threshold": threshold,
            "right_rows": int(len(right)),
            "affected_rows": affected_rows,
            "affected_pct": affected_rows / len(right) * 100 if len(right) else 0.0,
            "same_nandina_rows": same_rows,
            "different_nandina_rows": diff_rows,
            "pairs": pairs,
            "same_nandina_pairs": same_pairs,
            "different_nandina_pairs": diff_pairs,
            "method": "token_jaccard_rare_block",
            "rare_token_max_df": rare_limit,
        })
    return summary_rows, detail_rows


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    fields: list[str] = []
    for row in rows:
        for key, value in row.items():
            if key not in fields and not isinstance(value, (dict, list, tuple, set)):
                fields.append(key)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        if not fields:
            return
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_audits(outputs: dict[str, pd.DataFrame], audit_dir: Path, overwrite: bool) -> tuple[dict[str, Any], dict[str, str]]:
    audit_dir.mkdir(parents=True, exist_ok=True)
    for old in audit_dir.glob("*_v0.2.*"):
        if not overwrite:
            raise FileExistsError(f"Refusing to overwrite {old}; pass --overwrite")
    concentration_rows, concentration_summary = build_concentration(outputs)
    support_code_rows, support_eval_rows, support_summary = historical_support(outputs)
    exact_summary_rows = []
    exact_details = []
    for left_name, right_name in [("historico", "evaluacion"), ("historico", "desarrollo"), ("desarrollo", "evaluacion")]:
        summary, details = exact_duplicate_audit(outputs[left_name], outputs[right_name], f"{left_name}-{right_name}")
        exact_summary_rows.append(summary)
        exact_details.extend(details)
    near_summary, near_details = near_duplicate_audit(outputs["historico"], outputs["evaluacion"], "historico-evaluacion")
    independence = {
        "dam_overlap": _pairwise_overlaps({k: set(v[DAM]) for k, v in outputs.items()}),
        "id_unico_overlap": _pairwise_overlaps({k: set(v[ID_UNICO]) for k, v in outputs.items()}),
        "zero_dam_overlap": True,
        "zero_id_overlap": True,
    }
    independence["zero_dam_overlap"] = all(value == 0 for value in independence["dam_overlap"].values())
    independence["zero_id_overlap"] = all(value == 0 for value in independence["id_unico_overlap"].values())
    audit_summary = {
        "independence": independence,
        "concentration": concentration_summary,
        "historical_support": support_summary,
        "exact_duplicates_cross_split": exact_summary_rows,
        "near_duplicates_hist_eval": near_summary,
    }
    artifacts = {
        "independence_audit_v0.2.json": independence,
        "concentration_summary_v0.2.json": concentration_summary,
        "historical_support_summary_v0.2.json": support_summary,
        "audit_summary_v0.2.json": audit_summary,
    }
    for name, payload in artifacts.items():
        write_json(audit_dir / name, payload)
    csv_artifacts = {
        "concentration_by_dam_v0.2.csv": concentration_rows,
        "historical_support_by_code_v0.2.csv": support_code_rows,
        "historical_support_by_eval_row_v0.2.csv": support_eval_rows,
        "exact_duplicates_cross_split_summary_v0.2.csv": exact_summary_rows,
        "exact_duplicates_cross_split_details_v0.2.csv": exact_details,
        "near_duplicates_hist_eval_summary_v0.2.csv": near_summary,
        "near_duplicates_hist_eval_details_v0.2.csv": near_details,
    }
    for name, rows in csv_artifacts.items():
        write_csv_rows(audit_dir / name, rows)
    write_markdown_audit_summary(audit_dir / "audit_summary_v0.2.md", audit_summary)
    hashes = {artifact_key(path): sha256_file(path) for path in sorted(audit_dir.glob("*_v0.2.*"))}
    return audit_summary, hashes


def write_markdown_audit_summary(path: Path, audit_summary: dict[str, Any]) -> None:
    exact_he = next(row for row in audit_summary["exact_duplicates_cross_split"] if row["comparison"] == "historico-evaluacion")
    near_rows = audit_summary["near_duplicates_hist_eval"]
    support = audit_summary["historical_support"]
    eval_conc = audit_summary["concentration"]["evaluacion"]
    lines = [
        "# Auditoria split Aduanas Clase 87 v0.2",
        "",
        "Split aprobado: T5-safe-159. Las particiones son independientes por DAM y no fueron seleccionadas por metricas de modelo.",
        "",
        "## Resultado de compuerta",
        "",
        "- DAM compartidas entre particiones: 0.",
        "- id_unico compartidos entre particiones: 0.",
        f"- Casos de evaluacion con soporte historico: {support['eval_cases_with_historical_support']} de {support['eval_total_cases']}.",
        f"- Concentracion maxima DAM en evaluacion: {eval_conc['max_dam_pct']:.6f}%.",
        "",
        "## Duplicados",
        "",
        f"- Duplicados exactos historico-evaluacion: {exact_he['affected_rows']} filas de evaluacion afectadas; {exact_he['different_nandina_rows']} con NANDINA distinta.",
        "- Near-duplicates historico-evaluacion:",
    ]
    for row in near_rows:
        lines.append(f"  - umbral {row['threshold']:.2f}: {row['affected_rows']} filas afectadas, {row['pairs']} pares.")
    lines.extend([
        "",
        "## Soporte historico por bucket",
        "",
    ])
    for bucket, cases in support["bucket_cases"].items():
        codes = support["bucket_codes"].get(bucket, 0)
        lines.append(f"- {bucket}: {codes} codigos / {cases} casos.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_metadata(
    cfg: dict[str, Any],
    cfg_path: Path,
    source_hashes: dict[str, str],
    output_hashes: dict[str, str],
    audit_hashes: dict[str, str],
    validation: dict[str, Any],
    stats: dict[str, Any],
    audits: dict[str, Any],
) -> dict[str, Any]:
    try:
        config_file = cfg_path.relative_to(repo_root()).as_posix()
    except ValueError:
        config_file = cfg_path.as_posix()
    return {
        "dataset_name": "data_aduanas_clase87",
        "version": cfg["version"],
        "strategy": cfg["strategy"],
        "seed": cfg["seed"],
        "grouping_field": cfg["grouping_field"],
        "analysis_unit": cfg["analysis_unit"],
        "eligible_class": cfg["eligible_class"],
        "selection_policy": "explicit_dam_assignment_no_heuristic_search_no_model_metrics",
        "config_file": config_file,
        "config_sha256": sha256_file(cfg_path),
        "source_v0_1_sha256_verified": source_hashes,
        "output_sha256": output_hashes,
        "audit_sha256": audit_hashes,
        "approved_counts": cfg["approved_counts"],
        "split_stats": stats,
        "validation": validation,
        "audits": audits,
        "notes": cfg.get("notes", []),
    }

def validate_gate(cfg: dict[str, Any], validation: dict[str, Any], stats: dict[str, Any], audits: dict[str, Any]) -> None:
    if not validation["full_assignment"]:
        raise RuntimeError("Full assignment validation failed")
    if any(value != 0 for value in validation["dam_overlap"].values()):
        raise RuntimeError("DAM overlap validation failed")
    if any(value != 0 for value in validation["id_overlap"].values()):
        raise RuntimeError("id_unico overlap validation failed")
    if validation["eval_cases_without_historical_support"] != 0:
        raise RuntimeError("Evaluation historical support validation failed")
    if stats["evaluacion"]["max_dam_pct"] > cfg["requirements"]["eval_max_dam_concentration"] * 100:
        raise RuntimeError("Evaluation DAM concentration exceeds configured maximum")
    for split, checks in validation["sizes_match_approved"].items():
        if not all(checks.values()):
            raise RuntimeError(f"Approved-count validation failed for {split}: {checks}")
    expected = cfg.get("expected_audit_values", {})
    exact_he = next(row for row in audits["exact_duplicates_cross_split"] if row["comparison"] == "historico-evaluacion")
    near_095 = next(row for row in audits["near_duplicates_hist_eval"] if abs(row["threshold"] - 0.95) < 1e-9)
    if exact_he["affected_rows"] != expected.get("exact_duplicates_hist_eval_affected_rows"):
        raise RuntimeError("Unexpected historico-evaluacion exact duplicate count")
    if near_095["affected_rows"] != expected.get("near_duplicates_hist_eval_rows_at_0_95"):
        raise RuntimeError("Unexpected historico-evaluacion near duplicate count at 0.95")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--overwrite", action="store_true", help="Overwrite v0.2 outputs if present")
    return parser.parse_args()


def resolve_path(root: Path, path: Path) -> Path:
    return path if path.is_absolute() else root / path


def main() -> None:
    root = repo_root()
    args = parse_args()
    cfg_path = resolve_path(root, args.config)
    output_dir = resolve_path(root, args.output_dir)
    audit_dir = resolve_path(root, args.audit_dir)
    cfg = read_config(cfg_path)
    source_hashes = verify_source_hashes(root, cfg)
    source, source_cols = load_source_union(root, cfg)
    for required in [DAM, CODE, DESC, CASE_ID, ID_UNICO, SPLIT]:
        if required not in source.columns:
            raise RuntimeError(f"Required column missing from source union: {required}")
    parts = split_dataframe(source, cfg)
    outputs = materialize_outputs(parts, source_cols)
    output_hashes = write_outputs(outputs, output_dir, args.overwrite)
    audits, audit_hashes = write_audits(outputs, audit_dir, args.overwrite)
    stats = split_stats(outputs)
    validation = validation_summary(source, outputs, cfg)
    validate_gate(cfg, validation, stats, audits)
    metadata = build_metadata(cfg, cfg_path, source_hashes, output_hashes, audit_hashes, validation, stats, audits)
    metadata_path = output_dir / "data_aduanas_splits_clase87_v0.2_metadata.json"
    if metadata_path.exists() and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite {metadata_path}; pass --overwrite")
    write_json(metadata_path, metadata)
    metadata_hash = sha256_file(metadata_path)
    print(json.dumps({
        "status": "ok",
        "strategy": cfg["strategy"],
        "outputs": output_hashes,
        "metadata": {str(metadata_path): metadata_hash},
        "audits": audit_hashes,
        "validation": validation,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()



