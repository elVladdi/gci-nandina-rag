# Experimental Design B01 V05 — Independent transversal framework-positioning review

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B01_V05_TRANSVERSAL_FRAMEWORK_POSITIONING_INTERNAL_REVIEW_V01
DATE = 2026-09-25
ROLE = IA_GESTORA / LEAD_SCIENTIFIC_EDITOR
GOVERNING_DECISION = D-048
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION_RESPONSE_V01.md@f13fdf7929ed89d708cd6950974736acd67011c7
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
BASELINE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
BASELINE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
OUTPUT_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md
OUTPUT_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
OUTPUT_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
OUTPUT_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
AUTHORIZED_SCOPE_ONLY = PASS
FRAMEWORK_GENERAL_OBJECT = PASS
ARCHITECTURE_AS_TECHNICAL_CORE = PASS
AUDITABLE_CLASSIFICATION_SUPPORT_MESSAGE = PASS
EMPIRICAL_TESTBED_SUBORDINATION = PASS
CONFIGURABILITY_WITHOUT_GENERALIZATION = PASS
AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION_CLAIM = ABSENT
RELATED_WORK_PRESERVATION = PASS
SECTION_4_1_TO_4_2_3_PRESERVATION = PASS
SECTION_4_3_TO_4_8_SKELETON_PRESERVATION = PASS
SECTION_5_AND_LATER_PRESERVATION = PASS
RQ_COUNTS_CITATIONS = UNCHANGED
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER_QA = PASS
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OVERALL = PASS
AUTHOR_APPROVAL_GATE = OPEN
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Alcance de la auditoría

La revisión fue diferencial y conceptual respecto de D-048. Se verificó que la corrección no reabriera hechos científicos ya aprobados y que la jerarquía narrativa quedara explícita como:

`framework general → arquitectura como núcleo técnico → instanciación experimental concreta`.

## 2. Comparación V04 → V05 — PASS

La comparación independiente del Markdown confirma únicamente los cambios autorizados:

1. tres párrafos de Introduction en inglés;
2. sus tres espejos semánticos en español;
3. la primera oración de Section 3.7 en inglés;
4. la oración equivalente de Section 3.7 en español.

Related Work, RQ, 4.1–4.2.3, el esqueleto 4.3–4.8, Section 5 y posteriores permanecen textualmente idénticos. No cambiaron cifras ni citas.

## 3. Jerarquía científica y mensaje central — PASS

La Introduction ahora identifica de forma explícita el objeto de nivel artículo como un **configurable framework for auditable tariff-classification decision support** y establece que la arquitectura de Section 3 es su **technical core**.

El apoyo a clasificación está formulado con precisión como:

- recomendación/ranking de candidatos;
- evidencia documental específica por candidato;
- explicación controlada y trazable del Top-3 fijo;
- inspección a nivel de caso para revisión/auditoría.

No se afirma que el framework adjudique autónomamente una clasificación jurídica final ni que auditabilidad equivalga a corrección legal.

La evaluación en NANDINA de ocho dígitos, Capítulo 87 y contexto administrativo/documental peruano queda subordinada explícitamente como **instanciación experimental usada para evaluar el framework**, no como alcance conceptual del aporte. La posibilidad de utilizar otros bancos históricos, espacios de clases, profundidades arancelarias y corpus compatibles se mantiene como configurabilidad/reinstanciación y no como transferencia demostrada de desempeño.

## 4. Consistencia con Related Work y Section 4.1

D-048 exigía preservar Related Work y 4.1–4.2.3. Las expresiones allí conservadas que describen una `decision-support architecture` o una `concrete instantiation of the Section 3 architecture` no constituyen contradicción: en el master V05 la Introduction y 3.7 ya fijan expresamente que esa arquitectura es el núcleo técnico del framework. Por tanto, esas formulaciones pueden seguir describiendo el objeto arquitectónico específico de sus respectivas secciones sin redefinir el alcance general del artículo.

## 5. DOCX — PASS

Los hashes calculados independientemente coinciden con la respuesta de la IA de Redacción:

- MD: `82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8`;
- DOCX: `4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae`.

La comparación OOXML V04→V05 confirma que ambos paquetes conservan las mismas 14 partes y que únicamente `word/document.xml` cambió. `word/comments.xml` permanece byte-identical con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`.

V05 conserva 40 comentarios y cero `w:ins`, `w:del`, `w:moveFrom` o `w:moveTo`.

El DOCX fue renderizado independientemente en 40 páginas y todas fueron inspeccionadas visualmente. No se observaron clipping, solapamientos, glifos faltantes, tablas rotas ni defectos de maquetación.

## 6. Dictamen

```text
B01_V05_TRANSVERSAL_POSITIONING_REVIEW = PASS
B01_SCIENTIFIC_CONTENT = VERIFIED / PASS / PRESERVED
B01_STRUCTURE_V02_ALIGNMENT = PASS / PRESERVED
TRANSVERSAL_FRAMEWORK_POSITIONING = VERIFIED / PASS
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
```

La corrección requerida por D-048 queda técnicamente satisfecha. Esta auditoría no concede aprobación autoral, cierre, congelamiento ni integración. `ARTICLE_MASTER_V009` continúa como master canónico y `ARTICLE_MASTER_V010` no debe promoverse hasta aprobación explícita del autor y el gate posterior de integración.

Section 4.3–4.8 y Results permanecen no autorizados para redacción.