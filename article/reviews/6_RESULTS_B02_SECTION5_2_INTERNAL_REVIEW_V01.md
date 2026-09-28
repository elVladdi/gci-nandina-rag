# Internal review — Results B02 / Section 5.2 — V01

## Español

```text
REVIEW = 6_RESULTS_B02_SECTION5_2_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = IA_GESTORA
BLOCK = RESULTS_B02_SECTION_5_2
CANDIDATE_REVISION = V01
DELIVERY_RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V01.md@19806a4d25b08c9897476861ee85c0bfbe360b91
GOVERNING_PROMPT = article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f
GROUND_TRUTH_DECISION = D-092
EXECUTION_AUTHORIZATION = D-093
OVERALL_VERDICT = PASS_WITH_CORRECTIONS
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B03_PLUS = NOT_AUTHORIZED
```

## 1. Auditoría científica y diferencial

IA Gestora re-verificó el candidato acumulativo contra el baseline B01/V017 y contra las fuentes métricas congeladas del snapshot experimental `db0d0ad0d8435921a7838db6720eaea86a263763`.

Identidades observadas:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
SHA256 = 87b85f095e0cef6d6f9b12e70223596b563014a38bcacfa37c4e0448a66dad6c
GIT_BLOB_EXPECTED_FROM_BYTES = 804ae5709f08e878202f48465d4671bf70dc15c7

ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
SHA256 = c267f7da5415161b812aed10cef66929b6b6cd2be51ecb2196d43c2e1180ce6f
```

La comparación Markdown B01→B02 mostró modificaciones únicamente en §5.2 EN/ES: el placeholder heredado fue sustituido por cuatro párrafos de Results en cada espejo. Sections 1–5.1 y 5.3+ permanecieron intactas.

Las cifras y denominadores coinciden con las cuatro fuentes congeladas autorizadas: historical BM25 H100, flat normative BM25, hierarchical normative BM25 y D1a Text2Trade-inspired MNRL. La prosa mantiene candidate retrieval/ranking como objeto de medida, conserva a los tres métodos no históricos como comparadores y reserva los contrastes inferenciales para §5.6. No se filtraron CI, bootstrap, p-values, disposición HE2, sensibilidad, evidencia documental, explicación, literatura ni Discussion.

```text
GROUND_TRUTH_FIDELITY = PASS
SECTION_5_2_ONLY_DIFF = PASS
SECTIONS_1_TO_5_1_PRESERVED = PASS
SECTIONS_5_3_PLUS_PRESERVED = PASS
NO_INFERENTIAL_RESULT_LEAKAGE = PASS
NO_HE2_DISPOSITION_LEAKAGE = PASS
CANDIDATE_RETRIEVAL_BOUNDARY = PASS
COMPARATOR_ROLE_BOUNDARY = PASS
ENGLISH_PROSE = PASS
```

## 2. Corrección obligatoria de naturalidad en el espejo español

El contenido semántico español es fiel, pero contiene tres formulaciones híbridas/calco que no deben congelarse en el master:

1. `métricas de early ranking` → usar una formulación española natural y precisa, preferentemente `métricas de desempeño en las primeras posiciones del ranking`;
2. `framework primario` → alinear con la semántica del original como `flujo primario del framework`;
3. `Section 5.6` → `Sección 5.6`.

Estas correcciones son terminológicas/de naturalidad y no alteran cifras, resultados, inferencia ni alcance científico. No se autoriza reescritura adicional de §5.2.

```text
EN_ES_SEMANTIC_EQUIVALENCE = PASS
SPANISH_NATURALNESS = CORRECTION_REQUIRED
CORRECTION_SCOPE = NARROW / THREE_PHRASES_ONLY
```

## 3. Auditoría DOCX y D-035

El paquete DOCX candidato fue auditado estructuralmente:

```text
ZIP_OOXML_INTEGRITY = PASS
ZIP_ENTRY_SET = 14/14 PRESERVED
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / BYTE_IDENTICAL
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
```

Se renderizó el DOCX completo en 52 páginas. La comparación visual con B01 identificó cambios únicamente en las páginas 24–26 y 50–52; las demás páginas fueron idénticas al baseline previamente auditado. Las seis páginas modificadas fueron inspeccionadas y no presentan clipping, solapamientos, truncamiento material ni pérdida de formato.

El delta GitHub desde el HEAD pre-ejecución hasta la response contiene únicamente el artefacto pequeño de sección y la response. No se materializó el master acumulativo ni el DOCX en GitHub y no se observó Base64 manual, chunking, fragmentación o reensamblado.

```text
FULL_DOCX_RENDER = PASS / 52 PAGES
VISUAL_QA = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
```

## 4. Dictamen

```text
OVERALL_VERDICT = PASS_WITH_CORRECTIONS
SCIENTIFIC_CONTENT = PASS
NUMERICAL_FIDELITY = PASS
DIFFERENTIAL_SCOPE = PASS
DOCX_INTEGRITY = PASS
SPANISH_NATURALNESS = NARROW_CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = DO_NOT_OPEN_YET
NEXT_ACTOR = IA_REDACCION_AFTER_CORRECTION_PROMPT_AUTHORIZATION
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

B02 V01 no se somete todavía a aprobación autoral. La única acción permitida antes del nuevo gate es una corrección estrecha de las tres formulaciones indicadas, manteniendo intacto todo el contenido científico y numérico aprobado por esta auditoría.

---

## English

Results B02 V01 passes scientific, numerical, differential, OOXML, render, and timeout-safe handoff checks. The overall verdict is `PASS_WITH_CORRECTIONS` solely because the Spanish semantic-control mirror contains three mixed-language/calque formulations that require a narrow naturalness correction. No scientific or numerical rewriting is authorized. The author-approval gate remains closed until the corrected B02 V02 candidate is independently audited.