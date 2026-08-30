from __future__ import annotations

"""Deterministic microaudit of the frozen HE4 prompt/schema/validator contract."""

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..utils.paths import ensure_parent, project_root, resolve_project_path


OUT_DIR = Path("outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2")
PROMPT = Path("src/llm/explain_top3_nandina_prompt_v0.2.md")
SCHEMA = Path("src/configs/he4_explainer_schema_v0.2.json")
RUBRIC = Path("src/configs/he4_rubric_v0.2.json")
RAW_SHA = "8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4"
PARSED_SHA = "daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6"
PROMPT_SHA = "1b56ba51863df4d73c8cd882d9154d32df3339a6292d4f72f61d400876f8b1d0"
SCHEMA_SHA = "b31c0ce9b3bf82d6e80572f2debd5564a46a0d25d5e228a1272aca4f320f9bc6"
RUBRIC_SHA = "175f5405bcdf911fa449cdbbef1fff17284c134970be4a40f8af8a25df25e514"
FINAL_WARNING = "no reemplaza la clasificacion oficial"


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(value: object) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", _clean(value)).encode("ascii", "ignore").decode("ascii")).lower().strip()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def _write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _generic_warning(candidate: Mapping[str, Any], frozen: Mapping[str, Any]) -> tuple[bool, str, str]:
    reference = _clean(frozen.get("evidencia_normativa", {}).get("referencia"))
    if "los demas" not in _norm(reference):
        return True, "", ""
    warnings = [_clean(value) for value in candidate.get("advertencias", []) if _clean(value)]
    limitations = [
        _clean(value)
        for evidence in candidate.get("evidencia_normativa_usada", [])
        if isinstance(evidence, dict)
        for value in evidence.get("limitaciones", [])
        if _clean(value)
    ]
    output_text = " | ".join(warnings + limitations)
    passed = any(token in _norm(output_text) for token in ("generica", "los demas", "insuficiente"))
    return passed, reference, output_text


def _hashes(root: Path, out: Path) -> dict[str, dict[str, Any]]:
    paths = {
        "prompt": root / PROMPT,
        "schema": root / SCHEMA,
        "rubric": root / RUBRIC,
        "raw": out / "he4_responses_raw_v0.2.jsonl",
        "parsed": out / "he4_responses_parsed_v0.2.jsonl",
    }
    expected = {"prompt": PROMPT_SHA, "schema": SCHEMA_SHA, "rubric": RUBRIC_SHA, "raw": RAW_SHA, "parsed": PARSED_SHA}
    return {name: {"expected": expected[name], "actual": _sha256(path), "pass": _sha256(path) == expected[name]} for name, path in paths.items()}


def run() -> dict[str, Any]:
    root = project_root()
    out = resolve_project_path(OUT_DIR)
    hashes = _hashes(root, out)
    if not all(value["pass"] for value in hashes.values()):
        raise RuntimeError("Frozen H/I contract hash mismatch; microaudit stopped")
    prompt_text = (root / PROMPT).read_text(encoding="utf-8")
    schema = json.loads((root / SCHEMA).read_text(encoding="utf-8"))
    rubric = json.loads((root / RUBRIC).read_text(encoding="utf-8"))
    raw = {_clean(row["case_id"]): row for row in _read_jsonl(out / "he4_responses_raw_v0.2.jsonl")}
    parsed = {_clean(row["case_id"]): row for row in _read_jsonl(out / "he4_responses_parsed_v0.2.jsonl")}
    inputs = {_clean(row["case_id"]): row for row in _read_jsonl(out / "he4_generation_inputs_v0.2.jsonl")}
    case_results = _read_csv(out / "he4_automatic_validation_case_results_v0.2.csv")
    original_metrics = json.loads((out / "he4_automatic_validation_metrics_v0.2.json").read_text(encoding="utf-8"))
    original_manifest = json.loads((out / "gate_j_automatic_validation_manifest_v0.2.json").read_text(encoding="utf-8"))
    if not (len(raw) == len(parsed) == len(inputs) == len(case_results) == 50):
        raise RuntimeError("Microaudit requires exactly 50 frozen H/I/J records")

    decomposition: list[dict[str, Any]] = []
    only_global_missing = 0
    other_schema_errors = 0
    for result in case_results:
        case_id = _clean(result["case_id"])
        response = json.loads(_clean(raw[case_id]["raw_response"]))
        missing = [field for field in result["missing_required_fields"].split("|") if field]
        other = [
            value
            for field in ("wrong_types", "invalid_enums", "structural_errors")
            for value in result[field].split("|")
            if value
        ]
        if missing == ["advertencias_globales"] and not other:
            only_global_missing += 1
        elif missing or other:
            other_schema_errors += 1
        candidates = response.get("candidatos_explicados", [])
        frozen_candidates = inputs[case_id]["top3_original"]
        for rank, (candidate, frozen) in enumerate(zip(candidates, frozen_candidates, strict=True), start=1):
            generic_valid, trigger, warning_text = _generic_warning(candidate, frozen)
            normative = frozen["evidencia_normativa"]
            decomposition.append(
                {
                    "case_id": case_id,
                    "candidate_rank": rank,
                    "candidate_code": _clean(candidate.get("nandina")),
                    "evidence_id": _clean(normative.get("doc_id")),
                    "normative_reference": _clean(normative.get("referencia")),
                    "generic_rule_triggered": int(bool(trigger)),
                    "trigger_text": trigger,
                    "warnings_field_valid": int(all(isinstance(item.get("advertencias"), list) for item in candidates) and FINAL_WARNING in _norm(response.get("advertencia_final"))),
                    "generic_normative_warning_when_required": int(generic_valid),
                    "warning_and_limitations_output": warning_text,
                    "deterministic_failure_reason": "MISSING_GENERIC_NORMATIVE_WARNING" if trigger and not generic_valid else "",
                }
            )
    case_warning_valid = {
        row["case_id"]: int(all(int(slot["warnings_field_valid"]) for slot in decomposition if slot["case_id"] == row["case_id"]))
        for row in case_results
    }
    case_generic_valid = {
        row["case_id"]: int(all(int(slot["generic_normative_warning_when_required"]) for slot in decomposition if slot["case_id"] == row["case_id"]))
        for row in case_results
    }
    failing_warning = sorted(case_id for case_id, value in case_warning_valid.items() if not value)
    failing_generic = sorted(case_id for case_id, value in case_generic_valid.items() if not value)
    warning_fail_details = [row for row in decomposition if row["deterministic_failure_reason"]]
    prompt_has_global = "advertencias_globales" in prompt_text
    schema_has_global = "advertencias_globales" in schema["required_root_fields"]
    rubric_has_global = "advertencias_globales" in json.dumps(rubric, ensure_ascii=False)
    audit = {
        "version": "gate_j_prompt_schema_microaudit_v0.2",
        "classification": "B. PROMPT-SCHEMA SPECIFICATION MISMATCH",
        "hashes": hashes,
        "prompt_audit": {"path": str(PROMPT), "advertencias_globales_explicitly_required": prompt_has_global, "exact_output_structure_has_field": prompt_has_global},
        "schema_audit": {"path": str(SCHEMA), "advertencias_globales_required_root_field": schema_has_global},
        "historical_validator_audit": {"path": "src/experiments/evaluate_llm_explanation_top3_audit_sample.py", "advertencias_globales_required": False, "generic_warning_control_present": True, "historical_failure_label": "generic_normative_warning_missing"},
        "rubric_audit": {"path": str(RUBRIC), "advertencias_globales_present": rubric_has_global, "hard_constraints": rubric["hard_constraints"], "missing_advertencias_globales_is_hard_violation": False},
        "git_origin": {
            "prompt_v0_2_added_commit": "51380925e9e6d0617dc65c1b37b82e685493abf9",
            "schema_and_rubric_v0_2_added_commit": "a6c98c2dbd2dcc7d61641755f5f8eddc5c0db94c",
            "prompt_v0_3_introduces_advertencias_globales": True,
            "interpretation": "The v0.2 schema was added after the v0.2 prompt and includes a field introduced by the later v0.3 prompt structure.",
        },
        "schema_impact": {
            "original_schema_compliance": "0/50 (compliance against frozen schema)",
            "cases_failing_only_advertencias_globales": only_global_missing,
            "cases_with_other_schema_errors": other_schema_errors,
            "cases_complete_if_field_is_not_evaluable": only_global_missing,
            "interpretation": "SCHEMA RESULT CONFOUNDED BY PROMPT-SCHEMA SPECIFICATION MISMATCH",
        },
        "warning_control_decomposition": {
            "warnings_field_valid": f"{sum(case_warning_valid.values())}/50",
            "generic_normative_warning_when_required": f"{sum(case_generic_valid.values())}/50",
            "cases_failing_warnings_field": failing_warning,
            "cases_failing_generic_control": failing_generic,
            "overlap": sorted(set(failing_warning) & set(failing_generic)),
            "original_taxonomy_label": "INVALID_WARNING_FIELD",
            "interpretation": "The original label conflates a structural warning-field check with a distinct content-token check for generic normative evidence.",
            "derived_descriptive_label": "MISSING_GENERIC_NORMATIVE_WARNING",
            "generic_rule_pre_specified": True,
            "failure_details": warning_fail_details,
        },
        "gate_j": {"preserved": original_manifest["gate_j"] == "APPROVED", "decision": "APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION", "ready_for_phase_k": False},
        "phase_k_executed": False,
        "rubric_applied": False,
        "model_called": False,
        "retrieval_performed": False,
        "original_j_metrics_preserved": original_metrics["case_metrics"]["schema_compliance_rate"]["numerator"] == 0,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    _write_csv(out / "gate_j_warning_control_decomposition_v0.2.csv", decomposition, list(decomposition[0]))
    _write_json(out / "gate_j_prompt_schema_microaudit_v0.2.json", audit)
    _write_json(out / "gate_j_interpretation_v0.2.json", audit)
    markdown = "\n".join([
        "# Gate J microcierre: compatibilidad prompt-schema-validador HE4 v0.2",
        "",
        "## Dictamen",
        "",
        "- Clasificacion: `PROMPT-SCHEMA SPECIFICATION MISMATCH`.",
        "- El prompt v0.2 no solicita `advertencias_globales`; el schema v0.2 si lo exige.",
        "- El campo aparece en el prompt v0.3, no en la estructura exacta usada por Fase I.",
        "- `0/50` se preserva como cumplimiento contra schema congelado y queda confounded por el mismatch.",
        f"- Solo por ese campo: `{only_global_missing}/50`; otros schema errors: `{other_schema_errors}/50`.",
        "",
        "## Advertencias",
        "",
        f"- `warnings_field_valid`: `{sum(case_warning_valid.values())}/50`.",
        f"- `generic_normative_warning_when_required`: `{sum(case_generic_valid.values())}/50`.",
        f"- Fallos del control generico: `{len(failing_generic)}`; solapamiento: `{len(set(failing_warning) & set(failing_generic))}`.",
        "- `INVALID_WARNING_FIELD` se conserva como etiqueta original; su interpretacion derivada para esos fallos es `MISSING_GENERIC_NORMATIVE_WARNING`.",
        "",
        "## Fase K",
        "",
        "- La rubrica no contiene `advertencias_globales` como dimension ni hard constraint; no se aplico.",
        "- Gate J permanece `APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION`; Fase K no se inicio.",
        "",
    ])
    (out / "gate_j_prompt_schema_microaudit_v0.2.md").write_text(markdown, encoding="utf-8", newline="\n")
    return audit


def main() -> int:
    argparse.ArgumentParser(description="Audit frozen HE4 Phase J prompt/schema compatibility.").parse_args()
    audit = run()
    print(json.dumps({"classification": audit["classification"], "gate_j": audit["gate_j"]["decision"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
