# Revisión interna del prompt — Results B02 / Section 5.2 — V01

## Español

```text
REVIEW_TYPE = IA_GESTORA / PROMPT_INTERNAL_REVIEW
PROMPT = article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f
PROMPT_GIT_BLOB = 0fd0aa40419b248e5983f0cb445c187e92a4bc13
GROUND_TRUTH = D-092
CANONICAL_MASTER = ARTICLE_MASTER_V017
VERDICT = PASS
CORRECTIONS_REQUIRED = NONE
```

## 1. Alcance

El prompt abre exclusivamente §5.2 — Candidate retrieval performance y mantiene cerradas §5.3–§5.7, Discussion y Conclusion. La frontera diferencial es compatible con el master V017 y con la estructura congelada de Results.

## 2. Fidelidad del ground truth

Se verificó que el prompt reproduce correctamente los valores congelados por D-092 para los cuatro métodos sobre EVAL=1,056:

- historical BM25 H100;
- flat normative BM25 corregido;
- hierarchical normative BM25 corregido;
- D1a Text2Trade-inspired MNRL.

Top-1/3/5/10, Top-50 y MRR@100 coinciden con los cuatro artefactos métricos primarios congelados. La deep coverage jerárquica también conserva exactamente Recall@100=107/1056 y Recall@200/Pool@200=321/1056.

## 3. Separación descriptiva/inferencial

El prompt mantiene correctamente fuera de B02:

- bootstrap e intervalos de confianza;
- diferencias inferenciales historical-minus-comparator;
- disposición `HE2 = SUPPORTED`;
- inferencia HE2_B;
- sensibilidades y HE5.

Por tanto, §5.2 queda como reporte descriptivo de candidate retrieval/ranking performance, mientras §5.6 conserva la función inferencial definida por la estructura vigente.

## 4. Límites de interpretación

El prompt prohíbe correctamente interpretar Top-k/MRR como overall classification accuracy, corrección normativa, corrección jurídica, SOTA, generalización externa o desempeño operacional. También conserva la condición de que los comparadores no sustituyen la fuente histórica de candidatos del pipeline primario.

## 5. MWDP / D-035

```text
BASELINE_MD = ARTICLE_MASTER_V017 / EXACT IDENTITY REQUIRED
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx / EXACT IDENTITY REQUIRED
DOCX_RECONSTRUCTION_FROM_MD = PROHIBITED
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
REAL_FILE_HANDOFF = REQUIRED
```

La lista de QA cubre diff de sección, preservación del resto del master, equivalencia EN/ES, comentarios, tracked changes, integridad OOXML, render completo y handoff timeout-safe.

## 6. Dictamen

```text
SCIENTIFIC_SCOPE = PASS
GROUND_TRUTH_FIDELITY = PASS
RESULTS_VS_INFERENCE_BOUNDARY = PASS
CLAIM_CONTROL = PASS
MWDP = PASS
D035 = PASS
OVERALL_VERDICT = PASS
RESULTS_B02_EXECUTION_AUTHORIZATION = MAY_BE_ISSUED
```

---

## English

The B02 prompt faithfully implements D-092, limits drafting to §5.2, preserves the descriptive/inferential separation, freezes the exact four metric sources and V017/B01 DOCX baselines, and enforces MWDP/D-035. Verdict: `PASS`; execution authorization may be issued.