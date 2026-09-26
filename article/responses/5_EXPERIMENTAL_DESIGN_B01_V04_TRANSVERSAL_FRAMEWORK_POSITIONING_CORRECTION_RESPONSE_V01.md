# Experimental Design B01 V04 — Transversal framework positioning correction — Response V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION
GOVERNING_DECISION = D-048
STATUS = DELIVERED_FOR_GESTORA_AUDIT
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
BASELINE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
BASELINE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d / PASS
OUTPUT_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md
OUTPUT_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
OUTPUT_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
OUTPUT_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
AUTHORIZED_SCOPE_ONLY = PASS
RELATED_WORK_TEXTUALLY_IDENTICAL = YES
SECTION_4_1_TO_4_2_3_TEXTUALLY_IDENTICAL = YES
SECTION_4_3_TO_4_8_SKELETON_IDENTICAL = YES
SECTION_5_AND_LATER_TEXTUALLY_IDENTICAL = YES
RQ_UNCHANGED = YES
FIGURES_AND_COUNTS_UNCHANGED = YES
CITATIONS_UNCHANGED = YES
NON_BINDING_TESTBED_FORMULATION_REMOVED_FROM_INTRODUCTION = YES
FRAMEWORK_IDENTIFIED_AS_GENERAL_OBJECT = YES
ARCHITECTURE_IDENTIFIED_AS_TECHNICAL_CORE = YES
NANDINA_CHAPTER87_PERU_SUBORDINATED_TO_EXPERIMENTAL_INSTANTIATION = YES
AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION_CLAIM = NO
NOVELTY_CLAIM = NO
EMPIRICAL_GENERALIZATION_CLAIM = NO
FINAL_COMMENT_COUNT = 40
COMMENT_RANGE_START_COUNT = 40
COMMENT_RANGE_END_COUNT = 40
COMMENT_REFERENCE_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 40
CLIPPING = NONE
OVERLAP = NONE
MISSING_GLYPHS = NONE
LAYOUT_DEFECTS = NONE
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D-035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Párrafos modificados

La corrección se limitó exactamente a los siguientes elementos autorizados:

1. **Introduction, Part I — English**: párrafo que comenzaba `This study examines a decision-support architecture...`.
2. **Introduction, Part I — English**: párrafo que comenzaba `The article makes three bounded contributions...`.
3. **Introduction, Part I — English**: párrafo que comenzaba `The empirical evaluation uses an offline customs-classification testbed...`.
4. **Introduction, Part II — Spanish mirror**: los tres párrafos semánticamente correspondientes.
5. **Section 3.7, Part I — English**: únicamente la primera oración del primer párrafo, para hacer explícita la relación `framework → architecture as technical core`.
6. **Section 3.7, Part II — Spanish mirror**: únicamente la oración semánticamente equivalente.

No se modificó ningún otro párrafo.

### Resultado semántico controlado

La Introduction ahora presenta inequívocamente el objeto general como un **framework configurable para apoyo auditable a la clasificación arancelaria**, con la arquitectura de la Sección 3 como su **núcleo técnico**. El apoyo a clasificación se describe mediante recomendación/ranking de candidatos, evidencia documental específica por candidato y explicación controlada y trazable del Top-3 fijo. La trazabilidad se limita a inspección/revisión/auditoría a nivel de caso y no se equipara con corrección jurídica.

La evaluación se introduce subordinadamente como una instanciación experimental offline del framework en NANDINA de ocho dígitos, Capítulo 87 y el contexto administrativo/documental peruano definido en Methods. Se eliminó la formulación `The testbed is non-binding` / `El testbed es no vinculante` y se sustituyó por la frontera científica: el escenario evaluado no constituye despliegue aduanero operativo ni adjudicación jurídica final. La reinstanciación con otros datos, espacios de clases, profundidades arancelarias o corpus compatibles permanece descrita como configurabilidad, no como transferencia de desempeño.

### Verificación diferencial y DOCX

La comparación V04→V05 confirma que Related Work, las RQ, 4.1–4.2.3, el esqueleto 4.3–4.8 y Section 5+ permanecen textualmente idénticos. No cambiaron cifras ni citas. En el paquete DOCX, únicamente `word/document.xml` cambió; `word/comments.xml` permaneció byte-identical. Se conservaron 40 comentarios, 40 rangos de inicio, 40 rangos de fin, 40 referencias y cero tracked changes.

El DOCX V05 fue renderizado completo en 40 páginas e inspeccionado visualmente. No se observaron clipping, solapamientos, pérdida de glifos, tablas rotas ni otros defectos de maquetación.

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION
GOVERNING_DECISION = D-048
STATUS = DELIVERED_FOR_GESTORA_AUDIT
BASELINE_MD_SHA256_CHECK = PASS
BASELINE_DOCX_SHA256_CHECK = PASS
AUTHORIZED_SCOPE_ONLY = PASS
RELATED_WORK_TEXTUALLY_IDENTICAL = YES
SECTION_4_1_TO_4_2_3_TEXTUALLY_IDENTICAL = YES
SECTION_4_3_TO_4_8_SKELETON_IDENTICAL = YES
SECTION_5_AND_LATER_TEXTUALLY_IDENTICAL = YES
RQ_UNCHANGED = YES
FIGURES_AND_COUNTS_UNCHANGED = YES
CITATIONS_UNCHANGED = YES
FRAMEWORK_IDENTIFIED_AS_GENERAL_OBJECT = YES
ARCHITECTURE_IDENTIFIED_AS_TECHNICAL_CORE = YES
EMPIRICAL_INSTANTIATION_BOUNDARY = PASS
AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION_CLAIM = NO
NOVELTY_CLAIM = NO
EMPIRICAL_GENERALIZATION_CLAIM = NO
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 40
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The correction was restricted to the three authorized Introduction paragraphs in English and their Spanish semantic mirrors, plus only the first sentence of Section 3.7 in each language. No other paragraph was modified.

The manuscript now identifies the article-level object as a configurable framework for auditable tariff-classification decision support, with the frozen Section-3 architecture as its technical core. Classification support is expressed through ranked candidate recommendation, candidate-specific documentary evidence, and controlled, traceable explanation of the fixed Top-3. Case-level inspectability supports review/audit but is not stated as legal correctness.

The empirical setting is explicitly subordinated to framework evaluation: eight-digit NANDINA, Chapter 87, and the defined Peruvian administrative/documentary context are the reference experimental instantiation. The residual `non-binding testbed` wording was removed and replaced with the scientifically bounded statement that the evaluated setting is neither an operational customs deployment nor an autonomous legal adjudication. Re-instantiation remains a configurability property, not evidence of performance transfer.

Differential QA confirms that Related Work, the RQs, Sections 4.1–4.2.3, the 4.3–4.8 skeleton, and Section 5 onward are textually unchanged; figures/counts and citations are unchanged. Only `word/document.xml` changed in the DOCX package; `word/comments.xml` remained byte-identical. The candidate retains 40 comments and zero tracked changes. Full 40-page rendering and visual inspection passed without clipping, overlap, missing glyphs, or layout defects.
