# Prompt — Experimental Design B07 / Section 4.8 — V01

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente B07 de Experimental Design: **Section 4.8 Reproducibility resources** y su espejo español. No avances a Results ni modifiques ninguna sección anterior.

Este prompt opera bajo MWDP v1.0 y SPCCR. La omisión de una regla acumulativa no la deroga.

### 1. Onboarding obligatorio

Lee íntegramente y en este orden exacto:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. este prompt específico.

Después lee íntegramente:

- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
- `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
- `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`;
- `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
- `article/governance/D078_EXPERIMENTAL_DESIGN_B06_INTEGRATION_AND_V015_PROMOTION.md`;
- `article/governance/D079_EXPERIMENTAL_DESIGN_B07_SECTION4_8_GROUND_TRUTH_SYNC.md`;
- `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
- `article/manuscript/ARTICLE_MASTER_V015.md`.

Si el onboarding no puede completarse, detente con `BLOCKED_ONBOARDING` y no modifiques ningún artefacto.

### 2. Baselines exactos

Markdown canónico obligatorio:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
BASELINE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
```

Word acumulativo obligatorio, proporcionado por el autor:

```text
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
PRIOR_CITATION_COMMENTS = 40
PRIOR_TRACKED_CHANGES = 0
```

Si el DOCX no está disponible o su SHA-256 no coincide exactamente, detente con:

`BLOCKED_MISSING_EXACT_B06_V02_DOCX_BASELINE`

No reconstruyas el DOCX desde Markdown. No uses un Word anterior. Preserva los 40 comentarios heredados y sus anchors/references.

### 3. Re-verificación de fuentes públicas vivas

Antes de redactar, verifica directamente en GitHub:

```text
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
EXPECTED_REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
EXPECTED_REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
```

Lee al menos:

- `README.md` — blob esperado `eb31035160d88fbe5634ca8df414c4ed741bd624`;
- `docs/REPRODUCIBILITY.md` — blob `839b4245fcf4497ebf6ced28dd8771e3b29601c4`;
- `docs/DATA_PROVENANCE.md` — blob `e7fac0b48c9fc53c2e09f99807d8be7609277ac6`;
- `docs/EXPERIMENT_PROTOCOL.md` — blob `3782e98bd6423ce3a7cfe7a4cd5d620e2573ccaa`;
- `docs/DATA_CONTRACT.md`;
- `docs/TAXONOMY_AND_NORMATIVE_CORPUS.md`;
- `docs/USING_YOUR_OWN_DATA.md`;
- `docs/EXPECTED_RESULTS.md`;
- `configs/examples/custom_dataset.example.yaml`;
- `scripts/README.md` — blob `09ec6d886205290d6ae109762f1c5f90a053ef06`;
- `configs/presets/README.md` — blob `f698911b4604b4b0105fa0c5097754451b7263e3`;
- `data/README.md` — blob `062cf7ea2c0e35b1420561068bd254ca273c07f9`;
- el tree recursivo del snapshot para distinguir archivos realmente materializados de directorios/recursos solo planificados.

Consulta además D-079 y `article/CLAIM_EVIDENCE_MATRIX.md`, especialmente C15, C16 y C17.

Si el HEAD/tree cambió, no bloquees automáticamente. Evalúa si el drift cambia materialmente el estado real de recursos, scripts, presets, datos, resultados o validación clean-environment. Si sí, detente con `BLOCKED_MATERIAL_REPRO_REPOSITORY_DRIFT` y reporta la diferencia; no redactes desde un snapshot obsoleto.

### 4. Alcance exclusivo

Reemplaza únicamente los placeholders de:

- English: `## 4.8. Reproducibility resources`;
- Spanish: `## 4.8. Recursos de reproducibilidad` o heading equivalente.

No modifiques Sections 1–4.7. No redactes Results, Discussion, Conclusion ni end matter.

La función de 4.8 es explicar **qué recursos públicos existen actualmente, qué permiten reconstruir o preparar, qué permanece restringido/no materializado y cómo se distingue reproducción del estudio de referencia de replicación externa**.

### 5. Contenido obligatorio

#### 5.1 Repositorios y separación de funciones

Explica en prosa científica concisa que:

- el repositorio de desarrollo conserva el historial experimental, artefactos internos, diagnósticos y fuentes congeladas de la campaña;
- el repositorio público `gci-nandina-rag-reproducibility` está destinado al paquete científico limpio de reproducción/replicación;
- no deben confundirse el historial de desarrollo y el paquete público.

No conviertas la sección en una lista de commits o rutas internas.

#### 5.2 Recursos actualmente materializados

Describe solo recursos realmente presentes en el snapshot auditado:

- documentación del protocolo experimental y del contrato de datos;
- requisitos de jerarquía/nomenclatura y corpus normativo;
- reglas de procedencia y redistribución;
- distinción `reference` / `custom` / `synthetic` documentada por el repositorio;
- configuración de ejemplo para datos propios compatibles;
- estructura documental que define los metadatos de manifests, seeds, hashes, versiones, parámetros, entorno y outputs que una release reproducible debe registrar.

Puedes referirte a las **clases** de recursos; no llenes la prosa con hashes o nombres internos salvo que sean esenciales para el lector.

#### 5.3 Estado actual incompleto del paquete de referencia

Debe quedar inequívoco que, en el snapshot auditado para este manuscrito, el repositorio público **todavía no constituye una release de referencia computacional completa**.

No ocultes que todavía no están materializados en el tree auditado:

- el runner canónico `scripts/reproduce_all.py`;
- los runners ejecutables ejemplificados en README;
- un preset Clase-87 congelado en `configs/presets/`;
- dependency lock/`requirements.txt`;
- resultados canónicos de referencia en `results/`;
- datasets administrativos redistribuidos;
- una validación clean-environment documentada de la release final.

Formula esto como una limitación de **estado del paquete público**, no como fallo del diseño experimental ya ejecutado en el repositorio de desarrollo.

Los comandos de README/REPRODUCIBILITY son interfaces objetivo mientras los runners no estén materializados. No los presentes como comandos ya ejecutables si el snapshot vivo no cambia materialmente antes de la redacción.

#### 5.4 Reproducción vs replicación externa

Conserva C17:

- `reference reproduction`: repetir el estudio con un preset/entradas/configuración congelados cuando la release correspondiente esté materializada;
- `external replication`: ejecutar el protocolo con datos propios compatibles y generar un nuevo manifest/result set; no exige acuerdo numérico con el experimento de referencia.

Conserva C15/C16: configurabilidad para otros capítulos, profundidades o jurisdicciones es propiedad de diseño, **no evidencia de generalización empírica**.

#### 5.5 Datos, corpus y redistribución

Explica que:

- los artefactos solo deben redistribuirse cuando su estatus lo permita;
- los CSV administrativos de referencia no se publican automáticamente por existir en desarrollo;
- cuando una entrada requerida no pueda redistribuirse, el contrato prevé documentar, cuando proceda, hash esperado, esquema y ruta/instrucción de reconstrucción o colocación;
- una replicación externa debe registrar su propia procedencia, versiones, hashes, grouping unit, nivel objetivo y restricciones de divulgación.

No afirmes que los datos administrativos de referencia están públicamente disponibles si el snapshot no lo demuestra.

#### 5.6 Recheck pre-submission

Incluye una frase breve que deje la descripción atada al snapshot/versionado del repositorio y que la disponibilidad final será re-verificada antes de submission/freeze. No conviertas esta nota en lenguaje de gestión interna; debe sonar como una frontera reproducible/versionada del recurso.

### 6. Claims autorizados y prohibidos

Autorizados relevantes:

- C15 — configurabilidad para otros capítulos/niveles/jurisdicciones como propiedad de diseño;
- C17 — separación entre reproducción de referencia y replicación externa.

Prohibidos relevantes:

- C16 — generalización empírica demostrada fuera de Chapter 87;
- afirmar una release estable/completa no observada;
- afirmar reproducción one-command/fresh-clone no validada;
- afirmar redistribución pública de datos administrativos no validada;
- inferir corrección jurídica, legal validity o empirical generalization a partir de reproducibilidad/documentación.

`FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

### 7. Estilo

- Prosa de Methods concreta y sobria.
- Evita abstracciones vacías como “enhances reproducibility” sin indicar qué artefacto/contrato lo permite.
- No redactes una enumeración exhaustiva de carpetas o archivos.
- Diferencia explícitamente **documentado/presente**, **planificado/no materializado** y **restringido/no redistribuido**.
- No utilices “fully reproducible” para el snapshot actual.
- No presentes interfaces objetivo como funciones ya congeladas/ejecutables.

### 8. Artefactos obligatorios

Genera exactamente:

1. `article/sections/experimental_design/Experimental_Design_B07_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx`;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V01.md`.

El master Markdown candidato debe derivar de V015 y diferir únicamente en Section 4.8 EN/ES.

El DOCX candidato debe derivar **directamente** del binario exacto B06 V02 y conservar estilos, estructura, comentarios, anchors y contenido anterior. No reconstruyas Word desde Markdown.

### 9. QA obligatorio

Registra en la response:

```text
PROTOCOL_READ = PASS
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
SOURCE_SNAPSHOT_REPRO_HEAD
SOURCE_SNAPSHOT_REPRO_TREE
REPRO_REPOSITORY_DRIFT_ASSESSMENT
AUTHORIZED_CLAIMS_USED
CONDITIONAL_CLAIMS_USED
PROHIBITED_CLAIMS_AVOIDED
BASELINE_MD_SHA256
BASELINE_MD_GIT_BLOB
BASELINE_DOCX_SHA256
SECTION_4_8_ONLY_MD_DIFF
SECTIONS_1_TO_4_7_PRESERVED
RESULTS_PLUS_PRESERVED
EN_ES_EQUIVALENCE
RESULTS_LEAKAGE = NONE
REPRO_STATUS_OVERCLAIMING = NONE
PUBLIC_VS_RESTRICTED_BOUNDARY = PASS
PRESENT_VS_PLANNED_RESOURCE_BOUNDARY = PASS
ZIP_OOXML_INTEGRITY
ZIP_ENTRY_SET
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
MD_DOCX_SEMANTIC_EQUIVALENCE
FULL_DOCX_RENDER
VISUAL_QA
ENGLISH_WORD_COUNT_SECTION_4_8
EXPERIMENTAL_REVIEW_TRIGGER = NOT_REQUIRED_UNLESS_SOURCE_DRIFT_OR_NEW_EXPERIMENTAL_CLAIM
```

La response debe incluir además un apartado breve `MWDP_DELIVERY_CHECKLIST` con:

- onboarding/protocolo leído;
- bloque y versión;
- snapshots de fuentes;
- claims autorizados/condicionales/prohibidos;
- recheck de acceso;
- cobertura de citas si aplica;
- equivalencia EN/ES;
- master candidato;
- word count inglés;
- trigger de revisión experimental.

### 10. Exit

La response debe cerrar con:

```text
B07_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y realiza los handoffs reales de los candidatos MD/DOCX. Detente después de B07.

---

## English

Act only as the scientific Drafting AI for Experimental Design B07 / Section 4.8. Use `ARTICLE_MASTER_V015.md` and the exact B06 V02 DOCX as the sole cumulative baselines. Preserve MWDP v1.0, SPCCR, all inherited comments, and all prior approved content.

Before drafting, live-check `elVladdi/gci-nandina-rag-reproducibility` against the D-079 snapshot. Section 4.8 must accurately separate: (1) resources currently materialized in the public repository; (2) target/planned interfaces and reference-release components not yet materialized; and (3) restricted or not-yet-redistributed reference inputs.

The audited public snapshot documents protocol/data/taxonomy/provenance contracts and includes a custom-data configuration example, but it does not yet contain a complete runnable reference release. Do not claim that one-command fresh-clone reproduction, a frozen Class-87 preset, redistributed administrative reference data, canonical reference results, dependency lock, or clean-environment release validation already exists unless the live source has materially changed and that change is verified before drafting.

Preserve the distinction between reference reproduction and external replication. Configurability is a design property, not evidence of empirical generalization. Do not write Results, Discussion, Conclusion, final-gap, novelty, legal-correctness, or unsupported reproducibility claims.

Create only the B07 section artifact, cumulative B07 Markdown/DOCX candidates, and response V01. The DOCX must derive directly from the exact B06 V02 binary and must not be reconstructed from Markdown.