# Revisión interna — Experimental Design B07 / Section 4.8 — V01

## Español

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
DRAFT_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V01.md@c897204c1df5b591ff2c7742c53caa24baaf3b92
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V01.md@c3cc9971f7d2aaebd629b07cad235e8efa3ee526
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
GROUND_TRUTH = D-079
AUTHORIZATION = D-080
VERDICT = PASS
AUTHOR_APPROVAL_GATE = ELIGIBLE_TO_OPEN
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Alcance de la auditoría

Se auditó de forma independiente el contenido científico de Section 4.8, el cumplimiento de D-079/D-080, la procedencia de las afirmaciones sobre el repositorio público de reproducibilidad, el diferencial acumulativo Markdown, la continuidad binaria DOCX, la equivalencia EN/ES, la ausencia de Results leakage y la entrega timeout-safe exigida por D-035 después del timeout previo informado por el autor.

## 2. Fuentes y snapshot público

Se re-verificó `elVladdi/gci-nandina-rag-reproducibility` y se observó nuevamente:

```text
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
DRIFT = NONE / MATERIAL_STATE_UNCHANGED
```

El estado vivo conserva la frontera congelada por D-079: el repositorio público documenta contratos, protocolos, procedencia, taxonomía/corpus y una configuración de ejemplo, pero no materializa todavía una release computacional completa de referencia. La redacción B07 refleja correctamente esa diferencia y no convierte interfaces objetivo en capacidades ya ejecutables.

## 3. Auditoría científica y de claims

```text
C15_CONFIGURABILITY_AS_DESIGN_PROPERTY = PASS
C17_REFERENCE_REPRODUCTION_VS_EXTERNAL_REPLICATION = PASS
C16_EMPIRICAL_GENERALIZATION_OUTSIDE_CH87 = AVOIDED
FULL_REFERENCE_RELEASE_CLAIM = AVOIDED
ONE_COMMAND_FRESH_CLONE_REPRODUCTION = AVOIDED
PUBLIC_ADMINISTRATIVE_REFERENCE_DATA = AVOIDED
LEGAL_CORRECTNESS_FROM_REPRODUCIBILITY = AVOIDED
RESULTS_LEAKAGE = NONE
DISCUSSION_LEAKAGE = NONE
NOVELTY_LEAKAGE = NONE
```

Section 4.8 distingue correctamente: (a) repositorio de desarrollo vs paquete público; (b) recursos materializados vs recursos objetivo/no materializados; (c) reproducción del estudio de referencia vs replicación externa; y (d) artefactos públicos vs entradas restringidas/no redistribuidas. La última frase ata explícitamente la descripción a un snapshot versionado y exige recheck pre-submission.

No se encontraron abstracciones vacías que oculten el estado real del paquete. Las relaciones agente–acción–objeto y las fronteras de disponibilidad están expresadas de forma concreta.

## 4. Equivalencia EN/ES

La versión española conserva la misma fuerza, límites, condiciones y alcance que la inglesa. No se detectó ampliación semántica, atenuación de limitaciones ni generalización adicional.

```text
EN_ES_EQUIVALENCE = PASS
```

## 5. Auditoría del master Markdown candidato

Se verificó localmente contra el baseline B06 V02 exacto:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
BASELINE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
BASELINE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

B07_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
B07_MD_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
B07_MD_GIT_BLOB = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662
```

El diferencial está restringido exclusivamente a los placeholders de Section 4.8 EN/ES. Sections 1–4.7 y todo el contenido desde Results en adelante permanecen byte-semánticamente preservados respecto del baseline acumulativo.

```text
SECTION_4_8_ONLY_MD_DIFF = PASS
SECTIONS_1_TO_4_7_PRESERVED = PASS
RESULTS_PLUS_PRESERVED = PASS
ENGLISH_WORD_COUNT_SECTION_4_8 = 459
```

## 6. Auditoría del DOCX acumulativo

Se verificó contra el binario B06 V02 exacto:

```text
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
B07_DOCX_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
ZIP_ENTRY_SET = 14 / 14 IDENTICAL
ZIP_TEST = PASS
XML_RELS_PARSE = 14 / 14 PASS
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / BYTE_IDENTICAL
TRACKED_CHANGES = 0
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = 51 / 51 PAGES
VISUAL_QA = PASS
```

La inspección visual no mostró clipping, solapamientos, truncamiento, pérdida de encabezados ni degradación material de formato. Los nuevos textos de 4.8 aparecen completos en inglés y español.

## 7. D-035 / entrega timeout-safe

El autor informó que una primera ejecución de B07 cayó en timeout y luego volvió a ejecutar el bloque. La segunda ejecución se auditó bajo D-035.

La comparación del HEAD previo registrado por la respuesta (`a7111d8e30176b3ee59a4888e387107b0be49242`) con la response final muestra únicamente dos archivos añadidos en GitHub: el artefacto pequeño de Section 4.8 y la response. No se materializó el master Markdown acumulativo grande en GitHub, no aparecen chunks/fragmentos/archivos auxiliares y el DOCX tampoco fue subido al repositorio.

Los candidatos exactos fueron entregados al autor como archivos reales y recibidos para esta auditoría. Sus hashes coinciden con la response.

```text
D035_TRIGGERED_BY_PRIOR_TIMEOUT = YES
LARGE_MASTER_DIRECT_GITHUB_TRANSFER = NOT_PERFORMED
MASTER_MD_GITHUB_MATERIALIZATION = DEFERRED
DOCX_GITHUB_UPLOAD = NOT_PERFORMED
BASE64_OR_CHUNK_WORKAROUND = NOT_OBSERVED
AUXILIARY_REASSEMBLY_ARTIFACTS = NONE_OBSERVED
REAL_MD_HANDOFF_TO_AUTHOR = PASS
REAL_DOCX_HANDOFF_TO_AUTHOR = PASS
D027_AUTHOR_CUSTODY = ESTABLISHED_FOR_B07_CANDIDATES
TIMEOUT_SAFE_DELIVERY = PASS
```

No existe motivo para invalidar la segunda ejecución por el timeout previo; la ruta de entrega adoptada es consistente con D-035.

## 8. Dictamen

```text
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE = PASS
SOURCE_SNAPSHOT = PASS
REPRO_STATUS_BOUNDARY = PASS
PUBLIC_RESTRICTED_BOUNDARY = PASS
PRESENT_PLANNED_BOUNDARY = PASS
EN_ES_EQUIVALENCE = PASS
MD_DIFFERENTIAL = PASS
DOCX_CONTINUITY = PASS
OOXML_INTEGRITY = PASS
VISUAL_QA = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
OVERALL_VERDICT = PASS
```

No se requieren correcciones a B07 V01. El bloque es elegible para abrir exclusivamente el gate de aprobación autoral. Esta revisión no integra B07, no promueve un nuevo master y no autoriza Results.

---

## English

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
VERDICT = PASS
AUTHOR_APPROVAL_GATE = ELIGIBLE_TO_OPEN
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The independent audit confirms that B07 V01 accurately describes the currently materialized reproducibility resources and their limitations. The live public repository still matches D-079 (`main@254831cd955103faa2517065a7eed7fb340bbccc`, tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`). The text preserves C15 only as a design-configurability claim, uses C17 correctly, and avoids C16 and unsupported claims of a complete runnable reference release, one-command fresh-clone reproduction, public administrative reference data, legal correctness, or empirical generalization.

The cumulative Markdown differs from the exact B06 V02 baseline only in Section 4.8 EN/ES. The B07 DOCX derives from the exact B06 V02 binary; all 14 OOXML entries are preserved, only `word/document.xml` changed, all 40 inherited comments and anchors remain intact, tracked changes remain zero, Markdown/DOCX semantics agree, and the complete 51-page render passes visual QA.

The prior timeout reported by the author activates D-035. The second execution complied with the timeout-safe path: the large cumulative Markdown was not materialized through GitHub, the DOCX was not uploaded there, no chunk/Base64/reassembly workaround is observed in the repository delta, and the exact MD/DOCX candidates were handed to the author as real files with matching hashes.

```text
OVERALL_VERDICT = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
B07 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B07_V01_ONLY
RESULTS = NOT_AUTHORIZED
```
