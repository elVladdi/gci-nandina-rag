# Revisión experimental 0A-01 / 0A-01 Experimental Review

## Español

### Identificación

- Bloque revisado: `0A-01 — Ground truth documental`
- Revisor: IA experimental independiente
- Fecha de revisión inicial: 2026-09-02
- Dictamen inicial recibido: `PASS WITH CORRECTIONS`
- Pase experimental de cierre recibido: `PASS WITH 2 REQUIRED CORRECTIONS`
- Estado editorial actual: `REVISION_REQUIRED`
- Estado de remediación: `SECOND_REMEDIATION_INTEGRATED — PENDING_FINAL_EXPERIMENTAL_PASS`

### Correcciones de la primera revisión

1. **Normalización del vocabulario de estados de claims.** `CLAIM_EVIDENCE_MATRIX.md` debe usar exclusivamente `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED` y `REVIEW_REQUIRED`. Los calificadores metodológicos, de diseño, de protocolo o de temporalidad deben trasladarse a la columna de evidencia/uso y no crear estados adicionales.
2. **Proveniencia diferenciada del hallazgo `48/59`.** El hallazgo `995/1006` de v0.1 dispone de trazabilidad experimental verificada. El valor `48/59` puede conservarse como observación derivada/reportada, pero no debe tratarse con el mismo nivel de congelamiento mientras no exista un artefacto versionado que lo almacene o permita recomputarlo de forma auditable. Hasta entonces queda bajo `REVIEW_REQUIRED`.
3. **HE5 y resultados intermedios.** Cualquier interpretación histórica o intermedia atribuida a experimentos anteriores debe distinguirse de la decisión inferencial final. El estado vigente que gobierna el artículo es `HE5 = PENDING_GROUP3`, según el Plan Maestro vivo.
4. **Gobernanza del Plan Maestro.** La sincronización entre la copia local experimental y la copia viva en GitHub es una regla preexistente definida por el autor, no una regla nueva propuesta por la revisión. Solo la IA experimental está autorizada a modificar el Plan Maestro; la IA editora científica y la IA de redacción tienen acceso de solo lectura.

### Observación bibliográfica cerrada

La sugerencia de ampliar automáticamente la admisión de literatura nueva a proceedings de conferencias de primer nivel no se adopta. La política bibliográfica aprobada por el autor permanece vigente: para literatura académica nueva se exigen artículos de revista científica de alto impacto dentro de la ventana temporal definida en `BIBLIOGRAPHIC_FRAMEWORK.md`, salvo decisión posterior y expresa del autor.

Estado: `BIBLIOGRAPHIC_PROCEEDINGS_OBSERVATION = CLOSED / AUTHOR_POLICY_PREVAILS`.

### Verificación de EXP-08 y estado de HE5

Se verificó directamente el artefacto versionado:

`outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md`

El artefacto registra una interpretación histórica/intermedia específica de EXP-08: `HE5 = PARTIALLY_SUPPORTED`, con cuatro componentes y limitaciones explícitas de comparabilidad entre v0.1 y v0.2.

Esta interpretación se conserva como resultado histórico específico de EXP-08 y **no sustituye** el estado inferencial final vigente de HE5. El Plan Maestro vivo mantiene `HE2/HE5` pendientes de Grupo 3; por tanto, el artículo no tratará `HE5 = PARTIALLY_SUPPORTED` de EXP-08 como decisión definitiva de HE5. La gobernanza vigente para la decisión final es `HE5 = PENDING_GROUP3`.

### Pase experimental de cierre: dos correcciones requeridas

El pase de cierre posterior a la primera remediación confirmó como resueltos la normalización de estados, la separación `995/1006` frente a `48/59`, la condición `REVIEW_REQUIRED` de `48/59`, el carácter pendiente de la decisión final de HE5 y la política bibliográfica. Requirió exclusivamente dos correcciones:

1. reconocer explícitamente el artefacto EXP-08 y clasificar `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia, no como decisión inferencial final;
2. hacer inequívoca la sincronización del Plan Maestro como igualdad de contenido textual canónico entre copia local y copia GitHub, no mera equivalencia semántica, y declarar que D-011 supersede a D-009 en materias de sincronización, coexistencia y divergencia.

Ambas correcciones fueron integradas en `article/DECISIONS.md`, `article/SOURCE_REGISTRY.md` y este registro.

### Remediación acumulada integrada

- Estados de claims normalizados en `article/CLAIM_EVIDENCE_MATRIX.md`.
- `995/1006` y `48/59` separados por nivel de proveniencia.
- `48/59` permanece `REVIEW_REQUIRED`.
- EXP-08 reconocido como artefacto versionado con interpretación histórica/intermedia `HE5 = PARTIALLY_SUPPORTED`.
- Estado inferencial final de HE5 preservado como `PENDING_GROUP3`.
- Regla de unicidad, sincronización textual exacta y autoridad exclusiva de escritura del Plan Maestro congelada en `article/DECISIONS.md` y `article/SOURCE_REGISTRY.md`.
- D-011 declarado prevalente sobre D-009 para sincronización/coexistencia/divergencia.
- Política bibliográfica original preservada sin ampliación automática a proceedings.

### Gate

Corresponde ahora un **pase experimental final limitado a verificar estas dos correcciones y ausencia de regresiones**. No debe reabrirse 0A-01 desde cero.

0A-01 no puede marcarse `APPROVED` ni `FROZEN` hasta recibir `PASS — READY FOR AUTHOR APPROVAL` y la aprobación expresa del autor.

---

## English

### Identification

- Reviewed block: `0A-01 — Documentary ground truth`
- Reviewer: independent experimental AI
- Initial review date: 2026-09-02
- Initial verdict received: `PASS WITH CORRECTIONS`
- Closing experimental pass received: `PASS WITH 2 REQUIRED CORRECTIONS`
- Current editorial state: `REVISION_REQUIRED`
- Remediation status: `SECOND_REMEDIATION_INTEGRATED — PENDING_FINAL_EXPERIMENTAL_PASS`

### Corrections from the first review

1. **Normalization of claim-status vocabulary.** `CLAIM_EVIDENCE_MATRIX.md` must use only `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED`, and `REVIEW_REQUIRED`. Methodological, design, protocol, or temporal qualifiers must be moved to the evidence/permitted-use fields rather than creating additional statuses.
2. **Differentiated provenance for the `48/59` finding.** The v0.1 `995/1006` finding has verified experimental traceability. The `48/59` value may be retained as a derived/reported observation, but it must not be treated at the same freeze level until a versioned artifact stores it or permits auditable recomputation. Until then it remains under `REVIEW_REQUIRED`.
3. **HE5 and intermediate results.** Any historical or intermediate interpretation attributed to earlier experiments must be distinguished from the final inferential decision. The current state governing the article is `HE5 = PENDING_GROUP3`, according to the living Master Plan.
4. **Master Plan governance.** Synchronization between the local experimental copy and the living GitHub copy is a pre-existing rule defined by the author, not a new rule proposed by the review. Only the experimental AI is authorized to modify the Master Plan; the scientific-editor AI and drafting AI have read-only access.

### Closed bibliographic observation

The suggestion to automatically broaden admission of new literature to top-tier conference proceedings is not adopted. The author-approved bibliographic policy remains in force: new academic literature must consist of high-impact scientific-journal articles within the time window defined in `BIBLIOGRAPHIC_FRAMEWORK.md`, unless the author later makes an explicit contrary decision.

Status: `BIBLIOGRAPHIC_PROCEEDINGS_OBSERVATION = CLOSED / AUTHOR_POLICY_PREVAILS`.

### EXP-08 verification and HE5 status

The following versioned artifact was directly verified:

`outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md`

The artifact records a historical/intermediate interpretation specific to EXP-08: `HE5 = PARTIALLY_SUPPORTED`, with four components and explicit comparability limitations between v0.1 and v0.2.

This interpretation is preserved as a historical result specific to EXP-08 and **does not replace** the current final inferential status of HE5. The living Master Plan keeps `HE2/HE5` pending for Group 3; therefore, the article will not treat EXP-08's `HE5 = PARTIALLY_SUPPORTED` as the final HE5 decision. The current governance state for the final decision is `HE5 = PENDING_GROUP3`.

### Closing experimental pass: two required corrections

The closing pass after the first remediation confirmed as resolved the status normalization, the separation of `995/1006` from `48/59`, the `REVIEW_REQUIRED` status of `48/59`, the pending character of the final HE5 decision, and the bibliographic policy. It required only two corrections:

1. explicitly acknowledge the EXP-08 artifact and classify `HE5 = PARTIALLY_SUPPORTED` as a historical/intermediate interpretation rather than the final inferential decision;
2. make Master Plan synchronization unambiguously require equality of canonical textual content between the local and GitHub copies, rather than mere semantic equivalence, and state that D-011 supersedes D-009 on synchronization, coexistence, and divergence matters.

Both corrections were integrated into `article/DECISIONS.md`, `article/SOURCE_REGISTRY.md`, and this record.

### Integrated cumulative remediation

- Claim statuses normalized in `article/CLAIM_EVIDENCE_MATRIX.md`.
- `995/1006` and `48/59` separated by provenance level.
- `48/59` remains `REVIEW_REQUIRED`.
- EXP-08 acknowledged as a versioned artifact with historical/intermediate interpretation `HE5 = PARTIALLY_SUPPORTED`.
- Final inferential HE5 status preserved as `PENDING_GROUP3`.
- Master Plan uniqueness, exact textual synchronization, and exclusive write-authority rule frozen in `article/DECISIONS.md` and `article/SOURCE_REGISTRY.md`.
- D-011 declared controlling over D-009 for synchronization/coexistence/divergence.
- Original bibliographic policy preserved without automatic broadening to proceedings.

### Gate

A **final experimental pass limited to verifying these two corrections and the absence of regressions** is now required. 0A-01 must not be reopened from scratch.

0A-01 may not be marked `APPROVED` or `FROZEN` until `PASS — READY FOR AUTHOR APPROVAL` is received and the author gives express approval.
