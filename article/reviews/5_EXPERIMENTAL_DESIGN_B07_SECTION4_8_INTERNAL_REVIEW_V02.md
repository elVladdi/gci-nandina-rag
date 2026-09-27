# Revisión interna — Experimental Design B07 / Section 4.8 — V02

## Español

```text
REVIEW_ID = B07_SECTION_4_8_INTERNAL_REVIEW_V02
DATE = 2026-09-27
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
RESPONSE_REVIEWED = article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V02.md@b28723a1c1b8d66d8791f23a88a7ff77a2b61161
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V02.md@112669ae8998311d17b4510a2fc8afd7c1fdda49
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION.md@e7ee988c42c2095a0e0b60dd7a216bf148949419
AUTHOR_DECISION = D-082
EXECUTION_AUTHORIZATION = D-083
OVERALL_VERDICT = PASS
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B07_V02_ONLY
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

## 1. Identidad de los candidatos

Se verificaron directamente los archivos reales entregados al autor:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
GIT_BLOB_FROM_BYTES = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
```

Las identidades coinciden con la response V02.

## 2. Auditoría diferencial B07-C01

La comparación exacta entre B07 V01 y B07 V02 confirma que los únicos cambios del master Markdown están dentro de Section 4.8 EN/ES y responden a la observación autoral:

1. se elimina la apertura que presentaba y comparaba el repositorio interno de desarrollo experimental con el repositorio público;
2. la referencia posterior a procedimientos auditados deja de dirigir al lector al repositorio interno y se formula como procedimientos ejecutados y auditados para el estudio;
3. la frase sobre CSV administrativos deja de justificar su no publicación por su existencia en el repositorio interno y se expresa directamente como frontera de redistribución.

La Section 4.8 corregida abre directamente con `gci-nandina-rag-reproducibility`. No contiene menciones narrativas a `development repository`, `experimental-development repository`, `repositorio de desarrollo`, `repositorio interno` ni equivalentes dentro de 4.8.

```text
B07_C01 = CLOSED
PUBLIC_REPRO_REPOSITORY_FOCUS = PASS
INTERNAL_DEVELOPMENT_REPOSITORY_MENTION_IN_SECTION_4_8 = NONE
SECTIONS_1_TO_4_7_PRESERVED = PASS
RESULTS_PLUS_PRESERVED = PASS
NO_NEW_RESULTS = PASS
NO_NEW_CLAIMS = PASS
NO_NEW_LITERATURE = PASS
NO_SCOPE_EXPANSION = PASS
EN_ES_EQUIVALENCE = PASS
```

## 3. Fronteras científicas y snapshot público

El repositorio público fue reconsultado durante esta auditoría y permanece en:

```text
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
DRIFT = NONE
```

La V02 conserva correctamente las fronteras ya aprobadas: recursos materializados frente a planificados/no materializados; paquete público aún no equivalente a una release computacional completa; interfaces objetivo no presentadas como runners materializados; reproducción de referencia distinta de replicación externa; configurabilidad distinta de generalización empírica; y entradas administrativas no asumidas como públicamente redistribuibles.

No se observó leakage de Results ni ampliación de claims.

## 4. DOCX / OOXML y render

Auditoría independiente del binario V02:

```text
ZIP_ENTRY_SET = 14/14 / PRESERVED
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / SAME_AS_B07_V01
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

El diff de párrafos del `document.xml` coincide con el cambio estrecho de Section 4.8 EN/ES y no modifica otras secciones.

Se renderizaron independientemente B07 V01 y B07 V02. Ambos producen 51 páginas. Solo las páginas 23, 24, 49, 50 y 51 cambian visualmente; las otras 46 páginas son pixel-idénticas. Las cinco páginas modificadas fueron inspeccionadas y no presentan clipping, truncamiento, solapamiento ni pérdida material de formato.

```text
FULL_DOCX_RENDER = PASS / 51 PAGES
VISUAL_QA = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
```

## 5. D-035

D-035 permanece activado por el timeout previo. La ejecución V02 respetó la ruta timeout-safe observada: los candidatos MD/DOCX fueron entregados como archivos reales, el master acumulativo grande no fue materializado en GitHub, y entre el head pre-ejecución y la response solo se añadieron el artefacto pequeño de sección y la response. No se observaron artefactos de Base64 manual, chunking, fragmentación ni reensamblado.

```text
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO_OBSERVED
CHUNKING = NO_OBSERVED
FRAGMENTATION = NO_OBSERVED
REASSEMBLY = NO_OBSERVED
```

## 6. Dictamen

```text
SCIENTIFIC_CONTENT = PASS
AUTHOR_REQUESTED_SCOPE_CORRECTION = PASS
SOURCE_BOUNDARY = PASS
CLAIM_CONTROL = PASS
EN_ES_EQUIVALENCE = PASS
CUMULATIVE_CONTINUITY = PASS
DOCX_OOXML = PASS
VISUAL_QA = PASS
D035_DELIVERY = PASS
OVERALL_VERDICT = PASS
```

B07 V02 puede pasar exclusivamente al gate de aprobación del autor. Este PASS no equivale a aprobación autoral, integración ni promoción del master. `ARTICLE_MASTER_V015.md` continúa canónico hasta una eventual aprobación y materialización byte-exacta de V016. Results y secciones posteriores permanecen cerrados.

---

## English

B07 V02 was independently audited against the narrow author-requested B07-C01 correction. The exact delivered MD/DOCX identities match the response metadata. The only cumulative-master changes are inside Section 4.8 EN/ES and remove the internal experimental-development repository from manuscript prose while preserving all previously governed reproducibility boundaries.

The public reproducibility repository remains at HEAD `254831cd955103faa2517065a7eed7fb340bbccc`, tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`, with no drift. OOXML continuity passes: 14/14 package entries preserved, only `word/document.xml` changed, 40 comments and anchors preserved, and zero tracked changes. Independent rendering produced 51 pages; only pages 23, 24, 49, 50 and 51 changed, and all changed pages pass visual QA.

```text
OVERALL_VERDICT = PASS
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B07_V02_ONLY
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
