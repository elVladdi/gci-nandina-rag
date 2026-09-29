# D-190 — Reopen AI-use disclosure for Codex coding support and governed Redacción correction

## Español

```text
DECISION = D-190
PHASE = END_MATTER / METHODS_TRANSPARENCY
BLOCK = END_MATTER_B02_GENERATIVE_AI_DECLARATION_V02

PREVIOUS_DECISION = D-189
D189_GESTORA_TASK_CLOSURE = SUPERSEDED_BEFORE_FINAL_AUTHOR_APPROVAL_OF_AI_DISCLOSURE
D189_DECLARATION_V01 = SUPERSEDED / INCOMPLETE

REOPEN_REASON =
CODEX_AI_ASSISTED_CODING_USE_WAS_OMITTED_FROM_DECLARATION

CANONICAL_MASTER = ARTICLE_MASTER_V035
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V035.md
CANONICAL_MASTER_MD_SHA256 =
23a92e46f1fe3d7edfcf9210e1d90a133c17abf6b85e62ad3906171dc48589ac
CANONICAL_MASTER_MD_GIT_BLOB =
ddf3abb1826f93d5d82c0a135c0c2ae6b389e7fd

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 =
de3c60c59bd71e5c5b101c7281a675b68faaf8275af64d7403f1ff51fa60905b
CANONICAL_MASTER_DOCX_SIZE_BYTES = 110919
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

AUTHOR_INSTRUCTION =
IA_REDACCION_MUST_MATERIALIZE_CORRECTION_AND_RETURN_MD_DOCX
GESTORA_MUST_AUDIT
AUTHOR_MUST_APPROVE_FINAL_CANDIDATE

AUTHOR_APPROVAL_GATE = NOT_OPEN
```

## 1. Hallazgo

La declaración V01 preparada bajo D-189 informó el uso de ChatGPT (OpenAI) para apoyo en redacción y refinamiento del lenguaje, pero omitió el uso de Codex (OpenAI) como herramienta de apoyo en codificación.

El autor corrige explícitamente ese hecho y ordena que la rectificación siga el flujo normal del proyecto:

```text
BOUNDARY -> PROMPT -> PROMPT_REVIEW -> AUTHORIZATION ->
IA_REDACCION_EXECUTION -> MD/DOCX_HANDOFF ->
GESTORA_AUDIT -> AUTHOR_APPROVAL
```

IA Gestora no debe integrar directamente el texto corregido en el master.

## 2. Regla editorial Elsevier aplicable

La política vigente de Elsevier distingue:

1. IA usada para preparación del manuscrito: debe declararse en una sección separada antes de References;
2. IA usada para escribir o editar código como parte del proceso de investigación: debe describirse en Methods con el nivel de detalle apropiado.

Por tanto, el bloque V02 debe contener dos inserciones estrechamente delimitadas:

- una oración de transparencia metodológica sobre Codex en Methods / Reproducibility resources;
- la declaración final de IA antes de References, incluyendo ChatGPT y Codex.

No se autoriza ninguna otra modificación científica o editorial.

## 3. Texto exacto autorizado — Methods

### English

```text
OpenAI Codex was used as an AI-assisted software-development tool to support software implementation and code refinement. The authors reviewed and edited the Codex-assisted code as needed and retained responsibility for the final research software and its use in the reported study.
```

### Español

```text
OpenAI Codex se utilizó como herramienta de desarrollo de software asistida por IA para apoyar la implementación de software y el refinamiento de código. Los autores revisaron y editaron el código asistido por Codex según fue necesario y conservaron la responsabilidad sobre el software de investigación final y su uso en el estudio reportado.
```

Ubicación autorizada:

- English: al final de `## 4.8. Reproducibility resources`, inmediatamente antes de `# 5. Results`;
- Español: al final de `## 4.8. Recursos de reproducibilidad`, inmediatamente antes de `# 5. Resultados`.

## 4. Texto exacto autorizado — declaración final

### English heading

```text
# Declaration of generative AI and AI-assisted technologies in the manuscript preparation and research process
```

### English statement

```text
During the preparation of this work, the authors used ChatGPT (OpenAI) to support manuscript drafting and language refinement, and Codex (OpenAI) to support software implementation and code refinement. The authors reviewed and edited the AI-assisted outputs as needed and take full responsibility for the content of the publication and the final research software.
```

### Encabezado español

```text
# Declaración sobre el uso de IA generativa y tecnologías asistidas por IA en la preparación del manuscrito y el proceso de investigación
```

### Declaración española

```text
Durante la preparación de este trabajo, los autores utilizaron ChatGPT (OpenAI) como apoyo para la redacción del manuscrito y el refinamiento del lenguaje, y Codex (OpenAI) como apoyo para la implementación de software y el refinamiento de código. Los autores revisaron y editaron las salidas asistidas por IA según fue necesario y asumen plena responsabilidad por el contenido de la publicación y por el software de investigación final.
```

Ubicación autorizada:

- English: sección separada inmediatamente antes de `# References`;
- Español: sección separada inmediatamente antes de `# Referencias`.

## 5. Interpretación vinculante

La declaración:

- reconoce ChatGPT como apoyo de redacción/refinamiento lingüístico;
- reconoce Codex como apoyo de implementación/refinamiento de código;
- no atribuye autoría a herramientas de IA;
- no atribuye a Codex autoridad sobre diseño experimental, resultados, métricas, interpretación o conclusiones;
- no sustituye la descripción del LLM local experimental en Methods;
- no afirma que ChatGPT o Codex hayan validado científicamente el artículo;
- mantiene responsabilidad humana sobre manuscrito y software final.

## 6. Scope exacto

Solo se autorizan cuatro inserciones:

1. Methods EN — oración Codex;
2. Methods ES — oración Codex;
3. AI declaration EN antes de References;
4. AI declaration ES antes de Referencias.

Todo lo demás debe permanecer byte-equivalente en Markdown y estructuralmente preservado en DOCX.

No se autoriza completar:

- autores;
- afiliaciones;
- CRediT;
- Funding;
- competing interests;
- acknowledgements;
- Data availability;
- Code and reproducibility resources end-matter statement;
- References;
- Supplementary material;
- Figure 1;
- drafting-note cleanup.

Esos componentes permanecen bajo responsabilidad directa del autor por instrucción previa.

## 7. Estado

```text
CURRENT_DRAFTING_PHASE = END_MATTER / AI_DISCLOSURE_CORRECTION
CURRENT_GATE = END_MATTER_B02_GENERATIVE_AI_DECLARATION_V02_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_REVIEW_AND_AUTHORIZE_AI_DECLARATION_V02_PROMPT

GESTORA_TASK_STATUS = REOPENED_FOR_AI_DISCLOSURE_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
CANONICAL_MASTER = ARTICLE_MASTER_V035
```

---

## English

D-190 reopens the previously closed Managing-AI task solely because Codex (OpenAI) coding assistance was omitted from the AI-use disclosure.

Current Elsevier policy distinguishes AI used for manuscript preparation from AI-assisted coding used in the research process. The correction therefore requires one narrowly scoped Codex transparency sentence in Methods and a revised end-of-manuscript AI declaration naming both ChatGPT and Codex.

The correction must be executed by the Writing AI, which must return exact cumulative Markdown and DOCX candidates. The Managing AI will then audit them, and the author will make the final approval decision.
