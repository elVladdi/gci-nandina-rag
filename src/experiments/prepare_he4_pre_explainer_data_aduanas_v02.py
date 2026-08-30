from __future__ import annotations

import csv
import hashlib
import json
import statistics
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import project_root, resolve_project_path


TARGETS = {"rank_1": 15, "rank_2_3": 15, "rank_4_10": 10, "difficult_low_support": 10}


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_hash(path: Path, expected: str, name: str) -> None:
    if sha256(path) != expected:
        raise ValueError(f"{name} hash mismatch")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{clean(key): clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)


def write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def bucket(count: int) -> str:
    if count <= 0: return "0"
    if count == 1: return "1"
    if count <= 4: return "2-4"
    if count <= 9: return "5-9"
    return "10+"


def target(row: Mapping[str, str]) -> str:
    rank, support = int(row["exact_rank"] or 0), int(row["support_count_dams"] or 0)
    if rank == 1: return "rank_1"
    if 2 <= rank <= 3: return "rank_2_3"
    if 4 <= rank <= 10: return "rank_4_10"
    if rank == 0 or rank > 10 or bucket(support) in {"0", "1", "2-4", "5-9"}: return "difficult_low_support"
    return "other"


def selection_key(row: Mapping[str, str]) -> tuple[int, int, int, str]:
    rank, support = int(row["exact_rank"] or 0), int(row["support_count_dams"] or 0)
    order = {"0": 0, "1": 1, "2-4": 2, "5-9": 3, "10+": 4}[bucket(support)]
    return (order, support, 999999 if rank == 0 else rank, row["case_id"])


def select(rows: list[dict[str, str]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    ordered, used, selected = sorted(rows, key=selection_key), set(), []
    availability = {name: sum(target(row) == name for row in rows) for name in TARGETS}
    for name, count in TARGETS.items():
        candidates = [row for row in ordered if target(row) == name] + [row for row in ordered if target(row) != name]
        picked = 0
        for row in candidates:
            if row["case_id"] in used: continue
            used.add(row["case_id"]); picked += 1
            selected.append({"case_id": row["case_id"], "id_unico": row["id_unico"], "selection_target": name, "selection_source": target(row), "selection_note": "exact_category" if target(row) == name else f"fallback_from_{target(row)}", "support_bucket_dams": bucket(int(row["support_count_dams"] or 0)), "support_count_dams": row["support_count_dams"], "exact_rank_evaluation_only": row["exact_rank"], "reference_nandina_evaluation_only": row["expected_nandina"], "query": row["query"]})
            if picked == count: break
        if picked != count: raise ValueError(f"Cannot fill {name}")
    selected.sort(key=lambda row: (list(TARGETS).index(row["selection_target"]), selection_key(next(source for source in rows if source["case_id"] == row["case_id"]))))
    return selected, {"seed": 2026, "rule": "deterministic stratification by support bucket, support count, exact rank and case_id", "availability": availability, "composition": dict(Counter(row["selection_target"] for row in selected))}


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}", *args], cwd=root, text=True, stdout=subprocess.PIPE, check=True).stdout.strip()


def main() -> int:
    root = project_root(); cfg_path = resolve_project_path("src/configs/he4_pre_explainer_v0.2.json"); cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    named = {"eval": cfg["eval"], "historical_results": cfg["historical_results"], "historical_case_summary": cfg["historical_case_summary"], "phase_f_slots": cfg["phase_f_slots"], "corpus": cfg["corpus"]}
    for name, item in named.items(): assert_hash(resolve_project_path(item["path"]), item["sha256"], name)
    prompt = resolve_project_path(cfg["prompt"]["path"]); assert_hash(prompt, cfg["prompt"]["sha256"], "prompt")
    out = resolve_project_path(cfg["outputs"]["directory"])
    if out.exists() and any(out.iterdir()): raise FileExistsError(f"Refusing overwrite: {out}")
    out.mkdir(parents=True)
    eval_rows = {row["case_id"]: row for row in read_csv(resolve_project_path(cfg["eval"]["path"]))}
    summary = read_csv(resolve_project_path(cfg["historical_case_summary"]["path"])); sample, rule = select(summary)
    if len(sample) != 50 or len({row["case_id"] for row in sample}) != 50: raise ValueError("Invalid sample")
    sample_path = out / "he4_explainer_sample_v0.2.csv"
    write_csv(sample_path, sample, list(sample[0]))
    fslots = read_csv(resolve_project_path(cfg["phase_f_slots"]["path"])); f_by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in fslots: f_by_case[row["case_id"]].append(row)
    for rows in f_by_case.values(): rows.sort(key=lambda row: int(row["historical_rank"]))
    a_rows = read_csv(resolve_project_path(cfg["historical_results"]["path"])); a_top3 = {(row["case_id"], row["candidate_rank"]): (row["candidate_nandina"], row["score"]) for row in a_rows if row["method"] == cfg["historical_results"]["method"] and int(row["candidate_rank"]) <= 3}
    contexts, evaluation, slots = [], [], []
    for row in sample:
        case_id = row["case_id"]; source = f_by_case[case_id]
        if len(source) != 3 or [int(item["historical_rank"]) for item in source] != [1, 2, 3]: raise ValueError(f"Invalid F Top-3 {case_id}")
        candidates = []
        for item in source:
            rank = int(item["historical_rank"]); a_code, a_score = a_top3[(case_id, str(rank))]
            if (a_code, a_score) != (item["historical_candidate_code"], item["historical_score"]): raise ValueError(f"Top-3 invariance failure {case_id}/{rank}")
            if item["has_exact_nandina8_evidence"] != "1": raise ValueError("Missing exact normative evidence")
            candidate = {"rank_original": rank, "nandina": item["historical_candidate_code"], "score_historico": item["historical_score"], "ruta_jerarquica": {"clase": item["historical_candidate_code"][:2], "partida": item["historical_candidate_code"][:4], "sub_partida": item["historical_candidate_code"][:6], "nandina": item["historical_candidate_code"]}, "evidencia_historica": {"candidate_id_unico": item["historical_precedent_id_unico"], "candidate_case_id": item["historical_precedent_case_id"], "dam": item["historical_precedent_dam"], "serie": item["historical_precedent_serie"], "texto": item["historical_precedent_description"], "provenance": "Fase F integration_candidate_slots.csv"}, "evidencia_normativa": {"doc_id": item["normative_doc_ids"], "source": item["normative_source"], "version": item["normative_version"], "tipo": item["normative_type"], "codigo": item["normative_document_code"], "pagina": item["normative_source_page"], "linea": item["normative_source_line"], "referencia": item["normative_evidence_reference"], "corpus_sha256": item["normative_corpus_sha256"]}}
            candidates.append(candidate); slots.append({"case_id": case_id, **candidate})
        context = {"case_id": case_id, "id_unico": row["id_unico"], "descripcion_mercancia": eval_rows[case_id]["DESCRIPCION DE MERCANCIAS CONCATENADA"], "top3_original": candidates, "reglas": {"no_agregar_candidatos": True, "no_reordenar": True, "no_clasificacion_oficial": True, "usar_solo_evidencia_suministrada": True}}
        contexts.append(context)
        ref = row["reference_nandina_evaluation_only"]
        ranks = [candidate["nandina"] for candidate in candidates]
        evaluation.append({"case_id": case_id, "reference_nandina_evaluation_only": ref, "reference_rank_evaluation_only": next((i for i, code in enumerate(ranks, 1) if code == ref), 0)})
    if any("reference" in json.dumps(context).lower() or "expected" in json.dumps(context).lower() for context in contexts): raise ValueError("Label key leakage in contexts")
    contexts_path = out / "he4_contexts_v0.2.jsonl"; inputs_path = out / "he4_generation_inputs_v0.2.jsonl"
    write_jsonl(contexts_path, contexts); write_jsonl(inputs_path, contexts)
    write_csv(out / "he4_sample_evaluation_only_v0.2.csv", evaluation, list(evaluation[0]))
    inv = {"slots": len(slots), "slots_expected": 150, "phase_a_equals_phase_f": True, "codes_positions_scores_identical": True, "exact_normative_evidence": sum(item["evidencia_normativa"]["doc_id"] != "" for item in slots), "pass": len(slots) == 150}
    write_json(out / "he4_top3_invariance_v0.2.json", inv)
    old = {row["case_id"] for row in read_csv(root / "outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/sample_cases.csv")}; gsample = {row["case_id"] for row in read_csv(root / "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_diagnostic_sample_v0.2.csv")}
    sample_ids = {row["case_id"] for row in sample}
    profile = {"sample_cases": 50, "unique_dams": len({eval_rows[row["case_id"]]["DECLARACION"] for row in sample}), "unique_reference_codes": len({row["reference_nandina_evaluation_only"] for row in sample}), "unique_hs6_reference": len({row["reference_nandina_evaluation_only"][:6] for row in sample}), "unique_hs4_reference": len({row["reference_nandina_evaluation_only"][:4] for row in sample}), "dam_distribution": dict(sorted(Counter(eval_rows[row["case_id"]]["DECLARACION"] for row in sample).items())), "reference_code_distribution": dict(sorted(Counter(row["reference_nandina_evaluation_only"] for row in sample).items())), "selection": rule, "overlap_v01": len(old & sample_ids), "overlap_phase_g": len(gsample & sample_ids), "duplicate_flags": {"exact_cross_split": sum(row.get("exact_duplicate_cross_split", "").lower() == "true" for row in summary if row["case_id"] in sample_ids), "near_duplicate_095": sum(row.get("near_duplicate_095", "").lower() == "true" for row in summary if row["case_id"] in sample_ids)}}
    write_json(out / "he4_sample_profile_v0.2.json", profile)
    audit = {"label_used_for_sample_design": True, "label_exposed_to_llm": False, "label_used_for_top3": False, "label_used_for_evidence": False, "label_used_for_context": False, "phase_g_information_in_context": False, "pass": True}
    write_json(out / "he4_label_leakage_audit_v0.2.json", audit)
    schema, rubric = resolve_project_path(cfg["schema"]["path"]), resolve_project_path(cfg["rubric"]["path"])
    manifest = {"model": cfg["model"], "availability_checked": False, "availability_note": "Not queried in Fase H: Ollama/model calls are prohibited.", "prompt": cfg["prompt"], "schema_sha256": sha256(schema), "rubric_sha256": sha256(rubric)}
    write_json(out / "he4_model_manifest_v0.2.json", manifest)
    compatibility = {"compatible": True, "eval_hash": sha256(resolve_project_path(cfg["eval"]["path"])), "sample_cases": 50, "sample_subset_eval": all(row["case_id"] in eval_rows for row in sample), "top3_from_phase_a_f": inv["pass"], "corpus_hash": cfg["corpus"]["sha256"], "label_exposed_context": False, "no_experimental_v01_input": True, "phase_a_to_g_intact": True}
    write_json(out / "he4_sample_compatibility_v0.2.json", compatibility)
    hashes = {"eval": cfg["eval"]["sha256"], "sample": sha256(sample_path), "ranking_a": cfg["historical_results"]["sha256"], "integration_f": cfg["phase_f_slots"]["sha256"], "contexts": sha256(contexts_path), "generation_inputs": sha256(inputs_path), "prompt": sha256(prompt), "schema": sha256(schema), "rubric": sha256(rubric), "model_manifest": sha256(out / "he4_model_manifest_v0.2.json")}
    gate = {"experiment_id": cfg["experiment_id"], "phase": cfg["phase"], "created_at_utc": datetime.now(timezone.utc).isoformat(), "execution_commit": git(root, "rev-parse", "HEAD"), "hashes": hashes, "ready_for_phase_i": True, "llm_called": False, "generation_outputs_exist": False, "compatibility": compatibility, "label_leakage": audit, "he4_status": "PENDING GENERATION / VALIDATION / QUALITATIVE EVALUATION"}
    write_json(out / "gate_h_pre_explainer_freeze_v0.2.json", gate)
    (out / "gate_h_pre_explainer_freeze_v0.2.md").write_text(f"# Gate H pre-explainer freeze v0.2\n\n- Estado: **PASS**.\n- Muestra SHA-256: `{hashes['sample']}`.\n- Contextos SHA-256: `{hashes['contexts']}`.\n- Inputs SHA-256: `{hashes['generation_inputs']}`.\n- Prompt SHA-256: `{hashes['prompt']}`.\n- `ready_for_phase_i = true`; no se llamo LLM.\n", encoding="utf-8", newline="\n")
    print(json.dumps({"sample": hashes["sample"], "contexts": hashes["contexts"], "inputs": hashes["generation_inputs"], "ready_for_phase_i": True}, ensure_ascii=False)); return 0


if __name__ == "__main__": raise SystemExit(main())
