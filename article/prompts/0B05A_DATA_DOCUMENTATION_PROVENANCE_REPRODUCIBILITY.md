# Prompt 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail / Data documentation, provenance, reproducibility, and audit trail

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail`.

Este bloque es **fundacional y metodológico**. No busca demostrar novelty ni establecer un gap aduanero. Su finalidad es reconstruir con precisión qué significan y qué no significan dataset documentation, version/identity, provenance/lineage, reproducibility, transparency trail e internal algorithmic audit.

No redactes secciones del manuscrito, no cierres el gap, no busques literatura nueva, no modifiques GitHub ni el Plan Maestro y no avances a 0B-05B, 0B-05C, 0B-06, 0C ni fases posteriores.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/DECISIONS.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/STYLE_GUIDE.md`;
8. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
9. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
10. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`;
11. los freezes de `0B-01`, `0B-02`, `0B-03A`, `0B-03B`, `0B-04A` y `0B-04B`;
12. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
13. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
14. este prompt completo.

No reabras ni reinterpretes freezes anteriores.

### PDFs asignados

Analiza **exclusivamente** estos cinco PDF del corpus heredado:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

Para P03, identifica la obra por su identidad científica real visible en el PDF: **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**. No corrijas metadata bibliográfica desde memoria o web; conserva lo que el PDF permita verificar.

Si alguno no está accesible o no puede leerse íntegramente, identifica únicamente ese archivo. No sustituyas su contenido con web, abstracts, snippets, tesis, Anexo, conocimiento general ni otros PDF.

Todos los demás documentos del corpus quedan `OUT_OF_SCOPE_FOR_0B05A`.

### Objetivo científico del lote

El lote debe permitir responder, sin overclaiming:

1. Qué información proponen documentar Bender & Friedman y Gebru et al. y para qué objetivos científicos/operativos.
2. Qué diferencias existen entre `data statement`, `datasheet`, dataset description, dataset identity/version y dataset quality.
3. Qué significa provenance/lineage en FAIR Data Pipeline y qué objetos/relaciones registra.
4. Qué papel tienen código, configuración, inputs, outputs, registry y versioning para rastrear un resultado.
5. Qué definición operacional de reproducibility usa Pineau et al. y cómo se diferencia de replication/generalization.
6. Qué componentes del programa NeurIPS 2019 se evaluaron realmente y qué no puede generalizarse a toda la investigación ML.
7. Qué entiende Raji et al. por internal algorithmic audit, lifecycle documentation y transparency trail.
8. Qué diferencia existe entre un audit trail organizacional/end-to-end y una evaluación formal por salida como HE4.
9. Por qué documentación, provenance, reproducibility y auditability son propiedades relacionadas pero no equivalentes.
10. Cómo estos fundamentos permiten describir con precisión el proyecto sin convertirlos en evidencia de corrección arancelaria, corrección jurídica o generalización externa.

### Regla crítica de procedencia

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

Una afirmación que un paper atribuya a otro trabajo no se convierte en hecho independiente del artículo. Si el paper menciona impactos, sesgos, crisis de reproducibilidad, regulaciones, recomendaciones externas o beneficios generales basándose en terceros, clasifícalos como `SECONDARY_CLAIM_UNVERIFIED` salvo que el propio paper los mida directamente.

### Distinciones metodológicas obligatorias

Mantén separadas estas categorías:

- `DATASET_DOCUMENTATION`;
- `DATA_STATEMENT`;
- `DATASHEET_FOR_DATASETS`;
- `DATASET_IDENTITY_VERSIONING`;
- `DATA_PROVENANCE_LINEAGE`;
- `WORKFLOW_PROVENANCE`;
- `REPRODUCIBILITY`;
- `REPLICATION`;
- `GENERALIZATION`;
- `TRANSPARENCY_TRAIL`;
- `INTERNAL_ALGORITHMIC_AUDIT`;
- `OUTPUT_LEVEL_AUDITABILITY_EVALUATION`.

Reglas concretas:

- documentar un dataset no demuestra que sea representativo, correcto o adecuado para cualquier tarea;
- un datasheet no es una certificación de calidad;
- versionar identifica un estado; no garantiza por sí solo reproducibilidad;
- provenance describe linaje/relaciones de producción; no demuestra correctness;
- disponibilidad de código/datos no implica que un tercero pueda reproducir automáticamente el resultado;
- reproducibility no equivale a replication en otro entorno/dataset ni a generalization;
- un checklist de reproducibilidad no es una métrica universal de calidad científica;
- un transparency trail no equivale a formal output-level auditability;
- internal algorithmic auditing no demuestra corrección jurídica ni institucional de un sistema;
- la existencia de documentos de auditoría no prueba que cada claim de salida esté adecuadamente respaldado.

### Verificaciones específicas por paper

#### P01 — Bender & Friedman, Data Statements

Verifica:

- objetivo científico y ético declarado;
- esquema long-form/short-form;
- curation rationale, language variety, speaker, annotator, curator y otros campos realmente propuestos;
- relación con generalizability y reproducibility según los autores;
- límites/recomendaciones de adopción;
- qué claims de bias/harm dependen de fuentes secundarias.

No conviertas un data statement en garantía de ausencia de sesgo ni en validación estadística del dataset.

#### P02 — Gebru et al., Datasheets for Datasets

Verifica:

- motivación, composición, collection process, preprocessing/cleaning, uses, distribution y maintenance;
- destinatarios: dataset creators y consumers;
- relación declarada con transparency/accountability/reproducibility;
- carácter adaptable/no prescriptivo del cuestionario;
- tratamiento de datasets dinámicos/versionados;
- limitaciones reconocidas por autores.

No presentes datasheets como certificación de calidad, fairness o suitability universal.

#### P03 — FAIR Data Pipeline

Verifica:

- definición operacional de provenance/traceability;
- qué research objects registra el data registry;
- relación entre source data, processing scripts, model configuration, outputs y metadata;
- local/remote registry, read/write tracking y pipeline execution;
- version control y linkage;
- qué significa FAIR en el paper y qué claims son propios vs secundarios;
- límites de transferibilidad desde epidemiological/scientific workflows al presente estudio.

No confundas provenance con correctness, y no afirmes que registrar un pipeline vuelve automáticamente reproducible cualquier experimento.

#### P04 — Pineau et al., Reproducibility Program

Verifica:

- definición explícita de reproducibility usada por los autores;
- code submission policy;
- reproducibility challenge;
- reproducibility checklist;
- qué datos/resultados del programa NeurIPS 2019 se analizan;
- qué conclusiones son descriptivas del programa y cuáles son recomendaciones generales;
- diferencia entre reproducibility, replication, robustness y scientific reliability cuando el PDF la permita.

No conviertas el programa NeurIPS 2019 en prueba universal de que una práctica aislada garantiza reproducibilidad.

#### P05 — Raji et al., Internal Algorithmic Auditing

Verifica:

- objetivo del framework end-to-end;
- fases del lifecycle/audit y artefactos documentales;
- concepto de transparency trail;
- stakeholder/governance process;
- naturaleza de los ejemplos/escenarios utilizados;
- qué significa audit integrity/accountability dentro del paper;
- qué partes son framework/propuesta vs evaluación empírica;
- diferencia respecto de un protocolo de auditabilidad por salida como HE4.

No presentes SMACTR/internal audit como prueba de legal correctness ni como instrumento universalmente validado de output-level auditability.

### Relación con el piloto experimental

El proyecto actual puede usar este lote para fundamentar únicamente distinciones metodológicas como:

`DOCUMENTAR != VERSIONAR != RASTREAR PROVENANCE != REPRODUCIR != REPLICAR != GENERALIZAR`.

Y:

`LIFECYCLE AUDIT TRAIL != OUTPUT-LEVEL AUDITABILITY SCORE != LEGAL CORRECTNESS`.

El análisis no puede modificar el ground truth experimental congelado ni afirmar que el repositorio reproducible del proyecto satisface íntegramente todos los marcos de estos papers. Cualquier correspondencia con el proyecto debe etiquetarse `INFERENCIA_CRITICA` y delimitarse como adaptación metodológica.

### Relación con F1–F5

0B-05A no es un pressure test de novelty aduanera. Usa únicamente:

- `METHOD_FOUNDATION_RELEVANT`;
- `METHOD_CONTRAST_RELEVANT`;
- `METHOD_BOUNDARY_RELEVANT`;
- `NOT_RELEVANT_TO_GAP_CANDIDATE`.

Criterio esperado:

- **F1:** normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- **F2:** normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- **F3:** puede ser `METHOD_FOUNDATION_RELEVANT` para documentación de composición, curación, particiones y límites, sin inferir leakage.
- **F4:** `METHOD_BOUNDARY_RELEVANT` para separar provenance/reproducibility de correctness.
- **F5:** `METHOD_BOUNDARY_RELEVANT` para separar lifecycle audit trail de evaluación formal de auditabilidad por salida.

G6 permanece eliminado y G7 permanece absorbido en F2; no se reabren.

### Formato obligatorio de salida

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | tipo documental visible | observaciones`.

#### B. Matriz funcional de gobernanza/reproducibilidad
Una fila por paper:
`paper | problema | objeto documentado | mecanismo/propuesta | versioning | provenance/lineage | reproducibility | audit trail | métricas/evaluación | resultado principal | límite | función`.

#### C. Fichas individuales
Una por paper, usando las cuatro etiquetas de procedencia.

#### D. Taxonomía metodológica
Clasifica cada paper con las categorías obligatorias y explica solapamientos sin forzar equivalencias.

#### E. Mapa de trazabilidad por paper
Representa el flujo real, por ejemplo:

`SOURCE DATA -> PROCESS/CONFIG/CODE -> OUTPUT -> METADATA/PROVENANCE -> REVIEW/AUDIT`

solo cuando el paper lo sostenga. Para papers de documentación conceptual, representa el flujo documental correspondiente.

#### F. Relación metodológica con F1–F5
`paper | F1 | F2 | F3 | F4 | F5 | justificación` usando exclusivamente las etiquetas metodológicas autorizadas.

#### G. Claims metodológicos autorizables
Propón formulaciones precisas potencialmente utilizables después en Methods/Related Work, cada una con fuente y límite explícito. **No redactes todavía el manuscrito.**

#### H. Claims prohibidos o excesivos
Lista cerrada de formulaciones que estos cinco papers no autorizan.

#### I. Claims secundarios, inconsistencias y metadata pendiente
`paper | claim/inconsistencia | estado | acción futura necesaria`.

Presta especial atención a diferencias de versión/preprint/publicación y no reconstruyas metadata desde memoria.

#### J. Recomendación bibliográfica
`paper | función científica | uso potencial | recomendación | justificación`.

Usa cuando corresponda:

- `KEEP_CORE_METHOD`;
- `KEEP_SUPPORTING_METHOD`;
- `REVIEW_REQUIRED`;
- `EXCLUDE_FROM_ARTICLE`.

#### K. Dictamen

Concluye uno de:

- `PASS`;
- `PASS WITH CORRECTIONS`;
- `BLOCKED`.

Si es `PASS WITH CORRECTIONS`, enumera exactamente qué normalizaciones deberán gobernar un eventual freeze.

### Prohibiciones finales

No:

- redactes ninguna sección del artículo;
- declares novelty o gap definitivo;
- busques web o literatura nueva;
- utilices otros PDF;
- modifiques GitHub;
- modifiques el Plan Maestro;
- reinterpretes resultados experimentales congelados;
- abras 0B-05B/0B-05C/0B-06/0C;
- conviertas documentación, provenance, reproducibility o audit trail en correctness o legal validity.

Responde únicamente en español.

---

## English

### Role and scope

Execute only `0B-05A — Data documentation, provenance, reproducibility, and audit trail`. This is a foundational methodological batch, not a novelty search or manuscript-drafting task.

Read the governing article files, prior freezes, 0A ground truth, `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`, and this prompt before analyzing the five assigned inherited PDFs: Bender & Friedman data statements; Gebru et al. datasheets; the supplied FAIR Data Pipeline paper; Pineau et al. reproducibility program report; and Raji et al. end-to-end internal algorithmic auditing framework.

The core distinctions are:

`DOCUMENTATION != VERSION/IDENTITY != PROVENANCE/LINEAGE != REPRODUCIBILITY != REPLICATION != GENERALIZATION`

and

`LIFECYCLE AUDIT TRAIL != OUTPUT-LEVEL AUDITABILITY EVALUATION != LEGAL CORRECTNESS`.

Use `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`. Do not use web/new literature, out-of-batch PDFs, manuscript drafting, novelty claims, Master-Plan edits, experimental reinterpretation, or later-phase opening.

Return sections A–K exactly as specified in the Spanish instructions and respond only in Spanish.
