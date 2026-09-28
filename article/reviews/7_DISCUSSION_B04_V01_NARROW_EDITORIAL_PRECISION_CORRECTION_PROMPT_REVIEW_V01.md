# Internal review — Discussion B04 V01→V02 narrow editorial/scientific-precision correction prompt

## Español

```text
REVIEW = 7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION_PROMPT_REVIEW_V01
PHASE = DISCUSSION
BLOCK = DISCUSSION_B04_SECTION_6_4
SOURCE_REVIEW = article/reviews/7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V01.md
AUDIT_STANDARD = D-136 + MWDP_V1.0 + SPCCR_V1.0 + KBS_EWG_34_V01
PROMPT = article/prompts/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION.md
PROMPT_GIT_BLOB = 398a87aafb3627abc54f50abd9c51a1be59898ec
CANONICAL_MASTER = ARTICLE_MASTER_V026 / UNCHANGED
INPUT_CANDIDATE_MD_SHA256 = bfd15b2a3d28278b317a028e9cff0baeef8458ada5f8083f1b54cf267dd0d0ac
INPUT_CANDIDATE_DOCX_SHA256 = 8abb1dc3ca1885066be8588db328121eca907447faf5959be3f1b2d89d193b8b
SCIENTIFIC_SCOPE_CHANGE = NONE
NEW_LITERATURE = PROHIBITED
NEW_CITATIONS = PROHIBITED
NEW_RESULTS_OR_INFERENCE = PROHIBITED
SECTION_6_2_LEGACY_DEBT_EDIT = PROHIBITED
VERDICT = PASS
MANDATORY_CORRECTIONS_TO_PROMPT = NONE
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

La revisión confirma que el prompt traduce de forma cerrada las observaciones de la auditoría B04 V01 sin abrir el alcance científico. Exige corregir la sobreinterpretación sobre `why a candidate entered the ranking`, retirar identificadores internos de implementación/QA del texto publicable, reemplazar voz de gobernanza por lenguaje científico reader-facing, naturalizar el español y aplicar concreción KBS/SPCCR.

El prompt preserva exactamente el ground truth autorizado de RQ2/RQ3, la modalidad LLM-as-judge, los límites `AUDITABILITY ≠ LEGAL_CORRECTNESS` y `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`, y la prohibición de novelty, SOTA, safety, causalidad, deployment readiness y generalización externa.

La corrección se limita a §6.4 inglés/español y parte de los candidatos B04 V01 exactos, cuya identidad debe verificarse antes de editar. No autoriza reconstruir Word desde Markdown ni modificar §6.2 pese a la deuda editorial transversal registrada. Conserva 48 comentarios, 0 tracked changes y ausencia de nuevas citas.

```text
PROMPT_SCOPE = NARROW / EXACT
KBS_READER_FACING_CONTROL = PASS
INTERNAL_TERMINOLOGY_CONTROL = PASS
ANTI_OVERCLAIMING_CONTROL = PASS
SPANISH_NATURALNESS_CONTROL = PASS
D022_D027_D035 = EXPLICIT / PASS
EXPECTED_EXIT = DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

The correction prompt passes internal review. It is narrowly scoped to the defects identified in Discussion B04 V01, preserves all scientific ground truth and prohibitions, and adds no literature, citations, results, or inference. It explicitly enforces reader-facing terminology, KBS/SPCCR concreteness, Spanish naturalness, exact candidate identities, Word preservation, D-022/D-027/D-035 handoff discipline, and a hard stop before §6.5.

```text
VERDICT = PASS
MANDATORY_CORRECTIONS_TO_PROMPT = NONE
READY_FOR_EXECUTION_AUTHORIZATION = YES
```
