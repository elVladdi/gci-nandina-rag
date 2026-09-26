# Experimental Design B02 / Section 4.3 — ground-truth review V01

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_B02_SECTION4_3_GROUND_TRUTH_REVIEW_V01
DATE = 2026-09-26
ROLE = IA_GESTORA / INDEPENDENT_GROUND_TRUTH_RECONSTRUCTION
PARENT_DECISION = D-050
CANONICAL_MASTER = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
TARGET_SECTION = 4.3 Documentary corpus and evidence resource
STATUS = PASS_FOR_ATOMIC_DRAFTING_GATE
```

## 1. Objeto de la revisión

Reconstruir, antes de abrir la redacción de Section 4.3, qué recurso documental/normativo fue realmente consumido por la ruta experimental integrada que alimentó la evidencia específica por candidato y la explicación posterior. La revisión separa deliberadamente: (a) el diseño arquitectónico genérico de Section 3; (b) la instanciación experimental primaria; (c) experimentos/correcciones posteriores de sensibilidad normativa.

La revisión no autoriza Results, no redefine Architecture y no interpreta asociación documental como corrección jurídica.

## 2. Fuentes primarias verificadas

### 2.1 Configuración de integración histórica–normativa

`src/configs/historical_normative_integration_v0.2.json` establece que:

- el ranking histórico es la única fuente del ranking y se congela en Top-3 antes de la etapa documental;
- el corpus normativo consumido por la integración primaria es el corpus NANDINA jerárquico congelado en Phase C;
- la operación documental es `CODE_TO_NORMATIVE_EVIDENCE_LOOKUP`;
- cada código NANDINA-8 del Top-3 histórico congelado se busca directamente en el corpus jerárquico;
- no se usa la etiqueta de evaluación, la consulta comercial, pools alternativos ni D1A para seleccionar evidencia;
- no existe fallback que sustituya un candidato sin evidencia exacta;
- la etapa documental no reranquea, no fusiona scores, no inserta candidatos y no usa un LLM.

### 2.2 Configuración y construcción de la explicación

`src/configs/he4_pre_explainer_v0.2.json`, `src/experiments/build_llm_explanation_top3_sample.py` y `src/experiments/build_llm_explanation_top3_audit_sample.py` confirman que la explicación posterior recibe el mismo corpus NANDINA jerárquico. Los constructores indexan el corpus por código NANDINA-8 y, para cada candidato del Top-3 fijo, asocian el registro exacto del código. Si no existe registro exacto, se conserva una advertencia; no se sustituye el candidato por otro código.

El payload documental puede incluir descripción NANDINA, contexto jerárquico de sección/capítulo/partida/subpartida y metadatos de procedencia textual. El contexto parental sirve para contextualizar el código exacto y no debe presentarse como evidencia exacta de una subpartida distinta.

### 2.3 Construcción del corpus jerárquico

`src/corpus/build_hierarchical_nandina_corpus.py` construye un registro por código NANDINA válido de ocho dígitos y conserva, cuando están disponibles:

- sección y título;
- capítulo y título;
- partida de cuatro dígitos y descripción;
- subpartida HS de seis dígitos y descripción;
- código NANDINA de ocho dígitos y descripción;
- unidad física;
- página/línea/texto fuente;
- una representación textual jerárquica para indexación/contexto.

La preparación limpia encabezados y espacios y evita repetir texto jerárquico redundante. La ausencia de un nivel parental no se rellena inventando contenido.

`data/processed/corpus/nandina/summary.csv` registra para el corpus derivado de la fuente congelada 1,020 partidas de cuatro dígitos, 1,117 registros HS-6 y 7,648 registros NANDINA-8. Estos conteos son caracterización del recurso, no métricas de desempeño; pueden usarse solo si aportan valor metodológico real.

### 2.4 Fuente documental, autoridad y versión temporal

`data/processed/corpus/nandina/run_metadata.json` identifica como fuente primaria procesada la **Decisión 885 de la Comisión de la Comunidad Andina — NANDINA, Gaceta Oficial del Acuerdo de Cartagena 4359**, procesada desde PDF.

La verificación independiente de fuente oficial confirma:

- la Decisión 885 aprobó la NANDINA y entró en vigencia el **1 de enero de 2022**;
- la Decisión 906, publicada en la Gaceta Oficial 5062 del **25 de octubre de 2022**, modificó la NANDINA aprobada mediante la Decisión 885;
- la Decisión 906 entró en vigencia el **1 de enero de 2023**;
- la propia Comunidad Andina describe la Decisión 906 como actualización de codificación, descripción y notas complementarias para determinadas subpartidas.

Fuentes oficiales verificadas por la IA Gestora:

- Comunidad Andina / GOAC 5062: `https://www.comunidadandina.org/DocOficialesFiles/Gacetas/GACETA%205062.pdf`;
- Tribunal de Justicia de la Comunidad Andina, Proceso 02-IP-2023: confirma que la Decisión 885 fue publicada en GOAC 4359 el 21-10-2021 y derogó la Decisión 812;
- Comunidad Andina, nota oficial del 25-10-2022 sobre aprobación de la Decisión 906.

## 3. Distinción crítica: arquitectura genérica vs. instanciación ejecutada

Section 3 define una arquitectura configurable en la que una etapa documental puede recuperar evidencia específica para cada candidato fijo. Esa descripción arquitectónica **no obliga** a que toda instanciación use BM25, búsqueda semántica o búsqueda por texto libre.

En la instanciación primaria que alimentó Phase F/HE4, la evidencia documental se asoció mediante **lookup exacto del código NANDINA-8 ya fijado por el ranking histórico**. Por tanto, Section 4.3 debe describir esta operación concreta como asociación/lookup de evidencia por código, y no como una búsqueda BM25 de la descripción comercial sobre el corpus normativo.

Esta precisión no contradice Architecture: es una decisión de configuración de la instanciación experimental.

## 4. Alcance del corpus y alcance empírico

El corpus jerárquico congelado representa la nomenclatura NANDINA de la fuente procesada, no solo Chapter 87. Sin embargo, en la evaluación primaria los códigos consultados en él provienen del Top-3 generado por el banco histórico del escenario Chapter 87. Deben mantenerse separadas estas dos dimensiones:

```text
CORPUS_DOCUMENTARY_SCOPE = NANDINA_HIERARCHY_FROM_FROZEN_SOURCE
EMPIRICAL_CANDIDATE_SCOPE = CHAPTER_87_INSTANCE
```

No debe inferirse desempeño fuera de Chapter 87 por el hecho de que el recurso documental tenga cobertura más amplia.

## 5. Deriva normativa y tratamiento correcto de Decision 906

Existe una frontera temporal material: los casos administrativos del experimento corresponden a 2026, mientras que el corpus congelado que alimentó la integración primaria y HE4 deriva de Decision 885 y no incorpora retroactivamente Decision 906.

Por tanto:

```text
DECISION_885_EFFECTIVE = 2022-01-01
DECISION_906_MODIFIES_885_EFFECTIVE = 2023-01-01
PRIMARY_PHASE_F_HE4_CORPUS = DECISION_885_DERIVED / FROZEN
PRIMARY_PHASE_F_HE4_CORPUS_RETROACTIVELY_REPLACED_BY_906 = false
TEMPORAL_VERSION_MISMATCH_RELATIVE_TO_2026_CASES = DISCLOSE
```

El repositorio contiene una línea correctiva posterior con corpus actualizado por Decision 906 y comparaciones controladas. El Plan Maestro registra que esa corrección tuvo impacto cuantitativo acotado y que no exigió reejecutar downstream. **Eso no autoriza a reescribir la historia experimental como si HE4 hubiera usado Decision 906.**

En Section 4.3 debe informarse la versión efectivamente usada y su frontera temporal. Los efectos cuantitativos de la corrección pertenecen a Results/robustness y no deben anticiparse aquí.

## 6. Recursos que no deben atribuirse al contexto primario de HE4 sin evidencia adicional

El repositorio contiene otros recursos documentales, entre ellos Arancel de Aduanas 2022, resoluciones de clasificación y corpora experimentales más amplios. La configuración primaria de integración y HE4 verificada para este gate no demuestra que esos recursos hayan alimentado el contexto final de explicación.

Por tanto:

```text
ARANCEL_2022_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
CLASSIFICATION_RESOLUTIONS_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
BROADER_CORPUS_RAG_FAMILY_AS_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
```

Pueden mencionarse en otros bloques solo si una fuente primaria de ejecución autoriza esa función concreta.

## 7. Claims y límites epistémicos

Autorizado para Section 4.3:

- identificar autoridad, fuente y versión temporal del recurso documental efectivamente usado;
- describir la preparación jerárquica del corpus;
- describir el lookup exacto por código NANDINA-8 para los candidatos fijos;
- indicar que la etapa documental no altera composición ni orden del Top-3;
- explicar que la evidencia/contexto jerárquico se entrega downstream para explicación controlada;
- declarar explícitamente la desalineación temporal Decision 885 / Decision 906 respecto de los casos 2026;
- mantener configurabilidad como propiedad de arquitectura, no como generalización empírica.

Prohibido:

- `NORMATIVE_ASSOCIATION => SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY => LEGAL_CORRECTNESS`;
- afirmar que el corpus congelado estaba normativamente actualizado a 2026;
- afirmar que Decision 906 alimentó HE4/Phase F si solo intervino en la línea correctiva posterior;
- describir el lookup primario como BM25/query-based retrieval;
- introducir métricas/resultados de Decision 906, HE4, retrieval o robustez;
- presentar Arancel 2022, resoluciones u otros corpora como contexto de HE4 sin prueba de consumo;
- declarar novelty, FINAL_GAP o superioridad.

## 8. Nivel de detalle KBS

La prosa publicable debe explicar el objeto científico y el procedimiento, no inventariar el repositorio. Rutas, hashes, nombres físicos de archivos/configuraciones y labels internos se usan para auditoría y reproducibilidad, pero no deben gobernar Section 4.3.

La redacción esperada es compacta: fuente/autoridad/temporalidad → preparación/representación jerárquica → asociación exacta por código y fronteras funcionales → limitación temporal explícita.

## 9. Dictamen

```text
GROUND_TRUTH_COHERENCE = PASS
PRIMARY_EVIDENCE_RESOURCE_IDENTIFIED = YES
PRIMARY_EVIDENCE_ASSOCIATION_IDENTIFIED = EXACT_NANDINA8_CODE_LOOKUP
RERANKING_IN_DOCUMENTARY_STAGE = NO
TEMPORAL_BOUNDARY_IDENTIFIED = YES
DECISION_906_CORRECTIVE_LINE_DISTINGUISHED = YES
PRIMARY_HE4_CONTEXT_SCOPE = SUFFICIENTLY_IDENTIFIED
SECTION_4_3_ATOMIC_DRAFTING = ELIGIBLE
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
