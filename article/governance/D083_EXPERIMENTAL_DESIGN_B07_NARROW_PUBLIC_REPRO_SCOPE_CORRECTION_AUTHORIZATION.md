# D-083 — Autorización de corrección estrecha B07 sobre alcance público de reproducibilidad / Authorization for narrow B07 public-reproducibility scope correction

## Español

```text
DECISION_ID = D-083
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-082
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION.md@e7ee988c42c2095a0e0b60dd7a216bf148949419
AUTHORIZED_PROMPT_GIT_BLOB = a492b8f53b463aba3295fd71b12dc9f637e74fea
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B07_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION_PROMPT_REVIEW_V01.md@60d25426aa0e092617f9df866ee9a4d06101d77f
PROMPT_REVIEW_RESULT = PASS
AUTHORIZED_CORRECTION = B07-C01_ONLY
B07_STATE = REVISION_REQUIRED / AUTHORIZED_FOR_NARROW_CORRECTION
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Se autoriza exclusivamente corregir B07-C01 sobre los candidatos B07 V01 exactos. La IA de Redacción debe eliminar de Section 4.8 la mención narrativa al repositorio interno de desarrollo y abrir directamente sobre el repositorio público `gci-nandina-rag-reproducibility`.

La ejecución debe preservar todas las demás fronteras científicas ya aprobadas de B07 V01 y usar D-035 de forma obligatoria debido al timeout previo.

```text
BASELINE_MD_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
BASELINE_DOCX_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
REAL_FILE_HANDOFF = REQUIRED
```

La salida esperada es B07 V02 pendiente de nueva auditoría Gestora. No se abre Results.

---

## English

```text
DECISION_ID = D-083
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-082
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION.md@e7ee988c42c2095a0e0b60dd7a216bf148949419
AUTHORIZED_PROMPT_GIT_BLOB = a492b8f53b463aba3295fd71b12dc9f637e74fea
PROMPT_REVIEW_RESULT = PASS
AUTHORIZED_CORRECTION = B07-C01_ONLY
B07_STATE = REVISION_REQUIRED / AUTHORIZED_FOR_NARROW_CORRECTION
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS = NOT_AUTHORIZED
```

Only B07-C01 is authorized. Remove the internal development repository from Section 4.8 manuscript prose, retain all other scientifically correct reproducibility boundaries, and use the D-035 timeout-safe handoff path. B07 V02 must return to Managing-AI audit before any author-approval gate can reopen.