# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.1
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-046
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_AUTHORIZED_BLOCK = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
ARCHITECTURE = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = REOPENED / AUTHORIZED / ACTIVE
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado completa esa base y solo se vuelve canónico después de auditoría de la IA Gestora, aprobación autoral cuando corresponda e integración técnica verificada.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, decisiones congeladas, literatura primaria verificada cuando corresponda y fuentes experimentales gobernantes para todo hecho empírico.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- Secuencia editorial: problema/posicionamiento → arquitectura general → instanciación experimental → resultados → interpretación.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de recuperación documental y generación.
- La recuperación documental/normativa aporta evidencia para candidatos ya fijados y no cambia su composición ni orden.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero ni retroalimenta la clasificación.
- El reranking LLM permanece diagnóstico salvo decisión expresa posterior.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de análisis; DAM/declaración es unidad de agrupamiento cuando existe dependencia.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es manuscript master inglés; Part II es espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, entradas, acciones, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

### Principio editorial específico de Methods

**Methods describe objetos científicos, procedencia, procedimientos, decisiones de diseño, ejecución, protocolos de evaluación y controles de validez. La identidad técnica exhaustiva de artefactos pertenece al repositorio/manifiestos de reproducibilidad salvo que un identificador concreto sea metodológicamente indispensable.**

Por tanto, la prosa principal no se organiza alrededor de SHA-256, rutas internas, nombres de scripts, nombres físicos de archivos o labels internos de configuración.

## 3. Estructura acumulativa

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion + Limitations
7. Conclusion
8. KBS end matter

La estructura detallada gobernante es `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, aprobada mediante D-045. V02 conserva la estructura previa excepto por la reestructuración controlada de Section 4.

### 3.1 Section 4 aprobada

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

## 4. Política del master acumulativo y DOCX

1. Cada bloque parte del último master aprobado e integrado.
2. Master Markdown canónico: `ARTICLE_MASTER_V009.md`, SHA-256 `ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28`, Git blob `40f20437458715c615fc1762f025ebcdbb3b6fc2`.
3. DOCX canónico correspondiente: `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`, custodia local efectiva del autor, SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, 40 comentarios heredados y 0 tracked changes en la última auditoría aprobada.
4. D-021/D-027 gobiernan custodia local binaria; D-035 gobierna handoff timeout-safe.
5. No se reconstruye DOCX desde Markdown.
6. No Base64 manual, chunking, recomposición ni workarounds de transferencia.
7. Los bloques nuevos preservan exactamente secciones/comentarios ya aprobados salvo alcance explícitamente reabierto.
8. El master candidato no se vuelve canónico hasta superar auditoría, aprobación e integración aplicables.
9. `ARTICLE_MASTER_V010` permanece suspendido/no materializado; la numeración V010 queda reservada para una futura integración aprobada derivada de la nueva B01, no para la prosa observada anterior.

## 5. Continuidad operativa de la IA Gestora

La IA Gestora continúa automáticamente cuando el siguiente paso es determinista y autorizado. Solo se detiene por decisión científica/editorial del autor, archivo exacto no disponible, dependencia bajo otra autoridad, contradicción irresuelta entre fuentes o evidencia insuficiente.

## 6. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Structure V02 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED; two editorial forward references reopened narrowly |
| Canonical master | `ARTICLE_MASTER_V009.md` |
| Experimental Design B01 revised | REOPENED / ACTIVE / AUTHORIZED |
| Section 4.3+ | NOT_AUTHORIZED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Los grupos experimentales no se administran aquí. `SRC-03` se consulta en modo de solo lectura cuando una afirmación o gate editorial depende materialmente de ellos.

## 7. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED; Section 4 amended by D-045 |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5A | Experimental Design B01 revised — two Section-3 forward-reference edits + 4.1 + 4.2.1–4.2.3 | **ACTIVE / AUTHORIZED** |
| 5B | 4.3 Documentary corpus and evidence resource | NOT_AUTHORIZED until 5A closes |
| 5C+ | 4.4–4.8 | atomic later gates |
| 6 | Results provisional | Experimental Design sufficiently stable + editorial gate + consumable evidence |
| 7 | Figures/visualizations | specific experimental/editorial control |
| 8 | Final Results | required evidence/visualizations closed |
| 9 | Discussion + Limitations | final Results + authorized literature contrast |
| 10 | Conclusion | Discussion closed |
| 11 | Abstract | complete manuscript |
| 12 | Title + Keywords | Abstract/manuscript complete |
| 13 | Transversal synchronization | according to live external dependencies |
| 14 | Scientific audit/freeze | after synchronization and required audits |
| 15 | Final KBS adaptation | scientific freeze + current submission requirements |

## 8. Concurrencia con el proceso experimental

Solo la IA Experimental administra el Plan Maestro experimental. La IA Gestora y la IA de Redacción consultan `SRC-03` en solo lectura.

D-034 mantiene:

```text
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
```

Último snapshot editorial registrado:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
DEVELOPMENT_MAIN = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

La ejecución de B01 debe comprobar cambios materiales del `SRC-03` vivo antes de redactar.

## 9. Fase activa — Experimental Design B01 revisada

### 9.1 Alcance autorizado

Solo:

- dos enmiendas editoriales de forward-reference en 3.5 y 3.7, sin modificar la arquitectura científica;
- 4.1 `Experimental setting and scope`;
- 4.2 `Historical data and experimental dataset construction`;
- 4.2.1 `Source and data collection`;
- 4.2.2 `Processing and curation`;
- 4.2.3 `Partition construction and dataset composition`.

No 4.3 ni posteriores.

### 9.2 Función narrativa

B01 debe explicar qué instanciación se evaluó, con qué recurso histórico, cómo se obtuvo el material administrativo, cómo se transformó/curó y cómo se construyeron las particiones experimentales. El experimento se presenta como evaluación offline de una arquitectura/procedimiento, no como herramienta operativa. `Evaluar` es la fuerza epistémica preferida.

La procedencia debe comenzar por la fuente administrativa y el acopio real. El Excel intermedio, nombres de hojas, nombres de scripts, rutas internas y hashes pueden permanecer en artefactos de reproducibilidad, pero no gobiernan la prosa publicable.

### 9.3 Ground truth y fuentes

Precedencia:

1. `SRC-03` + artefactos/commits congelados de desarrollo para estado experimental, datasets, particiones y hechos técnicos;
2. `SRC-02` (`Anexo_1_NANDINA_LLM_RAG_v13.docx`) para metodología operativa y procedimiento de fuente/recolección cuando no contradiga `SRC-03`;
3. `SRC-01` para problema/objetivos/hipótesis/alcance aprobados;
4. `SRC-04` solo para comparación/detección de discrepancias;
5. guía KBS-34 para nivel de detalle publicable.

Hechos relevantes ya identificados, sujetos a verificación directa en ejecución:

- fuente administrativa: consultas Aduanet/SUNAT para importación para el consumo, Aduana Marítima del Callao;
- periodo de declaraciones y criterios administrativos/temáticos definidos en `SRC-02`;
- acopio manual previo a normalización automatizada;
- intermedio reconstruido: 11,320 series / 107 DAM;
- Chapter 87 antes de curación: 4,232 registros;
- curados: 4,106;
- H100: 2,950 series / 28 DAM / 66 códigos representados;
- DEV: 100 / 6 / 9;
- EVAL: 1,056 / 67 / 42 códigos de referencia representados;
- v0.2 con asignaciones explícitas de DAM;
- cero solapamiento DAM y cero solapamiento del identificador de serie entre particiones;
- no afirmar que 66 códigos constituyen el universo completo de Chapter 87.

Los SHA, rutas, nombres físicos y labels internos pueden usarse para verificación, pero no deben trasladarse automáticamente a la prosa.

### 9.4 Claims y límites

C06 y C07 son relevantes y autorizados dentro de Methods/validity. C15 puede usarse solo como propiedad de diseño, no como evidencia de generalización. C16/C18 permanecen prohibidos. C19 solo si fuera imprescindible como snapshot histórico; C20 no usar. C21 se difiere preferentemente a 4.3/4.4/Limitations. No introducir C04/C05, HE2/HE5, EXP11/EXP12 ni resultados inferenciales en B01.

### 9.5 Transferencia y entregables

Patrón D-035:

- section MD pequeño: GitHub;
- response pequeña: GitHub;
- master Markdown acumulativo candidato: adjunto exacto al autor + SHA-256;
- DOCX acumulativo candidato: adjunto exacto al autor + SHA-256;
- sin transferencia grande redundante, Base64 manual, chunking o recomposición.

## 10. Ciclo obligatorio

```text
IA Gestora reconstruye estado/evidencia
→ abre/versiona bloque y prompt
→ IA de Redacción ejecuta solo el bloque
→ entrega artefactos y respuesta versionada
→ IA Gestora audita independientemente
→ corrección si corresponde
→ PASS
→ aprobación expresa del autor cuando aplique
→ IA Gestora integra/promueve técnicamente
→ continúa automáticamente hasta el siguiente gate real
```

## 11. Estado inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ONLY_NEW_B01_PROMPT_UNDER_STRUCTURE_V02
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
PREVIOUS_OBSERVED_B01_V02 = NOT_BASELINE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Purpose and binding frame

The article remains a cumulative KBS Research Article. The governing structure is `KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, author-approved under D-045. Related Work, Introduction, and the scientific Architecture are closed/integrated; canonical master remains V009. Experimental Design B01 has been reopened under D-046.

Methods must describe scientific objects, provenance, procedures, design choices, execution, evaluation protocols, and validity controls. Exhaustive artifact identity belongs in reproducibility manifests/resources unless indispensable to understanding the method.

## 2. Section-4 structure

Section 4 follows: 4.1 experimental setting/scope; 4.2 historical data and experimental-dataset construction with source/collection, processing/curation, and partition construction/composition; 4.3 documentary corpus/evidence resource; 4.4 partition validity/dependence controls; 4.5 experimental configuration/execution; 4.6 evaluation framework/protocols with three functional subsections; 4.7 statistical/robustness analysis; 4.8 reproducibility resources.

## 3. Active block

B01 is limited to two editorial Section-3 forward-reference amendments plus 4.1 and 4.2.1–4.2.3. Drafting must start from canonical V009 and its exact DOCX. The previously observed B01 V02 is not a baseline.

The experiment is an offline experimental evaluation of a concrete architecture instantiation, not an operational decision-support tool. Historical-data provenance begins with the administrative source and actual collection process. Internal paths, hashes, worksheet/script/file names are verification metadata, not the organizing principle of publication prose. `Evaluate` is preferred to `validate`; configurability is not empirical generalization.

## 4. Immediate gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
NEXT_ACTOR = DRAFTING_AI
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
