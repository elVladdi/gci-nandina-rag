# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.0 / SECTION_4_REDESIGN_PENDING
LATEST_EDITORIAL_DECISION = D-044
STRUCTURE_STATUS = SECTION_4_REOPENED_FOR_CONCEPTUAL_REVIEW
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED_WITH_TWO_BACKWARD_DEPENDENCIES_FLAGGED_FOR_LATER_AMENDMENT
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = SECTION_4_CONCEPTUAL_REAUDIT
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
PREVIOUS_KBS34_4_2_CORRECTION_PROMPT = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021: el DOCX acumulativo aprobado permanece bajo custodia local exacta del autor y se identifica por SHA-256.
- D-022: prompts y respuestas operativas sustantivas de la IA de Redacción se versionan en GitHub; el chat conserva solo el puntero mínimo.
- D-023: los cierres técnicos no reabren revisión científica y no usan mecanismos redundantes de transferencia.
- D-027: la custodia local exige entrega efectiva del binario exacto al autor.
- D-034: Architecture y Experimental Design pueden redactarse bajo gates editoriales propios sin que Group 6 bloquee por sí mismo esos bloques.
- D-035: handoff timeout-safe para artefactos acumulativos grandes; no Base64 manual, fragmentación/chunking, recomposición ni reintentos de la vía grande que ya falló.
- D-037: Architecture B01 integrada y V008 promovido.
- D-038: Architecture B02 abierta.
- D-039: Architecture B02 aprobada por el autor y V009 autorizado.
- D-040: Architecture B02 integrada; Section 3 cerrada; `ARTICLE_MASTER_V009` promovido a master canónico.
- D-041: Experimental Design B01 fue abierto originalmente para 4.1 y 4.2.1–4.2.4.
- D-042: la primera versión corregida de B01 fue aprobada por el autor, pero su integración no llegó a materializarse.
- D-043: la aprobación/integración de V010 fue suspendida al detectarse exceso de SHA, rutas y nombres de artefactos en 4.2.
- D-044: la observación se amplió a toda Section 4; la sección completa queda reabierta para revisión conceptual y el prompt correctivo limitado a 4.2 queda superado.

La codificación interna automática de una API/conector no constituye Base64 manual.

### Secciones cerradas

- Related Work 2.1–2.6: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Introduction B01: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Decision-support architecture 3.1–3.7: `CLOSED / APPROVED / FROZEN / INTEGRATED`, con dos dependencias editoriales hacia Section 4 registradas para enmienda coordinada después del rediseño de Section 4; la arquitectura científica no se reabre por ese motivo.

El master canónico permanece en `ARTICLE_MASTER_V009.md`. No existe `ARTICLE_MASTER_V010` materializado.

### Arquitectura científica congelada

```text
commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ candidate-specific documentary/normative evidence retrieval
→ evidence-context construction
→ local LLM
→ controlled explanation of the fixed Top-3
```

La recuperación histórica genera y ordena candidatos. El Top-3 se fija antes de etapas downstream. La recuperación documental/normativa asocia evidencia sin insertar, eliminar, sustituir ni reordenar candidatos. El LLM local explica el Top-3 fijo y no clasifica desde cero ni retroalimenta el ranking. El reranking LLM permanece diagnóstico y fuera del flujo principal.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

### Section 4 — observación conceptual vigente

La Section 4 completa está observada. El problema identificado no se limita a detalles de trazabilidad técnica. La revisión debe corregir el objeto narrativo de Methods y reorganizar la sección alrededor de la evaluación experimental offline de una instanciación concreta de la arquitectura.

La nueva estructura deberá establecer, antes de redactar nuevos bloques:

1. qué instanciación experimental se evaluó y bajo qué alcance;
2. cómo se obtuvieron, prepararon y curaron el banco histórico y el corpus documental/normativo;
3. cómo se construyeron las particiones y se controlaron dependencia, leakage, duplicados y near-duplicates;
4. cómo se configuraron y ejecutaron los componentes de la arquitectura;
5. cómo se evaluó cada función/RQ y con qué métricas/protocolos;
6. qué análisis estadísticos y de sensibilidad están autorizados;
7. qué recursos de reproducibilidad se ponen a disposición, sin convertir la prosa principal en un inventario de SHA, rutas o nombres internos de artefactos.

La formulación «piloto no vinculante de apoyo a decisiones» no debe gobernar 4.1. El experimento evalúa la arquitectura/procedimiento; una futura herramienta de apoyo a decisiones es una posible aplicación posterior. El verbo preferido es `evaluar`, conforme al objetivo aprobado, no `validar` salvo soporte epistémico adicional.

La reinstanciación con otros bancos históricos, espacios de clases, profundidades arancelarias, jurisdicciones o corpus compatibles puede describirse como configurabilidad/replicación metodológica, nunca como transferencia empírica demostrada.

### Gate vigente

```text
CURRENT_GATE = SECTION_4_CONCEPTUAL_REAUDIT
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = RECONSTRUCT_AND_AUDIT_SECTION_4_STRUCTURE_BEFORE_ANY_DRAFTING_PROMPT
CANONICAL_MASTER = ARTICLE_MASTER_V009
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
DRAFTING_AI_PROMPT = NONE_AUTHORIZED
PREVIOUS_PROMPT_5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION = DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.0 / SECTION_4_REDESIGN_PENDING
LATEST_EDITORIAL_DECISION = D-044
STRUCTURE_STATUS = SECTION_4_REOPENED_FOR_CONCEPTUAL_REVIEW
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED_WITH_TWO_BACKWARD_DEPENDENCIES_FLAGGED_FOR_LATER_AMENDMENT
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = SECTION_4_CONCEPTUAL_REAUDIT
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
PREVIOUS_KBS34_4_2_CORRECTION_PROMPT = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

D-044 broadens the previous 4.2-specific correction into a complete conceptual reopening of Section 4. The current framing partly conflates the experiment with a future decision-support tool and gives internal artifact traceability too much authority over the publication-facing Methods narrative.

The complete Section 4 must be redesigned around the offline experimental evaluation of a concrete architecture instantiation: scope, resource acquisition/preparation, partition and dependence controls, system configuration/execution, evaluation protocols, authorized analysis, and reproducibility resources. SHA values, internal repository paths and filenames are not the organizing principle of Methods and belong in manifests/reproducibility resources unless methodologically indispensable.

The architecture itself remains scientifically frozen. Two backward-facing sentences in Section 3 that anticipate hashes/artifact identities in Section 4 are flagged for coordinated editorial amendment only after the revised Section 4 organization is approved.

Configurability to other historical banks, class spaces, tariff depths, jurisdictions, or compatible corpora is a design/re-instantiation property and must not be stated as empirical performance transfer.

### Current gate

```text
CURRENT_GATE = SECTION_4_CONCEPTUAL_REAUDIT
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = RECONSTRUCT_AND_AUDIT_SECTION_4_STRUCTURE_BEFORE_ANY_DRAFTING_PROMPT
CANONICAL_MASTER = ARTICLE_MASTER_V009
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
DRAFTING_AI_PROMPT = NONE_AUTHORIZED
PREVIOUS_PROMPT_5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION = DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
