# D-184 — Keywords B03 V01 post-approval KBS compliance reopening and V02 requirement

## Español

```text
DECISION = D-184
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B03_KEYWORDS

CANONICAL_MASTER = ARTICLE_MASTER_V034
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V034.md
CANONICAL_MASTER_MD_SHA256 = 37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca
CANONICAL_MASTER_MD_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

PREVIOUS_KEYWORDS_VERSION = B03_V01
PREVIOUS_KEYWORDS_AUTHOR_APPROVAL = D-182
PREVIOUS_KEYWORDS_INTEGRATION = D-183
PREVIOUS_KEYWORDS_PROMOTION = VERIFIED / RETAINED

COMPLIANCE_REVIEW =
article/reviews/11_FRONT_MATTER_B03_KEYWORDS_KBS_SUBMISSION_COMPLIANCE_REVIEW_V01.md@cf3ceb70d6dc109e47cc80b1bf3b8b58f0c3a5ca
COMPLIANCE_REVIEW_GIT_BLOB =
b0f816647b041e7ece171cefb41d6ebd0bbf128a
COMPLIANCE_REVIEW_RESULT = REVISE_KEYWORDS_TO_V02

KEYWORDS_B03_V01_SCIENTIFIC_VALIDITY = RETAINED_PASS
KEYWORDS_B03_V01_AUTHOR_APPROVAL = RETAINED
KEYWORDS_B03_V01_CANONICAL_PROMOTION = RETAINED
KEYWORDS_B03_V01_SUBMISSION_ELIGIBILITY = WITHDRAWN

D183_PROMOTION_VERIFICATION = RETAINED_PASS
D183_FRONT_MATTER_CLOSURE = SUPERSEDED_FOR_KEYWORDS_COMPLIANCE_ONLY

KEYWORDS_B03_V02_REQUIRED = YES

TARGET_KEYWORDS_EN_V02 =
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Large language model; Provenance

TARGET_KEYWORDS_ES_V02 =
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Modelo de lenguaje grande; Procedencia

TITLE = CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = CLOSED / APPROVED / FROZEN / INTEGRATED
KEYWORDS = V01_CANONICAL_BUT_NOT_SUBMISSION_ELIGIBLE / V02_REQUIRED
FRONT_MATTER_FINALIZATION = REOPENED_FOR_KEYWORDS_V02_ONLY
END_MATTER_FINALIZATION = HOLD / NOT_AUTHORIZED
```

### 1. Motivo de reapertura

Después de la promoción verificada de V034 y durante la transición hacia End Matter, IA Gestora revalidó las instrucciones actuales de sumisión de Elsevier aplicables al journal.

La guía vigente establece un máximo de seis keywords y recomienda evitar plurales innecesarios y keywords que mezclen múltiples conceptos.

B03 V01 contiene siete términos. Por tanto, aunque su contenido fue científicamente aprobado y promovido correctamente, no debe usarse como versión final de sumisión.

### 2. Preservación de la aprobación previa

D-184 no invalida retrospectivamente:

- la aprobación del autor bajo D-182;
- la auditoría técnica/editorial PASS;
- la promoción byte-exacta a V034;
- la integridad de V034 como master canónico actual.

El hallazgo afecta únicamente la elegibilidad de la lista de Keywords para sumisión.

### 3. V02 fijada

La lista V02 se reduce a seis términos.

`Documentary evidence` se retira únicamente de las Keywords. Permanece en el Title y en todo el cuerpo del artículo.

`Large language models` se normaliza a `Large language model`.

`Provenance and traceability` se normaliza a `Provenance`.

La IA de Redacción no debe generar alternativas.

### 4. Baselines

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V034.md
INPUT_MASTER_MD_SHA256 = 37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca
INPUT_MASTER_MD_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx
INPUT_MASTER_DOCX_SHA256 = 8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84
INPUT_MASTER_DOCX_SIZE_BYTES = 110943
INPUT_MASTER_DOCX_COMMENTS = 48
INPUT_MASTER_DOCX_TRACKED_CHANGES = 0
INPUT_MASTER_DOCX_PAGE_COUNT = 71
```

### 5. Gate

```text
CURRENT_DRAFTING_PHASE = FRONT_MATTER / KEYWORDS
CURRENT_GATE = FRONT_MATTER_B03_KEYWORDS_V02_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_AND_REVIEW_KEYWORDS_B03_V02_PROMPT

CANONICAL_MASTER = ARTICLE_MASTER_V034
TITLE = CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = CLOSED / APPROVED / FROZEN / INTEGRATED
KEYWORDS = V02_REQUIRED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-184 reopens only Keywords after a post-approval KBS submission-compliance audit found that the current Elsevier author guidance limits the list to six keywords.

The author's B03 V01 approval, the technical/editorial PASS, and the byte-exact V034 promotion remain historically and canonically valid. What is withdrawn is V01's final submission eligibility.

B03 V02 is fixed to six terms. Title and Abstract remain frozen. End Matter remains unauthorized until V02 is approved and integrated.
