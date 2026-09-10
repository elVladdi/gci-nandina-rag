# PROMPT 34 — PRESERVAR EVIDENCIA ATTEMPT05 Y DIAGNOSTICAR ENTORNO D1a SIN REEJECUCIÓN

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque consolida dos tareas necesarias después del fallo de Attempt05:

1. preservar en GitHub únicamente la evidencia de auditoría no sensible del fallo ya ocurrido;
2. diagnosticar exhaustivamente, en modo read-only, la preparación del entorno Python para D1a, de modo que una futura autorización no vuelva a consumirse por una dependencia ausente.

**NO ejecutes nuevamente Attempt05. NO hagas retry ni resume. NO ejecutes retrieval, EV03 real, EV04 real, D1a real, EVAL ni inferencia del modelo. NO instales paquetes en este bloque.**

---

## 1. Estado de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main científico esperado:

`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Este commit contiene la autorización v0.4 integrada y debe permanecer sin cambios durante este bloque.

Attempt05 fue reportado por la ejecución local de Prompt33 como:

- comando: `python -B -m src.experiments.run_0b05c_corrective_numerical_v04 --execute-authorized`;
- `invocation_count = 1`;
- `exit_code = 1`;
- error terminal reportado: `ModuleNotFoundError: No module named 'sentence_transformers'`;
- último paso completado reportado: `11_EV04_corrected_evaluation_ENRICHED_MRR`;
- último paso iniciado reportado: `12_D1a_corrected_execution_under_future_v04_authorization`;
- retry/resume reportados: 0/0;
- commit local de resultado reportado: `525261c0d25d8286e25b1f618655115719540c8b`;
- parent local reportado: `812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`;
- rama local reportada: `codex/0b05c-v04-attempt05-execution-result`;
- la rama de resultado completa NO fue publicada por bloqueo de seguridad del host.

Plan esperado:

`fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Article esperado:

`254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de escribir verifica:

- `origin/main == 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`;
- Plan/article en los heads indicados;
- no existe una rama remota `codex/0b05c-v04-attempt05-execution-result`;
- no vuelvas a invocar el pipeline bajo ninguna circunstancia.

Si el commit local `525261c...` y los archivos locales de evidencia ya no son recuperables, **STOP / EVIDENCE_LOCAL_STATE_UNAVAILABLE**. No reconstruyas, no inventes y no reejecutes.

---

## 2. Preservación segura de evidencia — NO publicar outputs potencialmente sensibles

El repositorio remoto es público. No publiques en este bloque los 26 outputs generados dentro de los future roots, corpus derivados, índices, rankings ni métricas runtime.

Crea desde `main = 812cb69...` una rama nueva:

`codex/0b05c-attempt05-failclosed-evidence-env-diagnosis`

Recupera del commit local `525261c...` o del working tree de Prompt33, **sin modificar contenido**, únicamente:

1. `outputs/audits/0b05c_attempt05_execution_v0.4/attempt05_execution_record_v0.4.json`
2. `outputs/audits/0b05c_attempt05_execution_v0.4/attempt05_stdout.txt`
3. `outputs/audits/0b05c_attempt05_execution_v0.4/attempt05_stderr.txt`

Antes de commitear:

- verifica SHA-256 y tamaños contra lo reportado en Prompt33:
  - execution record: SHA-256 `4ab2d26c1dbfdb0cb4bff620db079e123fff9db1a5935343459ce7b5eea4eceb`, 13064 bytes;
  - stdout: SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, 0 bytes;
  - stderr: SHA-256 `2c28ad49f530ef7a77b2c72a9ecfada3442969337dd6542cf2c46360c7620e4a`, 2705 bytes.
- si cualquiera no coincide: `STOP / EVIDENCE_HASH_MISMATCH`.

No copies ningún otro archivo del commit local de resultado.

El commit local completo `525261c...` debe preservarse localmente como evidencia bruta si todavía existe, pero **no se publica** en este bloque.

---

## 3. Diagnóstico ambiental read-only obligatorio

La auditoría externa ha identificado estáticamente que:

- `requirements.txt` declara `sentence-transformers`;
- `src/experiments/build_text2trade_mnrl_index_v02.py` contiene `from sentence_transformers import SentenceTransformer` a nivel de módulo;
- `run_d1a_corrective_0b05c_v04.py:execute_authorized()` lanza ese builder mediante subprocess durante D1a;
- el preflight v0.4 validaba archivos/bindings/modelo pero no probaba la disponibilidad importable de la dependencia runtime.

Verifica esto directamente desde el checkout y persiste un diagnóstico factual.

### 3.1 Probe del intérprete

Registra:

- `sys.executable`;
- `sys.version`;
- plataforma;
- `python -m pip --version`;
- hash SHA-256 del `requirements.txt` versionado.

### 3.2 Probe de dependencias sin instalación

Usa el MISMO intérprete `python` que se usaría para el runner y prueba, sin instalar nada, la importabilidad de todas las dependencias de `requirements.txt` mediante este mapa explícito:

- `numpy` -> `numpy`
- `pandas` -> `pandas`
- `pdfplumber` -> `pdfplumber`
- `pypdf` -> `pypdf`
- `tqdm` -> `tqdm`
- `sentence-transformers` -> `sentence_transformers`
- `hnswlib` -> `hnswlib`
- `torch` -> `torch`
- `openpyxl` -> `openpyxl`

Para cada una registra:

- import PASS/FAIL;
- versión cuando sea accesible sin side effects;
- módulo path cuando sea accesible;
- excepción exacta si falla.

### 3.3 Probe de los dos módulos reales D1a

Ejecuta exclusivamente imports read-only en subprocess separados:

`python -B -c "import src.experiments.build_text2trade_mnrl_index_v02"`

`python -B -c "import src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02"`

Captura exit code y stderr. No llames `main()` de esos módulos.

### 3.4 Cierre causal

Solo si la evidencia lo soporta, clasifica:

`ATTEMPT05_FAILURE_CLASS = MISSING_RUNTIME_PYTHON_DEPENDENCY`

No atribuyas todavía causa a una versión específica ni instales/cambies paquetes.

Distingue explícitamente:

- `requirements_declared_dependency`;
- `runtime_import_available`;
- `module_import_available`.

La mera presencia en `requirements.txt` no equivale a paquete instalado.

---

## 4. Contrato de readiness para un futuro Attempt06

Sin crear aún v0.5, Attempt06 ni una nueva autorización, define en el diagnóstico un **ENVIRONMENT_READINESS_CONTRACT** que deberá pasar antes de cualquier futura autorización:

1. mismo intérprete identificado por `sys.executable` para probe, preflight y ejecución;
2. todas las dependencias runtime requeridas por D1a importables;
3. import directo de `build_text2trade_mnrl_index_v02` = PASS;
4. import directo de `evaluate_text2trade_mnrl_data_aduanas_v02` = PASS;
5. frozen model exacto presente, tamaño y SHA-256 correctos;
6. todos los bindings Git del futuro runner/gate exactos;
7. roots del nuevo intento ausentes en un worktree limpio;
8. environment probe ejecutado **antes** de integrar cualquier nueva autorización;
9. si cualquier import falla, autorización NO debe integrarse;
10. registrar versiones reales del entorno que finalmente pase.

Esto corrige el defecto de proceso que permitió que Prompt33 consumiera una autorización aunque faltaba una dependencia declarada.

---

## 5. Artefacto de diagnóstico

Crea exactamente:

`outputs/audits/0b05c_attempt05_environment_diagnosis_v0.4/attempt05_environment_diagnosis_v0.4.json`

Debe contener:

- identidad de main/authorization commit;
- referencia al execution record y sus hashes;
- clasificación probatoria: `CODEX_LOCAL_READ_ONLY_ENVIRONMENT_DIAGNOSIS / NOT_INDEPENDENT_GITHUB_CI`;
- evidencia estática de imports y requirements;
- interpreter/environment probe;
- tabla de dependencias;
- resultados de imports de los dos módulos D1a;
- failure class, solo si demostrada;
- `ENVIRONMENT_READINESS_CONTRACT`;
- `ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED`;
- `ATTEMPT05_RETRY = FORBIDDEN`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

No agregues datos brutos de los 26 outputs; solo referencias/hashes ya presentes en el execution record.

---

## 6. Alcance del candidato

El candidato debe contener exactamente **4 paths nuevos** respecto de main:

1. execution record;
2. stdout;
3. stderr;
4. diagnosis JSON.

No modificar:

- main;
- gate/specs/autorización v0.4;
- código/tests;
- Plan/article;
- EXP11B/EXP12;
- outputs runtime generados por Attempt05.

No instalar dependencias. No limpiar ni reutilizar partial roots. No ejecutar Attempt05.

Produce un único commit candidato y publica únicamente:

`codex/0b05c-attempt05-failclosed-evidence-env-diagnosis`

---

## 7. Reporte obligatorio

Persiste en `codex/prompts-temporary`:

`codex_prompts_tmp/34_RESPUESTA_PRESERVAR_EVIDENCIA_ATTEMPT05_Y_DIAGNOSTICAR_ENTORNO_D1A.md`

Incluye:

- main y refs protegidas;
- disponibilidad del commit local `525261c...`;
- branch/commit/tree/parent del candidato audit-only;
- 4 paths y blobs;
- verificación de hashes de execution record/stdout/stderr;
- resultado completo del dependency/import probe;
- failure class resultante;
- confirmación de que no se instaló nada;
- confirmación de que no se publicaron corpus/índices/métricas runtime;
- confirmación `Attempt05` no fue reejecutado;
- `ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Responde únicamente con el reporte final exigido.
