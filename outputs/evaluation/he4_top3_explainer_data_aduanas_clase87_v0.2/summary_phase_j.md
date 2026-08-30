# EXP-04 Fase J - Controles automaticos HE4 v0.2

- Gate J: `APPROVED`.
- La validacion es deterministica y offline; no regenera ni modifica respuestas de Fase I.
- HE4 global permanece pendiente de evaluacion cualitativa de Fase K.

## Metricas por caso

| Control | Resultado |
| --- | ---: |
| raw_json_parse_rate | 50/50 (1.0000) |
| parsed_raw_identity_rate | 50/50 (1.0000) |
| schema_compliance_rate | 0/50 (0.0000) |
| candidate_set_closure_rate | 50/50 (1.0000) |
| top3_order_preservation_rate | 50/50 (1.0000) |
| rank_consistency_rate | 50/50 (1.0000) |
| external_code_free_rate | 50/50 (1.0000) |
| missing_candidate_free_rate | 50/50 (1.0000) |
| duplicate_candidate_free_rate | 50/50 (1.0000) |
| historical_reference_validity_rate | 50/50 (1.0000) |
| normative_reference_validity_rate | 50/50 (1.0000) |
| fabricated_reference_free_rate | 50/50 (1.0000) |
| out_of_context_reference_free_rate | 50/50 (1.0000) |
| required_fields_completeness_rate | 0/50 (0.0000) |
| comparison_presence_rate | 50/50 (1.0000) |
| warnings_field_compliance_rate | 50/50 (1.0000) |
| traceability_completeness_rate | 50/50 (1.0000) |
| explicit_label_leakage_free_rate | 50/50 (1.0000) |

## Metricas por slot

| Control | Resultado |
| --- | ---: |
| candidate_code_valid_rate | 150/150 (1.0000) |
| rank_consistent_rate | 150/150 (1.0000) |
| historical_reference_valid_rate | 150/150 (1.0000) |
| normative_reference_valid_rate | 150/150 (1.0000) |

## Regla historica agregada

- Cumplimiento de los umbrales congelados: `True`.
- No existia una regla pre-generacion de PASS/FAIL por caso; por ello no se calcula tasa de automatic_validation_pass.
