# D-209 — FAST-F02 execution authorization

## Decision

```text
DECISION = D-209
PHASE = FAST_FINALIZATION / FAST_F02
PREVIOUS_DECISION = D-208

AUTHORIZED_ACTOR = IA_DE_REDACCION_CIENTIFICA
PROMPT = article/prompts/18_FAST_F02_END_MATTER_REFERENCES_SUPPLEMENTARY_V01.md@ad0787898271adb8ab77fe78293140a2511cdc9d
PROMPT_GIT_BLOB = 5a38905b03e0d44d1b3125f866996fc03b92aa79

PROMPT_REVIEW = article/reviews/18_FAST_F02_PROMPT_INTERNAL_REVIEW_V01.md@48571dcade1d7d66760afbcd1a8c051ed3397ed5
PROMPT_REVIEW_GIT_BLOB = c93cec7d59dac5ceaeb065b1c78e99551e1e282e
PROMPT_REVIEW_RESULT = PASS

INPUT_MD = article/manuscript/ARTICLE_MASTER_V038.md
INPUT_MD_GIT_BLOB = b508aeccb7dab93a8b4cf25b185aa429dbe5577f
INPUT_MD_SHA256 = 6201a9a47f86630f5f275ca7a6d9a01c2c642140a7f803cb390d26848721572e

INPUT_DOCX = ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.docx
INPUT_DOCX_SHA256 = 7506189f32af5c9e99cb3bc87530b9ffd2ca09e3348f886c2b6c194080a21fe8
INPUT_DOCX_SIZE_BYTES = 351420

AUTHOR_ADMINISTRATIVE_FIELDS = INTENTIONALLY_BLANK / CLOSED / NONBLOCKING

AUTHORIZED_CONTENT = DATA_AVAILABILITY + CODE_REPRODUCIBILITY + REFERENCES_25 + SUPPLEMENTARY_S1_S7_FIG_S1_S2

EXPECTED_EXIT = FAST_F02_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F03 = NOT_AUTHORIZED
```

D-209 authorizes one consolidated FAST-F02 execution using Prompt 18 V01.

The exact Word baseline must be used directly; no reconstruction from Markdown is allowed.

No additional author declarations are required. CRediT, Funding, competing-interest, Acknowledgements, and absent author metadata remain blank under D-208.

No new scientific analysis, metric, inference, experiment, or citation outside the audited 25-work inventory is authorized.

The execution stops at FAST_F02_COMPLETED_PENDING_GESTORA_AUDIT and returns control to IA Gestora del Artículo.
