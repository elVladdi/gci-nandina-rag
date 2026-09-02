# Registro de decisiones / Decision Log

## Español

Este archivo conserva decisiones metodológicas y editoriales ya resueltas para evitar contradicciones futuras. Las decisiones solo se modifican mediante una nueva entrada que documente el cambio y su motivo.

### D-001 — Rama exclusiva del artículo

**Decisión:** usar `article/main-manuscript` exclusivamente para el artículo científico principal.

**Motivo:** separar redacción y revisión del desarrollo experimental.

**Estado:** FROZEN.

### D-002 — Bilingüismo obligatorio

**Decisión:** todo artefacto de redacción, planificación, revisión y decisión que se incorpore a GitHub dentro del entorno del artículo debe existir en español e inglés con equivalencia semántica.

**Motivo:** mantener control semántico en español y una versión inglesa publicable sin divergencias científicas.

**Estado:** FROZEN.

### D-003 — Orden de redacción

**Decisión:** no redactar el manuscrito en orden de lectura. Tras Fase 0, el orden será Methods → Related Work → Results congelados → figuras/tablas → Introduction provisional → Results definitivos → Discussion → Limitations → Conclusions → Abstract → Title.

**Motivo:** minimizar reescritura y evitar formular contribuciones antes de conocer evidencia y literatura.

**Estado:** FROZEN.

### D-004 — Función del Top-3

**Decisión:** Top-3 histórico se denomina recuperación de candidatos; no se denomina accuracy global del RAG/sistema.

**Motivo:** la métrica evalúa presencia del código de referencia en el conjunto de candidatos recuperados.

**Estado:** FROZEN.

### D-005 — Separación funcional

**Decisión:** recuperación histórica = generación/ranking de candidatos; recuperación normativa = evidencia documental; LLM local = explicación controlada del conjunto recuperado.

**Motivo:** preservar la arquitectura científica vigente y evitar reinterpretar el LLM como clasificador autónomo.

**Estado:** FROZEN.

### D-006 — Repositorios

**Decisión:** `gci-nandina-rag` conserva desarrollo y artículo en rama separada; `gci-nandina-rag-reproducibility` se destina al paquete científico limpio de reproducción/replicación final.

**Motivo:** separar historial experimental de artefacto reproducible publicado.

**Estado:** FROZEN.

### D-007 — Commit gate

**Decisión:** los bloques de manuscrito se integrarán como versiones aprobadas después de auditoría editorial/metodológica, auditoría experimental independiente y aprobación del autor.

**Motivo:** evitar que borradores no validados se conviertan en estado editorial de referencia.

**Estado:** FROZEN.

### D-008 — Generalidad del framework

**Decisión:** la configurabilidad para otros capítulos, jurisdicciones o niveles arancelarios se describirá como propiedad de diseño, no como generalización empíricamente demostrada.

**Motivo:** la evaluación empírica actual está delimitada al alcance experimental definido.

**Estado:** FROZEN.

### D-009 — Fuente operativa del Plan Maestro experimental

**Decisión:** para el artículo, la copia GitHub ubicada en `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`, se considera equivalente operativo de la copia local iterativa `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`.

**Motivo:** la copia GitHub permite a cualquier IA del flujo consultar directamente la fuente operativa vigente y evita exigir al autor que adjunte repetidamente la copia local.

**Regla:** mientras esta equivalencia permanezca vigente en `SOURCE_REGISTRY.md`, el Plan Maestro debe consultarse directamente en GitHub y no solicitarse como adjunto. El archivo de esa rama es una fuente viva mientras la investigación siga abierta; su blob SHA se registra como snapshot de cada corte de revisión y no como identidad inmutable de la fuente.

**Estado:** FROZEN.

### D-010 — Idioma del chat y bilingüismo de GitHub

**Decisión:** todas las respuestas de las IAs al autor dentro del chat deben emitirse en español, salvo solicitud expresa del autor en otro idioma. La obligación español-inglés aplica exclusivamente a los artefactos que se creen o integren en GitHub dentro del entorno del artículo.

**Motivo:** separar la interacción operativa, que se mantiene en español, de los artefactos editoriales versionados, que deben conservar equivalencia semántica bilingüe.

**Regla:** un borrador, auditoría o análisis entregado en chat debe presentarse en español. Si posteriormente ese contenido se aprueba para incorporarse a GitHub, la versión que se versiona debe contener español e inglés con equivalencia semántica. No se exige duplicar en inglés las respuestas ordinarias del chat.

**Estado:** FROZEN.

---

## English

This file preserves methodological and editorial decisions that have already been resolved in order to prevent future contradictions. Decisions may only be changed through a new entry documenting the change and its rationale.

### D-001 — Dedicated article branch

**Decision:** use `article/main-manuscript` exclusively for the main scientific article.

**Rationale:** separate writing and review from experimental development.

**Status:** FROZEN.

### D-002 — Mandatory bilingualism

**Decision:** every writing, planning, review, and decision artifact incorporated into GitHub within the article workspace must exist in Spanish and English with semantic equivalence.

**Rationale:** preserve semantic control in Spanish and a publication-ready English version without scientific divergence.

**Status:** FROZEN.

### D-003 — Drafting order

**Decision:** do not draft the manuscript in reading order. After Phase 0, the order will be Methods → Related Work → frozen Results → figures/tables → provisional Introduction → final Results → Discussion → Limitations → Conclusions → Abstract → Title.

**Rationale:** minimize rewriting and avoid formulating contributions before evidence and literature are known.

**Status:** FROZEN.

### D-004 — Role of Top-3

**Decision:** historical Top-3 is termed candidate retrieval; it is not termed overall RAG/system accuracy.

**Rationale:** the metric evaluates whether the reference code is present in the retrieved candidate set.

**Status:** FROZEN.

### D-005 — Functional separation

**Decision:** historical retrieval = candidate generation/ranking; normative retrieval = documentary evidence; local LLM = controlled explanation of the retrieved set.

**Rationale:** preserve the current scientific architecture and avoid reinterpreting the LLM as an autonomous classifier.

**Status:** FROZEN.

### D-006 — Repositories

**Decision:** `gci-nandina-rag` retains development and the article in a separate branch; `gci-nandina-rag-reproducibility` is reserved for the clean final scientific reproduction/replication package.

**Rationale:** separate experimental history from the published reproducibility artifact.

**Status:** FROZEN.

### D-007 — Commit gate

**Decision:** manuscript blocks will be integrated as approved versions only after editorial/methodological audit, independent experimental audit, and author approval.

**Rationale:** prevent unvalidated drafts from becoming the reference editorial state.

**Status:** FROZEN.

### D-008 — Framework generality

**Decision:** configurability for other chapters, jurisdictions, or tariff levels will be described as a design property, not as empirically demonstrated generalization.

**Rationale:** the current empirical evaluation is bounded by the defined experimental scope.

**Status:** FROZEN.

### D-009 — Operational source of the experimental Master Plan

**Decision:** for the article workflow, the GitHub copy at `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`, is treated as the operational equivalent of the iterative local copy `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`.

**Rationale:** the GitHub copy allows any AI in the workflow to consult the current operational source directly and avoids repeatedly requiring the author to attach the local copy.

**Rule:** while this equivalence remains current in `SOURCE_REGISTRY.md`, the Master Plan must be consulted directly on GitHub and must not be requested as an attachment. The file on that branch is a living source while the research remains open; its blob SHA is recorded as the snapshot for each review cutoff rather than as the immutable identity of the source.

**Status:** FROZEN.

### D-010 — Chat language and GitHub bilingualism

**Decision:** all AI responses to the author in chat must be produced in Spanish unless the author expressly requests another language. The Spanish-English requirement applies exclusively to artifacts created or integrated into GitHub within the article workspace.

**Rationale:** separate operational interaction, which remains in Spanish, from versioned editorial artifacts, which must preserve bilingual semantic equivalence.

**Rule:** a draft, audit, or analysis delivered in chat must be presented in Spanish. If that content is later approved for incorporation into GitHub, the version committed to GitHub must contain Spanish and English with semantic equivalence. Ordinary chat responses do not need to be duplicated in English.

**Status:** FROZEN.
