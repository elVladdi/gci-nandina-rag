# Revisión interna del prompt — B04 narrow precision correction — V01

## Español

```text
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
PROMPT_GIT_BLOB = a45b51e2a39ce6d415edc227a9a5b66862a00cf6
GOVERNING_DECISION = D-063
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
AUTHORIZED_ITEMS = B04-C01 / B04-C02 ONLY
DELIVERABLES = SECTION_V02 + MASTER_MD_V02 + MASTER_DOCX_V02 + RESPONSE
DOCX_HANDOFF = REQUIRED
OOXML_QA = REQUIRED
ALL_PAGE_RENDER_AND_VISUAL_INSPECTION = REQUIRED
OUT_OF_SCOPE_REWRITE = PROHIBITED
B05 = NOT_AUTHORIZED
VERDICT = PASS
```

Se comparó el prompt correctivo contra D-063, la revisión científica B04 V01 y MWDP v1.0. Las cuatro sustituciones literales EN/ES coinciden con las correcciones autorizadas; los hashes baseline coinciden con los artefactos entregados y verificados por la IA Gestora; el prompt exige continuidad DOCX directa desde B04 V01, preservación de 40 comentarios/anclajes, cero tracked changes, render completo y handoff real al autor.

El prompt no autoriza reescritura adicional de 4.5, no reabre B02/B03, no modifica experimentos ni fuentes gobernantes y no abre 4.6+ o Results. Los entregables V02 y el stop state son compatibles con MWDP-B06 y con el gate suspendido de aprobación autoral.

`PASS`: el prompt puede ejecutarse sin correcciones adicionales.

---

## English

```text
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
PROMPT_GIT_BLOB = a45b51e2a39ce6d415edc227a9a5b66862a00cf6
GOVERNING_DECISION = D-063
AUTHORIZED_ITEMS = B04-C01 / B04-C02 ONLY
DELIVERABLES = SECTION_V02 + MASTER_MD_V02 + MASTER_DOCX_V02 + RESPONSE
DOCX_HANDOFF = REQUIRED
OOXML_QA = REQUIRED
ALL_PAGE_RENDER_AND_VISUAL_INSPECTION = REQUIRED
OUT_OF_SCOPE_REWRITE = PROHIBITED
B05 = NOT_AUTHORIZED
VERDICT = PASS
```

The correction prompt was checked against D-063, the B04 V01 scientific review, and MWDP v1.0. Its four literal EN/ES replacements exactly match the authorized corrections; baseline identities match the artifacts independently verified by the Managing AI; and the prompt preserves direct DOCX continuity, all 40 inherited comment anchors, zero tracked changes, full render/visual QA, and actual author handoff.

No additional Section-4.5 rewrite, experimental change, B02/B03 reopening, Section-4.6+ drafting, or Results drafting is authorized. The prompt is executable as written.