# Revisión interna — Results B01 / Section 5.1 — V01

## Español

```text
REVIEW = 6_RESULTS_B01_SECTION5_1_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = IA_GESTORA
BLOCK = RESULTS_B01_SECTION_5_1
DELIVERY_RESPONSE = article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md@6796dd29f3c530e91c463a207aea9e9dd8e9d187
GOVERNING_PROMPT = article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e
GROUND_TRUTH = D-087
EXECUTION_AUTHORIZATION = D-088
VERDICT = PASS
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_RESULTS_B01_V01_ONLY
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Identidad de artefactos

IA Gestora verificó independientemente los archivos entregados al autor:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
GIT_BLOB_EXPECTED_FROM_BYTES = 35edb134f3d060bad4257d314cf415d9ecf17b6c

ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
```

Las identidades coinciden con la response versionada.

El artefacto pequeño de sección fue verificado en GitHub:

```text
article/sections/results/Results_B01_V01.md
COMMIT = 28948cad188b7ad79ab44b6b9e19b90e659e5f1d
GIT_BLOB = 5566b70bef1c201e8f0269a0e2fbd5306f014d0c
```

## 2. Auditoría diferencial del Markdown

La comparación byte/textual entre `ARTICLE_MASTER_V016` y el candidato B01 muestra cambios exclusivamente en el placeholder de §5.1 de Part I English y su espejo semántico de Part II Spanish.

No se modificaron Sections 1–4.8. Los placeholders de §5.2–§5.7, Discussion, Conclusion y end matter permanecen sin redacción científica nueva.

```text
SECTION_5_1_ONLY_DIFF = PASS
SECTIONS_1_TO_4_8_PRESERVED = PASS
SECTIONS_5_2_PLUS_PRESERVED = PASS
NO_SCOPE_EXPANSION = PASS
```

## 3. Auditoría científica claim-by-claim

IA Gestora reconsultó directamente las dos fuentes congeladas en `main@db0d0ad0d8435921a7838db6720eaea86a263763`:

```text
SOURCE_A = data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
GIT_BLOB = bcb02c9c3493235a6f80991158c5b24fa7c04510

SOURCE_B = outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json
GIT_BLOB = fb21eb0d8ef77cdedaa32698b854595629ed526d
```

La §5.1 coincide con el ground truth congelado:

- benchmark v0.2: 4,106 SERIE totalmente asignadas;
- H100 = 2,950 SERIE / 28 DAM / 66 códigos representados;
- DEV = 100 / 6 / 9;
- EVAL = 1,056 / 67 / 42;
- solapamiento cross-partition de DAM = 0 y de `id_unico` = 0 en los tres pares;
- soporte histórico nominal = 1,056/1,056 SERIE EVAL y 42/42 códigos EVAL;
- duplicados exactos H100–EVAL = 35/1,056 (3.31%), 34 same-NANDINA y 1 different-NANDINA, con `same_dam_rows=0`;
- near-duplicates H100–EVAL: 55 filas (5.21%; 82 pares) a Jaccard ≥0.90; 44 (4.17%; 46 pares) a ≥0.95; 37 (3.50%; 38 pares) a ≥0.98.

La redacción mantiene correctamente las fronteras interpretativas: soporte nominal no equivale a Top-k; separación por DAM no equivale a independencia i.i.d.; similitud residual no se convierte en estimación de efecto; y no se introducen claims de legal correctness, accuracy global ni generalización externa.

```text
GROUND_TRUTH_FIDELITY = PASS
NO_RETRIEVAL_PERFORMANCE_LEAKAGE = PASS
NO_INFERENTIAL_RESULT_LEAKAGE = PASS
NO_HE2_HE5_DISPOSITION_LEAKAGE = PASS
NO_DISCUSSION_LEAKAGE = PASS
NO_LEGAL_CORRECTNESS_CLAIM = PASS
NO_EMPIRICAL_GENERALIZATION_CLAIM = PASS
```

## 4. Equivalencia EN/ES

Los cinco párrafos científicos de §5.1 presentan equivalencia semántica EN/ES. Conteos, denominadores, porcentajes, thresholds y límites interpretativos se conservan.

```text
EN_ES_EQUIVALENCE = PASS
```

## 5. Auditoría DOCX / OOXML

Comparación contra el binario canónico B07 V02:

```text
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CANDIDATE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
ZIP_ENTRY_SET = 14 / 14 PRESERVED
CHANGED_PACKAGE_PARTS = word/document.xml ONLY
COMMENTS_XML = BYTE_IDENTICAL
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
COMMENT_IDS = 0..39 / UNIQUE
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

El diff de párrafos OOXML muestra exactamente dos reemplazos lógicos: el placeholder inglés de §5.1 por cinco párrafos y el placeholder español por cinco párrafos. No se detectaron cambios científicos fuera del bloque autorizado.

El texto científico de MD y DOCX es semánticamente equivalente en ambos idiomas.

## 6. QA visual

IA Gestora renderizó de nuevo el DOCX completo. El candidato produce 52 páginas frente a 51 del baseline, aumento esperable por la incorporación de §5.1. Se inspeccionaron las 52 páginas renderizadas.

```text
FULL_DOCX_RENDER = PASS / 52 OF 52
NO_CLIPPING = PASS
NO_OVERLAP = PASS
NO_TRUNCATION = PASS
NO_BROKEN_TABLES = PASS
NO_MATERIAL_FORMAT_LOSS = PASS
```

## 7. D-035

Los candidatos acumulativos fueron entregados como archivos reales. No se observó Base64 manual, chunking, fragmentación ni reensamblado, y el master grande no fue materializado directamente en GitHub.

```text
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO
CHUNKING = NO
FRAGMENTATION = NO
REASSEMBLY = NO
```

## 8. Dictamen

```text
OVERALL_VERDICT = PASS
RESULTS_B01_V01 = SCIENTIFICALLY_AND_EDITORIALLY_READY_FOR_AUTHOR_REVIEW
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_RESULTS_B01_V01_ONLY
RESULTS_B02_PLUS = NOT_AUTHORIZED
```

No se requiere corrección previa al gate autoral.

---

## English

Managing-AI independent audit of Results B01 V01 is PASS. The cumulative MD changes only §5.1 in the English master and Spanish semantic-control mirror; all frozen observations match the two controlling v0.2 aggregate sources. No retrieval-performance, inferential, HE2/HE5, Discussion, legal-correctness, or external-generalization claim leaked into the block. The DOCX preserves all 14 OOXML package entries, 40 comments, zero tracked changes, and changes only `word/document.xml`. Full 52-page render QA passed. Results B01 V01 may proceed to author review only; §5.2+ remains closed.