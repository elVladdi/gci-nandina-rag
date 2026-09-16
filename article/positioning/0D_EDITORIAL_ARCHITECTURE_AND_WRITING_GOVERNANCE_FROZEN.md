# 0D — Arquitectura editorial y gobernanza pre-redacción — FROZEN / Editorial Architecture and Pre-Drafting Governance — FROZEN

## Español

### 1. Estado

```text
0D = CLOSED / APPROVED / FROZEN
0D1 = CLOSED / APPROVED / FROZEN
0D2 = CLOSED / APPROVED / FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D2_V02_INTERNAL_REVIEW = PASS
0D_AUTHOR_APPROVAL = RECEIVED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Este artefacto congela conjuntamente la arquitectura editorial aprobada de 0D-1 y la gobernanza pre-redacción aprobada de 0D-2. Los artefactos analíticos V02 y sus revisiones conservan el detalle; este archivo funciona como estado canónico de transferencia hacia Fase 1.

### 2. Arquitectura del artículo

#### 1. Introduction

- 1.1 Problem and pilot scope
- 1.2 State-of-the-art limitation and positioning
- 1.3 Provisional contribution and Research Questions

La Introduction se redactará después de que Methods, Related Work y resultados disponibles estén suficientemente estables.

#### 2. Related Work

- 2.1 HS classification and candidate retrieval
- 2.2 RAG, agents and regulatory reasoning
- 2.3 Explainability, source support and auditability
- 2.4 Validity, provenance and reproducibility
- 2.5 Positioning synthesis

#### 3. Methods

- 3.1 Design, scope and units
- 3.2 Data, corpora, versioning and curation
- 3.3 v0.2 partitioning and dependence controls
- 3.4 Historical retrieval and Top-k / fixed Top-3
- 3.5 Post-ranking normative retrieval
- 3.6 Candidate–evidence integration and invariance
- 3.7 Local LLM and controlled explanation
- 3.8 Function-specific evaluation design
- 3.9 Validity, normative drift and reproducibility

#### 4. Results

- 4.1 Benchmark and split controls
- 4.2 Historical candidate retrieval / RQ1
- 4.3 Normative retrieval and integration / RQ2
- 4.4 Controlled explanation / RQ3
- 4.5 Sensitivities and documentary validity
- 4.6 Inferential validity / RQ4 — `BLOCKED_BY_GROUP3`
- 4.7 EXP-11B, si se integra — `BLOCKED_BY_C10_C11_RECONCILIATION`

#### 5. Discussion

- 5.1 Meaning of the functional contract
- 5.2 Comparison with prior art
- 5.3 Decision-support implications
- 5.4 Validity and transferability

La Discussion permanece bloqueada hasta disponer de Results definitivos; 5.4 depende además de Grupo 3.

#### 6. Limitations

- 6.1 Benchmark and data limitations
- 6.2 HE4 and auditability limitations
- 6.3 Normative drift
- 6.4 Reproducibility and external-validity limits

Conclusions, Abstract y Title definitivo se redactan en fases tardías conforme a `ARTICLE_WRITING_PLAN.md`.

### 3. Figuras y tablas

Mapa congelado de planificación:

- Figure 1 — arquitectura: ranking histórico fijo → evidencia normativa sin reranking → explicación del Top-3 inmutable sin feedback; terminología `architectural/functional separation`, nunca separación causal.
- Table 1 — benchmark H100/DEV/EVAL.
- Table 2 — componente → tarea → output → métrica → interpretación permitida/prohibida.
- Table 3 — H100 Top-k/MRR.
- Table 4 — recuperación normativa, asociación 3168/3168, trazabilidad y preservación de ranking.
- Table 5 — HE4.
- Table 6 — drift/overlap/sensibilidad de 0B-05C.
- Table 7 — comparación de literatura, opcional.
- Figure 2 — mapa de validez, opcional.
- Table 8 — Grupo 3, esencial cuando el experimento aplicable cierre.
- Table 9 — EXP-11B solo tras reconciliar C10/C11 y decidir su integración.
- Figure 3 — sensibilidad por tamaño/composición: no recomendada en el estado actual.

### 4. Contrato científico preservado

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Flujo canónico:

`Descripción comercial → normalización → recuperación histórica → ranking histórico Top-k → Top-3 fijo → evidencia normativa para esos candidatos → construcción de contexto → LLM local → explicación auditable`.

### 5. Journal targeting y condiciones editoriales

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
```

El núcleo científico debe escribirse de manera transferible entre A/B/C. Los requisitos KBS aún no verificables desde fuente primaria accesible no se inventan. Se revalidarán antes del paquete final de submission.

### 6. Gobernanza obligatoria para Fase 1 en adelante

Gobierna:

`article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0 / FROZEN`.

La IA de Redacción debe leerlo íntegramente en cada bloque. Un prompt de bloque puede ser más restrictivo, pero no puede omitir o debilitar reglas acumulativas del protocolo.

Se preservan especialmente:

- master acumulativo `.md` + `.docx`;
- Word interno bilingüe;
- APA 7 provisional solo en Word;
- Mendeley final por el autor;
- comentarios de auditoría anclados a cada cita inglesa;
- recuperación full-text claim por claim;
- versionado `BLOCK_REVISION`, `MASTER_CANDIDATE_REVISION`, `MASTER_INTEGRATION`;
- no reconstrucción silenciosa del Word desde cero;
- claim–evidence y anti-overclaiming;
- revisión experimental únicamente cuando exista trigger.

### 7. Dependencias que 0D no elimina

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

El freeze de 0D no convierte condiciones científicas pendientes en resultados cerrados.

---

## English

### 1. Status

```text
0D = CLOSED / APPROVED / FROZEN
0D1 = CLOSED / APPROVED / FROZEN
0D2 = CLOSED / APPROVED / FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D2_V02_INTERNAL_REVIEW = PASS
0D_AUTHOR_APPROVAL = RECEIVED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

This artifact jointly freezes the approved 0D-1 editorial architecture and approved 0D-2 pre-drafting governance. Detailed V02 responses/reviews remain authoritative for analysis; this file is the canonical transfer state into Phase 1.

### 2. Article architecture

The frozen modular architecture is: Introduction (problem/scope; state-of-the-art limitation/positioning; provisional contribution/RQs); Related Work (HS classification/candidate retrieval; RAG/agents/regulatory reasoning; explainability/source support/auditability; validity/provenance/reproducibility; positioning synthesis); Methods (design/scope/units; data/corpora/versioning/curation; v0.2 partitioning/dependence controls; historical Top-k/fixed Top-3; post-ranking normative retrieval; candidate–evidence integration/invariance; local-LLM controlled explanation; function-specific evaluation; validity/drift/reproducibility); Results aligned to benchmark/RQ1/RQ2/RQ3/sensitivity/RQ4, with RQ4 blocked by Group 3 and EXP-11B blocked by C10/C11 reconciliation; Discussion deferred until final Results; and Limitations covering benchmark/data, HE4/auditability, normative drift, and reproducibility/external validity. Conclusions, final Abstract, and final Title are late-stage outputs.

### 3. Figures and tables

The planning map includes Figure 1 for the fixed historical ranking → non-reranking normative evidence → immutable-Top-3 explanation/no-feedback architecture using `architectural/functional separation`, never causal separation; Tables 1–6 for benchmark/component-role/H100/normative/HE4/drift evidence; optional literature Table 7 and validity Figure 2; essential post-Group-3 Table 8; EXP-11B Table 9 only after reconciliation/inclusion; and no current recommendation for the size/composition sensitivity Figure 3.

### 4. Preserved scientific contract

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Canonical flow: commercial description → normalization → historical retrieval → historical Top-k → fixed Top-3 → candidate-specific normative evidence → context construction → local LLM → auditable explanation.

### 5. Journal targeting and editorial conditions

Target A is Knowledge-Based Systems; Plan B is Expert Systems with Applications; Plan C is Information Processing & Management. Research article is the operational type. KBS-specific template and final reference style remain unverified; neutral-master and provisional-APA7 policies apply. The scientific core must remain transferable among A/B/C, and still-unverified KBS submission requirements must be revalidated before final submission.

### 6. Binding Phase-1+ governance

`article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0 / FROZEN`) governs every block. Writing AI must read it in full each time. Block prompts may be stricter but may not omit or weaken cumulative rules. The paired cumulative Markdown/Word masters, bilingual Word, provisional Word-only APA7, author-controlled final Mendeley, citation-anchored audit comments, claim-level full-text re-retrieval, explicit revision semantics, no silent Word reconstruction, claim–evidence controls, and conditional Experimental-AI trigger remain mandatory.

### 7. Dependencies preserved

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

Freezing 0D does not turn pending scientific conditions into closed results.
