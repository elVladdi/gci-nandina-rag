# D-051 — Experimental Design B02 / Section 4.3 opening

```text
DECISION_ID = D-051
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
PARENT_DECISION = D-050
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_3 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Motivo de apertura

D-050 integró Experimental Design B01 y promovió `ARTICLE_MASTER_V010` como master canónico. Cumplido ese gate, la IA Gestora reconstruyó independientemente el ground truth de `4.3 Documentary corpus and evidence resource` antes de autorizar nueva redacción.

La revisión gobernante es:

`article/reviews/5_EXPERIMENTAL_DESIGN_B02_SECTION4_3_GROUND_TRUTH_REVIEW_V01.md`

Su dictamen es `PASS_FOR_ATOMIC_DRAFTING_GATE`.

## 2. Alcance atómico autorizado

Se autoriza exclusivamente redactar y materializar:

- Part I English: `4.3 Documentary corpus and evidence resource`;
- Part II Spanish semantic-control mirror: `4.3 Corpus documental y recurso de evidencia`.

No se autoriza modificar el contenido científico congelado de Sections 1–4.2.3. No se autoriza redactar 4.4 ni posteriores. No se autoriza Results, Discussion, Conclusion, FINAL_GAP ni novelty.

El bloque debe partir de `ARTICLE_MASTER_V010.md` y del DOCX canónico exacto bajo custodia local del autor.

## 3. Ground truth científico congelado para B02

### 3.1 Recurso documental primario

La ruta experimental integrada que alimentó Phase F/HE4 usó como recurso de evidencia un **corpus NANDINA jerárquico derivado de la Decisión 885 de la Comisión de la Comunidad Andina**.

El corpus contiene representación jerárquica de la nomenclatura de la fuente procesada. La evaluación empírica sigue delimitada por los candidatos Chapter 87 generados upstream por el banco histórico.

```text
PRIMARY_EXPLANATION_EVIDENCE_RESOURCE = HIERARCHICAL_NANDINA_CORPUS_DERIVED_FROM_DECISION_885
CORPUS_DOCUMENTARY_SCOPE = FULL_NANDINA_HIERARCHY_FROM_FROZEN_SOURCE
EMPIRICAL_CANDIDATE_SCOPE = CHAPTER_87_INSTANCE
```

### 3.2 Operación documental primaria

En la instanciación ejecutada, la asociación de evidencia se realiza mediante **lookup directo del código NANDINA-8 de cada candidato del Top-3 fijo**.

```text
PRIMARY_EVIDENCE_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_IN_PRIMARY_PHASE_F = false
DOCUMENTARY_STAGE_MAY_RERANK = false
DOCUMENTARY_STAGE_MAY_INSERT_OR_SUBSTITUTE_CANDIDATES = false
FALLBACK_TO_ANOTHER_CODE_IF_EXACT_RECORD_MISSING = false
PARENT_CONTEXT_IS_CONTEXT_NOT_EXACT_EVIDENCE = true
```

La terminología arquitectónica genérica de “documentary/normative evidence retrieval” no debe inducir a afirmar que la instanciación primaria realizó BM25 o búsqueda de texto libre sobre el corpus normativo. Section 4.3 debe describir la configuración realmente ejecutada.

### 3.3 Preparación y representación

El recurso conserva, cuando están disponibles, niveles de sección, capítulo, partida de cuatro dígitos, subpartida HS de seis dígitos y subpartida NANDINA de ocho dígitos, además de descripciones, unidad física y procedencia textual. La jerarquía puede emplearse como contexto downstream, pero no convierte automáticamente un texto parental en evidencia exacta de otra subpartida.

Los conteos de composición del corpus pueden incorporarse únicamente si mejoran la descripción metodológica y permanecen claramente como caracterización del recurso, no como resultados de desempeño.

### 3.4 Autoridad y frontera temporal

Queda congelado para este bloque:

```text
DECISION_885_AUTHORITY = COMMISSION_OF_THE_ANDEAN_COMMUNITY
DECISION_885_EFFECTIVE = 2022-01-01
DECISION_906 = MODIFICATION_OF_DECISION_885_NANDINA
DECISION_906_PUBLICATION = GOAC_5062 / 2022-10-25
DECISION_906_EFFECTIVE = 2023-01-01
PRIMARY_PHASE_F_HE4_CORPUS = DECISION_885_DERIVED / FROZEN
PRIMARY_PHASE_F_HE4_CORPUS_RETROACTIVELY_REPLACED_BY_906 = false
TEMPORAL_VERSION_MISMATCH_RELATIVE_TO_2026_CASES = DISCLOSE
```

La Decisión 906 actualizó la nomenclatura antes del periodo de los casos administrativos de 2026. Section 4.3 debe declarar con precisión que el recurso congelado usado por la ruta primaria deriva de Decision 885 y que, por ello, existe una limitación de vigencia/versionado respecto del escenario 2026.

La línea correctiva posterior basada en Decision 906 no reescribe retroactivamente qué corpus consumieron Phase F/HE4. Sus efectos cuantitativos pertenecen a Results/robustness y no se anticipan en 4.3.

### 3.5 Recursos no autorizados como contexto primario de explicación

No se ha establecido para este gate que el contexto primario de HE4 haya consumido Arancel de Aduanas 2022, resoluciones de clasificación u otros corpora más amplios disponibles en el repositorio.

```text
ARANCEL_2022_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
CLASSIFICATION_RESOLUTIONS_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
BROADER_CORPUS_RAG_FAMILY_AS_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
```

## 4. Fronteras de interpretación

Permanecen vinculantes:

- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- el Top-3 fijo no puede ser alterado downstream;
- el LLM explica candidatos fijados y no clasifica desde cero;
- no se afirma que el corpus Decision-885-derived estuviera actualizado a la normativa vigente en 2026;
- no se afirma generalización de desempeño fuera de Chapter 87.

## 5. Regla editorial de Methods

La prosa publicable debe identificar fuente, autoridad, versión temporal, preparación/representación y procedimiento de asociación de evidencia a un nivel suficiente para reproducir el experimento conceptualmente.

No deben trasladarse al cuerpo del artículo, salvo necesidad científica excepcional:

- SHA-256;
- rutas de repositorio;
- nombres físicos de archivos o scripts;
- labels internos de configuración/experimento;
- inventarios técnicos de índices.

La identidad técnica exhaustiva queda en reproducibility resources/manifests.

## 6. Fuentes técnicas primarias requeridas para ejecución

La IA de Redacción debe verificar directamente, como mínimo:

- `src/configs/historical_normative_integration_v0.2.json`;
- `src/configs/he4_pre_explainer_v0.2.json`;
- `src/corpus/build_hierarchical_nandina_corpus.py`;
- `data/processed/corpus/nandina/run_metadata.json`;
- `data/processed/corpus/nandina/summary.csv`;
- `src/experiments/build_llm_explanation_top3_sample.py` y/o `build_llm_explanation_top3_audit_sample.py`;
- `SRC-03` vivo para comprobar que no exista una decisión posterior que cambie materialmente estos hechos.

Para autoridad y vigencia normativa, D-051 congela los hechos oficiales verificados por la IA Gestora. Si la IA de Redacción consulta las fuentes oficiales, no puede reemplazar por inferencia la versión efectivamente usada en el experimento.

## 7. Gate operativo

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
NEXT_ACTOR = DRAFTING_AI
AUTHORIZED_SCOPE = SECTION_4_3_ONLY_ENGLISH_PLUS_SPANISH_MIRROR
BASELINE_MASTER = ARTICLE_MASTER_V010
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

La apertura no equivale a aprobación de la futura redacción. Todo entregable B02 deberá ser auditado independientemente por la IA Gestora y, cuando corresponda, aprobado por el autor antes de integración.
