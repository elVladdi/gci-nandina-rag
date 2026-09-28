# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.33
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-122
CANONICAL_MASTER = ARTICLE_MASTER_V023
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V023.md
CANONICAL_MASTER_MD_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
CANONICAL_MASTER_MD_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = DISCUSSION
CURRENT_GATE = DISCUSSION_B01_SECTION_6_1_DRAFTING_V01
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = OPEN / AUTHORIZED_FOR_DRAFTING
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V023.md` es el master Markdown canónico verificado. Results §5.1–§5.7 están cerrados, aprobados, congelados e integrados.

La promoción B07 a V023 fue byte-exacta y está registrada en:

`article/governance/D120_RESULTS_B07_AUTHOR_APPROVAL_V023_VERIFICATION_AND_RESULTS_CLOSURE.md@baa9e4e16a673668914858856038f36920c976d2`.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 60
```

## 2. Secuencia vigente de Discussion

La estructura congelada mantiene:

```text
6.1 Separating candidate ranking from documentary evidence
6.2 Controlled use of the LLM for explanation
6.3 Comparison with prior work
6.4 Implications for auditable decision support
6.5 Configurability and transfer conditions
6.6 Limitations
```

Solo §6.1 está abierto. §6.2–§6.6 no están autorizados.

## 3. Discussion B01 / Section 6.1

Boundary:

`article/governance/D121_DISCUSSION_B01_SECTION6_1_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md@6c7120c261fa4216c89bfaac322cedf36f504eb8`

Prompt:

`article/prompts/7_DISCUSSION_B01_SECTION6_1.md@fdc7f4994d69573c903a24ea87926bc2af454298`

Git blob:

`3038967213e92f7da9ae13f2dd3587f036ad0445`

Revisión:

`article/reviews/7_DISCUSSION_B01_SECTION6_1_PROMPT_INTERNAL_REVIEW_V01.md@4d15de80bf875145984038f32958e8debfa656f3` — `PASS`.

Autorización:

`article/governance/D122_DISCUSSION_B01_SECTION6_1_EXECUTION_AUTHORIZATION.md@c063d8deeead13223bf34730e68d3d0a3b375098`.

## 4. Contrato científico B01

§6.1 interpretará el valor metodológico de fijar el Top-3 antes de la asociación documental y lo contrastará funcionalmente con Lee et al. (2021) y Lee et al. (2023), ambos ya citados y verificados en el manuscrito.

Se autoriza sostener que la separación explícita de autoridad permite atribuir las métricas de candidate retrieval al componente histórico y las propiedades de coverage/association/traceability a la etapa documental. No se autoriza afirmar que esa separación cause mejor desempeño, que el framework sea globalmente superior, que la asociación documental pruebe corrección normativa/jurídica ni que la diferencia constituya novelty.

No se permiten comparaciones numéricas directas con resultados de los dos papers debido a diferencias de tarea, dataset, nivel HS, espacio de clases y protocolo.

## 5. Política Word y citas

El baseline Word tiene 40 comentarios. B01 debe introducir exactamente dos nuevas citas en la Parte I inglesa—Lee et al. (2021) y Lee et al. (2023)—y exactamente dos nuevos comentarios de cita. El candidato esperado debe contener:

```text
COMMENTS = 42
TRACKED_CHANGES = 0
```

Los 40 comentarios heredados deben preservarse sin modificación. D-035 continúa activo y Word no debe reconstruirse desde Markdown.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_DISCUSSION_B01_SECTION_6_1
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V023.md
BASELINE_MASTER_MD_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
BASELINE_MASTER_MD_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
BASELINE_DOCX_SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
EXPECTED_RESPONSE = article/responses/7_DISCUSSION_B01_SECTION6_1_RESPONSE_V01.md
EXPECTED_SECTION = article/sections/discussion/Discussion_B01_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx
EXPECTED_EXIT = DISCUSSION_B01_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V023 is the canonical verified master and Results 5.1–5.7 are fully integrated. Discussion B01 / Section 6.1 is the only open drafting block. It is restricted to bounded interpretation of fixed candidate ranking versus documentary association, with functional comparison to the verified Lee et al. (2021) and Lee et al. (2023) precedents. No novelty, causal performance claim, cross-dataset numerical superiority, overall-system accuracy, normative/legal correctness, downstream Discussion, or Conclusion content is authorized.

```text
CURRENT_GATE = DISCUSSION_B01_SECTION_6_1_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B01 = AUTHORIZED
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```