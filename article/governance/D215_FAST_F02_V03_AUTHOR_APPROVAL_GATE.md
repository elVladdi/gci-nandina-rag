# D-215 — FAST-F02 V03 Author Approval Gate

## Español

```text
DECISION = D-215
PHASE = FAST_FINALIZATION / FAST_F02
PREVIOUS_DECISION = D-214

GESTORA_REVIEW =
article/reviews/20_FAST_F02_V03_PRESENTATION_CONSISTENCY_INTERNAL_REVIEW_V01.md@71ed5d043bd0a3afbcbc1714c1d0aa2b34641925
GESTORA_REVIEW_GIT_BLOB =
b4c4cf846b6d4d7eb96f3c943ec61ae5dd775f62
GESTORA_REVIEW_RESULT = PASS

SOURCE_RESPONSE =
article/responses/20_FAST_F02_V03_PRESENTATION_CONSISTENCY_CORRECTION_RESPONSE_V01.md@6fffd704b97cf1a1c43cdda90f78c033bb07dd53
SOURCE_RESPONSE_GIT_BLOB =
4a7732c9392e0d7ef3474c21a391863f38c924f3

CANDIDATE_MAIN_MD =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V03.md
CANDIDATE_MAIN_MD_SHA256 =
4367b60f181a4d399ecba4dc205ccb6dcba0d7237effa762753ccb8bb9065074
CANDIDATE_MAIN_MD_EXPECTED_GIT_BLOB =
9a7427365a0bd8a5fc340e27eda5aa98a02a4a1f

CANDIDATE_MAIN_DOCX =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V03.docx
CANDIDATE_MAIN_DOCX_SHA256 =
2a3a7b6b724728027756fdafd5572e63beab03eaa414bdc4a529bba1bfe989e3
CANDIDATE_MAIN_DOCX_SIZE_BYTES = 578737
CANDIDATE_MAIN_DOCX_PAGE_COUNT = 85

SUPPLEMENTARY_MD =
SUPPLEMENTARY_MATERIAL_FAST_F02_V03.md
SUPPLEMENTARY_MD_SHA256 =
9c08af66edcae7f39cbf06590105d2e0d0d2a184840c7595fe354078346f934d
SUPPLEMENTARY_MD_GIT_BLOB =
2eaacc07319d7cb926c5ebb26acf9f40f85f733b

SUPPLEMENTARY_DOCX =
SUPPLEMENTARY_MATERIAL_FAST_F02_V03.docx
SUPPLEMENTARY_DOCX_SHA256 =
f2f4ced99305789c5d194470a6cd1280a825386f1ea06620ef0ff18f2f7616bd
SUPPLEMENTARY_DOCX_SIZE_BYTES = 122189
SUPPLEMENTARY_DOCX_PAGE_COUNT = 20

FIGURE_2_CANONICAL_SVG =
article/figures/FAST_F02_Figure2_Explanation_Quality_V02.svg
FIGURE_2_CANONICAL_SVG_GIT_BLOB =
fbb3ea93b93224c4de23ae58d455695b5955cfe0

FIGURE_2_CANONICAL_PNG_SHA256 =
35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673

SCIENTIFIC_CONTENT = PASS
PRESENTATION_CONSISTENCY = PASS
REFERENCE_BIJECTION = PRESERVED_25_OF_25
AUTHOR_ADMINISTRATIVE_FIELDS = INTENTIONALLY_BLANK / D-208
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

AUTHOR_APPROVAL_GATE = OPEN
CANONICAL_MASTER = ARTICLE_MASTER_V038
CANONICAL_PROMOTION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
IF_APPROVED_PROMOTION_TARGET = article/manuscript/ARTICLE_MASTER_V039.md
IF_APPROVED_PROMOTION_EXPECTED_GIT_BLOB =
9a7427365a0bd8a5fc340e27eda5aa98a02a4a1f

FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED_BY_THIS_DECISION
```

## 1. Dictamen de la Gestora

La corrección FAST-F02 V03 pasa la auditoría Gestora completa.

Se verificó independientemente:

- identidad de los cuatro archivos V03 reales;
- diferencia Markdown limitada al scope D-214;
- cuatro figuras EN + cuatro figuras ES;
- cuatro media assets científicos únicos;
- Supplementary con Tables S1-S7 + Figure S1 solamente;
- Figure 2 canónica y reutilizada en ambas mitades del master;
- 48 comments preservados;
- cero tracked changes;
- filas no divididas y headers repetidos en Tables 2-7;
- render completo de 85 páginas del artículo y 20 páginas del Supplementary;
- ausencia de defectos visuales bloqueantes;
- ausencia de nueva ciencia.

## 2. Nota sobre el PNG de Figure 2

La copia raster recibida separadamente por el canal de chat no conserva los bytes exactos del PNG canónico.

Esto no bloquea el gate porque el DOCX V03 contiene el PNG canónico exacto, con SHA-256:

`35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673`

La Gestora lo recuperó byte-exact mediante extracción del media part del DOCX. Esa copia exacta es la que gobierna el gate autoral y la futura entrega.

## 3. Decisión requerida del Autor

El Autor debe decidir sobre FAST-F02 V03 como paquete completo:

- artículo Markdown;
- artículo DOCX;
- Supplementary Markdown;
- Supplementary DOCX;
- Figure 2 canónica.

Opciones:

```text
APPROVE:
Apruebo FAST-F02 V03.

REJECT / CORRECTION:
No apruebo FAST-F02 V03: [corrección concreta]
```

## 4. Efecto de una aprobación

Si el Autor aprueba:

1. la Gestora promoverá byte-exact el Markdown V03 a `ARTICLE_MASTER_V039.md`;
2. verificará el Git blob contra `9a7427365a0bd8a5fc340e27eda5aa98a02a4a1f`;
3. registrará el DOCX V03 como baseline Word canónico bajo custodia del Autor;
4. cerrará FAST-F02 como APPROVED / INTEGRATED;
5. solo entonces abrirá FAST-F03 para ensamblaje final de submission.

No se autoriza promoción antes de la decisión explícita del Autor.

---

## English

FAST-F02 V03 passes Managing-AI audit and is now at the Author approval gate. No canonical promotion is authorized until the Author explicitly approves the complete V03 package.
