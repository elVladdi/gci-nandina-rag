# Revisión interna del prompt — Results B01 / Section 5.1 — V01

## Español

```text
REVIEW_TYPE = PROMPT_INTERNAL_REVIEW
BLOCK = RESULTS_B01_SECTION_5_1
PROMPT = article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e
PROMPT_GIT_BLOB = a0f4005e8c406574d39b5540dfbf676f3d4acc0d
GROUND_TRUTH_DECISION = D-087@22a63fa715ae2c7bddb92af06d65c417f257932b
VERDICT = PASS
```

## 1. Auditoría de alcance

El prompt autoriza únicamente Section 5.1 — Data and partition checks. Conserva cerradas Sections 5.2–5.7, Discussion, Conclusion, `FINAL_GAP` y `NOVELTY`. No existe autorización implícita para continuar a otro bloque.

## 2. Auditoría de fuentes y cifras

Las dos fuentes agregadas exigidas corresponden al snapshot experimental congelado `db0d0ad0d8435921a7838db6720eaea86a263763`:

- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`, Git blob `bcb02c9c3493235a6f80991158c5b24fa7c04510`;
- `outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json`, Git blob `fb21eb0d8ef77cdedaa32698b854595629ed526d`.

Las cifras congeladas del prompt coinciden con ambos artefactos: 4,106 series asignadas; H100 2,950/28/66; DEV 100/6/9; EVAL 1,056/67/42; cero solapamiento DAM e `id_unico`; soporte histórico nominal 1,056/1,056 y 42/42; 35 duplicados exactos H100–EVAL; y diagnósticos near-duplicate 55/44/37 filas a umbrales 0.90/0.95/0.98 respectivamente.

## 3. Auditoría de interpretación

El prompt separa correctamente:

- separación de DAM/identificadores frente a similitud textual residual;
- soporte histórico nominal frente a desempeño Top-k;
- resultados descriptivos de partición frente a inferencia;
- candidate retrieval frente a overall classification accuracy;
- Results frente a Discussion.

No autoriza claims de i.i.d., ausencia total de similitud, legal correctness, generalización externa ni causalidad.

## 4. Continuidad acumulativa y Word

Los baselines exigidos son exactamente los canónicos vigentes:

```text
ARTICLE_MASTER_V016.md
SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40
TRACKED_CHANGES = 0
```

El prompt prohíbe reconstrucción DOCX desde Markdown y exige modificación diferencial únicamente del placeholder §5.1 EN/ES.

## 5. D-035

La política timeout-safe queda explícita y suficiente: Base64 manual, chunking, fragmentación y reensamblado están prohibidos; no debe intentarse materialización directa del master acumulativo grande mediante GitHub; MD/DOCX deben entregarse como archivos reales al autor.

## 6. Dictamen

```text
SCIENTIFIC_SCOPE = PASS
SOURCE_IDENTITY = PASS
NUMERICAL_GROUND_TRUTH = PASS
CLAIM_BOUNDARIES = PASS
RESULTS_DISCUSSION_SEPARATION = PASS
CUMULATIVE_BASELINES = PASS
DOCX_CONTINUITY_REQUIREMENTS = PASS
D035 = PASS
PROMPT_VERDICT = PASS
EXECUTION_AUTHORIZATION_MAY_BE_ISSUED = YES / B01 ONLY
```

---

## English

The Results B01 prompt passes internal review. It is restricted to Section 5.1, uses the exact frozen v0.2 aggregate sources and canonical V016/B07-V02 baselines, preserves the distinction between partition separation and residual textual similarity, and prohibits leakage of retrieval-performance, inferential, HE2/HE5, Discussion, legal-correctness, and external-generalization claims. D-035 timeout-safe handoff is explicit. Execution may be authorized for B01 only.