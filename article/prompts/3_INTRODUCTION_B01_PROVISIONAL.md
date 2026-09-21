# Introduction B01 — Provisional Introduction

## 1. Alcance autorizado

Ejecuta exclusivamente `INTRODUCTION_B01 / Section 1 Introduction` como versión provisional.

No redactes Decision-support architecture, Experimental design, Results, Discussion, Conclusion, Abstract, Title, Keywords ni end matter.

Aplica obligatoriamente:

- `article/START_HERE.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`;
- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
- `article/governance/D023_TECHNICAL_CLOSURE_MODE.md` cuando corresponda;
- `article/governance/D025_RELATED_WORK_B06_APPROVAL_INTEGRATION_AND_INTRODUCTION_START.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- `article/STYLE_GUIDE.md`;
- Sections 2.1–2.6 ya aprobadas en el master canónico.

D-022 gobierna la respuesta: toda respuesta sustantiva debe quedar versionada en GitHub. En chat solo se permite el puntero mínimo autorizado.

## 2. Baseline acumulativo obligatorio

### Markdown canónico

Usa como baseline exacto:

`article/manuscript/ARTICLE_MASTER_V006.md`

Git blob esperado:

`7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`

### DOCX local

Conforme a D-021, continúa sobre el binario local aprobado de B06:

`ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx`

o una copia local renombrada que sea byte-for-byte idéntica.

SHA-256 obligatorio:

`3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`

Preserva exactamente:

- Related Work 2.1–2.6 en inglés y español;
- los 36 comentarios Word heredados;
- estilos, estructura y controles acumulativos;
- cero tracked changes.

Si el DOCX exacto no está disponible, detente con `BASELINE_DOCX_ACCESS_REQUIRED`; no reconstruyas el Word desde Markdown.

## 3. Función científica de la Introduction

La Introduction debe responder, en este orden, las siguientes preguntas narrativas:

1. ¿Cuál es el problema concreto de apoyo a la clasificación arancelaria que motiva el estudio?
2. ¿Qué hacen las familias de enfoques existentes y qué limitación verificable permanece cuando ranking, evidencia documental y generación pueden intervenir en momentos distintos de la decisión?
3. ¿Por qué esa limitación importa para evaluación, trazabilidad y revisión humana?
4. ¿Qué arquitectura propone estudiar este trabajo a alto nivel?
5. ¿Cuáles son las contribuciones científicas acotadas del artículo?
6. ¿En qué contexto experimental se evalúan esas contribuciones?
7. ¿Qué preguntas de investigación guían la evaluación?
8. ¿Cómo se organiza el resto del artículo?

No conviertas la Introduction en un resumen de Related Work ni en una descripción anticipada de Methods.

## 4. Secuencia narrativa obligatoria

Usa el flujo:

`problema concreto → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones acotadas → contexto de evaluación → RQs → roadmap`

Objetivo orientativo para Part I English: **900–1300 palabras**, salvo que una versión más breve cumpla íntegramente la función narrativa. Prefiere prosa continua y cohesionada. Las RQs pueden presentarse en una lista breve si mejora claridad.

## 5. Problema y antecedentes

La apertura debe ser concreta y evitar formulaciones genéricas sobre “la importancia de la IA”. Debe establecer que la clasificación arancelaria se apoya en descripciones comerciales y nomenclaturas jerárquicas y que los sistemas automáticos pueden cumplir funciones distintas: clasificación directa, ranking de candidatos, recuperación documental, control de búsqueda o generación de explicaciones.

La síntesis de antecedentes debe ser mucho más breve que Related Work. Reutiliza únicamente los antecedentes necesarios para sostener la limitación. No repitas el recorrido de Sections 2.1–2.6 autor por autor.

Para cualquier cita bibliográfica usada en la versión inglesa:

1. reabre la fuente primaria;
2. verifica el pasaje exacto;
3. limita el claim a lo soportado;
4. añade comentario Word anclado a la cita inglesa con el pasaje verificable, siguiendo el patrón acumulativo vigente.

No cites artefactos internos como si fueran bibliografía científica.

## 6. Limitación técnica defendible

La limitación no debe formularse como ausencia universal de trabajos previos. Debe derivarse del posicionamiento ya congelado:

- existe prior art de clasificación directa y jerárquica;
- existe prior art de candidate prediction + evidence retrieval;
- existen sistemas regulatorios/agentic donde evidence o LLM participa en search/decision making;
- existe prior art de regulatory AI con evaluación de explanation/source support.

Por ello, la limitación defendible se formula en términos de **separación operacional y evaluativa**: cuando candidate ranking, evidencia normativa y generación cumplen funciones diferentes, mezclar su autoridad dificulta atribuir qué componente produjo la decisión, qué componente solo la documenta y qué métrica corresponde a cada salida.

No uses “functional contract”, “separation of authority” u otras abstracciones como sustituto de la explicación. Si aparecen, deben operacionalizarse inmediatamente mediante acciones observables.

## 7. Propuesta de alto nivel

La Introduction debe presentar, sin entrar todavía en detalles de implementación, una arquitectura en la que:

1. una etapa de recuperación histórica genera y ordena candidatos;
2. el ranking y un Top-3 quedan fijados antes de la recuperación normativa;
3. la recuperación normativa asocia evidencia con esos candidatos sin insertar, eliminar, sustituir ni reordenar códigos;
4. un LLM local downstream recibe candidatos y contexto documental para producir explicación, sin modificar candidatos ni retroalimentar la clasificación;
5. ranking, asociación documental y explicación se evalúan por separado;
6. las particiones respetan DAM cuando la estructura compartida de la declaración introduce dependencia.

No presentes esta arquitectura como un hecho empírico ya validado; la Introduction presenta el objeto de estudio.

## 8. Contribuciones que pueden declararse

Las contribuciones deben ser concretas, distinguibles y acotadas. Puedes formular tres contribuciones principales, preferiblemente en un párrafo compacto o una enumeración breve:

1. **Arquitectónica-metodológica:** formalización de una arquitectura en la que ranking histórico, evidencia normativa y explicación downstream tienen funciones no superpuestas y límites explícitos de modificación.
2. **Evaluación:** diseño de una evaluación por función que distingue candidate retrieval, asociación documental y explicación/auditabilidad, incorporando partición agrupada por DAM cuando existe dependencia.
3. **Reproducibilidad/transferibilidad de la implementación:** documentación y recursos que permiten reinstanciar el procedimiento con otro banco histórico, otro espacio de clases y otro corpus documental, sin afirmar que el rendimiento observado generaliza a esas configuraciones.

No llames a estas contribuciones `novel`, `first`, `unique` ni equivalentes. No afirmes que cada componente sea nuevo.

El repositorio de reproducibilidad puede mencionarse a alto nivel como parte de la contribución de reproducibilidad, pero sus contenidos concretos deben describirse en la sección metodológica/end matter correspondiente, no en detalle aquí.

## 9. Contexto experimental

Solo después de que la propuesta y contribuciones sean claras, introduce el testbed aduanero offline.

Usa exclusivamente la terminología exacta de los ground truths para:

- alcance NANDINA/HS;
- unidad SERIE;
- agrupamiento por DAM;
- banco histórico;
- corpus documental/normativo;
- benchmark y particiones;
- rol del LLM local.

El testbed es una instanciación empírica de la arquitectura, no su definición conceptual.

No incluyas resultados, porcentajes, p-values, métricas observadas ni conclusiones empíricas.

## 10. Research Questions

La Introduction debe presentar versiones publicables, semánticamente equivalentes a las RQs retenidas por 0C y al estado experimental reconciliado, sin códigos internos como HE4, Grupo 3, C10 o EXP11.

Conserva este contenido:

- **RQ1:** desempeño de recuperación de candidatos del recuperador histórico bajo particiones disjuntas por DAM;
- **RQ2:** capacidad de asociar evidencia normativa identificable a cada candidato del Top-3 histórico fijo sin alterar su orden;
- **RQ3:** capacidad del LLM local restringido a preservar candidatos y orden y producir explicaciones estructuradas con evidencia identificable;
- **RQ4:** límites de validez introducidos por dependencia intra-DAM, near-duplicates residuales, composición del banco histórico y drift normativo al interpretar los resultados del piloto.

Puedes mejorar la redacción para publicación, pero no cambiar su objeto ni introducir nuevas RQs.

## 11. Configurabilidad y alcance

Debe quedar comprensible que la arquitectura no depende conceptualmente de un único dataset, espacio de clases o corpus documental: esos elementos son entradas/configuraciones reemplazables del procedimiento.

Pero preserva estrictamente:

`CONFIGURABILITY / REPLICABILITY ≠ EMPIRICAL_GENERALIZATION`

La Introduction puede afirmar que otro investigador **puede reinstanciar o replicar el procedimiento** con sus propios datos, clases y corpus si sigue las interfaces y pasos documentados. No puede afirmar que obtendrá el mismo rendimiento ni que los resultados se generalizan fuera del testbed evaluado.

## 12. Estilo de escritura

Aplica KBS_EWG_34_V01 y SPCCR.

Reglas específicas:

- sujeto/componente concreto antes de la acción;
- acción antes de abstracción;
- una oración debe permitir identificar quién hace qué, con qué entrada y bajo qué restricción;
- evita cadenas de nominalizaciones y frases de gobernanza;
- no uses códigos internos en la prosa publicable;
- no uses “framework” repetidamente cuando `architecture`, `procedure`, `retrieval stage` o `evaluation design` sea más preciso;
- no describas el artículo como si fuera un protocolo administrativo;
- evita frases como “this functional contract operationalizes...” si pueden sustituirse por una descripción concreta de las etapas;
- el inglés debe sonar como artículo científico originalmente escrito en inglés; el español es espejo de control semántico, no traducción literal rígida.

## 13. Fronteras obligatorias

Debe permanecer cierto:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Queda prohibido:

- `first`, `novel`, `unique`, `unprecedented`, `to our knowledge, the first`;
- ausencia universal de prior art;
- SOTA o superioridad cross-study;
- resultados o performance del presente estudio;
- causalidad no identificada;
- que normative evidence pruebe substantive/legal correctness;
- que explanation/auditability pruebe legal correctness;
- que provenance/reproducibility prueben correctness;
- que configurability implique empirical generalization;
- que el testbed NANDINA/Chapter-Class 87 defina el alcance conceptual de la arquitectura;
- cualquier apertura anticipada de Architecture, Experimental design, Results o Discussion.

## 14. Artefactos de salida

Genera exactamente:

1. `article/sections/introduction/Introduction_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx` — solo local bajo D-021; no subir a GitHub
4. `article/responses/3_INTRODUCTION_B01_RESPONSE_V01.md`

Los dos Markdown científicos deben contener Part I English y Part II Spanish semantic-control mirror.

El master candidato debe partir de `ARTICLE_MASTER_V006.md` y modificar exclusivamente el placeholder de Introduction en ambas partes. Related Work 2.1–2.6 debe permanecer byte-for-byte igual en Markdown.

El DOCX debe partir del binario B06 aprobado y modificar exclusivamente Introduction, preservando los 36 comentarios heredados y agregando únicamente comentarios para las nuevas citas inglesas de Introduction.

No promuevas todavía `ARTICLE_MASTER_V007`.

## 15. QA obligatorio antes del commit

Verifica y registra en la respuesta GitHub:

- baseline MD blob correcto;
- baseline DOCX SHA-256 correcto;
- Related Work 2.1–2.6 preservado exactamente;
- 36/36 comentarios heredados preservados;
- número de citas inglesas nuevas y cobertura de comentarios;
- equivalencia semántica EN–ES;
- ausencia de tracked changes;
- integridad OOXML;
- render completo del DOCX candidato;
- SHA-256 final del DOCX local;
- Introduction como único contenido científico nuevo;
- ausencia de resultados del estudio;
- ausencia de novelty/SOTA/universal-absence claims;
- RQ1–RQ4 presentes y semánticamente alineadas;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`;
- secciones posteriores no modificadas.

## 16. Commit y respuesta GitHub

Después del QA, crea un único commit semántico que añada exclusivamente los tres archivos Markdown autorizados:

- `article/sections/introduction/Introduction_B01_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V01.md`

No subas el DOCX.

No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, governance, masters canónicos, Related Work 2.1–2.6, fuentes experimentales ni secciones posteriores.

La respuesta GitHub debe contener el informe completo de ejecución. Conforme a D-022, no reproduzcas ese informe en chat.

Si la interfaz exige un mensaje final, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_RESPONSE_V01.md@<commit_sha>`

Después, detente. La IA Gestora realizará auditoría independiente y solicitará aprobación del autor antes de cualquier integración o apertura de Decision-support architecture.
