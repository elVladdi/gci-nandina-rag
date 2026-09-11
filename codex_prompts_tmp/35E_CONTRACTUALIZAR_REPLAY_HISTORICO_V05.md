# PROMPT 35E — CONTRACTUALIZAR REPLAY HISTÓRICO v0.5 ANTES DE INTEGRACIÓN

## Rol y objetivo

Actúa como **ejecutor técnico controlado preautorización**. Este bloque corrige un único hallazgo residual de la auditoría externa de Prompt35D y debe producir un candidato v0.5 limpio, con el replay histórico de 21 vectores convertido en requisito contractual fail-closed para toda futura preautorización de Attempt06.

El candidato Prompt35D:

- rama `codex/0b05c-v05-remediated-preauthorization-candidate-v3`
- commit `1f30047b8b3d6d6d484cd6bb96716a0ac1fbd19e`

queda **REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED** exclusivamente por el finding descrito aquí. Puedes reutilizar su contenido como fuente de trabajo, pero NO debe ser parent ni ancestro del candidato final.

**NO autorices ni ejecutes Attempt06. NO reejecutes Attempt05. NO ejecutes retrieval científico, EV03 real, EV04 real, D1a completo ni EVAL real. NO instales ni actualices dependencias.**

---

# 1. Estado exacto de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main científico esperado:

`c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`

Refs protegidas:

- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de editar:

1. `git fetch`;
2. verifica `origin/main == c873ff1...`;
3. verifica que Prompt35D `1f30047...` existe, parent directo `c873ff1...`, pero NO está integrado;
4. verifica Plan/Article exactos;
5. verifica que no exista authorization record v0.5 en main;
6. verifica `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
7. verifica ausencia de los 16 prospective roots v0.5 en el checkout de trabajo destinado a este candidato;
8. no uses partial roots v0.4 como inputs científicos.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Rama corregida

Crea desde `main = c873ff1...`:

`codex/0b05c-v05-remediated-preauthorization-candidate-v4`

Puedes recuperar al working tree el contenido útil de `1f30047...` sin introducirlo como ancestro. El candidato final debe ser:

- un único commit;
- parent directo `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`;
- sin merge;
- sin authorization record v0.5;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`.

Preserva íntegramente las correcciones válidas de Prompt35D salvo los cambios estrictamente necesarios para este finding.

---

# 3. Finding F35E-01 — El replay histórico pasó, pero sigue siendo opcional en preflight futuro

La auditoría externa confirmó:

- Prompt35D realizó un replay histórico con **21 vectores** y obtuvo PASS;
- los artefactos necesarios estaban disponibles durante Prompt35D;
- el readiness versionado registra `historical_vector_replay.status = PASS` y `sample_count = 21`;
- sin embargo `optional_historical_vector_replay()` devuelve `OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE` si faltan los assets, y `preauthorization_environment_preflight()` todavía puede devolver `status=PASS` en ese caso.

Esto viola el contrato fijado en Prompt35D: una vez que el baseline auditado demostró que el replay estaba disponible y pasó, su desaparición posterior no puede degradarse silenciosamente a “opcional”. Debe ser un blocker preautorización.

## 3.1 Contractualización obligatoria

Añade al contrato ambiental/gate v0.5 un estado inequívoco, por ejemplo:

`historical_vector_replay_required = true`

El nombre puede variar solo si la semántica queda igual de explícita.

Desde este candidato en adelante, todo preflight preautorización y autorizado debe exigir, antes de cualquier side effect:

1. que existan los assets de replay requeridos;
2. que sus identidades gobernadas coincidan exactamente;
3. que el replay se ejecute;
4. que el replay devuelva PASS;
5. que `sample_count == 21`.

No se permite retornar PASS si el replay requerido resulta `NOT_AVAILABLE`, `SKIPPED`, `OPTIONAL_*`, `FAIL` o equivalente.

## 3.2 Assets y validación obligatoria

Usa el metadata histórico congelado como autoridad. Debes verificar al menos:

- `vectors.npy`;
- docstore;
- id_map;
- vector-integrity sample CSV usado para el replay;
- metadata que gobierna esos paths/hashes.

Para los tres assets principales ya gobernados conserva hash/size exactos.

Para el sample CSV agrega validación explícita:

- path exacto desde metadata;
- archivo presente;
- SHA-256 exacto contra el valor versionado en metadata/gate de integridad correspondiente;
- CSV legible;
- exactamente 21 filas;
- exactamente 21 `vector_index` únicos;
- índices enteros no negativos y dentro del rango de vectors/docstore/id_map;
- ningún `stored_text_sha256` vacío o malformed;
- el texto reconstruido debe conservar la comprobación hash ya existente.

Si el metadata histórico no expone directamente el SHA del sample en el nodo que actualmente lees, sigue la referencia versionada correcta hasta el `vector_integrity_gate`/metadata que sí lo contiene. No inventes hashes.

## 3.3 Resultado contractual del replay

El helper puede conservar el nombre actual o renombrarse, pero debe diferenciar claramente:

- `REQUIRED_REPLAY_PASS` / equivalente;
- cualquier ausencia o mismatch => excepción fail-closed.

El resultado devuelto al environment preflight debe contener como mínimo:

- `status = PASS`;
- `required = true`;
- `sample_count = 21`;
- `cosine_min`;
- `max_absolute_difference`;
- `tolerance`;
- clasificación `ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT`.

`preauthorization_environment_preflight()` debe comprobar explícitamente `required is true`, `status == PASS` y `sample_count == 21` antes de devolver PASS.

## 3.4 Readiness y manifest futuro

El readiness v0.5 debe registrar de forma inequívoca:

`historical_vector_replay_required = true`

junto con el PASS observado.

El environment fingerprint/provenance del futuro manifest de ejecución también debe exigir y conservar evidencia de que el replay requerido pasó en el preflight usado para autorizar/ejecutar. No basta con conservar solo Python/packages.

No conviertas el vector replay en resultado científico nuevo. Sigue siendo:

`ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT`.

---

# 4. Negativos obligatorios

Añade pruebas/shadows que demuestren FAIL_CLOSED antes de autorización ante cada caso:

1. `vectors.npy` ausente;
2. docstore ausente;
3. id_map ausente;
4. sample CSV ausente;
5. sample CSV con SHA distinto al metadata;
6. sample con 20 filas;
7. sample con 22 filas;
8. `vector_index` duplicado;
9. `vector_index` fuera de rango;
10. `stored_text_sha256` vacío/malformed;
11. replay devuelve `status != PASS`;
12. replay devuelve `sample_count != 21`;
13. environment preflight recibe resultado `OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE` o equivalente => FAIL.

El positivo debe demostrar:

- 21/21 únicos;
- hashes exactos;
- replay PASS;
- preflight environment PASS;
- cero side effects científicos.

No basta con mocks que omitan validar los archivos físicos para todos los negativos de assets/sample. Usa `tempdir` con archivos reales cuando corresponda.

---

# 5. Reprobe actual obligatorio

No instales ni actualices paquetes. Usa el mismo entorno aislado ya identificado por Prompt35D si sigue disponible.

Al final repite un reprobe fresco del contrato completo:

- executable SHA exacto;
- Python/platform exactos;
- 8 paquetes críticos exactos;
- 42 distribuciones exactas;
- 31 imports project-local exactos;
- model manifest 9/9 PASS_EXACT;
- smoke 32x384 float32 finito normalizado;
- replay histórico **REQUIRED / 21/21 PASS**;
- capacity PASS.

Si el entorno o los replay assets ya no están disponibles, no publiques candidato v4: persiste únicamente el reporte administrativo con `STOP / CURRENT_ENVIRONMENT_OR_REQUIRED_REPLAY_NOT_AVAILABLE`.

---

# 6. Preservaciones obligatorias

No cambies:

- MRR@100 racional prospectivo;
- MRR@200 legacy;
- contribución 101–200 racional;
- EV04 aggregate 28 filas;
- EV03 recovered historical semantics;
- Decision906 exactamente dos códigos `87044110` y `87045110`;
- modelo D1a frozen / no retraining;
- EVAL N=1056;
- 19 pasos;
- 16 roots v0.5;
- `V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05`;
- exact-five-path future authorization commit;
- bindings baseline↔authorization;
- import closure 31 y runtime data dependencies 22, salvo que una derivación automática legítima demuestre un cambio requerido por este pequeño fix; si cambia, documenta exactamente por qué;
- validación fuerte D1a;
- ledger físico;
- manifest provenance;
- fail-close Attempt05.

No modifiques Plan, Article, EXP11B ni EXP12.

---

# 7. Tests y clasificación epistemológica

Ejecuta:

1. suite nueva/relevante F35E;
2. suite focalizada v0.5 completa;
3. regresión relevante v0.4, reportando honestamente non-successes históricos ya conocidos sin maquillarlos.

Todo test local debe clasificarse:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

No declares GitHub CI si no existe.

---

# 8. Salida y publicación

Si todo pasa:

- publica únicamente la rama candidata v4;
- NO integres a main;
- NO crees authorization record v0.5;
- NO autorices Attempt06;
- NO ejecutes Attempt06.

El reporte debe incluir:

- branch/commit/parent/tree;
- diff exacto contra `c873ff1...`;
- comparación conceptual con Prompt35D indicando paths realmente cambiados por F35E;
- evidencia de `historical_vector_replay_required=true`;
- negativos 1–13;
- fresh reprobe final;
- tests;
- riesgos residuales runtime inevitables;
- estado exacto final.

Persistencia obligatoria del reporte:

`codex_prompts_tmp/35E_RESPUESTA_CONTRACTUALIZAR_REPLAY_HISTORICO_V05.md`

en rama `codex/prompts-temporary`.

## Estado final permitido

Solo si todo pasa:

```text
PROMPT35E = COMPLETED
V05_CANDIDATE = BUILT / CURRENT_ENVIRONMENT_VERIFIED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
F35E_01_HISTORICAL_REPLAY_CONTRACT = CLOSED_BY_CODE_TEST_AND_FRESH_REPROBE
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

No declares `READY_FOR_ATTEMPT06`, `AUTHORIZED` ni `CLOSED`.
