# D-053 — Experimental Design B02 narrow coherence correction

```text
DECISION_ID = D-053
DATE = 2026-09-25
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-052
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
SCIENTIFIC_CONTENT_4_3 = VERIFIED / PASS
MASTER_CANDIDATE_GLOBAL_STATUS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
CORRECTION_SCOPE = TWO_NARROW_COHERENCE_ITEMS_ONLY
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The independent audit `article/reviews/5_EXPERIMENTAL_DESIGN_B02_INTERNAL_REVIEW_V01.md` verified the scientific content of Section 4.3 and the DOCX package. No scientific rewriting of B02 is authorized.

## Authorized corrections

### C01 — Structure label

The next cumulative candidate must implement the D-052 deferred label correction:

```text
KBS_ARTICLE_WORKING_STRUCTURE_V01
→ KBS_ARTICLE_WORKING_STRUCTURE_V02
```

Apply this only to the cumulative-master structural label wherever the legacy label is displayed/stored. Do not alter scientific prose.

### C02 — Documentary authority coherence

The newly verified Section 4.3 establishes an Andean Community documentary resource, while four inherited formulations still suggest a Peruvian documentary corpus/context. A narrow transversal amendment is authorized solely to remove that ambiguity.

English Introduction replacement:

```text
To evaluate the framework, we instantiate it in an offline customs-classification testbed for eight-digit NANDINA subheading recommendation within Chapter 87 and the Peruvian administrative and documentary context defined in Methods.
```

with:

```text
To evaluate the framework, we instantiate it in an offline customs-classification testbed for eight-digit NANDINA subheading recommendation within Chapter 87, using the Peruvian administrative context and the Andean documentary resource defined in Methods.
```

Spanish Introduction replacement:

```text
Para evaluar el framework, este se instancia en un testbed aduanero offline para la recomendación de subpartidas NANDINA de ocho dígitos dentro del Capítulo 87 y del contexto administrativo y documental peruano definido en Métodos.
```

with:

```text
Para evaluar el framework, este se instancia en un testbed aduanero offline para la recomendación de subpartidas NANDINA de ocho dígitos dentro del Capítulo 87, utilizando el contexto administrativo peruano y el recurso documental andino definidos en Métodos.
```

English Section-3 drafting-note replacement:

```text
the Peruvian corpus
→ the documentary resource used in the experiment
```

Spanish Section-3 drafting-note replacement:

```text
corpus peruano
→ recurso documental utilizado en el experimento
```

## Frozen content

Everything else remains frozen. In particular:

- do not rewrite Section 4.3;
- do not change Sections 4.1–4.2.3;
- do not change Related Work;
- do not otherwise rewrite Introduction or Architecture;
- do not draft 4.4+;
- do not draft Results;
- do not add references, metrics, results, novelty claims, or FINAL_GAP.

The correction candidate must be produced from the exact B02 V01 artifacts:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.md
BASELINE_MD_SHA256 = 22f5a6e1168e08ef6281488024a4ac5e4f6742ee90a96d8f31e5453c592bf592
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.docx
BASELINE_DOCX_SHA256 = 40d492911b2163a4c6a837f292f3056aa49bcbf69ce9dc3caf50aa80f021ae1e
EXPECTED_COMMENTS = 40
EXPECTED_TRACKED_CHANGES = 0
```

After execution, IA Gestora must perform a differential audit before the author-approval gate can reopen.
