# Fase 1 — Methods B01 — Revisión V02 / Closed Revision Prompt

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Corrige exclusivamente la entrega `Methods B01 — Design, scope, and units` V01. No avances a B02 ni a ninguna otra sección.

Usa como punto de control editorial el HEAD `18817325ecd46c1ddc27a2cc76052e20676d5f0a` y lee íntegramente, además del onboarding/MWDP obligatorio:

- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`;
- `article/ARTICLE_STATUS.md`;
- `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`;
- `article/sections/methods/Methods_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`;
- el `SRC-03` vivo indicado en `SOURCE_REGISTRY.md`;
- este prompt.

El estado experimental correcto para este corte es `GROUP3 = NOT_STARTED`. No uses resultados ni inferencias de Grupo 3.

### Correcciones obligatorias y exclusivas

#### B01-M01 — Sustituir lenguaje de gobernanza interna

Eliminar de la prosa publicable la formulación `governing study artifacts` / `artefactos gobernantes del estudio`. Sustituirla por una formulación científica autosuficiente y orientada al lector que delimite el alcance sin mencionar archivos o controles editoriales internos.

No introducir en B01 detalles que correspondan a 3.2–3.9.

#### B01-M02 — Definir correctamente DAM en inglés

En la primera aparición inglesa, no usar simplemente `customs declaration (DAM)`. Debe quedar claro que DAM procede de la denominación administrativa española `Declaración Aduanera de Mercancías`, acompañada por una aclaración inglesa breve y natural. Mantener `DAM` como término operativo posterior.

La versión española mantiene `Declaración Aduanera de Mercancías (DAM)`.

#### B01-M03 — Eliminar el claim positivo de configurabilidad

Eliminar la afirmación positiva `The architecture may be configurable beyond the evaluated setting` y su equivalente español, porque introduce C15 fuera del conjunto de claims autorizado para este bloque.

Mantener únicamente el límite de validez correspondiente: **la evaluación no establece generalización empírica fuera del alcance de Capítulo 87**.

No añadir C15 al checklist. Los únicos claims declarados para B01 siguen siendo:

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
```

### Contenido que debe conservarse

Conservar, salvo ajustes mínimos necesarios para fluidez y equivalencia bilingüe:

- piloto experimental aplicado y offline;
- Capítulo 87 como alcance empírico evaluado;
- apoyo a decisión no vinculante;
- revisión experta fuera del flujo automático;
- historical retrieval = generación/ranking de candidatos;
- normative retrieval = evidencia documental sin sustituir/reordenar el ranking histórico;
- local LLM = explicación downstream del Top-3 fijo, sin clasificación desde cero ni inserción/eliminación/sustitución/reordenamiento/feedback;
- SERIE como unidad de observación/análisis;
- DAM como unidad de agrupamiento cuando la dependencia sea metodológicamente relevante;
- SERIE/descripción comercial normalizada como unidad de consulta;
- historical Top-k y fixed historical Top-3 como objetos de salida correspondientes.

No introduzcas resultados, cifras, métricas, inferencia, causalidad, gap final, novelty, literatura externa ni contenido de B02–B09.

### Citación

Mantener `CITATION_COMMENT_COVERAGE = 0/0`. No añadir literatura externa para resolver estas correcciones.

### Artefactos V02

No sobrescribas ni elimines los artefactos V01. Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V02.md`;
2. `article/sections/methods/Methods_B01_V02.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.docx`.

`ARTICLE_MASTER_CANDIDATE_V02.*` sigue siendo candidato y contiene únicamente B01 revisado. No crees `ARTICLE_MASTER_V001.*`; la integración canónica requiere aprobación del autor.

No modifiques `ARTICLE_STATUS.md`, reviews, prompts, `DECISIONS.md`, `CLAIM_EVIDENCE_MATRIX.md`, literatura congelada ni Plan Maestro.

### Word V02

El `.docx` debe reproducir exactamente el contenido científico de `ARTICLE_MASTER_CANDIDATE_V02.md`, conservar:

- Part I — English manuscript master;
- Part II — Spanish semantic-control mirror;
- layout neutral/reversible y editable;
- cero citas y, por tanto, cero comentarios de cita en este bloque;
- ausencia de Mendeley o campos bibliográficos simulados.

### Checklist de salida

Finaliza con:

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V02
B01_M01 = ADDRESSED
B01_M02 = ADDRESSED
B01_M03 = ADDRESSED
SOURCE_SNAPSHOT(S) = [SHAs realmente leídos]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```

No declares B01 `APPROVED` ni `FROZEN`.

---

## English

Act exclusively as the Writing AI and revise only `Methods B01 — Design, scope, and units` V01. Do not advance to B02 or any other section. Use editorial HEAD `18817325ecd46c1ddc27a2cc76052e20676d5f0a`, read the V01 internal review plus the mandatory onboarding/MWDP artifacts, and preserve `GROUP3 = NOT_STARTED` as the current experimental state.

Apply only the three required corrections:

1. replace internal process wording such as `governing study artifacts` with self-contained manuscript-facing scientific wording;
2. define DAM at first English occurrence through its source administrative name `Declaración Aduanera de Mercancías`, with a brief natural English clarification;
3. remove the positive configurability claim corresponding to C15 and retain only the boundary that empirical generalization beyond Chapter 87 was not evaluated.

Do not broaden the claim set: `AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]`. Preserve the scientific content already accepted in principle, add no results/metrics/inference/literature, and keep citation-comment coverage at `0/0`.

Create only the four V02 artifacts listed in the Spanish section. Do not overwrite V01 or create an approved `ARTICLE_MASTER_V001.*`. The V02 Word candidate must exactly mirror the V02 Markdown scientific content, remain bilingual/editable/neutral, and contain no simulated Mendeley fields. End with the exact checklist above and `DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW`.
