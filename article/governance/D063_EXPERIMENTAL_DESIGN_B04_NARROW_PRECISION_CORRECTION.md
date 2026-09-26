# D-063 — Experimental Design B04 narrow precision correction

## Español

```text
DECISION_ID = D-063
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-062
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524
SCIENTIFIC_SCOPE = VERIFIED / PASS
MASTER_CANDIDATE_GLOBAL_STATUS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
CORRECTION_SCOPE = TWO_NARROW_PRECISION_ITEMS_ONLY
EXPERIMENTAL_REVIEW = NOT_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

La auditoría independiente B04 V01 verificó la arquitectura, el alcance científico, la trazabilidad experimental, el diferencial Markdown, la continuidad DOCX, los 40 comentarios/anclajes heredados y la ausencia de tracked changes. No se autoriza reescritura científica general de 4.5.

Se autorizan exclusivamente dos correcciones de precisión, cada una aplicada en inglés y en el espejo español:

1. **B04-C01:** reformular la oración sobre `history_depth=2950` para distinguir el banco H100 de 2,950 registros y la profundidad configurada de la existencia efectiva de scores solo para documentos con coincidencias léxicas;
2. **B04-C02:** formular condicionalmente la existencia de un match documental exacto NANDINA-8, de modo que Methods describa la regla de lookup sin anticipar como outcome la cobertura exacta observada en Phase F.

Los textos exactos autorizados están congelados en `article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md` y deben ser reproducidos literalmente por el prompt correctivo.

## Baselines correctivos exactos

```text
BASELINE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
EXPECTED_COMMENTS = 40
EXPECTED_TRACKED_CHANGES = 0
```

La corrección debe partir de estos candidatos B04 V01 exactos. Está prohibido volver a B03, reconstruir Word desde Markdown, modificar otra oración o anticipar 4.6+ o Results.

Después de la ejecución, la IA Gestora debe realizar una auditoría diferencial estricta de B04 V02. Solo si esa auditoría pasa puede reabrirse el gate de aprobación autoral.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_NARROW_PRECISION_CORRECTION
NEXT_ACTOR = IA_REDACCION
AUTHOR_APPROVAL_GATE = SUSPENDED
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-063
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-062
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524
SCIENTIFIC_SCOPE = VERIFIED / PASS
MASTER_CANDIDATE_GLOBAL_STATUS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
CORRECTION_SCOPE = TWO_NARROW_PRECISION_ITEMS_ONLY
EXPERIMENTAL_REVIEW = NOT_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The independent B04 V01 audit verified architecture, scientific scope, experimental traceability, Markdown differential integrity, DOCX continuity, preservation of all 40 inherited comment anchors, and zero tracked changes. No general scientific rewrite of Section 4.5 is authorized.

Only two precision corrections are authorized, each mirrored in English and Spanish: (1) distinguish the 2,950-record H100 bank and configured `history_depth=2950` from the implementation's score dictionary, which materializes lexically matched documents; and (2) make exact NANDINA-8 evidence matching conditional so Methods describes the lookup rule without disclosing the observed exact-coverage outcome as if it were a design condition.

The exact replacement text is frozen in the governing internal review. The correction must start from the exact B04 V01 candidate Markdown and DOCX masters identified above. Returning to B03, reconstructing Word from Markdown, changing any other sentence, or drafting Section 4.6+ or Results is prohibited.

After execution, the Managing AI must perform a strict differential audit of B04 V02. The author-approval gate may reopen only after that audit passes.