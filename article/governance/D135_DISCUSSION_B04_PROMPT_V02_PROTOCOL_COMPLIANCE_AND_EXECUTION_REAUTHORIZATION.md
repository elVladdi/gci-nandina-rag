# D-135 — Discussion B04 prompt V02 protocol compliance and execution reauthorization

## Español

```text
DECISION = D-135
PHASE = DISCUSSION
BLOCK = DISCUSSION_B04_SECTION_6_4
SECTION = 6.4 IMPLICATIONS FOR AUDITABLE DECISION SUPPORT
SCIENTIFIC_BOUNDARY = article/governance/D133_DISCUSSION_B04_SECTION6_4_INTERPRETIVE_BOUNDARY_AND_AUDITABILITY_TRACE.md@be5a3df880d6fea49e18e64d6080d3485a5850de
PRIOR_PROMPT = article/prompts/7_DISCUSSION_B04_SECTION6_4.md@982375ae4b6660bd05d962b7ed681d59354e39c0
PRIOR_PROMPT_GIT_BLOB = f75fde7e666cbcc527de3f29c5dd787c14318836
PRIOR_AUTHORIZATION = D-134
PRIOR_PROMPT_EXECUTION_STATUS = SUPERSEDED / DO_NOT_EXECUTE
ACTIVE_PROMPT = article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md@9d84059e8620219cd83c3b3dad91c4af900d447e
ACTIVE_PROMPT_GIT_BLOB = dcc3b40d29e1f6913cce96bee43403f3ab03e1d0
ACTIVE_PROMPT_REVIEW = article/reviews/7_DISCUSSION_B04_SECTION6_4_PROMPT_INTERNAL_REVIEW_V02.md@7716a4916662e8116ac84c7626e38caa7e7d66d9
ACTIVE_PROMPT_REVIEW_GIT_BLOB = c6601458c512f5ec3fa7abb39b4ef53fec649948
ACTIVE_PROMPT_REVIEW_RESULT = PASS
MANDATORY_CORRECTIONS = NONE
CANONICAL_MASTER = ARTICLE_MASTER_V026
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V026.md
CANONICAL_MASTER_MD_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
CANONICAL_MASTER_MD_GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
BASELINE_DOCX_SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
BASELINE_COMMENTS = 48
BASELINE_TRACKED_CHANGES = 0
BASELINE_PAGE_COUNT = 64
MWDP_V1_0 = BINDING / EXPLICIT_IN_ACTIVE_PROMPT
SPCCR_V1_0 = BINDING / EXPLICIT_IN_ACTIVE_PROMPT
D022 = BINDING
D027 = BINDING
D035 = BINDING
SCIENTIFIC_SCOPE_CHANGE = NONE
DISCUSSION_B04_V01 = AUTHORIZED_FOR_EXECUTION
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Motivo

Una revisión transversal del método de IA Gestora contra el protocolo maestro congelado detectó una omisión operacional en el prompt B04 V01: aunque su boundary científico, resultados, claims, límites y entregables eran correctos, el prompt no referenciaba expresamente `MWDP_V1.0` ni `SPCCR_V1.0` y no reproducía de forma explícita el preflight obligatorio de `START_HERE.md`, el checklist acumulativo de entrega de MWDP ni las obligaciones de D-022/D-027 junto con D-035.

Esta omisión no altera el contenido científico autorizado por D-133 ni invalida la integración B03/V026. Sin embargo, `MWDP-B02` establece que cada prompt cerrado debe referenciar expresamente el protocolo maestro; la ausencia de una regla en un prompt no la deroga. Por ello, antes de ejecutar B04 se sustituye el prompt V01 por V02 y se reautoriza formalmente la ejecución.

### Efecto

`article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md` conserva íntegramente el scope científico de B04 y añade explícitamente:

- onboarding completo y reconstrucción del estado vivo desde GitHub;
- `MWDP_V1.0` y su checklist obligatorio de entrega;
- `SPCCR_V1.0` y sus controles de claridad;
- disciplina repository-first de D-022;
- entrega efectiva del DOCX al autor bajo D-027;
- handoff timeout-safe de D-035;
- verificación previa de identidades exactas de Markdown y Word;
- trazado explícito de claims, snapshots, cobertura de comentarios, equivalencia EN/ES, conteo del texto principal inglés y trigger de revisión experimental.

No se autoriza ningún resultado, fuente, cita, claim, inferencia o bloque adicional. No se añaden citas en §6.4; deben conservarse exactamente 48 comentarios y 0 tracked changes.

```text
AUTHORIZED_ACTION = EXECUTE_DISCUSSION_B04_V01_ONLY_USING_PROMPT_V02
EXPECTED_EXIT = DISCUSSION_B04_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-135 supersedes the B04 V01 prompt for execution and reauthorizes Discussion B04 using the protocol-complete V02 prompt. The scientific boundary is unchanged. V02 explicitly carries the frozen MWDP, active SPCCR rule, START_HERE preflight, repository-first response discipline, exact DOCX author handoff, timeout-safe artifact handoff, and the complete MWDP delivery checklist. D-134 remains part of the audit trail but its V01 prompt is no longer the active execution instruction.

```text
ACTIVE_PROMPT = article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md
ACTIVE_PROMPT_GIT_BLOB = dcc3b40d29e1f6913cce96bee43403f3ab03e1d0
PROMPT_REVIEW = PASS
DISCUSSION_B04_V01 = AUTHORIZED_FOR_EXECUTION
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```
