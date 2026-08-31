from __future__ import annotations

"""Validate and aggregate the received blind HE4 AI expert-role scoring.

This module never scores, edits, or completes the received CSV.  It only
validates the frozen contract and derives reproducible aggregate artifacts.
"""

import argparse
import csv
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import ensure_parent, project_root, resolve_project_path


OUT = Path("outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2")
DIMENSIONS = (
    "trazabilidad",
    "verificabilidad",
    "separacion_historico_normativo",
    "prudencia_de_la_conclusion",
    "consistencia_con_top3_fijo",
    "deteccion_de_evidencia_normativa_generica",
    "comparacion_entre_candidatos",
    "utilidad_para_auditoria_humana",
)
EXPECTED_HASHES = {
    "rubric": "175f5405bcdf911fa449cdbbef1fff17284c134970be4a40f8af8a25df25e514",
    "review_packet": "e400a5a9b342cef519307713f435629ccb241a1f6eed2ec2d7f7c57a633c2a3d",
    "scoring_guide": "f0be109fd742f33a9ce1df1b2569317a85a8b51d4c61c576e1e2957850408eea",
    "pre_scoring_manifest": "a44716dc1eb4b3ebbfa44295668c99f340b48ae992772f4ed55c1f733931ffef",
    "scoring_template": "5779d6e5f59c8f947a4efa0903da79ff0ec62c8047b79a2eb94ade0518c980c4",
    "inputs": "117ebffc1a113dfc2e28aeffc05b3e0b88998e6a245cd05f14d16147fbdc1596",
    "raw": "8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4",
    "parsed": "daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6",
    "j_metrics": "3dc43932698033cc94149d20be9a474662e990152b1fd1d66f3d067285f21b85",
    "j_microaudit": "8d7258ecd1ff6273d8772fc21da55a70d0bc03721c3fc7fd969a498654bafe5f",
}
EXPECTED_COLUMNS = [
    "case_id",
    *[field for dimension in DIMENSIONS for field in (f"{dimension}_score", f"{dimension}_justification")],
    "hard_violation",
    "hard_violation_type",
    "total_score",
    "auditable",
    "general_notes",
]
CASE_SCORES_COLUMNS = [
    "case_id",
    *[field for dimension in DIMENSIONS for field in (f"{dimension}_score", f"{dimension}_justification")],
    "hard_violation",
    "hard_violation_type",
    "human_entered_total_score",
    "recomputed_total_score",
    "human_entered_auditable",
    "recomputed_auditable",
    "total_score_consistent",
    "auditable_consistent",
    "general_notes",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def count_distribution(values: Iterable[int]) -> dict[str, int]:
    counts = Counter(values)
    return {str(score): counts.get(score, 0) for score in (0, 1, 2)}


def rate(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 6) if denominator else 0.0


def validate_received_scoring(paths: Mapping[str, Path]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    actual_hashes = {name: sha256(path) for name, path in paths.items()}
    mismatches = {
        name: {"expected": EXPECTED_HASHES[name], "actual": actual_hashes[name]}
        for name in EXPECTED_HASHES
        if actual_hashes[name] != EXPECTED_HASHES[name]
    }
    if mismatches:
        raise RuntimeError(f"Frozen input hash mismatch: {json.dumps(mismatches, sort_keys=True)}")

    pre_manifest = read_json(paths["pre_scoring_manifest"])
    if pre_manifest["evaluator_modality"] != "A. HUMAN/MANUAL REVIEW" or not pre_manifest["no_model_judge"]:
        raise RuntimeError("Historical pre-scoring provenance diverged")
    if tuple(read_json(paths["rubric"])["dimensions"]) != DIMENSIONS:
        raise RuntimeError("Frozen rubric dimensions diverged")

    # The authorized received CSV is UTF-8 with a BOM; reading as utf-8-sig
    # preserves its bytes for hashing while comparing its logical header.
    with paths["scoring_template"].open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise RuntimeError("Received scoring CSV columns do not match the frozen contract")
        rows = list(reader)
    packet = read_jsonl(paths["review_packet"])
    packet_ids = [row["case_id"] for row in packet]
    case_ids = [row["case_id"] for row in rows]
    if len(rows) != 50 or len(set(case_ids)) != 50 or set(case_ids) != set(packet_ids):
        raise RuntimeError("Received scoring CSV does not contain the exact 50 review-packet cases")

    score_count = 0
    justification_count = 0
    total_consistent = 0
    auditable_consistent = 0
    derived_rows: list[dict[str, Any]] = []
    for row in rows:
        scores: list[int] = []
        for dimension in DIMENSIONS:
            score_value = row[f"{dimension}_score"].strip()
            if score_value not in {"0", "1", "2"}:
                raise RuntimeError(f"Invalid {dimension} score in {row['case_id']}")
            if not row[f"{dimension}_justification"].strip():
                raise RuntimeError(f"Missing {dimension} justification in {row['case_id']}")
            scores.append(int(score_value))
            score_count += 1
            justification_count += 1
        hard_violation = row["hard_violation"].strip()
        if hard_violation not in {"SI", "NO"}:
            raise RuntimeError(f"Ambiguous hard_violation value in {row['case_id']}")
        if hard_violation == "SI" and not row["hard_violation_type"].strip():
            raise RuntimeError(f"Missing hard_violation_type in {row['case_id']}")
        recomputed_total = sum(scores)
        entered_total = row["total_score"].strip()
        if entered_total != str(recomputed_total):
            raise RuntimeError(f"Manual total_score mismatch in {row['case_id']}")
        recomputed_auditable = "SI" if recomputed_total >= 12 and hard_violation == "NO" else "NO"
        entered_auditable = row["auditable"].strip()
        if entered_auditable not in {"SI", "NO"} or entered_auditable != recomputed_auditable:
            raise RuntimeError(f"Manual auditable mismatch in {row['case_id']}")
        total_consistent += 1
        auditable_consistent += 1
        derived_rows.append({
            "case_id": row["case_id"],
            **{field: row[field] for dimension in DIMENSIONS for field in (f"{dimension}_score", f"{dimension}_justification")},
            "hard_violation": hard_violation,
            "hard_violation_type": row["hard_violation_type"],
            "human_entered_total_score": entered_total,
            "recomputed_total_score": recomputed_total,
            "human_entered_auditable": entered_auditable,
            "recomputed_auditable": recomputed_auditable,
            "total_score_consistent": True,
            "auditable_consistent": True,
            "general_notes": row["general_notes"],
        })
    validation = {
        "template_sha256": actual_hashes["scoring_template"],
        "columns_exact": True,
        "case_count": len(rows),
        "unique_case_ids": len(set(case_ids)),
        "case_id_set_matches_review_packet": True,
        "case_order_matches_review_packet": case_ids == packet_ids,
        "score_count": score_count,
        "justification_count": justification_count,
        "total_score_consistency": {"numerator": total_consistent, "denominator": len(rows), "value": rate(total_consistent, len(rows))},
        "auditable_consistency": {"numerator": auditable_consistent, "denominator": len(rows), "value": rate(auditable_consistent, len(rows))},
        "frozen_input_sha256": actual_hashes,
    }
    return derived_rows, validation


def build_outputs(rows: list[dict[str, Any]], validation: Mapping[str, Any], paths: Mapping[str, Path]) -> dict[str, Any]:
    totals = [int(row["recomputed_total_score"]) for row in rows]
    auditable_rows = [row for row in rows if row["recomputed_auditable"] == "SI"]
    hard_violations = [row for row in rows if row["hard_violation"] == "SI"]
    dimension_rows = []
    for dimension in DIMENSIONS:
        values = [int(row[f"{dimension}_score"]) for row in rows]
        dimension_rows.append({
            "dimension": dimension,
            "score_0_count": values.count(0),
            "score_1_count": values.count(1),
            "score_2_count": values.count(2),
            "mean_score": round(statistics.mean(values), 6),
            "median_score": statistics.median(values),
        })
    metrics = {
        "version": "he4_qualitative_metrics_v0.2",
        "evaluation_basis": "frozen blind HE4 review packet + frozen HE4 rubric",
        "evaluator_modality": "AI_EXPERT_ROLE",
        "evaluator_identifier": "independent_ai_reviewer_01",
        "human_scoring": False,
        "llm_as_judge": True,
        "scoring_date": "NOT_RECORDED_IN_RECEIVED_CSV",
        "scoring_processed_at_utc": datetime.now(timezone.utc).isoformat(),
        "cases": len(rows),
        "auditable": {"numerator": len(auditable_rows), "denominator": len(rows), "rate": rate(len(auditable_rows), len(rows))},
        "non_auditable": {"numerator": len(rows) - len(auditable_rows), "denominator": len(rows), "rate": rate(len(rows) - len(auditable_rows), len(rows))},
        "total_score": {
            "mean": round(statistics.mean(totals), 6),
            "median": statistics.median(totals),
            "min": min(totals),
            "max": max(totals),
            "distribution": {str(total): totals.count(total) for total in range(17) if totals.count(total)},
        },
        "hard_violations": {"count": len(hard_violations), "rate": rate(len(hard_violations), len(rows))},
        "dimension_metrics": {row["dimension"]: {key: value for key, value in row.items() if key != "dimension"} for row in dimension_rows},
        "validation": validation,
    }
    sample_rows: dict[str, dict[str, str]] = {}
    with paths["sample"].open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            sample_rows[row["case_id"]] = row
    bucket_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        sample = sample_rows[row["case_id"]]
        bucket_groups[(sample["selection_target"], sample["support_bucket_dams"])].append(row)
    bucket_rows = []
    for (selection_target, support_bucket_dams), group in sorted(bucket_groups.items()):
        group_totals = [int(row["recomputed_total_score"]) for row in group]
        bucket_rows.append({
            "selection_target": selection_target,
            "support_bucket_dams": support_bucket_dams,
            "cases": len(group),
            "auditable_cases": sum(row["recomputed_auditable"] == "SI" for row in group),
            "auditable_rate": rate(sum(row["recomputed_auditable"] == "SI" for row in group), len(group)),
            "mean_total_score": round(statistics.mean(group_totals), 6),
        })
    microaudit = read_json(paths["j_microaudit"])
    warning_cases = set(microaudit["warning_control_decomposition"]["cases_failing_generic_control"])
    warning_rows = []
    for label, group in (("generic_normative_warning_missing", [row for row in rows if row["case_id"] in warning_cases]), ("other_cases", [row for row in rows if row["case_id"] not in warning_cases])):
        group_totals = [int(row["recomputed_total_score"]) for row in group]
        warning_rows.append({
            "group": label,
            "cases": len(group),
            "auditable_cases": sum(row["recomputed_auditable"] == "SI" for row in group),
            "auditable_rate": rate(sum(row["recomputed_auditable"] == "SI" for row in group), len(group)),
            "mean_total_score": round(statistics.mean(group_totals), 6),
            "generic_normative_warning_control": "failed" if label != "other_cases" else "passed",
        })
    j_metrics = read_json(paths["j_metrics"])
    joint = {
        "version": "he4_he4_joint_jk_assessment_v0.2",
        "he4_j": {
            "gate": "APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION",
            "top3_order_preservation": j_metrics["case_metrics"]["top3_order_preservation_rate"],
            "traceability_completeness": j_metrics["case_metrics"]["traceability_completeness_rate"],
            "generic_normative_warning_control": "41/50",
            "prompt_schema_limitation": "PROMPT_SCHEMA_SPECIFICATION_MISMATCH",
        },
        "he4_k": {
            "gate": "APPROVED WITH EVALUATOR-MODALITY LIMITATION",
            "auditable": metrics["auditable"],
            "hard_violations": metrics["hard_violations"],
            "qualitative_result": "Qualitative scores were processed without changing the received evaluation.",
        },
        "j_k_concordance": {
            "statement": "All 50 cases passed the preserved structural Top-3 and traceability controls in J, while K marks 28 of 50 as individually auditable under the frozen qualitative threshold. The two controls measure different properties and are not interchangeable.",
            "structural_pass_cases": 50,
            "qualitative_auditable_cases": len(auditable_rows),
        },
        "he4_global": "PARTIALLY SUPPORTED",
        "limitations": [
            "PROMPT_SCHEMA_SPECIFICATION_MISMATCH",
            "EVALUATOR_MODALITY_DEVIATION",
            "The qualitative scoring was performed by an independent AI reviewer operating under the frozen expert-role rubric, rather than by the human review modality originally prepared in the pre-scoring protocol.",
        ],
        "evaluator_provenance": {
            "evaluator_modality": "AI_EXPERT_ROLE",
            "evaluator_identifier": "independent_ai_reviewer_01",
            "human_scoring": False,
            "llm_as_judge": True,
            "external_evidence_used": False,
            "ground_truth_exposed": False,
            "reference_rank_exposed": False,
            "bucket_exposed": False,
            "web_used": False,
            "retrieval_used": False,
        },
    }
    hard_violation_rows = [{"case_id": row["case_id"], "hard_violation": row["hard_violation"], "hard_violation_type": row["hard_violation_type"], "recomputed_total_score": row["recomputed_total_score"], "recomputed_auditable": row["recomputed_auditable"]} for row in hard_violations]
    return {"case_scores": rows, "dimension_rows": dimension_rows, "metrics": metrics, "hard_violation_rows": hard_violation_rows, "bucket_rows": bucket_rows, "warning_rows": warning_rows, "joint": joint}


def findings_markdown(metrics: Mapping[str, Any], dimensions: list[Mapping[str, Any]], warning_rows: list[Mapping[str, Any]]) -> str:
    lines = [
        "# EXP-04 Fase K: evaluación cualitativa HE4 v0.2",
        "",
        "## Procedencia y limitación",
        "",
        "La puntuación recibida fue realizada por `AI_EXPERT_ROLE` (`independent_ai_reviewer_01`), no por la modalidad `HUMAN/MANUAL REVIEW` preparada originalmente. Esto se registra como `EVALUATOR_MODALITY_DEVIATION`; no se modificaron los scores ni justificaciones recibidos.",
        "",
        "No se expusieron ground truth, rank de referencia ni buckets durante la puntuación; tampoco se utilizó evidencia externa, web o retrieval. `advertencias_globales` permanece excluido por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.",
        "",
        "## Resultado",
        "",
        f"- Casos auditables: {metrics['auditable']['numerator']}/{metrics['auditable']['denominator']} ({metrics['auditable']['rate']:.1%}).",
        f"- No auditables: {metrics['non_auditable']['numerator']}/{metrics['non_auditable']['denominator']} ({metrics['non_auditable']['rate']:.1%}).",
        f"- Total: media {metrics['total_score']['mean']:.2f}, mediana {metrics['total_score']['median']}, rango {metrics['total_score']['min']}-{metrics['total_score']['max']}.",
        f"- Hard violations: {metrics['hard_violations']['count']}.",
        "",
        "## Dimensiones",
        "",
        "| Dimensión | 0 | 1 | 2 | Media | Mediana |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        *[f"| {row['dimension']} | {row['score_0_count']} | {row['score_1_count']} | {row['score_2_count']} | {row['mean_score']:.2f} | {row['median_score']} |" for row in dimensions],
        "",
        "## Comparación con advertencias J",
        "",
        "| Grupo J | Casos | Auditables | Tasa | Media total |",
        "| --- | ---: | ---: | ---: | ---: |",
        *[f"| {row['group']} | {row['cases']} | {row['auditable_cases']} | {row['auditable_rate']:.1%} | {row['mean_total_score']:.2f} |" for row in warning_rows],
        "",
        "## Dictamen HE4",
        "",
        "HE4 se clasifica como `PARTIALLY SUPPORTED`: J preserva los controles estructurales relevantes, mientras K aporta 28 fichas auditables bajo la regla congelada. El resultado conserva tanto la limitación prompt-schema de J como la desviación de modalidad del evaluador en K.",
        "",
    ]
    return "\n".join(lines)


def run() -> dict[str, Any]:
    root = project_root()
    out = resolve_project_path(OUT)
    paths = {
        "rubric": root / "src/configs/he4_rubric_v0.2.json",
        "review_packet": out / "he4_qualitative_review_packet_v0.2.jsonl",
        "scoring_guide": out / "he4_qualitative_scoring_guide_v0.2.md",
        "pre_scoring_manifest": out / "gate_k_pre_scoring_manifest_v0.2.json",
        "scoring_template": out / "he4_qualitative_scoring_template_v0.2.csv",
        "inputs": out / "he4_generation_inputs_v0.2.jsonl",
        "raw": out / "he4_responses_raw_v0.2.jsonl",
        "parsed": out / "he4_responses_parsed_v0.2.jsonl",
        "j_metrics": out / "he4_automatic_validation_metrics_v0.2.json",
        "j_microaudit": out / "gate_j_prompt_schema_microaudit_v0.2.json",
        "sample": out / "he4_explainer_sample_v0.2.csv",
    }
    rows, validation = validate_received_scoring({name: path for name, path in paths.items() if name != "sample"})
    artifacts = build_outputs(rows, validation, paths)
    output_paths = {
        "case_scores": out / "he4_qualitative_case_scores_v0.2.csv",
        "dimension_metrics": out / "he4_qualitative_dimension_metrics_v0.2.csv",
        "metrics": out / "he4_qualitative_metrics_v0.2.json",
        "hard_violations": out / "he4_qualitative_hard_violations_v0.2.csv",
        "by_bucket": out / "he4_qualitative_by_bucket_v0.2.csv",
        "warning_comparison": out / "he4_qualitative_warning_comparison_v0.2.csv",
        "findings": out / "he4_qualitative_findings_v0.2.md",
        "joint_assessment": out / "he4_he4_joint_jk_assessment_v0.2.json",
        "manifest": out / "gate_k_qualitative_evaluation_manifest_v0.2.json",
        "summary": out / "summary_phase_k.md",
    }
    write_csv(output_paths["case_scores"], artifacts["case_scores"], CASE_SCORES_COLUMNS)
    write_csv(output_paths["dimension_metrics"], artifacts["dimension_rows"], ["dimension", "score_0_count", "score_1_count", "score_2_count", "mean_score", "median_score"])
    write_json(output_paths["metrics"], artifacts["metrics"])
    write_csv(output_paths["hard_violations"], artifacts["hard_violation_rows"], ["case_id", "hard_violation", "hard_violation_type", "recomputed_total_score", "recomputed_auditable"])
    write_csv(output_paths["by_bucket"], artifacts["bucket_rows"], ["selection_target", "support_bucket_dams", "cases", "auditable_cases", "auditable_rate", "mean_total_score"])
    write_csv(output_paths["warning_comparison"], artifacts["warning_rows"], ["group", "cases", "auditable_cases", "auditable_rate", "mean_total_score", "generic_normative_warning_control"])
    output_paths["findings"].write_text(findings_markdown(artifacts["metrics"], artifacts["dimension_rows"], artifacts["warning_rows"]), encoding="utf-8", newline="\n")
    write_json(output_paths["joint_assessment"], artifacts["joint"])
    non_manifest_hashes = {name: sha256(path) for name, path in output_paths.items() if name not in {"manifest", "summary"}}
    manifest = {
        "version": "gate_k_qualitative_evaluation_manifest_v0.2",
        "phase": "EXP-04 K",
        "gate_k": "APPROVED WITH EVALUATOR-MODALITY LIMITATION",
        "ready_for_phase_l": True,
        "evaluator_modality": "AI_EXPERT_ROLE",
        "evaluator_identifier": "independent_ai_reviewer_01",
        "human_scoring": False,
        "llm_as_judge": True,
        "evaluation_basis": "frozen blind HE4 review packet + frozen HE4 rubric",
        "methodological_deviation": True,
        "methodological_deviation_type": "EVALUATOR_MODALITY_DEVIATION",
        "original_pre_scoring_modality": "HUMAN/MANUAL REVIEW",
        "rubric_frozen": True,
        "ground_truth_exposed": False,
        "reference_rank_exposed": False,
        "bucket_exposed": False,
        "external_evidence_used": False,
        "web_used": False,
        "retrieval_used": False,
        "scores_modified_by_codex": False,
        "advertencias_globales_excluded": True,
        "prompt_schema_limitation_preserved": True,
        "pre_scoring_manifest_preserved": True,
        "input_sha256": validation["frozen_input_sha256"],
        "validation": validation,
        "outputs_sha256_excluding_manifest_and_summary": non_manifest_hashes,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    write_json(output_paths["manifest"], manifest)
    summary = "\n".join([
        "# EXP-04 Fase K closure summary",
        "",
        "- Gate K: APPROVED WITH EVALUATOR-MODALITY LIMITATION.",
        "- Evaluator modality: AI_EXPERT_ROLE (independent_ai_reviewer_01).",
        "- Original prepared modality: HUMAN/MANUAL REVIEW.",
        "- Methodological deviation: EVALUATOR_MODALITY_DEVIATION.",
        f"- Auditable: {artifacts['metrics']['auditable']['numerator']}/50 ({artifacts['metrics']['auditable']['rate']:.1%}).",
        f"- HE4 global: {artifacts['joint']['he4_global']}.",
        f"- Manifest SHA-256: {sha256(output_paths['manifest'])}.",
        "- Fase L was not executed.",
        "",
    ])
    output_paths["summary"].write_text(summary, encoding="utf-8", newline="\n")
    return {"manifest": manifest, "output_sha256": {name: sha256(path) for name, path in output_paths.items()}, "metrics": artifacts["metrics"]}


def main() -> int:
    argparse.ArgumentParser(description="Close HE4 Phase K from received AI expert-role scoring.").parse_args()
    result = run()
    print(json.dumps({"gate_k": result["manifest"]["gate_k"], "auditable": result["metrics"]["auditable"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
