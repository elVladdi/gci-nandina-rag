# Introduction B01 — Technical closure after author approval

## 1. Objective único

Ejecuta exclusivamente el cierre técnico pendiente de `INTRODUCTION_B01_V02` ya aprobada por el autor.

**NO redactes, NO corrijas y NO reinterpretes contenido científico.**

El objetivo único es materializar en GitHub los dos Markdown exactos ya generados durante V02 y cerrar su trazabilidad. Después, detente.

## 2. Gobernanza obligatoria

Lee y aplica:

- `article/reviews/3_INTRODUCTION_B01_INTERNAL_REVIEW_V02.md@c611712b329f97c9d66b547cee8f469b0ab4f007`;
- `article/reviews/3_INTRODUCTION_B01_AUTHOR_APPROVAL_V01.md@4503f4664286bb09ab9e40a19de8e10b76a77090`;
- `article/governance/D031_INTRODUCTION_B01_AUTHOR_APPROVAL_AND_TECHNICAL_CLOSURE_GATE.md@a68c50cdd7215436b2ee2b802d13b700f86d2af8`;
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V04.md@d1057e570e3d43f69f5707f859ad5e6aac834ca8`;
- D-022 y D-023.

Verifica que la rama sea `article/main-manuscript` y que D-031 esté en su historia antes de escribir.

## 3. Artefactos exactos que deben recuperarse

Durante V02 ya se generaron localmente:

```text
SECTION_MD_LOCAL = Introduction_B01_V02.md
SECTION_MD_EXPECTED_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4

MASTER_CANDIDATE_MD_LOCAL = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md
MASTER_CANDIDATE_MD_EXPECTED_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
```

Busca primero esos **archivos locales exactos** en la sesión/filesystem que ejecutó V02.

Calcula SHA-256 antes de cualquier operación GitHub.

## 4. Regla de éxito

Solo puedes continuar si:

```text
SECTION_MD_SHA256_MATCH = PASS
MASTER_CANDIDATE_MD_SHA256_MATCH = PASS
```

No normalices saltos de línea, no cambies encoding, no añadas newline final, no reformatees Markdown y no vuelvas a generar ninguno de los archivos.

La identidad textual exacta reportada en V04 gobierna este cierre.

## 5. Estrategia GitHub autorizada

Si ambos archivos exactos están disponibles, usa GitHub Git Database API para evitar el bloqueo anterior del Contents API.

Secuencia recomendada:

1. crea un blob UTF-8 para `Introduction_B01_V02.md` con su contenido exacto;
2. crea un blob UTF-8 para `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md` con su contenido exacto;
3. crea el blob de la respuesta técnica definida en §7;
4. toma el tree SHA del HEAD vivo de `article/main-manuscript` como base;
5. crea un nuevo tree que añada exclusivamente los tres paths autorizados;
6. crea un único commit con el HEAD vivo como parent;
7. mueve `article/main-manuscript` al nuevo commit mediante fast-forward.

No uses placeholders, Base64 documental, fragmentación del master, archivos temporales en GitHub, ramas auxiliares, force-push ni commits parciales.

## 6. Paths autorizados

El único commit de éxito debe añadir exclusivamente:

- `article/sections/introduction/Introduction_B01_V02.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md`;
- `article/responses/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_RESPONSE_V01.md`.

No modifiques todavía:

- `ARTICLE_MASTER_V006.md`;
- `ARTICLE_STATUS.md`;
- `ARTICLE_WRITING_PLAN.md`;
- governance;
- Related Work;
- DOCX;
- Architecture ni ninguna sección posterior.

La promoción a `ARTICLE_MASTER_V007.md` corresponde a la IA Gestora después de auditar este cierre.

## 7. Respuesta técnica obligatoria

Crea:

`article/responses/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_RESPONSE_V01.md`

Si hay éxito, debe registrar como mínimo:

```text
BLOCK = INTRODUCTION_B01
TASK = POST_APPROVAL_TECHNICAL_CLOSURE
RECOVERY_RESULT = PASS
SECTION_MD_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4
SECTION_MD_IDENTITY = PASS
MASTER_CANDIDATE_MD_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
MASTER_CANDIDATE_MD_IDENTITY = PASS
SCIENTIFIC_CONTENT_MODIFIED = NO
DOCX_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
LATER_SECTIONS_MODIFIED = NO
AUTHOR_APPROVAL = PRESERVED
GITHUB_MARKDOWN_TRANSFER = COMPLETE
ARTICLE_MASTER_V007 = NOT_PROMOTED
DECISION_SUPPORT_ARCHITECTURE = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 8. Stop condition si los archivos exactos no existen

Si uno o ambos archivos locales exactos no están disponibles o no coinciden en SHA-256:

- no los reconstruyas;
- no uses el DOCX para recrearlos;
- no modifiques GitHub salvo la respuesta de blocker;
- crea únicamente `article/responses/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_RESPONSE_V01.md` con:

```text
BLOCK = INTRODUCTION_B01
TASK = POST_APPROVAL_TECHNICAL_CLOSURE
RECOVERY_RESULT = FAIL
STOP_CONDITION = APPROVED_MARKDOWN_LOCAL_ARTIFACTS_UNAVAILABLE_OR_HASH_MISMATCH
EXPECTED_SECTION_MD_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4
EXPECTED_MASTER_CANDIDATE_MD_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
RECONSTRUCTION_ATTEMPTED = NO
SCIENTIFIC_CONTENT_MODIFIED = NO
ARTICLE_MASTER_V007 = NOT_PROMOTED
DECISION_SUPPORT_ARCHITECTURE = NOT_STARTED
```

Después detente. Una reconstrucción controlada, si fuera necesaria, requerirá nueva autorización de la IA Gestora.

## 9. Prohibiciones

Queda prohibido:

- editar la Introduction aprobada;
- volver a auditar literatura o claims;
- cambiar citas o comentarios Word;
- regenerar el DOCX;
- promover `ARTICLE_MASTER_V007`;
- abrir Decision-support architecture;
- actualizar status/plan;
- ejecutar cualquier bloque posterior.

## 10. Respuesta final de chat

Después del commit, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_RESPONSE_V01.md@<commit_sha>`

Después, detente.
