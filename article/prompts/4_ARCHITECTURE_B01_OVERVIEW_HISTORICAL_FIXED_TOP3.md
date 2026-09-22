# Architecture B01 — Overview, historical retrieval, and fixed Top-3

## Español

### 1. Identidad del bloque

```text
BLOCK = ARCHITECTURE_B01
SECTION = 3. Decision-support architecture
AUTHORIZED_SUBSECTIONS = 3.1 / 3.2 / 3.3 / 3.4
STATUS_AT_ENTRY = AUTHORIZED / DRAFTING_PENDING
GOVERNING_DECISION = D-034
BASELINE_MASTER = ARTICLE_MASTER_V007
BASELINE_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx
BASELINE_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
INHERITED_CITATION_COMMENTS = 40
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FIGURES = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta **exclusivamente Architecture B01**. No avances a 3.5–3.7 ni a ninguna sección posterior.

### 2. Rol

Actúa como **IA de Redacción científica**. No actúes como IA Gestora ni como IA Experimental. No cambies gates, estados, decisiones, Plan Maestro experimental ni claims autorizados.

Tu tarea es redactar el bloque autorizado sobre el master acumulativo aprobado, preservar exactamente todo el contenido previo y entregar un candidato para auditoría. No puedes aprobar, congelar, integrar ni promover el resultado por tu cuenta.

### 3. Onboarding obligatorio y gate de entrada

Antes de redactar, lee en el orden de `article/START_HERE.md` y reconstruye el estado vivo de `article/main-manuscript`.

Verifica como mínimo:

- `article/START_HERE.md`;
- `article/ARTICLE_STATUS.md@3e8b370d419cb0ce07e6762ee84bfe8cee2b6dcb`;
- `article/ARTICLE_WRITING_PLAN.md@3f468db6ece05128cfbf91c3f916cbc2c84175d1`;
- `article/governance/D033_INTRODUCTION_B01_INTEGRATION_AND_V007_PROMOTION.md@c2b11917c3adebee6986268ec6793f9156d7e551`;
- `article/governance/D034_G6_G7_EDITORIAL_CONCURRENCY_AND_ARCHITECTURE_GATE.md@8a4124cfddea3dc1e5b5af9bece3d5f2efb5de5a`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`;
- `article/manuscript/ARTICLE_MASTER_V007.md`.

Registra el onboarding dentro de la respuesta GitHub del bloque. Por D-022, no uses el chat para una respuesta sustantiva.

Detente antes de redactar si:

- la rama no es `article/main-manuscript`;
- D-034 no está en la historia;
- `ARTICLE_MASTER_V007.md` no tiene exactamente el blob gobernante;
- el DOCX baseline no está disponible o su SHA-256 no coincide;
- el estado vivo contradice la autorización de Architecture B01.

### 4. Fuentes científicas y metodológicas obligatorias

#### 4.1. Master editorial aprobado

Usa `ARTICLE_MASTER_V007.md` y su Introduction/Related Work aprobados como restricciones de coherencia. **No los edites.**

#### 4.2. SRC-02 — fuente arquitectónica/metodológica

Debes leer la versión vigente aprobada de:

`Anexo_1_NANDINA_LLM_RAG_v13.docx`

Los sufijos de plataforma como `(5)` no definen una versión científica distinta. Identifica el documento por su contenido interno y por `SOURCE_REGISTRY.md`.

Para este bloque revisa específicamente las partes que establecen:

- recuperación histórica para el ranking principal;
- Top-3 fijo;
- precedentes históricos asociados;
- recuperación normativa posterior para evidencia;
- LLM local restringido a explicación;
- reranking LLM únicamente diagnóstico;
- arquitectura funcional del piloto y metodología donde BM25 genera el ranking histórico y fija el Top-3.

`SRC02_ACCESS = PASS` es obligatorio. Si SRC-02 no está accesible, detente con `ARCHITECTURE_SOURCE_ACCESS_REQUIRED`. No reconstruyas su contenido desde memoria, la Introduction o conversaciones anteriores.

#### 4.3. Estado experimental y fuentes primarias de implementación

Consulta el Plan Maestro experimental vivo definido como SRC-03 y confirma que el corte consumible por el artículo sigue siendo compatible con D-030. Para verificar la implementación histórica, consulta directamente en `main@ca065618d5df0019f76ef5a971e858d91c263e1f`:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `docs/exp04_bm25_historico_v02_inventory.md`;
- otros scripts/configuraciones primarios solo si una afirmación concreta de B01 lo exige.

Usa estas fuentes para comprobar acciones implementadas, no para introducir métricas o resultados.

### 5. Ground truth del bloque

Claims autorizados relevantes:

- `C01`: la recuperación histórica genera y ordena los candidatos principales;
- `C02`: la recuperación normativa aporta evidencia documental y no reemplaza el ranking histórico — solo como frontera downstream en 3.1/3.4, sin redactar todavía 3.5;
- `C03`: el LLM local explica un Top-3 previamente recuperado y no clasifica desde cero — solo como frontera downstream en 3.1, sin redactar todavía 3.6;
- `C15`: configurabilidad es propiedad de diseño, no generalización — no desarrollar 3.7 en este bloque.

Arquitectura congelada:

```text
commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ candidate-specific normative evidence retrieval
→ context construction
→ local LLM
→ controlled/auditable explanation
```

Autoridad de componentes:

```text
historical retrieval = candidate generation and ranking
normative retrieval = evidence attachment, no candidate reranking
local LLM = downstream explanation only
LLM reranker = diagnostic only, not primary flow
```

### 6. Objetivo narrativo único

Redacta la primera mitad de Section 3 para que un lector comprenda **cómo se forma y se congela el conjunto de candidatos antes de cualquier recuperación normativa o generación**.

La narrativa debe progresar así:

`end-to-end overview → query representation/normalization → historical record retrieval/ranking → code-level candidate ranking → fixed Top-3 boundary`.

No conviertas esta sección en una explicación del experimento Clase 87 ni en documentación de software.

### 7. Contenido requerido por subsección

#### 3.1. Overview and information flow

Explica el flujo extremo a extremo a nivel arquitectónico y la autoridad de cada etapa. Debe quedar inequívoco que:

- la entrada es una descripción comercial;
- la consulta normalizada alimenta la recuperación histórica;
- la recuperación histórica determina el ranking de candidatos;
- el Top-3 queda fijado antes de las etapas downstream;
- recuperación normativa, construcción de contexto y LLM operan después y no pueden cambiar la composición ni el orden del Top-3;
- ranking, evidencia y explicación son salidas funcionalmente separables.

Menciona las etapas downstream solo para delimitar el flujo; **no desarrolles** la lógica de 3.5–3.7.

Mantén el placeholder de la figura de arquitectura sin generar una figura final ni una referencia cruzada definitiva. Grupo 6/figuras continúa no autorizado.

#### 3.2. Query representation and normalization

Define la interfaz de entrada y la transformación de la descripción comercial a una representación textual determinista apta para recuperación.

Distingue:

- **contrato arquitectónico**: el recuperador recibe una consulta textual normalizada de forma reproducible;
- **instanciación experimental**: operaciones, parámetros y detalles exactos que deben documentarse después en Experimental design.

Puedes describir operaciones de normalización solo si están verificadas en SRC-02 y/o en el código gobernante. No conviertas una decisión concreta de implementación en requisito universal del framework si no está gobernado como tal.

#### 3.3. Historical candidate retrieval and ranking

Explica el mecanismo conceptual con acciones observables:

1. una colección histórica etiquetada contiene descripciones y códigos asociados;
2. la consulta normalizada se compara con los registros históricos mediante una función de recuperación/scoring;
3. los registros se ordenan por score;
4. el ranking a nivel de registro conserva el precedente histórico que sustenta cada hit;
5. cuando varios registros corresponden al mismo código, el ranking de códigos evita duplicar candidatos y conserva el precedente mejor posicionado como evidencia histórica asociada;
6. el resultado es un ranking Top-k de códigos candidatos con trazabilidad hacia precedentes históricos.

La implementación experimental usa BM25; verifica su comportamiento en el runner v0.2. Sin embargo, evita redactar BM25 como requisito universal del **contrato arquitectónico** si la frase se refiere a reinstanciaciones posibles. Los valores de `k1`, `b`, profundidades, tamaños de banco, nombres de columnas, hashes y cifras de desempeño se reservan para Experimental design/Results.

No presentes la recuperación normativa como fuente principal de candidatos.

#### 3.4. Fixed candidate set

Define operacionalmente qué significa `fixed Top-3`:

- son los tres primeros **códigos candidatos únicos** del ranking histórico que entran al procesamiento downstream;
- la membresía y el orden quedan cerrados en este punto;
- las etapas posteriores pueden asociar evidencia y generar explicación, pero no insertar, eliminar, sustituir ni reordenar esos candidatos;
- esta frontera permite atribuir la generación del ranking a la etapa histórica y evaluar downstream outputs por separado.

Evita una lista de prohibiciones estilo gobernanza. Expresa esta lógica como procedimiento científico conciso y natural.

### 8. Distinción obligatoria: arquitectura vs. instanciación experimental

Section 3 debe presentar el **procedimiento general y sus interfaces**. Section 4 será el lugar para:

- NANDINA y Clase/Capítulo 87 como testbed;
- datasets H100/DEV/EVAL y sus tamaños/hashes;
- nombre exacto de columnas;
- particiones DAM;
- configuración BM25 exacta;
- parámetros y software/hardware;
- corpus normativo concreto;
- LLM/configuración de inferencia;
- métricas y protocolos de evaluación;
- resultados.

En B01 evita desplazar esos detalles a Architecture.

### 9. Estilo obligatorio

Aplica KBS_EWG_34_V01, MWDP y SPCCR.

Redacta con patrón:

`componente → acción → entrada/salida → restricción`.

Evita:

- nominalizaciones encadenadas;
- frases largas que compriman varias contribuciones o restricciones;
- jerga de gobernanza (`contract`, `gate`, `frozen`) en la prosa publicable cuando pueda expresarse científicamente;
- retórica promocional;
- explicaciones tipo tesis excesivamente didácticas;
- abstracciones no conectadas a una acción observable.

El término `fixed` puede usarse en `fixed Top-3` por ser terminología científica congelada; no conviertas el resto de la sección en lenguaje de control editorial.

Longitud orientativa para 3.1–3.4 en Part I: **900–1,400 palabras en inglés**, ajustable si la claridad exige menos o un poco más. No rellenes por alcanzar una cuota.

### 10. Citas y comentarios Word

Architecture B01 describe principalmente el diseño propio y no requiere insertar literatura solo para decorar la sección.

Si introduces una **nueva cita científica** en el texto inglés:

- reabre la fuente primaria;
- verifica claim por claim;
- crea un comentario Word anclado a esa cita inglesa con fuente, pasaje de soporte, traducción, justificación semántica y límites.

Si no introduces citas nuevas:

```text
EXPECTED_CITATION_COMMENTS = 40
NEW_CITATION_COMMENTS = 0
```

Los 40 comentarios heredados deben preservarse exactamente.

### 11. DOCX acumulativo

Trabaja exclusivamente sobre el DOCX baseline exacto:

`ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`

SHA-256 obligatorio:

`d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`

No reconstruyas el Word desde Markdown.

Inserta 3.1–3.4 en Part I y su espejo semántico en Part II. Elimina únicamente las notas/placeholders de redacción correspondientes a las subsecciones completadas. Conserva intactos 3.5–3.7 y todas las secciones posteriores.

Antes de entregar:

- verifica OOXML;
- verifica `0 tracked changes`;
- verifica comentarios y anclajes;
- renderiza el DOCX completo;
- inspecciona visualmente **todas** las páginas;
- registra page count y QA en la respuesta.

D-027 exige entrega efectiva del DOCX candidato al autor como archivo descargable. La mera existencia en `/mnt/data` o filesystem temporal no establece custodia.

### 12. Artefactos de salida autorizados

Genera exclusivamente:

1. `article/sections/architecture/Architecture_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.md`
3. `article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md`
4. `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx` — local, con entrega efectiva al autor; **no subir a GitHub** salvo autorización posterior.

El Markdown de sección y el master candidato deben contener Part I English + Part II Spanish semantic-control mirror según la estructura vigente.

El commit de entrega debe modificar/añadir únicamente los tres artefactos Markdown autorizados. No modifiques todavía `ARTICLE_STATUS`, `ARTICLE_WRITING_PLAN`, governance, `ARTICLE_MASTER_V007.md`, claims ni fuentes.

### 13. QA obligatorio en la respuesta V01

`article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md` debe registrar, como mínimo:

```text
BLOCK = ARCHITECTURE_B01
BASELINE_MASTER_MD_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
BASELINE_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
SRC02_ACCESS = PASS
EXPERIMENTAL_MAIN_CHECKPOINT_VERIFIED = ca065618d5df0019f76ef5a971e858d91c263e1f
SECTIONS_DRAFTED = 3.1 / 3.2 / 3.3 / 3.4
ARCHITECTURE_BEFORE_TESTBED = PASS
HISTORICAL_RANKING_AUTHORITY = PASS
FIXED_TOP3_BOUNDARY = PASS
NORMATIVE_STAGE_NOT_USED_FOR_RERANKING = PASS
LLM_NOT_USED_AS_CLASSIFIER = PASS
DIAGNOSTIC_RERANKER_NOT_IN_PRIMARY_FLOW = PASS
RESULTS_LEAKAGE = 0
CLASS87_PREMATURE_SCOPE = 0
NEW_BIBLIOGRAPHIC_CITATION_COUNT = <N>
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = <N>
TRACKED_CHANGES = 0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
SPCCR_ABSTRACTION_DENSITY = PASS
SPCCR_AGENT_ACTION_OBJECT_CLARITY = PASS
SPCCR_OBSERVABLE_PROCESS_LANGUAGE = PASS
SPCCR_GOVERNANCE_JARGON_LEAKAGE = PASS
SPCCR_SENTENCE_LOAD = PASS
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = <N>
CANDIDATE_DOCX_SHA256 = <SHA256>
AUTHOR_HANDOFF_DOCX = COMPLETED
PRIOR_APPROVED_TEXT_MODIFIED = NO
SECTIONS_3_5_TO_3_7_MODIFIED = NO
LATER_SECTIONS_MODIFIED = NO
ARTICLE_MASTER_V008 = NOT_PROMOTED
ARCHITECTURE_B02 = NOT_STARTED
EXPERIMENTAL_DESIGN = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 14. Stop conditions

Detente sin redactar o sin integrar si ocurre cualquiera de estas condiciones:

- baseline Markdown o DOCX no coincide exactamente;
- SRC-02 no está accesible;
- Plan Maestro/SRC-03 presenta contradicción material con D-034 o el corte editorial;
- la descripción que pretendes escribir exige un dato arquitectónico no sustentado;
- no puedes preservar el DOCX acumulativo y sus comentarios;
- el alcance requerido excede 3.1–3.4.

Registra el blocker en la respuesta V01; no improvises una solución.

### 15. Prohibiciones explícitas

No:

- redactes 3.5–3.7;
- redactes Experimental design, Results o Discussion;
- generes/finalices Figure 1;
- actives Grupo 6 o Grupo 7;
- modifiques Plan Maestro experimental;
- recalcules métricas;
- introduzcas resultados;
- uses H100/Clase 87 para definir la arquitectura general;
- declares novelty, SOTA, “first”, superioridad global o ausencia universal;
- conviertas configurabilidad en generalización;
- conviertas evidencia en legal correctness;
- promuevas `ARTICLE_MASTER_V008`;
- modifiques archivos de status/plan/governance.

### 16. Respuesta final de chat

Después del commit y del handoff real del DOCX, responde en chat únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md@<commit_sha>`

junto con el archivo DOCX descargable exigido por D-027. No añadas explicación sustantiva en chat.

---

# English

## 1. Block identity and single scope

Execute **Architecture B01 only**, covering Sections 3.1–3.4 of `Decision-support architecture`. D-034 authorizes this block and no later block.

The governing baseline is `ARTICLE_MASTER_V007.md`, Git blob `436e0522db0ac348efaed86f4e53a7e6db372471`, plus the exact cumulative DOCX `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`, SHA-256 `d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`, with 40 inherited citation comments.

Architecture B02, Experimental design, Results, Discussion, and figures remain unauthorized.

## 2. Role and onboarding

Act as the scientific Drafting AI, not the Managing AI or Experimental AI. Read the mandatory onboarding files and verify the live branch state, D-033, D-034, Writing Plan V2.8, Article Status, Source Registry, Claim–Evidence Matrix, Style Guide, and `ARTICLE_MASTER_V007.md` before drafting. Record the onboarding in the versioned response rather than in substantive chat text.

Stop if the branch/state/baseline does not match the governing identities.

## 3. Mandatory sources

Read current SRC-02, `Anexo_1_NANDINA_LLM_RAG_v13.docx` (platform filename suffixes do not define scientific versions), specifically the passages governing historical ranking, fixed Top-3, historical precedents, downstream normative evidence, explanation-only local LLM, diagnostic reranking, and the methodology where BM25 generates the historical ranking and fixes the Top-3.

`SRC02_ACCESS = PASS` is mandatory. Do not reconstruct SRC-02 from memory or earlier conversation.

Verify the implementation against the experimental Master Plan and `main@ca065618d5df0019f76ef5a971e858d91c263e1f`, especially:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `docs/exp04_bm25_historico_v02_inventory.md`.

Use these implementation sources to verify actions, not to leak results into Architecture.

## 4. Governing ground truth

Authorized claims include C01 (historical retrieval generates/ranks candidates), C02 (normative retrieval provides evidence without replacing historical ranking), C03 (the local LLM explains a previously retrieved Top-3 and does not classify from scratch), and C15 (configurability is a design property, not empirical generalization).

The mandatory flow is:

`commercial description → normalization → historical retrieval → historical Top-k ranking → fixed Top-3 → candidate-specific normative evidence retrieval → context construction → local LLM → controlled/auditable explanation`.

Historical retrieval owns candidate generation/ranking. Normative retrieval attaches evidence without reranking. The local LLM is explanation-only. LLM reranking is diagnostic and not part of the primary flow.

## 5. Narrative objective and subsection requirements

The single narrative objective is to explain **how the candidate set is formed and made immutable before any normative retrieval or generation**.

### 3.1 Overview and information flow

Explain the end-to-end flow and component authority at architecture level. The normalized query feeds historical retrieval; historical retrieval determines the ranking; the Top-3 is fixed before downstream stages; normative retrieval/context construction/local LLM occur later and cannot change Top-3 membership or order. Mention downstream stages only to delimit the flow; do not draft Sections 3.5–3.7. Keep the architecture-figure placeholder but do not generate/finalize a figure or definitive cross-reference.

### 3.2 Query representation and normalization

Define the input interface and deterministic transformation from commercial description to a reproducible textual query representation. Distinguish the architecture-level interface from exact experimental operations/parameters, which belong in Experimental design. Only describe normalization operations that are verified in SRC-02 and/or governing code.

### 3.3 Historical candidate retrieval and ranking

Describe a labeled historical collection, query-to-record scoring, descending record ranking, traceability to supporting historical precedents, code-level deduplication that preserves the highest-ranked supporting precedent, and the resulting Top-k code ranking. Verify the current experimental behavior against the v0.2 runner. The experiment uses BM25, but do not turn BM25 into a universal interface requirement when discussing re-instantiation. Exact parameters, depths, dataset sizes, hashes, column names, and performance metrics belong later.

### 3.4 Fixed candidate set

Define the fixed Top-3 as the first three unique code candidates from the historical ranking passed downstream. Membership and order become immutable at this boundary. Later stages may attach evidence and produce explanations but may not insert, delete, substitute, or reorder candidates. Express this as natural scientific procedure rather than governance-style prohibitions.

## 6. Architecture versus experimental instantiation

Section 3 presents the general procedure and interfaces. Section 4 will contain the NANDINA/Class-87 testbed, H100/DEV/EVAL identities, DAM partitions, exact BM25 configuration, concrete corpus/model/settings, evaluation protocols, software/hardware, hashes, and results. Do not move those details into B01.

## 7. Style, citations, and DOCX

Apply KBS_EWG_34_V01, MWDP, SPCCR, and the pattern `component → action → input/output → constraint`. Avoid abstraction density, chained nominalizations, governance jargon in publication prose, thesis-like didactic exposition, promotional language, and overloaded sentences. English Part I target length is approximately 900–1,400 words for 3.1–3.4, but clarity overrides quota.

Do not add literature merely for decoration. Any new scientific citation requires primary-source reopening and a Word comment anchored to the English citation with source, supporting passage, translation, semantic rationale, and limits. If no new citations are needed, preserve exactly the 40 inherited comments.

Work on the exact cumulative DOCX; never reconstruct it from Markdown. Insert 3.1–3.4 in Part I and the semantically equivalent Spanish mirror in Part II, remove only the drafting notes/placeholders for the completed subsections, and preserve 3.5–3.7 and all later material. Require zero tracked changes, structural comment checks, full-document rendering, visual inspection of every page, SHA-256 reporting, and actual author handoff under D-027.

## 8. Authorized outputs

Create only:

- `article/sections/architecture/Architecture_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.md`;
- `article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md`;
- local `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx`, actually handed to the author and not uploaded to GitHub.

The GitHub delivery commit must add/modify only the three authorized Markdown artifacts. Do not update status/plan/governance, promote V008, or open any later block.

The response must record all baseline/source checks, scope controls, architecture boundaries, EN/ES equivalence, five SPCCR checks, comments, zero tracked changes, OOXML/full-render QA, candidate DOCX SHA-256, actual author handoff, no prior-text modification, no 3.5–3.7/later-section modification, and `FINAL_GAP = NOT_DEFINED`, `NOVELTY = NOT_DECLARED`.

## 9. Stop conditions and final chat response

Stop rather than infer or reconstruct if the exact baselines fail, SRC-02 is inaccessible, the experimental state materially conflicts with the editorial cutoff, an architecture fact lacks a governing source, DOCX/comments cannot be preserved, or the requested content would exceed 3.1–3.4.

After a successful commit and actual DOCX handoff, chat must contain only:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md@<commit_sha>`

plus the downloadable DOCX required by D-027.