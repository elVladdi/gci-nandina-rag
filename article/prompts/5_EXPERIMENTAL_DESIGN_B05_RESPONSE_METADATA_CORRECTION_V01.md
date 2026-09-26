# Prompt — Experimental Design B05 response metadata correction — V01

## Español

### Rol y alcance

Actúa como **IA de Redacción** únicamente para corregir la metadata de autocontrol de la response de B05. Esta es una corrección documental atómica posterior a la revisión interna de la IA Gestora.

No redactes ni modifiques contenido científico. No modifiques el artefacto de sección, el master Markdown candidato, el DOCX candidato, gobernanza, estado editorial, plan de redacción, experimentos, `main`, SRC-03 ni ningún archivo distinto de la nueva response V02 indicada abajo.

### Fuentes vinculantes

Lee íntegramente:

1. `article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md@ee7cd01b652d85791c84eeb26398b224038074ca`;
2. `article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_INTERNAL_REVIEW_V01.md@bad6a978ef0a6e70c6db675cf77ff8bf7f2942cf`;
3. `article/CLAIM_EVIDENCE_MATRIX.md` vigente;
4. `article/sections/experimental_design/Experimental_Design_B05_V01.md@44e72613f9750425446d61987edb383e87feb222`.

### Defecto exacto que debe corregirse

La response V01 declara:

```text
CONDITIONAL_CLAIMS_USED = NONE
```

La declaración es incorrecta. La matriz claim–evidencia mantiene C14 en estado `CONDITIONAL`:

> HE4 aporta evidencia sobre estructura, trazabilidad y auditabilidad bajo su protocolo de evaluación — solo con límites explícitos.

La Sección 4.6.3 utiliza ese claim de forma correctamente delimitada: caracteriza las puntuaciones cualitativas como evidencia para analizar estructura, trazabilidad, verificabilidad y auditabilidad bajo el esquema ejecutado, y excluye expresamente validación humana, corrección jurídica, decisión oficial y reconstrucción causal fiel.

### Corrección obligatoria

Genera exclusivamente:

`article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V02.md`

La V02 debe preservar semánticamente toda la response V01 y corregir, en español e inglés, el autocontrol para registrar explícitamente:

```text
CONDITIONAL_CLAIMS_USED = C14 / HE4_STRUCTURE_TRACEABILITY_AUDITABILITY_WITH_EXPLICIT_LIMITATIONS / CONDITIONS_SATISFIED
```

Añade una nota breve en la sección de control científico indicando que:

- C14 es el único claim condicional utilizado en 4.6;
- su uso cumple la condición de límites explícitos;
- no se convierte auditabilidad en legal correctness;
- la modalidad `AI_EXPERT_ROLE / LLM-as-judge` y la ausencia de human scoring permanecen declaradas;
- no existe cambio de contenido científico respecto de `Experimental_Design_B05_V01.md`.

### Identidades que deben conservarse sin cambios

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B05_V01.md
SECTION_ARTIFACT_COMMIT = 44e72613f9750425446d61987edb383e87feb222
SECTION_ARTIFACT_GIT_BLOB = 1cb53e31f86689a6c886e9f7a5e13ea2f5519d99
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
MASTER_CANDIDATE_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = 20105abb745e382b923e4eb43d9a771a722df9e3
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
DOCX_CANDIDATE_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
```

No regeneres ni vuelvas a entregar MD/DOCX. No cambies hashes ni afirmes una nueva auditoría técnica de esos binarios: la revisión de Gestora ya los declaró `PASS`.

### Gate de salida

Cierra la response V02 con:

```text
RESPONSE_METADATA_CORRECTION = COMPLETED_PENDING_GESTORA_AUDIT
SCIENTIFIC_CONTENT_CHANGED = NO
SECTION_ARTIFACT_CHANGED = NO
MASTER_CANDIDATE_MD_CHANGED = NO
MASTER_CANDIDATE_DOCX_CHANGED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

En chat responde únicamente en español e informa la ruta y commit exactos de la response V02. No avances a otro bloque.

---

## English

### Role and scope

Act as the **Drafting AI** only to correct the B05 execution-response self-check metadata. This is an atomic documentary correction after the Managing AI's independent review.

Do not rewrite or modify scientific content. Do not modify the section artifact, cumulative Markdown candidate, cumulative DOCX candidate, governance, editorial status, writing plan, experiments, `main`, SRC-03, or any file other than the new response V02 specified below.

Read in full:

1. `article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md@ee7cd01b652d85791c84eeb26398b224038074ca`;
2. `article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_INTERNAL_REVIEW_V01.md@bad6a978ef0a6e70c6db675cf77ff8bf7f2942cf`;
3. the current `article/CLAIM_EVIDENCE_MATRIX.md`;
4. `article/sections/experimental_design/Experimental_Design_B05_V01.md@44e72613f9750425446d61987edb383e87feb222`.

The V01 statement `CONDITIONAL_CLAIMS_USED = NONE` is incorrect because C14 is `CONDITIONAL` and Section 4.6.3 uses that claim within its explicit required limitations.

Create only:

`article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V02.md`

Preserve the V01 response semantically and change the bilingual self-check to:

```text
CONDITIONAL_CLAIMS_USED = C14 / HE4_STRUCTURE_TRACEABILITY_AUDITABILITY_WITH_EXPLICIT_LIMITATIONS / CONDITIONS_SATISFIED
```

Add a brief bilingual control note stating that C14 is the only conditional claim used in 4.6, its explicit-limit condition is satisfied, auditability is not converted into legal correctness, `AI_EXPERT_ROLE / LLM-as-judge` and `human_scoring=false` remain explicit, and no scientific manuscript content changed.

Preserve the section/MD/DOCX identities listed in the Spanish instructions exactly. Do not regenerate or redeliver those artifacts.

Stop with:

```text
RESPONSE_METADATA_CORRECTION = COMPLETED_PENDING_GESTORA_AUDIT
SCIENTIFIC_CONTENT_CHANGED = NO
SECTION_ARTIFACT_CHANGED = NO
MASTER_CANDIDATE_MD_CHANGED = NO
MASTER_CANDIDATE_DOCX_CHANGED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Respond in Spanish in chat with only the exact response V02 path and commit. Do not advance to another block.