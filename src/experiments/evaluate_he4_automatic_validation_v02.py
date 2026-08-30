from __future__ import annotations

"""Offline, deterministic automatic controls for EXP-04 HE4 Phase J."""

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import ensure_parent, project_root, resolve_project_path


OUT_DIR = Path("outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2")
CONFIG_PATH = Path("src/configs/he4_pre_explainer_v0.2.json")
EXPECTED_CASES = 50
EXPECTED_RANKS = [1, 2, 3]
SUPPORT_VALUES = {"alto", "medio", "bajo"}
FINAL_WARNING_FRAGMENT = "no reemplaza la clasificacion oficial"
RESERVED_OUTPUT_KEYS = {
    "expected_nandina",
    "reference_code",
    "ground_truth",
    "target",
    "correct_candidate",
    "correctness",
}
OFFICIAL_CLASSIFICATION_PATTERNS = (
    "clasificacion oficial es",
    "clasificación oficial es",
    "debe clasificarse",
    "se clasifica oficialmente",
    "codigo correcto es",
    "código correcto es",
)
ROOT_REQUIRED_FIELDS = (
    "id_unico",
    "case_id",
    "descripcion_mercancia",
    "resumen_observable",
    "candidatos_explicados",
    "comparacion_top3",
    "advertencias_globales",
    "conclusion_auditable",
    "advertencia_final",
)
CANDIDATE_REQUIRED_FIELDS = (
    "rank_original",
    "nandina",
    "ruta_jerarquica",
    "soporte",
    "evidencia_historica_usada",
    "evidencia_normativa_usada",
    "coincidencias",
    "diferencias_o_dudas",
    "razon_de_soporte",
    "advertencias",
)
PHASE_J_FILES = (
    "he4_automatic_validation_case_results_v0.2.csv",
    "he4_automatic_validation_slot_results_v0.2.csv",
    "he4_automatic_validation_metrics_v0.2.json",
    "he4_automatic_validation_errors_v0.2.csv",
    "he4_automatic_validation_by_bucket_v0.2.csv",
    "he4_reference_validation_v0.2.json",
    "he4_traceability_validation_v0.2.json",
    "gate_j_automatic_validation_manifest_v0.2.json",
    "summary_phase_j.md",
)


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(value: object) -> str:
    text = unicodedata.normalize("NFKD", _clean(value)).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text).lower().strip()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in csv.DictReader(handle)]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fieldnames: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def _walk_keys(value: object) -> set[str]:
    if isinstance(value, dict):
        return {str(key).lower() for key in value} | set().union(*(_walk_keys(item) for item in value.values()))
    if isinstance(value, list):
        return set().union(*(_walk_keys(item) for item in value)) if value else set()
    return set()


def _is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _as_list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _schema_check(response: object) -> dict[str, Any]:
    result = {
        "schema_valid": False,
        "missing_required_fields": [],
        "extra_fields": [],
        "wrong_types": [],
        "invalid_enums": [],
        "structural_errors": [],
        "required_fields_complete": False,
    }
    if not isinstance(response, dict):
        result["structural_errors"].append("response_not_object")
        return result

    result["missing_required_fields"] = [field for field in ROOT_REQUIRED_FIELDS if field not in response]
    root_types = {
        "id_unico": str,
        "case_id": str,
        "descripcion_mercancia": str,
        "resumen_observable": dict,
        "candidatos_explicados": list,
        "comparacion_top3": dict,
        "conclusion_auditable": str,
        "advertencia_final": str,
    }
    for field, expected_type in root_types.items():
        if field in response and not isinstance(response[field], expected_type):
            result["wrong_types"].append(f"{field}: expected_{expected_type.__name__}")
    for field in ("id_unico", "case_id", "descripcion_mercancia", "conclusion_auditable", "advertencia_final"):
        if field in response and isinstance(response[field], str) and not response[field].strip():
            result["structural_errors"].append(f"{field}: empty")

    candidates = response.get("candidatos_explicados")
    if not isinstance(candidates, list):
        result["structural_errors"].append("candidatos_explicados: not_list")
    else:
        if len(candidates) != 3:
            result["structural_errors"].append("candidatos_explicados: expected_3")
        for position, candidate in enumerate(candidates, start=1):
            prefix = f"candidatos_explicados[{position}]"
            if not isinstance(candidate, dict):
                result["structural_errors"].append(f"{prefix}: not_object")
                continue
            for field in CANDIDATE_REQUIRED_FIELDS:
                if field not in candidate:
                    result["missing_required_fields"].append(f"{prefix}.{field}")
            for field in ("rank_original",):
                if field in candidate and not isinstance(candidate[field], int):
                    result["wrong_types"].append(f"{prefix}.{field}: expected_int")
            for field in ("nandina", "razon_de_soporte"):
                if field in candidate and not isinstance(candidate[field], str):
                    result["wrong_types"].append(f"{prefix}.{field}: expected_str")
                elif field in candidate and not candidate[field].strip():
                    result["structural_errors"].append(f"{prefix}.{field}: empty")
            for field in ("ruta_jerarquica",):
                if field in candidate and not isinstance(candidate[field], dict):
                    result["wrong_types"].append(f"{prefix}.{field}: expected_object")
            for field in ("evidencia_historica_usada", "evidencia_normativa_usada", "coincidencias", "diferencias_o_dudas", "advertencias"):
                if field in candidate and not isinstance(candidate[field], list):
                    result["wrong_types"].append(f"{prefix}.{field}: expected_list")
            if "soporte" in candidate and _norm(candidate["soporte"]) not in SUPPORT_VALUES:
                result["invalid_enums"].append(f"{prefix}.soporte")
    result["required_fields_complete"] = not result["missing_required_fields"]
    result["schema_valid"] = not any(
        (result["missing_required_fields"], result["wrong_types"], result["invalid_enums"], result["structural_errors"])
    )
    return result


def _references_for_candidate(
    candidate: Mapping[str, Any],
    frozen_candidate: Mapping[str, Any],
    global_historical: set[str],
    case_historical: set[str],
    global_normative: set[str],
    case_normative: set[str],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    expected_historical = _clean(frozen_candidate.get("evidencia_historica", {}).get("candidate_id_unico"))
    expected_normative = _clean(frozen_candidate.get("evidencia_normativa", {}).get("doc_id"))
    slots: list[dict[str, Any]] = []
    historical_ids = [
        _clean(entry.get("candidate_id_unico"))
        for entry in _as_list(candidate.get("evidencia_historica_usada"))
        if isinstance(entry, dict) and _clean(entry.get("candidate_id_unico"))
    ]
    normative_ids = [
        _clean(entry.get("evidence_id"))
        for entry in _as_list(candidate.get("evidencia_normativa_usada"))
        if isinstance(entry, dict) and _clean(entry.get("evidence_id"))
    ]
    historical_valid = expected_historical in historical_ids
    normative_valid = expected_normative in normative_ids
    fabricated = 0
    out_of_context = 0
    for reference_type, ids, global_ids, case_ids in (
        ("historical", historical_ids, global_historical, case_historical),
        ("normative", normative_ids, global_normative, case_normative),
    ):
        for reference_id in ids:
            exists = reference_id in global_ids
            allowed = reference_id in case_ids
            if not exists:
                fabricated += 1
            elif not allowed:
                out_of_context += 1
            slots.append(
                {
                    "reference_type": reference_type,
                    "reference_id": reference_id,
                    "reference_exists": int(exists),
                    "reference_allowed": int(allowed),
                    "reference_candidate_match": int(reference_id == (expected_historical if reference_type == "historical" else expected_normative)),
                }
            )
    return {
        "historical_reference_valid": int(historical_valid),
        "normative_reference_valid": int(normative_valid),
        "historical_reference_exists": int(bool(historical_ids) and all(value in global_historical for value in historical_ids)),
        "historical_reference_allowed": int(bool(historical_ids) and all(value in case_historical for value in historical_ids)),
        "historical_reference_candidate_match": int(historical_valid),
        "normative_reference_exists": int(bool(normative_ids) and all(value in global_normative for value in normative_ids)),
        "normative_reference_allowed": int(bool(normative_ids) and all(value in case_normative for value in normative_ids)),
        "normative_reference_candidate_match": int(normative_valid),
        "fabricated_reference_count": fabricated,
        "out_of_context_reference_count": out_of_context,
        "historical_reference_ids": historical_ids,
        "normative_reference_ids": normative_ids,
    }, slots


def _generic_normative_warning(candidate: Mapping[str, Any], frozen_candidate: Mapping[str, Any]) -> bool:
    source_text = _norm(frozen_candidate.get("evidencia_normativa", {}).get("referencia"))
    if "los demas" not in source_text:
        return True
    warnings = _as_list(candidate.get("advertencias"))
    limitations = [
        value
        for evidence in _as_list(candidate.get("evidencia_normativa_usada"))
        if isinstance(evidence, dict)
        for value in _as_list(evidence.get("limitaciones"))
    ]
    warning_text = _norm(" ".join(_clean(value) for value in warnings + limitations))
    return any(fragment in warning_text for fragment in ("generica", "los demas", "insuficiente"))


def _case_validation(
    sample: Mapping[str, str],
    frozen: Mapping[str, Any],
    raw: Mapping[str, Any] | None,
    parsed: Mapping[str, Any] | None,
    global_historical: set[str],
    global_normative: set[str],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    case_id = _clean(frozen.get("case_id"))
    base: dict[str, Any] = {
        "case_id": case_id,
        "id_unico": _clean(frozen.get("id_unico")),
        "selection_target": _clean(sample.get("selection_target")),
        "raw_parseable": 0,
        "parsed_matches_raw": 0,
        "schema_valid": 0,
        "missing_required_fields": "",
        "extra_fields": "",
        "wrong_types": "",
        "invalid_enums": "",
        "structural_errors": "",
        "candidate_set_exact": 0,
        "top3_order_preserved": 0,
        "rank_field_consistency": 0,
        "external_code_count": 0,
        "missing_candidate_count": 3,
        "duplicate_candidate_count": 0,
        "unexpected_candidate_count": 0,
        "historical_reference_valid": 0,
        "normative_reference_valid": 0,
        "fabricated_reference_count": 0,
        "out_of_context_reference_count": 0,
        "required_fields_complete": 0,
        "comparison_present": 0,
        "warnings_field_valid": 0,
        "generic_normative_warning_when_required": 0,
        "no_official_classification_claim": 0,
        "explicit_label_leakage": 0,
        "traceability_complete": 0,
        "automatic_validation_pass": "NOT_DEFINED_PRE_GENERATION",
        "failure_reasons": "",
    }
    slot_rows: list[dict[str, Any]] = []
    failures: list[str] = []
    raw_response: object = None
    if raw and isinstance(raw.get("raw_response"), str):
        try:
            raw_response = json.loads(raw["raw_response"])
            base["raw_parseable"] = int(isinstance(raw_response, dict))
        except json.JSONDecodeError:
            failures.append("SCHEMA_ERROR")
    if base["raw_parseable"] and parsed:
        base["parsed_matches_raw"] = int(raw_response == parsed.get("parsed_response"))
        if not base["parsed_matches_raw"]:
            failures.append("OTHER_PREDEFINED_AUTOMATIC_ERROR")
    else:
        failures.append("SCHEMA_ERROR")

    schema = _schema_check(raw_response)
    for field in ("missing_required_fields", "extra_fields", "wrong_types", "invalid_enums", "structural_errors"):
        base[field] = "|".join(schema[field])
    base["schema_valid"] = int(schema["schema_valid"])
    base["required_fields_complete"] = int(schema["required_fields_complete"])
    if not base["schema_valid"]:
        failures.append("SCHEMA_ERROR")
    if not base["required_fields_complete"]:
        failures.append("MISSING_REQUIRED_FIELD")

    response = raw_response if isinstance(raw_response, dict) else {}
    frozen_candidates = _as_list(frozen.get("top3_original"))
    explained = [candidate for candidate in _as_list(response.get("candidatos_explicados")) if isinstance(candidate, dict)]
    expected_codes = [_clean(candidate.get("nandina")) for candidate in frozen_candidates]
    actual_codes = [_clean(candidate.get("nandina")) for candidate in explained]
    actual_ranks = [candidate.get("rank_original") for candidate in explained]
    expected_by_rank = {int(candidate.get("rank_original") or 0): candidate for candidate in frozen_candidates}
    case_historical = {_clean(candidate.get("evidencia_historica", {}).get("candidate_id_unico")) for candidate in frozen_candidates}
    case_normative = {_clean(candidate.get("evidencia_normativa", {}).get("doc_id")) for candidate in frozen_candidates}
    base["external_code_count"] = sum(1 for code in actual_codes if code and code not in expected_codes)
    base["missing_candidate_count"] = sum((Counter(expected_codes) - Counter(actual_codes)).values())
    base["duplicate_candidate_count"] = sum(count - 1 for code, count in Counter(actual_codes).items() if code and count > 1)
    base["unexpected_candidate_count"] = base["external_code_count"]
    base["candidate_set_exact"] = int(
        len(explained) == 3
        and Counter(actual_codes) == Counter(expected_codes)
        and base["duplicate_candidate_count"] == 0
    )
    base["top3_order_preserved"] = int(actual_codes == expected_codes)
    base["rank_field_consistency"] = int(actual_ranks == EXPECTED_RANKS)
    if base["external_code_count"]:
        failures.append("EXTERNAL_CODE")
    if base["missing_candidate_count"]:
        failures.append("MISSING_CANDIDATE")
    if base["duplicate_candidate_count"]:
        failures.append("DUPLICATE_CANDIDATE")
    if not base["top3_order_preserved"] or not base["rank_field_consistency"]:
        failures.append("ORDER_VIOLATION")

    historical_validities: list[int] = []
    normative_validities: list[int] = []
    generic_warnings: list[bool] = []
    for position, frozen_candidate in enumerate(frozen_candidates, start=1):
        expected_rank = int(frozen_candidate.get("rank_original") or 0)
        candidate = explained[position - 1] if len(explained) >= position else {}
        references, refs = _references_for_candidate(candidate, frozen_candidate, global_historical, case_historical, global_normative, case_normative)
        historical_validities.append(references["historical_reference_valid"])
        normative_validities.append(references["normative_reference_valid"])
        generic_warnings.append(_generic_normative_warning(candidate, frozen_candidate))
        for ref in refs:
            ref.update({"case_id": case_id, "rank_original": expected_rank, "expected_nandina": _clean(frozen_candidate.get("nandina"))})
        slot_rows.append(
            {
                "case_id": case_id,
                "rank_original": expected_rank,
                "expected_nandina": _clean(frozen_candidate.get("nandina")),
                "output_nandina": _clean(candidate.get("nandina")),
                "code_valid": int(_clean(candidate.get("nandina")) == _clean(frozen_candidate.get("nandina"))),
                "rank_consistent": int(candidate.get("rank_original") == expected_rank),
                "historical_reference_valid": references["historical_reference_valid"],
                "normative_reference_valid": references["normative_reference_valid"],
                "historical_reference_exists": references["historical_reference_exists"],
                "historical_reference_allowed": references["historical_reference_allowed"],
                "historical_reference_candidate_match": references["historical_reference_candidate_match"],
                "normative_reference_exists": references["normative_reference_exists"],
                "normative_reference_allowed": references["normative_reference_allowed"],
                "normative_reference_candidate_match": references["normative_reference_candidate_match"],
                "fabricated_reference_count": references["fabricated_reference_count"],
                "out_of_context_reference_count": references["out_of_context_reference_count"],
                "historical_reference_ids": "|".join(references["historical_reference_ids"]),
                "normative_reference_ids": "|".join(references["normative_reference_ids"]),
                "reference_assertions": refs,
            }
        )
    base["historical_reference_valid"] = int(len(historical_validities) == 3 and all(historical_validities))
    base["normative_reference_valid"] = int(len(normative_validities) == 3 and all(normative_validities))
    base["fabricated_reference_count"] = sum(row["fabricated_reference_count"] for row in slot_rows)
    base["out_of_context_reference_count"] = sum(row["out_of_context_reference_count"] for row in slot_rows)
    if not base["historical_reference_valid"]:
        failures.append("INVALID_HISTORICAL_REFERENCE")
    if not base["normative_reference_valid"]:
        failures.append("INVALID_NORMATIVE_REFERENCE")
    if base["fabricated_reference_count"]:
        failures.append("FABRICATED_REFERENCE")
    if base["out_of_context_reference_count"]:
        failures.append("OUT_OF_CONTEXT_REFERENCE")

    comparison = response.get("comparacion_top3")
    if isinstance(comparison, dict):
        criteria = _as_list(comparison.get("criterios_comparados"))
        best = comparison.get("candidato_con_mayor_soporte")
        base["comparison_present"] = int(
            bool(criteria)
            and isinstance(best, dict)
            and _clean(best.get("nandina")) in expected_codes
            and best.get("rank_original") in EXPECTED_RANKS
        )
    candidate_warning_types_ok = all(isinstance(candidate.get("advertencias"), list) for candidate in explained)
    final_warning = _norm(response.get("advertencia_final"))
    base["warnings_field_valid"] = int(candidate_warning_types_ok and FINAL_WARNING_FRAGMENT in final_warning)
    base["generic_normative_warning_when_required"] = int(len(generic_warnings) == 3 and all(generic_warnings))
    if not base["comparison_present"]:
        failures.append("MISSING_REQUIRED_FIELD")
    if not base["warnings_field_valid"] or not base["generic_normative_warning_when_required"]:
        failures.append("INVALID_WARNING_FIELD")
    text = _norm(json.dumps(response, ensure_ascii=False))
    base["no_official_classification_claim"] = int(not any(_norm(pattern) in text for pattern in OFFICIAL_CLASSIFICATION_PATTERNS))
    if not base["no_official_classification_claim"]:
        failures.append("OTHER_PREDEFINED_AUTOMATIC_ERROR")
    base["explicit_label_leakage"] = int(bool(RESERVED_OUTPUT_KEYS & _walk_keys(response)))
    if base["explicit_label_leakage"]:
        failures.append("OTHER_PREDEFINED_AUTOMATIC_ERROR")
    base["traceability_complete"] = int(
        raw is not None
        and parsed is not None
        and _clean(raw.get("case_id")) == case_id
        and _clean(parsed.get("case_id")) == case_id
        and _clean(raw.get("input_hash")) == _clean(parsed.get("input_hash"))
        and len(frozen_candidates) == 3
    )
    if not base["traceability_complete"]:
        failures.append("OTHER_PREDEFINED_AUTOMATIC_ERROR")
    base["failure_reasons"] = "|".join(dict.fromkeys(failures))
    return base, slot_rows


def _metric(numerator: int, denominator: int) -> dict[str, Any]:
    return {"numerator": numerator, "denominator": denominator, "value": numerator / denominator if denominator else 0.0}


def _output_hashes(out: Path) -> dict[str, str]:
    return {name: _sha256(out / name) for name in PHASE_J_FILES if name != "gate_j_automatic_validation_manifest_v0.2.json"}


def _summary(metrics: Mapping[str, Any], gate: str) -> str:
    lines = [
        "# EXP-04 Fase J - Controles automaticos HE4 v0.2",
        "",
        f"- Gate J: `{gate}`.",
        "- La validacion es deterministica y offline; no regenera ni modifica respuestas de Fase I.",
        "- HE4 global permanece pendiente de evaluacion cualitativa de Fase K.",
        "",
        "## Metricas por caso",
        "",
        "| Control | Resultado |",
        "| --- | ---: |",
    ]
    for name, value in metrics["case_metrics"].items():
        lines.append(f"| {name} | {value['numerator']}/{value['denominator']} ({value['value']:.4f}) |")
    lines.extend(["", "## Metricas por slot", "", "| Control | Resultado |", "| --- | ---: |"])
    for name, value in metrics["slot_metrics"].items():
        lines.append(f"| {name} | {value['numerator']}/{value['denominator']} ({value['value']:.4f}) |")
    lines.extend([
        "",
        "## Regla historica agregada",
        "",
        f"- Cumplimiento de los umbrales congelados: `{metrics['frozen_aggregate_pass']['passed']}`.",
        "- No existia una regla pre-generacion de PASS/FAIL por caso; por ello no se calcula tasa de automatic_validation_pass.",
        "",
    ])
    return "\n".join(lines)


def run() -> dict[str, Any]:
    root = project_root()
    config = json.loads(resolve_project_path(CONFIG_PATH).read_text(encoding="utf-8"))
    out = resolve_project_path(config["outputs"]["directory"])
    gate_h = json.loads((out / "gate_h_pre_explainer_freeze_v0.2.json").read_text(encoding="utf-8"))
    gate_i = json.loads((out / "gate_i_generation_manifest_v0.2.json").read_text(encoding="utf-8"))
    input_paths = {
        "sample": out / "he4_explainer_sample_v0.2.csv",
        "contexts": out / "he4_contexts_v0.2.jsonl",
        "generation_inputs": out / "he4_generation_inputs_v0.2.jsonl",
        "prompt": root / config["prompt"]["path"],
        "schema": root / config["schema"]["path"],
        "rubric": root / config["rubric"]["path"],
        "raw_responses": out / "he4_responses_raw_v0.2.jsonl",
        "parsed_responses": out / "he4_responses_parsed_v0.2.jsonl",
        "generation_execution": out / "he4_generation_execution_v0.2.csv",
        "gate_i_pre_generation": out / "gate_i_pre_generation_check_v0.2.json",
    }
    expected_hashes = {
        **gate_h["hashes"],
        "raw_responses": "8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4",
        "parsed_responses": "daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6",
        "generation_execution": "323a79cb2a54601c669e711bb4f698fa328f0c51a9f77998612d46bbfbb9cc80",
        "gate_i_pre_generation": "a36232f0846f9babdf12e48c9779e1c10cae5b406dd91de1db7a06a9a231bfbb",
    }
    input_hashes = {name: {"expected": expected_hashes[name], "actual": _sha256(path), "pass": _sha256(path) == expected_hashes[name]} for name, path in input_paths.items() if name in expected_hashes}
    if not all(record["pass"] for record in input_hashes.values()):
        raise RuntimeError("Frozen Phase H/I input hash mismatch; Phase J stopped before validation")
    if not input_paths["contexts"].read_bytes() == input_paths["generation_inputs"].read_bytes():
        raise RuntimeError("Frozen HE4 contexts and generation inputs diverged")

    sample = _read_csv(input_paths["sample"])
    inputs = _read_jsonl(input_paths["generation_inputs"])
    raw_rows = _read_jsonl(input_paths["raw_responses"])
    parsed_rows = _read_jsonl(input_paths["parsed_responses"])
    if not all(len(collection) == EXPECTED_CASES for collection in (sample, inputs, raw_rows, parsed_rows)):
        raise RuntimeError("Phase J requires exactly 50 H/I records in every frozen input")
    input_by_case = {_clean(row.get("case_id")): row for row in inputs}
    raw_by_case = {_clean(row.get("case_id")): row for row in raw_rows}
    parsed_by_case = {_clean(row.get("case_id")): row for row in parsed_rows}
    if any(len(collection) != EXPECTED_CASES for collection in (input_by_case, raw_by_case, parsed_by_case)):
        raise RuntimeError("Duplicate or empty case_id in frozen H/I inputs")
    global_historical = {
        _clean(candidate.get("evidencia_historica", {}).get("candidate_id_unico"))
        for payload in inputs
        for candidate in _as_list(payload.get("top3_original"))
    }
    global_normative = {
        _clean(candidate.get("evidencia_normativa", {}).get("doc_id"))
        for payload in inputs
        for candidate in _as_list(payload.get("top3_original"))
    }
    case_rows: list[dict[str, Any]] = []
    slot_rows: list[dict[str, Any]] = []
    for sample_row in sample:
        case_id = _clean(sample_row.get("case_id"))
        row, slots = _case_validation(sample_row, input_by_case[case_id], raw_by_case.get(case_id), parsed_by_case.get(case_id), global_historical, global_normative)
        case_rows.append(row)
        slot_rows.extend(slots)
    if len(slot_rows) != EXPECTED_CASES * 3:
        raise RuntimeError("Phase J expected 150 candidate slots")

    error_rows = [
        {"case_id": row["case_id"], "selection_target": row["selection_target"], "error_type": error_type}
        for row in case_rows
        for error_type in row["failure_reasons"].split("|")
        if error_type
    ]
    case_metrics = {
        "raw_json_parse_rate": _metric(sum(row["raw_parseable"] for row in case_rows), 50),
        "parsed_raw_identity_rate": _metric(sum(row["parsed_matches_raw"] for row in case_rows), 50),
        "schema_compliance_rate": _metric(sum(row["schema_valid"] for row in case_rows), 50),
        "candidate_set_closure_rate": _metric(sum(row["candidate_set_exact"] for row in case_rows), 50),
        "top3_order_preservation_rate": _metric(sum(row["top3_order_preserved"] for row in case_rows), 50),
        "rank_consistency_rate": _metric(sum(row["rank_field_consistency"] for row in case_rows), 50),
        "external_code_free_rate": _metric(sum(not row["external_code_count"] for row in case_rows), 50),
        "missing_candidate_free_rate": _metric(sum(not row["missing_candidate_count"] for row in case_rows), 50),
        "duplicate_candidate_free_rate": _metric(sum(not row["duplicate_candidate_count"] for row in case_rows), 50),
        "historical_reference_validity_rate": _metric(sum(row["historical_reference_valid"] for row in case_rows), 50),
        "normative_reference_validity_rate": _metric(sum(row["normative_reference_valid"] for row in case_rows), 50),
        "fabricated_reference_free_rate": _metric(sum(not row["fabricated_reference_count"] for row in case_rows), 50),
        "out_of_context_reference_free_rate": _metric(sum(not row["out_of_context_reference_count"] for row in case_rows), 50),
        "required_fields_completeness_rate": _metric(sum(row["required_fields_complete"] for row in case_rows), 50),
        "comparison_presence_rate": _metric(sum(row["comparison_present"] for row in case_rows), 50),
        "warnings_field_compliance_rate": _metric(sum(row["warnings_field_valid"] for row in case_rows), 50),
        "traceability_completeness_rate": _metric(sum(row["traceability_complete"] for row in case_rows), 50),
        "explicit_label_leakage_free_rate": _metric(sum(not row["explicit_label_leakage"] for row in case_rows), 50),
    }
    slot_metrics = {
        "candidate_code_valid_rate": _metric(sum(row["code_valid"] for row in slot_rows), 150),
        "rank_consistent_rate": _metric(sum(row["rank_consistent"] for row in slot_rows), 150),
        "historical_reference_valid_rate": _metric(sum(row["historical_reference_valid"] for row in slot_rows), 150),
        "normative_reference_valid_rate": _metric(sum(row["normative_reference_valid"] for row in slot_rows), 150),
    }
    frozen_pass = {
        "json_valido_rate_min": case_metrics["raw_json_parse_rate"]["value"] >= 0.95,
        "ranking_preservado_rate": case_metrics["top3_order_preservation_rate"]["value"] == 1.0,
        "sin_codigos_fuera_pool_rate": case_metrics["external_code_free_rate"]["value"] == 1.0,
        "evidencia_historica_citada_por_candidato_rate_min": case_metrics["historical_reference_validity_rate"]["value"] >= 0.95,
        "evidencia_normativa_citada_por_candidato_rate_min": case_metrics["normative_reference_validity_rate"]["value"] >= 0.95,
        "comparacion_top3_presente_rate_min": case_metrics["comparison_presence_rate"]["value"] >= 0.95,
        "advertencia_final_presente_rate_min": case_metrics["warnings_field_compliance_rate"]["value"] >= 0.95,
        "sin_senales_reranking_rate": case_metrics["top3_order_preservation_rate"]["value"] == 1.0,
        "sin_clasificacion_oficial_rate": all(row["no_official_classification_claim"] for row in case_rows),
    }
    metrics = {
        "version": "he4_automatic_validation_metrics_v0.2",
        "cases": 50,
        "candidate_slots": 150,
        "case_metrics": case_metrics,
        "slot_metrics": slot_metrics,
        "automatic_validation_pass": {"applicable": False, "reason": "No pre-generation per-case PASS/FAIL rule existed in the frozen schema or historical validator."},
        "frozen_aggregate_pass": {"criteria": frozen_pass, "passed": all(frozen_pass.values())},
        "error_taxonomy": dict(sorted(Counter(row["error_type"] for row in error_rows).items())),
    }
    bucket_rows = []
    for bucket in ("rank_1", "rank_2_3", "rank_4_10", "difficult_low_support"):
        subset = [row for row in case_rows if row["selection_target"] == bucket]
        for metric_name in ("raw_parseable", "schema_valid", "candidate_set_exact", "top3_order_preserved", "historical_reference_valid", "normative_reference_valid", "comparison_present", "warnings_field_valid", "traceability_complete"):
            bucket_rows.append({"selection_target": bucket, "metric": metric_name, **_metric(sum(row[metric_name] for row in subset), len(subset))})
    references = {
        "version": "he4_reference_validation_v0.2",
        "definition": "Reference existence is tested against the frozen 50-input H context; allowed means present in the same case context; candidate match means it belongs to the slot rank.",
        "historical_global_ids": len(global_historical),
        "normative_global_ids": len(global_normative),
        "slot_metrics": slot_metrics,
        "fabricated_reference_total": sum(row["fabricated_reference_count"] for row in case_rows),
        "out_of_context_reference_total": sum(row["out_of_context_reference_count"] for row in case_rows),
    }
    traceability = {
        "version": "he4_traceability_validation_v0.2",
        "definition": "case_id -> H input -> Top-3/evidence -> I raw -> I parsed -> J validation",
        "cases": [
            {
                "case_id": row["case_id"],
                "input_present": row["case_id"] in input_by_case,
                "raw_present": row["case_id"] in raw_by_case,
                "parsed_present": row["case_id"] in parsed_by_case,
                "traceability_complete": bool(row["traceability_complete"]),
            }
            for row in case_rows
        ],
    }
    case_fields = list(case_rows[0])
    slot_fields = [field for field in slot_rows[0] if field != "reference_assertions"]
    _write_csv(out / PHASE_J_FILES[0], case_rows, case_fields)
    _write_csv(out / PHASE_J_FILES[1], slot_rows, slot_fields)
    _write_json(out / PHASE_J_FILES[2], metrics)
    _write_csv(out / PHASE_J_FILES[3], error_rows, ["case_id", "selection_target", "error_type"])
    _write_csv(out / PHASE_J_FILES[4], bucket_rows, ["selection_target", "metric", "numerator", "denominator", "value"])
    _write_json(out / PHASE_J_FILES[5], references)
    _write_json(out / PHASE_J_FILES[6], traceability)
    gate_j = "APPROVED"
    (out / PHASE_J_FILES[8]).write_text(_summary(metrics, gate_j), encoding="utf-8", newline="\n")
    output_hashes = _output_hashes(out)
    large = [{"path": name, "size_bytes": (out / name).stat().st_size} for name in PHASE_J_FILES if (out / name).is_file() and (out / name).stat().st_size > 25 * 1024 * 1024]
    over_50 = [row for row in large if row["size_bytes"] > 50 * 1024 * 1024]
    if over_50:
        raise RuntimeError("Phase J output exceeds 50 MiB; stopped before manifest")
    manifest = {
        "version": "gate_j_automatic_validation_manifest_v0.2",
        "gate_j": gate_j,
        "gate_j_meaning": "Automatic evaluation integrity and reproducibility are approved; individual response failures remain experimental observations.",
        "he4_j": "AUTOMATIC CONTROLS",
        "he4_global_status": "PENDING QUALITATIVE EVALUATION - FASE K",
        "phase_k_executed": False,
        "exp10_executed": False,
        "deterministic_offline": True,
        "no_model_calls": True,
        "no_retrieval": True,
        "input_hashes": input_hashes,
        "raw_and_parsed_unchanged_after_j": {key: input_hashes[key]["pass"] for key in ("raw_responses", "parsed_responses")},
        "metrics": metrics,
        "output_sha256": output_hashes,
        "outputs_over_25_mib": large,
        "outputs_over_50_mib": over_50,
        "manifest_self_hash_excluded": True,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    _write_json(out / PHASE_J_FILES[7], manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic EXP-04 HE4 Phase J automatic controls.")
    parser.parse_args()
    manifest = run()
    print(json.dumps({"gate_j": manifest["gate_j"], "cases": manifest["metrics"]["cases"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
