# Related Work B05 V01 — cierre técnico V05 / ejecución mínima

## Autoridad y sustitución

Este prompt **sustituye V04** para el cierre técnico de `RELATED_WORK_B05 / V01`.

Aplica obligatoriamente:

- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
- `article/governance/D023_TECHNICAL_CLOSURE_MINIMAL_EXECUTION_MODE.md`.

B05 V01 ya tiene revisión interna `PASS` y aprobación del autor `YES`. **No existe redacción, auditoría científica ni revisión bibliográfica pendiente.**

No avances a B06 / Section 2.6 ni a ninguna sección posterior.

## Regla de reinicio rápido

Este V05 se emite porque el intento V04 fue detenido por el autor antes de modificar la rama y estaba realizando operaciones innecesarias de Base64/fragmentación sobre Markdown.

Si en esta misma conversación/sesión ya completaste el onboarding obligatorio de `START_HERE` para B05, **no lo repitas**. No vuelvas a leer `README`, `SOURCE_REGISTRY`, `CLAIM_EVIDENCE_MATRIX`, `STYLE_GUIDE`, literatura, fuentes primarias, evidencias experimentales ni corpus KBS.

En una sesión nueva, completa el onboarding obligatorio **una sola vez** y después aplica D023: no repitas lecturas durante este cierre.

## Estado del DOCX

El DOCX aprobado permanece exclusivamente bajo custodia local del autor conforme a D021:

`ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`

SHA-256 aprobado:

`042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

**No abras, no leas, no renderices, no resaves, no codifiques, no subas y no reconstruyas el DOCX.**

## Dos artefactos científicos ya aprobados

Usa exactamente los archivos locales ya producidos:

1. `RelatedWork_B05_V01.md`
   - SHA-256 obligatorio: `1093cacb99de062f687786cb29f06ae96fdc2b16160d29287df797ed339a0495`

2. `ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`
   - SHA-256 obligatorio: `56c1e03af0d803777818a973462e4e70c849266b56f5cb11f396cc915fc22efe`

Calcula/verifica cada SHA-256 **una sola vez**. Si ya fue calculado y verificado en este mismo intento V05, no lo recalcules.

Si cualquiera no coincide o no está disponible, detente sin modificar la rama y aplica D022.

No analices su contenido científico. No compares párrafos. No vuelvas a verificar fuentes. No calcules `git hash-object` local.

## Informe oficial de respuesta

El tercer archivo del commit debe ser:

`article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`

con exactamente este contenido UTF-8:

~~~markdown
# Related Work B05 — cierre técnico V01

```text
BLOCK = RELATED_WORK_B05
BLOCK_REVISION = V01
SECTION = 2.5 Reproducibility and evaluation in knowledge-based decision support
SCIENTIFIC_DRAFT = COMPLETE
INTERNAL_REVIEW = PASS
AUTHOR_APPROVAL = YES
SOURCE_SUPPORT = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
PRIOR_CITATION_COMMENTS_PRESERVED = 25/25
B05_CITATION_COMMENT_COVERAGE = 7/7
TOTAL_CITATION_COMMENT_COUNT = 32
DOCX_REPOSITORY_UPLOAD = DEFERRED_BY_D021
DOCX_LOCAL_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
SECTION_MD_SHA256 = 1093cacb99de062f687786cb29f06ae96fdc2b16160d29287df797ed339a0495
MASTER_CANDIDATE_MD_SHA256 = 56c1e03af0d803777818a973462e4e70c849266b56f5cb11f396cc915fc22efe
EXECUTION_MODE = D023_MINIMAL_TECHNICAL_CLOSURE
TEXT_ARTIFACTS_COMMITTED = 3/3
SEMANTIC_COMMIT = SEE_GIT_HISTORY_FOR_THIS_RESPONSE
NET_FILE_SCOPE = EXACTLY_3_MD_FILES
B05_B06_BOUNDARY = PASS
RELATED_WORK_B06 = NOT_AUTHORIZED
```

Este archivo es la respuesta oficial completa de la IA de Redacción. El commit que contiene este archivo constituye el `SEMANTIC_COMMIT`; no se incrusta su SHA dentro del propio archivo para evitar una dependencia circular del hash del commit.
~~~

No generes ningún otro reporte.

## Procedimiento técnico obligatorio y corto

Antes de escribir, verifica **una sola vez** el HEAD vivo de `article/main-manuscript`. Debe ser el commit desde el cual se te haya indicado ejecutar este V05. Si no coincide, detente y aplica D022.

Después ejecuta únicamente esta secuencia:

1. verificar una sola vez los dos SHA-256 locales anteriores;
2. crear un blob Git para `RelatedWork_B05_V01.md` usando **texto UTF-8 directo** (`encoding = utf-8`);
3. crear un blob Git para `ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md` usando **texto UTF-8 directo** (`encoding = utf-8`);
4. crear un blob Git para `2_RELATED_WORK_B05_RESPONSE_V01.md` usando **texto UTF-8 directo** (`encoding = utf-8`);
5. crear un único tree, basado en el tree del HEAD vivo, que añada exactamente esos tres paths;
6. crear un único commit con ese tree y el HEAD vivo como único parent;
7. mover `article/main-manuscript` a ese commit mediante fast-forward (`force = false`);
8. verificar una sola vez que el HEAD final sea ese commit;
9. detenerte.

### Paths exactos del tree

- `article/sections/related_work/RelatedWork_B05_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`
- `article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`

## Prohibiciones operativas expresas

Para **todos los tres Markdown**, queda prohibido:

- Base64;
- fragmentar o trocear el contenido;
- procesar rangos de 20k/60k o cualquier otra división artificial;
- reconstruir el archivo mediante concatenación de fragmentos;
- hacer pruebas de conectividad repetidas;
- comprobar repetidamente si los blobs existen;
- efectuar round-trips de descarga para volver a analizar el contenido;
- calcular `git hash-object` local;
- crear placeholders, `__noop__`, archivos temporales o commits auxiliares;
- usar `create_file`/Contents API de forma que genere varios commits;
- crear ramas temporales;
- force push;
- volver a revisar fuentes, evidencias, estilo o contenido científico.

Si una única llamada `create_blob` UTF-8 falla para cualquiera de los archivos, **detente inmediatamente**. No pruebes Base64 ni fragmentación como fallback.

## Alcance del commit

El commit semántico debe contener **exactamente tres archivos nuevos `.md`** y ningún otro cambio.

No modifiques:

- governance;
- prompts;
- `ARTICLE_STATUS.md`;
- `ARTICLE_WRITING_PLAN.md`;
- masters canónicos;
- B01–B04;
- B06;
- archivos experimentales.

## Respuesta de interfaz — D022

No escribas en chat ningún informe, hash, explicación, QA, estado ni detalle de ejecución.

Toda respuesta sustantiva queda en:

`article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`

Si la interfaz obliga a un mensaje final, responde **únicamente**:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md@<commit_sha>`

No añadas ninguna otra frase.
