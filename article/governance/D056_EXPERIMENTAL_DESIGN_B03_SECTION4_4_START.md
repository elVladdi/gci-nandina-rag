# D-056 — Experimental Design B03 / Section 4.4 start

```text
DECISION_ID = D-056
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B03
SECTION = 4.4 Partition validity and dependence controls
CANONICAL_MASTER = ARTICLE_MASTER_V011
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V011.md
CANONICAL_MASTER_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
CANONICAL_MASTER_MD_GIT_BLOB = c2aee16c219ed33c16e8e647fbd56f4dacc2cd61
SECTION_4_4 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base

D-055 cerró e integró Experimental Design B02 y promovió `ARTICLE_MASTER_V011.md` como master canónico. Se verificó además el `SRC-03` vivo antes de abrir este bloque: HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, Plan Maestro blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`. El corte conserva como principios congelados SERIE como unidad de análisis y DAM/declaración como unidad de agrupamiento cuando existe dependencia; el benchmark v0.2 vigente mantiene H100 2,950 series/28 DAM/66 códigos, DEV 100 series/6 DAM y EVAL 1,056 series/67 DAM/42 códigos.

El ground truth experimental previo obliga además a distinguir independencia entre particiones de independencia entre observaciones: v0.2 elimina DAM compartidas entre particiones, pero las series pertenecientes a una misma DAM dentro de una partición no deben tratarse automáticamente como independientes. Los duplicados y near-duplicates constituyen controles/limitaciones separados y no deben confundirse con unicidad de `id_unico` ni con el control de agrupamiento por DAM.

## 2. Alcance autorizado

Se autoriza exclusivamente la redacción de:

- Part I: `4.4 Partition validity and dependence controls`;
- Part II: espejo español semánticamente equivalente.

No se reabre 4.1–4.3 ni Sections 1–3. No se redacta 4.5–4.8, Results, Discussion, Conclusion, Abstract o Title.

## 3. Regla de evidencia

La IA de Redacción debe verificar directamente el estado vivo de `SRC-03`, `main` y los artefactos experimentales pertinentes antes de formular cualquier hecho. No debe copiar ciegamente snapshots editoriales si el repositorio experimental vivo ha avanzado.

El bloque debe describir el diseño y los controles de validez realmente ejecutados, no resultados narrativos adelantados. Cualquier cifra, regla de partición, control de leakage, duplicado/near-duplicate o dependencia debe ser trazable a evidencia primaria versionada.

## 4. Gate

El prompt atómico gobernante es `article/prompts/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4.md`. La entrega vuelve a la IA Gestora para auditoría independiente. No hay autorización implícita para B04/4.5.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B03_SECTION_4_4_DRAFTING
NEXT_ACTOR = IA_REDACCION
SECTION_4_4 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
