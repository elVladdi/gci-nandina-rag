# Revisión interna 0B-03A / 0B-03A Internal Review

## Español

### 1. Identificación

- Bloque: `0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`.
- Tipo de revisión: científica/editorial interna contra los seis PDF primarios asignados.
- Entrega revisada: análisis bibliográfico A–K producido por la IA de redacción.
- Estado previo: `READY_FOR_DRAFTING`.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Revisión experimental: **`NOT_REQUIRED`**.
- Aprobación del autor: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-03B: **`NOT_STARTED`**.

### 2. Resultado general

La entrega cumple el alcance de 0B-03A. Los seis PDF fueron tratados como fuentes primarias del lote, no se abrió literatura nueva, no se redactó el manuscrito y no se declaró novelty ni gap definitivo. La taxonomía funcional central es científicamente útil: distingue clasificación directa, clasificadores transformer fine-tuned, RAG que participa en la decisión de código, RAG documental para QA, in-context classification con ejemplos recuperados y clasificación multimodal.

Los hallazgos que gobiernan el lote se sostienen tras la comprobación contra los PDF primarios:

- `RAG + LLM + HS classification` ya tiene antecedente directo en THE-RAG; esa combinación no puede plantearse por sí sola como diferenciación.
- En THE-RAG el LLM participa en la determinación del código y el efecto de RAG depende de modelo/configuración; no existe mejora universal.
- ICCA-RAG es un sistema de asistencia/QA documental aduanera, no un benchmark de clasificación HS.
- Koch & Power usan modelos transformer fine-tuned como clasificadores cerrados; deben distinguirse de un LLM generativo que decide códigos mediante prompting.
- Gholamian et al. estudian taxonomías de producto Icecat/WDC-222, no HS; su valor para este artículo es metodológico y de robustez/ICL.
- En Amel et al., la magnitud del beneficio multimodal depende del baseline exacto: `D=.500 -> I+D=.582` equivale a +8.2 puntos porcentuales, mientras `T+D+C=.647 -> mejor multimodal=.653` equivale a +0.6 puntos porcentuales.

### 3. Correcciones menores obligatorias para el freeze

#### C1 — THE-RAG: identidad exacta de variante de Gemini

Los resultados HS6 Top-3 `.44, .47, .51, .59, .60` para chunks 250, 1000, 1500, 2000 y 3000 corresponden a **`gemini_1.5_flash`**, no a `gemini_1.5_flash_8b`. La tabla del paper contiene ambas variantes y deben permanecer diferenciadas. Por ejemplo, para chunk 250 el valor HS6 Top-3 de `gemini_1.5_flash_8b` es `.18`, mientras el de `gemini_1.5_flash` es `.44`.

El contraejemplo de no universalidad sí queda verificado: para `llama3.1_8b`, HS6 Top-3 es `.14` en CoT/no-RAG y `.11/.09` con THE-RAG en chunks 250/500. El freeze debe conservar esos valores con identidad de modelo y configuración explícitas.

#### C2 — Koch & Power: normalización terminológica

El paper usa el rótulo “LLM” para BERT multilingual, XLM-RoBERTa Large, RoBERTa y RoBERTa Large. Operacionalmente, en el experimento son **transformer encoders fine-tuned con cabeza de clasificación en un espacio cerrado de etiquetas**. En el artefacto congelado se debe preferir `FINE_TUNED_TRANSFORMER_CLASSIFIER`; si se conserva `FINE_TUNED_LLM`, debe quedar marcado como terminología de los autores y no equipararse a `DIRECT_GENERATIVE_LLM_CLASSIFICATION`.

#### C3 — ICCA-RAG: función de la evidencia

`RAG_EVIDENCE_SUPPORT` puede utilizarse solo con un calificador: ICCA-RAG recupera documentos/regulación para **construir contexto de respuesta en QA aduanero**. No recupera evidencia normativa después de fijar un Top-k de códigos ni demuestra el contrato `candidato -> evidencia -> explicación`. Su metadata de documento/sección y contextual backtracking constituyen procedencia técnica útil, pero no una evaluación formal de auditabilidad por candidato ni corrección jurídica.

#### C4 — Gholamian et al.: alcance del experimento humano

Los resultados humanos `76/72/97` (Icecat) y `72/67/95` (WDC-222) son correctos. Sin embargo, la finalidad principal de esa sección es **validar la calidad/recuperabilidad de las perturbaciones y comprobar si ejemplos semánticamente similares ayudan a mapear descripciones degradadas**. No debe generalizarse como evidencia de que precedentes históricos mejoran decisiones humanas de clasificación HS o aduanera. Además, el benchmark no usa códigos HS.

#### C5 — Semántica del pressure test

En la matriz F1–F5/G6, `SUPPORTS_CANDIDATE` debe leerse exclusivamente como “el paper aporta contraste compatible con la supervivencia provisional del candidato dentro de este lote”. No significa evidencia positiva de novelty ni prueba de ausencia en toda la literatura. Para el freeze, esta regla debe registrarse expresamente.

#### C6 — Multimodalidad

Preservar siempre el baseline al informar las ganancias de P06. No escribir “multimodality improves accuracy by 8.2%” sin especificar que el contraste de los autores es `D-only .500` frente a `I+D .582`, es decir, **+8.2 puntos porcentuales**. Frente al mejor texto enriquecido `T+D+C=.647`, el mejor Top-1 multimodal `.653` añade solo **+0.6 puntos porcentuales**.

### 4. Candidatos a gap después de la revisión

No se autoriza ninguna novelty. El estado correcto para 0B-03A es:

- F1/G1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F2/G2: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F3/G3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH; METHODOLOGICAL`.
- F4/G4: `CANDIDATE_GAP_ONLY — SURVIVES AS METHODOLOGICAL DISTINCTION`.
- F5/G5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED BY ICCA-RAG`.
- G6: `CANDIDATE_GAP_ONLY — SURVIVES; METHODOLOGICAL`.
- G7: `CANDIDATE_GAP_ONLY — NEW/PROVISIONAL; MUST BE PRESSURE-TESTED IN 0B-03B`.

G7 no puede congelarse como gap: 0B-03B contiene agentes y sistemas de razonamiento regulatorio que pueden mostrar una separación funcional comparable entre clasificación, recuperación, razonamiento y explicación.

### 5. Función bibliográfica provisional

La distribución propuesta es aceptable para el mapa, no como obligación de cita final:

- P01 Marra de Artiñano et al.: `KEEP_CORE`.
- P02 Koch & Power: `KEEP_CORE`.
- P03 THE-RAG: `KEEP_CORE`.
- P04 ICCA-RAG: `KEEP_CORE`.
- P05 Gholamian et al.: `KEEP_SUPPORTING`.
- P06 Amel et al.: `KEEP_CORE`.

### 6. Gate

No se requiere devolver el lote a la IA de redacción: las correcciones son de normalización y alcance, y pueden integrarse editorialmente en el artefacto congelado después de aprobación expresa del autor.

El siguiente paso autorizado es únicamente:

`AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> integrar C1–C6 -> crear freeze canónico 0B-03A -> abrir 0B-03B`.

Hasta esa aprobación, 0B-03B, 0B-04, 0C y fases posteriores permanecen cerrados.

---

## English

### 1. Identification

- Block: `0B-03A — LLM, RAG, and multimodality in customs classification/compliance`.
- Review type: internal scientific/editorial review against the six assigned primary PDFs.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Experimental review: **`NOT_REQUIRED`**.
- Author approval: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-03B: **`NOT_STARTED`**.

### 2. Overall assessment

The drafting deliverable satisfies the 0B-03A scope. The six primary PDFs were analyzed without opening new literature, manuscript drafting, or declaring novelty/final gap. Its central functional distinction is valid: direct generative classification, fine-tuned transformer classification, RAG used to determine codes, customs-document QA RAG, retrieval-assisted in-context classification, and multimodal classification are not interchangeable paradigms.

The governing batch findings survive primary-PDF verification: THE-RAG is direct prior art for RAG+LLM HS classification and its LLM participates in code determination; ICCA-RAG is customs-document QA rather than an HS-classification benchmark; Koch & Power operationally use fine-tuned transformer encoders as closed-label classifiers; Gholamian et al. do not evaluate HS codes; and Amel et al.'s multimodal gain is baseline-dependent.

### 3. Required minor corrections for freeze

**C1 — THE-RAG model identity.** The HS6 Top-3 sequence `.44/.47/.51/.59/.60` belongs to `gemini_1.5_flash`, not `gemini_1.5_flash_8b`. Keep both variants explicitly separate. The verified Llama counterexample is CoT/no-RAG `.14` versus THE-RAG `.11/.09` at chunks 250/500.

**C2 — Koch & Power terminology.** Normalize the operational category to `FINE_TUNED_TRANSFORMER_CLASSIFIER`. If `FINE_TUNED_LLM` is retained, mark it as author terminology and do not equate it with generative LLM classification.

**C3 — ICCA-RAG evidence role.** Its retrieval provides contextual evidence for customs QA, not post-ranking evidence for a fixed code candidate set. Document/section metadata and backtracking are technical provenance, not a formal per-candidate auditability or legal-correctness protocol.

**C4 — Gholamian human study.** The reported human values are correct, but the experiment primarily validates perturbation recoverability/semantic preservation and mapping with semantically similar examples. Do not generalize it into demonstrated human HS/customs decision-support benefit.

**C5 — Pressure-test semantics.** `SUPPORTS_CANDIDATE` means contrast compatible with provisional survival in this batch; it is not positive evidence of novelty or proof of absence across the literature.

**C6 — Multimodality.** Always name the baseline. The authors' `.500 -> .582` comparison is +8.2 percentage points; the strongest enriched-text-to-best-multimodal Top-1 comparison is `.647 -> .653`, or +0.6 percentage points.

### 4. Candidate-gap status

F1/F2 survive only in their narrow forms; F3 and G6 remain methodological; F4 remains a methodological distinction; F5 is further narrowed by ICCA-RAG; G7 is new and provisional and must be pressure-tested in 0B-03B. All remain `CANDIDATE_GAP_ONLY`; none establishes novelty.

### 5. Gate

No drafting-AI rerun is required. After express author approval, C1–C6 may be editorially integrated into the canonical 0B-03A freeze and only then may 0B-03B open. Experimental review is not required unless a later bibliographic interpretation directly changes a frozen experimental fact or claim.
