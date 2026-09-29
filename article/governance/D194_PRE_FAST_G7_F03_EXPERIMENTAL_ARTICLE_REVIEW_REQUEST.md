# D-194 — Reapertura controlada pre-FAST para auditoría científica G7-F03 de IA Experimental

## Español

```text
DECISION = D-194
PHASE = PRE_FAST_FINALIZATION / CROSS_ROLE_SCIENTIFIC_AUDIT
PREVIOUS_DECISION = D-193

CANONICAL_MASTER = ARTICLE_MASTER_V036
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V036.md
CANONICAL_MASTER_MD_GIT_BLOB = c9dcbcc376cdb121d30dc2408756a6c95b569a90
CANONICAL_MASTER_MD_SHA256 = 8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8

EXPERIMENTAL_G7_F03_REQUEST =
article/prompts/13_G7_F03_EXPERIMENTAL_ARTICLE_REVIEW_REQUEST_V01.md@08f17e31afb73f6f7532b16e49609a204d6019d9
EXPERIMENTAL_G7_F03_REQUEST_GIT_BLOB =
5eabd0bc2ba114008d56028b6beb24c8fdd5ef1e

G7_F01_SOURCE_FREEZE_MD_GIT_BLOB =
feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430
G7_F01_SOURCE_FREEZE_JSON_GIT_BLOB =
776fcb52e8ada9967504001b897c75b4108bfb63

EXPERIMENTAL_MAIN_HEAD_AT_REQUEST =
db0d0ad0d8435921a7838db6720eaea86a263763
G7_F01_FROZEN_ARTICLE_HEAD =
2aad97aaceec0af6be0edb9ba0dd29170ad35baf
CURRENT_ARTICLE_HEAD_AT_REQUEST =
952a56bb09c95bc7a93baec9b0a560889d253195

FAST_FINALIZATION_MODE =
PROPOSED / NOT_AUTHORIZED / PENDING_G7_F03
ARTICLE_EDITING_DURING_GATE = FROZEN
NEXT_ACTOR = IA_EXPERIMENTAL
NEXT_ACTION = EXECUTE_G7_F03_ARTICLE_SCIENTIFIC_REVIEW
```

## 1. Motivo

El Autor solicitó que, antes de organizar la finalización editorial rápida del manuscrito, IA Experimental revise la versión canónica sustancialmente finalizada del artículo y resuelva la ficha G7-F03 de su propio Plan Maestro.

La solicitud responde a un hecho de gobernanza: G7-F01 congeló las fuentes científicas y dejó G7-F03 como ficha prospectiva, con un requisito explícito de comparar el artículo futuro con el head editorial congelado y reconciliar cualquier drift científico material.

Desde ese freeze, el artículo avanzó hasta `ARTICLE_MASTER_V036.md`, incluyendo Experimental Design, Results, Discussion, Conclusion, Front Matter y la declaración final de uso de IA.

## 2. Separación de competencias

IA Gestora no decide el resultado de G7-F03.

IA Experimental conserva autoridad sobre:

- fuentes experimentales congeladas;
- resultados y denominadores;
- inferencia;
- disposición experimental de hipótesis;
- límites científicos;
- tablas canónicas G5;
- figuras científicas G6;
- cualquier necesidad real de nueva acción experimental.

IA Gestora conserva autoridad editorial sobre:

- organización posterior del `FAST_FINALIZATION_MODE`;
- prompts de IA de Redacción;
- integración editorial;
- gates de aprobación del Autor.

El Autor conserva el gate final.

## 3. Alcance de la consulta

La solicitud versionada pide a IA Experimental:

1. ejecutar el drift check exigido por G7-F01;
2. auditar científicamente V036 contra G3/G4/G5/G6 y cierres pertinentes;
3. resolver G7-F03 conforme a su Plan vigente;
4. disponer científicamente las nueve presentaciones G5 y las tres figuras G6 respecto del artículo;
5. evaluar la compatibilidad científica de una figura arquitectónica editorial;
6. revisar la propuesta provisional de tres macrofichas `FAST_FINALIZATION_MODE`;
7. entregar a IA Gestora las condiciones obligatorias para organizar la fase final.

## 4. FAST_FINALIZATION_MODE provisional

La propuesta entregada a IA Experimental, aún no autorizada, es:

- FINAL-F01 — Scientific Presentation & Visual Structuring;
- FINAL-F02 — End Matter & Reference Integrity;
- FINAL-F03 — Submission Assembly & Final QA.

No se fija todavía el inventario definitivo de tablas o figuras. Ese inventario se decidirá después del dictamen G7-F03, combinando:

- evidencia científica congelada G5/G6;
- auditoría de IA Experimental;
- patrón editorial KBS-34;
- necesidad de legibilidad;
- economía de elementos visuales.

## 5. Freeze temporal

Hasta recibir el dictamen G7-F03:

```text
ARTICLE_MASTER_V036 = FROZEN_AS_REVIEW_BASELINE
NEW_WRITING_PROMPT = NOT_AUTHORIZED
TABLE_FIGURE_INTEGRATION = NOT_AUTHORIZED
FAST_FINALIZATION_EXECUTION = NOT_AUTHORIZED
NEW_EXPERIMENT = NOT_AUTHORIZED_BY_THIS_DECISION
```

La revisión no reabre EXP12 ni habilita nuevas métricas, CIs, p-values o resultados.

## 6. Reconciliación de metadatos editoriales heredados

Los párrafos narrativos inferiores de `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` todavía conservaban referencias históricas a V035 y al DOCX previo de Keywords, aunque los bloques de control superiores ya gobernaban V036.

D-194 autoriza corregir exclusivamente esos metadatos narrativos para que la IA Experimental reciba un estado editorial no contradictorio:

- master vigente: `ARTICLE_MASTER_V036.md`;
- Word canónico: `ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`;
- SHA-256 Word: `d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d`;
- comentarios: 48;
- tracked changes: 0;
- páginas: 72.

No se modifica contenido científico ni el master V036.

## 7. Gate vigente

```text
CURRENT_DRAFTING_PHASE = PRE_FAST_FINALIZATION
CURRENT_GATE = EXPERIMENTAL_G7_F03_REVIEW_PENDING
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_EXPERIMENTAL
NEXT_ACTION = EXECUTE_G7_F03_ARTICLE_SCIENTIFIC_REVIEW
EXPECTED_EXIT = G7_F03_DIAGNOSTIC_AND_FAST_CONSTRAINTS

GESTORA_TASK_STATUS = ACTIVE / COORDINATION_ONLY
FAST_FINALIZATION_MODE = PROPOSED / NOT_AUTHORIZED / PENDING_G7_F03
SUBMISSION_READY = NOT_ASSERTED
```

Después de la respuesta de IA Experimental, IA Gestora debe reorganizar el FAST_FINALIZATION_MODE en función de ese dictamen y presentarlo al Autor.

---

## English

D-194 opens a controlled pre-FAST cross-role scientific audit. ARTICLE_MASTER_V036 is frozen as the review baseline while Experimental AI is asked to execute/resolve G7-F03 under its own current Master Plan.

The versioned request requires the G7-F01 drift check, a full scientific audit of V036 against frozen experimental evidence, scientific disposition of the nine G5 table presentations and three approved G6 figures, and review of the provisional three-block FAST_FINALIZATION_MODE.

No manuscript editing, table/figure integration, new experiment, new metric, new confidence interval, new p-value, or EXP12 reopening is authorized by D-194.

After the G7-F03 response, Managing AI will reorganize the finalization workflow and submit it to the Author.
