# D-137 — Discussion B04 V02 narrow correction execution authorization

## Español

```text
DECISION = D-137
PHASE = DISCUSSION
BLOCK = DISCUSSION_B04_SECTION_6_4
V01_EXECUTION_RESPONSE = article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V01.md@e27f03b3d4103a3436fe26566a97a22c974ce57c
V01_INTERNAL_REVIEW = article/reviews/7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V01.md@29fa044040c4b061641e711b7a4b906d3b51cb6b
V01_REVIEW_RESULT = PASS_WITH_CORRECTIONS
AUDIT_GOVERNANCE = D-136
ACTIVE_CORRECTION_PROMPT = article/prompts/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION.md@660768b25ae639185181e22433213a1886e13bfd
ACTIVE_CORRECTION_PROMPT_GIT_BLOB = 398a87aafb3627abc54f50abd9c51a1be59898ec
PROMPT_REVIEW = article/reviews/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION_PROMPT_REVIEW_V01.md@68e15b98c4451c9af803691ff592f33540f2ca75
PROMPT_REVIEW_GIT_BLOB = 2672337747a0893e971f34ef5dd8448cc9fa45d0
PROMPT_REVIEW_RESULT = PASS
CANONICAL_MASTER = ARTICLE_MASTER_V026 / UNCHANGED
INPUT_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.md
INPUT_CANDIDATE_MD_SHA256 = bfd15b2a3d28278b317a028e9cff0baeef8458ada5f8083f1b54cf267dd0d0ac
INPUT_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.docx
INPUT_CANDIDATE_DOCX_SHA256 = 8abb1dc3ca1885066be8588db328121eca907447faf5959be3f1b2d89d193b8b
AUTHORIZED_ACTION = EXECUTE_DISCUSSION_B04_V02_NARROW_CORRECTION_ONLY
NEXT_ACTOR = IA_REDACCION
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisión

Se autoriza exclusivamente una revisión V02 de Discussion §6.4 para resolver las correcciones obligatorias identificadas por IA Gestora. La autorización no cambia el boundary científico D-133 ni abre nuevas claims.

La V02 debe corregir cinco aspectos: precisión de la afirmación sobre inspectabilidad del ranking; eliminación de identificadores internos de implementación/QA; eliminación de voz de gobernanza interna; naturalidad del español; y concreción editorial conforme a KBS/SPCCR. Las cifras, límites científicos, ausencia de nuevas citas y estructura argumental de B04 deben preservarse.

La corrección debe partir de los candidatos B04 V01 exactos y verificar sus SHA-256 antes de editar. El Word no puede reconstruirse desde Markdown. Se conservan exactamente 48 comentarios y 0 tracked changes salvo que una anomalía previa obligue a detener la ejecución.

La deuda editorial detectada en §6.2 queda registrada, pero no está autorizada para modificación en esta ejecución.

```text
EXPECTED_EXIT = DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT
DISCUSSION_B04_V01 = REVISION_REQUIRED
DISCUSSION_B04_V02 = AUTHORIZED_FOR_EXECUTION
NEXT_ACTOR = IA_REDACCION
```

---

## English

D-137 authorizes only the narrow Discussion B04 V02 correction defined by the reviewed correction prompt. The scientific boundary is unchanged. The revision must remove the retrieval-rationale overstatement, internal implementation/QA labels, internal-governance voice, and avoidable Spanish Anglicisms while preserving all authorized metrics, limitations, 48 inherited comments, zero tracked changes, and the exact scope of Section 6.4.

```text
AUTHORIZED_ACTION = EXECUTE_DISCUSSION_B04_V02_NARROW_CORRECTION_ONLY
EXPECTED_EXIT = DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```
