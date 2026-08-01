# Revision cualitativa de fichas auditables 10B v0.1

## 1. Objetivo

Evaluar cualitativamente si las fichas auditables generadas en Fase 10B son utiles para auditoria humana. La revision no busca medir de nuevo el rendimiento del recuperador ni validar juridicamente la clasificacion arancelaria; busca determinar si una persona experta puede entender el caso, rastrear la evidencia usada, comparar los candidatos Top-3 y decidir donde concentrar su revision.

Esta revision no ejecuto LLM, no ejecuto Ollama, no uso OpenAI ni APIs remotas, no regenero outputs de 10B y no amplio la muestra.

## 2. Alcance de la revision

Se revisaron los artefactos versionados y regenerables de Fase 10B:

- `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_quality_metrics.json`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/case_audit_quality_summary.csv`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards.md`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/sample_cases.csv`, solo para recuperar `expected_rank_historical`.

El alcance cualitativo cubre 10 fichas de las 50 generadas por 10B. No se modificaron fichas originales ni outputs de 10B.

## 3. Criterio de seleccion de las 10 fichas

La seleccion fue trazable y basada en `case_audit_quality_summary.csv`, cruzado con `sample_cases.csv`.

Se observo que los 50 casos tienen tres niveles de score de auditabilidad:

- Alto: `1.0`
- Medio: `0.9333333333333333`
- Bajo: `0.8666666666666667`

Se usaron cuatro cupos de revision:

- 3 casos de score alto, con `expected_rank_historical = 1` y sin fallos registrados.
- 3 casos de score medio, con `expected_rank_historical = 1` y fallos secundarios representativos.
- 2 casos de score bajo, priorizando fallos acumulados y un caso con conclusion ausente.
- 2 casos donde la NANDINA esperada no estaba en rank 1, seleccionados aparte para probar si la ficha ayuda cuando el Top-1 historico no coincide con la etiqueta esperada.

Hubo solapamiento potencial entre "score alto" y "NANDINA esperada no rank 1". Para evitar doble conteo, los casos no-rank-1 se documentaron como categoria propia aunque algunos tengan score `1.0`.

## 4. Casos seleccionados

| case_id | id_unico | score auditabilidad | rank historico esperado | razon de seleccion | ruta de ficha original |
| --- | --- | ---: | ---: | --- | --- |
| `DA-EVAL-00316` | `118-2026-10-096423-00-36` | 1.0 | 1 | Alto, sin fallos, repuesto especifico de embrague | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00316.md` |
| `DA-EVAL-00520` | `118-2026-10-128583-00-2569` | 1.0 | 1 | Alto, sin fallos, pieza de suspension/rotula | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00520.md` |
| `DA-EVAL-00778` | `118-2026-10-146957-00-1227` | 1.0 | 1 | Alto, sin fallos, caso marcado como difficult_low_support | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00778.md` |
| `DA-EVAL-00047` | `118-2026-10-006732-00-1` | 0.9333333333333333 | 1 | Medio, fallos de advertencia normativa generica y datos faltantes | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00047.md` |
| `DA-EVAL-00059` | `118-2026-10-007407-00-1` | 0.9333333333333333 | 1 | Medio, coincidencias observables faltantes y datos faltantes ausentes | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00059.md` |
| `DA-EVAL-00067` | `118-2026-10-008011-00-42` | 0.9333333333333333 | 1 | Medio, caso con comparacion clara pero advertencias incompletas | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00067.md` |
| `DA-EVAL-00021` | `118-2026-10-002710-00-3` | 0.8666666666666667 | 1 | Bajo, fallos acumulados: normativa generica, coincidencias y datos faltantes | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00021.md` |
| `DA-EVAL-00053` | `118-2026-10-006732-00-45` | 0.8666666666666667 | 7 | Bajo, conclusion ausente y Top-3 no contiene la NANDINA esperada en rank 1 | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00053.md` |
| `DA-EVAL-00064` | `118-2026-10-008011-00-34` | 1.0 | 2 | NANDINA esperada no rank 1, score alto, sin fallos | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00064.md` |
| `DA-EVAL-00429` | `118-2026-10-120519-00-28` | 1.0 | 7 | NANDINA esperada no rank 1, score alto, contraste con etiqueta esperada rank 7 | `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00429.md` |

## 5. Rubrica cualitativa aplicada

La revision asigno juicios cualitativos breves: `alto`, `medio` o `bajo`.

| Dimension | Pregunta guia |
| --- | --- |
| Claridad para auditor humano | La ficha permite entender rapidamente que mercancia se revisa y cuales son los tres candidatos? |
| Trazabilidad de evidencia | La explicacion conserva ids y fragmentos suficientes para rastrear la evidencia historica y normativa? |
| Pertinencia de coincidencias | Las coincidencias destacadas corresponden a atributos observables relevantes del caso? |
| Utilidad de diferencias/dudas | Las diferencias ayudan a discriminar candidatos y a revisar alternativas? |
| Manejo de incertidumbre | La ficha declara datos faltantes, evidencia generica o soporte bajo cuando corresponde? |
| Suficiencia para revision experta | La ficha reduce trabajo al experto sin reemplazar su juicio? |
| Riesgo de sobreafirmacion | La ficha evita afirmar clasificacion oficial o certeza excesiva? |

## 6. Revision por ficha

### DA-EVAL-00316

- Mercancia: kit de embrague Peugeot, repuesto automotriz metalico.
- Top-3: `87089310`, `87089400`, `87141090`.
- Fortalezas: la ficha separa bien el embrague frente a direccion y partes de motocicletas; cita evidencia historica muy cercana y conserva ids.
- Problemas o ambiguedades: el part number difiere de la evidencia historica, pero esa duda queda solo en el resumen y no se convierte en recomendacion de verificacion. Hay textos normativos truncados, por ejemplo terminan en `u`.
- Sirve para auditoria: si. Es una ficha clara para revisar un caso de alta coincidencia.
- Mejora concreta: agregar un campo visible "verificar part number" cuando el resumen detecta que el numero de parte no coincide exactamente.

### DA-EVAL-00520

- Mercancia: conjunto de junta/bola inferior frontal izquierda Toyota.
- Top-3: `87088010`, `87088090`, `87089921`.
- Fortalezas: el candidato 1 queda bien sustentado por una evidencia historica identica y por una norma especifica de rotulas; los alternativos se explican como genericos o ajenos.
- Problemas o ambiguedades: el candidato 3 se marca con advertencia de "Transmisiones cardanicas" como generica, aunque en realidad parece una diferencia normativa especifica, no una genericidad.
- Sirve para auditoria: si. Es util porque muestra claramente por que el Top-1 es superior.
- Mejora concreta: distinguir entre "normativa generica" y "normativa especifica pero no pertinente".

### DA-EVAL-00778

- Mercancia: guarnicion de bastidor Toyota para automoviles y camionetas.
- Top-3: `87089919`, `87089999`, `87089399`.
- Fortalezas: la ficha muestra coincidencia historica fuerte para el Top-1 y advierte genericidad en codigos residuales de alternativos.
- Problemas o ambiguedades: la frase "la evidencia normativa coincide claramente" es demasiado fuerte porque el texto normativo es "Partes", poco discriminante. La evidencia historica domina la justificacion.
- Sirve para auditoria: si, con cautela. Orienta bien, pero el experto debe revisar si la partida residual es suficiente.
- Mejora concreta: bajar la fuerza del lenguaje cuando la norma sea residual o de tipo "partes/los demas".

### DA-EVAL-00047

- Mercancia: microbus electrico HDK DEL6142K, 14 asientos.
- Top-3: `87024090`, `87031000`, `87046010`.
- Fortalezas: compara tipo de vehiculo, funcion y atributos tecnicos; los alternativos se descartan por uso distinto.
- Problemas o ambiguedades: la ficha dice que `8702.40.90 - Los demas` coincide claramente, pero esa norma es residual. Tambien usa "Electronico" como material/composicion, que no es un material de la mercancia.
- Sirve para auditoria: si, pero requiere lectura critica.
- Mejora concreta: separar energia/propulsion de material; marcar "Los demas" como evidencia normativa de baja especificidad aun cuando el historico sea fuerte.

### DA-EVAL-00059

- Mercancia: SUV Ford Lincoln Navigator, gasolina, 3500 cc, 4x4, 8 asientos.
- Top-3: `87032410`, `87032310`, `87032390`.
- Fortalezas: identifica traccion 4x4 como atributo discriminante y preserva la comparacion Top-3.
- Problemas o ambiguedades: la ficha no explicita con claridad la diferencia clave entre `870324` y `870323`, que parece depender de cilindrada/rango de motor. Se apoya casi solo en traccion 4x4.
- Sirve para auditoria: parcialmente. Ayuda a rastrear evidencia, pero no basta para discriminar codigos cercanos.
- Mejora concreta: exigir que la comparacion de vehiculos incluya cilindrada, combustible y subpartida cuando esos atributos definan la diferencia.

### DA-EVAL-00067

- Mercancia: carretilla electrica para carga a corta distancia, conductor a pie, 300 kg.
- Top-3: `87168090`, `87142000`, `87169000`.
- Fortalezas: las diferencias son utiles: carretilla de carga frente a silla de ruedas y frente a parte/neumatico.
- Problemas o ambiguedades: el Top-1 se declara solo `medio` por diferencias de modelo y potencia, pero la conclusion igual suena suficientemente decisiva. El codigo `87168090` es residual y debe advertirse mejor.
- Sirve para auditoria: si. Es una de las fichas mas utiles para comparar candidatos operativamente.
- Mejora concreta: hacer que la conclusion herede el nivel de soporte; si el soporte es medio, cerrar con "requiere verificacion experta" de forma explicita.

### DA-EVAL-00021

- Mercancia: hatchback electrico Yonsland D21.
- Top-3: `87038090`, `87032290`, `87116000`.
- Fortalezas: la ficha identifica diferencias importantes: modelo distinto, gasolina frente a electrico, trimoto frente a hatchback.
- Problemas o ambiguedades: no registra coincidencias para ningun candidato, aunque existen atributos obvios compartidos como vehiculo de pasajeros/electrico para Top-1. La normativa residual `Los demas` no se advierte. La conclusion dice que el codigo "podria no ser exacto", lo que es honesto, pero faltan instrucciones de revision.
- Sirve para auditoria: si, pero como ficha de alerta, no como soporte suficiente.
- Mejora concreta: obligar al formato a listar al menos una coincidencia y una diferencia por candidato, o justificar explicitamente cuando no haya coincidencias.

### DA-EVAL-00053

- Mercancia: timon/steering wheel assembly para carro de golf electrico o mecanico.
- Top-3: `87082990`, `87082910`, `87085011`.
- Fortalezas: expone que los tres candidatos recuperados no coinciden bien con la mercancia observada.
- Problemas o ambiguedades: no hay conclusion auditable; el "mayor soporte" no tiene motivo. La NANDINA esperada estaba en rank historico 7, por lo que la ficha muestra una falla importante del Top-3, pero no lo senaliza como escalamiento.
- Sirve para auditoria: si, pero principalmente para detectar que el Top-3 no basta.
- Mejora concreta: agregar una decision de escalamiento cuando todos los candidatos tengan soporte bajo o cuando la conclusion quede ausente.

### DA-EVAL-00064

- Mercancia: neumatico de aire de caucho para monociclo electrico.
- Top-3: `87169000`, `87142000`, `87141090`; la NANDINA esperada estaba en rank 2.
- Fortalezas: la ficha explica el Top-1 con evidencia historica de rueda/neumatico y reconoce que el rank 2 se asocia a vehiculos para invalidos.
- Problemas o ambiguedades: como la etiqueta esperada esta en rank 2, la ficha deberia ser mas cautelosa. Declara el Top-1 como mas probable sin resaltar que el rank 2 tiene una relacion normativa funcional fuerte con el monociclo electrico.
- Sirve para auditoria: parcialmente. Es muy util para ver el conflicto, pero no para resolverlo sin experto.
- Mejora concreta: cuando el caso provenga de un estrato rank 2-3, destacar explicitamente que hay disputa entre evidencia historica de parte y contexto funcional de vehiculo.

### DA-EVAL-00429

- Mercancia: servo-embrague para buses, componente hidraulico-neumatico de metal/caucho.
- Top-3: `87089310`, `87089932`, `87089400`; la NANDINA esperada estaba en rank 7.
- Fortalezas: la ficha compara embrague, sistema hidraulico y direccion de forma comprensible.
- Problemas o ambiguedades: el Top-1 se afirma como mejor codigo aunque la etiqueta esperada de muestra estaba en rank 7 (`87089399`). La ficha no advierte que el Top-3 podria estar incompleto para auditoria.
- Sirve para auditoria: parcialmente. Ayuda a revisar el Top-3 recibido, pero no detecta por si sola que puede faltar el candidato esperado.
- Mejora concreta: incluir un indicador externo al LLM para revision humana: "NANDINA esperada fuera del Top-3" o "caso de recuperacion insuficiente", sin enviar esa etiqueta al LLM.

## 7. Hallazgos transversales

### Que funciona bien

- La estructura de ficha es util: identificacion, mercancia, Top-3, respuesta, evidencia citada y controles.
- La trazabilidad formal es fuerte: cada candidato conserva evidencia historica y normativa con ids.
- La ficha ayuda a auditar preservacion del ranking y evita ocultar que el LLM no recupera ni reordena.
- Las diferencias entre candidatos son, en general, mas utiles que las coincidencias para detectar casos de bajo soporte.

### Debilidades repetidas

- La evidencia normativa residual (`Los demas`, `Partes`) a veces se trata como si fuera soporte sustantivo.
- En vehiculos con subpartidas cercanas, la comparacion puede omitir el atributo juridicamente decisivo, por ejemplo cilindrada o tipo exacto de propulsion.
- Las advertencias de datos faltantes no siempre aparecen aunque el caso las necesita.
- Hay casos donde la conclusion usa lenguaje demasiado decisivo en comparacion con el soporte declarado.
- Algunos textos de ficha muestran problemas de codificacion heredados de 10B; eso no impide auditar, pero reduce legibilidad.

### Comparacion de candidatos

Las fichas si ayudan a comparar candidatos cuando los alternativos son semanticamente distintos. Funcionan bien en casos como carretilla frente a silla de ruedas o parte/neumatico. Funcionan peor cuando las subpartidas son cercanas y dependen de atributos normativos finos.

### Evidencia normativa

La evidencia normativa es suficiente como ancla de trazabilidad, pero a menudo es demasiado generica para sostener una decision cualitativa. Conviene que el formato distinga tres situaciones: norma especifica y pertinente, norma especifica pero no pertinente, y norma residual/generica.

### Peso de la evidencia historica

La evidencia historica domina la explicacion. Esto es coherente con la metodologia de 10B, pero el informe de tesis debe aclarar que el LLM explica el ranking historico, no produce una verdad juridica independiente.

### Formato de ficha

El formato es funcional, pero necesita pequenas mejoras para auditoria humana: un bloque de "alertas de revision", una conclusion calibrada por soporte, y una advertencia visible cuando todos los candidatos son debiles o cuando la evidencia normativa es residual.

## 8. Decision

Fase 10B es suficiente como evidencia de explicacion auditable estructural: demuestra que el pipeline puede generar fichas trazables, con Top-3 preservado, evidencia citada y comparacion legible sin usar al LLM como clasificador ni re-ranker.

Sin embargo, para presentar utilidad real de auditoria humana se recomienda una Fase 10D acotada de mejora de formato/rubrica/prompt, sin generacion masiva. La 10D deberia enfocarse en:

- alertas de normativa generica;
- conclusion calibrada por nivel de soporte;
- campos obligatorios de atributos decisivos por tipo de mercancia;
- senal de escalamiento cuando todos los candidatos tienen soporte bajo;
- senal metodologica externa cuando la etiqueta esperada queda fuera del Top-3, sin exponerla al LLM.

## 9. Recomendacion para la tesis

En resultados, presentar 10B como una prueba de explicabilidad auditable sobre una muestra controlada de 50 casos, no como una evaluacion masiva ni como validacion juridica final. La evidencia cuantitativa debe ir junto con esta revision cualitativa corta: las metricas muestran cumplimiento estructural, mientras que la revision humana identifica utilidad, limites y mejoras.

Debe explicarse que no se hizo generacion masiva porque el objetivo metodologico era evaluar la utilidad de fichas auditables, no maximizar volumen de respuestas LLM. La decision protege reproducibilidad, costo, control experimental y coherencia con el rol definido del LLM: explicar candidatos recuperados, no clasificar desde cero.

La fase puede vincularse con antecedentes de explicabilidad en clasificacion aduanera como evidencia de un enfoque human-in-the-loop: el sistema recupera precedentes y evidencia normativa, el LLM organiza una explicacion trazable, y la decision final permanece en revision experta.
