# D-050 — Experimental Design B01 V010 integration

```text
DECISION_ID = D-050
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B01
PARENT_DECISION = D-049
AUTHOR_APPROVAL = RECEIVED / PRESERVED
SCIENTIFIC_REVIEW = PASS
TECHNICAL_INTEGRATION = PASS
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARTICLE_MASTER_V010 = PROMOTED / CANONICAL
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
CANONICAL_CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
SECTION_4_3 = ELIGIBLE / NOT_YET_AUTHORIZED
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Verificación de integración

D-049 autorizó promover el Markdown acumulativo aprobado `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md` únicamente si su materialización canónica como `ARTICLE_MASTER_V010.md` devolvía exactamente el Git blob esperado `8dc09fb841162005b2155491735336b0e70187c6`.

La IA Gestora verificó en la rama `article/main-manuscript` que:

`article/manuscript/ARTICLE_MASTER_V010.md`

existe y GitHub reporta exactamente:

`GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6`.

La identidad coincide con la fijada por D-049 para el artefacto aprobado, cuyo SHA-256 es `82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8`.

La carga fue realizada por el autor en el commit `40534bffe62ebdc1a145837a3b9ccfc93c9863c7`. No fue necesaria reconstrucción, Base64 manual, fragmentación, chunking ni recomposición.

## 2. Cierre de B01

Experimental Design B01 V05 queda definitivamente:

`CLOSED / APPROVED / FROZEN / INTEGRATED`.

Se preservan como contenido aprobado:

- las correcciones editoriales controladas de Sections 3.5 y 3.7;
- Section 4.1;
- Section 4.2 y 4.2.1–4.2.3;
- el posicionamiento transversal que define el objeto general como un framework configurable para apoyo auditable a la clasificación arancelaria, con la arquitectura de Section 3 como núcleo técnico;
- la separación entre alcance conceptual del framework e instanciación experimental en NANDINA de ocho dígitos, Capítulo 87 y contexto peruano.

## 3. Master canónico

Desde esta decisión, el master Markdown canónico pasa a ser:

`article/manuscript/ARTICLE_MASTER_V010.md`

El DOCX aprobado correspondiente permanece bajo custodia local efectiva del autor:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx`

SHA-256:

`4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae`.

## 4. Gate posterior

La integración satisface la condición de D-049 para que Section 4.3 sea elegible. Esta decisión no redacta ni autoriza todavía su contenido científico.

```text
CURRENT_GATE = POST_B01 / PRE_SECTION_4_3
SECTION_4_3 = ELIGIBLE / NOT_YET_AUTHORIZED
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

Antes de abrir 4.3, la IA Gestora debe reconstruir su ground truth documental y experimental y emitir una decisión/prompt atómico separado.
