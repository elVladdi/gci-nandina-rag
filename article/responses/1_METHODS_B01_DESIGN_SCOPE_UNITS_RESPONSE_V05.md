# Fase 1 — Methods B01 — Informe de revisión V05 conforme a KBS-34

## Español

### 1. Onboarding y estado operativo

**ARCHIVOS LEÍDOS:** onboarding completo de `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`, íntegro); `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`; `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`; `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md` completo; `article/literature/KBS_34_ARTICLE_EDITORIAL_PATTERN_MATRIX.md` completo; `article/reviews/1_METHODS_B01_KBS_EDITORIAL_REAUDIT_V03.md`; `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V03.md`; `article/sections/methods/Methods_B01_V03.md`; `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md`; `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md`; el `SRC-03` vivo; y `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V05.md`.

**FASE ACTIVA:** `PHASE_1 = OPENED`.

**ESTADO DEL BLOQUE ASIGNADO:** `METHODS_B01 = REVISION_REQUIRED`.

**REDACCIÓN AUTORIZADA:** SÍ, exclusivamente para V05 de `Methods B01 — Design, scope, and units`. El prompt V04 no se ejecutó y quedó supersedido antes de ejecución por D-013, la reauditoría KBS de V03 y el prompt V05.

**DECISIONES CONGELADAS RELEVANTES:** recuperación histórica como generador/ranking de candidatos; Top-3 histórico fijado antes de la recuperación normativa; recuperación normativa como evidencia documental sin reranking; LLM local posterior como generador de explicación controlada sin feedback al ranking; evaluación por función; SERIE como unidad de análisis; DAM como unidad de agrupamiento cuando la dependencia sea metodológicamente relevante; apoyo a decisión no vinculante; revisión experta fuera del flujo automatizado; `CONFIGURABILITY / REPLICABILITY ≠ EMPIRICAL GENERALIZATION`; `MWDP_V1.0`, `SPCCR_V1.0` y `KBS_EWG_34_V01` como controles vigentes de redacción.

**CLAIMS AUTORIZADOS RELEVANTES:** `C01`, `C02`, `C03`, `C07`, `C15`.

**CLAIMS CONDICIONALES USADOS:** ninguno.

**CLAIMS PROHIBIDOS O PENDIENTES USADOS:** ninguno.

**FUENTES EXTERNAS QUE DEBEN VERIFICARSE:** ninguna. Los 34 artículos KBS se utilizaron solo como evidencia editorial de la guía aprobada y no se citan como fuentes científicas en B01.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** `ARTICLE_STATUS.md` conserva el gate previo de V04, pero D-013, la reauditoría KBS V03 y el prompt V05 son posteriores y específicos, dejan V04 supersedido y autorizan V05. No se modificó `ARTICLE_STATUS.md`. El `SRC-03` vivo avanzó a `GROUP3 = IN_PROGRESS`, con G3-F01–G3-F03 cerradas y G3-F04 todavía no autorizada; este cambio no afecta el contenido de B01 porque V05 no consume resultados ni inferencias de Grupo 3 y los principios arquitectónicos relevantes permanecen sin cambio.

### 2. Correcciones ejecutadas

- **B01-M09 — ADDRESSED.** Se regeneró el master Word como paquete DOCX/OOXML válido y se sometió a QA estructural, de render y de equivalencia visible.
- **B01-M10 — ADDRESSED.** La vista inicial conserva el flujo general, pero limita las invariantes a Top-3 fijado antes de evidencia normativa, evidencia sin reranking y LLM posterior sin feedback al ranking. La enumeración exhaustiva de restricciones finas no se repite en 3.1.
- **B01-M11 — ADDRESSED.** La prosa describe entradas, operaciones y salidas antes de sintetizar una única vez el `functional contract`. Se eliminaron formulaciones como `fixed sequence of responsibilities` y se redujo el tono contractual.
- **B01-M12 — ADDRESSED.** La configurabilidad se expresa con precondiciones concretas: recurso histórico etiquetado alineado con un universo de clases definido, corpus documental/normativo compatible con el mecanismo de recuperación e interfaces coherentes de representación/identificación. Se mantiene explícitamente la frontera entre configurabilidad/replicabilidad y generalización empírica.
- **B01-M13 — ADDRESSED.** NANDINA Chapter 87 aparece después del método general como la instancia experimental evaluada, y la evidencia se delimita al piloto offline y a las versiones específicas de datos, corpus y configuración utilizadas.

### 3. Alcance científico preservado

V05 conserva el alcance científico validado de V03. La recuperación histórica genera y ordena candidatos; el Top-3 queda fijado antes de la recuperación normativa; la recuperación normativa aporta evidencia sin alterar el orden; y el LLM local opera downstream para generar una explicación sin retroalimentar el ranking. Ranking, evidencia y explicación permanecen como funciones diferenciadas.

Se preservan además el carácter aplicado y offline del piloto, el apoyo a decisión no vinculante, la revisión experta fuera del flujo automatizado, SERIE como unidad de observación/análisis, DAM como unidad de agrupamiento cuando corresponde por dependencia, la descripción comercial normalizada como representación de consulta y el Top-k/Top-3 histórico fijo como salida pertinente para las etapas posteriores.

No se introdujeron resultados, métricas, inferencias estadísticas, causalidad, novelty final, superioridad, literatura externa, EXP-11B, resultados de Grupo 3, corrección jurídica ni contenido técnico reservado a B02–B09.

### 4. Artefactos V05

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V05.md`;
2. `article/sections/methods/Methods_B01_V05.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.docx`.

No se generó V04, no se creó `ARTICLE_MASTER_V001.*`, no se avanzó a B02 y no se modificó ninguna otra sección o archivo de gobernanza.

### 5. QA editorial y técnico

La revisión de prosa confirmó relaciones explícitas input–operación–output, baja a moderada densidad de abstracción y ausencia de sobrecarga de lenguaje contractual. La equivalencia semántica EN–ES conserva funciones, precondiciones, límites, unidades y fuerza epistémica.

El Word se verificó como paquete OOXML válido; contiene `word/document.xml`, no contiene comentarios ni tracked changes, renderiza correctamente y su texto visible reproduce el master Markdown V05.

---

## English

### 1. Onboarding and operational state

**FILES READ:** complete onboarding plus `MWDP_V1.0`, `STYLE_GUIDE`, `SPCCR_V1.0`, D-013, the complete approved substantive content of `KBS_EWG_34_V01`, the complete KBS-34 editorial matrix, the KBS-specific V03 reaudit, the V03 internal review, the V03 block/master/response, living `SRC-03`, and the closed V05 prompt.

**ACTIVE PHASE:** `PHASE_1 = OPENED`.

**ASSIGNED BLOCK STATE:** `METHODS_B01 = REVISION_REQUIRED`.

**DRAFTING AUTHORIZED:** YES, exclusively for Methods B01 V05. V04 was not executed and was superseded before execution by D-013, the KBS V03 reaudit, and the V05 prompt.

**RELEVANT FROZEN DECISIONS:** historical retrieval generates/ranks candidates; historical Top-3 is fixed before normative retrieval; normative retrieval provides documentary evidence without reranking; the downstream local LLM generates a controlled explanation without feeding content back into ranking; evaluation is function-specific; SERIES is the analysis unit; DAM is the grouping unit when dependence is methodologically relevant; decision support is non-binding; expert review remains outside the automated workflow; `CONFIGURABILITY / REPLICABILITY ≠ EMPIRICAL GENERALIZATION`; `MWDP_V1.0`, `SPCCR_V1.0`, and `KBS_EWG_34_V01` govern drafting.

**AUTHORIZED CLAIMS:** `C01`, `C02`, `C03`, `C07`, `C15`. No conditional or prohibited claim was used.

**EXTERNAL SOURCES REQUIRING VERIFICATION:** none. The 34 KBS articles serve only as editorial evidence for the approved guide and are not cited as scientific sources in B01.

**BLOCKERS OR CONTRADICTIONS:** `ARTICLE_STATUS.md` still carries the prior V04 gate, whereas later and more specific D-013, the KBS V03 reaudit, and the V05 prompt supersede V04 and authorize V05. `ARTICLE_STATUS.md` was not modified. Living `SRC-03` has advanced to Group 3 in progress, with G3-F01–G3-F03 closed and G3-F04 not yet authorized; this does not affect B01 because V05 consumes no Group-3 result or inference and the relevant frozen architectural principles remain unchanged.

### 2. Corrections implemented

- **B01-M09 — ADDRESSED:** the candidate Word master was regenerated as a valid DOCX/OOXML package and subjected to structural, render, and visible-text QA.
- **B01-M10 — ADDRESSED:** the opening overview retains only the central invariants needed in 3.1 and avoids reproducing the detailed LLM restriction list reserved for later subsections.
- **B01-M11 — ADDRESSED:** observable inputs, operations, and outputs precede the single synthesis using `functional contract`; governance-like wording was removed.
- **B01-M12 — ADDRESSED:** configurability is stated with bounded prerequisites for the labeled historical resource, target class universe, compatible documentary/normative corpus, and coherent representation/identifier interfaces. No automatic interoperability or empirical transfer is implied.
- **B01-M13 — ADDRESSED:** NANDINA Chapter 87 follows the general method as the evaluated experimental instance, with empirical evidence bounded to the offline pilot and the specific data/corpus/configuration versions used in that pilot.

### 3. Preserved scientific scope

V05 preserves V03's validated scientific scope and the authorized claim set. Historical retrieval ranks candidates and fixes the Top-3; normative retrieval documents those fixed candidates without reranking; the downstream local LLM generates an explanation without feeding generated content back to ranking; and ranking, evidence, and explanation remain distinct functions.

The applied offline pilot, non-binding decision-support role, expert review outside the automated flow, SERIES/DAM units, normalized commercial-description query representation, and historical Top-k/fixed-Top-3 outputs are preserved. No results, metrics, statistical inference, causal claim, final novelty, superiority, external literature, EXP-11B, Group-3 result, legal-correctness claim, or B02–B09 technical detail was introduced.

### 4. V05 artifacts

Exactly four V05 artifacts were produced: the bilingual response, standalone B01 V05 Markdown, candidate master V05 Markdown, and candidate master V05 DOCX. No V04 artifact, canonical approved master, B02 content, or governance modification was created.

### 5. Editorial and technical QA

Prose QA confirms explicit input–operation–output relations, low-to-moderate abstraction density, and no contract-language overload. EN–ES semantic equivalence preserves functions, prerequisites, limits, units, and epistemic strength.

The Word candidate is a valid OOXML package with `word/document.xml`, zero comments, zero tracked changes, successful rendering, and visible-text equivalence with the V05 Markdown master.

---

## Checklist / Lista de control

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
GUIDE_APPROVAL = D-013
BLOCK = Methods_B01
BLOCK_REVISION = V05
V04_STATUS = NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION
B01_M09 = ADDRESSED
B01_M10 = ADDRESSED
B01_M11 = ADDRESSED
B01_M12 = ADDRESSED
B01_M13 = ADDRESSED
SCIENTIFIC_CONTENT_SCOPE_FROM_V03 = PRESERVED
SOURCE_SNAPSHOT(S) = [article/main-manuscript@1e729cd4ade1fbee59f1e31762001886eb68aca7; START_HERE=e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be; README=8b11aed826d8c4985814f62e61a6554b8d77fa4a; ARTICLE_STATUS=b2686c9e40d1e1c08aa95fb6d82108bf582111d3; ARTICLE_WRITING_PLAN=e69da61e52d8dbb4c74f6e4a210ec5d06387e767; DECISIONS=895992ce2c13819b7ebeb69234d118654a714dea; SOURCE_REGISTRY=d32fa718933b97c0a1b95ff528b1cbd74cc7f44c; CLAIM_EVIDENCE_MATRIX=ceaa754ef0012862f4952b378dd4a12dfb6e33f7; STYLE_GUIDE=cac5c562a30da80db61da7a335381f21741f2d69; MWDP=34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e; SPCCR=0b48c86adc612077b98db82713f1a2af4e1e3231; D013=f1e53bb239eab5855a16af6212e22c063e541252; KBS_EWG_34_V01=bf62f84b176998b2801ee7be5da780aee5d84727; KBS_34_EPM_V01=da48ff92760856fd87aa78abb013118510b9f4dc; B01_KBS_REAUDIT_V03=1873504572881fe9f6c8ad1fb56930fd6a92e9a6; B01_INTERNAL_REVIEW_V03=23a7ebc5816cbb689421581cc024097ac7526d17; Methods_B01_V03=9e1e080ebceb17b60cb664162627dac57136939f; ARTICLE_MASTER_CANDIDATE_V03_MD=675611395176a311c1ccf61d1d2eb58693ddb822; B01_RESPONSE_V03=ce0b87b3a76db614360bae26ed2a20a4d33403ae; V05_PROMPT=92b334a9358058cb245d283b248a61d9f902a0a8; SRC03_HEAD=96cccb9a61f42ab97b1eba607524e33f992740f6; SRC03_BLOB=d3537bb07223e3fdeb074913d762179aec7d3c52]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
GENERAL_METHOD_FIRST = PASS
NANDINA_AS_TESTBED_SECOND = PASS
INPUT_OPERATION_OUTPUT_CLARITY = PASS
ABSTRACTION_DENSITY = LOW_TO_MODERATE
CONTRACT_LANGUAGE_OVERLOAD = ABSENT
CONFIGURABILITY_PRECONDITIONS = EXPLICIT_BOUNDED
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
DOCX_SHA256 = f4762115471246592ffe406f4ef9c18dc3140d034a55b628302292b0e4627355
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 352
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```
