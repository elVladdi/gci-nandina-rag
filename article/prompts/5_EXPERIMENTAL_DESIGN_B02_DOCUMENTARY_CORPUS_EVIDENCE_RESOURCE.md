# Experimental Design B02 — Section 4.3 Documentary corpus and evidence resource

## 1. Identidad del bloque

```text
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
GOVERNING_DECISION = article/governance/D051_EXPERIMENTAL_DESIGN_B02_SECTION4_3_OPENING.md
PARENT_DECISION = D-050
GROUND_TRUTH_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B02_SECTION4_3_GROUND_TRUTH_REVIEW_V01.md
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
BASELINE_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
INHERITED_CITATION_COMMENTS = 40
AUTHORIZED_SCOPE = SECTION_4_3_ONLY_ENGLISH_PLUS_SPANISH_SEMANTIC_MIRROR
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente este bloque. No avances a 4.4 ni a ningún bloque posterior.

## 2. Rol

Actúa exclusivamente como **IA de Redacción científica** subordinada a la gobernanza del artículo. No eres IA Gestora ni IA Experimental.

No puedes:

- modificar el Plan Maestro experimental;
- redefinir Architecture;
- reabrir B01;
- promover un master;
- autoasignar `APPROVED`, `FROZEN`, `CLOSED` o `INTEGRATED`;
- abrir 4.4+;
- redactar Results/Discussion/Conclusion;
- declarar FINAL_GAP o novelty.

## 3. Objetivo único

Redactar **Section 4.3 Documentary corpus and evidence resource** y su espejo semántico en español, explicando con precisión:

1. cuál fue la fuente documental efectivamente usada por la instanciación experimental primaria;
2. su autoridad y frontera temporal;
3. cómo se preparó y representó jerárquicamente el recurso;
4. cómo se asoció evidencia documental a cada candidato del Top-3 fijo;
5. qué restricciones preservaron el ranking histórico;
6. qué limitación de versionado existe frente a Decision 906 y el periodo 2026.

La sección debe explicar el procedimiento científico ejecutado, no inventariar archivos del repositorio.

## 4. Onboarding obligatorio y precedencia

Antes de redactar, confirma repo `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`, y lee íntegramente:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
6. `article/governance/D050_EXPERIMENTAL_DESIGN_B01_V010_INTEGRATION.md`;
7. `article/governance/D051_EXPERIMENTAL_DESIGN_B02_SECTION4_3_OPENING.md`;
8. `article/reviews/5_EXPERIMENTAL_DESIGN_B02_SECTION4_3_GROUND_TRUTH_REVIEW_V01.md`;
9. `article/SOURCE_REGISTRY.md`;
10. `article/CLAIM_REGISTRY.md`;
11. `article/CLAIM_EVIDENCE_MATRIX.md` cuando una formulación requiera comprobar fuerza epistémica;
12. `article/STYLE_GUIDE.md`;
13. `article/manuscript/ARTICLE_MASTER_V010.md` y verifica el Git blob esperado;
14. el DOCX baseline exacto `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx` y verifica su SHA-256.

Decisiones activas relevantes: D-021, D-022, D-023, D-027, D-034, D-035, D-045, D-048, D-050 y D-051.

D-051 y su ground-truth review gobiernan los hechos específicos de B02 si un archivo administrativo anterior del artículo conserva un snapshot editorial desactualizado.

Si el DOCX baseline no está disponible o su SHA no coincide, detente con:

`EXPERIMENTAL_DESIGN_B02_BASELINE_DOCX_MISMATCH`

No reconstruyas el DOCX desde Markdown.

## 5. Fuentes experimentales/técnicas requeridas

Verifica directamente en el repositorio de desarrollo las siguientes fuentes antes de escribir una afirmación técnica:

- `src/configs/historical_normative_integration_v0.2.json`;
- `src/configs/he4_pre_explainer_v0.2.json`;
- `src/corpus/build_hierarchical_nandina_corpus.py`;
- `data/processed/corpus/nandina/run_metadata.json`;
- `data/processed/corpus/nandina/summary.csv`;
- `src/experiments/build_llm_explanation_top3_sample.py`;
- `src/experiments/build_llm_explanation_top3_audit_sample.py`;
- cualquier artefacto adicional estrictamente necesario para resolver una duda puntual, sin ampliar el alcance del bloque.

Lee también el `SRC-03` vivo:

```text
BRANCH = docs/plan-maestro-temporal-2026-08-31
PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Solo para verificar que no exista una decisión experimental posterior que invalide materialmente el ground truth congelado por D-051. Si encuentras una contradicción material, **no la reconcilies por inferencia**; detente con:

`EXPERIMENTAL_DESIGN_B02_MATERIAL_SOURCE_CONTRADICTION`

## 6. Búsqueda externa y bibliografía

```text
NEW_SCIENTIFIC_LITERATURE_SEARCH = NOT_AUTHORIZED
GENERAL_WEB_SEARCH = NOT_REQUIRED
NEW_SCIENTIFIC_REFERENCES = NOT_AUTHORIZED
```

D-051 ya congela la autoridad y fechas normativas verificadas por la IA Gestora. Puedes comprobar fuentes oficiales primarias solo si tu entorno ya ofrece acceso directo y sin ampliar la tarea, pero no sustituyas el hecho experimental de qué versión fue consumida.

No agregues entradas nuevas a la bibliografía general en este bloque. Las Decisiones 885 y 906 pueden identificarse textualmente como instrumentos oficiales dentro de Methods; su normalización bibliográfica final queda para el gate correspondiente.

## 7. Ground truth obligatorio

### 7.1 Recurso primario que alimentó la explicación

La ruta primaria integrada de Phase F/HE4 consumió un **corpus NANDINA jerárquico derivado de la Decisión 885 de la Comisión de la Comunidad Andina**.

No describas este recurso como un “Peruvian normative corpus” si esa frase sugiere que su autoridad primaria es una norma nacional peruana. La fuente del recurso verificado es supranacional andina. El escenario experimental sí tiene contexto administrativo peruano por sus datos históricos, pero esa dimensión no cambia la autoridad del corpus documental aquí descrito.

No atribuyas al contexto primario de HE4 el Arancel de Aduanas 2022, resoluciones de clasificación ni corpora RAG más amplios: su consumo no está establecido por las fuentes primarias de este gate.

### 7.2 Cobertura y estructura

El corpus procesa la nomenclatura de la fuente NANDINA congelada y no está recortado conceptualmente a Chapter 87. La instanciación experimental, sin embargo, consulta códigos producidos por el Top-3 histórico del escenario Chapter 87.

La representación jerárquica conserva, cuando existe:

- sección;
- capítulo;
- partida de cuatro dígitos;
- subpartida HS de seis dígitos;
- subpartida NANDINA de ocho dígitos;
- descripciones asociadas;
- unidad física;
- procedencia textual de la fuente.

Puedes incluir los conteos verificados del corpus —1,020 partidas de cuatro dígitos, 1,117 registros HS-6 y 7,648 registros NANDINA-8— **solo si** aportan valor metodológico y no hacen la sección innecesariamente inventarial. No son métricas de desempeño.

### 7.3 Operación documental ejecutada

Este punto es crítico:

```text
PRIMARY_EVIDENCE_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_IN_PRIMARY_PHASE_F = false
DOCUMENTARY_STAGE_RERANKING = false
CANDIDATE_INSERTION = false
CANDIDATE_SUBSTITUTION = false
FALLBACK_TO_OTHER_CODE = false
```

Para cada candidato del Top-3 ya fijado por el ranking histórico, la ruta primaria usa el **código NANDINA-8 del candidato** para localizar su registro exacto en el corpus jerárquico.

No describas esa configuración como:

- BM25 sobre la descripción comercial;
- búsqueda semántica de la consulta sobre el corpus;
- reranking normativo;
- fusión de scores histórico/normativo;
- clasificación normativa independiente.

La palabra arquitectónica genérica `retrieval` puede mantenerse al referirse al framework de Section 3, pero al describir **esta instanciación** debes especificar que la operación implementada fue un lookup exacto por código.

Si no existe evidencia exacta para un código, la lógica verificada no debe presentarse como sustitución automática por otra subpartida.

### 7.4 Contexto jerárquico vs. evidencia exacta

Los niveles parentales pueden contextualizar un candidato, pero no deben confundirse con una coincidencia exacta de la subpartida de ocho dígitos.

No conviertas un texto de capítulo/partida/HS-6 en evidencia exacta NANDINA-8 si el registro exacto no existe.

### 7.5 Autoridad y temporalidad

Debes identificar de forma clara y breve:

- **Decision 885**, Comisión de la Comunidad Andina, aprobó la NANDINA usada como fuente del recurso congelado y entró en vigencia el **1 January 2022**;
- **Decision 906** modificó Decision 885, fue publicada en GOAC 5062 el **25 October 2022** y entró en vigencia el **1 January 2023**;
- la ruta primaria de Phase F/HE4 mantuvo el corpus derivado de Decision 885;
- los casos administrativos evaluados corresponden al escenario 2026 ya definido en B01.

Por tanto, debes revelar una **version/temporal-boundary limitation**: el recurso documental congelado de la ruta primaria no incorpora retroactivamente las modificaciones de Decision 906.

No extrapoles esta observación a una afirmación más fuerte como “all Chapter-87 evidence was obsolete/incorrect”. D-051 establece un desajuste de versión temporal; no demuestra que Decision 906 haya cambiado cada código Chapter 87 consumido.

No escribas resultados cuantitativos de la corrección Decision 906. La línea correctiva posterior pertenece a robustness/Results.

## 8. Función narrativa esperada de Section 4.3

Construye una sección compacta —preferentemente 2 a 4 párrafos, salvo necesidad justificada— con esta lógica:

1. **Fuente y autoridad**: qué documento oficial alimentó el recurso y qué representa.
2. **Preparación y representación**: cómo se estructuró jerárquicamente la nomenclatura para asociar evidencia identificable.
3. **Uso experimental**: lookup exacto por código para cada candidato fijo; evidencia/contexto downstream; sin reranking ni sustitución.
4. **Frontera temporal**: Decision 906 modificó Decision 885 antes del escenario 2026; el experimento primario conservó el snapshot Decision-885-derived y esa condición limita la vigencia documental de la evidencia usada.

No repitas la explicación completa de Architecture 3.1–3.7. Section 4.3 responde **cómo se instanció** la capa documental en el experimento.

## 9. Reglas de prosa KBS

1. Prosa científica directa, concreta y observable.
2. No gobernanza/contratos internos en el manuscript.
3. No SHA-256 en el cuerpo ni en tablas publicables.
4. No rutas internas de repositorio.
5. No nombres físicos de JSON/JSONL/config/scripts.
6. No labels `Phase F`, `HE4`, `v0.2`, etc. en la prosa publicable salvo que sean imprescindibles para una referencia cruzada; en principio no lo son.
7. No inventario de archivos/índices.
8. No abstracciones como “normative intelligence layer” si puede explicarse la operación concreta.
9. No afirmar legal correctness, normative correctness sustantiva ni decisión jurídica final.
10. No afirmar que la evidencia documental participa en el ranking histórico.
11. No afirmar que el LLM modifica candidatos.
12. No generalizar desempeño fuera de Chapter 87.
13. No anticipar resultados, métricas, hipótesis o robustez.
14. No convertir la limitación temporal en una conclusión de invalidez general.
15. Mantener `evaluate/evaluación`, no elevar la fuerza epistémica a `validate/validated` sin criterio explícito.

## 10. Correspondencia English ↔ Spanish

Part I English es el texto científico principal. Part II Spanish es espejo de control semántico.

Ambas versiones deben conservar exactamente:

- fuente/autoridad;
- naturaleza jerárquica del corpus;
- lookup exacto por código;
- Top-3 fijo e inmutabilidad downstream;
- no reranking/no sustitución;
- temporalidad Decision 885/906;
- limitación del snapshot usado;
- ausencia de claim de corrección legal.

No traduzcas `evidence` como una formulación que implique prueba jurídica concluyente. Preferir `evidencia documental` / `documentary evidence` según contexto.

## 11. Alcance de edición del master

Modifica **solo**:

- el placeholder/contenido de `4.3 Documentary corpus and evidence resource` en Part I;
- el placeholder/contenido de `4.3 Corpus documental y recurso de evidencia` en Part II.

Todo texto aprobado de Sections 1–4.2.3 debe permanecer científicamente y textualmente intacto. Los placeholders 4.4–4.8 deben permanecer sin desarrollo.

No modifiques 3.5 ni 3.7: sus ajustes editoriales ya quedaron integrados en V010.

Si el proceso de edición altera contenido fuera del scope, detente con:

`EXPERIMENTAL_DESIGN_B02_OUT_OF_SCOPE_MUTATION`

## 12. Entregables obligatorios

### 12.1 Section file en GitHub

Crear:

`article/sections/experimental_design/Experimental_Design_B02_V01.md`

Debe contener únicamente la nueva Section 4.3 en inglés y español, precedida por un encabezado de control breve que identifique bloque/versión. No declarar aprobación.

### 12.2 Response en GitHub

Crear:

`article/responses/5_EXPERIMENTAL_DESIGN_B02_RESPONSE_V01.md`

Debe registrar como mínimo:

- repo/rama/HEAD de entrada;
- fuentes gobernantes leídas;
- evidencia técnica primaria verificada;
- comprobación del `SRC-03` vivo y si hubo cambios materiales;
- resumen claim-by-claim de las afirmaciones introducidas y su soporte;
- archivos modificados/generados;
- SHA-256 de los dos artefactos acumulativos locales;
- comentarios heredados preservados;
- tracked changes;
- QA/render del DOCX;
- confirmación de que 4.4+ y Results no fueron redactados;
- cualquier limitación o stop condition activada.

No uses `PASS`, `APPROVED`, `FROZEN`, `CLOSED` o `INTEGRATED` como autoestado operativo. Puedes reportar `EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT` si todo terminó técnicamente.

### 12.3 Master Markdown acumulativo candidato

Generar localmente a partir de V010 exacto:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.md`

No subirlo a GitHub si su transferencia directa incumple D-035. Entrégalo al autor como adjunto exacto y reporta SHA-256.

### 12.4 DOCX acumulativo candidato

Editar **el DOCX baseline exacto**, sin reconstrucción desde Markdown, y generar:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.docx`

Entrégalo al autor como adjunto exacto y reporta SHA-256.

Debe preservar los **40 comentarios de citas heredados** y mantener `tracked_changes = 0`, salvo hallazgo inesperado que obligue a detenerse y reportar.

## 13. QA obligatoria del DOCX

Antes de la entrega:

1. verifica SHA del baseline antes de editar;
2. verifica que los 40 comentarios heredados sigan presentes;
3. verifica `tracked_changes = 0`;
4. renderiza el DOCX candidato completo;
5. inspecciona visualmente **todas las páginas**;
6. confirma que no aparezcan desbordes, páginas corruptas, headings duplicados, secciones desplazadas o pérdida de comentarios/citas;
7. reporta page count y resultado de inspección.

No declares QA completa sin inspección visual integral.

## 14. Handoff D-035 / D-022

- Prompt operativo y response: GitHub.
- Section MD pequeño: GitHub.
- Master acumulativo MD y DOCX: entrega exacta al autor por adjunto cuando la transferencia al repo sea innecesaria o susceptible de timeout.
- No Base64 manual.
- No chunking.
- No fragmentación/reensamblado.
- No archivos auxiliares para eludir límites.
- No reconstrucción silenciosa del DOCX.

Si no puedes entregar el DOCX exacto al autor, detente con:

`EXPERIMENTAL_DESIGN_B02_DOCX_HANDOFF_FAILED`

## 15. Validación antes de finalizar

Confirma explícitamente:

```text
SECTION_4_3_ONLY = YES
PRIMARY_RESOURCE = DECISION_885_DERIVED_HIERARCHICAL_NANDINA_CORPUS
PRIMARY_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_CLAIM = NO
DOCUMENTARY_RERANKING_CLAIM = NO
CANDIDATE_SUBSTITUTION_CLAIM = NO
DECISION_906_TEMPORAL_BOUNDARY_DISCLOSED = YES
DECISION_906_RESULTS_ANTICIPATED = NO
PERUVIAN_NATIONAL_AUTHORITY_MISATTRIBUTION = NO
ARANCEL2022_AS_PRIMARY_HE4_CONTEXT = NO
CLASSIFICATION_RESOLUTIONS_AS_PRIMARY_HE4_CONTEXT = NO
LEGAL_CORRECTNESS_CLAIM = NO
SECTION_4_4_PLUS_DRAFTED = NO
RESULTS_DRAFTED = NO
FROZEN_TEXT_MUTATED = NO
FINAL_GAP_DEFINED = NO
NOVELTY_DECLARED = NO
```

## 16. Stop conditions

Detente sin improvisar si ocurre cualquiera:

- baseline DOCX ausente o SHA distinto;
- V010 no coincide con el Git blob gobernante;
- cambio vivo de SRC-03 que contradiga materialmente D-051;
- evidencia primaria muestra que Phase F/HE4 consumió otro corpus distinto del congelado;
- no puedes distinguir exact lookup de query retrieval con evidencia directa;
- la autoridad/temporalidad de Decision 885/906 resulta contradictoria;
- el DOCX no puede editarse sin reconstrucción;
- el DOCX exacto no puede entregarse;
- se requeriría modificar 4.4+, Results o texto congelado para completar la tarea.

No resuelvas una contradicción material con conocimiento general.

## 17. Formato de cierre en chat

Por D-022, no pegues la response completa en el chat. Responde únicamente con:

- ruta del response versionado en GitHub;
- commit SHA que lo contiene;
- nombres y SHA-256 de los dos adjuntos acumulativos entregados;
- estado `EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT` o el stop code correspondiente.

No avances después de ese punto.
