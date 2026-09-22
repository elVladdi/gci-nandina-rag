# PREG8-001 — Preflight no gobernante para G8-F01/G8-F02

## 0. Naturaleza

Este artefacto adelanta únicamente el diseño de auditoría futura. No activa Grupo 8, no audita un candidato final inexistente, no modifica tesis/artículo, no cierra discrepancias y no sustituye los outputs formales de G8.

Precondición formal aún no cumplida:

```text
GROUP7 = NOT_CLOSED
G8-F01 = PROSPECTIVE / NOT_AUTHORIZED
```

---

## 1. Objetivo

Transformar los riesgos ya identificados en Grupos 3–6 y en PREG7-001/PREG7-002 en un contrato de checks reutilizable cuando existan candidatos finales de tesis y artículo.

---

## 2. Esquema futuro de G8-F01

Cada claim material deberá tener como mínimo:

```text
document_id
section_id
claim_instance_id
controlled_claim_id
claim_text_observed
claim_type
primary_source_path
primary_source_commit_or_blob
canonical_table_id
canonical_figure_id
expected_numeric_value_or_rule
observed_numeric_value
uncertainty_level
population_N
DAM_N
condition_name
superseded_source_detected
mandatory_qualification
forbidden_overclaim
status
correction_required
```

Estados propuestos para la auditoría formal:

```text
PASS
PASS_WITH_QUALIFICATION
MISMATCH_NUMERIC
MISMATCH_SCOPE
MISMATCH_UNCERTAINTY
SUPERSEDED_SOURCE
OVERCLAIM
NOT_TRACEABLE
NOT_APPLICABLE
```

---

## 3. Checks numéricos prioritarios G8-F01

### G8-PRE-001 — Población evaluada

```text
EXPECTED:
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
```

Todo `1006`, `59 DAM`, `62 NANDINA` u otro denominador legacy debe justificarse explícitamente como snapshot histórico o corregirse.

### G8-PRE-002 — HE2_A

- exactamente cinco métricas primarias: Top-1, Top-3, Top-5, Top-10, MRR@100;
- tres comparadores corregidos: Flat, Hierarchical, D1a;
- 15 contrastes;
- estimando `Historical − comparator`;
- CI congelado 99%;
- ningún CI por brazo;
- Top-50 fuera del rol decisional primario.

### G8-PRE-003 — HE2_B

- un contraste primario: `Recall@200 − Recall@100`;
- CI congelado 95%;
- Recall@100 = 0.1013257576;
- Recall@200 = 0.3039772727;
- diferencia = 0.2026515152;
- CI95 = [0.0667631058, 0.3416013079];
- Pool@200 nunca como segundo contraste confirmatorio.

### G8-PRE-004 — Phase E

- descriptivo solamente;
- cuatro variantes formales G3C-005;
- 70/30 solo contexto;
- diagnostic union separado;
- sin CI/p-values/contrastes inferenciales.

### G8-PRE-005 — HE5

```text
HE5 = INCONCLUSIVE
DESCRIPTION = NOT_ESTIMABLE
HIERARCHY = DESCRIPTIVE_ONLY
PRECEDENT_SUPPORT = DESCRIPTIVE_ONLY / NO_INSUFFICIENCY_THRESHOLD
INTERNAL_VALIDITY = DOCUMENTED_LIMITATION
```

Conteos jerárquicos permitidos:

```text
SAME_CHAPTER = 147
SAME_HS4 = 284
SAME_HS6 = 87
```

Buckets exactos:

```text
1 DAM
2 DAM
3-4 DAM
5+ DAM
```

No permitir etiquetas retrospectivas `insufficient`, `low support`, `2-4`, `10+` como si fueran categorías congeladas.

### G8-PRE-006 — EXP11A

- sensibilidad conjunta tamaño/composición;
- no causal;
- 31 corridas observadas si se representa la figura;
- H25 10 / H50-D1 5 / H50-D2 5 / H75 10 / H100 ref. 1;
- no superponer summaries como nueva evidencia.

### G8-PRE-007 — EXP11B

- diez pares de seeds observados;
- mismo EVAL de 1056;
- sin superpoblación de seeds;
- no pseudorreplicar `10×1056`.

### G8-PRE-008 — 0B-05C

Únicamente Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
overall = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Prohibido resumir como impacto global cero.

### G8-PRE-009 — EXP12

```text
CLOSED_WITHOUT_RETRIEVAL
D-HIGH/D-MID/D-LOW = NOT_SELECTED
DIVERSITY_EFFECT = NOT_ESTIMABLE
```

Prohibido: global infeasibility, seed counterfactuals, HE5 positive/negative evidence.

---

## 4. Checks metodológicos G8-F02

### G8-PRE-M01 — Unidad y dependencia

Toda sección debe distinguir:

```text
SERIE = unidad de análisis/observación
DAM/DECLARACION = unidad de agrupamiento/dependencia cuando corresponde
```

### G8-PRE-M02 — Partición

La metodología final debe describir el benchmark v0.2 y no limitarse a “identificadores no repetidos”. El control de DAM debe ser coherente con el análisis inferencial.

### G8-PRE-M03 — Arquitectura

Secuencia obligatoria:

```text
descripción comercial
→ normalización
→ recuperación histórica
→ ranking histórico Top-k
→ Top-3 fijo
→ evidencia normativa
→ constructor de contexto
→ LLM local
→ explicación auditable Top-3
```

Normativa no reordena. LLM no clasifica desde cero ni modifica candidatos. Reranker permanece diagnóstico.

### G8-PRE-M04 — Métodos vs resultados

Ningún resultado final puede usar una población, configuración, fuente o métrica diferente de la declarada en Methods salvo que se identifique como sensibilidad/anexo.

### G8-PRE-M05 — Results vs Discussion

Discussion puede interpretar solo claims aprobados por G4 y puntos autorizados por G4-F03. No puede añadir mecanismo causal, novedad absoluta, SOTA, superioridad cross-study ni legal correctness.

### G8-PRE-M06 — Tablas/figuras/texto

- las cifras del texto deben coincidir con G5;
- las figuras deben coincidir con G6 cerrado;
- captions no pueden añadir claims;
- MAIN/SECONDARY/APPENDIX/TEXT_ONLY debe preservarse.

### G8-PRE-M07 — Reproducibilidad

Conservar explícitamente limitaciones G2B-L01..L11 y no convertir `HASH_BOUND_LOCAL_ONLY` en missing/invalid ni `DECLARED_NOT_RECOVERABLE` en error experimental.

---

## 5. Registro anticipado de outputs superseded/prohibidos

Como mínimo deberán detectarse automáticamente o por revisión:

```text
- Attempts01–05 de 0B-05C para interpretación actual
- candidato G5-F02 v01 superseded
- métricas/particiones legacy N=1006 de la tesis previa, salvo contexto histórico explícito
- reranker legacy de 20 casos si se presenta como resultado final sin fuente vigente
- cualquier figura legacy fuera del catálogo G6 aprobado, salvo figura conceptual independiente y gobernada
- EXP12 forensic diagnostic promovido a resultado gobernante
```

---

## 6. Riesgos ya materializados en la tesis preauditada

```text
R001 legacy EVAL_N=1006
R002 legacy historical metrics 0.8628/0.9374/0.9801/0.9062
R003 HE2 provisional instead of SUPPORTED
R004 HE5 partially supported instead of INCONCLUSIVE
R005 obsolete support buckets and low-support inference
R006 ambiguous/incomplete description prevalence inference despite NOT_ESTIMABLE
R007 normative runs still described as pending repetition
R008 legacy hybrid integration figure/result outside current G6 presentation contract
R009 Top-k wording drifting toward global accuracy
R010 thesis/article experimental snapshot divergence
```

---

## 7. Freeze-readiness criteria prepared for G8-F03

La futura decisión `APPROVED_FOR_SCIENTIFIC_FREEZE` debe exigir simultáneamente:

```text
G3–G7 = CLOSED / APPROVED
OPEN_BLOCKING_CLAIMS = 0
OPEN_NUMERIC_MISMATCHES = 0
OPEN_SCOPE_MISMATCHES = 0
OPEN_SUPERSEDED_SOURCE_USES = 0
OPEN_FIGURE/TABLE_MISMATCHES = 0
UNDECLARED_POSTHOC_ANALYSES = 0
FINAL_COMMITS_AND_HASHES_AVAILABLE = true
HISTORICAL_LIMITATIONS_VISIBLE = true
THESIS_ARTICLE_SCIENTIFIC_STATE_ALIGNED = true
```

---

## 8. Estado del preflight

```text
PREG8_001_RESULT = READY_AS_AUDIT_BLUEPRINT
FORMAL_G8_AUTHORIZED = false
FORMAL_G8_EXECUTED = false
FINAL_DOCUMENTS_AUDITED = false
NEW_SCIENCE = false
```

Este blueprint deberá ser actualizado después del cierre G6 y G7 para incorporar los commits finales, captions definitivos, candidato de tesis y candidato editorial del artículo.
