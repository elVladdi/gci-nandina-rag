# REGLA METODOLÓGICA PERMANENTE — REVISIÓN PREVENTIVA DE RIESGOS DE EJECUCIÓN (RPRE)

## 0. Propósito

Esta regla formaliza, para todo el trabajo experimental futuro del proyecto **Tesis San Marcos / gci-nandina-rag**, la estrategia que permitió reducir el riesgo antes de ejecuciones oficiales costosas como `Attempt06`.

Su objetivo es evitar consumir una autorización experimental, un intento `one-shot`, tiempo de cómputo o una cadena posterior de correcciones por fallos que podían haberse detectado razonablemente antes de la ejecución oficial.

Principio rector:

> **Antes de cualquier ejecución científica oficial, one-shot, costosa o que consuma una autorización, todo riesgo razonablemente detectable sin ejecutar el experimento oficial debe identificarse, verificarse y cerrarse previamente.**

La RPRE es una regla metodológica permanente. No depende del número de prompt, del chat activo ni del experimento concreto.

---

# 1. Relación con la gobernanza existente

La RPRE no sustituye la cadena de autoridad del proyecto:

`USUARIO → CODEX ejecuta → CODEX versiona evidencia/reporte → IA EXPERIMENTAL audita independientemente → recién después se aprueba/rechaza/continúa`

Tampoco convierte un preflight en una ejecución oficial.

Deben permanecer siempre separados:

`PREFLIGHT / SHADOW / DRY-RUN / STATIC CHECK ≠ OFFICIAL EXECUTION`

`RPRE_PASS ≠ EXECUTION_AUTHORIZED`

`EXECUTION_AUTHORIZED ≠ EXECUTED`

`EXECUTED ≠ APPROVED`

La RPRE es un **gate preventivo previo**. La autorización y la ejecución oficial conservan las reglas específicas del bloque experimental correspondiente.

## 1.1 Regla de transparencia hacia Codex

La RPRE es una **regla interna de gestión de IA Experimental**.

Por tanto:

- el usuario **no debe recibir ni reenviar a Codex un prompt separado denominado RPRE**;
- Codex **no necesita conocer que existe una regla llamada RPRE**;
- IA Experimental debe aplicar la RPRE internamente al diseñar el siguiente bloque operativo;
- si para cerrar riesgos hacen falta checks técnicos, IA Experimental los incorpora de manera natural dentro del prompt técnico que ya corresponda ejecutar;
- Codex solo ve y ejecuta las instrucciones técnicas concretas del bloque que IA Experimental le entregue;
- la existencia, evaluación y estado de la RPRE son responsabilidad de IA Experimental, no de Codex;
- no se debe crear interacción adicional con el usuario solo para comunicar que la RPRE existe.

En términos operativos:

`RPRE = REGLA INTERNA DE IA EXPERIMENTAL`

`CODEX = EJECUTOR DE CHECKS/ACCIONES QUE IA EXPERIMENTAL HAYA INCORPORADO EN EL PROMPT OPERATIVO`

`USUARIO = NO NECESITA GESTIONAR NI TRANSMITIR LA RPRE`

La regla debe ser **transparente para Codex y para el usuario**, salvo cuando IA Experimental necesite explicar por qué aún no autoriza una ejecución oficial.

---

# 2. Cuándo es obligatoria

IA Experimental debe aplicar la RPRE antes de autorizar un bloque si se cumple **al menos una** de estas condiciones:

1. la ejecución consume una autorización experimental;
2. la ejecución es `one-shot`, `no-retry`, `no-resume` o equivalente;
3. produce resultados científicos oficiales que alimentarán tesis, artículo, métricas o inferencia;
4. ejecuta un número relevante de bancos, seeds, condiciones, modelos, folds, escenarios o replicaciones;
5. usa artefactos congelados cuya alteración o rerun sería metodológicamente costoso;
6. un fallo exigiría nueva autorización, nuevo intento o una cadena correctiva relevante;
7. existe historial previo de fallos o correcciones en la misma familia experimental;
8. IA Experimental determina que el costo de una ejecución fallida justifica una revisión preventiva.

## 2.1 Casos normalmente exentos

No se exige una RPRE completa para tareas puramente administrativas o de bajo riesgo, por ejemplo:

- lectura o auditoría read-only;
- persistencia administrativa de prompts/respuestas;
- integración fast-forward de un candidato ya auditado externamente, si no ejecuta ciencia;
- reconciliación documental mínima del Plan Maestro;
- corrección textual o metadata sin efecto experimental;
- creación de un artefacto de cierre que no ejecuta el experimento.

La exención debe quedar registrada internamente por IA Experimental cuando pueda existir duda:

`RPRE_APPLICABILITY = NOT_REQUIRED / LOW_RISK_NON_EXECUTION_BLOCK`

La exención de un bloque no exime al **siguiente bloque científico oficial**.

---

# 3. Objetivo operativo

La RPRE debe responder, antes de ejecutar oficialmente:

1. ¿Qué puede invalidar el intento?
2. ¿Qué de eso puede detectarse antes de consumir la ejecución oficial?
3. ¿Qué evidencia concreta demuestra que ese riesgo está cerrado?
4. ¿Qué riesgo residual solo puede conocerse durante la ejecución?
5. ¿Existe algún riesgo bloqueante no resuelto?

La meta no es demostrar que el experimento no puede fallar. La meta es impedir que falle por una causa **razonablemente detectable de antemano**.

---

# 4. Dominios mínimos del mapa de riesgo

Para cada ejecución sometida a RPRE, IA Experimental debe revisar como mínimo los siguientes dominios, adaptándolos al experimento concreto.

## 4.1 Git y procedencia

- baseline científico correcto;
- parent/ancestry esperados;
- rama correcta;
- tree/diff/changed paths esperados;
- blobs y bindings correctos;
- ausencia de candidato rechazado o commit no autorizado en la genealogía;
- refs protegidas sin drift.

## 4.2 Inputs congelados

- existencia;
- paths correctos;
- SHA-256 esperados;
- row counts / tamaños / composición cuando gobiernen identidad;
- ausencia de dependencia de archivos locales no gobernados;
- ausencia de leakage, overlap o drift de partición.

## 4.3 Código y configuración

- script/módulo exacto;
- Git blob o hash correcto;
- configuración exacta;
- parámetros congelados;
- seeds/condiciones/folds/bancos correctos;
- reglas de orden/tie-break/normalización/serialización preservadas;
- ausencia de cambios semánticos no auditados.

## 4.4 Entorno de ejecución

- versión/runtime requerido;
- dependencias disponibles;
- imports;
- paths;
- permisos;
- espacio/recursos razonables cuando aplique;
- ausencia de dependencia de internet o estado externo no autorizado;
- working tree limpio cuando corresponda.

## 4.5 Outputs y persistencia

- output root correcto;
- política de directorio vacío/ausente;
- no overwrite silencioso;
- nombres y contratos de archivos;
- atomicidad o comportamiento ante fallo cuando sea relevante;
- separación entre outputs temporales y oficiales.

## 4.6 Semántica de ejecución

- número exacto de invocaciones;
- `retry` permitido/prohibido;
- `resume` permitido/prohibido;
- política ante fallo parcial;
- política ante resultado inesperado;
- prohibición de rerun silencioso;
- criterio inequívoco para consumir la autorización.

## 4.7 Riesgo metodológico

- denominadores congelados;
- población y unidad de análisis;
- agrupamiento/dependencia;
- leakage;
- common-clean o exclusiones;
- cambios de selección;
- alteración de seeds;
- cambios de métrica;
- cualquier condición que pueda cambiar la interpretación científica.

## 4.8 State machine y alcance

- qué está autorizado;
- qué permanece expresamente no autorizado;
- qué bloque se abre o cierra;
- qué no debe ejecutarse de forma colateral;
- ausencia de avance a EXP/grupo posterior;
- ausencia de modificación del Plan/Article salvo autorización explícita.

## 4.9 Reproducibilidad y trazabilidad

- evidencia suficiente para reconstruir la ejecución;
- hashes/manifests/ledgers necesarios;
- versión de código/config/input ligada al resultado;
- distinción entre evidencia Git, CI y observación local de Codex;
- capacidad de auditar posteriormente sin depender de memoria del chat.

---

# 5. Registro de riesgos

La RPRE debe producir un registro explícito para uso de IA Experimental. No es obligatorio exponer ese registro al usuario ni enviarlo a Codex como documento independiente, salvo que sea necesario para trazabilidad o auditoría.

Cada riesgo debe contener al menos:

```text
risk_id
category
failure_mode
why_it_matters
pre_execution_detectability = YES / PARTIAL / NO
preventive_check
evidence
status
blocks_official_execution = true / false
residual_risk
```

## 5.1 Estados permitidos

Cada riesgo debe finalizar en exactamente uno de estos estados:

`CLOSED_PRE_EXECUTION`

Riesgo detectable previamente y cerrado con evidencia suficiente.

`ACCEPTED_RESIDUAL_RISK`

No puede eliminarse razonablemente antes de la ejecución, pero está identificado y su aceptación es explícita. No debe utilizarse para encubrir un riesgo preflight evitable.

`BLOCKING_NOT_RESOLVED`

Existe un riesgo que puede invalidar la ejecución y no ha sido cerrado. Impide autorización oficial.

`NOT_APPLICABLE`

El dominio/riesgo no aplica al bloque, con justificación breve.

---

# 6. Clasificación de prioridad

Para evitar burocracia y hardening ilimitado, prioriza por consecuencia y detectabilidad, no por especulación.

## P0 — Bloqueante y preventivo

Una falla plausible que invalidaría/consumiría el intento y puede detectarse antes de ejecutar oficialmente.

Debe terminar en `CLOSED_PRE_EXECUTION`. Si no, no se autoriza.

## P1 — Alto riesgo residual

Puede afectar la ejecución o interpretación, pero no puede cerrarse totalmente sin ejecutar. Debe quedar explícito como `ACCEPTED_RESIDUAL_RISK` con mitigación y criterio de observación.

## P2 — No bloqueante

Puede generar inconvenientes menores o metadata imperfecta sin invalidar el contrato científico gobernante. Se registra cuando sea útil, pero no debe inflar artificialmente el gate.

No crear riesgos hipotéticos sin una vía causal razonable respaldada por arquitectura, código, datos, entorno o historia del proyecto.

---

# 7. Métodos preventivos permitidos

Antes de la ejecución oficial pueden utilizarse, según corresponda:

- inspección estática de código/config;
- verificación Git de parent/tree/diff/blob;
- validación de hashes y contratos;
- `preflight` read-only;
- `dry-run`;
- `shadow test`;
- ejecución en worktree temporal/detached;
- outputs temporales desechables;
- test vectors;
- comprobaciones de imports/dependencias/paths;
- validación de CLI y argumentos;
- CI o checks locales claramente clasificados;
- reproducción controlada de pasos que **no produzcan resultados oficiales**.

Estas acciones deben diseñarse para detectar fallos sin consumir el intento oficial ni contaminar outputs oficiales.

Si una prueba preventiva produce datos similares a los que produciría la ejecución oficial, deben permanecer inequívocamente etiquetados como temporales/no oficiales y no utilizarse como resultados científicos salvo autorización posterior específica.

---

# 8. Regla de no contaminación

Una RPRE no puede:

- observar resultados oficiales antes de la autorización cuando ello introduciría sesgo de decisión;
- cambiar parámetros por haber visto resultados;
- generar métricas científicas oficiales si aún no están autorizadas;
- escribir sobre outputs oficiales;
- rematerializar artefactos congelados in-place salvo autorización explícita;
- modificar inputs, seeds, particiones o código para “hacer pasar” el gate;
- convertir un shadow run en la ejecución oficial retrospectivamente.

El preflight debe validar **capacidad de ejecución**, no anticipar y optimizar el resultado científico.

---

# 9. Criterio de PASS de la RPRE

Solo puede declararse internamente:

```text
PRE_EXECUTION_RISK_REVIEW = PASS
BLOCKING_RISK_COUNT = 0
```

cuando:

1. todos los P0 relevantes están en `CLOSED_PRE_EXECUTION`;
2. no existe `BLOCKING_NOT_RESOLVED`;
3. los P1 residuales están explícitamente documentados y aceptados;
4. no se detectó drift de inputs/config/código/baseline;
5. el método oficial y sus prohibiciones están inequívocamente definidos;
6. la evidencia preventiva está suficientemente versionada o trazable para auditoría;
7. no se ejecutó accidentalmente el experimento oficial durante el preflight.

Si no se cumple:

```text
PRE_EXECUTION_RISK_REVIEW = FAIL / BLOCKED
OFFICIAL_EXECUTION = NOT_AUTHORIZED
```

IA Experimental no debe trasladar este estado como una tarea adicional al usuario; simplemente no debe emitir todavía el prompt que autorice la ejecución oficial.

---

# 10. Eficiencia: evitar idas y venidas innecesarias

La RPRE existe para **reducir** ciclos, no para crear una nueva cadena burocrática.

Por defecto:

1. IA Experimental consolida internamente en **un único mapa preventivo** todos los riesgos previsibles relevantes;
2. cuando necesita comprobaciones técnicas de Codex, las incorpora en el prompt operativo normal que corresponda, sin convertir la RPRE en una tarea separada para el usuario;
3. Codex ejecuta únicamente esas comprobaciones técnicas concretas, sin necesidad de gestionar ni conocer la regla metodológica RPRE;
4. IA Experimental audita el paquete completo;
5. solo si aparece un hallazgo bloqueante concreto se crea un bloque correctivo;
6. no se fragmenta un mismo mapa de riesgo en múltiples prompts sin necesidad técnica.

Cuando sea seguro y compatible con la gobernanza, la RPRE puede resolverse íntegramente mediante auditoría de IA Experimental y checks ya disponibles, sin enviar ninguna instrucción adicional a Codex.

Para ejecuciones `one-shot` o de alto costo, la autorización oficial solo puede emitirse **después** de que IA Experimental haya concluido internamente que la RPRE está en PASS.

---

# 11. Regla anti-hardening infinito

La RPRE termina cuando se han cerrado los riesgos razonablemente previsibles que podrían invalidar el intento.

No debe utilizarse para:

- refactorizar código por estética;
- mejorar arquitectura no relacionada;
- perseguir riesgo cero;
- abrir deudas técnicas marginales sin relación causal con el intento;
- repetir checks ya cerrados sin evidencia nueva;
- postergar indefinidamente una ejecución por riesgos puramente especulativos.

Criterio de suficiencia:

> **Si no queda ningún riesgo bloqueante razonablemente detectable antes de la ejecución y los riesgos residuales están explícitos, la revisión preventiva debe cerrarse.**

---

# 12. Regla post-mortem

Si una ejecución oficial falla, IA Experimental debe clasificar la causa:

`PREVENTABLE_PRE_EXECUTION`

La causa podía haberse detectado razonablemente con la RPRE. Debe incorporarse como nueva verificación obligatoria para futuras ejecuciones similares.

`NON_PREVENTABLE_RUNTIME`

La causa solo podía conocerse durante la ejecución o era razonablemente imprevisible. No constituye incumplimiento de la RPRE.

`PROCESS_OR_SCOPE_VIOLATION`

La ejecución incumplió el contrato, la autorización o las prohibiciones.

La RPRE evoluciona con evidencia real del proyecto, no con especulación.

---

# 13. Aplicación inmediata a EXP11B

La integración/cierre documental de la deuda de portabilidad puede tratarse como bloque no científico de bajo riesgo si se limita estrictamente a integración auditada y reconciliación documental.

Sin embargo, **antes de que IA Experimental emita una autorización oficial de EXP11B Retrieval H150/H200**, debe completar internamente una RPRE específica para ese retrieval.

Como mínimo debe cubrir:

- identidad de los 20 bancos;
- disponibilidad read-only de los bancos oficiales;
- bindings exactos de BM25/config/evaluator;
- H100/EVAL y denominador congelado;
- seeds/condiciones/orden;
- output root oficial ausente/vacío según contrato;
- one-shot semantics;
- no retry/no resume/no overwrite;
- entorno y dependencias;
- ausencia de drift desde el gate ya integrado;
- ausencia de autorización de EXP12/Grupo 2B;
- trazabilidad de cada una de las 20 ejecuciones y consolidación final.

Hasta que IA Experimental concluya que esa RPRE está en PASS:

`EXP11B_RETRIEVAL_H150_H200 = NOT_AUTHORIZED / NOT_EXECUTED`

Esto **no crea un prompt adicional para Codex**. La RPRE se gestiona por IA Experimental; cualquier check técnico necesario se incorporará de forma transparente en el bloque operativo que corresponda.

---

# 14. Persistencia y continuidad

Esta regla debe ser leída y aplicada por cualquier futura IA Experimental durante su onboarding.

El prompt maestro de continuidad debe referenciarla expresamente y además contener:

- su principio rector;
- triggers;
- estados;
- criterio de PASS;
- la regla de que RPRE es gestión interna de IA Experimental y no una tarea que el usuario deba reenviar a Codex.

Archivo canónico administrativo de esta regla:

`codex_prompts_tmp/00_REGLA_REVISION_PREVENTIVA_RIESGOS_EJECUCION.md`
