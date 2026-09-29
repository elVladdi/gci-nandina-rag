# D-202 — Autorización de ejecución FAST-F01 Scientific Presentation V01

## Español

```text
DECISION = D-202
PHASE = FAST_FINALIZATION / FAST_F01
PREVIOUS_DECISION = D-201

AUTHORIZED_ACTOR = IA_DE_REDACCION_CIENTIFICA
AUTHORIZED_BLOCK = FAST_F01_SCIENTIFIC_PRESENTATION_V01

PROMPT =
article/prompts/16_FAST_F01_SCIENTIFIC_PRESENTATION_V01.md@7f2059f4f78c04869572d7a62f91f6ceba53fb03
PROMPT_GIT_BLOB =
38886d41c017b9fb2a50157fbb9f12408ad178fe

PROMPT_INTERNAL_REVIEW =
article/reviews/16_FAST_F01_SCIENTIFIC_PRESENTATION_PROMPT_INTERNAL_REVIEW_V01.md@dacad6af16c70dc4e868fe1a8a378cce514190a2
PROMPT_INTERNAL_REVIEW_GIT_BLOB =
53875217b1a7e0ac416832ebc2b90e977eadd5dd
PROMPT_INTERNAL_REVIEW_RESULT = PASS

INPUT_MASTER_MD =
article/manuscript/ARTICLE_MASTER_V037.md
INPUT_MASTER_MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
INPUT_MASTER_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919

INPUT_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx
INPUT_MASTER_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
INPUT_MASTER_DOCX_SIZE_BYTES = 112705
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
BASELINE_PAGE_COUNT = 73

AUTHORIZED_MAIN_BODY_TABLES = 3
AUTHORIZED_MAIN_BODY_FIGURES = 2
SUPPLEMENTARY_INTEGRATION = NOT_AUTHORIZED_IN_FAST_F01

AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED_BY_THIS_DECISION
```

## 1. Autorización

D-202 autoriza a IA de Redacción científica a ejecutar exclusivamente Prompt 16 V01.

La ejecución debe mejorar la presentación científica de V037 sin introducir nueva evidencia, métricas, inferencia o cambio de claims.

## 2. Inventario visual autorizado

Cuerpo principal exacto:

1. Table 1 — experimental benchmark/evaluation overview;
2. Table 2 — G5-MAIN-01;
3. Table 3 — G5-MAIN-02;
4. Figure 1 — architecture schematic;
5. Figure 2 — G6-FIG-01.

No se autoriza un sexto elemento visual en el cuerpo.

## 3. Fuentes congeladas

Los componentes científicos deben permanecer vinculados a:

```text
G5-MAIN-01 blob =
cb68583ee2260e4455796bac99ad90995ca7ef92

G5-MAIN-02 blob =
359e4e19b5ef1d44983c03039162209293b2a44c

G6-FIG-01 SVG blob =
f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3

G6 caption registry blob =
0dcb43cfa56dfce2e6955f960184069beb36ba76
```

## 4. Baseline Word

La ejecución Word solo puede comenzar si IA de Redacción recibe el archivo real:

`ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx`

y verifica:

```text
SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
SIZE_BYTES = 112705
```

No reconstruir Word desde Markdown.

## 5. Stop condition

La ejecución termina en:

`FAST_F01_COMPLETED_PENDING_GESTORA_AUDIT`

Después:

```text
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
```

---

## English

D-202 authorizes Writing AI to execute only FAST-F01 Prompt 16 V01 against the exact V037 Markdown and approved 112705-byte Word baseline.

Exactly three main-body tables and two main-body figures are authorized. No new experiment, metric, inference, literature, supplementary integration, FAST-F02/03 execution, or Experimental G8 work is authorized.
