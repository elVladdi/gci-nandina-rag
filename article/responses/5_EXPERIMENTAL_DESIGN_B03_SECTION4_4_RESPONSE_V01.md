# Respuesta — Experimental Design B03 / Section 4.4

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B03_SECTION_4_4
VERSION = V01
ROLE = DRAFTING_AI
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4.md@8c3f845f419d84fa1f03c59482e8ebdb25b217c6
GOVERNING_DECISION = D-056
PARENT_DECISION = D-055
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V011.md
BASELINE_MASTER_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f / PASS
BASELINE_MASTER_GIT_BLOB = c2aee16c219ed33c16e8e647fbd56f4dacc2cd61 / PASS
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
SRC03_MATERIAL_CHANGE_FOR_4_4 = NO
AUTHORIZED_SCOPE = SECTION_4_4_ONLY
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
DISCUSSION = NOT_AUTHORIZED / NOT_DRAFTED
CONCLUSION = NOT_AUTHORIZED / NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Onboarding y estado

Se completó el onboarding obligatorio mediante lectura directa de `START_HERE.md`, `README.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`, D-055, D-056 y el prompt gobernante. Se detectó que `ARTICLE_STATUS.md` y parte de `ARTICLE_WRITING_PLAN.md` aún conservan un estado administrativo anterior asociado a D-053/V010; esta discrepancia no se resolvió por inferencia ni se modificaron esos archivos. D-055 y D-056, posteriores y vinculantes, junto con la identidad exacta del master V011 fijada por el prompt, gobiernan esta ejecución.

### Fuentes experimentales verificadas

Se consultó directamente el `SRC-03` vivo en `docs/plan-maestro-temporal-2026-08-31` y el repositorio de desarrollo `main`, sin modificar ninguno. Para las afirmaciones de 4.4 se verificaron, entre otras, las siguientes fuentes primarias:

- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json` — composición v0.2, solapamiento DAM=`0`, solapamiento `id_unico`=`0`, asignación completa, soporte histórico de `1056/1056` series y `42/42` códigos de evaluación, controles de duplicados exactos y diagnósticos near-duplicate;
- `src/configs/data_aduanas_split_clase87_v0.2.json` — asignaciones explícitas de DAM y requisitos de no solapamiento/soporte histórico;
- `data/processed/data_aduanas_splits_clase87_v0.1_metadata.json` y `src/evaluation/build_data_aduanas_splits.py` — naturaleza histórica del split v0.1 y muestreo a nivel de fila/serie estratificado por NANDINA, sin restricción de agrupamiento por DAM;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md` — SERIE como unidad de análisis, DAM como unidad de agrupamiento cuando existe dependencia y límites interpretativos del rediseño v0.2.

### Claims principales y evidencia

| Claim de Methods | Evidencia primaria / control | Límite preservado |
|---|---|---|
| v0.1 podía distribuir series de una misma DAM entre particiones porque su construcción no imponía agrupamiento por DAM | metadata v0.1 + `build_data_aduanas_splits.py` + ground truth 0A-02 | v0.1 se presenta solo como snapshot histórico; no se usa `48/59` ni se afirma leakage observado como hecho más amplio |
| v0.2 materializa particiones mediante asignaciones explícitas y mutuamente excluyentes de DAM | config v0.2 + metadata v0.2 | `seed=2026` se mantiene como procedencia/configuración, no como mecanismo de asignación v0.2 |
| H100=2950/28/66, DEV=100/6/9 y EVAL=1056/67/42 | metadata v0.2 | cifras estructurales de diseño, no métricas de desempeño |
| el solapamiento entre particiones es 0 para DAM y 0 para `id_unico` | metadata/config v0.2 | unicidad de identificadores no se equipara con independencia estadística |
| las 1056 series y los 42 códigos de EVAL tienen soporte histórico nominal | metadata v0.2 | soporte de clase no implica recuperar el código de referencia en un rank concreto |
| duplicados exactos y near-duplicates son controles diferentes del agrupamiento por DAM | metadata v0.2 | los umbrales Jaccard 0.90/0.95/0.98 se describen como diagnósticos, no filtros de exclusión |
| separación entre particiones por DAM no vuelve independientes a las series dentro de una DAM | ground truth 0A-02 + C07 | no se declara i.i.d.; los procedimientos inferenciales quedan para 4.7 |

### Artefactos

```text
SECTION_MD = article/sections/experimental_design/Experimental_Design_B03_V01.md
SECTION_MD_GIT_BLOB = 672fdeceef0e5eb5bb63e3d2349208ba7e86c33b
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md
MASTER_CANDIDATE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
MASTER_CANDIDATE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = dfea73f5f462fc65cf98347f796deadc6da58455
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED_TO_GESTORA_UNDER_D035_TIMEOUT_SAFE_HANDOFF
DOCX_CANDIDATE = NOT_REQUIRED_BY_THIS_PROMPT / NOT_GENERATED
```

El master acumulativo candidato se generó a partir de una copia local cuya identidad coincide exactamente con `ARTICLE_MASTER_V011.md` (mismo SHA-256 y Git blob). El control diferencial confirma que solo cambiaron los bloques inglés y español de 4.4: el prefijo hasta 4.4, el tramo desde 4.5 inglés hasta 4.4 español y el sufijo desde 4.5 español permanecen textualmente idénticos al baseline. Conforme al patrón D-035 para artefactos acumulativos grandes, el archivo exacto se entrega al autor como adjunto descargable y su materialización GitHub queda diferida a la IA Gestora; no se utilizó Base64 manual, fragmentación, chunking, recomposición ni reconstrucción del master.

### QA y fronteras

```text
EN_ES_SEMANTIC_EQUIVALENCE = PASS
SECTIONS_1_TO_4_3_MODIFIED = NO
SECTION_4_5_AND_LATER_MODIFIED = NO
RESULTS_LEAKAGE = NONE
SERIE_ANALYSIS_UNIT = PRESERVED
DAM_GROUPING_UNIT = PRESERVED
V0_1_V0_2_SEPARATION = PASS
SEED_AS_V02_ASSIGNMENT_MECHANISM = NO
DUPLICATES_NEAR_DUPLICATES_DAM_DEPENDENCE_COLLAPSED = NO
IID_INDEPENDENCE_CLAIM = NO
TOTAL_LEAKAGE_ELIMINATION_CLAIM = NO
GENERALIZATION_BEYOND_TESTBED = NO
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

La ejecución se detiene en 4.4 y vuelve a la IA Gestora para auditoría independiente claim-by-claim y control diferencial.

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B03_SECTION_4_4
VERSION = V01
ROLE = DRAFTING_AI
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4.md@8c3f845f419d84fa1f03c59482e8ebdb25b217c6
GOVERNING_DECISION = D-056
PARENT_DECISION = D-055
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V011.md
BASELINE_MASTER_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f / PASS
BASELINE_MASTER_GIT_BLOB = c2aee16c219ed33c16e8e647fbd56f4dacc2cd61 / PASS
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
SRC03_MATERIAL_CHANGE_FOR_4_4 = NO
AUTHORIZED_SCOPE = SECTION_4_4_ONLY
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Mandatory onboarding and direct primary-source verification were completed. The live experimental source and development `main` were read without modification. The verified evidence supports the legacy v0.1 row-level split risk, explicit DAM-level v0.2 assignments, zero DAM and `id_unico` overlap, frozen partition composition, historical support for all evaluation series/codes, and the separation among DAM grouping, record identity, exact duplicates, and Jaccard-based near-duplicate diagnostics. The 0.90/0.95/0.98 similarity thresholds are described only as diagnostics, not exclusion filters.

The cumulative candidate was derived from an exact local copy of `ARTICLE_MASTER_V011.md`. Differential QA confirms that only the English and Spanish Section 4.4 blocks changed; Section 4.5 and all later content remain unchanged and undrafted. Under the D-035 timeout-safe handoff pattern for large cumulative artifacts, the exact master candidate is handed directly to the author with SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`; GitHub materialization of that large candidate is deferred to the Managing AI. No manual Base64, fragmentation, chunking, or reconstruction was used.

```text
SECTION_MD = article/sections/experimental_design/Experimental_Design_B03_V01.md
SECTION_MD_GIT_BLOB = 672fdeceef0e5eb5bb63e3d2349208ba7e86c33b
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md
MASTER_CANDIDATE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
MASTER_CANDIDATE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = dfea73f5f462fc65cf98347f796deadc6da58455
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED_TO_GESTORA_UNDER_D035_TIMEOUT_SAFE_HANDOFF
SECTION_4_5_PLUS = NOT_DRAFTED
RESULTS = NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

`EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT`
