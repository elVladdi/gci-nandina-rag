# D-212 — FAST-F02 V02 Global Table/Figure Corrective Execution Authorization

## Español

```text
DECISION = D-212
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION
PREVIOUS_DECISION = D-211

AUTHORIZED_ACTOR = IA_DE_REDACCION_CIENTIFICA
AUTHORIZED_BLOCK = FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01

PROMPT =
article/prompts/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01.md@d842a5976c78b11c84571cbfe727916799e0f207
PROMPT_GIT_BLOB =
19f205ed87f7ce67ba6fe22e3d93c6fea3907ef7

PROMPT_REVIEW =
article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_PROMPT_INTERNAL_REVIEW_V01.md@957eec348a6f63cf1c26f6ba8b87eacbe8085c17
PROMPT_REVIEW_GIT_BLOB =
f77b52b7b55cae9ae558632c5306a1fde6b7ba8c
PROMPT_REVIEW_RESULT = PASS

GLOBAL_EDITORIAL_AUDIT =
article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_EDITORIAL_AUDIT_V01.md@c8b5ef3bd3a8d326757c293ccc3c2bff657f7034
GLOBAL_EDITORIAL_AUDIT_GIT_BLOB =
f622b55336f5549472f8e26aeceba71aed2af009
GLOBAL_EDITORIAL_AUDIT_RESULT = REVISION_REQUIRED

INPUT_MAIN_MD =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.md
INPUT_MAIN_MD_SHA256 =
c6909699b9b7272d12cbe57f02d5897b78c8a489c9105bdf69e23e4462e90dd4
INPUT_MAIN_MD_GIT_BLOB =
4c891641a86d0622cdc9fb7b2afee6f4691ee320
INPUT_MAIN_MD_SIZE_BYTES = 305240

INPUT_MAIN_DOCX =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.docx
INPUT_MAIN_DOCX_SHA256 =
bd584ce9817ce8d251cbe43a6e737612039a5ba82c932f1637839d66466e9e31
INPUT_MAIN_DOCX_SIZE_BYTES = 356835
INPUT_MAIN_DOCX_PAGE_COUNT = 81

INPUT_SUPPLEMENTARY_MD =
SUPPLEMENTARY_MATERIAL_FAST_F02_V01.md
INPUT_SUPPLEMENTARY_MD_SHA256 =
fd2ff32090f2262787a0f661bf67300bca158733b24edae0a37ac90dffd0a89f
INPUT_SUPPLEMENTARY_MD_GIT_BLOB =
d10207e99ca76c1b501f57c9cf2b620e54c03a3f

INPUT_SUPPLEMENTARY_DOCX =
SUPPLEMENTARY_MATERIAL_FAST_F02_V01.docx
INPUT_SUPPLEMENTARY_DOCX_SHA256 =
ad6b7f5cbfa695ab61eb4f9b5469f061eb804074c5bfb8c735bdef81d700cc9e
INPUT_SUPPLEMENTARY_DOCX_SIZE_BYTES = 222424
INPUT_SUPPLEMENTARY_DOCX_PAGE_COUNT = 21

EXPECTED_MAIN_TABLES = 7
EXPECTED_MAIN_FIGURES = 4
EXPECTED_SUPPLEMENTARY_TABLES = 7
EXPECTED_SUPPLEMENTARY_FIGURES = 1

AUTHOR_APPROVAL_GATE = CLOSED / SUPERSEDED
CANONICAL_MASTER = ARTICLE_MASTER_V038
CANONICAL_PROMOTION = NOT_AUTHORIZED

EXPECTED_EXIT = FAST_F02_V02_COMPLETED_PENDING_GESTORA_AUDIT
FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED_BY_THIS_DECISION
```

## 1. Autorización

D-212 autoriza una única ejecución correctiva de IA de Redacción para materializar el plan editorial global de tablas y figuras definido por la auditoría 19.

La ejecución debe partir de los cuatro archivos reales FAST-F02 V01 exactos y producir FAST-F02 V02.

## 2. Alcance

Se autoriza únicamente:

- reorganización de los resultados numéricos en las siete tablas auditadas;
- creación de la nueva figura de perfil cualitativo desde los ocho promedios congelados;
- promoción editorial de G6-FIG-03 desde Supplementary al cuerpo principal sin alteración científica;
- renumeración mecánica de tablas/figuras y actualización de cross-references;
- compactación de prosa numérica redundante;
- actualización consecuente del Supplementary a siete tablas y una figura.

## 3. Prohibiciones

No se autoriza nueva ciencia, nuevo análisis, nueva métrica, nueva inferencia, nuevo CI, nuevo p-value, nueva literatura, ni cambio en la disposición de hipótesis.

Los campos administrativos de autoría permanecen en blanco.

## 4. Gate

```text
CURRENT_GATE = FAST_F02_V02_CORRECTIVE_WRITING_EXECUTION_AUTHORIZED
NEXT_ACTOR = IA_DE_REDACCION_CIENTIFICA
NEXT_ACTION = EXECUTE_PROMPT_19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01
EXPECTED_EXIT = FAST_F02_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

---

## English

D-212 authorizes one corrective Writing-AI execution of FAST-F02 V02 against the exact FAST-F02 V01 main manuscript and Supplementary baselines.

The scope is presentation-only: seven main tables, four main figures, prose deduplication, and Supplementary relocation of the already approved EXP11A figure. No new scientific analysis is authorized.
