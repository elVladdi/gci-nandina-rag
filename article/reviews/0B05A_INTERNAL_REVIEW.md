# Revisión interna 0B-05A / 0B-05A Internal Review

## Español

### 1. Dictamen

**VEREDICTO: `PASS WITH MINOR CORRECTIONS`**  
**MATERIAL_ERRORS: `0`**  
**EXPERIMENTAL_REVIEW: `NOT_REQUIRED`**  
**AUTHOR_APPROVAL: `PENDING`**

La entrega de 0B-05A fue contrastada a nivel de claim contra los cinco PDF primarios asignados. El análisis es sustantivamente correcto, respeta el alcance del lote y mantiene separadas las propiedades que el prompt exigía no colapsar.

No se detectó ninguna reinterpretación de resultados experimentales congelados, ninguna declaración de novelty/gap definitivo ni ninguna modificación del Plan Maestro. Por ello no se activa revisión de la IA experimental.

### 2. Resultado de la verificación primaria

#### P01 — Bender & Friedman, Data Statements

Se verifica que el trabajo propone `data statements` como práctica profesional de documentación para NLP, distingue versiones larga y breve, caracteriza curación/población/contexto y contempla un apéndice de procedencia para datasets derivados. Los dos casos son reconstrucciones `post hoc`, no una validación experimental del efecto de adoptar data statements. Los `value scenarios` son explícitamente plausibles y no predictivos.

**Corrección menor C1:** en el artefacto congelado, evitar `demuestra` cuando se describa el efecto de la documentación. La formulación preferida es que los casos **ilustran la sustancia y redactabilidad/factibilidad documental del esquema**, mientras los beneficios sobre bias, ingeniería, generalización o reproducibilidad permanecen como argumentos/beneficios esperados de los autores, no efectos causalmente demostrados.

#### P02 — Gebru et al., Datasheets for Datasets

Se verifican las categorías de ciclo de vida, las preguntas sobre relaciones entre instancias, splits recomendados y su rationale, mantenimiento/actualizaciones y el objetivo secundario de facilitar reproducibilidad. La copia primaria analizada identifica `arXiv:1803.09010v8 [cs.DB] — 1 Dec 2021`.

**Corrección menor C2:** preservar la identidad de la **copia analizada** como arXiv v8. No completar silenciosamente la metadata editorial final desde otras fuentes. Para evitar una inferencia más fuerte de la necesaria, registrar la metadata final como `REVIEW_REQUIRED_FOR_FINAL_CITATION` / `NO_VERIFICABLE_EN_LA_COPIA_ANALIZADA`, no como afirmación de que una publicación final no exista.

**Corrección menor C3:** mantener explícita la incompatibilidad terminológica con Pineau et al.: Gebru et al. incluyen dentro de su objetivo secundario la posibilidad de crear datasets alternativos de características similares; no homogeneizar esa expresión con la taxonomía 2×2 de P04.

#### P03 — Mitchell et al., FAIR Data Pipeline

Se verifican la identidad científica y DOI, el análisis de 17 use cases, la gestión de research objects y la trazabilidad de outputs a través de código/modelos hacia datos primarios. El paper establece expresamente que la reproducibilidad es deseable, pero **no es un core requirement**; el requisito crítico es poder identificar qué código se ejecutó sobre qué datasets y preservar provenance/traceability.

**Corrección menor C4:** en el freeze, mantener como núcleo `PROVENANCE/LINEAGE + VERSION IDENTIFICATION`, no `REPRODUCIBILITY FRAMEWORK`. Cuando se enumeren mecanismos técnicos, usar únicamente los que estén explícitamente documentados en el PDF y evitar que una lista de versiones, identificadores, commits o checksums se interprete como garantía de reproducibilidad o correctness.

#### P04 — Pineau et al., NeurIPS 2019 Reproducibility Program

Se verifica la taxonomía operacional: mismos datos + mismas herramientas = `Reproducible`; datos diferentes + mismas herramientas = `Replicable`; mismos datos + herramientas diferentes = `Robust`; datos y herramientas diferentes = `Generalisable`. También se verifican los datos centrales del programa: 6,743 submissions, 21.1% de aceptación, 40% de código en submission, 74.4% en camera-ready; 173 papers claimed y 73 instituciones en el challenge.

**Corrección menor C5:** conservar siempre la taxonomía como **convención adoptada por este paper**, no como terminología universal. Mantener las asociaciones observadas separadas de causalidad y la advertencia de que disponibilidad de código/datos no prueba correctness ni reproducción automática. No afirmar que el programa demostró mejora causal de la calidad científica.

#### P05 — Raji et al., Internal Algorithmic Auditing

Se verifican el carácter end-to-end del internal audit, las cinco etapas de SMACTR (`Scoping`, `Mapping`, `Artifact Collection`, `Testing`, `Reflection`), el `transparency trail`, la acumulación de artefactos documentales y el uso de escenarios/organizaciones hipotéticos para ilustrar el framework.

**Corrección menor C6:** `Post-Audit` puede aparecer en la figura/flujo posterior, pero no debe convertirse en una sexta etapa de SMACTR. Asimismo, cualquier lenguaje del paper que sugiera un procedimiento `validated` debe describirse con cautela: el PDF no presenta un benchmark/control empírico que demuestre eficacia causal de SMACTR. `Transparency trail`/ADHF = auditabilidad del lifecycle y reconstrucción documental, no `output-level auditability`, auditoría externa independiente ni legal correctness.

### 3. Síntesis gobernante del lote

La síntesis de la entrega queda aceptada con las correcciones anteriores:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

Y, en paralelo:

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`

**Corrección menor C7:** esta taxonomía debe usarse como frontera metodológica, no como una escala lineal en la que una propiedad implique automáticamente la siguiente.

### 4. Efecto sobre F1–F5

No se modifica el estado congelado de los candidatos.

- F1/F2: no reciben evidencia de novelty en este lote.
- F3: recibe únicamente fundamento para documentar relaciones, unidades, curación y particiones; `documentar dependencia ≠ controlarla ≠ demostrar independencia`.
- F4: se refuerza la frontera `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5: el lote confirma prior art fuerte en provenance, transparency trails e internal auditing. Por tanto, queda prohibida cualquier formulación amplia de «ausencia de trazabilidad/auditabilidad». Solo permanece como candidato estrecho la **evaluación formal, explícita y separada de auditabilidad documental por salida**, todavía sin status de novelty.
- G6 permanece eliminado; G7 permanece absorbido en F2.

### 5. Claims y metadata

La lista de claims autorizables/prohibidos de la entrega es metodológicamente aceptable, siempre que en el freeze se apliquen C1–C7 y se mantengan las etiquetas `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `SECONDARY_CLAIM_UNVERIFIED` y `NO_VERIFICABLE_EN_PDF` con alcance literal.

No se autoriza convertir claims de terceros citados dentro de estos papers en hechos independientes sin verificar la fuente primaria correspondiente.

### 6. Gate

Estado resultante:

```text
0B-05A = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0B-05B = NOT_STARTED / CLOSED_BY_GATE
```

El freeze de 0B-05A requiere aprobación expresa del autor. Las correcciones C1–C7 deberán incorporarse al artefacto canónico congelado; no es necesario devolver el bloque a la IA de redacción por no existir errores materiales.

---

## English

### 1. Verdict

**VERDICT: `PASS WITH MINOR CORRECTIONS`**  
**MATERIAL_ERRORS: `0`**  
**EXPERIMENTAL_REVIEW: `NOT_REQUIRED`**  
**AUTHOR_APPROVAL: `PENDING`**

The 0B-05A drafting deliverable was checked claim-by-claim against the five assigned primary PDFs. It is substantively correct, remains within batch scope, and preserves the distinctions required by the governing prompt. No frozen experimental result was reinterpreted, no final novelty/gap was claimed, and no Master-Plan modification is implicated.

### 2. Mandatory minor corrections for freeze

**C1 — Bender & Friedman.** Treat data statements as a documentation/contextualization proposal. The two cases are post-hoc illustrations, and the value scenarios are not predictive. Do not present bias/generalization/reproducibility benefits as experimentally demonstrated causal effects.

**C2 — Gebru et al. metadata.** The analyzed copy is `arXiv:1803.09010v8 [cs.DB] — 1 Dec 2021`. Do not silently reconstruct final editorial metadata from outside the assigned PDF. For the freeze, use `REVIEW_REQUIRED_FOR_FINAL_CITATION` / `NO_VERIFICABLE_EN_LA_COPIA_ANALIZADA` rather than implying that no later publication exists.

**C3 — Gebru vs Pineau terminology.** Do not silently harmonize their uses of reproducibility. Gebru et al. explicitly include creating alternative datasets with similar characteristics as a secondary reproducibility objective, whereas Pineau et al. adopt a specific 2×2 taxonomy.

**C4 — FAIR Data Pipeline.** Its governing role is provenance/lineage and version identification. The authors explicitly state that full reproducibility is desirable but not a core requirement. Technical identifiers/versioning mechanisms must not be converted into guarantees of reproducibility or correctness.

**C5 — Pineau et al.** Preserve `reproducible ≠ replicable ≠ robust ≠ generalisable` as the convention adopted by this paper. Keep observed associations separate from causal claims; code/data availability does not by itself establish correctness or automatic reproducibility, and the program did not establish causal improvement in scientific-paper quality.

**C6 — Raji et al.** SMACTR has five named stages. Post-Audit shown in the broader process must not be turned into a sixth SMACTR stage. The framework is illustrated rather than empirically benchmarked for causal effectiveness. Transparency trail/ADHF concern lifecycle auditability, not formal per-output auditability, independent external audit, or legal correctness.

**C7 — Cross-paper taxonomy.** The accepted distinctions are methodological boundaries, not a linear maturity ladder in which one property entails the next.

### 3. Gap-candidate impact

F1/F2 receive no novelty evidence. F3 gains documentation/dependency-reporting foundation only. F4 is reinforced as a boundary separating provenance/reproducibility/auditability from substantive or legal correctness. F5 is further constrained by strong prior art on provenance, transparency trails, and internal audit: only the narrow candidate of a **formal, explicit, separate documentary auditability evaluation at output level** remains, still without novelty status. G6 stays eliminated and G7 stays merged into F2.

### 4. Gate

```text
0B-05A = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0B-05B = NOT_STARTED / CLOSED_BY_GATE
```

Author approval is required before freezing 0B-05A. C1–C7 must be incorporated into the canonical frozen artifact. No return to the drafting AI is required because no material errors were found.
