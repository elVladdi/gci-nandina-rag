# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01 — Clasificación HS directa y aprendizaje supervisado`: **`APPROVED / FROZEN`**.
- `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`**.
- Estado de 0B-03A: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Dictamen interno de 0B-03A: **`PASS WITH MINOR CORRECTIONS`**.
- Revisión experimental de 0B-03A: **`NOT_REQUIRED`**.
- Freeze de 0B-03A: **`NOT_YET_AUTHORIZED`**.
- `0B-03B`: **`NOT_STARTED`**.
- Plan de lotes: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Corpus PDF consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### 0B-01 — cierre formal

```text
0B-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Artefacto canónico:
`article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`

### 0B-02 — cierre formal

```text
0B-02 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Artefacto canónico:
`article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`

Registros:
- `article/reviews/0B02_INTERNAL_REVIEW.md`;
- `article/reviews/0B02_AUTHOR_APPROVAL.md`.

Correcciones gobernantes ya congeladas:

1. P01: test temporal final 1,652, validación 1,835; HS6 Top-3 0.955 sin retrieved sentences y 0.937 con retrieved sentences.
2. P03: 226,703 casos tabulados frente a 211,435 asignados explícitamente a train/validation/test; 15,268 permanecen `NO_VERIFICABLE_EN_PDF`.
3. P03: helpfulness operativo 65.7% (score 4–5); >85% corresponde a otra distribución de percepción; reducción de tiempo/esfuerzo = percepción, no causalidad.
4. P02/P04/P06: Text2Trade `REVIEW_REQUIRED` y sin validación externa sectorial; P04 ≈84.23% no es detección adjudicada de misclasificación; P06 imprime Recall=`TP/(TP+TN)` y sus F1 se conservan con caveat; CV por triples no demuestra independencia ni leakage.

### 0B-03A — revisión interna completada

La entrega de la IA de redacción fue contrastada con los seis PDF primarios del lote. Registro de revisión:

`article/reviews/0B03A_INTERNAL_REVIEW.md`

Dictamen:

```text
0B-03A = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE = NOT_YET_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

#### Hallazgos gobernantes

- THE-RAG constituye antecedente directo de `RAG + LLM + HS classification`; por sí sola esa combinación no puede convertirse en una diferenciación futura.
- En THE-RAG el LLM participa en la determinación del código y RAG no mejora universalmente todas las configuraciones.
- ICCA-RAG es QA/asistencia documental aduanera, no benchmark de clasificación HS; metadata/backtracking es procedencia técnica, no corrección jurídica ni auditabilidad formal por candidato.
- Koch & Power debe describirse operacionalmente como clasificación mediante transformer encoders fine-tuned con cabeza de clasificación, aunque el paper utilice la etiqueta LLM.
- Gholamian et al. evalúa taxonomías Icecat/WDC-222, no HS; su uso es supporting para robustez/ICL.
- Amel et al.: el efecto multimodal depende del baseline exacto.

#### Correcciones C1–C6 a integrar solo después de aprobación del autor

1. **THE-RAG/model identity:** `.44/.47/.51/.59/.60` HS6 Top-3 corresponde a `gemini_1.5_flash`, no a `gemini_1.5_flash_8b`; preservar separadas ambas variantes. El contraejemplo `llama3.1_8b` queda verificado: `.14` CoT/no-RAG frente a `.11/.09` THE-RAG en chunks 250/500.
2. **Koch & Power:** normalizar como `FINE_TUNED_TRANSFORMER_CLASSIFIER`; si se conserva `FINE_TUNED_LLM`, marcarlo como terminología de autores.
3. **ICCA-RAG:** `RAG_EVIDENCE_SUPPORT` solo con calificador de contexto para QA documental; no equivale a evidencia normativa posterior a Top-k fijo.
4. **Gholamian:** el experimento humano 76/72/97 y 72/67/95 valida principalmente perturbaciones/mapeo con ejemplos similares; no generalizar a beneficio humano de clasificación HS.
5. **Pressure test:** `SUPPORTS_CANDIDATE` significa contraste compatible con supervivencia provisional en este lote, no evidencia de novelty ni prueba de ausencia global.
6. **Amel multimodal:** `D=.500 -> I+D=.582` = +8.2 puntos porcentuales; `T+D+C=.647 -> mejor multimodal=.653` = +0.6 puntos porcentuales.

No se requiere nueva ejecución de la IA de redacción. Las correcciones son de normalización/alcance y pueden integrarse editorialmente en el artefacto canónico después de la aprobación expresa del autor.

### Candidatos provisionales después de la revisión 0B-03A

Todos permanecen `CANDIDATE_GAP_ONLY`; ninguno establece novelty:

- F1/G1: `SURVIVES IN NARROW FORM` — precedentes históricos generan/fijan ranking y normativa llega después sin reordenar.
- F2/G2: `SURVIVES IN NARROW FORM` — generador posterior limitado a Top-k fijo, sin introducir/reordenar códigos.
- F3/G3: `SURVIVES THIS BATCH; METHODOLOGICAL` — control explícito por unidad administrativa/grupo.
- F4/G4: `SURVIVES AS METHODOLOGICAL DISTINCTION` — predictive/candidate performance ≠ corrección sustantiva/jurídica adjudicada.
- F5/G5: `FURTHER NARROWED BY ICCA-RAG` — evaluación formal por caso de trazabilidad/auditabilidad, no mera metadata/faithfulness.
- G6: `SURVIVES; METHODOLOGICAL` — ground truth independiente/adjudicado para claims de correctness.
- G7: `NEW/PROVISIONAL` — separación entre papel clasificatorio y explicativo del LLM; debe someterse a presión en 0B-03B.

### Gate vigente de 0B-03A

```text
revisión interna completada
-> aprobación expresa del autor
-> integrar C1–C6
-> crear artefacto canónico FROZEN de 0B-03A
-> abrir 0B-03B
```

Hasta recibir aprobación expresa, **no** está autorizado abrir 0B-03B ni avanzar a 0B-04, 0C o fases posteriores.

La IA experimental solo se incorporará si una interpretación bibliográfica afecta directamente un hecho experimental, claim experimental o restricción metodológica bajo su autoridad. En 0B-03A no se detectó esa necesidad.

### Prohibiciones vigentes

No está autorizado:
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
- abrir 0B-03B antes de freeze de 0B-03A;
- usar resultados experimentales pendientes como cerrados;
- convertir secondary claims en hechos sin verificación primaria.

### Fases posteriores

- `0B-03B`: `NOT_STARTED`.
- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Revista objetivo: **no definida ni congelada**; se decidirá en 0D.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**; 0A-01 and 0A-02 are **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01: **`APPROVED / FROZEN`**.
- 0B-02: **`APPROVED / FROZEN`**.
- Active block: **`0B-03A — LLM, RAG, and multimodality in customs classification/compliance`**.
- 0B-03A: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Experimental review: **`NOT_REQUIRED`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-03B: **`NOT_STARTED`**.
- Consolidated corpus: 62 distinct works/documents with primary verifiable access `62/62`.
- Target journal: pending until Phase 0D.
- Manuscript drafting: not started.

### 0B-03A internal review

The drafting deliverable was checked against all six primary PDFs. Review record:
`article/reviews/0B03A_INTERNAL_REVIEW.md`.

The governing findings are retained: THE-RAG is direct prior art for RAG+LLM HS classification and its LLM participates in code determination; its RAG effect is configuration-dependent rather than universal. ICCA-RAG is customs-document QA rather than an HS-classification benchmark. Koch & Power operationally use fine-tuned transformer encoders as closed-label classifiers. Gholamian et al. use Icecat/WDC product taxonomies rather than HS. Amel et al.'s multimodal gain depends on the exact baseline.

Required freeze corrections C1–C6 are: preserve exact THE-RAG model identity; normalize Koch & Power's operational taxonomy; qualify ICCA-RAG's evidence role; narrow interpretation of Gholamian's human experiment; define pressure-test labels as provisional contrast rather than novelty evidence; and report Amel's multimodal gains against the exact baseline.

No drafting-AI rerun is needed. These corrections may be editorially integrated only after express author approval.

### Candidate-gap status

F1/F2 survive only in narrow form; F3 and G6 remain methodological; F4 remains a methodological distinction; F5 is further narrowed by ICCA-RAG; G7 is new/provisional and must be pressure-tested in 0B-03B. All are `CANDIDATE_GAP_ONLY`; none establishes novelty.

### Current gate

`internal review complete -> express author approval -> integrate C1–C6 -> canonical 0B-03A freeze -> open 0B-03B`.

Until express approval, 0B-03B and later phases remain closed. Experimental-AI review is not required for this batch because no literature interpretation changes a frozen experimental fact, claim, or restriction.
