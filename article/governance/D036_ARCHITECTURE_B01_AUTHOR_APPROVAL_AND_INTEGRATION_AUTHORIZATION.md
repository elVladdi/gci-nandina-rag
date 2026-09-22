# D-036 — Architecture B01 author approval and integration authorization

```text
DECISION_ID = D-036
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
BLOCK = ARCHITECTURE_B01
AUTHOR_DECISION = APPROVED
SCIENTIFIC_REVIEW = PASS
TECHNICAL_REVIEW = PASS
INTEGRATION = AUTHORIZED / NOT_YET_COMPLETED
ARTICLE_MASTER_V008 = AUTHORIZED / NOT_YET_PROMOTED
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión autoral

El autor aprobó expresamente Architecture B01 después del dictamen independiente de la IA Gestora registrado en:

`article/reviews/4_ARCHITECTURE_B01_TIMEOUT_SAFE_HANDOFF_INTERNAL_REVIEW_V01.md@02297eafeae44162a4ccc6a67472daae918d0d6b`

La aprobación alcanza exclusivamente las Sections 3.1–3.4 en Part I y su espejo semántico en Part II.

## 2. Artefactos aprobados

```text
SECTION_MD = Architecture_B01_V01.md
SECTION_MD_SHA256 = 1aee2f9ea5235058376fa09377de9db9f6b6a1e755e8ae69dd406198bf040309
SECTION_MD_GIT_BLOB = 5098448cfc7cefe2b5bbce82e5b0ea4bda181862

CUMULATIVE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md
CUMULATIVE_CANDIDATE_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d

CUMULATIVE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
CUMULATIVE_CANDIDATE_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

El DOCX y el Markdown acumulativo exactos permanecen bajo custodia efectiva del autor conforme a D-027 y D-035. La IA Gestora verificó sus identidades antes de abrir el gate de aprobación.

## 3. Estado científico de Architecture B01

Architecture B01 queda:

```text
ARCHITECTURE_B01 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED / READY_FOR_INTEGRATION
SECTIONS_3_1_TO_3_4 = FROZEN_PENDING_CANONICAL_MATERIALIZATION
SCIENTIFIC_REDRAFT = NOT_AUTHORIZED
```

La redacción aprobada fija las siguientes fronteras de diseño:

- la consulta normalizada alimenta la recuperación histórica;
- la recuperación histórica genera y ordena los candidatos;
- el ranking a nivel de código conserva trazabilidad al precedente histórico;
- los tres primeros códigos únicos forman un Top-3 fijo;
- recuperación documental, construcción de contexto y LLM permanecen downstream y no pueden modificar membresía u orden del Top-3;
- el reranking diagnóstico no retroalimenta el flujo principal;
- las puntuaciones de recuperación no se interpretan como probabilidad de corrección jurídica.

## 4. Integración y promoción

La aprobación autoral autoriza, pero no sustituye, la materialización canónica.

La integración se considerará completada únicamente cuando el Markdown acumulativo exacto verificado se materialice canónicamente como:

`article/manuscript/ARTICLE_MASTER_V008.md`

con identidad textual correspondiente al artefacto aprobado de SHA-256:

`895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d`

D-035 sigue vinculante: no debe reintentarse una transferencia directa grande por una vía que ya produjo timeout, ni recurrirse a Base64 manual, fragmentación, chunking o recomposición como workaround. Hasta materialización segura, `ARTICLE_MASTER_V007` sigue siendo el último master Markdown físicamente versionado en GitHub y el candidato B01 V02 es el master aprobado pendiente de promoción técnica.

## 5. Gate posterior

Esta decisión **no abre automáticamente Architecture B02**.

```text
NEXT_GATE = ARCHITECTURE_B01_CANONICAL_INTEGRATION
ARCHITECTURE_B02 = ELIGIBLE_AFTER_INTEGRATION / NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

Una vez completada y verificada la promoción técnica de `ARTICLE_MASTER_V008`, la IA Gestora podrá emitir una decisión separada para abrir Architecture B02.
