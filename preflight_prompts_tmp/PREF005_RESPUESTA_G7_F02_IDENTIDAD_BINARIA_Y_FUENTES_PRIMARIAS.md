# PREF005 — G7-F02 binary identity and primary sources

```text
PROMPT114_EXECUTION = COMPLETED_READ_ONLY_PREFLIGHT / NO_G7_F02_EXECUTION
WORKSPACE_CONTRACT = PASS / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA / origin=https://github.com/elVladdi/gci-nandina-rag.git
MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
FICHAS_OBSERVED = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
PLAN_OBSERVED = 60b7add68e2bb14101a6fa47c512f619516d0545
THESIS_MANIFEST_BLOB = 42b89b512b8db818238bfd0da22a7c75c207d9f1
THESIS_EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_EXPECTED_SIZE_BYTES = 4360620
THESIS_BINARY_CANDIDATE_PATHS = NONE_FOUND_IN_ALLOWED_LOCAL_TREE
THESIS_BINARY_RECHECK = BLOCKED
THESIS_OBSERVED_SHA256 = NOT_AVAILABLE
THESIS_OBSERVED_SIZE_BYTES = NOT_AVAILABLE
PROJECT_CANDIDATE_COUNT = 4
PROJECT_CANDIDATES = SEE_TABLE_BELOW
APPROVED_PROJECT_BINARY_IDENTITY = AMBIGUOUS
APPROVED_PROJECT_PATH = NOT_DETERMINED
APPROVED_PROJECT_SHA256 = NOT_DETERMINED
APPROVED_PROJECT_SIZE_BYTES = NOT_DETERMINED
ANNEX_CANDIDATE_COUNT = 0
ANNEX_DISTINCT_HASH_COUNT = 0
ANNEX_CANDIDATES = NONE_FOUND_IN_ALLOWED_LOCAL_TREE
APPROVED_ANNEX_BINARY_IDENTITY = NOT_FOUND
APPROVED_ANNEX_PATH = NOT_AVAILABLE
APPROVED_ANNEX_SHA256 = NOT_AVAILABLE
APPROVED_ANNEX_SIZE_BYTES = NOT_AVAILABLE
SOURCE_FILE_READABILITY_CHECK = FOUR_PROJECT_CANDIDATES_HAVE_PDF_HEADER / THESIS_NOT_FOUND / ANNEX_NOT_FOUND
PREF005_RESULT = BLOCKED_SOURCE_IDENTITY
G7_F02_ACTIVATION_RECOMMENDATION = DO_NOT_AUTHORIZE
G7_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
THESIS_MODIFIED = false
ARTICLE_MODIFIED = false
MAIN_MODIFIED = false
FICHAS_MODIFIED = false
PLAN_MODIFIED = false
EXP12_REOPENED = false
EXTERNAL_AUDIT = PENDING
```

## Search and candidate evidence

The read-only recursive filename search was confined to `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\`. Neither `Molleapasa_gv_vigente_2026-09-22.docx` nor `Molleapasa_gv(5).docx` was found. No equivalent clearly traceable to the author-confirmed current master was found. The manifest's `/Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx` is a library path, not an accessible local candidate within the permitted search tree; its recorded hash is an expectation, not an observed recheck. `Molleapasa_gv(4).docx` and unrelated thesis files were not substituted.

The exact approved-project reference filename `Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` was not found. These four differently named project PDFs are accessible, have the `%PDF-` header, and are byte-distinct; none is selected as the approved source:

| Absolute path | Filename | Size (bytes) | SHA-256 | Last write (UTC) |
| --- | --- | ---: | --- | --- |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 1\Metodología de investigación\Proyecto de Tesis.pdf` | `Proyecto de Tesis.pdf` | 693464 | `2c5a67df0a940847c5b074463676bb7b2016405884d78407458c55a1f47a0318` | `2024-08-03T12:53:55Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis V.2.pdf` | `Proyecto de Tesis V.2.pdf` | 520982 | `b621b10e590147ba3aa80668e27d0aa90d0b374ab9abc4d139c6714c9528867f` | `2024-12-21T23:35:38Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis V1.pdf` | `Proyecto de Tesis V1.pdf` | 540127 | `38b2e8dd545647ce4ab64f8c1a6ed1e4093e56b3e2635eda21ddd284a1b41dcd` | `2024-12-21T14:19:24Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis.pdf` | `Proyecto de Tesis.pdf` | 530779 | `b274b27bbe0693a9270a4aeafe181224462b69ec0860630cb2cebda06b379805` | `2024-12-21T04:58:09Z` |

No `Anexo_1_NANDINA_LLM_RAG_v13*.docx` copy was found in the permitted tree. Versioned text names the logical approved annex and the approved-project reference, but does not bind any accessible candidate above to approved bytes or provide an annex SHA-256. No candidate DOCX could undergo a ZIP/readability check. The PDF header check is a format check only, not a claim that any PDF is the approved project.

## Exact evidence required before G7-F02 authorization

1. Provide an accessible copy of the author-confirmed current thesis binary `Molleapasa_gv(5).docx` or `Molleapasa_gv_vigente_2026-09-22.docx` within the permitted local tree, or authorize a separate means to retrieve the manifest-bound library file. Its observed SHA-256 and size must equal the manifest values above.
2. Provide the approved `Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` binary, or explicitly identify which of the four distinct local PDFs is approved, with a byte-level SHA-256 binding. Do not infer approval from name, date, size, or content similarity.
3. Provide the approved `Anexo_1_NANDINA_LLM_RAG_v13.docx` binary within the permitted tree, or identify an accessible author-approved copy with an explicit byte-level binding. Its SHA-256, size, and DOCX readability remain unverified.

No thesis candidate was created; no source was copied, renamed, edited, or normalized. G7-F02 remains unexecuted and requires a separate external audit and authorization even after a future successful preflight.
