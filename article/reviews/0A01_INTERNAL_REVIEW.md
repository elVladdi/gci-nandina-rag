# Revisión interna 0A-01 / 0A-01 Internal Review

## Español

### Estado

- Bloque: `0A-01 — Ground truth documental`.
- Insumo revisado: segunda entrega corregida de la IA de redacción.
- Dictamen interno: **PASS WITH MINOR TERMINOLOGY CORRECTION**.
- Siguiente gate autorizado: **auditoría experimental independiente**.
- No se autoriza todavía 0A-02.

### Aspectos validados

La segunda entrega corrige adecuadamente los problemas detectados en la primera revisión interna:

1. trata `SRC-03` como fuente GitHub viva y registra el blob SHA como snapshot del corte, no como identidad inmutable;
2. no interpreta sufijos automáticos `(3)`, `(4)`, `(5)` como versiones científicas por sí solos;
3. mantiene los resultados `3,000/100/1,006` de la tesis preliminar como snapshot experimental obsoleto y no como estado vigente;
4. distingue correctamente ausencia de `id_unico` repetidos de independencia por DAM;
5. incorpora explícitamente el problema de dependencia estructural del split v0.1: `995/1006` casos de evaluación pertenecían a DAM presentes en histórico y `48/59` DAM de evaluación también aparecían en histórico;
6. conserva `SERIE` como unidad de análisis y utiliza `DAM` como unidad de agrupamiento para construir particiones sin DAM compartidas;
7. identifica el benchmark vigente v0.2 como H100 `2,950` series / `28` DAM / `66` códigos, DEV `100` series / `6` DAM y EVAL `1,056` series / `67` DAM / `42` códigos;
8. conserva las métricas H100 vigentes como métricas de recuperación de candidatos y no como accuracy global del sistema;
9. mantiene EXP-11B retrieval, EXP-12 y Grupo 3 como dependencias pendientes y no anticipa resultados.

### Precisión terminológica a conservar

En redacciones posteriores debe preferirse una formulación precisa:

> El agrupamiento por DAM elimina el **solapamiento de DAM entre particiones** y, con ello, la dependencia cruzada causada por compartir una misma declaración entre histórico/desarrollo/evaluación. No implica que las 1,056 series del evalset sean internamente independientes entre sí; cuando varias series pertenecen a una misma DAM, la inferencia debe respetar esa agrupación.

Evitar expresiones absolutas como "la DAM impide toda dependencia entre particiones" si pueden interpretarse más allá del control de grupos compartidos.

### Puntos que debe verificar la IA experimental

La auditoría experimental independiente debe comprobar directamente en el repositorio y artefactos congelados:

- cifras `995/1006` y `48/59` del split v0.1;
- ausencia de DAM compartidas en v0.2;
- composición H100/DEV/EVAL v0.2;
- métricas H100 congeladas;
- estado real de EXP-11B retrieval, EXP-12 y Grupo 3;
- coherencia entre las formulaciones documentales y el diseño experimental ejecutado;
- que ninguna conclusión del snapshot 3,000/1,006 se esté heredando como resultado vigente.

### Addendum de supersesión posterior a la auditoría experimental

Esta revisión interna se conserva como registro histórico y no se reescribe retrospectivamente. Sin embargo, la auditoría experimental posterior determinó que la cifra `48/59` no dispone todavía del mismo nivel de trazabilidad congelada que `995/1006`.

Por tanto, el estado vigente de `48/59` se rige por `C20 = REVIEW_REQUIRED` en `CLAIM_EVIDENCE_MATRIX.md`. La mención de `48/59` dentro de los aspectos inicialmente validados documenta lo que la revisión interna consideró aceptable en ese corte, pero **no autoriza su uso actual como hallazgo congelado del manuscrito**.

### Gate

`0A-01` pasa de `REVISION_REQUIRED` a `EXPERIMENTAL_REVIEW`.

No debe declararse `APPROVED` ni `FROZEN` hasta recibir y resolver el feedback de la IA experimental y contar con aprobación expresa del autor.

---

## English

### Status

- Block: `0A-01 — Documentary ground truth`.
- Reviewed input: second corrected delivery from the drafting AI.
- Internal verdict: **PASS WITH MINOR TERMINOLOGY CORRECTION**.
- Authorized next gate: **independent experimental audit**.
- 0A-02 is not yet authorized.

### Validated aspects

The second delivery adequately corrects the issues identified during the first internal review:

1. it treats `SRC-03` as a living GitHub source and records the blob SHA as a cutoff snapshot rather than as an immutable identity;
2. it does not interpret automatic suffixes `(3)`, `(4)`, `(5)` as scientific versions by themselves;
3. it preserves the `3,000/100/1,006` results from the preliminary thesis as a stale experimental snapshot rather than as current status;
4. it correctly distinguishes absence of repeated `id_unico` values from DAM-level independence;
5. it explicitly incorporates the structural-dependence problem in v0.1: `995/1006` evaluation cases belonged to DAMs present in the historical set and `48/59` evaluation DAMs also appeared in the historical set;
6. it preserves `SERIES` as the analysis unit and uses `DAM` as the grouping unit to construct partitions without shared DAMs;
7. it identifies the current v0.2 benchmark as H100 `2,950` series / `28` DAM / `66` codes, DEV `100` series / `6` DAM, and EVAL `1,056` series / `67` DAM / `42` codes;
8. it preserves the current H100 metrics as candidate-retrieval metrics rather than overall system accuracy;
9. it keeps EXP-11B retrieval, EXP-12, and Group 3 as pending dependencies and does not anticipate results.

### Terminology precision to preserve

Later drafting should prefer the following precise formulation:

> DAM grouping removes **DAM overlap across partitions** and therefore the cross-partition dependence caused by sharing the same declaration across historical/development/evaluation sets. It does not imply that the 1,056 series in the evaluation set are internally independent of one another; when multiple series belong to the same DAM, inferential procedures must respect that grouping.

Avoid absolute wording such as "DAM prevents all dependence across partitions" if it could be interpreted more broadly than the shared-group control actually supports.

### Items for the experimental AI to verify

The independent experimental audit must verify directly against the repository and frozen artifacts:

- the `995/1006` and `48/59` v0.1 figures;
- absence of shared DAMs in v0.2;
- v0.2 H100/DEV/EVAL composition;
- frozen H100 metrics;
- actual status of EXP-11B retrieval, EXP-12, and Group 3;
- consistency between documentary formulations and the executed experimental design;
- that no conclusion from the 3,000/1,006 snapshot is inherited as a current result.

### Supersession addendum after the experimental audit

This internal review is preserved as a historical record and is not retrospectively rewritten. However, the subsequent experimental audit determined that the `48/59` figure does not yet have the same level of frozen traceability as `995/1006`.

Accordingly, the current status of `48/59` is governed by `C20 = REVIEW_REQUIRED` in `CLAIM_EVIDENCE_MATRIX.md`. Its appearance among the initially validated aspects documents what the internal review considered acceptable at that cutoff, but **does not authorize its current use as a frozen manuscript finding**.

### Gate

`0A-01` moves from `REVISION_REQUIRED` to `EXPERIMENTAL_REVIEW`.

It must not be declared `APPROVED` or `FROZEN` until the experimental AI feedback has been received and resolved and the author has expressly approved the block.
