# Experimental Design B02 V01 — narrow coherence correction

## 1. Identity

```text
BLOCK = EXPERIMENTAL_DESIGN_B02_NARROW_COHERENCE_CORRECTION
GOVERNING_DECISION = article/governance/D053_EXPERIMENTAL_DESIGN_B02_NARROW_COHERENCE_CORRECTION.md
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B02_INTERNAL_REVIEW_V01.md
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.md
BASELINE_MD_SHA256 = 22f5a6e1168e08ef6281488024a4ac5e4f6742ee90a96d8f31e5453c592bf592
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.docx
BASELINE_DOCX_SHA256 = 40d492911b2163a4c6a837f292f3056aa49bcbf69ce9dc3caf50aa80f021ae1e
SCIENTIFIC_CONTENT_4_3 = VERIFIED / PASS / DO_NOT_REWRITE
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Execute only this correction. Do not advance.

## 2. Role

Act only as the Drafting AI. This is a mechanical/editorial coherence correction, not a new scientific drafting block.

Do not reopen scientific review, bibliography, experiments, Results, or later Methods sections.

## 3. Required onboarding

Read current `article/START_HERE.md`, `article/ARTICLE_STATUS.md`, `article/ARTICLE_WRITING_PLAN.md`, D-052, D-053, the B02 internal review, and the current approved Structure V02. Verify the two baseline file hashes before editing.

If either baseline is missing or its hash differs, stop with:

`B02_NARROW_CORRECTION_BASELINE_MISMATCH`

Do not reconstruct the DOCX from Markdown.

## 4. Authorized edits — exactly these

### C01 — cumulative structure label

Replace the legacy cumulative-master label wherever it is displayed/stored:

```text
KBS_ARTICLE_WORKING_STRUCTURE_V01
→ KBS_ARTICLE_WORKING_STRUCTURE_V02
```

This includes cover/footer or equivalent visible master-label occurrences in the DOCX and the master label in Markdown. Do not change surrounding wording or layout except as required by this literal replacement.

### C02a — English Introduction

Replace exactly:

```text
To evaluate the framework, we instantiate it in an offline customs-classification testbed for eight-digit NANDINA subheading recommendation within Chapter 87 and the Peruvian administrative and documentary context defined in Methods.
```

with:

```text
To evaluate the framework, we instantiate it in an offline customs-classification testbed for eight-digit NANDINA subheading recommendation within Chapter 87, using the Peruvian administrative context and the Andean documentary resource defined in Methods.
```

### C02b — Spanish Introduction

Replace exactly:

```text
Para evaluar el framework, este se instancia en un testbed aduanero offline para la recomendación de subpartidas NANDINA de ocho dígitos dentro del Capítulo 87 y del contexto administrativo y documental peruano definido en Métodos.
```

with:

```text
Para evaluar el framework, este se instancia en un testbed aduanero offline para la recomendación de subpartidas NANDINA de ocho dígitos dentro del Capítulo 87, utilizando el contexto administrativo peruano y el recurso documental andino definidos en Métodos.
```

### C02c — Section-3 internal drafting notes

English:

```text
the Peruvian corpus
→ the documentary resource used in the experiment
```

Spanish:

```text
corpus peruano
→ recurso documental utilizado en el experimento
```

These two edits apply only to the internal drafting notes introducing Section 3.

## 5. Frozen content

All other text must remain byte/textually unchanged as far as the file format permits.

Specifically:

- Section 4.3 scientific prose: unchanged;
- Sections 4.1–4.2.3: unchanged;
- Related Work: unchanged;
- all other Introduction/Architecture prose: unchanged;
- 4.4–4.8 placeholders: unchanged;
- Results/Discussion/Conclusion: unchanged.

No references, metrics, claims, citations, or results may be added or removed.

## 6. DOCX requirements

Edit the exact DOCX baseline directly.

Required final checks:

```text
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0
DOCX_RECONSTRUCTED_FROM_MD = NO
MANUAL_BASE64 = NO
CHUNKING_OR_REASSEMBLY = NO
RENDER_ALL_PAGES = REQUIRED
VISUAL_INSPECTION_ALL_PAGES = REQUIRED
```

If an unexpected mutation occurs outside the authorized replacements, stop with:

`B02_NARROW_CORRECTION_OUT_OF_SCOPE_MUTATION`

## 7. Deliverables

Create a small response in GitHub:

`article/responses/5_EXPERIMENTAL_DESIGN_B02_NARROW_COHERENCE_CORRECTION_RESPONSE_V01.md`

Do not overwrite the already audited Section 4.3 section file.

Deliver to the author as direct attachments:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md`
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx`

Report SHA-256 for both files and the exact count of authorized replacements performed.

Use the D-035 timeout-safe handoff pattern. No manual Base64, fragmentation, chunking, or reconstruction.

## 8. Stop state

Finish with:

`EXECUTION_COMPLETED_PENDING_GESTORA_DIFFERENTIAL_AUDIT`

Do not claim APPROVED, CLOSED, FROZEN, or INTEGRATED.
