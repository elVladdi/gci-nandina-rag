# PROMPT122-R2 — Respuesta de preflight G7-F03 sobre ARTICLE_MASTER_V028

La ejecución se limitó al preflight de alineación científica de lo ya redactado y al diagnóstico de completitud del artículo en construcción. La entrada gobernante fue exclusivamente `article/manuscript/ARTICLE_MASTER_V028.md` de `article/main-manuscript` en el commit fijado; `ARTICLE_MASTER_V026.md` y `ARTICLE_MASTER_V027.md` no se utilizaron como base de trabajo. No se modificó el artículo, no se modificó la tesis, no se ejecutó Grupo 8 y no se redactaron todavía las secciones faltantes.

```text
PROMPT122_R2_EXECUTION = COMPLETE
ARTICLE_MASTER_INPUT = article/manuscript/ARTICLE_MASTER_V028.md
ARTICLE_SOURCE_BRANCH = article/main-manuscript
ARTICLE_SOURCE_COMMIT = 235893711cedca743a506f4f5da8f779268b8ed0
ARTICLE_MASTER_BLOB_SHA = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
ARTICLE_MASTER_SIZE = 258157
ARTICLE_MASTER_STATUS = WORK_IN_PROGRESS / NOT_FINAL
THESIS_FINAL_IDENTITY_MATCH = true
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false

ALIGNMENT_ITEMS_TOTAL = 19
ALIGNMENT_CRITICAL = 0
ALIGNMENT_MAJOR = 3
ALIGNMENT_MINOR = 3
ALIGNMENT_KEEP = 13

COMPLETENESS_COMPONENTS_TOTAL = 21
COMPLETE_CURRENT = 3
PARTIAL = 5
PLACEHOLDER = 12
MISSING = 1

ESTIMATED_FUTURE_G7_F03_BLOCKS = 7
ARTICLE_READY_FOR_FINAL_AUDIT = false
NEW_REFERENCES = 0
WEB_SEARCH_USED = false
GROUP8_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Precondiciones e identidades verificadas

Se verificó el gate de `writing_prompts_tmp/121N_AUDITORIA_EXTERNA_PASS.md` en el commit `be902fa0df0cc40ac9a5ad2cb8a040dc3ceeb9e6`:

```text
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
```

La identidad del master V028 coincidió exactamente con el contrato:

```text
path = article/manuscript/ARTICLE_MASTER_V028.md
branch = article/main-manuscript
commit = 235893711cedca743a506f4f5da8f779268b8ed0
blob_sha = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
size = 258157 bytes
```

La tesis final y su trazabilidad también coincidieron exactamente:

```text
Molleapasa_gv_G7F02_FINAL_CLEAN.docx
SHA256 = e734e1b93e82e732d7db99eec9fd22334e67f9621dacfedc4a559ab90f785a85
SIZE = 3909601

g7_thesis_claim_traceability_v0.3_FINAL.csv
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

V028 declara de forma explícita que es una base editable acumulativa y no un manuscrito terminado. La auditoría respetó ese estado: los placeholders y notas de drafting se trataron como incompletitud editorial, no como contradicciones científicas.

## 2. Matriz completa de alineación científica

| ARTICLE_SYNC_ID | ARTICLE_LOCATION | THESIS_GOVERNING_LOCATION | CURRENT_ARTICLE_TEXT_OR_CLAIM | FINAL_THESIS_STATE | DISPOSITION | SEVERITY | SCIENTIFIC_REASON | PROPOSED_MINIMAL_ACTION |
|---|---|---|---|---|---|---|---|---|
| ARS-001 | Title — instrucción de trabajo | Alcance final de G7-F02; Conclusiones | El título debe definirse al final, priorizando la contribución arquitectónica y usando aduanas como aplicación/testbed si mejora la precisión. | La tesis final delimita un piloto offline del Capítulo 87 y separa arquitectura, evidencia y explicación sin convertir el testbed en generalización. | KEEP | NONE | La instrucción de título es compatible con el alcance final y no contiene un claim empírico adicional. | Mantener la instrucción hasta el bloque final de front matter; no fijar aún un título definitivo. |
| ARS-002 | 1. Introduction y RQ1–RQ4 | Cap. IV; 4.2; Conclusiones | Presenta ranking histórico, Top-3 fijo, evidencia normativa posterior, LLM explicador, unidad SERIE, agrupamiento DAM y testbed offline del Capítulo 87. | Es la misma separación funcional y el mismo alcance interno aprobado. | KEEP | NONE | No se detectaron denominadores obsoletos, atribución incorrecta de funciones ni sobreafirmaciones jurídicas o de generalización. | Conservar; sincronizar solo las referencias internas que resulten afectadas por futuros bloques. |
| ARS-003 | 2. Related work y 2.6 Positioning | Cap. II y 4.3.5 / Tabla 23 | Posiciona el trabajo por autoridad no solapada entre ranking, evidencia y explicación, sin reclamar novedad de componentes aislados ni superioridad global. | La tesis final usa el mismo contraste funcional y evita comparaciones numéricas directas entre estudios no equivalentes. | KEEP | NONE | El posicionamiento respeta los guardrails de comparabilidad y no convierte evidencia recuperada en corrección jurídica. | Conservar la lógica; cerrar posteriormente la lista bibliográfica controlada. |
| ARS-004 | 3. Decision-support architecture | 3.2.4; 4.1.5; 4.3.1 y 4.3.4 | Recuperación histórica genera y ordena; Top-3 queda fijo; evidencia documental se asocia después; LLM solo explica y no retroalimenta el ranking. | Arquitectura final: histórico → Top-3 fijo → evidencia normativa por candidato → contexto → explicación local. | KEEP | NONE | Coincidencia funcional directa con la tesis final. | Conservar. |
| ARS-005 | 4.1–4.4; datos, particiones y dependencia | 3.3–3.6; 4.1.1; Tabla 10; Conclusión 2 | SERIE como unidad; DAM como grupo cuando aplica; 4,106 curadas; H100 2,950/28/66; DEV 100/6/9; EVAL 1,056/67/42; split DAM-disjoint. | Mismos conteos y mismo contrato de dependencia. | KEEP | NONE | Los tamaños, denominadores, unidad de análisis y control de dependencia están alineados. | Conservar. |
| ARS-006 | 4.5, 4.6.1 y 5.2 — recuperación histórica | 4.1.4 / Tabla 14; 4.2.2; Conclusión 3 | Top-1 0.5095; Top-3 0.6714; Top-5 0.7633; Top-10 0.8911; Top-50 0.9915; MRR@100 0.6297; se presenta como ranking de candidatos. | Mismos valores y límite: superioridad de recuperación histórica, no accuracy global del sistema. | KEEP | NONE | No se detectó confusión entre ranking y clasificación end-to-end. | Conservar. |
| ARS-007 | 4.7 y 5.6 — inferencia HE2 | 3.8.3; 4.2.2; Tabla 21; Conclusiones 3–4 | Bootstrap pareado por clusters DAM, 10,000 réplicas; 15 IC bilaterales 99% > 0; contraste Recall@200−Recall@100 con IC 95% > 0; sin p-values. | HE2 respaldada por exactamente ese contrato inferencial interno. | KEEP | NONE | El artículo no introduce p-values ni extiende la inferencia a población externa. | Conservar. |
| ARS-008 | 4.6.1, 5.2 y 5.5 — comparadores normativos y cobertura profunda | 4.1.3 / Tablas 12–13; 4.2.2; Conclusión 4 | Comparadores plano, jerárquico y D1a permanecen comparadores; cobertura profunda se separa del ranking temprano; Attempt06 se describe como correctivo descriptivo, no efecto global nulo. | La tesis final mantiene el ranking histórico como mecanismo principal y la cobertura jerárquica profunda como objeto separado; `ATTEMPT06 != GLOBAL_ZERO_IMPACT`. | KEEP | NONE | La interpretación está delimitada correctamente. | Conservar. |
| ARS-009 | 5.3 y 6.1 — integración histórica–normativa | 4.1.5 / Tabla 16; 4.2.3; Conclusión 5 | Ranking invariante 1,056/1,056; 3,168/3,168 posiciones con trazabilidad histórica y normativa; evidencia no reordena. | Mismos conteos y misma función documental; HE3 respaldada en este componente. | KEEP | NONE | Coincide con la evidencia final de integración. | Conservar. |
| ARS-010 | 3.1/3.6/4.5 y protocolos de evaluación — reranker diagnóstico | 3.2.4; 3.8.4; 4.1.6 / Tabla 17 | V028 solo menciona que una ruta separada de reranking puede evaluarse o existe fuera del flujo principal; no documenta como procedimiento ejecutado la muestra diagnóstica de 20 casos. | Se ejecutó una prueba diagnóstica independiente de 20 casos; referencia en pool 19, fuera 1; no forma parte del ranking principal. | UPDATE_REQUIRED | MAJOR | El texto metodológico ya escrito queda incompleto frente a un experimento efectivamente ejecutado y utilizado en HE3. | En un bloque futuro, añadir únicamente el protocolo ejecutado del reranker diagnóstico, manteniéndolo fuera del flujo principal y sin inventar inferencia. |
| ARS-011 | 5. Results, 5.7 y 6. Discussion — reranker diagnóstico | 4.1.6 / Tabla 17; 4.2.3; 4.3.4; Tabla 24; Conclusión 6 | No reporta el resultado diagnóstico de 20 casos ni sus métricas antes/después. | Top-1 0.5000/0.5000; Top-3 0.6500/0.6500; Top-5 0.8000/0.8000; MRR 0.6326/0.6326; 0/19/0 mejora/empate/deterioro; diagnóstico solamente. | UPDATE_REQUIRED | MAJOR | La omisión deja incompleta la evidencia final de HE3 y puede hacer parecer que el reranker quedó solo como posibilidad de diseño. | Incorporar una subsección o párrafo breve en Results y su interpretación limitada en Discussion; no generalizar efecto nulo fuera de la muestra. |
| ARS-012 | 4.6.3 y 5.4 — HE4 central | 3.8.5; 4.1.7 / Tablas 18–19; 4.2.4; Conclusión 7 | Preservación Top-3/orden 50/50; trazabilidad 50/50; warning genérico 41/50 y faltante 9/50; 28/50 auditables; 22/50 no auditables; 0/50 violaciones graves; evaluador IA independiente, sin scoring humano. | Mismos estados y modalidad; HE4 parcialmente respaldada. | KEEP | NONE | Los conteos principales y los límites de interpretación están alineados. | Conservar. |
| ARS-013 | 5.4, 5.7, 6.2 y 6.4 — `schema compliance = 0/50` | 3.8.5; 4.1.7 / Tabla 18 y Nota; 4.2.4 | V028 cuantifica 0/50 de cumplimiento de esquema/completitud de campos por `advertencias_globales` y repite esa tasa como resultado. | La tesis final conserva la discrepancia de especificación como limitación metodológica; `advertencias_globales` quedó fuera de la evaluación y no se trató como métrica adicional. | DELETE_REQUIRED | MAJOR | La tasa 0/50 convierte una incompatibilidad de especificación en una métrica cuantitativa que la tesis final deliberadamente no usa como resultado HE4. | Eliminar la tasa 0/50 como resultado; conservar únicamente la descripción de la discrepancia prompt–esquema como limitación, sin borrar los controles HE4 válidos. |
| ARS-014 | 5.5 y RQ4 — HE5, sensibilidades y EXP12 | 3.8.6; 4.1.8 / Tabla 20; 4.2.5; Tabla 24; Conclusión 8 | EXP11A se interpreta como sensibilidad conjunta tamaño–composición no causal; H150/H200 como descriptivo sin superpoblación de seeds; Attempt06 no se resume como cero global; diversidad y calidad descriptiva no estimables; HE5 inconclusa. | Mismo estado final y mismos guardrails. | KEEP | NONE | No se detectaron umbrales post hoc ni reapertura de EXP12. | Conservar. |
| ARS-015 | 4.3 y RQ4 — corpus derivado de Decisión 885 y divergencia frente a Decisión 906 | 3.7.1–3.7.2; 4.1.2; 4.3.3; Tabla 24 | V028 identifica de forma específica Decisión 885, vigencia 2022 y una modificación posterior por Decisión 906, y usa esa diferencia como frontera temporal del corpus. | La tesis final sí exige vigencia/versionado y limita la validez del corpus, pero no materializa esos identificadores normativos específicos como resultado final. | VERIFY_ONLY | MINOR | No hay contradicción, pero la granularidad normativa del artículo excede lo explicitado por la tesis final y debe quedar respaldada por una fuente congelada propia del corpus antes de conservarse. | Verificar contra la fuente/versionado congelado del corpus; si no queda soportado literalmente, reducir al lenguaje de vigencia/versionado aprobado por la tesis. |
| ARS-016 | 5.3 — `exact NANDINA-8 association = 3,168/3,168` | 3.2.4; 3.8.4; 4.1.5 / Tabla 16; Conclusión 5 | V028 reporta asociación documental exacta NANDINA-8 en 3,168/3,168 slots y 1,056/1,056 casos. | La tesis final congela 3,168/3,168 de trazabilidad candidato–documento normativo y describe obtención de evidencia mediante el código del candidato, pero no presenta una tasa separada titulada “exact NANDINA-8 association”. | VERIFY_ONLY | MINOR | El contenido es compatible con el mecanismo, pero el nombre de la métrica es más fuerte/específico que la formulación gobernante de la tesis. | Verificar el artefacto congelado de integración; si no existe una métrica explícita de asociación exacta, usar la formulación de “documento normativo identificable/trazabilidad completa”. |
| ARS-017 | 6.1–6.5 Discussion | 4.3.1–4.3.7; Tablas 22–24 | Separa ranking/evidencia, acota el LLM, compara prior art por función, limita auditabilidad y distingue configurabilidad de transferencia empírica. | Mismas fronteras interpretativas de la tesis final. | KEEP | NONE | La discusión escrita respeta los límites de causalidad, legalidad y validez externa. | Conservar; completar 6.6 sin debilitar estos límites. |
| ARS-018 | 4.8 — estado del repositorio público de reproducibilidad | 3.7.6; 4.3.7 / Tabla 24; Conclusión 2 | V028 describe un snapshot público con protocolos/documentación pero sin runner canónico, preset, lock, resultados canónicos ni validación clean-room, y ordena re-verificación antes del envío. | La tesis final concluye reproducibilidad sustancial con limitaciones, activos locales/restringidos y no determinismo; no congela el estado exacto de un repositorio público externo al momento del futuro envío. | VERIFY_ONLY | MINOR | Es una afirmación potencialmente mutable y no debe quedar obsoleta al cierre del artículo. | Revalidar contra una fuente versionada del paquete de reproducibilidad inmediatamente antes del bloque de end matter; no usar búsqueda web en este preflight. |
| ARS-019 | Global — claims, disposiciones y guardrails | 4.2 / Tabla 21; Conclusiones | El texto escrito respalda HE2 dentro del benchmark, deja HE5 inconclusa, no inventa disposición terminal para HE1/HG, no equipara evidencia normativa o auditabilidad con corrección jurídica y no presenta configurabilidad como generalización. | HE1 y HG sin disposición formal terminal; HE2 respaldada; HE3 respaldada; HE4 parcialmente respaldada; HE5 inconclusa; guardrails congelados. | KEEP | NONE | No se detectó un overclaim terminal o jurídico en el texto actualmente redactado. | Conservar; al cerrar Conclusion, mantener exactamente estos límites y no crear una decisión agregada para HG. |

### Síntesis de alineación

V028 está **mayoritariamente alineado** con la tesis final. No se localizaron contradicciones críticas ni cifras centrales obsoletas en datasets, recuperación histórica, HE2, integración, HE4 principal o HE5. Las tres correcciones científicas mayores son acotadas: (1) documentar como ejecutado el reranker diagnóstico en Methods, (2) incorporar sus resultados y límites en Results/Discussion, y (3) retirar la tasa `0/50` de cumplimiento de esquema como métrica, conservando la discrepancia prompt–esquema solo como limitación. Tres afirmaciones adicionales requieren verificación contra fuentes congeladas antes de retener su granularidad actual: decisiones normativas 885/906, denominación de “asociación exacta NANDINA-8” para 3,168/3,168 y el estado puntual del paquete público de reproducibilidad.

## 3. Matriz completa de completitud de V028

| ARTICLE_COMPLETENESS_ID | SECTION_OR_COMPONENT | CURRENT_STATUS | WHAT_EXISTS_NOW | WHAT_IS_STILL_MISSING | THESIS_SOURCE_AVAILABLE | ADDITIONAL_FROZEN_SOURCE_REQUIRED | CAN_BE_COMPLETED_WITH_CURRENT_GOVERNING_SOURCES | DEPENDENCY | PROPOSED_FUTURE_BLOCK |
|---|---|---|---|---|---|---|---|---|---|
| AC-001 | Title | PLACEHOLDER | Instrucción editorial para definirlo al final. | Título científico final. | true | false | true | Cuerpo final, figuras/tablas y conclusión cerrados. | F03-B5 |
| AC-002 | Abstract | PLACEHOLDER | Orden retórico y objetivo aproximado de extensión. | Abstract completo con método, resultados principales y límites. | true | false | true | Cuerpo y conclusión cerrados. | F03-B5 |
| AC-003 | Keywords | PLACEHOLDER | Instrucción de seleccionar 5–7 al final. | Lista final de keywords. | true | false | true | Título y abstract cerrados. | F03-B5 |
| AC-004 | 1. Introduction | COMPLETE_CURRENT | Prosa completa, contribuciones, testbed, cuatro RQs y roadmap. | Solo sincronización de referencias internas si cambia la numeración futura. | true | false | true | Cambios posteriores de estructura. | F03-B6 |
| AC-005 | 2. Related work | COMPLETE_CURRENT | Prosa completa 2.1–2.6 y posicionamiento funcional. | Cierre bibliográfico formal en la lista de referencias. | true | true | false | Ledger/lista bibliográfica congelada del flujo del artículo. | F03-B4 |
| AC-006 | 3. Decision-support architecture | COMPLETE_CURRENT | Prosa arquitectónica completa 3.1–3.7; Top-3 fijo, evidencia y explicación separadas. | Integración del elemento gráfico final y limpieza de nota de drafting. | true | true | false | Especificación/activo gráfico congelado del artículo. | F03-B3 |
| AC-007 | 4. Experimental design | PARTIAL | Datos, corpus, split, configuración, evaluación HE2, HE4, HE5 y reproducibilidad ya redactados. | Incorporar el procedimiento ejecutado del reranker diagnóstico de 20 casos y resolver las verificaciones de corpus/reproducibilidad. | true | true | true | Resolución ARS-010, ARS-015, ARS-018. | F03-B1 |
| AC-008 | 5. Results | PARTIAL | 5.1–5.7 contienen resultados sustantivos de datos, retrieval, evidencia, HE4, sensibilidades e inferencia. | Resultado del reranker diagnóstico; retirar métrica 0/50 de esquema; resolver ARS-016; depurar notas de drafting. | true | true | true | Resolución ARS-011, ARS-013, ARS-016. | F03-B1 |
| AC-009 | 6. Discussion | PARTIAL | 6.1–6.5 están redactadas y científicamente delimitadas. | Integrar lectura del reranker; eliminar el uso métrico 0/50; redactar 6.6 Limitations, hoy placeholder. | true | false | true | Correcciones de Results cerradas. | F03-B2 |
| AC-010 | 7. Conclusion | PLACEHOLDER | Encabezado e instrucción retórica. | Conclusión completa: aporte, evidencia principal, alcance y límites; sin dictamen terminal inventado para HG/HE1. | true | false | true | Discussion finalizada. | F03-B2 |
| AC-011 | Figures | PLACEHOLDER | Existe al menos `[Figure 1 placeholder — overall architecture and information flow.]`; no hay conjunto final de figuras incorporado al master. | Selección, activos, captions, numeración y llamadas finales de figuras. | true | true | false | Especificaciones/activos gráficos congelados compatibles con el artículo. | F03-B3 |
| AC-012 | Tables | MISSING | No hay un conjunto de tablas científicas del artículo integrado en el master de publicación. | Seleccionar el mínimo de tablas necesarias para comunicar resultados sin duplicación; captions y llamadas. | true | false | true | Results científicos reconciliados. | F03-B3 |
| AC-013 | References | PLACEHOLDER | Existen numerosas citas autor–año en el cuerpo; la sección final de referencias sigue como placeholder. | Lista bibliográfica completa y reconciliada con todas las citas del artículo. | true | true | false | Fuente/ledger bibliográfico versionado del flujo del artículo; no nueva búsqueda web en este preflight. | F03-B4 |
| AC-014 | Data availability | PLACEHOLDER | Encabezado final sin texto. | Declaración final de disponibilidad, restricciones y procedencia de datos. | true | true | false | Decisiones y artefactos congelados de acceso/redistribución. | F03-B4 |
| AC-015 | Reproducibility resources | PARTIAL | Sección 4.8 sustantiva describe contratos, límites y snapshot público; la declaración final permanece vacía. | Cerrar declaración de código/recursos y revalidar el estado versionado del paquete antes del envío. | true | true | false | Snapshot/versionado congelado del paquete público y resolución ARS-018. | F03-B4 |
| AC-016 | CRediT | PLACEHOLDER | Solo encabezado. | Roles CRediT definitivos. | false | true | false | Declaración autoral aprobada. | F03-B4 |
| AC-017 | Funding | PLACEHOLDER | Solo encabezado. | Declaración de financiamiento o ausencia de financiamiento. | false | true | false | Información administrativa/autoral aprobada. | F03-B4 |
| AC-018 | Competing interests | PLACEHOLDER | Solo encabezado. | Declaración final de conflictos de interés. | false | true | false | Declaración autoral aprobada. | F03-B4 |
| AC-019 | Acknowledgements | PLACEHOLDER | Solo encabezado. | Texto final o decisión de omitir. | false | true | false | Decisión autoral y reconocimientos aprobados. | F03-B4 |
| AC-020 | Supplementary material | PLACEHOLDER | Sección marcada como opcional y placeholder. | Decidir si existe material suplementario; si existe, inventario y referencias internas. | true | true | false | Plan de presentación final y disponibilidad de artefactos suplementarios. | F03-B4 |
| AC-021 | Submission cleanup / master publicable | PARTIAL | V028 conserva notas de drafting y una PART II en español como espejo de control semántico interno. | Retirar notas de trabajo y contenido interno no destinado al envío; conservar solo el master inglés final, con referencias cruzadas y consistencia editorial cerradas. | true | false | true | Todos los bloques de contenido, figuras/tablas y end matter cerrados. | F03-B6 |

### Síntesis de completitud

V028 contiene un núcleo científico amplio y utilizable, pero **no es un manuscrito terminado**. Introduction, Related work y la arquitectura están en estado `COMPLETE_CURRENT`; Experimental design, Results y Discussion requieren todavía sincronización o cierre; Title, Abstract, Keywords, Conclusion y la mayor parte del end matter permanecen como placeholders; las tablas científicas del artículo todavía no están integradas; y las figuras siguen sin materialización final en el master. La PART II en español y las notas de drafting son controles internos de construcción y deberán retirarse del master de envío.

## 4. Secuencia mínima propuesta para terminar G7-F03

La evidencia observada justifica **7 bloques futuros** si se mantiene una separación auditable entre corrección científica, completitud, presentación, metadatos y auditoría. Algunos podrían fusionarse solo si los insumos externos/autoriales ya estuvieran congelados al iniciar el bloque correspondiente.

1. **F03-B1 — Reconciliación científica de Methods/Results existentes.** Resolver ARS-010 a ARS-016: incorporar el reranker diagnóstico ejecutado, retirar `schema compliance 0/50` como métrica, conservar la discrepancia como limitación y verificar las tres afirmaciones marcadas `VERIFY_ONLY`. No redactar aún front matter.
2. **F03-B2 — Cierre de Discussion y Conclusion.** Completar 6.6 Limitations y la Sección 7 usando la tesis final como fuente científica, incluyendo los límites de HE3/HE4/HE5 y evitando dictamen terminal para HE1/HG.
3. **F03-B3 — Figuras y tablas del artículo.** Definir e integrar el conjunto mínimo de elementos visuales y tabulares, captions y referencias cruzadas, preservando resultados congelados y evitando duplicación entre texto, tablas y figuras.
4. **F03-B4 — Referencias y end matter.** Reconciliar la lista bibliográfica desde la fuente versionada del artículo y completar Data availability, reproducibility resources, CRediT, funding, competing interests, acknowledgements y la decisión sobre supplementary material. Este bloque depende de declaraciones autorales/administrativas y del snapshot congelado de reproducibilidad.
5. **F03-B5 — Front matter final.** Solo después del cuerpo cerrado: definir Title, Abstract y Keywords de acuerdo con la estructura KBS congelada y el alcance realmente reportado.
6. **F03-B6 — Coherencia científica y editorial global.** Retirar notas de drafting y el espejo semántico interno no destinado a envío, verificar todas las referencias internas, cifras, denominadores, captions, RQs y guardrails, y producir el master inglés coherente para auditoría.
7. **F03-B7 — Auditoría final del artículo.** Auditoría integral de completitud, consistencia científica, referencias, figuras/tablas, end matter y preparación para la etapa de aprobación que corresponda. No implica Grupo 8.

## 5. Bloqueadores reales para cierre final

No hay un bloqueador que impida este preflight, pero sí dependencias reales que impiden declarar el artículo listo para auditoría final ahora:

- falta resolver el reranker diagnóstico en Methods/Results/Discussion;
- debe eliminarse como resultado la tasa `schema compliance = 0/50` y conservarse solo la limitación de especificación;
- las afirmaciones específicas sobre Decisiones 885/906, “asociación exacta NANDINA-8” y estado del paquete público de reproducibilidad requieren verificación contra fuentes congeladas antes de su cierre;
- faltan figuras y tablas finales del artículo;
- falta la lista bibliográfica final reconciliada;
- faltan declaraciones autorales/administrativas para CRediT, funding, competing interests y acknowledgements;
- faltan Title, Abstract, Keywords, Limitations, Conclusion y el end matter final;
- V028 conserva notas de drafting y el espejo español de control interno, por lo que todavía no es un master de envío.

## 6. Estado terminal

```text
ARTICLE_MASTER_GOVERNING_VERSION = ARTICLE_MASTER_V028.md
ARTICLE_MASTER_V026_USED_AS_BASE = false
ARTICLE_MASTER_V027_USED_AS_BASE = false
ARTICLE_MASTER_V028_STATUS = WORK_IN_PROGRESS / NOT_FINAL
PROMPT122_R2_EXECUTION = COMPLETE
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
GROUP8_EXECUTED = false
ARTICLE_READY_FOR_FINAL_AUDIT = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detenido para auditoría externa. No se ejecutó ninguna edición del artículo ni ningún bloque posterior.