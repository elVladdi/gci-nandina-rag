# Fase 1 — Methods B01 — Design, scope, and units / Prompt cerrado de redacción

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Ejecuta **únicamente `Methods B01 — Design, scope, and units`**. No avances a B02 ni a ninguna otra sección.

Antes de redactar, lee íntegramente y aplica, en este orden:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — **MWDP_V1.0, obligatorio e íntegro**;
10. `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`;
11. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
12. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
13. `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`;
14. el `SRC-03` vivo indicado en `SOURCE_REGISTRY.md`;
15. este prompt.

No uses memoria de chats como sustituto de esos archivos. Si un archivo gobernante contradice otro, no reconcilies silenciosamente: detén únicamente la afirmación afectada y repórtala.

### Estado autorizado

```text
PHASE_1 = OPENED
METHODS_B01 = READY_FOR_DRAFTING
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
MWDP_VERSION = MWDP_V1.0
TARGET_A = Knowledge-Based Systems
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT_AT_ENTRY
```

El Plan Maestro vivo registra avances posteriores de Grupo 3 que todavía no han sido reconciliados editorialmente como claims del artículo. **No utilices esos resultados en B01.**

### Objetivo del bloque

Redactar una subsección Methods 3.1 publicable que defina con precisión el diseño general, el alcance y las unidades del estudio, sin anticipar procedimientos detallados ni resultados.

Debe dejar inequívocamente establecido:

- que el estudio es un **piloto experimental aplicado y offline** de apoyo a la recomendación auditable de subpartidas NANDINA;
- que el alcance empírico corresponde al ámbito congelado de **Clase/Capítulo 87** según las fuentes gobernantes;
- que la salida es de **apoyo a decisión y no vinculante**, y que la revisión experta se mantiene fuera del flujo automático;
- la separación funcional: recuperación histórica = generación/ranking de candidatos; recuperación normativa = evidencia documental para candidatos ya fijados, sin reranking; LLM local = explicación controlada del Top-3 fijo, sin clasificar desde cero ni insertar/eliminar/sustituir/reordenar candidatos ni retroalimentar la clasificación;
- `unidad de observación/análisis = SERIE de DAM`;
- `unidad de agrupamiento/dependencia = DAM`;
- `unidad de consulta = SERIE / descripción comercial normalizada`;
- `unidad de salida = ranking histórico Top-k / Top-3 histórico fijo`;
- que la configurabilidad arquitectónica no equivale a generalización empírica fuera del alcance evaluado.

### Claims permitidos

Usa solo lo necesario de:

- `C01` — recuperación histórica genera y ordena candidatos;
- `C02` — recuperación normativa aporta evidencia documental y no sustituye el ranking histórico;
- `C03` — LLM local explica el Top-3 recuperado y no clasifica desde cero;
- `C07` — solo como principio metodológico de agrupamiento/dependencia intra-DAM, sin inferencia de resultados.

Todo claim debe mantenerse dentro de su alcance autorizado.

### Contenido prohibido en B01

No incluir:

- resultados o métricas;
- cifras H100/DEV/EVAL;
- resultados EXP-11A, EXP-11B, EXP-12, EXP-12b o Grupo 3;
- tests, p-values, intervalos, efectos o conclusiones inferenciales;
- lenguaje causal no autorizado;
- `FINAL_GAP` o novelty final;
- afirmaciones de ausencia universal de prior art;
- accuracy global del RAG/sistema;
- corrección jurídica o clasificación legalmente vinculante;
- generalización empírica fuera del alcance evaluado;
- detalle de datasets/corpora/curación reservado a 3.2;
- detalle de particiones/leakage/near-duplicates reservado a 3.3;
- detalle algorítmico o hiperparámetros de retrieval reservado a 3.4–3.6;
- detalle de prompts/modelo LLM reservado a 3.7;
- detalle de métricas/protocolos de evaluación reservado a 3.8;
- análisis de drift/reproducibilidad reservado a 3.9;
- prosa de Results, Discussion, Introduction o Conclusions.

### Citación y fuentes

No fuerces literatura externa en esta subsección. Si B01 puede sustentarse íntegramente con las fuentes metodológicas gobernantes, mantén `CITATION_COMMENT_COVERAGE = 0/0`.

Si consideras indispensable una cita externa, debes cumplir MWDP-S01–S04 y MWDP-C01–C06: recuperar el full text en la sesión activa, verificar el pasaje exacto, no citar por memoria y añadir el comentario Word anclado a la cita. Si no puedes recuperar el full text, usa `ACCESS_RECHECK_REQUIRED` y no incorpores la cita.

### Estilo

- Texto de publicación: inglés académico natural, preciso y sobrio, compatible con KBS y transferible a ESWA/IPM.
- Evita lenguaje promocional, novelty implícita y redundancia.
- Una función científica principal por párrafo.
- La versión española es espejo semántico de control, no una reformulación más fuerte o extensa.
- Preserva exactamente la terminología congelada y las fronteras anti-overclaiming de MWDP_V1.0.

### Artefactos obligatorios de V01

Esta es la **primera inicialización** del master acumulativo; no existe un `ARTICLE_MASTER_V001` aprobado previo. Por ello la creación inicial del candidato no se considera reconstrucción prohibida, pero debe declararse explícitamente como `INITIAL_MASTER_CANDIDATE_INITIALIZATION`.

Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V01.md` — informe de ejecución, onboarding, checklist MWDP y resumen de archivos generados;
2. `article/sections/methods/Methods_B01_V01.md` — bloque independiente bilingüe, con Part I English y Part II Spanish semantic-control mirror;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md` — candidato acumulativo inicial bilingüe que contiene únicamente B01;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.docx` — Word acumulativo candidato bilingüe, editable, neutral/reversible y con APA 7 provisional cuando corresponda.

No crees `ARTICLE_MASTER_V001.*`: ese nombre queda reservado para una futura **integración aprobada por el autor**.

No modifiques `ARTICLE_STATUS.md`, `DECISIONS.md`, `CLAIM_EVIDENCE_MATRIX.md`, reviews, prompts, literatura congelada ni Plan Maestro.

### Word obligatorio

El `.docx` debe cumplir íntegramente MWDP_V1.0:

- Part I — English manuscript master;
- Part II — Spanish semantic-control mirror;
- estilos semánticos simples y layout neutral;
- sin columnas ni maquetación KBS supuesta;
- APA 7 solo como capa provisional;
- preservar editabilidad;
- comentarios de auditoría anclados a cada cita inglesa si existiera alguna;
- no usar Mendeley ni simular campos Mendeley.

### Checklist obligatorio al final de la respuesta

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = [SHAs realmente leídos]
AUTHORIZED_CLAIMS_USED = [...]
CONDITIONAL_CLAIMS_USED = NONE / [...]
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [...]
CITATION_COMMENT_COVERAGE = n/n
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md + .docx
MASTER_INITIALIZATION = INITIAL_MASTER_CANDIDATE_INITIALIZATION
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
DELIVERY_STATE = DRAFTING / AWAITING_INTERNAL_REVIEW
```

No declares el bloque `APPROVED` ni `FROZEN`.

---

## English

### Operating instruction

Act exclusively as the **Writing AI** for the scientific article in `elVladdi/gci-nandina-rag`, branch `article/main-manuscript`.

Execute **only `Methods B01 — Design, scope, and units`**. Do not advance to B02 or any other section.

Before drafting, fully read and apply the mandatory onboarding hierarchy listed in the Spanish section, including `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`) in full, the frozen 0D architecture/governance artifact, the 0A documentary and experimental ground truths, the Phase-1 Methods entry gate, the living `SRC-03`, and this prompt. Chat memory may not substitute for those sources.

### Authorized state

```text
PHASE_1 = OPENED
METHODS_B01 = READY_FOR_DRAFTING
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
MWDP_VERSION = MWDP_V1.0
TARGET_A = Knowledge-Based Systems
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT_AT_ENTRY
```

The living Master Plan contains later Group-3 progress that has not yet been editorially reconciled as article claims. Do **not** use those results in B01.

### Block objective and boundaries

Draft a publication-ready Methods 3.1 subsection defining only the overall study design, evaluated scope, system-function boundaries, and analysis/query/output/grouping units. Preserve the exact scientific architecture and anti-overclaiming boundaries described in the Spanish section and MWDP_V1.0.

Usable claims are limited to `C01`, `C02`, `C03`, and, when methodologically necessary, `C07` only as a grouping/dependence principle. Do not report results, metrics, experimental outcomes, statistical inference, causal effects, final gap/novelty, legal correctness, overall system accuracy, empirical generalization, or technical detail reserved for Methods 3.2–3.9.

Do not force external literature into B01. Any external citation must be re-retrieved and audited under MWDP source and Word-comment rules.

### Mandatory V01 artifacts

This is the declared first initialization of the cumulative master candidate; there is no prior approved `ARTICLE_MASTER_V001`. Generate only:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V01.md`;
2. `article/sections/methods/Methods_B01_V01.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.docx`.

Reserve `ARTICLE_MASTER_V001.*` for a later author-approved integration. Do not modify editorial-control files, frozen literature, or the experimental Master Plan.

The Word candidate must be bilingual (English publication master + Spanish semantic-control mirror), editable, neutral/reversible, provisionally APA 7 where applicable, and must contain citation-anchored audit comments for every English citation if any are used. Do not use or simulate Mendeley fields.

End with the exact MWDP delivery checklist specified in the Spanish section and set `DELIVERY_STATE = DRAFTING / AWAITING_INTERNAL_REVIEW`. Do not self-approve or freeze the block.
