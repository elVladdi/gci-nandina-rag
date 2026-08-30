from __future__ import annotations

"""Prepare the blind human review package for HE4 Phase K without scoring it."""

import argparse
import csv
import hashlib
import json
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
FORBIDDEN = {"expected_nandina", "reference_code", "reference_rank", "exact_rank", "correctness", "target", "selection_bucket", "selection_target"}
EXPECTED = {
    "rubric": "175f5405bcdf911fa449cdbbef1fff17284c134970be4a40f8af8a25df25e514",
    "raw": "8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4",
    "parsed": "daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def walk_keys(value: object) -> set[str]:
    if isinstance(value, dict):
        return {str(key).lower() for key in value} | set().union(*(walk_keys(item) for item in value.values()))
    if isinstance(value, list):
        return set().union(*(walk_keys(item) for item in value)) if value else set()
    return set()


def guide() -> str:
    rows = [
        ("Trazabilidad", "Conserva `case_id`, `id_unico`, rank, NANDINA, `candidate_id_unico` y `evidence_id` por candidato.", "Conserva ids principales, pero falta algun identificador o la cita no es facil de rastrear.", "Omite ids criticos o mezcla evidencia entre candidatos."),
        ("Verificabilidad", "Cada afirmacion relevante puede contrastarse con descripcion, evidencia historica o evidencia normativa citada.", "Hay afirmaciones mayormente verificables, pero algunas no tienen soporte claro.", "Introduce atributos, funciones o inferencias no presentes en el payload."),
        ("Separacion historico/normativo", "Explica por separado que aporta la evidencia historica y que aporta la normativa.", "Cita ambas fuentes, pero las mezcla en la justificacion.", "Presenta la evidencia historica como si fuera validacion normativa, o ignora una fuente."),
        ("Prudencia de la conclusion", "Usa lenguaje como compatible, sugiere y requiere revision experta; calibra la conclusion al nivel de soporte.", "Evita clasificacion oficial, pero suena mas decisiva que el soporte declarado.", "Afirma certeza, codigo correcto o correspondencia definitiva."),
        ("Consistencia con Top-3 fijo", "Explica los tres candidatos en el orden recibido y declara que no reordena.", "Mantiene el orden, pero la comparacion sugiere ranking alternativo de forma ambigua.", "Reordena, recomienda fuera del Top-3 o elimina candidatos."),
        ("Deteccion de evidencia normativa generica", "Marca como generica/residual evidencia tipo Los demas, Partes o formulas similares; no la trata como soporte sustantivo.", "Detecta algunas genericidades, pero omite otras o las comunica con poca visibilidad.", "Usa norma residual como evidencia fuerte sin advertencia."),
        ("Comparacion entre candidatos", "Compara criterios observables y normativos relevantes: producto, funcion, atributos tecnicos, alcance normativo y similitud historica.", "Compara candidatos, pero omite algun criterio decisivo o solo explica diferencias obvias.", "No compara el Top-3 o solo repite descripciones."),
        ("Utilidad para auditoria humana", "Permite decidir donde revisar: candidato mas compatible, dudas, evidencia debil y necesidad de escalamiento experto.", "Ayuda a rastrear evidencia, pero no orienta bien la revision siguiente.", "No reduce el trabajo auditor o puede inducir una decision no sustentada."),
    ]
    lines = ["# HE4 qualitative scoring guide v0.2", "", "Fuente congelada: `docs/rubrica_auditabilidad_llm_top3_v0.1.md`.", "", "Cada dimension se puntua 0, 1 o 2. Una ficha es auditable solo con total >=12/16 y sin hard violation.", "", "| Dimension | 2 | 1 | 0 |", "| --- | --- | --- | --- |"]
    lines.extend(f"| {name} | {two} | {one} | {zero} |" for name, two, one, zero in rows)
    lines.extend(["", "## Hard constraints", "", "- Top-3 exactamente preservado y ordenado.", "- Sin codigos NANDINA fuera de `top3_original`.", "- Sin clasificacion oficial ni lenguaje categorico de codigo definitivamente correcto.", "- Conclusion como apoyo documental para revision experta.", "- JSON estricto en el artefacto tecnico.", "", "`advertencias_globales` esta excluido del scoring por el mismatch prompt-schema congelado.", ""])
    return "\n".join(lines)


def run() -> dict[str, Any]:
    root = project_root()
    out = resolve_project_path(OUT)
    paths = {
        "rubric": root / "src/configs/he4_rubric_v0.2.json",
        "rubric_source": root / "docs/rubrica_auditabilidad_llm_top3_v0.1.md",
        "raw": out / "he4_responses_raw_v0.2.jsonl",
        "parsed": out / "he4_responses_parsed_v0.2.jsonl",
        "inputs": out / "he4_generation_inputs_v0.2.jsonl",
        "j_metrics": out / "he4_automatic_validation_metrics_v0.2.json",
        "j_microaudit": out / "gate_j_prompt_schema_microaudit_v0.2.json",
    }
    for name in ("rubric", "raw", "parsed"):
        if sha256(paths[name]) != EXPECTED[name]:
            raise RuntimeError(f"Frozen {name} hash mismatch; Phase K preparation stopped")
    rubric = json.loads(paths["rubric"].read_text(encoding="utf-8"))
    if tuple(rubric["dimensions"]) != DIMENSIONS:
        raise RuntimeError("Frozen rubric dimensions diverged")
    inputs = {row["case_id"]: row for row in read_jsonl(paths["inputs"])}
    parsed = {row["case_id"]: row for row in read_jsonl(paths["parsed"])}
    if len(inputs) != 50 or len(parsed) != 50 or set(inputs) != set(parsed):
        raise RuntimeError("Expected 50 matching frozen HE4 cases")
    packet = []
    for case_id, payload in inputs.items():
        response = parsed[case_id]["parsed_response"]
        record = {
            "case_id": payload["case_id"],
            "id_unico": payload["id_unico"],
            "descripcion_mercancia": payload["descripcion_mercancia"],
            "top3_original": payload["top3_original"],
            "evidencia_historica": [candidate["evidencia_historica"] for candidate in payload["top3_original"]],
            "evidencia_normativa": [candidate["evidencia_normativa"] for candidate in payload["top3_original"]],
            "llm_response": response,
            "dimensions": list(DIMENSIONS),
        }
        if FORBIDDEN & walk_keys(record):
            raise RuntimeError(f"Blind packet contains forbidden evaluation metadata: {case_id}")
        packet.append(record)
    template_fields = ["case_id"] + [field for dimension in DIMENSIONS for field in (f"{dimension}_score", f"{dimension}_justification")] + ["hard_violation", "hard_violation_type", "total_score", "auditable", "general_notes"]
    template = [{field: row["case_id"] if field == "case_id" else "" for field in template_fields} for row in packet]
    write_jsonl(out / "he4_qualitative_review_packet_v0.2.jsonl", packet)
    write_csv(out / "he4_qualitative_scoring_template_v0.2.csv", template, template_fields)
    (out / "he4_qualitative_scoring_guide_v0.2.md").write_text(guide(), encoding="utf-8", newline="\n")
    manifest = {
        "version": "gate_k_pre_scoring_manifest_v0.2",
        "phase_k_status": "AWAITING HUMAN RUBRIC SCORING",
        "gate_k": "PENDING HUMAN SCORING",
        "ready_for_human_scoring": True,
        "ready_for_phase_l": False,
        "evaluator_modality": "A. HUMAN/MANUAL REVIEW",
        "evaluator_identifier": "unassigned_human_reviewer",
        "scoring_date": None,
        "scoring_rule": "0-2 per frozen dimension; auditable iff total >= 12/16 and no hard violation",
        "labels_hidden": True,
        "buckets_hidden": True,
        "external_evidence_prohibited": True,
        "excluded_from_qualitative_scoring_reason": "PROMPT_SCHEMA_SPECIFICATION_MISMATCH",
        "rubric": {"path": str(paths["rubric"].relative_to(root)), "sha256": sha256(paths["rubric"]), "source_path": str(paths["rubric_source"].relative_to(root)), "source_sha256": sha256(paths["rubric_source"])},
        "inputs_sha256": {name: sha256(path) for name, path in paths.items() if name != "rubric_source"},
        "no_scores_assigned": True,
        "no_model_judge": True,
        "no_retrieval": True,
        "no_web": True,
        "phase_k_executed": False,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    write_json(out / "gate_k_pre_scoring_manifest_v0.2.json", manifest)
    return manifest


def main() -> int:
    argparse.ArgumentParser(description="Prepare blind human HE4 qualitative scoring package.").parse_args()
    manifest = run()
    print(json.dumps({"gate_k": manifest["gate_k"], "cases": 50}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
