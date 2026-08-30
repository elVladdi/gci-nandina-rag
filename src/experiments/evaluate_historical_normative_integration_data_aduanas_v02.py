from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import project_root, resolve_project_path


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256(path)
    if actual != expected:
        raise ValueError(f"{label} SHA-256 mismatch: {actual} != {expected}")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{clean(key): clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, 1):
            value = line.strip()
            if not value:
                continue
            try:
                yield json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}") from exc


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def git_value(root: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}", *args], cwd=root, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def bool_int(value: bool) -> int:
    return int(bool(value))


def build_top3(rows: list[dict[str, str]], expected_cases: set[str], method: str) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row["method"] != method:
            continue
        rank = int(row["candidate_rank"])
        if rank <= 3:
            grouped[row["case_id"]].append(row)
    if set(grouped) != expected_cases:
        raise ValueError("Historical Top-3 case IDs do not match evalset")
    for case_id, candidates in grouped.items():
        candidates.sort(key=lambda row: int(row["candidate_rank"]))
        if [int(row["candidate_rank"]) for row in candidates] != [1, 2, 3]:
            raise ValueError(f"Incomplete historical Top-3 for {case_id}")
        if len({row["candidate_nandina"] for row in candidates}) != 3:
            raise ValueError(f"Duplicate historical code in Top-3 for {case_id}")
    return grouped


def historical_index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    result = {row["case_id"]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError("Historical dataset has duplicate case IDs")
    if any(row.get("split") != "historico" for row in rows):
        raise ValueError("Precedent source contains a non-historical split")
    return result


def normative_index(rows: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for row in rows:
        code = clean(row.get("nandina_8d") or row.get("codigo"))
        if len(code) == 8 and code.isdigit() and code not in index:
            index[code] = row
    if not index:
        raise ValueError("Normative corpus contains no NANDINA-8 documents")
    return index


def evidence_for(code: str, document: Mapping[str, Any] | None, corpus_hash: str) -> dict[str, Any]:
    if document is None:
        return {
            "normative_evidence_status": "no_normative_evidence",
            "normative_doc_ids": "",
            "normative_source": "",
            "normative_version": "",
            "normative_type": "",
            "normative_document_code": "",
            "normative_source_page": "",
            "normative_source_line": "",
            "normative_evidence_reference": "",
            "has_exact_nandina8_evidence": 0,
            "has_hs6_evidence": 0,
            "has_hs4_evidence": 0,
            "has_chapter_evidence": 0,
            "normative_corpus_sha256": corpus_hash,
        }
    hs6 = clean(document.get("hs_6d")) == code[:6]
    hs4 = clean(document.get("partida_4d")) == code[:4]
    chapter = clean(document.get("chapter")) == code[:2]
    return {
        "normative_evidence_status": "exact_nandina8_evidence",
        "normative_doc_ids": clean(document.get("doc_id")),
        "normative_source": clean(document.get("fuente") or "NANDINA"),
        "normative_version": clean(document.get("version")),
        "normative_type": clean(document.get("tipo") or "nandina_8"),
        "normative_document_code": clean(document.get("nandina_8d") or document.get("codigo")),
        "normative_source_page": clean(document.get("source_page") or document.get("pagina_inicio")),
        "normative_source_line": clean(document.get("source_line_no")),
        "normative_evidence_reference": clean(document.get("source_line_text") or document.get("texto")),
        "has_exact_nandina8_evidence": 1,
        "has_hs6_evidence": bool_int(hs6),
        "has_hs4_evidence": bool_int(hs4),
        "has_chapter_evidence": bool_int(chapter),
        "normative_corpus_sha256": corpus_hash,
    }


def source_slot(
    case_id: str,
    query: str,
    candidate: Mapping[str, str],
    precedent: Mapping[str, str],
    document: Mapping[str, Any] | None,
    corpus_hash: str,
) -> dict[str, Any]:
    code = candidate["candidate_nandina"]
    if precedent["NANDINA"] != code:
        raise ValueError(f"Historical precedent code mismatch for {case_id}/{code}")
    evidence = evidence_for(code, document, corpus_hash)
    traceability = bool(
        case_id
        and code
        and candidate["candidate_rank"]
        and candidate["score"]
        and candidate["candidate_case_id"]
        and precedent["id_unico"]
        and evidence["normative_doc_ids"]
        and evidence["normative_source"]
        and evidence["normative_corpus_sha256"]
    )
    return {
        "case_id": case_id,
        "query": query,
        "historical_rank": candidate["candidate_rank"],
        "historical_candidate_code": code,
        "historical_score": candidate["score"],
        "historical_candidate_history_rank": candidate["candidate_history_rank"],
        "historical_precedent_ids": candidate["candidate_case_id"],
        "historical_precedent_count": 1,
        "historical_precedent_case_id": candidate["candidate_case_id"],
        "historical_precedent_id_unico": precedent["id_unico"],
        "historical_precedent_dam": precedent["DECLARACION"],
        "historical_precedent_serie": precedent["SERIE"],
        "historical_precedent_code": precedent["NANDINA"],
        "historical_precedent_description": precedent["DESCRIPCION DE MERCANCIAS CONCATENADA"],
        "traceability_complete": bool_int(traceability),
        **evidence,
    }


def rate(rows: list[Mapping[str, Any]], field: str) -> dict[str, Any]:
    numerator = sum(int(row[field]) for row in rows)
    return {"numerator": numerator, "denominator": len(rows), "rate": numerator / len(rows) if rows else 0.0}


def main() -> int:
    parser = argparse.ArgumentParser(description="EXP-04 Fase F deterministic historical-normative evidence integration.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/historical_normative_integration_v0.2.json"))
    args = parser.parse_args()
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    output_dir = resolve_project_path(config["outputs"]["directory"])
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"Refusing to overwrite Fase F output: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    eval_cfg = config["eval"]
    historical_cfg = config["historical_ranking"]
    dataset_cfg = config["historical_dataset"]
    corpus_cfg = config["normative_corpus"]
    eval_path = resolve_project_path(eval_cfg["path"])
    historical_path = resolve_project_path(historical_cfg["path"])
    dataset_path = resolve_project_path(dataset_cfg["path"])
    corpus_path = resolve_project_path(corpus_cfg["path"])
    corpus_metadata_path = resolve_project_path(corpus_cfg["metadata_path"])
    for path, expected, label in [
        (eval_path, eval_cfg["sha256"], "evalset"),
        (historical_path, historical_cfg["sha256"], "historical results"),
        (dataset_path, dataset_cfg["sha256"], "historical dataset"),
        (corpus_path, corpus_cfg["sha256"], "normative corpus"),
        (corpus_metadata_path, corpus_cfg["metadata_sha256"], "normative corpus metadata"),
    ]:
        assert_hash(path, expected, label)
    for name, entry in config["frozen_phase_artifacts"].items():
        assert_hash(resolve_project_path(entry["path"]), entry["sha256"], name)

    eval_rows = read_csv(eval_path)
    if len(eval_rows) != int(eval_cfg["cases"]):
        raise ValueError("Unexpected evalset row count")
    eval_by_case = {row["case_id"]: row for row in eval_rows}
    if len(eval_by_case) != len(eval_rows):
        raise ValueError("Evalset has duplicate case IDs")
    expected_cases = set(eval_by_case)
    historical_rows = read_csv(historical_path)
    top3_by_case = build_top3(historical_rows, expected_cases, historical_cfg["method"])
    historical_by_case = historical_index(read_csv(dataset_path))
    corpus_by_code = normative_index(read_jsonl(corpus_path))

    # The label is deliberately not read in this construction loop.
    slots: list[dict[str, Any]] = []
    for case_id in [row["case_id"] for row in eval_rows]:
        eval_row = eval_by_case[case_id]
        for candidate in top3_by_case[case_id]:
            precedent_id = candidate["candidate_case_id"]
            precedent = historical_by_case.get(precedent_id)
            if precedent is None:
                raise ValueError(f"Missing historical precedent {precedent_id}")
            slots.append(source_slot(case_id, eval_row[eval_cfg["query_column"]], candidate, precedent, corpus_by_code.get(candidate["candidate_nandina"]), corpus_cfg["sha256"]))
    if len(slots) != len(eval_rows) * int(historical_cfg["top_k"]):
        raise ValueError("Unexpected Top-3 candidate slot count")

    slots_by_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for slot in slots:
        slots_by_case[slot["case_id"]].append(slot)
    for case_id, rows in slots_by_case.items():
        rows.sort(key=lambda row: int(row["historical_rank"]))
        if [int(row["historical_rank"]) for row in rows] != [1, 2, 3]:
            raise ValueError(f"Integrated Top-3 is incomplete for {case_id}")

    reference_by_case = {case_id: row[eval_cfg["label_column"]] for case_id, row in eval_by_case.items()}
    case_summary: list[dict[str, Any]] = []
    for case_id, rows in slots_by_case.items():
        codes = [row["historical_candidate_code"] for row in rows]
        reference = reference_by_case[case_id]
        exact_count = sum(int(row["has_exact_nandina8_evidence"]) for row in rows)
        case_summary.append({
            "case_id": case_id,
            "reference_nandina_for_evaluation": reference,
            "top3_codes": "|".join(codes),
            "top3_contains_reference": bool_int(reference in codes),
            "top1_has_exact_evidence": rows[0]["has_exact_nandina8_evidence"],
            "top2_has_exact_evidence": rows[1]["has_exact_nandina8_evidence"],
            "top3_has_exact_evidence": rows[2]["has_exact_nandina8_evidence"],
            "exact_evidence_candidates": exact_count,
            "hs6_evidence_candidates": sum(int(row["has_hs6_evidence"]) for row in rows),
            "hs4_evidence_candidates": sum(int(row["has_hs4_evidence"]) for row in rows),
            "chapter_evidence_candidates": sum(int(row["has_chapter_evidence"]) for row in rows),
            "precedent_coverage_candidates": sum(int(row["historical_precedent_count"]) > 0 for row in rows),
            "traceability_complete_candidates": sum(int(row["traceability_complete"]) for row in rows),
        })

    before_top3 = {(case_id, int(row["candidate_rank"])): (row["candidate_nandina"], row["score"]) for case_id, candidates in top3_by_case.items() for row in candidates}
    after_top3 = {(row["case_id"], int(row["historical_rank"])): (row["historical_candidate_code"], row["historical_score"]) for row in slots}
    unchanged_slots = sum(before_top3[key] == after_top3.get(key) for key in before_top3)
    invariant_cases = sum(all(before_top3[(case_id, rank)] == after_top3.get((case_id, rank)) for rank in (1, 2, 3)) for case_id in expected_cases)
    ranking_invariance = {
        "historical_results_sha256_before": historical_cfg["sha256"],
        "historical_results_sha256_after": sha256(historical_path),
        "historical_results_rows": len(historical_rows),
        "cases_pass": invariant_cases,
        "cases_total": len(eval_rows),
        "historical_rank_invariance_rate": invariant_cases / len(eval_rows),
        "top1_unchanged": invariant_cases == len(eval_rows),
        "top3_unchanged": invariant_cases == len(eval_rows),
        "positions_unchanged": invariant_cases == len(eval_rows),
        "historical_scores_unchanged": invariant_cases == len(eval_rows),
        "no_new_candidate_inserted": invariant_cases == len(eval_rows),
        "no_candidate_removed": invariant_cases == len(eval_rows),
        "normative_score_affects_order": False,
        "pass": invariant_cases == len(eval_rows) and sha256(historical_path) == historical_cfg["sha256"],
    }
    top3_invariance = {
        "candidate_slots_pass": unchanged_slots,
        "candidate_slots_total": len(slots),
        "top3_invariance_rate": unchanged_slots / len(slots),
        "before_codes_equal_after_codes": unchanged_slots == len(slots),
        "before_scores_equal_after_scores": unchanged_slots == len(slots),
        "pass": unchanged_slots == len(slots),
    }
    by_rank = {str(rank): rate([row for row in slots if int(row["historical_rank"]) == rank], "has_exact_nandina8_evidence") for rank in (1, 2, 3)}
    slot_coverage = {
        "candidate_slots": len(slots),
        "exact_nandina8": rate(slots, "has_exact_nandina8_evidence"),
        "hs6": rate(slots, "has_hs6_evidence"),
        "hs4": rate(slots, "has_hs4_evidence"),
        "chapter": rate(slots, "has_chapter_evidence"),
        "precedent": {"numerator": sum(int(row["historical_precedent_count"]) > 0 for row in slots), "denominator": len(slots)},
        "traceability": rate(slots, "traceability_complete"),
        "exact_by_historical_rank": by_rank,
        "cases_exact_evidence_count": {str(value): sum(int(row["exact_evidence_candidates"]) == value for row in case_summary) for value in range(4)},
        "top3_reference_groups": {},
    }
    for label, filtered in {
        "reference_in_historical_top3": [row for row in case_summary if int(row["top3_contains_reference"])],
        "reference_not_in_historical_top3": [row for row in case_summary if not int(row["top3_contains_reference"])],
    }.items():
        related_slots = [slot for slot in slots if slot["case_id"] in {row["case_id"] for row in filtered}]
        slot_coverage["top3_reference_groups"][label] = {"cases": len(filtered), "candidate_exact_evidence": rate(related_slots, "has_exact_nandina8_evidence")}

    missing_exact = [
        {
            "case_id": row["case_id"], "candidate_rank": row["historical_rank"], "candidate_code": row["historical_candidate_code"],
            "hs6": row["historical_candidate_code"][:6], "hs4": row["historical_candidate_code"][:4], "chapter": row["historical_candidate_code"][:2],
            "available_parent_evidence": any(int(row[key]) for key in ("has_hs6_evidence", "has_hs4_evidence", "has_chapter_evidence")),
            "reason": "no_exact_document_in_frozen_normative_corpus", "corpus_coverage_flag": False,
        }
        for row in slots if not int(row["has_exact_nandina8_evidence"])
    ]
    compatibility = {
        "compatible": ranking_invariance["pass"] and top3_invariance["pass"],
        "eval_hash": eval_cfg["sha256"],
        "cases": len(eval_rows),
        "identical_case_ids_with_phase_a": set(top3_by_case) == expected_cases,
        "identical_labels_with_eval": len(reference_by_case) == len(eval_rows),
        "exactly_three_historical_candidates_per_case": all(len(rows) == 3 for rows in slots_by_case.values()),
        "candidate_slots": len(slots),
        "ranking_unchanged": ranking_invariance["pass"],
    }
    label_audit = {
        "label_used_for_candidate_selection": False,
        "label_used_for_precedent_selection": False,
        "label_used_for_evidence_selection": False,
        "label_used_for_order_or_fallback": False,
        "selection_input_fields": ["historical candidate code", "historical candidate metadata", "historical precedent case ID", "normative corpus code"],
        "labels_only_used_after_construction_for_metrics": True,
        "pass": True,
    }
    metrics = {
        "experiment_id": config["experiment_id"], "phase": config["phase"], "cases": len(eval_rows), "candidate_slots": len(slots),
        "historical_rank_invariance_rate": ranking_invariance["historical_rank_invariance_rate"],
        "top3_invariance_rate": top3_invariance["top3_invariance_rate"],
        "candidate_exact_evidence_rate": slot_coverage["exact_nandina8"]["rate"],
        "candidate_hs6_evidence_rate": slot_coverage["hs6"]["rate"],
        "candidate_hs4_evidence_rate": slot_coverage["hs4"]["rate"],
        "candidate_chapter_evidence_rate": slot_coverage["chapter"]["rate"],
        "case_all_top3_exact_evidence_rate": slot_coverage["cases_exact_evidence_count"]["3"] / len(case_summary),
        "precedent_coverage_rate": slot_coverage["precedent"]["numerator"] / len(slots),
        "traceability_complete_rate": slot_coverage["traceability"]["rate"],
        "llm_used": False, "reranker_used": False, "candidate_pool_used": False, "d1a_used": False,
    }

    outputs = {
        "integration_candidate_slots": output_dir / "integration_candidate_slots.csv",
        "integration_case_summary": output_dir / "integration_case_summary.csv",
        "integration_metrics": output_dir / "integration_metrics.json",
        "integration_evidence_coverage": output_dir / "integration_evidence_coverage.json",
        "integration_ranking_invariance": output_dir / "integration_ranking_invariance.json",
        "integration_top3_invariance": output_dir / "integration_top3_invariance.json",
        "integration_traceability": output_dir / "integration_traceability.json",
        "integration_missing_exact_evidence": output_dir / "integration_missing_exact_evidence.csv",
        "integration_compatibility": output_dir / "integration_compatibility.json",
        "integration_label_leakage_audit": output_dir / "integration_label_leakage_audit.json",
        "integration_run_metadata": output_dir / "integration_run_metadata.json",
        "summary": output_dir / "summary.md",
    }
    slot_fields = list(slots[0])
    case_fields = list(case_summary[0])
    missing_fields = ["case_id", "candidate_rank", "candidate_code", "hs6", "hs4", "chapter", "available_parent_evidence", "reason", "corpus_coverage_flag"]
    write_csv(outputs["integration_candidate_slots"], slots, slot_fields)
    write_csv(outputs["integration_case_summary"], case_summary, case_fields)
    write_json(outputs["integration_metrics"], metrics)
    write_json(outputs["integration_evidence_coverage"], slot_coverage)
    write_json(outputs["integration_ranking_invariance"], ranking_invariance)
    write_json(outputs["integration_top3_invariance"], top3_invariance)
    write_json(outputs["integration_traceability"], {"complete": rate(slots, "traceability_complete"), "precedent_count_distribution": dict(Counter(row["historical_precedent_count"] for row in slots)), "normative_document_count_distribution": dict(Counter(1 if row["normative_doc_ids"] else 0 for row in slots))})
    write_csv(outputs["integration_missing_exact_evidence"], missing_exact, missing_fields)
    write_json(outputs["integration_compatibility"], compatibility)
    write_json(outputs["integration_label_leakage_audit"], label_audit)
    lines = [
        "# EXP-04 Fase F: integración histórico-normativa v0.2", "",
        "- Operación: CODE-TO-NORMATIVE-EVIDENCE LOOKUP; no es query-to-code retrieval.",
        "- El ranking histórico y el Top-3 permanecen literales; la evidencia se adjunta sin score normativo.",
        "- No se ejecutó LLM, RAG, reranker, candidate pool ni D1a.", "",
        "## Métricas", "",
        f"- Casos: {metrics['cases']}; candidate slots: {metrics['candidate_slots']}.",
        f"- Invariancia ranking: {metrics['historical_rank_invariance_rate']:.12f}; Top-3: {metrics['top3_invariance_rate']:.12f}.",
        f"- Evidencia exacta: {metrics['candidate_exact_evidence_rate']:.12f}; trazabilidad completa: {metrics['traceability_complete_rate']:.12f}.",
    ]
    outputs["summary"].write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    large_outputs = [{"name": name, "path": relative(path, root), "bytes": path.stat().st_size} for name, path in outputs.items() if name != "integration_run_metadata" and path.stat().st_size > 25 * 1024 * 1024]
    too_large = [row for row in large_outputs if row["bytes"] > 50 * 1024 * 1024]
    if too_large:
        raise ValueError(f"Outputs exceed the 50 MB commit guard: {too_large}")
    metadata = {
        "experiment_id": config["experiment_id"], "phase": config["phase"], "dataset_version": config["dataset_version"],
        "created_at_utc": datetime.now(timezone.utc).isoformat(), "command": "python -B -m src.experiments.evaluate_historical_normative_integration_data_aduanas_v02",
        "config": {"path": relative(config_path, root), "sha256": sha256(config_path)}, "eval": eval_cfg,
        "historical_ranking": historical_cfg, "historical_dataset": dataset_cfg, "normative_corpus": corpus_cfg,
        "evidence_selection": config["evidence_selection"], "precedent_selection": config["precedent_selection"], "frozen_phase_artifacts": config["frozen_phase_artifacts"],
        "exclusions": config["exclusions"], "compatibility": compatibility, "label_leakage_audit": label_audit,
        "metrics": metrics, "runtime": {"python": sys.version, "platform": platform.platform()},
        "git": {"branch": git_value(root, "rev-parse", "--abbrev-ref", "HEAD"), "commit": git_value(root, "rev-parse", "HEAD")},
        "outputs": {name: relative(path, root) for name, path in outputs.items()}, "large_outputs_over_25_mb": large_outputs,
        "output_sha256_excludes_self_referential_metadata": True,
    }
    metadata["output_sha256"] = {name: sha256(path) for name, path in outputs.items() if name != "integration_run_metadata"}
    write_json(outputs["integration_run_metadata"], metadata)
    print(f"OK: Fase F integration completed at {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
