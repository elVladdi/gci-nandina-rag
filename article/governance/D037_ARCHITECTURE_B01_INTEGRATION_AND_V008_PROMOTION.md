# D-037 — Architecture B01 integration and ARTICLE_MASTER_V008 promotion

```text
DECISION_ID = D-037
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
BLOCK = ARCHITECTURE_B01
AUTHOR_APPROVAL_DECISION = D-036
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARTICLE_MASTER_V008 = PROMOTED / CANONICAL
ARCHITECTURE_B02 = ELIGIBLE / NOT_YET_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Cierre de integración

La aprobación autoral de Architecture B01 registrada en D-036 queda técnicamente materializada. El master acumulativo aprobado fue promovido de forma exacta a:

`article/manuscript/ARTICLE_MASTER_V008.md`

Identidad canónica:

```text
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
PROMOTION_COMMIT = 7624a47832d169ded56e7cc542c2f47999c8fdb4
```

El Git blob fue calculado previamente sobre el archivo exacto bajo custodia del autor y la materialización devolvió exactamente el mismo blob `0145d13e1bc4e4fdeab79f7bad83d00f67221a76`. Por tanto, no hubo reconstrucción científica, normalización, fragmentación ni cambio de contenido durante la promoción.

## 2. DOCX canónico

El DOCX acumulativo correspondiente permanece bajo custodia local efectiva del autor conforme a D-021, D-027 y D-035:

```text
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CANONICAL_CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

## 3. Estado de Architecture B01

Las Sections 3.1–3.4 de Part I y su espejo semántico de Part II quedan:

`CLOSED / APPROVED / FROZEN / INTEGRATED`

No se autoriza redacción adicional de B01 salvo futura enmienda expresa.

## 4. Gate posterior

La integración vuelve elegible el bloque siguiente, pero no lo abre automáticamente:

```text
CURRENT_GATE = POST_ARCHITECTURE_B01 / PRE_B02
ARCHITECTURE_B02 = ELIGIBLE / NOT_YET_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

La IA Gestora debe reconstruir el estado canónico y emitir una autorización/prompts separados antes de iniciar Architecture B02.

## 5. Dependencia experimental externa

El último HEAD verificado del Plan Maestro experimental es:

`docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`

Ese estado registra Group 6 en curso con G6-F01 cerrado/aprobado/integrado y no altera el cierre científico de Architecture B01 ni autoriza por sí mismo Architecture B02.