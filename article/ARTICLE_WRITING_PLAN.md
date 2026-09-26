# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.3
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-052
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_AUTHORIZED_BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_3 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado completa esa base y solo se vuelve canónico después de auditoría independiente, aprobación autoral cuando corresponda e integración técnica verificada.

La redacción se rige por `KBS_EWG_34_V01`, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, decisiones activas, literatura primaria verificada cuando corresponda y fuentes experimentales gobernantes para todo hecho empírico.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- Secuencia narrativa: problema/posicionamiento → arquitectura general → instanciación experimental → resultados → interpretación.
- El objeto general es un **framework configurable para apoyo auditable a la clasificación arancelaria**.
- La arquitectura de Section 3 es el núcleo técnico del framework.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la etapa documental y generativa.
- La evidencia documental/normativa se asocia a candidatos ya fijados y no cambia composición ni orden.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero ni retroalimenta el ranking.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive normative correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de análisis; DAM/declaración es unidad de agrupamiento cuando la dependencia entre series es metodológicamente relevante.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es el manuscript principal en inglés; Part II es el espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, entradas, acciones, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

### 2.1 Regla específica de Methods

Methods describe objetos científicos, procedencia, procedimientos, decisiones de diseño, ejecución, protocolos de evaluación y controles de validez. La identidad técnica exhaustiva de artefactos pertenece al repositorio/manifiestos de reproducibilidad salvo que un identificador concreto sea metodológicamente indispensable.

La prosa principal no se organiza alrededor de SHA-256, rutas internas, nombres físicos de archivos/scripts, nombres de hojas o labels internos de configuración.

## 3. Estructura acumulativa

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion + Limitations
7. Conclusion
8. KBS end matter

La estructura detallada gobernante es `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, aprobada mediante D-045.

### 3.1 Section 4 aprobada

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

## 4. Política del master acumulativo y DOCX

1. Cada bloque parte del último master aprobado e integrado.
2. Master Markdown canónico: `ARTICLE_MASTER_V010.md`, SHA-256 `82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8`, Git blob `8dc09fb841162005b2155491735336b0e70187c6`.
3. DOCX canónico correspondiente: `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx`, custodia local efectiva del autor, SHA-256 `4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae`, 40 comentarios heredados y 0 tracked changes en la auditoría aprobada.
4. D-021/D-027 gobiernan custodia local binaria; D-035 gobierna handoff timeout-safe.
5. No se reconstruye DOCX desde Markdown.
6. No Base64 manual, chunking, recomposición ni workarounds de transferencia.
7. Los bloques nuevos preservan exactamente las secciones/comentarios ya aprobados salvo alcance explícitamente reabierto.
8. Un master candidato no se vuelve canónico hasta superar auditoría, aprobación e integración aplicables.
9. D-052 identificó un metadato residual en el encabezado de V010: aún figura `KBS_ARTICLE_WORKING_STRUCTURE_V01`. V010 no se edita retroactivamente; el siguiente master acumulativo candidato debe actualizar ese rótulo a V02 sin alterar contenido científico fuera del alcance autorizado.

## 5. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Structure V02 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Experimental Design B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V010.md` |
| Experimental Design B02 / 4.3 | **OPEN / AUTHORIZED_FOR_DRAFTING** |
| Sections 4.4–4.8 | NOT_AUTHORIZED |
| Experimental figures/captions from Group 6 | CLOSED / APPROVED externally; EDITORIAL_INTEGRATION_DEFERRED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Los grupos experimentales no se administran aquí. `SRC-03` se consulta en modo de solo lectura cuando una afirmación o gate editorial depende materialmente de ellos.

## 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED; Section 4 amended by D-045 |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5A | Experimental Design B01 — 4.1 + 4.2.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5B | 4.3 Documentary corpus and evidence resource | **ACTIVE / AUTHORIZED** |
| 5C | 4.4 Partition validity and dependence controls | NOT_AUTHORIZED until 5B closes/integrates |
| 5D | 4.5 Experimental system configuration and execution | later atomic gate |
| 5E | 4.6 Evaluation framework and protocols | later atomic gate |
| 5F | 4.7 Statistical and robustness analysis | later atomic gate |
| 5G | 4.8 Reproducibility resources | later atomic gate |
| 6 | Results provisional | Experimental Design sufficiently stable + editorial gate + consumable evidence |
| 7 | Integración editorial de figuras experimentales ya aprobadas | Group 6 CLOSED / APPROVED; insertar solo cuando Results/material secundario correspondiente esté abierto |
| 8 | Final Results | Results provisional + recursos visuales/tabulares autorizados + auditoría editorial |
| 9 | Discussion + Limitations | final Results + authorized literature contrast |
| 10 | Conclusion | Discussion closed |
| 11 | Abstract | complete manuscript |
| 12 | Title + Keywords | Abstract/manuscript complete |
| 13 | Transversal synchronization | according to live external dependencies |
| 14 | Scientific audit/freeze | after synchronization and required audits |
| 15 | Final KBS adaptation | scientific freeze + current submission requirements |

**Fase 7 ya no es una fase de producción científica de figuras.** Grupo 6 produjo y aprobó tres figuras/captions experimentales. El trabajo editorial futuro consiste en seleccionar su destino final autorizado e insertarlas sin alterar métricas, claims, escalas, captions científicos o incertidumbre congelada.

`Figure 1` de Section 3.1 sigue siendo una figura arquitectónica distinta y no queda cubierta por Grupo 6.

## 7. Concurrencia con el proceso experimental

Solo la IA Experimental administra `SRC-03` y el Plan Maestro experimental. La IA Gestora y la IA de Redacción lo consultan en solo lectura.

No se congela aquí un snapshot permanente del estado experimental: antes de cada bloque que dependa de hechos experimentales se consulta la rama viva `docs/plan-maestro-temporal-2026-08-31` y se determina si un cambio posterior altera materialmente los hechos que pretende consumir el artículo.

Último corte sincronizado por D-052:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Este avance externo no modifica el gate editorial local. Ningún avance experimental autoriza por sí mismo Results, Discussion o el freeze científico final.

## 8. Fase activa — Experimental Design B02 / Section 4.3

### 8.1 Alcance autorizado

Solo:

- Part I: `4.3 Documentary corpus and evidence resource`;
- Part II: `4.3 Corpus documental y recurso de evidencia`.

No modificar Sections 1–4.2.3. No redactar 4.4+.

### 8.2 Función narrativa

4.3 debe explicar la **instanciación concreta** de la capa documental definida genéricamente en Architecture. Debe identificar el recurso documental realmente usado, su autoridad y temporalidad, su preparación/representación y el mecanismo real de asociación de evidencia a los candidatos ya fijados.

No debe repetir toda Architecture ni presentar inventarios técnicos del repositorio.

### 8.3 Ground truth congelado

D-051 y `article/reviews/5_EXPERIMENTAL_DESIGN_B02_SECTION4_3_GROUND_TRUTH_REVIEW_V01.md` gobiernan el bloque:

```text
PRIMARY_EVIDENCE_RESOURCE = HIERARCHICAL_NANDINA_CORPUS_DERIVED_FROM_DECISION_885
PRIMARY_EVIDENCE_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_IN_PRIMARY_PHASE_F = false
DOCUMENTARY_STAGE_RERANKING = false
CANDIDATE_INSERTION = false
CANDIDATE_SUBSTITUTION = false
FALLBACK_TO_ANOTHER_CODE = false
PARENT_CONTEXT_IS_CONTEXT_NOT_EXACT_EVIDENCE = true
CORPUS_SCOPE = NANDINA_HIERARCHY_FROM_FROZEN_SOURCE
EMPIRICAL_CANDIDATE_SCOPE = CHAPTER_87_INSTANCE
DECISION_885_EFFECTIVE = 2022-01-01
DECISION_906_MODIFIES_885_EFFECTIVE = 2023-01-01
PRIMARY_PHASE_F_HE4_CORPUS_RETROACTIVELY_REPLACED_BY_906 = false
TEMPORAL_VERSION_MISMATCH_RELATIVE_TO_2026_CASES = DISCLOSE
```

La evidencia documental de la ruta primaria se asocia mediante lookup exacto del código NANDINA-8 de cada candidato del Top-3 ya fijado. La formulación genérica `documentary/normative evidence retrieval` de Architecture no debe convertirse en una afirmación falsa de BM25/query search sobre el corpus para la instanciación primaria.

La fuente documental es supranacional andina; no debe llamarse “Peruvian normative corpus” si ello atribuye autoridad nacional peruana al recurso derivado de Decision 885. El contexto administrativo de los casos sí es peruano.

### 8.4 Frontera temporal

Decision 885 fue el snapshot documental consumido por la ruta primaria. Decision 906 modificó esa NANDINA y entró en vigencia antes de los casos 2026. El manuscrito debe revelar esta condición como limitación de versión/temporalidad.

No se debe afirmar:

- que el corpus primario estaba actualizado a la normativa 2026;
- que Decision 906 alimentó retroactivamente HE4/Phase F;
- que todos los códigos Chapter 87 usados quedaron necesariamente modificados o incorrectos;
- resultados cuantitativos de la corrección posterior.

### 8.5 Recursos fuera del contexto primario no demostrados

Hasta evidencia primaria en contrario, no atribuir al contexto final de explicación:

- Arancel de Aduanas 2022;
- resoluciones de clasificación;
- corpora RAG más amplios presentes en el repositorio.

### 8.6 Transferencia y entregables

Patrón D-035:

- section MD pequeño: GitHub;
- response pequeña: GitHub;
- master Markdown acumulativo candidato: adjunto exacto al autor + SHA-256;
- DOCX acumulativo candidato: adjunto exacto al autor + SHA-256;
- no Base64 manual, chunking, recomposición o reconstrucción del DOCX.

El próximo master acumulativo candidato debe además corregir el rótulo estructural residual V01→V02 identificado en D-052 y preservar 40 comentarios, 0 tracked changes y render integral aprobado.

## 9. Ciclo obligatorio

```text
IA Gestora reconstruye estado/evidencia
→ abre/versiona bloque y prompt
→ IA de Redacción ejecuta solo el bloque
→ entrega artefactos y response versionada
→ IA Gestora audita independientemente claim por claim
→ corrección si corresponde
→ PASS
→ aprobación expresa del autor cuando aplique
→ IA Gestora integra/promueve técnicamente
→ abre el siguiente gate solo si queda habilitado
```

## 10. Estado inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ONLY_B02_SECTION_4_3_PROMPT
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B02_DOCUMENTARY_CORPUS_EVIDENCE_RESOURCE.md
PROMPT_STATUS = VALID / UNCHANGED_BY_D052
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
BASELINE_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
BASELINE_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
NEXT_CANDIDATE_STRUCTURE_LABEL_CORRECTION = V01_TO_V02_METADATA_ONLY
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Governing frame

The article remains a cumulative KBS Research Article under author-approved Structure V02. Related Work, Introduction, Architecture, and Experimental Design B01 are closed and integrated. `ARTICLE_MASTER_V010.md` remains the canonical manuscript master.

Methods describe scientific objects, provenance, procedures, design choices, execution, evaluation protocols, and validity controls. Exhaustive artifact identity belongs in reproducibility resources rather than the main narrative unless scientifically indispensable.

D-052 synchronized the live external state without reopening scientific prose. Group 6 is now closed/approved and supplies three approved experimental figures/captions for future editorial integration. Group 7 is in progress, with G7-F01 closed and G7-F02 active. Neither change opens Results or alters the current B02 gate.

## 2. Active block

Experimental Design B02 remains limited to Section 4.3 and its Spanish semantic-control mirror. The verified primary evidence resource is the hierarchical NANDINA corpus derived from Andean Community Decision 885.

The primary integrated path associates evidence through **exact NANDINA-8 code lookup** for each already fixed Top-3 candidate. It does not perform query-based normative retrieval, reranking, score fusion, candidate insertion, or candidate substitution.

Decision 906 modified Decision 885 and became effective before the 2026 administrative scenario. The primary path nevertheless consumed the frozen Decision-885-derived resource. This version boundary must be disclosed without implying that every Chapter-87 record was necessarily changed or invalid and without anticipating corrective robustness results.

## 3. Immediate gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
NEXT_ACTOR = DRAFTING_AI
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B02_DOCUMENTARY_CORPUS_EVIDENCE_RESOURCE.md
PROMPT_STATUS = VALID / UNCHANGED_BY_D052
BASELINE_MASTER = ARTICLE_MASTER_V010
NEXT_CANDIDATE_STRUCTURE_LABEL_CORRECTION = V01_TO_V02_METADATA_ONLY
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
