# PROMPT 35C — CORREGIR v0.5: CONTRATO D1a + LEDGER REAL + TRANSICIÓN DE AUTORIZACIÓN + HARDENING FINAL

## Rol y objetivo

Actúa como **ejecutor técnico controlado**. Este bloque corrige en una sola pasada el candidato v0.5 de Prompt35B después de auditoría externa independiente.

El candidato Prompt35B `a3d4c7b6067e1ed6ac10606a9c2a8ab46336bfda` queda **REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED**. NO lo integres a `main` ni lo uses como parent del candidato corregido.

Este bloque debe producir un candidato v0.5 limpio, con parent directo del `main` actual, corrigiendo conjuntamente todos los hallazgos F35C-01 a F35C-06.

**NO autorices ni ejecutes Attempt06. NO reejecutes Attempt05. NO ejecutes retrieval científico, EV03 real, EV04 real, D1a completo ni EVAL real. NO instales/actualices dependencias.**

---

# 1. Estado obligatorio de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main esperado:

`c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`

Este main ya contiene exclusivamente la integración auditada de Prompt35A sobre `812cb69...`.

Candidato Prompt35B rechazado, solo como fuente de trabajo a corregir:

- rama: `codex/0b05c-v05-remediated-preauthorization-candidate`
- commit: `a3d4c7b6067e1ed6ac10606a9c2a8ab46336bfda`
- parent: `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`
- tree: `8a48c32ba4c6ce21ba4ac941cad3d1ac064f9981`

Refs protegidas:

- Plan: `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article: `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de editar:

1. `git fetch`;
2. verifica `origin/main == c873ff1...`;
3. verifica Prompt35B candidate exacto pero NO lo integres;
4. verifica Plan/Article exactos;
5. verifica working tree tracked limpio;
6. verifica que no exista authorization record v0.5 en `main`;
7. verifica Attempt06 `NOT_AUTHORIZED / NOT_EXECUTED`;
8. no uses outputs parciales Attempt05 como inputs científicos.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Rama corregida y estrategia de historia

Crea desde `main = c873ff1...`:

`codex/0b05c-v05-remediated-preauthorization-candidate-v2`

Puedes recuperar el contenido útil de `a3d4c7b...` al working tree/index **sin introducir ese commit como ancestro** y luego corregirlo.

El candidato final debe tener:

- un único commit técnico/científico;
- parent directo `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`;
- ningún merge commit;
- ningún authorization record v0.5;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`.

Preserva las correcciones válidas de Prompt35B: fail-close sanitizado Attempt05, environment gate, 9-file model manifest, smoke offline, 21-vector replay opcional-fuerte, EV03 empty ranking contract, finitud, summary estricto, manifest/ledger/orchestration hardening; corrige lo indicado a continuación.

---

# 3. F35C-01 — D1a v0.5 tiene tres contratos de filenames incompatibles

La auditoría externa confirmó un blocker determinista.

Actualmente el spec v0.5 conserva en `runner_outputs` filenames `...v0.4.*`, el unified ledger espera filenames `...v0.5.*`, mientras `legacy.expected_paths()` de `run_d1a_corrective_0b05c_v01.py` usa constantes `RUNNER_FILENAMES` `...v0.1.*`.

Además el spec v0.5 cambia el path del runner a `run_d1a_corrective_0b05c_v05.py` pero conserva el Git blob SHA-1/canonical SHA-256 del runner v0.4. También los `specification_id` EV03/EV04/D1a siguen marcados `v0.4`.

## Corrección obligatoria

No modifiques `run_d1a_corrective_0b05c_v01.py` ni otros componentes históricos.

Implementa en la frontera D1a v0.5 un contrato propio de outputs v0.5. Debe existir una única autoridad para los cuatro runner outputs:

- `d1a_corrective_vs_original_comparison_v0.5.json`
- `d1a_corrective_case_level_comparison_v0.5.jsonl`
- `d1a_corrective_output_hash_ledger_v0.5.csv`
- `d1a_corrective_execution_manifest_v0.5.json`

La ejecución D1a v0.5 debe escribir exactamente esos nombres, no los v0.1 ni v0.4.

Obligatorio:

1. `specification_id` exactos v0.5 para EV03, EV04 y D1a;
2. `runner_outputs` D1a exactos v0.5;
3. `hash_ledger_contract.included_paths`/`excluded_self_path` D1a exactos v0.5;
4. binding del runner D1a al **blob real del nuevo archivo v0.5**, no al blob v0.4;
5. binding canónico de cualquier nuevo source v0.5 debe derivarse de bytes Git INDEX/staged o equivalente canónico, no de bytes CRLF ambiguos del checkout;
6. el adapter v0.5 debe dejar de depender de los hard-coded `RUNNER_FILENAMES` v0.1 para los outputs propios del runner;
7. `common._d1a_summary_reference` o su wrapper v0.5 debe resolver exactamente los outputs v0.5 del spec.

Crea una prueba contractual explícita:

`D1A_SPEC_RUNNER_SET == D1A_ACTUAL_PRODUCER_SET == UNIFIED_LEDGER_D1A_RUNNER_SUBSET`

Debe PASS por igualdad exacta. Muta un nombre en cada lado y demuestra FAIL_CLOSED.

Prueba también que el propio D1a hash-ledger contract coincide exactamente con los paths realmente producidos por el adapter v0.5 **sin ejecutar D1a científico**.

---

# 4. F35C-02 — PRODUCER_SET no fue derivado independientemente y el ledger no detecta archivos extra reales

El candidato rechazado construye `producer_runtime_paths()` empezando desde:

`gate["runtime_hash_ledger_contract"]["expected_paths"]`

y luego solo particiona ese mismo conjunto. Eso NO es una derivación independiente de productores.

Además `validate_runtime_ledger()` itera únicamente sobre `produced`; no descubre archivos reales inesperados dentro de los roots gobernados. Por tanto un archivo extra on-disk puede escapar al control.

## Corrección obligatoria

### 4.1 EXPECTED_SET

Derívalo exclusivamente de contratos/specs declarativos v0.5.

### 4.2 PRODUCER_SET

Derívalo independientemente desde los productores reales de los pasos 1–17: constantes/path-builders propios de:

- preflight runtime record;
- EV03 builder/evaluator;
- EV04 builder/evaluator;
- D1a builder/evaluator/adapter v0.5;
- case comparisons;
- aggregate comparisons;
- unified summary;
- execution manifest.

`producer_runtime_paths()` NO puede leer `expected_paths` para construir el productor.

### 4.3 OBSERVED_SET runtime

En el step 18, descubre recursivamente los archivos realmente existentes bajo los `FUTURE_ROOTS`/discovery roots contractuales. Compara:

`OBSERVED_SET == EXPECTED_SET`

excluyendo únicamente el self-path del ledger según el contrato y manejando de forma explícita roots que sean archivos individuales.

Debe fallar por:

- missing esperado;
- unexpected real on-disk;
- path collision;
- `execution_failed.json` en success path;
- modificación post-step13 cuando exista snapshot.

Tests mínimos en tempdir:

- exact physical file set => PASS;
- borrar un archivo físico => FAIL;
- crear un archivo extra físico dentro de discovery root => FAIL;
- introducir `execution_failed.json` => FAIL;
- mutar bytes de un archivo snapshot => FAIL.

No aceptes como suficiente tests que solo muten sets Python sin crear el archivo extra en disco.

---

# 5. F35C-03 — La transición futura de autorización v0.5 está subvalidada

No crees una autorización real en este bloque, pero la futura transición debe quedar diseñada y shadow-tested antes de integrar v0.5.

El `preflight_authorized()` v0.5 rechazado solo verifica strings de estado y un authorization record mínimo. Recupera como mínimo la robustez del contrato v0.4 auditado.

## Contrato obligatorio de autorización v0.5

Implementa funciones equivalentes a:

- `authorization_record_contract()`;
- `validate_authorization_record_schema()`;
- `validate_authorization_baseline_ancestry()`;
- `validate_authorization_record_bindings()`;
- `_authorization_projection()`;
- `validate_authorization_transition()`;
- `load_authorization_transition_from_git()`.

La futura autorización debe exigir:

1. baseline v0.5 auditado como proper ancestor del commit de autorización;
2. authorization record con schema **exacto**, sin missing ni extra keys;
3. bindings baseline exactos de gate + EV03 spec + EV04 spec + D1a spec mediante:
   - path;
   - Git blob SHA-1;
   - canonical Git blob SHA-256;
   - canonical size bytes;
4. authorized gate/specs leídos del commit y filesystem deben coincidir;
5. immutable projection baseline→authorized exacta;
6. únicos campos mutables permitidos:
   - gate status/readiness;
   - cuatro flags `*_NUMERICAL_EXECUTION`;
   - `authorization_record_present`;
   - `attempt06`;
   - cada spec: solo su propia flag + `attempt06`;
7. `corrective_retrieval_executed`, `corrective_metrics_computed`, `runtime_authorization_record_present` permanecen false al autorizar;
8. cualquier deriva de corpus, MRR, paths, modelo, environment contract, ledger, code binding o schema => FAIL_CLOSED;
9. `preflight_authorized()` debe validar esta transición completa antes de cualquier side effect y antes de devolver PASS.

## Binding de dependencias/código

No dejes `candidate_source_bindings` como metadata no validada. Usa bindings canónicos Git y verifícalos en el futuro preflight autorizado. Incluye como mínimo:

- los cuatro sources v0.5;
- builders/evaluators reutilizados que realmente ejecutará v0.5;
- config/corpus/EVAL frozen;
- BM25 binary/index frozen requerido para control;
- specs/gate por la transición de autorización;
- modelo completo por el environment gate local SHA/size manifest.

No confundas Git canonical bytes con checkout CRLF bytes.

## Positive authorization shadow obligatorio

Sin crear authorization record real ni autorizar Attempt06, construye en memoria/tempdir o mediante fixtures una transición baseline→authorized válida y demuestra PASS.

Negativos obligatorios:

- field científico/técnico alterado => FAIL;
- path/root alterado => FAIL;
- environment contract alterado => FAIL;
- code binding alterado => FAIL;
- auth record missing field => FAIL;
- auth record extra field => FAIL;
- binding SHA incorrecto => FAIL;
- baseline que no sea proper ancestor/equivalente fixture inválido => FAIL;
- spec/gate filesystem distinto del commit autorizado => FAIL.

No declares futura autorización lista si estos controles no pasan.

---

# 6. F35C-04 — R13: coherencia ranking↔summary todavía incompleta

Mantén el contrato de 10 rankings vacíos EV03, pero fortalece casos no vacíos.

Para cada case_id con candidate rows:

- todos los candidate rows deben tener `nandina_ref` igual al del case summary;
- `candidate_rank` contiguo 1..N;
- count candidate rows == `retrieved_count`;
- `top1_code` == primer código efectivo;
- `rank_ref` del summary debe ser **exactamente** la posición real de `nandina_ref` en el ranking efectivo, o 0 si no aparece;
- EV04 mantiene códigos únicos.

Para casos vacíos conserva:

- retrieved_count=0;
- rank_ref=0;
- top1 fields vacíos;
- cero candidate rows.

Añade negativos explícitos para `summary.rank_ref` incorrecto y `candidate_row.nandina_ref` discordante.

## Métricas completas en step13

No limites integridad a `metric_table`.

Para EV04 valida el objeto completo de métricas persistidas contra el contrato canónico v0.4/v0.5 de 92 keys, aliases MRR, 27 rows, tipos/finitud y valores derivados del case summary, de forma compatible con persist/reload y sin depender del orden de keys dentro de cada row.

Para EV03 valida también el objeto completo frente a las métricas rederivables del case summary bajo el evaluator congelado, no solo 17 filas.

No modifiques las definiciones científicas.

---

# 7. F35C-05 — Manifest runtime: provenance de autorización demasiado débil

El manifest final v0.5 no debe conservar solo `{status, record}`.

Debe incorporar y validar de forma no ambigua al menos:

- execution authorization commit;
- authorization baseline commit;
- authorization transition proof;
- cuatro flags autorizadas;
- authorization record binding con Git blob SHA-1 + canonical SHA-256 + size;
- authorized gate/spec artifact bindings;
- environment fingerprint usado realmente;
- 19-step order;
- roots v0.5;
- resultados/refs permitidos.

Schema exacto, `allow_nan=False`, no-overwrite, round-trip PASS, cero referencias runtime a partial roots v0.4.

Añade negativos por provenance incompleta o inconsistente.

---

# 8. F35C-06 — Auditoría exhaustiva de tokens/identidades stale

Haz un scan semántico de todos los nuevos artifacts/sources v0.5.

`v0.4` solo puede aparecer cuando sea explícitamente antecedente histórico, por ejemplo:

- Attempt05 failclosed;
- `v04_partial_roots` / política NEVER_INPUT;
- referencia histórica claramente etiquetada.

NO puede aparecer como identidad corriente v0.5 en:

- `specification_id`;
- current runner output filename;
- current hash-ledger included/excluded path;
- current execution command;
- current source code identity;
- current runner binding.

Igualmente, ningún `v0.1`/`v0.4` runner filename D1a puede ser el output actual de v0.5.

Para EV03/EV04/D1a:

- `specification_id` debe ser v0.5;
- command/module actual debe ser v0.5 donde exista wrapper v0.5;
- Git blob SHA-1/canonical SHA-256 debe corresponder al archivo cuyo path declara.

Produce una allowlist explícita de ocurrencias históricas `v0.4` y falla ante cualquier stale current identity fuera de ella.

---

# 9. Preservaciones metodológicas obligatorias

No cambies:

- MRR@100 = exact rational from `rank_ref` + final float conversion;
- MRR@200 = legacy `sum(float(reciprocal_rank))` in frozen row order;
- contribution 101–200 = exact rational difference;
- EV04 aggregate = 28 rows con contribution tercera;
- EV03 recovered historical semantics;
- Decision906 scope = solo `87044110`, `87045110`;
- D1a frozen model/config/EVAL;
- no retraining;
- 19-step scientific order.

No cambies Plan, Article, EXP11B, EXP12 ni componentes históricos v0.1–v0.4 salvo los cuatro JSON v0.4 de estado y failclose sanitizado ya autorizados por Prompt35B.

---

# 10. Environment gate y riesgos runtime

Preserva y vuelve a ejecutar read-only/localmente el environment gate con el intérprete fingerprinted que ya pasó, si continúa disponible:

- Python 3.10.11;
- executable SHA-256 `b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961`;
- imports requeridos;
- 9/9 model files exactos;
- offline 32-string smoke `(32,384)` float32 finite normalized;
- 21-vector historical replay si sus artefactos locales siguen disponibles;
- disk/RAM reprobe.

No conviertas esta evidencia local en CI independiente.

Riesgos que deben permanecer residuales:

- `FULL_7644_DOCUMENT_ENCODE`;
- `FULL_1056_QUERY_ENCODE_AND_EVALUATION`;
- `RUNTIME_MEMORY_CPU_IO_PEAK`;
- `FUTURE_OUTPUT_HASHES`;
- `EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS`.

No declares `RISK_ZERO`.

---

# 11. Shadow integral obligatorio antes de publicar

Ejecuta sin retrieval científico ni D1a completo:

1. preauthorization closed preflight;
2. environment/model smoke;
3. optional 21-vector replay;
4. EV03 frozen original-vs-original con 1056 casos / 10 empty rankings;
5. R13 rank_ref/nandina consistency positivos y negativos;
6. EV04 92-key / 27-row full metric validation persist/reload;
7. aggregate EV03 17 / EV04 28 + NaN/Inf negatives;
8. unified summary positivos/negativos;
9. D1a v0.5 path-contract three-way equality;
10. D1a ledger-contract actual-producer consistency;
11. manifest full-provenance round-trip/negatives;
12. EXPECTED_SET vs independently derived PRODUCER_SET;
13. OBSERVED_SET filesystem exact/missing/extra/failure-record/snapshot-mutation tests;
14. positive authorization-transition shadow + todos los negativos de §5;
15. 19-step synthetic pipeline + missing/reordered/FAIL/early-final negatives;
16. stale-token/current-identity audit.

Si aparece cualquier contradicción nueva: `FAIL_CLOSED / NEW_BLOCKING_INVARIANT` y no declares candidato listo.

---

# 12. Tests y regresión

Añade/modifica únicamente tests v0.5 necesarios para cubrir F35C-01..06.

Ejecuta:

- todos los tests v0.5 focalizados;
- regresiones v0.4 relevantes para MRR/EV03/D1a, interpretando correctamente estados históricos consumidos;
- no es obligatorio ocultar fallos históricos de harness incompatibles con estados ya consumidos; repórtalos exactamente;
- no ejecutes full scientific retrieval/EVAL.

Clasificación:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

Reporta comandos exactos, PASS/FAIL/ERROR/SKIP y duración.

---

# 13. Artefactos/state v0.5

Mantén un bundle equivalente al Prompt35B, corregido. No crees authorization record v0.5.

Estados máximos permitidos:

```text
V05_CORRECTED_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
GATE_STATUS = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED
AUTHORIZATION_READINESS = NOT_AUTHORIZED
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

---

# 14. Verificación Git final

Antes de commit/push:

- diff exacto frente a `c873ff1...`;
- ningún path fuera de alcance;
- ninguna modificación Plan/Article/EXP11B/EXP12;
- no authorization record v0.5;
- no runtime roots v0.5 creados;
- no partial v0.4 usado/copied/cleaned;
- no raw stderr ni rutas absolutas host-locales en artefactos públicos;
- bindings de sources/artifacts coherentes con INDEX/Git canonical bytes.

Publica únicamente:

`codex/0b05c-v05-remediated-preauthorization-candidate-v2`

No integres a `main`.

---

# 15. Persistencia administrativa

Después del trabajo técnico:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch` antes de escribir;
3. no rebase/amend/force;
4. crea exclusivamente:

`codex_prompts_tmp/35C_RESPUESTA_CORREGIR_V05_CONTRATOS_D1A_LEDGER_AUTORIZACION.md`

El reporte debe incluir:

- branch/commit/tree/parent del candidato corregido;
- diff exacto y blobs;
- cierre F35C-01..06 con evidencia;
- tabla D1a three-way path identity;
- resultado real de ledger observed-extra filesystem negative;
- resultado authorization positive/negative shadow;
- stale-token allowlist/audit;
- environment/replay status;
- tests completos;
- riesgos residuales;
- estado inequívoco `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`.

Responde únicamente con ese reporte final.