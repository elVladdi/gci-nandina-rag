# Prompt — Experimental Design B05 / Section 4.6 — V01

## Español

### Rol

Actúa como **IA de Redacción** del artículo científico principal destinado a *Knowledge-Based Systems*. Ejecuta exclusivamente `EXPERIMENTAL_DESIGN_B05`, limitado a Section 4.6, sus subsecciones 4.6.1–4.6.3 y su espejo español.

No eres la autoridad de cierre experimental ni editorial. No modifiques experimentos, datos, métricas, scripts, `main`, SRC-03, Plan Maestro, decisiones, reviews, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni gobernanza.

### 1. Onboarding obligatorio — orden exacto

Trabaja en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Antes de redactar, lee íntegramente y **en este orden exacto**:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. este prompt completo: `article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md`.

Después lee íntegramente:

10. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — MWDP v1.0;
11. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` — SPCCR;
12. `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
13. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
14. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
15. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`;
16. `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
17. `article/governance/D066_EXPERIMENTAL_DESIGN_B04_INTEGRATION_AND_V013_PROMOTION.md`;
18. `article/governance/D067_EXPERIMENTAL_DESIGN_B05_SECTION4_6_GROUND_TRUTH_SYNC.md`;
19. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
20. `article/manuscript/ARTICLE_MASTER_V013.md`.

Registra en la response, antes de los resultados de ejecución:

```text
ARCHIVOS_LEIDOS = [...]
FASE_ACTIVA = EXPERIMENTAL DESIGN
ESTADO_BLOQUE_ASIGNADO = B05 / SECTION 4.6 / AUTHORIZED_BY_THIS_PROMPT_ONLY_IF_EXECUTION_DECISION_IS_ACTIVE
REDACCION_AUTORIZADA = SI / NO
DECISIONES_CONGELADAS_RELEVANTES = [...]
CLAIMS_AUTORIZADOS_RELEVANTES = [...]
CLAIMS_PROHIBIDOS_O_PENDIENTES_RELEVANTES = [...]
FUENTES_EXTERNAS_QUE_DEBEN_VERIFICARSE = [SRC-03, main, artefactos primarios]
BLOQUEOS_O_CONTRADICCIONES_DETECTADOS = NONE / [detalle]
```

Si cualquier control vivo indica que este prompt aún no está autorizado para ejecución, detente sin redactar.

### 2. Baselines exactos obligatorios

#### 2.1 Markdown canónico

Usa exclusivamente:

`article/manuscript/ARTICLE_MASTER_V013.md`

Identidad obligatoria:

- SHA-256: `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`;
- Git blob: `06beaa052e2f1bcc630647040762fe78d3838a62`.

Verifica el Git blob antes de editar. Si no coincide, detente con `BLOCKED_BASELINE_MD_DRIFT`.

#### 2.2 DOCX acumulativo

El autor debe adjuntar exactamente:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`

SHA-256 obligatorio:

`cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`

Calcula el hash antes de modificarlo. Si falta o no coincide, detente con:

`BLOCKED_MISSING_EXACT_B04_V02_DOCX_BASELINE`

Está prohibido reconstruir el DOCX desde Markdown, HTML, PDF, texto plano o un Word anterior.

### 3. Único alcance científico autorizado

Redacta exclusivamente:

- `4.6 Evaluation framework and protocols`;
- `4.6.1 Candidate-retrieval evaluation`;
- `4.6.2 Documentary-evidence evaluation`;
- `4.6.3 Controlled-explanation evaluation`;
- el espejo semántico español completo de esas cuatro piezas.

La función congelada es:

`RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida`.

No redactes 4.7, 4.8 ni Results. No reabras Sections 1–4.5.

### 4. Research questions gobernantes

El master canónico fija:

- **RQ1:** desempeño de candidate retrieval histórico bajo particiones disjuntas por DAM;
- **RQ2:** asociación de evidencia normativa identificable con cada candidato del Top-3 fijo sin alterar el orden;
- **RQ3:** preservación del Top-3/orden y producción de explicaciones estructuradas vinculadas a evidencia por un LLM local restringido;
- **RQ4:** límites de validez asociados con dependencia intra-DAM, near-duplicates, composición histórica y drift normativo.

En 4.6, RQ1–RQ3 deben mapearse explícitamente a sus protocolos. RQ4 se menciona únicamente para señalar que sus procedimientos de dependencia/robustez se desarrollan en 4.4 y 4.7; no dupliques esos contenidos.

### 5. Sincronización viva obligatoria antes de redactar

Consulta directamente:

- SRC-03: rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- `main` vivo del repositorio de desarrollo;
- los artefactos primarios requeridos abajo.

Registra HEAD/blob observados. El corte conocido al emitir este prompt es:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

No los asumas inmutables. Si existe drift, determina si altera materialmente los protocolos de 4.6. Si existe contradicción científica no reconciliable con evidencia primaria, detente con `EXECUTION_STOPPED / REQUIRES_GESTORA_REVIEW`.

### 6. 4.6.1 — Candidate-retrieval evaluation

Consulta como mínimo:

- `docs/analysis/group3/g3_analytical_contract_v0.1.md`;
- artefactos congelados de historical retrieval v0.2 necesarios para verificar definiciones de ranking/métrica;
- las familias normativas corregidas comparables identificadas por el contrato G3 cuando necesites describir la lógica comparativa;
- artefactos adicionales solo si son necesarios para verificar un claim metodológico.

La redacción debe establecer, sin reportar valores observados:

1. SERIE como unidad primaria de evaluación de candidate retrieval;
2. presencia/posición del código de referencia en el ranking como objeto medido;
3. Top-1, Top-3, Top-5, Top-10 y MRR@100 como métricas primarias del protocolo HE2_A; Top-50 únicamente como métrica suplementaria si su inclusión mejora la claridad;
4. que el desempeño histórico se compara bajo el contrato congelado con las familias normativas comparables autorizadas —flat, hierarchical y D1a corregidas— sin confundir esos comparadores con la ruta primaria del framework;
5. que deep coverage/HE2_B es una dimensión distinta del early ranking, con Recall@100 y Recall@200/Pool@200 según el contrato congelado;
6. que candidate-pool variants de Phase E funcionan como inventarios descriptivos de cobertura y no como sustitutos del ranking histórico principal;
7. la interpretación permitida: estas métricas evalúan **recuperación/ranking de candidatos**, no accuracy global del sistema ni corrección jurídica.

No desarrolles aquí bootstrap, intervalos, multiplicidad, sensibilidad H25/H50/H75/H150/H200 o decisión de hipótesis; corresponden principalmente a 4.7 y Results.

### 7. 4.6.2 — Documentary-evidence evaluation

Consulta como mínimo:

- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json`;
- `integration_evidence_coverage.json`;
- `integration_traceability.json`;
- `integration_ranking_invariance.json`;
- `integration_top3_invariance.json`;
- `integration_missing_exact_evidence.csv` únicamente si necesitas comprender la definición protocolaria, no para narrar su resultado;
- código/configuración Phase F si una definición no queda probada por metadata.

Describe el protocolo sobre el **Top-3 histórico ya fijado**. Debe quedar claro:

1. la unidad puede expresarse a nivel de candidate slot y, cuando corresponda, caso;
2. la evidencia exacta se evalúa por disponibilidad de asociación NANDINA-8 al candidato;
3. el contexto jerárquico puede caracterizarse separadamente (HS6/HS4/chapter), sin promover parent context a evidencia exacta;
4. se evalúa la disponibilidad del precedente histórico y la trazabilidad candidato–precedente–evidencia;
5. se controla invariancia de composición/orden del ranking Top-3 tras asociar evidencia;
6. el label de evaluación no participa en la selección/asociación y solo se utiliza posteriormente cuando una métrica lo requiere;
7. la interpretación permitida es **cobertura, asociación y trazabilidad documental**; no legal correctness ni substantive normative correctness.

No reportes en Methods tasas observadas, por ejemplo `1.0`, `100%`, `3168/3168`, `1056/1056` o cualquier outcome de Phase F.

### 8. 4.6.3 — Controlled-explanation evaluation

Consulta directamente:

- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_scoring_guide_v0.2.md`;
- `gate_j_automatic_validation_manifest_v0.2.json`;
- `gate_k_pre_scoring_manifest_v0.2.json`;
- `gate_k_qualitative_evaluation_manifest_v0.2.json`;
- `he4_sample_profile_v0.2.json`;
- los artefactos frozen de rúbrica/review packet identificados en manifests cuando sean necesarios para confirmar definiciones.

Mantén dos capas separadas:

#### 8.1 Controles automáticos

Explica las familias de checks estructurales y de trazabilidad, tales como:

- preservación del Top-3 y del orden;
- ausencia de códigos externos o duplicados;
- consistencia de rank;
- validez/trazabilidad de referencias histórica y normativa;
- presencia de comparación y advertencias requeridas según el contrato aplicable;
- parseo/estructura del artefacto;
- ausencia de leakage explícito de label.

No inventes un `automatic_validation_pass` por caso: el manifiesto congelado registra que no existía una regla pre-generación de PASS/FAIL por caso para ese campo.

#### 8.2 Evaluación cualitativa

Describe las ocho dimensiones congeladas, puntuadas 0–2:

1. traceability;
2. verifiability;
3. separation of historical and normative evidence;
4. prudence of the conclusion;
5. consistency with the fixed Top-3;
6. detection of generic normative evidence;
7. comparison among candidates;
8. utility for human audit.

Criterio congelado de ficha auditable:

`total >= 12/16 AND no hard violation`.

Hard constraints:

- Top-3 exactamente preservado y ordenado;
- ningún código fuera de `top3_original`;
- ninguna clasificación oficial ni afirmación categórica de código definitivamente correcto;
- conclusión formulada como apoyo documental para revisión experta;
- JSON estricto en el artefacto técnico.

`advertencias_globales` queda fuera del scoring por el mismatch prompt-schema congelado.

#### 8.3 Muestra y modalidad del evaluador

La muestra cualitativa congelada contiene 50 casos seleccionados determinísticamente por support bucket, support count, exact rank y `case_id`, con seed 2026. La composición es:

- `difficult_low_support`: 10;
- `rank_1`: 15;
- `rank_2_3`: 15;
- `rank_4_10`: 10.

La modalidad efectiva del evaluador fue `AI_EXPERT_ROLE / LLM-as-judge`, **no human scoring**. El manifiesto registra una `EVALUATOR_MODALITY_DEVIATION` respecto de la modalidad originalmente prevista `HUMAN/MANUAL REVIEW`. Ground truth, reference rank y bucket no fueron expuestos al evaluador; no utilizó evidencia externa ni web.

Esta limitación metodológica debe expresarse con claridad y neutralidad. No presentes la evaluación como revisión humana ni ocultes la desviación de modalidad.

La interpretación permitida se limita a estructura, trazabilidad, verificabilidad y auditabilidad bajo el protocolo definido. No implica corrección jurídica, validez oficial de clasificación ni reconstrucción causal fiel de por qué el ranking upstream fue producido.

### 9. Contenido que pertenece a 4.7 o Results y está prohibido aquí

No incluyas:

- valores observados Top-k, MRR, cobertura, invariancia o scores HE4;
- `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE` o cualquier decisión de hipótesis;
- intervalos, p-values, estimaciones bootstrap o decisiones inferenciales;
- resultados EXP11A/EXP11B/0B-05C;
- resultados de hard violations o proporción de casos auditables;
- conclusiones de superioridad, degradación o equivalencia entre métodos;
- resultados por bucket de HE4;
- Discussion/literature contrast;
- novelty o final gap.

Si un artefacto fuente contiene valores de Results junto con definiciones metodológicas, extrae únicamente las definiciones necesarias para 4.6.

### 10. Estilo científico

- Prosa directa, concreta y verificable; evita abstracciones vacías.
- No conviertas Methods en inventario de rutas, hashes o nombres internos.
- Introduce identificadores técnicos solo cuando sean necesarios para comprender o reproducir el protocolo.
- Evita repetir 4.4 y 4.5.
- Explica qué se evaluó, sobre qué unidad, con qué criterio y qué interpretación permite.
- Part I English publication-facing primero; Part II español como espejo semántico completo.
- No hagas claims más fuertes en un idioma que en el otro.

### 11. Entregables obligatorios

Versiona en GitHub:

1. `article/sections/experimental_design/Experimental_Design_B05_V01.md`
   - trazabilidad;
   - Part I English;
   - Part II Spanish.

2. `article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md`
   - onboarding;
   - HEAD/blob de SRC-03 y commit de `main` observados;
   - matriz claim/protocolo → fuente primaria;
   - verificación de ausencia de Results leakage;
   - QA Markdown/DOCX;
   - hashes finales.

Genera localmente desde V013 exacto:

3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md`

Solo pueden sustituirse los placeholders de 4.6/4.6.1/4.6.2/4.6.3 en Part I y Part II. Sections 1–4.5 y 4.7+ deben permanecer sin cambios de contenido.

Genera además, partiendo **solo** del DOCX B04 V02 exacto:

4. `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx`

El DOCX debe entregarse efectivamente al autor y permanecer bajo custodia local; no lo subas a GitHub salvo instrucción expresa posterior.

### 12. QA obligatorio

#### Markdown

- baseline V013 blob = PASS;
- solo placeholders de 4.6–4.6.3 EN/ES sustituidos;
- Sections 1–4.5 sin cambios = PASS;
- Sections 4.7+ sin cambios = PASS;
- equivalencia EN/ES = PASS;
- Results leakage = NONE.

#### DOCX

- SHA-256 baseline B04 V02 = PASS;
- ZIP/OOXML integrity = PASS;
- XML/RELS parse = PASS;
- comentarios heredados: 40 starts / 40 ends / 40 references preservados;
- no comments nuevos salvo necesidad bibliográfica expresamente justificada;
- tracked changes = 0;
- 4.6–4.6.3 EN presente = PASS;
- 4.6–4.6.3 ES presente = PASS;
- 4.7 boundary EN/ES preservada = PASS;
- Sections 1–4.5 y 4.7+ sin mutación de contenido = PASS;
- equivalencia MD/DOCX = PASS;
- render completo = PASS, sin clipping, truncamiento, superposición o pérdida material de formato.

### 13. Autocontrol obligatorio

Antes de cerrar verifica:

```text
RQ1 -> CANDIDATE_RETRIEVAL_PROTOCOL
RQ2 -> DOCUMENTARY_EVIDENCE_PROTOCOL
RQ3 -> CONTROLLED_EXPLANATION_PROTOCOL
RQ4 -> VALIDITY_ROBUSTNESS_BOUNDARY_ONLY
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
AUTOMATIC_CHECKS != QUALITATIVE_RUBRIC
QUALITATIVE_EVALUATOR = AI_EXPERT_ROLE / LLM_AS_JUDGE
HUMAN_SCORING = FALSE
SECTION_4_7_CONTENT = NONE
RESULTS_VALUES_IN_4_6 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 14. Gate de salida

Detente después de B05 V01, los masters candidatos y la response versionada.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Responde únicamente en español en chat y entrega el DOCX candidato como archivo descargable.

---

## English

### Role and exact scope

Act as the **Drafting AI** for the main *Knowledge-Based Systems* article. Execute only `EXPERIMENTAL_DESIGN_B05`, limited to Section 4.6, Sections 4.6.1–4.6.3, and their full Spanish semantic-control mirror. Do not modify experiments, data, scripts, experimental branches, governance, status/plan files, or any section outside this scope.

### Mandatory onboarding

Read, in this exact order: `START_HERE.md → README.md → ARTICLE_STATUS.md → ARTICLE_WRITING_PLAN.md → DECISIONS.md → SOURCE_REGISTRY.md → CLAIM_EVIDENCE_MATRIX.md → STYLE_GUIDE.md → this task prompt`. Then read MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-066, D-067, Structure V02, and canonical `ARTICLE_MASTER_V013.md`. Record the required onboarding fields in the versioned response. If live controls do not authorize execution of this prompt, stop before drafting.

### Exact cumulative baselines

Markdown baseline: `article/manuscript/ARTICLE_MASTER_V013.md`, SHA-256 `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`, Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`.

DOCX baseline: `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`, SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`. If this exact binary is unavailable or mismatched, stop with `BLOCKED_MISSING_EXACT_B04_V02_DOCX_BASELINE`. Never reconstruct the DOCX from Markdown or an older Word file.

### Scientific function

Section 4.6 must map `RQ → system function → output → evaluation unit → metric/protocol → permitted interpretation`. RQ1 maps to candidate retrieval, RQ2 to documentary-evidence association, and RQ3 to controlled explanation. RQ4 is only a validity/robustness boundary here because its procedures are handled by Sections 4.4 and 4.7.

### Candidate retrieval

Use the frozen Group-3 analytical contract and primary retrieval artifacts. Define SERIE as the primary evaluation unit and the reference code's presence/rank as the measured object. The primary HE2_A metrics are Top-1, Top-3, Top-5, Top-10, and MRR@100; Top-50 is supplementary. The eligible comparison families are corrected flat normative, hierarchical normative, and D1a, but these comparators must not be confused with the framework's primary historical-ranking path. Deep coverage/HE2_B is separate from early ranking and uses Recall@100 and Recall@200/Pool@200 under the frozen contract. Phase-E candidate pools are descriptive coverage inventories. Do not develop inference/robustness procedures here; they belong primarily in Section 4.7. Candidate retrieval is not overall classification accuracy.

### Documentary evidence

Use Phase-F integration metadata and traceability/coverage/invariance artifacts to define the protocol over an already fixed historical Top-3. Describe candidate-slot/case-level evidence availability, exact NANDINA-8 association, hierarchical context where applicable, historical-precedent coverage, candidate–precedent–evidence traceability, and Top-3/ranking invariance. Parent context must not be promoted to exact evidence. Evaluation labels do not participate in evidence selection. Do not report observed coverage/invariance rates. Documentary association/coverage is not substantive normative or legal correctness.

### Controlled explanation

Keep automatic structural/traceability controls separate from qualitative evaluation. Automatic checks include Top-3/order preservation, external/duplicate-code absence, rank consistency, historical/normative reference validity, traceability, comparison/required-warning structure where applicable, parse/format controls, and explicit-label leakage controls. Do not invent a retrospective per-case automatic PASS rule.

The frozen qualitative rubric has eight 0–2 dimensions: traceability, verifiability, historical/normative separation, prudence, fixed-Top-3 consistency, detection of generic normative evidence, candidate comparison, and utility for human audit. A case is auditable at `>=12/16` with no hard violation. Hard constraints are exact Top-3/order preservation, no outside codes, no official/categorical classification claim, documentary-support framing for expert review, and strict JSON in the technical artifact. `advertencias_globales` is excluded from scoring because of the frozen prompt-schema mismatch.

The qualitative sample contains 50 deterministically selected cases: 10 difficult/low-support, 15 rank-1, 15 rank-2/3, and 10 rank-4/10 cases, selected by frozen support/rank criteria with seed 2026. The actual evaluator modality was `AI_EXPERT_ROLE / LLM-as-judge`, not human scoring. The frozen manifest records an evaluator-modality deviation from the originally planned human/manual modality. Ground truth, reference rank, bucket, external evidence, and web information were not exposed/used. State this limitation clearly. Auditability is not legal correctness.

### Prohibited content

Do not include observed Top-k/MRR, coverage, invariance, HE4 score or auditability rates; HE2/HE5 dispositions; bootstrap intervals, p-values or inferential decisions; EXP11A/EXP11B/0B-05C outcomes; bucket results; literature contrast; novelty; final gap; or any Results prose. Section 4.7, 4.8, Results, Discussion, and Conclusion remain closed.

### Deliverables and QA

Version `article/sections/experimental_design/Experimental_Design_B05_V01.md` and `article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md`. Generate cumulative `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md` from exact V013 and `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` from the exact B04 V02 DOCX. Only the 4.6/4.6.1/4.6.2/4.6.3 placeholders may be replaced in both language parts.

Verify baseline identities, differential scope, EN/ES equivalence, absence of Results leakage, OOXML integrity and XML/RELS parsing, preservation of all 40 inherited comment starts/ends/references, zero tracked changes, MD/DOCX semantic equivalence, preservation of the 4.7 boundary, and a complete visual render without clipping or truncation. Deliver the DOCX to the author under local custody; do not upload it to GitHub unless expressly instructed.

Stop after B05 V01 with:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```