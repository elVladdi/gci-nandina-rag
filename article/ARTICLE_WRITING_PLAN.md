# Plan maestro de redacción / Master Writing Plan

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, sin alterar el diseño experimental aprobado y sin mezclar estados históricos del repositorio. El manuscrito se construirá únicamente con evidencia documental y experimental autorizada.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- Ningún resultado pendiente podrá redactarse como hallazgo.
- La recuperación histórica genera y ordena candidatos.
- La recuperación normativa aporta evidencia documental y no sustituye el ranking histórico.
- El LLM local explica un conjunto de candidatos previamente recuperado; no clasifica desde cero ni introduce códigos externos.
- El Top-3 histórico se describirá como recuperación de candidatos, no como accuracy global del sistema.
- La unidad SERIE y la dependencia por DAM se distinguirán en todo análisis pertinente.
- La generalidad configurable del framework no se presentará como generalización empíricamente demostrada.
- Toda afirmación deberá poder rastrearse a Proyecto, Anexo, Plan Maestro, GitHub, literatura, web o inferencia explícita.
- Todo contenido debe existir en español e inglés con equivalencia semántica.

### 3. Orden de construcción

| Fase | Entregable | Estado inicial | Gate |
|---|---|---|---|
| 0A | Ground truth documental y experimental | IN_ANALYSIS | coherencia de fuentes y estado |
| 0B | Mapa crítico de literatura y taxonomía | NOT_STARTED | cobertura y clasificación de trabajos |
| 0C | Gap, contribución y Research Questions | BLOCKED | depende de 0A y 0B |
| 0D | Arquitectura final del paper y journal fit | BLOCKED | depende de 0C |
| 1 | Methods | BLOCKED | Fase 0 aprobada |
| 2 | Related Work | BLOCKED | Fase 0 aprobada |
| 3 | Results congelados disponibles | BLOCKED | claims autorizados |
| 4 | Figuras y tablas preliminares | BLOCKED | secciones 1–3 suficientemente estables |
| 5 | Introduction provisional | BLOCKED | gap, métodos y resultados parciales estables |
| 6 | Integración EXP-11B / EXP-12 / Grupo 3 | BLOCKED | ejecución experimental cerrada |
| 7 | Results definitivos | BLOCKED | Fase 6 cerrada |
| 8 | Discussion + Limitations | BLOCKED | Results definitivos |
| 9 | Conclusions | BLOCKED | Discussion cerrada |
| 10 | Abstract + Title | BLOCKED | manuscrito completo |
| 11 | Ajuste final a revista | BLOCKED | target seleccionado y manuscrito completo |

### 4. Subfase 0A — Ground truth documental y experimental

Debe reconstruir y congelar:

- jerarquía documental vigente;
- objetivo general, OE1–OE5 y HE1–HE5 en formulación documental exacta;
- arquitectura científica vigente;
- estado FROZEN / EXECUTED / PENDING de cada experimento relevante;
- benchmark H100 y métricas autorizadas;
- restricciones sobre EXP-11A;
- estado de EXP-11B, EXP-12 y Grupo 3;
- unidades de análisis y agrupamiento;
- controles de leakage, duplicados y near-duplicates;
- límites de HE4;
- snapshot GitHub de referencia para cada corte de redacción.

**Salida:** inventario de fuentes, matriz de discrepancias y estado experimental consolidado.

### 5. Subfase 0B — Literatura

Cada trabajo se analizará por:

- problema;
- dataset;
- nivel HS objetivo;
- tarea exacta;
- input;
- método/modelo;
- clasificación, retrieval, validación, búsqueda, generación o enfoque híbrido;
- métricas;
- esquema de validación;
- uso de jerarquía;
- información normativa;
- explicabilidad;
- auditabilidad;
- precedentes históricos;
- uso de LLM;
- limitaciones;
- diferencia respecto del presente trabajo.

Taxonomía mínima:

1. clasificación directa;
2. clasificación jerárquica;
3. retrieval de códigos o precedentes;
4. validación/corrección;
5. búsqueda semántica;
6. métodos con conocimiento estructurado;
7. LLM para clasificación;
8. LLM/agentes para razonamiento normativo;
9. explicación/auditabilidad;
10. enfoques híbridos.

**Salida:** mapa comparativo de literatura y candidatos a gap, sin declarar novelty todavía.

### 6. Subfase 0C — Posicionamiento científico

Solo después de 0A y 0B se definirán:

- gap empírico;
- gap metodológico;
- gap de apoyo a decisiones/auditabilidad;
- tres formulaciones alternativas de contribución central;
- Research Questions candidatas;
- claims principales y secundarios;
- qué OE/HE pertenecen al paper y cuáles permanecen en la tesis.

**Salida:** contribución central provisional + RQs + claim-evidence matrix aprobada.

### 7. Subfase 0D — Arquitectura editorial

Debe decidir:

- IMRaD definitivo;
- orden lógico de subsecciones;
- tablas y figuras esenciales;
- secciones redactables inmediatamente;
- secciones bloqueadas por experimentos pendientes;
- target journal principal y alternativas;
- riesgos de novelty, validez, leakage, dependencia, generalización y overclaiming.

**Salida:** Gate de Fase 0: PASS / PASS WITH CORRECTIONS / BLOCKED.

### 8. Orden de redacción después de Fase 0

El orden de escritura será: Methods → Related Work → Results congelados → Figuras/Tablas → Introduction provisional → resultados pendientes → Results definitivos → Discussion → Limitations → Conclusions → Abstract → Title → adaptación final a revista.

No se redactarán Abstract, Title definitivo ni Discussion antes de disponer de resultados suficientemente cerrados.

### 9. Ciclo de cada bloque

1. Verificación de fuentes y estado experimental.
2. Actualización de claims autorizados/prohibidos.
3. Preparación de prompt bilingüe cerrado para IA de redacción.
4. Recepción del borrador bilingüe.
5. Auditoría científica, metodológica y editorial.
6. Corrección si corresponde.
7. Auditoría independiente por IA experimental.
8. Resolución de observaciones.
9. Aprobación del autor.
10. Commit semántico y actualización de plan/estado/decisiones.

### 10. Criterios de aprobación de un bloque

Un bloque solo puede pasar a `APPROVED` cuando:

- todas las afirmaciones están respaldadas;
- no contiene resultados pendientes presentados como hechos;
- respeta las funciones de histórico, normativo y LLM;
- mantiene terminología consistente;
- no confunde reproducibilidad con generalización;
- las versiones ES/EN son semánticamente equivalentes;
- las cifras y referencias coinciden en ambos idiomas;
- la auditoría experimental no presenta objeciones críticas.

`FROZEN` requiere además aprobación expresa del autor y ausencia de dependencias experimentales abiertas para ese bloque.

### 11. Journal targeting

Targets preliminares a evaluar después del análisis de literatura y contribución:

1. Knowledge-Based Systems;
2. Expert Systems with Applications;
3. Information Processing & Management;
4. Decision Support Systems;
5. Government Information Quarterly;
6. Artificial Intelligence and Law, solo si el énfasis jurídico-normativo final lo justifica.

La revista no se considerará elegida hasta completar Fase 0D y revisar scope, artículos recientes, límites de extensión y exigencias de reproducibilidad vigentes.

---

## English

### 1. Purpose

Manage the iterative construction of the main scientific article without anticipating results, altering the approved experimental design, or mixing historical repository states. The manuscript will be built only from authorized documentary and experimental evidence.

### 2. Governing principles

- The article will not be an abbreviated version of the thesis.
- No pending result may be drafted as a finding.
- Historical retrieval generates and ranks candidates.
- Normative retrieval provides documentary evidence and does not replace the historical ranking.
- The local LLM explains a previously retrieved candidate set; it does not classify from scratch or introduce external codes.
- Historical Top-3 will be described as candidate retrieval, not as overall system accuracy.
- The SERIES analysis unit and DAM-level dependence will be distinguished in every relevant analysis.
- Configurable framework generality will not be presented as empirically demonstrated generalization.
- Every claim must be traceable to the Project, Annex, Master Plan, GitHub, literature, web research, or an explicitly identified inference.
- All content must exist in Spanish and English with semantic equivalence.

### 3. Construction order

| Phase | Deliverable | Initial status | Gate |
|---|---|---|---|
| 0A | Documentary and experimental ground truth | IN_ANALYSIS | source and status consistency |
| 0B | Critical literature map and taxonomy | NOT_STARTED | coverage and work classification |
| 0C | Gap, contribution, and Research Questions | BLOCKED | depends on 0A and 0B |
| 0D | Final paper architecture and journal fit | BLOCKED | depends on 0C |
| 1 | Methods | BLOCKED | approved Phase 0 |
| 2 | Related Work | BLOCKED | approved Phase 0 |
| 3 | Available frozen Results | BLOCKED | authorized claims |
| 4 | Preliminary figures and tables | BLOCKED | sufficiently stable Sections 1–3 |
| 5 | Provisional Introduction | BLOCKED | stable gap, methods, and partial results |
| 6 | EXP-11B / EXP-12 / Group 3 integration | BLOCKED | closed experimental execution |
| 7 | Final Results | BLOCKED | closed Phase 6 |
| 8 | Discussion + Limitations | BLOCKED | final Results |
| 9 | Conclusions | BLOCKED | closed Discussion |
| 10 | Abstract + Title | BLOCKED | complete manuscript |
| 11 | Final journal adaptation | BLOCKED | selected target and complete manuscript |

### 4. Subphase 0A — Documentary and experimental ground truth

It must reconstruct and freeze:

- current documentary hierarchy;
- general objective, OE1–OE5, and HE1–HE5 in exact documentary wording;
- current scientific architecture;
- FROZEN / EXECUTED / PENDING status of every relevant experiment;
- H100 benchmark and authorized metrics;
- EXP-11A interpretation restrictions;
- EXP-11B, EXP-12, and Group 3 status;
- units of analysis and grouping;
- leakage, duplicate, and near-duplicate controls;
- HE4 limitations;
- reference GitHub snapshot for each writing cutoff.

**Output:** source inventory, discrepancy matrix, and consolidated experimental status.

### 5. Subphase 0B — Literature

Each work will be analyzed by:

- problem;
- dataset;
- target HS level;
- exact task;
- input;
- method/model;
- classification, retrieval, validation, search, generation, or hybrid approach;
- metrics;
- validation scheme;
- hierarchy use;
- normative information;
- explainability;
- auditability;
- historical precedents;
- LLM use;
- limitations;
- difference from the present work.

Minimum taxonomy:

1. direct classification;
2. hierarchical classification;
3. code or precedent retrieval;
4. validation/correction;
5. semantic search;
6. structured-knowledge methods;
7. LLMs for classification;
8. LLMs/agents for normative reasoning;
9. explanation/auditability;
10. hybrid approaches.

**Output:** comparative literature map and candidate gaps, without declaring novelty yet.

### 6. Subphase 0C — Scientific positioning

Only after 0A and 0B will the following be defined:

- empirical gap;
- methodological gap;
- decision-support/auditability gap;
- three alternative formulations of the central contribution;
- candidate Research Questions;
- primary and secondary claims;
- which OE/HE elements belong in the paper and which remain thesis-only.

**Output:** provisional central contribution + RQs + approved claim-evidence matrix.

### 7. Subphase 0D — Editorial architecture

It must decide:

- final IMRaD structure;
- logical subsection order;
- essential tables and figures;
- sections that can be drafted immediately;
- sections blocked by pending experiments;
- primary target journal and alternatives;
- novelty, validity, leakage, dependence, generalization, and overclaiming risks.

**Output:** Phase 0 Gate: PASS / PASS WITH CORRECTIONS / BLOCKED.

### 8. Drafting order after Phase 0

The writing order will be: Methods → Related Work → frozen Results → Figures/Tables → provisional Introduction → pending results → final Results → Discussion → Limitations → Conclusions → Abstract → Title → final journal adaptation.

The Abstract, final Title, and Discussion will not be drafted before results are sufficiently closed.

### 9. Cycle for each block

1. Verify sources and experimental status.
2. Update authorized/prohibited claims.
3. Prepare a constrained bilingual prompt for the drafting AI.
4. Receive the bilingual draft.
5. Perform scientific, methodological, and editorial audit.
6. Correct when necessary.
7. Obtain independent audit from the experimental AI.
8. Resolve observations.
9. Obtain author approval.
10. Make a semantic commit and update plan/status/decisions.

### 10. Block approval criteria

A block may move to `APPROVED` only when:

- every claim is supported;
- no pending result is presented as fact;
- the functions of historical retrieval, normative retrieval, and the LLM are respected;
- terminology remains consistent;
- reproducibility is not confused with generalization;
- ES/EN versions are semantically equivalent;
- figures, numbers, and references match across languages;
- the experimental audit raises no critical objections.

`FROZEN` additionally requires explicit author approval and no open experimental dependency affecting that block.

### 11. Journal targeting

Preliminary targets to be evaluated after literature and contribution analysis:

1. Knowledge-Based Systems;
2. Expert Systems with Applications;
3. Information Processing & Management;
4. Decision Support Systems;
5. Government Information Quarterly;
6. Artificial Intelligence and Law, only if the final legal-normative emphasis justifies it.

No journal will be treated as selected until Phase 0D is complete and its current scope, recent related articles, length constraints, and reproducibility requirements have been reviewed.
