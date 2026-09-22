# THESIS CURRENT MASTER MANIFEST — 2026-09-22

## 0. Purpose

Persistent, non-governing identification record for the thesis file explicitly declared by the author as the **current thesis** on 2026-09-22.

This manifest does **not** approve the scientific content of the thesis, does not close G7-F01/G7-F02, and does not declare the thesis final. It establishes the exact current working binary to be used by subsequent preflight work and, once formally authorized, by the future G7 source-freeze process.

## 1. Canonical current working thesis snapshot

```text
THESIS_CURRENT_WORKING_MASTER = true
AUTHOR_CONFIRMED_CURRENT = true
AUTHOR_CONFIRMATION_DATE = 2026-09-22
ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
CANONICAL_LIBRARY_PATH = /Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx
LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
LIBRARY_BACKING_FILE_ID = file_0000000051cc820eba659f9c9c28771a
MIME_TYPE = application/vnd.openxmlformats-officedocument.wordprocessingml.document
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
PARSED_PAGE_COUNT = 129
```

## 2. Document identity

The uploaded document is the UNMSM thesis titled:

```text
Evaluación de un piloto experimental offline de gestión de información documental
para la recomendación auditable de subpartidas NANDINA mediante recuperación
documental y explicación controlada con LLM local
```

Author:

```text
Vladimir MOLLEAPASA GUTIÉRREZ
```

## 3. Status semantics

```text
THESIS_MASTER_STATUS = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED
THESIS_FINAL_APPROVAL_STATUS = NOT_DECLARED
FORMAL_G7_F01_FREEZE_STATUS = NOT_EXECUTED
FORMAL_G7_F02_STATUS = NOT_EXECUTED
```

`CURRENT_WORKING_MASTER` means that this exact binary is the thesis version to audit and update from this point forward unless the author explicitly supplies and identifies a newer one.

It does not mean that the content has already passed G7 or G8.

### 3.1. Correction-baseline semantics

On 2026-09-22 the author clarified that this exact thesis was drafted **before the execution and closure of the later methodological/experimental groups and their fichas**, and therefore it is the thesis that must be corrected and synchronized against the scientific state produced by those groups.

```text
THESIS_CORRECTION_BASELINE = true
THESIS_DRAFTED_BEFORE_GROUP_EXECUTION = true
THESIS_CONTENT_EXPECTED_TO_CONTAIN_PRE_GROUP_SCIENTIFIC_STATE = true
THESIS_TO_BE_CORRECTED_IN_FUTURE_G7_F02 = true
THESIS_IS_CURRENT_SCIENTIFIC_GROUND_TRUTH = false
THESIS_CORRECTION_MUST_USE_CLOSED_GROUP_OUTPUTS = true
```

Interpretation:

- this binary is the **baseline document to correct**, not a scientifically frozen thesis;
- discrepancies against later closed groups are expected and must not be treated as evidence that those groups are wrong;
- during future G7-F02, corrections must flow from the frozen/canonical outputs, claims, tables, figures and limitations established by the governed experimental sequence;
- no correction should be applied silently before the corresponding G7 authorization and source-freeze;
- the corrected thesis must be versioned as a new candidate and must preserve traceability back to this baseline SHA-256.

## 4. Supersession rule

```text
Molleapasa_gv(4).docx = HISTORICAL_PREVIOUS_COPY / NOT_CURRENT_WORKING_MASTER
Molleapasa_gv(5).docx = CURRENT_WORKING_MASTER_SOURCE_UPLOAD / CORRECTION_BASELINE
```

Do not delete or rewrite the historical copy. Do not use it as the current thesis in new preflight or G7 work.

## 5. Cross-chat retrieval rule

For other chats within the `Tesis San Marcos` project, retrieve the current thesis from the persistent Library using either:

```text
CANONICAL_LIBRARY_PATH = /Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx
LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
```

and verify the expected SHA-256 before any programmatic editing or formal freeze:

```text
08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
```

If a later author-confirmed thesis is supplied, create a new dated manifest and explicitly supersede this snapshot; never silently replace the identity.

## 6. Governance

This manifest is preparatory metadata only.

```text
G6_STATE_CHANGED = false
G7_ACTIVATED = false
G8_ACTIVATED = false
PLAN_MODIFIED = false
FICHAS_MODIFIED = false
MAIN_MODIFIED = false
ARTICLE_MODIFIED = false
THESIS_CONTENT_MODIFIED = false
```
