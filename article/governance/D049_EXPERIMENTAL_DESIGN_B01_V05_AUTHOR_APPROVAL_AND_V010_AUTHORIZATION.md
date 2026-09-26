# D-049 — Experimental Design B01 V05 author approval and V010 authorization

```text
DECISION_ID = D-049
DATE = 2026-09-25
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B01
PARENT_DECISION = D-048
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_V05_TRANSVERSAL_FRAMEWORK_POSITIONING_INTERNAL_REVIEW_V01.md@27b8a707a617f5a541ff53dfdb769f9064b63cd1
AUTHOR_DECISION = APPROVED
SCIENTIFIC_REVIEW = PASS
TRANSVERSAL_POSITIONING_REVIEW = PASS
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
APPROVED_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
EXPECTED_ARTICLE_MASTER_V010_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
APPROVED_MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_MASTER_CANDIDATE_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
CANONICAL_CITATION_COMMENTS_AFTER_B01 = 40
TRACKED_CHANGES = 0
ARTICLE_MASTER_V010 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_3 = ELIGIBLE_AFTER_V010_INTEGRATION / NOT_YET_AUTHORIZED
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión autoral

El autor aprobó expresamente `Experimental Design B01 V05` después del PASS independiente de la IA Gestora. La aprobación preserva el rediseño de Section 4 bajo Structure V02 y la corrección transversal de D-048.

Quedan aprobados y congelados para integración:

- las dos enmiendas editoriales controladas de Sections 3.5 y 3.7;
- Section 4.1 `Experimental setting and scope`;
- Section 4.2 `Historical data and experimental dataset construction`;
- Sections 4.2.1–4.2.3;
- la corrección transversal V05 que presenta el objeto general como framework configurable de apoyo auditable a la clasificación arancelaria, con la arquitectura de Section 3 como núcleo técnico.

La aprobación no abre contenido científico de Section 4.3 ni posteriores.

## 2. Artefactos aprobados

```text
CUMULATIVE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md
SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
EXPECTED_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6

CUMULATIVE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

La IA Gestora verificó nuevamente los hashes exactos de los archivos entregados antes de registrar esta decisión.

## 3. Jerarquía científica congelada

El master aprobado fija la siguiente jerarquía narrativa:

`framework general → arquitectura como núcleo técnico → instanciación experimental concreta`.

El framework apoya la clasificación mediante ranking/recomendación de candidatos, evidencia documental específica por candidato y explicación controlada/trazable. No adjudica autónomamente una clasificación jurídica final.

NANDINA a ocho dígitos, Capítulo 87 y el contexto administrativo/documental peruano son la instanciación empírica usada para evaluar el framework, no su alcance conceptual. La reinstanciación con otros bancos históricos, espacios de clases, profundidades arancelarias o corpus compatibles sigue siendo una propiedad de configurabilidad y no evidencia de transferencia de desempeño.

## 4. Integración y promoción

Se autoriza materializar, sin modificación de contenido, el Markdown acumulativo exacto aprobado como:

`article/manuscript/ARTICLE_MASTER_V010.md`

La integración solo se considerará completada cuando el blob Git del archivo materializado sea exactamente:

`8dc09fb841162005b2155491735336b0e70187c6`

D-023 y D-035 permanecen vinculantes. No se autoriza Base64 manual, fragmentación, chunking, recomposición ni reconstrucción. El encoding interno del conector/API no constituye Base64 manual.

El DOCX aprobado permanece bajo custodia local efectiva del autor conforme a D-021/D-027 y se convierte en el próximo baseline acumulativo únicamente después de la verificación de integración.

## 5. Gate posterior

La aprobación autoral autoriza la integración, pero no la sustituye.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V010_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
SECTION_4_3 = ELIGIBLE_AFTER_INTEGRATION / NOT_AUTHORIZED
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Después de verificar V010, la IA Gestora debe emitir una decisión separada de integración y podrá abrir el siguiente bloque atómico elegible: Section 4.3 `Documentary corpus and evidence resource`.
