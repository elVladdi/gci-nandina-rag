# Revisión experimental 0A-01 / 0A-01 Experimental Review

## Español

### Identificación

- Bloque revisado: `0A-01 — Ground truth documental`
- Revisor: IA experimental independiente
- Fecha de revisión: 2026-09-02
- Dictamen recibido: `PASS WITH CORRECTIONS`
- Estado editorial posterior al dictamen: `REVISION_REQUIRED`
- Estado de remediación: `INTEGRATED — PENDING_CLOSING_EXPERIMENTAL_PASS`

### Correcciones aceptadas

1. **Normalización del vocabulario de estados de claims.** `CLAIM_EVIDENCE_MATRIX.md` debe usar exclusivamente `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED` y `REVIEW_REQUIRED`. Los calificadores metodológicos, de diseño, de protocolo o de temporalidad deben trasladarse a la columna de evidencia/uso y no crear estados adicionales.
2. **Proveniencia diferenciada del hallazgo `48/59`.** El hallazgo `995/1006` de v0.1 dispone de trazabilidad experimental verificada. El valor `48/59` puede conservarse como observación derivada/reportada, pero no debe tratarse con el mismo nivel de congelamiento mientras no exista un artefacto versionado que lo almacene o permita recomputarlo de forma auditable. Hasta entonces queda bajo `REVIEW_REQUIRED`.
3. **HE5 y resultados intermedios.** Cualquier interpretación histórica o intermedia atribuida a experimentos anteriores debe distinguirse de la decisión inferencial final. El estado vigente que gobierna el artículo es `HE5 = PENDING_GROUP3`, según el Plan Maestro vivo. No se incorporará una interpretación específica de EXP-08 como hecho de gobernanza sin verificar primero su artefacto exacto.
4. **Gobernanza del Plan Maestro.** La sincronización entre la copia local experimental y la copia viva en GitHub es una regla preexistente definida por el autor, no una regla nueva propuesta por la revisión. Solo la IA experimental está autorizada a modificar el Plan Maestro; la IA editora y la IA de redacción tienen acceso de solo lectura. Las dos copias representan un único documento lógico y no pueden mantenerse divergentes.

### Observación no adoptada

La sugerencia de ampliar automáticamente la admisión de literatura nueva a proceedings de conferencias de primer nivel no se adopta. La política bibliográfica aprobada por el autor permanece vigente: para literatura académica nueva se exigen artículos de revista científica de alto impacto dentro de la ventana temporal definida en `BIBLIOGRAPHIC_FRAMEWORK.md`, salvo decisión posterior y expresa del autor.

### Verificación adicional realizada por la edición científica

El Plan Maestro vivo consultado en su ubicación registrada mantiene explícitamente que `HE2/HE5` permanecen pendientes de Grupo 3. La búsqueda efectuada sobre el estado accesible del repositorio no permitió localizar todavía un artefacto versionado de EXP-08 que justifique congelar una formulación histórica `PARTIALLY_SUPPORTED` para HE5. En consecuencia, esa formulación no se incorpora como claim autorizado y permanece pendiente de verificación documental si vuelve a resultar relevante.

### Remediación integrada

- Estados de claims normalizados en `article/CLAIM_EVIDENCE_MATRIX.md`.
- `995/1006` y `48/59` separados por nivel de proveniencia.
- Estado final de HE5 preservado como pendiente de Grupo 3.
- Regla de unicidad, sincronización y autoridad exclusiva de escritura del Plan Maestro congelada en `article/DECISIONS.md` y `article/SOURCE_REGISTRY.md`.
- Política bibliográfica original preservada sin ampliación automática a proceedings.
- `article/ARTICLE_STATUS.md` actualizado para solicitar únicamente un pase experimental de cierre.

### Gate

La remediación está integrada. Corresponde ahora un pase experimental de cierre que verifique que las correcciones fueron aplicadas sin regresiones. 0A-01 no puede marcarse `APPROVED` ni `FROZEN` hasta recibir dicho pase y la aprobación expresa del autor.

---

## English

### Identification

- Reviewed block: `0A-01 — Documentary ground truth`
- Reviewer: independent experimental AI
- Review date: 2026-09-02
- Received verdict: `PASS WITH CORRECTIONS`
- Editorial state after the verdict: `REVISION_REQUIRED`
- Remediation status: `INTEGRATED — PENDING_CLOSING_EXPERIMENTAL_PASS`

### Accepted corrections

1. **Normalization of claim-status vocabulary.** `CLAIM_EVIDENCE_MATRIX.md` must use only `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED`, and `REVIEW_REQUIRED`. Methodological, design, protocol, or temporal qualifiers must be moved to the evidence/permitted-use fields rather than creating additional statuses.
2. **Differentiated provenance for the `48/59` finding.** The v0.1 `995/1006` finding has verified experimental traceability. The `48/59` value may be retained as a derived/reported observation, but it must not be treated at the same freeze level until a versioned artifact stores it or permits auditable recomputation. Until then it remains under `REVIEW_REQUIRED`.
3. **HE5 and intermediate results.** Any historical or intermediate interpretation attributed to earlier experiments must be distinguished from the final inferential decision. The current state governing the article is `HE5 = PENDING_GROUP3`, according to the living Master Plan. No specific EXP-08 interpretation will be incorporated as a governance fact until its exact artifact is verified.
4. **Master Plan governance.** Synchronization between the local experimental copy and the living GitHub copy is a pre-existing rule defined by the author, not a new rule proposed by the review. Only the experimental AI is authorized to modify the Master Plan; the scientific-editor AI and drafting AI have read-only access. Both copies represent one logical document and may not remain divergent.

### Observation not adopted

The suggestion to automatically broaden admission of new literature to top-tier conference proceedings is not adopted. The author-approved bibliographic policy remains in force: new academic literature must consist of high-impact scientific-journal articles within the time window defined in `BIBLIOGRAPHIC_FRAMEWORK.md`, unless the author later makes an explicit contrary decision.

### Additional verification performed by scientific editing

The living Master Plan consulted at its registered location explicitly maintains that `HE2/HE5` remain pending for Group 3. The search performed over the accessible repository state did not yet locate a versioned EXP-08 artifact sufficient to freeze a historical `PARTIALLY_SUPPORTED` formulation for HE5. Accordingly, that formulation is not incorporated as an authorized claim and remains pending documentary verification if it becomes relevant again.

### Integrated remediation

- Claim statuses normalized in `article/CLAIM_EVIDENCE_MATRIX.md`.
- `995/1006` and `48/59` separated by provenance level.
- Final HE5 status preserved as pending Group 3.
- Master Plan uniqueness, synchronization, and exclusive write-authority rule frozen in `article/DECISIONS.md` and `article/SOURCE_REGISTRY.md`.
- Original bibliographic policy preserved without automatic broadening to proceedings.
- `article/ARTICLE_STATUS.md` updated to request only a closing experimental pass.

### Gate

Remediation is integrated. A closing experimental pass is now required to verify that the corrections were applied without regressions. 0A-01 may not be marked `APPROVED` or `FROZEN` until that pass is received and the author gives express approval.
