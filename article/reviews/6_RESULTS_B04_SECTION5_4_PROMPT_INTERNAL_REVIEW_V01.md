# Internal review — Results B04 / Section 5.4 prompt — V01

## Español

```text
REVIEW = 6_RESULTS_B04_SECTION5_4_PROMPT_INTERNAL_REVIEW_V01
PROMPT = article/prompts/6_RESULTS_B04_SECTION5_4.md
PROMPT_COMMIT = 290d8668f138839cfce11752fc1010e778ddee31
PROMPT_GIT_BLOB = 98161fb0e606205cc6c429c81765c59b5ade3a23
GROUND_TRUTH_DECISION = D-104
CANONICAL_MASTER = ARTICLE_MASTER_V019
VERDICT = PASS
```

### 1. Baselines

`PASS`.

El prompt fija correctamente:

```text
ARTICLE_MASTER_V019.md
SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e

ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40
TRACKED_CHANGES = 0
```

El alcance diferencial restringe la edición a §5.4 EN/ES y mantiene §5.5+ cerrada.

### 2. Fuentes experimentales

`PASS`.

El prompt vincula exclusivamente el snapshot `main@db0d0ad0d8435921a7838db6720eaea86a263763` y los artefactos HE4 congelados de D-104, con sus blobs exactos. No habilita literatura, resultados históricos ni fuentes mutables como reemplazo.

### 3. Ground truth numérico

`PASS`.

El contrato preserva los objetos medidos correctos:

- 50 casos / 150 slots;
- preservación estructural y trazabilidad en 50/50 casos y referencias/rank válidos en 150/150 slots;
- `automatic_validation_pass = NOT_APPLICABLE`;
- `schema_compliance = 0/50` bajo `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- 28/50 casos auditables, 22/50 no auditables, media 11.72, mediana 12, rango 6–15, 0 hard violations;
- las ocho medias dimensionales congeladas;
- warning control 41/50 y comparación descriptiva 1/9 vs 27/41;
- modalidad real `AI_EXPERT_ROLE`, `llm_as_judge=true`, `human_scoring=false`.

No se introduce una tasa automática retrospectiva ni inferencia inexistente.

### 4. Límites de interpretación

`PASS`.

El prompt impide explícitamente:

- legal/substantive normative correctness;
- overall classification accuracy;
- human expert validation;
- causal faithfulness;
- external generalization;
- inferencia/significancia en comparaciones descriptivas;
- leakage de §5.5/§5.6/Discussion.

C13 permanece prohibido y C14 no se usa como claim paraguas sin límites. C35–C41 quedaron registrados como claims específicos autorizados antes de abrir drafting.

### 5. Transparencia sobre limitaciones

`PASS`.

El prompt obliga a reportar tanto fortalezas como debilidades y evita cherry-picking. Requiere conservar la baja verificabilidad media (0.54), la separación histórico-normativa (1.04), el 56% de casos auditables, el mismatch prompt-schema y la desviación de modalidad del evaluador.

### 6. MWDP / D-035

`PASS`.

Se preservan continuidad DOCX, 40 comentarios, 0 tracked changes y entrega timeout-safe. No se autoriza reconstrucción desde Markdown, Base64 manual, chunking, fragmentación, reensamblado ni materialización GitHub del master grande.

### 7. Dictamen

```text
SCIENTIFIC_SCOPE = PASS
SOURCE_BINDING = PASS
NUMERICAL_GROUND_TRUTH = PASS
CLAIM_GOVERNANCE = PASS
INTERPRETATION_BOUNDARIES = PASS
DIFFERENTIAL_SCOPE = PASS
DOCX_CONTINUITY = PASS
D035 = PASS
PROMPT_REVIEW = PASS
```

Se recomienda autorizar exclusivamente B04 V01 bajo este prompt. B05+, Discussion y Conclusion permanecen cerradas.

---

## English

The B04 prompt passes internal review. It binds the exact V019/B03 DOCX baselines, frozen HE4 sources, numerical ground truth, schema-mismatch interpretation, actual AI-evaluator modality, and C35–C41 claim boundaries. It prohibits retrospective automatic-pass construction, human-validation claims, legal correctness, overall accuracy, causal faithfulness, external generalization, and leakage into later Results/Discussion. Differential scope and D-035 controls are adequate.