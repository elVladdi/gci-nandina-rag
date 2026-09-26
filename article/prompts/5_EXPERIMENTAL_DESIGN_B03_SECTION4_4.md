# Prompt 5 — Experimental Design B03 / Section 4.4

## Rol

Actúa como **IA de Redacción** del artículo científico principal destinado a *Knowledge-Based Systems*. Ejecuta exclusivamente el bloque `EXPERIMENTAL_DESIGN_B03` autorizado por D-056.

Tu función es redactar Methods con precisión empírica y trazabilidad. No eres la IA Experimental: no modifiques experimentos, datos, métricas, scripts, Plan Maestro ni repositorios experimentales.

## Onboarding obligatorio

Trabaja en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Lee íntegramente, antes de redactar:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/STYLE_GUIDE.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/DECISIONS.md`;
8. `article/governance/D055_EXPERIMENTAL_DESIGN_B02_INTEGRATION_AND_V011_PROMOTION.md`;
9. `article/governance/D056_EXPERIMENTAL_DESIGN_B03_SECTION4_4_START.md`;
10. este prompt completo.

El baseline acumulativo obligatorio es:

`article/manuscript/ARTICLE_MASTER_V011.md`

Identidad congelada:

- SHA-256: `ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f`;
- Git blob: `c2aee16c219ed33c16e8e647fbd56f4dacc2cd61`.

No reconstruyas el master desde archivos anteriores y no reescribas secciones aprobadas.

## Fuente experimental viva obligatoria

Antes de redactar consulta directamente:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- y, cuando sea necesario, `main`, commits y artefactos primarios que prueben las reglas de partición, composición, DAM, duplicados y near-duplicates.

Corte editorial al abrir B03:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
H100 = 2950 series / 28 DAM / 66 codes
DEV = 100 series / 6 DAM
EVAL = 1056 series / 67 DAM / 42 codes
```

Estos SHA son un corte de apertura, no una autorización para ignorar drift. Si el estado vivo cambió, registra el nuevo SHA y determina si afecta materialmente 4.4 antes de redactar.

No solicites al autor adjuntos que ya estén versionados en GitHub.

## Alcance único autorizado

Redacta exclusivamente:

- Part I: `4.4 Partition validity and dependence controls`;
- Part II: `4.4 Validez de las particiones y controles de dependencia`.

Preserva sin cambios Sections 1–4.3 y todo el resto del master.

No redactes 4.5–4.8, Results, Discussion, Conclusion, Abstract, Title ni Keywords.

## Función narrativa de 4.4

Explicar **por qué las particiones utilizadas para la evaluación vigente son metodológicamente válidas dentro del alcance del piloto y qué dependencia residual debe seguir respetándose**.

La sección debe permitir que el lector entienda, con objetos y controles observables:

1. cuál fue el riesgo detectado en el split histórico v0.1;
2. por qué compartir DAM entre banco histórico y evaluación podía introducir dependencia/leakage cuando varias series de una misma declaración comparten o aproximan descripciones y códigos;
3. cómo el benchmark v0.2 controla ese riesgo mediante particiones disjuntas por DAM/declaración;
4. que `SERIE` sigue siendo la unidad de análisis;
5. que `DAM` es la unidad de agrupamiento cuando existe dependencia;
6. que ausencia de DAM compartidas **entre particiones** no implica independencia automática de series **dentro de una misma DAM**;
7. qué papel tienen los controles de duplicados exactos y near-duplicates y qué no demuestran;
8. qué limitaciones residuales deben conservarse para interpretar posteriormente métricas e inferencia.

## Ground truth vinculante

Mantén, salvo que evidencia primaria viva obligue a una corrección documentada:

```text
ANALYSIS_UNIT = SERIE
DEPENDENCE_GROUPING_UNIT = DAM / customs declaration
CURRENT_BENCHMARK = v0.2
CROSS_PARTITION_DAM_OVERLAP = 0
H100 = 2950 series / 28 DAM / 66 codes
DEV = 100 series / 6 DAM
EVAL = 1056 series / 67 DAM / 42 codes
V0_1 = HISTORICAL_SNAPSHOT
V0_1_SPLIT = ROW_LEVEL_STRATIFIED_BY_NANDINA / seed 2026
V0_2_SPLIT = EXPLICIT_DAM_ASSIGNMENTS
ID_UNICO_UNIQUENESS != DAM_INDEPENDENCE
EXACT_DUPLICATE_CONTROL != DAM_GROUPING_CONTROL
NEAR_DUPLICATE_CONTROL != DAM_GROUPING_CONTROL
CROSS_PARTITION_DAM_DISJOINTNESS != WITHIN_DAM_SERIES_INDEPENDENCE
```

El ground truth experimental consolidado de 0A-02 establece expresamente que v0.2 elimina DAM compartidas entre particiones, pero no convierte automáticamente en independientes las series pertenecientes a una misma DAM dentro del evalset. Toda formulación inferencial posterior debe respetar ese agrupamiento.

### v0.1

El split v0.1 es histórico y no gobierna la evaluación final. Cuando se mencione, su función es explicar el riesgo metodológico que motivó el rediseño, no reportarlo como benchmark vigente.

La cifra histórica `3,000/100/1,006` solo puede usarse con su condición de snapshot histórico y evidencia primaria verificable.

No uses `48/59` como hecho cerrado si su trazabilidad continúa en estado `REVIEW_REQUIRED`.

La observación `995/1006` solo puede incorporarse si verificas directamente su fuente y su significado exacto. No la conviertas en una afirmación más amplia de leakage sin demostrar el vínculo correspondiente.

### v0.2

Explica el mecanismo real de partición. No digas que v0.2 fue aleatorizado por `seed=2026` si la implementación vigente materializa el split mediante listas explícitas de DAM; el seed puede permanecer como atributo de configuración/procedencia sin haber decidido las asignaciones v0.2.

No confundas:

- disjunción por DAM;
- unicidad de identificadores;
- duplicados textuales exactos;
- near-duplicates;
- balance o cobertura de códigos.

Son propiedades distintas y deben describirse separadamente.

### Duplicados y near-duplicates

No presentes umbrales de similitud como filtros si en el diseño real son diagnósticos/descriptores. El Plan Maestro vigente registra, para el flujo histórico prospectivo, umbrales 0.90/0.95/0.98 como descriptores y no como exclusión automática; verifica si y cómo ese hecho es pertinente al benchmark evaluado antes de trasladarlo a 4.4.

No afirmes que la disjunción por DAM elimina todo riesgo de similitud textual residual. Si existen análisis complementarios de exact/near duplicates, descríbelos únicamente con el alcance que demuestran y sin adelantar resultados que correspondan a Section 5.

## Fronteras obligatorias

No afirmar:

- independencia i.i.d. de las 1,056 series de evaluación;
- eliminación total de leakage por el solo hecho de separar DAM;
- que unicidad de `id_unico` demuestra independencia estadística;
- que ausencia de duplicados exactos elimina near-duplicates;
- que un umbral diagnóstico fue criterio de exclusión si no lo fue;
- generalización empírica fuera de Chapter 87;
- causalidad a partir de EXP-11A;
- resultados H150/H200 como si pertenecieran al benchmark primario;
- `EXP12_DIVERSITY_EFFECT` como estimable;
- resultados, p-values o conclusiones de Results antes de su gate;
- `FINAL_GAP` o `NOVELTY`.

Conserva:

`FINAL_GAP = NOT_DEFINED`

`NOVELTY = NOT_DECLARED`

## Estilo Methods obligatorio

Aplica SPCCR y la guía KBS vigente.

La prosa debe ser concreta. Evita abstracciones editoriales como “robust validity framework”, “comprehensive leakage mitigation” o “strict independence guarantee”. Nombra el objeto, la operación y la restricción: DAM, SERIE, partición, asignación, solapamiento, duplicado, similitud, agrupamiento.

No conviertas Methods en inventario de rutas, hashes, scripts o nombres internos. Los identificadores técnicos exhaustivos pertenecen a reproducibilidad; menciona un artefacto concreto solo si es metodológicamente indispensable.

No escribas Results disfrazados de Methods. Las cifras estructurales del diseño y composición sí son admisibles; las métricas de desempeño y conclusiones inferenciales no pertenecen a 4.4.

## Literatura y web

No hagas búsqueda web para este bloque salvo que una decisión editorial posterior lo autorice expresamente. 4.4 debe basarse primordialmente en el diseño experimental y sus artefactos primarios. No introduzcas literatura nueva para justificar retrospectivamente decisiones ya congeladas.

## Entregables obligatorios

Genera en GitHub, sin modificar el master canónico:

1. `article/sections/experimental_design/Experimental_Design_B03_V01.md`
   - solo Part I 4.4 y Part II 4.4;
   - debe ser autocontenido para auditoría.

2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md`
   - copia acumulativa derivada de `ARTICLE_MASTER_V011.md`;
   - únicamente 4.4 puede pasar de placeholder a prosa científica;
   - todo contenido aprobado previo debe preservarse.

3. `article/responses/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_RESPONSE_V01.md`
   - onboarding completado;
   - HEAD/blob de fuentes vivas realmente consultadas;
   - archivos creados;
   - claims principales y evidencia primaria que los soporta;
   - controles de frontera ejecutados;
   - confirmación explícita de que 4.5+ y Results no fueron redactados.

Si el flujo vigente de custodia DOCX requiere generar candidato binario, sigue estrictamente D-021/D-027/D-035 y las decisiones posteriores aplicables. No reconstruyas un DOCX aprobado desde Markdown y no uses Base64/chunking manual.

## QA antes de entregar

Verifica como mínimo:

- 4.4 inglés y español son semánticamente equivalentes;
- no se modificó 4.1–4.3;
- no se modificaron Sections 1–3;
- no se redactó 4.5+;
- no se adelantaron resultados;
- DAM y SERIE conservan sus roles correctos;
- v0.1 y v0.2 no se mezclan;
- `seed=2026` no se presenta falsamente como mecanismo de asignación v0.2;
- duplicados, near-duplicates y dependencia por DAM no se colapsan en un único concepto;
- no se declara independencia i.i.d.;
- no se declara eliminación total de leakage;
- no se declara generalización fuera del testbed;
- `FINAL_GAP` y `NOVELTY` permanecen sin definir/declarar.

## Gate de salida

Detente después de producir los tres entregables autorizados.

No integres B03 al master canónico.
No abras B04.
No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md` ni archivos de gobernanza.
No modifiques `SRC-03` ni `main`.

La entrega debe volver a la **IA Gestora** para auditoría independiente claim-by-claim y control diferencial contra `ARTICLE_MASTER_V011.md`.

Responde únicamente en español en el chat.
