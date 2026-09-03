# 0B-03A — LLM, RAG y multimodalidad en clasificación/compliance aduanero / LLM, RAG, and multimodality in customs classification/compliance

## Español

### 1. Estado

- Bloque: `0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis A–K de seis PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Aprobación expresa del autor: recibida el `2026-09-02`.
- Revisión experimental: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.

Registros gobernantes:

- `article/reviews/0B03A_INTERNAL_REVIEW.md`;
- `article/reviews/0B03A_AUTHOR_APPROVAL.md`.

Este artefacto congela el mapa canónico del sub-lote. `KEEP_CORE` o `KEEP_SUPPORTING` expresan función dentro del mapa, no obligación de cita final. La admisibilidad bibliográfica final sigue sometida a `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Reglas canónicas de interpretación

1. `RAG + LLM + HS` **no** es una combinación novedosa por sí misma.
2. Debe distinguirse el LLM que **decide/clasifica** del LLM que **explica candidatos ya fijados**.
3. `RAG_CLASSIFICATION` ≠ `RAG_EVIDENCE_SUPPORT` ≠ RAG documental para QA.
4. Reranking ≠ explanation.
5. Procedencia técnica de documentos/sections ≠ auditabilidad formal por candidato ≠ corrección jurídica.
6. Fine-tuned transformer classification ≠ LLM generativo que produce códigos mediante prompting.
7. In-context examples/precedentes similares ≠ evidencia normativa documental.
8. Multimodalidad no implica mejora general; toda ganancia debe informar el baseline exacto.
9. Ausencia de group split documentado no demuestra leakage.
10. `SUPPORTS_CANDIDATE` en el pressure test significa solo **contraste compatible con supervivencia provisional en este lote**; no constituye evidencia de novelty ni prueba de ausencia en toda la literatura.
11. Claims de terceros permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta comprobar su fuente primaria.

### 3. Matriz canónica de los seis trabajos

| ID | Trabajo | Tarea real / función | Datos principales | Resultado/rasgo relevante | Caveat gobernante | Función |
|---|---|---|---|---|---|---|
| P01 | Marra de Artiñano, Riottini Depetris y Volpe Martincus, *Automatic Product Classification in International Trade: Machine Learning and Large Language Models* | `DIRECT_LLM_CLASSIFICATION` HS2/4/6; GPT-3.5 zero-shot frente a ML clásico | Datos aduaneros de Chile; evaluación en Paraguay y USDA; ML entrenado con ~1 millón de observaciones chilenas | GPT-3.5 ≈62% HS6, 77% HS4, 86% HS2 en Chile; comportamiento más estable entre fuentes que varios ML entrenados sobre Chile | GPT es obligado a emitir best estimate ante insuficiencia; no RAG, no normativa recuperada, no trazabilidad; el pequeño experimento humano N=100 no autoriza productividad institucional general | `KEEP_CORE` |
| P02 | Koch & Power, *Automating Harmonized System (HS) Code Classification from Unstructured Shipping Manifests using Large Language Models* | `FINE_TUNED_TRANSFORMER_CLASSIFIER` para HS6 | ~1.4M manifiestos de India; >3,000 HS6; 96 capítulos; split estratificado 60/20/20 | XLM-R Large: accuracy 87.9%, weighted F1 .876 | “LLM” es terminología de autores; operacionalmente son encoders transformer fine-tuned con classification head y label space cerrado; no RAG/evidencia/auditabilidad; no group split documentado | `KEEP_CORE` |
| P03 | Kim, Kim & Choi, THE-RAG | `RAG_CLASSIFICATION`; dense + BM25 + reranking + dos etapas; LLM decide el código | Tabla arancelaria, notas explicativas y casos; test principal de 100 consultas complejas | `gemini_1.5_flash` HS6 Top-3 = .44/.47/.51/.59/.60 para chunks 250/1000/1500/2000/3000 | Esos valores **no** corresponden a `gemini_1.5_flash_8b`. RAG no mejora universalmente: `llama3.1_8b` CoT/no-RAG .14 vs THE-RAG .11/.09 en chunks 250/500. La evidencia participa en la clasificación; no existe Top-k histórico protegido ni auditoría formal por caso | `KEEP_CORE` |
| P04 | Hu et al., ICCA-RAG | `RAG_EVIDENCE_SUPPORT` **para QA documental aduanero**, no benchmark HS | PDFs, imágenes, tablas, texto y materiales regulatorios; BM25 + BGE-M3 + FAISS/HNSW + query rewriting | Reporta mejoras de answer correctness 20.1%, relevancy 15.3% y faithfulness 18.7% frente a comparadores | Las métricas son de QA/generación, no accuracy HS. Document ID/section y contextual backtracking = procedencia técnica; no equivalen a evidencia post-ranking sobre Top-k fijo, auditoría formal por candidato ni legal correctness | `KEEP_CORE` |
| P05 | Gholamian et al., *LLM-Based Robust Product Classification in Commerce and Compliance* | `IN_CONTEXT_CLASSIFICATION` + `ROBUSTNESS_EVALUATION`; retrieval de Top-5 ejemplos similares | Icecat y WDC-222; **no HS** | GPT-4 few-shot es el más robusto bajo perturbaciones. Estudio humano: Icecat 76/72/97 y WDC-222 72/67/95 en clean/combined/combined+similar examples | El experimento humano sirve principalmente para validar perturbaciones/recuperabilidad semántica y mapeo con ejemplos similares; no demuestra beneficio humano de clasificación HS/aduanera. Precedentes similares ≠ RAG documental | `KEEP_SUPPORTING` |
| P06 | Amel et al., *Multimodal Approach for Harmonized System Code Prediction* | `MULTIMODAL_CLASSIFICATION` HS6 | 2,144 declaraciones; 16 HS6; texto + título/categoría + imagen; split 80/10/10 | D-only .500 Top-1; I+D .582; T+D+C .647; mejor multimodal .653 Top-1 | `.500 -> .582` = **+8.2 puntos porcentuales** frente a D-only; frente al mejor texto enriquecido `.647 -> .653` = **+0.6 pp**. No RAG, normativa, explicación ni group split documentado | `KEEP_CORE` |

### 4. Correcciones C1–C6 congeladas

#### C1 — THE-RAG: identidad exacta de modelo

La serie HS6 Top-3 `.44/.47/.51/.59/.60` corresponde a `gemini_1.5_flash`, no a `gemini_1.5_flash_8b`. Ambas variantes deben permanecer separadas en cualquier uso posterior. El contraejemplo de no universalidad de RAG queda congelado como `llama3.1_8b`: `.14` CoT/no-RAG frente a `.11/.09` THE-RAG en chunks 250/500.

#### C2 — Koch & Power: taxonomía operacional

Usar `FINE_TUNED_TRANSFORMER_CLASSIFIER` como categoría funcional. Si se reproduce “LLM”, indicar que es terminología del paper y no equipararla con clasificación generativa por prompting.

#### C3 — ICCA-RAG: función exacta de evidence support

Su retrieval construye contexto para **QA aduanero**. No implementa el contrato del proyecto actual `ranking histórico fijado -> evidencia normativa posterior -> explicación sin reordenar`. La metadata de documento/sección y backtracking aportan procedencia técnica, no evaluación formal de auditabilidad ni legal correctness.

#### C4 — Gholamian: alcance del experimento humano

Los valores humanos reportados son válidos dentro del estudio, pero no deben migrar a una afirmación de beneficio humano para clasificación HS. Icecat/WDC-222 son taxonomías de producto, no códigos HS.

#### C5 — Pressure test

`SUPPORTS_CANDIDATE` significa solamente que el trabajo no falsifica y aporta contraste compatible con la supervivencia provisional del candidato dentro del sub-lote. No es evidencia de novelty ni demostración de ausencia en la literatura total.

#### C6 — Multimodalidad

Toda cifra de mejora debe declarar su baseline. No escribir “multimodality improves accuracy by 8.2%” sin especificar `D-only=.500 -> I+D=.582`, equivalente a +8.2 pp. Frente al texto enriquecido, la mejora Top-1 máxima es `.647 -> .653`, +0.6 pp.

### 5. Patrones congelados del sub-lote

- “LLM” cubre paradigmas diferentes: prompting generativo, transformer fine-tuning, RAG con decisión de código e in-context classification.
- La posición causal del LLM en el pipeline es más informativa que su mera presencia.
- RAG puede decidir el código, apoyar QA documental o aportar contexto; el término RAG no determina por sí mismo la función del conocimiento.
- Descripciones incompletas, abreviadas o ambiguas afectan a varios enfoques y pueden motivar estrategias de robustez/contexto.
- Precedentes semánticamente similares ya se utilizan como ejemplos para ICL; no son novedosos por sí mismos.
- RAG no garantiza mejora: el efecto depende del modelo, retrieval, chunking y configuración.
- Multimodalidad puede ayudar, pero la magnitud depende del baseline y del conjunto de features textuales disponible.
- Procedencia técnica/faithfulness no equivale a auditabilidad jurídica ni a corrección sustantiva.

### 6. Estado congelado de candidatos provisionales

Todos permanecen `CANDIDATE_GAP_ONLY`; ninguno constituye novelty.

- **F1/G1 — `SURVIVES IN NARROW FORM`:** precedentes históricos recuperados generan/fijan ranking y la normativa se recupera después exclusivamente para respaldar esos candidatos sin reordenarlos.
- **F2/G2 — `SURVIVES IN NARROW FORM`:** generador posterior limitado a un Top-k ya fijado, sin capacidad de incorporar códigos externos ni alterar el orden.
- **F3/G3 — `SURVIVES THIS BATCH; METHODOLOGICAL`:** control explícito de dependencia por unidad administrativa/grupo cuando observaciones relacionadas pueden cruzar particiones.
- **F4/G4 — `SURVIVES AS METHODOLOGICAL DISTINCTION`:** candidate/predictive performance, similitud o coherence scoring no equivalen a corrección sustantiva/jurídica adjudicada independientemente.
- **F5/G5 — `FURTHER NARROWED BY ICCA-RAG`:** evaluación formal, por salida/caso, de trazabilidad y auditabilidad documental, diferenciada de metadata, faithfulness, relevance o accuracy.
- **G6 — `SURVIVES; METHODOLOGICAL`:** ground truth independiente/adjudicado para claims de correctness, separado de labels históricos asumidos correctos.
- **G7 — `NEW/PROVISIONAL; PRESSURE TEST REQUIRED IN 0B-03B`:** separación explícita entre papel clasificatorio y papel explicativo del LLM dentro de sistemas aduaneros híbridos.

### 7. Claims que este freeze prohíbe

- “RAG + LLM para HS es novedoso”.
- “Los LLM de Koch & Power generan libremente el código”.
- “ICCA-RAG es un benchmark de clasificación HS”.
- “Faithfulness o backtracking prueban corrección jurídica”.
- “Gholamian demuestra que precedentes históricos mejoran decisiones humanas HS”.
- “La multimodalidad mejora 8.2% frente a cualquier baseline textual”.
- “RAG mejora necesariamente la clasificación”.
- “La ausencia de group split en antecedentes demuestra leakage”.
- cualquier F1–F5/G6/G7 como gap definitivo o novelty antes de 0C.

### 8. Próximo gate

0B-03A queda cerrado. El siguiente bloque autorizado es `0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`. Su función será someter a presión F1–F5/G6/G7 frente a trabajos agentic, regulatory-search y hierarchical reasoning.

---

## English

### 1. Status

- Block: `0B-03A — LLM, RAG, and multimodality in customs classification/compliance`.
- Status: **`APPROVED / FROZEN`**.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Express author approval: received on `2026-09-02`.
- Experimental review: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Definitive gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.

Governing records: `article/reviews/0B03A_INTERNAL_REVIEW.md` and `article/reviews/0B03A_AUTHOR_APPROVAL.md`.

### 2. Canonical interpretation rules

`RAG + LLM + HS` is not novel by itself. Distinguish LLMs that determine codes from LLMs that explain fixed candidates; RAG classification from RAG evidence support and customs QA; reranking from explanation; technical provenance from formal auditability and legal correctness; fine-tuned transformer classifiers from generative LLM code production; similar-example ICL from normative evidence; and multimodal effects by exact baseline. Missing grouped splits do not prove leakage. `SUPPORTS_CANDIDATE` is only provisional within-batch contrast, not novelty evidence.

### 3. Canonical six-paper map

- **P01 Marra de Artiñano et al.** — direct GPT-3.5 HS classification; cross-source comparison; no RAG/normative evidence/auditability; `KEEP_CORE`.
- **P02 Koch & Power** — operationally fine-tuned transformer encoders in a closed HS6 label space; XLM-R Large 87.9% accuracy / .876 weighted F1; `KEEP_CORE`.
- **P03 THE-RAG** — RAG classification where the LLM determines the HS code. The `.44/.47/.51/.59/.60` HS6 Top-3 series belongs to `gemini_1.5_flash`; RAG is not universally beneficial, with `llama3.1_8b` `.14` no-RAG versus `.11/.09` RAG at chunks 250/500; `KEEP_CORE`.
- **P04 ICCA-RAG** — customs-document QA RAG with BM25/BGE-M3/FAISS-HNSW and document/section provenance; not HS classification and not formal per-candidate auditability; `KEEP_CORE`.
- **P05 Gholamian et al.** — robust product-taxonomy classification on Icecat/WDC-222, not HS; similar-example ICL and perturbation study; `KEEP_SUPPORTING`.
- **P06 Amel et al.** — multimodal HS6 classification; +8.2 percentage points only against D-only `.500 -> .582`, and +0.6 points against enriched-text `.647 -> .653`; `KEEP_CORE`.

### 4. Frozen corrections C1–C6

C1 preserves exact THE-RAG model identity and the Llama no-universal-benefit counterexample. C2 normalizes Koch & Power to `FINE_TUNED_TRANSFORMER_CLASSIFIER`. C3 restricts ICCA-RAG evidence support to customs QA context rather than fixed-candidate post-ranking evidence. C4 limits the Gholamian human-study interpretation and preserves that its datasets are not HS. C5 defines pressure-test labels as provisional, not novelty evidence. C6 requires every multimodal-gain claim to state its exact baseline.

### 5. Frozen patterns

LLM-based classification spans technically different paradigms; the LLM's causal role matters more than its mere presence. RAG can determine a code, support customs QA, or provide context and does not guarantee improvement. Similar precedents are already used for ICL. Description quality matters across studies. Multimodal gains are baseline-dependent. Technical provenance/faithfulness does not establish legal correctness or formal auditability.

### 6. Provisional candidate status

F1/F2 survive only in narrow form; F3 and G6 remain methodological; F4 remains a methodological distinction; F5 is further narrowed by ICCA-RAG; and G7 is new/provisional and must be pressure-tested in 0B-03B. All remain `CANDIDATE_GAP_ONLY`; none establishes novelty.

### 7. Prohibited downstream claims

Do not claim RAG+LLM+HS as novelty; do not treat Koch & Power as free generative code production; do not treat ICCA-RAG as HS classification or faithfulness/backtracking as legal correctness; do not generalize Gholamian to human HS decision improvement; do not state a generic 8.2% multimodal gain; do not state that RAG necessarily improves classification; and do not infer leakage from missing grouped splits.

### 8. Next gate

0B-03A is closed. The next authorized block is `0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning`, which must pressure-test F1–F5/G6/G7 before any Phase 0C gap decision.
