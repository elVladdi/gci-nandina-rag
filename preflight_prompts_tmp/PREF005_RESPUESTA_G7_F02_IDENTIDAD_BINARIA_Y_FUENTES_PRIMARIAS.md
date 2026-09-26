# PREF005 — G7-F02 binary identity and primary sources (author-supplied completion)

```text
PROMPT114_EXECUTION = COMPLETED_WITH_AUTHOR_SUPPLIED_BINARIES / NO_G7_F02_EXECUTION
WORKSPACE_CONTRACT = PASS / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA / origin=https://github.com/elVladdi/gci-nandina-rag.git
MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
FICHAS_OBSERVED = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
PLAN_OBSERVED = 60b7add68e2bb14101a6fa47c512f619516d0545
THESIS_MANIFEST_BLOB = 42b89b512b8db818238bfd0da22a7c75c207d9f1
THESIS_EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_EXPECTED_SIZE_BYTES = 4360620
THESIS_BINARY_CANDIDATE_PATHS = C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 2 - Tesis\Molleapasa_gv.docx; STAGED_BYTE_IDENTICAL_COPY_BELOW
THESIS_BINARY_RECHECK = PASS
THESIS_OBSERVED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_OBSERVED_SIZE_BYTES = 4360620
PROJECT_CANDIDATE_COUNT = 5 / 1_AUTHOR_CONFIRMED_EXACT_FILENAME + 4_PREVIOUSLY_AMBIGUOUS
PROJECT_CANDIDATES = SEE_TABLE_BELOW
APPROVED_PROJECT_BINARY_IDENTITY = PASS / AUTHOR_CONFIRMED_EXACT_FILENAME
APPROVED_PROJECT_PATH = C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 1 - Proyecto de investigación\Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf
APPROVED_PROJECT_SHA256 = 25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421
APPROVED_PROJECT_SIZE_BYTES = 1323188
ANNEX_CANDIDATE_COUNT = 1 / AUTHOR_CONFIRMED_V13
ANNEX_DISTINCT_HASH_COUNT = 1
ANNEX_CANDIDATES = C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 1 - Proyecto de investigación\Anexo_1_NANDINA_LLM_RAG_v13.docx
APPROVED_ANNEX_BINARY_IDENTITY = PASS / AUTHOR_CONFIRMED_AUXILIARY_SOURCE / NOT_GENERAL_GATE
APPROVED_ANNEX_PATH = C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 1 - Proyecto de investigación\Anexo_1_NANDINA_LLM_RAG_v13.docx
APPROVED_ANNEX_SHA256 = 8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067
APPROVED_ANNEX_SIZE_BYTES = 1573922
SOURCE_FILE_READABILITY_CHECK = PASS / BOTH_DOCX_ZIP_CRC_OK / PDF_75_PAGES_FIRST_PAGE_TEXT_READABLE
PREF005_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
G7_F02_ACTIVATION_RECOMMENDATION = ELIGIBLE_FOR_IA_EXPERIMENTAL_AUTHORIZATION
G7_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
THESIS_MODIFIED = false
ARTICLE_MODIFIED = false
MAIN_MODIFIED = false
FICHAS_MODIFIED = false
PLAN_MODIFIED = false
EXP12_REOPENED = false
EXTERNAL_AUDIT = PENDING
```

## Author-supplied source identity and staging

The earlier Prompt114 search was limited to `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\` and therefore could not find the three files later supplied by the author under `C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\`. The author has explicitly designated these three binaries as authoritative and authorized local, unversioned staging. The supplied `Molleapasa_gv.docx` has the *exact* 4,360,620 bytes and SHA-256 recorded for the manifest's `Molleapasa_gv(5).docx` / `Molleapasa_gv_vigente_2026-09-22.docx`; this is byte identity, not selection by similar filename. No older thesis copy was substituted.

The files were copied without editing to the non-repository staging directory `C:\Users\Vladimir\AppData\Local\Temp\PREF005-authoritative-2026-09-25\`. Each staged SHA-256 and size matches its corresponding original. The originals remain unchanged; staging is temporary and must not be treated as a permanent source repository. No binary was added to Git.

| Author-confirmed source (absolute path) | Last write (UTC) | Size (bytes) | SHA-256 | Staged filename |
| --- | --- | ---: | --- | --- |
| `C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 2 - Tesis\Molleapasa_gv.docx` | `2026-08-20T02:21:20Z` | 4360620 | `08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed` | `Molleapasa_gv.docx` |
| `C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 1 - Proyecto de investigación\Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` | `2026-08-04T02:26:50.0574464Z` | 1323188 | `25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421` | `Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` |
| `C:\Users\Vladimir\OneDrive\Documentos\Tesis - UNMSM\Anexo 1 - Proyecto de investigación\Anexo_1_NANDINA_LLM_RAG_v13.docx` | `2026-08-05T05:29:45Z` | 1573922 | `8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067` | `Anexo_1_NANDINA_LLM_RAG_v13.docx` |

Both staged DOCX files open as ZIP packages with the required Office parts (`[Content_Types].xml`, `_rels/.rels`, `word/document.xml`), and a full ZIP CRC check found no bad member. The staged PDF opens with Poppler and pypdf: 75 unencrypted pages, and first-page text extraction returned 525 characters. pypdf reported nonfatal whitespace warnings in object headers; no readability failure occurred. This is a minimal file-type/readability check, not scientific re-audit.

The author clarified that **only the current thesis and approved project are mandatory gates for G7-F02 authorization**. The byte-identified v13 is a confirmed auxiliary methodological source, not a general blocking gate. All three happen to be available and readable. This completion does not authorize G7-F02; the ficha remains `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED` pending independent audit and a separate authorization.

## Earlier ambiguous candidates (not selected)

Before the author supplied the exact approved project, the following four byte-distinct PDFs were found in the earlier permitted tree. They remain nonauthoritative; none was selected by date, size, or similarity:

| Absolute path | Filename | Size (bytes) | SHA-256 | Last write (UTC) |
| --- | --- | ---: | --- | --- |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 1\Metodología de investigación\Proyecto de Tesis.pdf` | `Proyecto de Tesis.pdf` | 693464 | `2c5a67df0a940847c5b074463676bb7b2016405884d78407458c55a1f47a0318` | `2024-08-03T12:53:55Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis V.2.pdf` | `Proyecto de Tesis V.2.pdf` | 520982 | `b621b10e590147ba3aa80668e27d0aa90d0b374ab9abc4d139c6714c9528867f` | `2024-12-21T23:35:38Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis V1.pdf` | `Proyecto de Tesis V1.pdf` | 540127 | `38b2e8dd545647ce4ab64f8c1a6ed1e4093e56b3e2635eda21ddd284a1b41dcd` | `2024-12-21T14:19:24Z` |
| `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\Semestre 2\Proyecto de Tesis.pdf` | `Proyecto de Tesis.pdf` | 530779 | `b274b27bbe0693a9270a4aeafe181224462b69ec0860630cb2cebda06b379805` | `2024-12-21T04:58:09Z` |

No thesis candidate or G7-F02 working document was created. The only copies made are the unversioned staging binaries above. No source was renamed, edited, or normalized. G7-F02 remains unexecuted and requires a separate external audit and authorization.
