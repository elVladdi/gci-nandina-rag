# D-075 — Autorización de ejecución de la corrección estrecha B06 / B06 narrow-correction execution authorization

## Español

```text
DECISION_ID = D-075
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-074
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CORRECTION_SCOPE = B06-C01 / B06-C02 / B06-C03 / B06-C04 ONLY
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
AUTHORIZED_PROMPT_GIT_BLOB = 90592518a2197ee6a7889797bf43da60b8b06fcf
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_NARROW_METHODS_CORRECTION_PROMPT_REVIEW_V01.md@024fa0eb8a47425c49241ac0db4bd929bcfbf202
PROMPT_REVIEW_RESULT = PASS
B06_STATE = REVISION_REQUIRED / NARROW_CORRECTION_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Autorización

Después de la auditoría independiente B06 V01 (`PASS WITH CORRECTIONS`) y de la revisión `PASS` del prompt correctivo, se autoriza exclusivamente la ejecución del microgate definido en `5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md`.

Ningún otro prompt B06 correctivo queda autorizado de forma concurrente. D-075 no reabre Sections 1–4.6 ni autoriza Section 4.8 o Results.

### 2. Baselines obligatorios

La IA de Redacción debe recibir y usar como únicos baselines de edición:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

No se permite editar desde V014/B05 ni reconstruir el DOCX desde Markdown.

### 3. Correcciones autorizadas

El microgate se limita a:

- B06-C01: matriz común de remuestreo `10000 × 67`, 67 clusters DAM y regla de multiplicidad;
- B06-C02: Top-50 suplementaria con IC 95% y medida de efecto pareada no estandarizada;
- B06-C03: reglas metodológicas HE5 omitidas;
- B06-C04: identidades correctas de las dos fuentes Group-3 en la response.

### 4. Estado de salida esperado

La ejecución debe producir los artefactos B06 V02 y volver a IA Gestora para auditoría diferencial. No se abre automáticamente el gate autoral.

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B06_V01_NARROW_METHODS_CORRECTION
EXPECTED_SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
EXPECTED_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-075
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-074
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
AUTHORIZED_PROMPT_GIT_BLOB = 90592518a2197ee6a7889797bf43da60b8b06fcf
PROMPT_REVIEW_RESULT = PASS
B06_STATE = REVISION_REQUIRED / NARROW_CORRECTION_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

D-075 authorizes only the independently reviewed narrow B06 correction contract. The exact B06 V01 Markdown and DOCX candidates are the sole editing baselines; returning to V014/B05 or reconstructing the DOCX from Markdown is prohibited.

Execution is limited to B06-C01 through B06-C04. The expected B06 V02 section artifact, cumulative Markdown/DOCX candidates, and response must return to the Managing AI for differential audit. This decision does not open author approval, Section 4.8, or Results.