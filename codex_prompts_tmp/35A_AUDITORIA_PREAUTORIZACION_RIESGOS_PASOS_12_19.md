# PROMPT 35A — AUDITORÍA PREAUTORIZACIÓN DE RIESGOS PASOS 12–19

## Supersesión

Este bloque **REEMPLAZA TEMPORALMENTE** al Prompt35 ya creado. **NO ejecutes Prompt35 todavía.** Primero debe completarse y auditarse externamente este Prompt35A.

## Rol

Actúa como **auditor técnico preautorización**. El objetivo es intentar detectar y anular, antes de construir v0.5 o autorizar Attempt06, todos los riesgos previsibles de fallo de los pasos 12–19 del pipeline 0B-05C.

Este bloque es exclusivamente de diagnóstico, shadow validation y pruebas en memoria/tempdir.

**NO:**
- modifiques `main`;
- construyas v0.5;
- crees authorization record nuevo;
- autorices Attempt06;
- ejecutes Attempt05 ni Attempt06;
- hagas retry/resume;
- instales, actualices o desinstales paquetes;
- ejecutes retrieval científico, EV03 real, EV04 real, D1a real ni EVAL real;
- reutilices outputs parciales de Attempt05 como inputs científicos;
- publiques corpus, índices, rankings o métricas runtime parciales.

Los outputs parciales de Attempt05 pueden leerse **solo como evidencia diagnóstica** para demostrar si la lógica downstream de los pasos 13–15 aceptaría estructuralmente esos artefactos. Clasificación obligatoria: `DIAGNOSTIC_ONLY / NOT_SCIENTIFIC_RESULT / NEVER_REUSED_FOR_ATTEMPT06`.

---

# 1. Estado de entrada

Repositorio: `elVladdi/gci-nandina-rag`

`main` esperado:
`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Evidencia audit-only de Attempt05:
- rama: `codex/0b05c-attempt05-failclosed-evidence-env-diagnosis`
- commit: `5144bbdfc3b36e6172ecdd604a3e71d256ab248b`
- parent: `812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Commit local bruto reportado de Attempt05, si continúa disponible:
`525261c0d25d8286e25b1f618655115719540c8b`

Refs protegidas:
- Plan: `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article: `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Verifica primero que `main`, Plan y Article siguen exactos y que Attempt05 no fue reejecutado.

---

# 2. Objetivo metodológico

Para cada paso 12–19 clasifica todos los riesgos identificados en exactamente una de estas categorías:

1. `ELIMINATED_BY_PREAUTH_VERIFICATION`
2. `REDUCED_BY_PREAUTH_VERIFICATION`
3. `RESIDUAL_RUNTIME_RISK_CANNOT_BE_ELIMINATED_PREAUTH`
4. `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05`

Para cada riesgo registra:
- `risk_id`;
- paso;
- mecanismo de fallo;
- evidencia estática;
- prueba/probe realizado;
- resultado;
- categoría final;
- mitigación si no puede eliminarse;
- si debe convertirse en gate obligatorio de v0.5.

No concluyas `READY_FOR_ATTEMPT06`. El máximo estado de este bloque es:
`PREAUTH_RISK_AUDIT_COMPLETED / V05_NOT_BUILT / ATTEMPT06_NOT_AUTHORIZED`.

---

# 3. PASO 12 — D1a: auditoría exhaustiva antes de autorización

Este es el riesgo principal.

## 3.1 Dependencias realmente necesarias

No uses `requirements.txt` ciegamente como lista de blockers. Distingue:
- dependencias declaradas;
- imports directos de builder/evaluator;
- dependencias transitivas necesarias para que esos módulos importen y para cargar/usar `SentenceTransformer`;
- dependencias declaradas pero fuera del path D1a actual.

En particular, verifica estáticamente que el path actual usa exact brute-force y `hnsw=false`; no clasifiques `hnswlib` como blocker salvo evidencia de import/uso real en este path.

## 3.2 Descubrimiento read-only de intérpretes existentes

Sin instalar nada, inventaría intérpretes Python preexistentes razonablemente vinculados al proyecto o al usuario:
- `sys.executable` actual;
- `.venv`, `venv`, `env` dentro del proyecto si existen;
- entornos Conda visibles si existen;
- runtimes/cache de Codex ya existentes;
- otros Python encontrados mediante mecanismos del SO (`where python`, `py -0p`, etc.).

No hagas búsqueda ilimitada de todo el disco.

Para cada intérprete candidato registra sin exponer rutas absolutas en el artefacto público:
- identificador sanitizado;
- versión Python;
- SHA-256 del ejecutable si es práctico;
- import PASS/FAIL de `numpy`, `sentence_transformers`, `torch`, `tqdm` y cualquier otra dependencia que el import real revele;
- import directo PASS/FAIL de:
  - `src.experiments.build_text2trade_mnrl_index_v02`
  - `src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02`.

El reporte administrativo puede contener la ruta local exacta; el artefacto audit-only público no.

## 3.3 Modelo congelado: verificar el directorio completo

No basta `model.safetensors`.

Usa como referencia el manifest histórico versionado en:
`data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json`

Verifica read-only todos los archivos del modelo que ese manifest gobierna:
- path relativo;
- tamaño;
- SHA-256.

Registra missing/mismatch/extra por separado. Un extra no es blocker salvo que pueda alterar la carga; justifícalo.

## 3.4 Smoke test offline del modelo — solo si existe un intérprete que pasa imports

Con:
- `HF_HUB_OFFLINE=1`
- `TRANSFORMERS_OFFLINE=1`
- el mismo intérprete candidato
- el modelo local congelado
- `device=cpu`
- `max_seq_length=128`

haz exclusivamente:
1. carga real `SentenceTransformer(local_model_dir)`;
2. encode de un conjunto **sintético/no científico** de 32 strings triviales;
3. `batch_size=32`;
4. `convert_to_numpy=True`;
5. `normalize_embeddings=True`.

Verifica:
- carga sin red;
- shape `(32, 384)`;
- dtype convertible/estable a `float32`;
- todos los valores finitos;
- normas aproximadamente 1 dentro del criterio numérico propio de float32, sin convertir esto en resultado científico.

No uses descripciones EVAL ni corpus real en este smoke test.

Si ningún intérprete pasa imports, **no hagas smoke test** y clasifica environment como blocker real.

## 3.5 Inputs y patch contract D1a

Read-only/in-memory/tempdir:
- verifica SHA de corpus original y EVAL;
- verifica N=1056 y case_id únicos;
- deriva el corpus Decision906 en memoria/tempdir con el patch contractual;
- verifica 7644 documentos NANDINA-8 únicos;
- exactamente dos documentos cambiados;
- orden y cardinalidad preservados;
- resto de documentos idénticos bajo el contrato previsto;
- deriva config runtime en memoria/tempdir y comprueba que solo cambien los cuatro campos permitidos.

No construyas embeddings del corpus real.

## 3.6 Recursos del host

Registra read-only:
- espacio libre en el volumen del checkout;
- memoria RAM disponible si puede obtenerse sin instalar paquetes;
- tamaño observado de los outputs parciales de Attempt05;
- tamaños históricos del índice/evaluación D1a.

Deriva un margen de seguridad razonado para Attempt06. No inventes un umbral sin justificarlo.

Clasifica fallos de capacidad como `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` cuando corresponda.

---

# 4. PASO 13 — Integrity validation

Si el commit local bruto `525261c...` está disponible, inspecciona **read-only** los partial roots de Attempt05 y reproduce exactamente las condiciones del `integrity()` actual para EV03/EV04, sin escribir dentro de esos roots.

Además verifica los hashes de esos archivos contra el inventory del execution record donde estén disponibles.

Resultado esperado de esta auditoría:
- demostrar si el paso 13 habría aceptado los outputs EV03/EV04 ya producidos;
- identificar cualquier riesgo no cubierto por simple existencia de archivos.

No promociones esos outputs a resultados científicos.

---

# 5. PASO 14 — Case-level comparisons

Usa las funciones actuales de comparación sobre los outputs parciales EV03/EV04 de Attempt05 **solo en memoria o tempdir**.

Verifica de forma efectiva:
- mismos case_id;
- no duplicados;
- `nandina_ref` estable;
- ranking continuo;
- códigos no vacíos;
- unicidad de códigos EV04;
- schema/order completo;
- construcción completa de las filas de comparación.

No escribas el resultado en los future roots v0.4/v0.5.

Añade controles negativos sintéticos mínimos para demostrar fail-closed ante:
- case_id faltante/extra;
- duplicado;
- rank gap;
- código duplicado EV04;
- `nandina_ref` alterado.

Si los partials no están disponibles, usa frozen original-vs-original como shadow y marca la limitación.

---

# 6. PASO 15 — Aggregate comparisons

Con los mismos partials EV03/EV04, ejecuta en memoria/tempdir el aggregate comparison actual.

EV04 debe demostrar:
- schema canónico 92 keys;
- metric_table 27;
- aggregate 28;
- orden exacto;
- contribución `mrr_101_200_contribution` presente en tercera posición;
- denominadores válidos;
- valores finitos.

Añade controles negativos sintéticos para missing/extra metric, reordenamiento, denominador distinto y NaN/Inf.

Clasifica si el riesgo del paso 15 queda efectivamente eliminado para EV03/EV04 a partir de los outputs ya observados.

---

# 7. PASO 16 — Unified sensitivity summary

No requiere retrieval nuevo. Prueba la función actual en tempdir/memoria con:
- aggregates EV03/EV04 válidos del shadow anterior;
- un `d1a_summary` sintético estructuralmente válido construido a partir de referencias de los outputs D1a históricos congelados, sin tratarlos como resultado corregido.

Verifica PASS del camino positivo y FAIL ante D1a ausente/malformed.

Distingue:
- riesgo de lógica/schema del paso 16;
- dependencia residual de que el paso 12 produzca un D1a válido.

---

# 8. PASO 17 — Execution manifest

Prueba en tempdir la construcción y serialización del manifest con objetos sintéticos válidos que respeten el schema real.

Verifica:
- serialización JSON;
- autorización/provenance presentes;
- 19-step execution order completo;
- ausencia de referencias a roots v0.4 parciales cuando se proyecte la futura v0.5;
- fail-closed por path preexistente.

No escribas en roots reales.

---

# 9. PASO 18 — Exact hash ledger

Haz una auditoría de cierre de conjunto de outputs, antes de ejecución.

Deriva por dos vías independientes:

A. `EXPECTED_SET`: paths declarados por el ledger contract/specs.

B. `PRODUCER_SET`: todos los archivos que el código de los pasos 1–17 está diseñado para crear en una ejecución exitosa, incluyendo builder/evaluator D1a, comparisons, summary, manifest y runtime authorization record, excluyendo solo el ledger a sí mismo según contrato.

Compara exactamente A vs B y reporta:
- missing in producer;
- unexpected producer outputs;
- path collisions;
- files condicionados solo a fallo (`execution_failed.json`) que no deben existir en success path.

Luego, en tempdir, crea placeholders para el set contractual y ejecuta el validator del ledger:
- exact set => PASS;
- remove one => FAIL;
- add one unexpected => FAIL.

Esto no verifica hashes futuros, pero debe eliminar cualquier inconsistencia de diseño de cardinalidad/nombres antes de Attempt06.

---

# 10. PASO 19 — Final completion state

Ejecuta el `run_authorized_pipeline()` con operaciones **100% sintéticas** y sin side effects científicos:
- 18 pasos válidos + final PASS => PASS;
- cualquier step anterior FAIL => fail-closed;
- falta/reordenamiento de operación => fail-closed;
- final antes de 18 estados => fail-closed.

Clasifica el riesgo residual real de este paso.

---

# 11. Matriz final de riesgo obligatoria

Produce una matriz resumida por pasos 12–19 con:
- riesgo inicial (`HIGH/MEDIUM/LOW`);
- pruebas realizadas;
- evidencia;
- riesgo eliminado sí/no;
- riesgo residual;
- mitigación obligatoria;
- `V05_GATE_REQUIRED = true/false`.

Debe responder explícitamente estas preguntas:

1. ¿Qué riesgos pueden considerarse anulados antes de una ejecución real?
2. ¿Qué riesgos solo pueden reducirse?
3. ¿Qué riesgos son intrínsecamente runtime y no pueden eliminarse por completo?
4. ¿Existe actualmente algún blocker que impida siquiera construir/autorización futura?
5. Si existe blocker ambiental, ¿hay un intérprete preexistente que ya lo resuelva sin instalar nada?
6. ¿Qué controles deben incorporarse obligatoriamente a v0.5 antes de autorizar Attempt06?

No propongas una autorización Attempt06 en este bloque.

---

# 12. Artefacto audit-only

Crea una rama desde `main`:
`codex/0b05c-preauthorization-risk-audit-12-19`

Crea exactamente un artefacto público sanitizado:
`outputs/audits/0b05c_preauthorization_risk_audit_v0.4/preauthorization_risk_audit_steps12_19_v0.4.json`

No debe contener:
- rutas absolutas host-locales;
- corpus/índices/rankings/métricas parciales;
- secretos;
- resultados científicos nuevos.

Sí debe contener:
- classification;
- baseline/ref bindings;
- matriz de riesgos;
- resultados de environment candidates sanitizados;
- model manifest verification;
- smoke status si fue posible;
- diagnostic shadow PASS/FAIL de pasos 13–19;
- residual risk register;
- recomendaciones de mitigación;
- `ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `V05 = NOT_BUILT`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Publica esa rama, pero no la integres a main.

---

# 13. Persistencia administrativa

Después del trabajo, vuelve a `codex/prompts-temporary`, haz `git fetch` y persiste exclusivamente:

`codex_prompts_tmp/35A_RESPUESTA_AUDITORIA_PREAUTORIZACION_RIESGOS_PASOS_12_19.md`

El reporte debe contener el detalle completo, incluidas rutas locales de intérpretes si son necesarias para remediación; el artefacto público debe permanecer sanitizado.

Clasificación de toda prueba local:
`CODEX_LOCAL_PREAUTHORIZATION_RISK_AUDIT / NOT_INDEPENDENT_GITHUB_CI`.

Responde únicamente con el reporte final exigido.
