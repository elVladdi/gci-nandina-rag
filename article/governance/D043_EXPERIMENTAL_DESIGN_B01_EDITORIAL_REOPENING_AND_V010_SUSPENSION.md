# D-043 — Reapertura editorial de Experimental Design B01 y suspensión de V010

## Español

```text
DECISION_ID = D-043
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-042
AUTHOR_RECONSIDERATION = RECEIVED
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_FACTS = PRESERVED
EXPERIMENTAL_DESIGN_B01_EDITORIAL_STATUS = REVISION_REQUIRED
D042_AUTHOR_APPROVAL_FOR_CURRENT_TEXT = SUSPENDED_BEFORE_INTEGRATION
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
CANONICAL_MASTER = ARTICLE_MASTER_V009
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El autor reabrió la revisión de Experimental Design B01 antes de la materialización de `ARTICLE_MASTER_V010`, al identificar que Section 4.2 trasladó al cuerpo publicable detalles de trazabilidad interna —hashes SHA-256, rutas relativas de repositorio y nombres exactos de archivos— cuya utilidad editorial no había sido justificada.

La observación obliga a una reauditoría editorial específica contra `KBS_EWG_34_V01` y el corpus KBS-34. La aprobación registrada en D-042 no se elimina como hecho histórico, pero su autorización de integración queda suspendida para la versión textual V02. No se promoverá V010 ni se abrirá Experimental Design B02 hasta corregir y volver a auditar Section 4.2.

La reapertura no invalida los hechos científicos ya verificados —procedencia, selección, curación, composición de las particiones, control por DAM y límites de la reconstrucción—. El problema es de selección y presentación de detalle técnico en la prosa destinada a KBS.

Regla correctiva provisional: la prosa principal debe priorizar qué datos se usaron, cómo se obtuvieron/procesaron/curaron, cómo se construyeron las particiones y qué contienen. Los identificadores técnicos de integridad, rutas internas y nombres de archivos deben permanecer en manifiestos, repositorios o recursos de reproducibilidad, salvo que un nombre concreto sea metodológicamente indispensable para comprender o reproducir una operación descrita en el texto.

## English

```text
DECISION_ID = D-043
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-042
AUTHOR_RECONSIDERATION = RECEIVED
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_FACTS = PRESERVED
EXPERIMENTAL_DESIGN_B01_EDITORIAL_STATUS = REVISION_REQUIRED
D042_AUTHOR_APPROVAL_FOR_CURRENT_TEXT = SUSPENDED_BEFORE_INTEGRATION
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
CANONICAL_MASTER = ARTICLE_MASTER_V009
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author reopened Experimental Design B01 before `ARTICLE_MASTER_V010` was materialized after identifying that Section 4.2 moved internal traceability details—SHA-256 hashes, repository-relative paths, and exact filenames—into publication-facing prose without a demonstrated editorial need.

This observation requires a focused editorial reaudit against `KBS_EWG_34_V01` and the KBS-34 corpus. D-042 remains part of the historical record, but its integration authorization is suspended for textual version V02. V010 will not be promoted and Experimental Design B02 will not be opened until Section 4.2 is corrected and reaudited.

The reopening does not invalidate the already-verified scientific facts concerning provenance, selection, curation, partition composition, DAM-level control, or reconstruction boundaries. The defect concerns selection and presentation of technical detail in KBS-facing prose.

Provisional corrective rule: the main manuscript should prioritize what data were used, how they were obtained/processed/curated, how partitions were constructed, and what those partitions contain. Integrity identifiers, internal paths, and filenames should remain in manifests, repositories, or reproducibility resources unless a concrete filename is methodologically necessary to understand or reproduce an operation described in the article.