# PROMPT105 — CORREGIR G6-F02: HASH LEDGER CANÓNICO Y ACCESIBILIDAD DE G6-FIG-03

## 0. Rol y alcance

Actúa como **Codex ejecutor reproducible** del proyecto de tesis `elVladdi/gci-nandina-rag`.

Este prompt NO reinicia G6-F02 y NO autoriza una nueva ejecución científica desde cero.

Prompt104 quedó interrumpido por límite de uso después de haber materializado y publicado un candidato remoto. La auditoría externa independiente verificó que el candidato existe y que G6-F02 quedó registrado como `CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED`, pero detectó **dos correcciones bloqueantes y localizadas**:

1. el ledger SHA-256 fue calculado sobre bytes materializados CRLF del workspace Windows para varios artefactos de texto, mientras los bytes canónicos versionados en Git están normalizados y presentan tamaños distintos; por tanto, el ledger actual no es verificable directamente contra el contenido versionado remoto;
2. `G6-FIG-03` usa etiquetas categóricas de `7.5 pt`, por debajo del mínimo efectivo `8.5 pt` exigido por el registry G6-F01.

Debes corregir exclusivamente esos dos puntos, revalidar el candidato completo y persistir el reporte oficial de recuperación.

No cambies datos, claims, métricas, inferencia, CI, p-values, layout científico, número de figuras ni semántica visual.

`Prompt103` permanece `SUPERSEDED / DO_NOT_EXECUTE`.

---

# 1. Workspace local canónico obligatorio

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier cambio ejecuta y registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list
git fetch origin
```

STOP si el toplevel no corresponde al workspace canónico, el origin no es `elVladdi/gci-nandina-rag`, existe drift material de las refs congeladas o hay cambios locales no relacionados que impidan aislar la corrección.

---

# 2. Estado remoto congelado después de la interrupción

Verifica exactamente:

```text
MAIN_BASE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_BASE = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_POSTEXEC = 804b59b73d7d2803d15e0adcb80546410a6718b8
PROMPT104 = 350677e7af3427dcfb7a9fd3fd05ebfe8e450fd1
G6_F02_BRANCH = figures/g6-f02-render-v01
G6_F02_CANDIDATE_V01 = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
G6_F02_CANDIDATE_PARENT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

Estado esperado de fichas:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

No vuelvas a activar G6-F02. No modifiques Plan Maestro. No autorices G6-F03.

---

# 3. Preservación del candidato existente

La rama `figures/g6-f02-render-v01` debe existir en:

```text
2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

Verifica que frente a `MAIN_BASE` sea:

```text
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
```

y que el conjunto acumulado de paths modificados sea exactamente el original de Prompt104:

```text
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

No añadas ningún path nuevo al candidato corregido.

La corrección puede producir un segundo commit sobre la misma rama; por tanto, tras la corrección se acepta `COMMITS_AHEAD = 2` siempre que `COMMITS_BEHIND = 0` y el conjunto acumulado de paths frente a `MAIN_BASE` siga siendo exactamente esos 10.

---

# 4. Corrección 1 — accesibilidad G6-FIG-03

Fuente rectora:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
blob = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
```

El registry exige para G6-FIG-03:

```text
Minimum effective font size 8.5 pt
Category labels remain horizontal
```

El candidato V01 usa actualmente `7.5` para las etiquetas categóricas del eje x.

Debes modificar exclusivamente `src/figures/group6/render_g6_fig_03_exp11a.py` en la parte necesaria para que **ninguna etiqueta efectiva de G6-FIG-03 quede por debajo de 8.5 pt**.

Como mínimo:

```text
H25
H50-D1
H50-D2
H75
H100 ref.
```

deben renderizarse horizontalmente con `font size >= 8.5 pt`.

Si el aumento provoca solapamiento, puedes ajustar únicamente espaciado geométrico, ancho útil o posiciones dentro del mismo layout `2x3`, sin cambiar:

- seis paneles;
- orden de métricas;
- orden de condiciones;
- rango y `[0,1]`;
- jitter congelado;
- símbolos;
- número de marcas;
- interpretación no causal.

Regenera únicamente los outputs afectados por esa modificación. Se permite regenerar los tres pares SVG/PNG para revalidación global, pero no cambiar su diseño salvo que sea consecuencia técnica necesaria y no científica.

---

# 5. Corrección 2 — semántica canónica del hash ledger

El ledger V01 contiene SHA-256/tamaños de varios archivos de texto correspondientes a bytes CRLF materializados en el workspace, no a los bytes canónicos versionados en Git. Ejemplos observados por auditoría externa:

```text
src/figures/group6/render_g6_fig_01_he2.py
ledger size = 9369
Git canonical size = 9181

figures/group6/g6_fig_01_he2.svg
ledger size = 23901
Git canonical size = 23713
```

Esto debe corregirse.

## Regla de hash canónico

Para `g6_figure_hash_ledger_v0.1.csv`, el campo:

```text
sha256
size_bytes
```

debe representar **los bytes canónicos versionados por Git**, no los bytes del working tree sujetos a `core.autocrlf`.

Para artefactos ya existentes en HEAD usa los bytes de Git, por ejemplo mediante:

```powershell
git show HEAD:path/to/file
```

Para archivos modificados aún no committed:

1. stagea primero el archivo;
2. obtén los bytes canónicos del índice (`git show :path/to/file`) o mecanismo equivalente que lea exactamente el blob staged;
3. calcula SHA-256 y tamaño sobre esos bytes;
4. escribe el ledger;
5. stagea el ledger;
6. vuelve a verificar todas las filas contra los blobs/index canónicos antes del commit.

Para PNG, al ser binarios, el SHA-256 debe corresponder directamente a sus bytes versionados.

No cambies `.gitattributes` y no añadas otro manifest.

Puedes agregar al ledger una columna adicional opcional, por ejemplo:

```text
hash_semantics
```

con valor:

```text
CANONICAL_GIT_CONTENT_BYTES
```

pero no es obligatorio si la semántica queda explícita en `notes` y en la respuesta oficial.

El ledger no necesita auto-hashearse a sí mismo.

---

# 6. Revalidación científica completa

Tras las correcciones, vuelve a ejecutar y validar las tres figuras contra el registry.

Debes confirmar como mínimo:

## G6-FIG-01

- 3 paneles;
- A = valores absolutos sin CI por brazo;
- B = 15 contrastes con CI congelado 99%;
- C = exactamente un contraste HE2_B con CI congelado 95%;
- sin p-values;
- `Pool@200` no se convierte en estimando confirmatorio;
- rangos `[0,1]`, `[-0.1,1]`, `[-0.1,1]`.

## G6-FIG-02

- 1 panel;
- exactamente 15 marcas;
- 4 variantes formales + 1 contextual;
- `diagnostic_union_hierarchical_dual` excluido;
- y `[0,0.35]`;
- sin CI/p-values/líneas de conexión/regresión/smoothing;
- ticks/leyenda >= 9 pt y axis labels >= 10 pt conforme al registry.

## G6-FIG-03

- 6 paneles `2x3`;
- exactamente 31 corridas observadas por panel según inventario `10/5/5/10/1`;
- 6 summaries verificados pero no graficados;
- D1/D2 resuelto desde `dominant_stratum`;
- y `[0,1]` en todos los paneles;
- jitter determinista idéntico entre paneles;
- H100 una marca/diamante por panel;
- ninguna etiqueta efectiva < 8.5 pt;
- sin CI/p-values/regresión/smoothing/agregados nuevos;
- preservación explícita de sensibilidad conjunta tamaño-composición / no causal.

---

# 7. Determinismo

Ejecuta los tres scripts dos veces consecutivas sin modificar inputs.

Confirma byte-identidad de:

```text
3 SVG
3 PNG
```

entre ambas ejecuciones en el mismo entorno canónico.

Después de stagear los outputs finales, verifica además que los hashes canónicos del ledger coincidan exactamente con los bytes de Git/index que serán versionados.

Registra:

```text
PYTHON_VERSION
PILLOW_VERSION
PILLOW_AVAILABLE_IN_CANONICAL_RUNTIME = true/false
MATPLOTLIB_USED = false
PANDAS_USED = false
DETERMINISM_CHECK
CANONICAL_HASH_LEDGER_CHECK
```

No instales ni descargues paquetes durante esta corrección. Si Pillow deja de estar disponible en el runtime canónico, STOP y repórtalo; no improvises otra biblioteca.

---

# 8. Commit correctivo candidato

Trabaja sobre la misma rama:

```text
figures/g6-f02-render-v01
```

Partiendo exactamente de:

```text
2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

Crea un único commit correctivo.

Después del commit y push, verifica frente a `MAIN_BASE`:

```text
COMMITS_AHEAD = 2
COMMITS_BEHIND = 0
CUMULATIVE_CHANGED_PATH_COUNT = 10
```

No integres a `main`.

---

# 9. Estado de fichas

La ficha ya está correctamente registrada como:

```text
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

No vuelvas a cambiar el estado.

Solo si es necesario para trazabilidad, añade al final de `04_REGISTRO_ESTADO_FICHAS.md` un bloque documental de **candidato corregido pendiente de reauditoría**, sin cambiar la fila de estado, con:

```text
G6_F02_CORRECTION_PROMPT = PROMPT105
G6_F02_INITIAL_CANDIDATE = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
G6_F02_CORRECTED_CANDIDATE = <sha>
CORRECTION_SCOPE = HASH_LEDGER_CANONICAL_BYTES + FIG03_MIN_FONT_8_5
EXTERNAL_REAUDIT = PENDING
G6_F03_AUTHORIZED = false
```

Si haces esta actualización, modifica exclusivamente `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md` sobre la rama de fichas actual `804b59b73d7d2803d15e0adcb80546410a6718b8` y genera un commit separado.

No modifiques Plan Maestro.

---

# 10. Respuesta oficial de recuperación

Prompt104 no alcanzó a persistir su respuesta oficial por agotamiento de cuota. **No fabriques retrospectivamente una respuesta 104 como si hubiera existido.**

Persiste la respuesta real de esta recuperación en:

```text
codex_prompts_tmp/105_RESPUESTA_CORREGIR_G6_F02_HASH_LEDGER_Y_ACCESIBILIDAD_FIG03.md
```

sobre:

```text
codex/prompts-temporary
```

La respuesta debe declarar explícitamente:

```text
PROMPT104_INTERRUPTED_AFTER_REMOTE_CANDIDATE = true
PROMPT104_RESPONSE_WAS_NOT_PERSISTED = true
PROMPT105_EXECUTION = COMPLETE
MAIN_BASE
PLAN_BASE
FICHAS_POSTEXEC
INITIAL_CANDIDATE
CORRECTED_CANDIDATE
COMMITS_AHEAD
COMMITS_BEHIND
CUMULATIVE_CHANGED_PATH_COUNT
CORRECTION_CHANGED_PATHS
FIG03_MIN_EFFECTIVE_FONT_PT
DETERMINISM_CHECK
CANONICAL_HASH_LEDGER_CHECK
PYTHON_VERSION
PILLOW_VERSION
PILLOW_AVAILABLE_IN_CANONICAL_RUNTIME
FIGURE_VALIDATION_SUMMARY
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
G6_F03_AUTHORIZED = false
EXTERNAL_REAUDIT = PENDING
```

No declares G6-F02 `PASS`, `APPROVED`, `CLOSED` ni `INTEGRATED`.

---

# 11. Criterios para la reauditoría externa

El candidato corregido solo será aprobable si se confirma simultáneamente:

1. mismo parent científico `MAIN_BASE`;
2. exactamente 10 paths acumulados frente a `MAIN_BASE`;
3. ninguna figura adicional;
4. G6-FIG-03 cumple mínimo efectivo 8.5 pt;
5. ledger SHA-256 y tamaños coinciden con bytes canónicos versionados de cada artefacto;
6. determinismo de SVG/PNG entre dos ejecuciones;
7. datos, paneles, marcas, rangos e incertidumbre siguen siendo exactamente los autorizados;
8. cero nuevas métricas/inferencia/CI/p-values;
9. artículo y tesis sin cambios;
10. G6-F03 sigue no autorizado.

Si cualquier punto falla, deja G6-F02 pendiente de corrección y no avances.
