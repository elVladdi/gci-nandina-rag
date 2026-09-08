# CODEX — Diagnóstico read-only de `WinError 5` en 0B-05C

## Rol

Actúa exclusivamente como **diagnosticador del entorno local**. No eres ejecutor científico en este bloque.

El intento numérico 0B-05C anterior terminó de forma cerrada antes de crear artefactos, con el bloqueo reportado:

`WinError 5` al intentar crear `outputs/evaluation/0b05c_corrective_numerical_v0.1`.

La auditoría externa determinó:

`0B05C_NUMERICAL_EXECUTION_ATTEMPT_01 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

No existen resultados numéricos nuevos válidos y deben permanecer:

- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`

## Objetivo único

Determinar, con evidencia read-only, la causa del `WinError 5` que impidió crear el runtime root de 0B-05C.

**No soluciones todavía el problema. No reintentes la ejecución. No crees archivos o directorios dentro del repositorio.**

---

## Estado Git de referencia

Repositorio:

`elVladdi/gci-nandina-rag`

Base científica autorizada:

`main = origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`

Tree esperado de esa base:

`c84da63249619e94ae69fb2a6f080dd3f84cbcf4`

Authorization baseline:

`0e074db638f6b7163d98d34f08f76e1efde07b7f`

Rama local usada por el intento fallido:

`codex/0b05c-corrective-numerical-execution-v01`

La rama de ejecución **no fue publicada** y no hubo commit candidato.

No alteres:

- `main`
- `origin/main`
- `docs/plan-maestro-temporal-2026-08-31`
- `article/main-manuscript`
- EXP11B
- EXP12
- ningún XLSX
- ningún archivo tracked o untracked

---

# 1. PROHIBICIONES ABSOLUTAS

Durante este diagnóstico **NO** ejecutes ninguno de estos actos:

- `python -m src.experiments.run_0b05c_corrective_numerical_v01 --execute-authorized`
- ninguna variante de ejecución del runner 0B-05C;
- ningún builder/evaluator/retrieval;
- ningún rerun de EV03, EV04 o D1a;
- `mkdir`, `New-Item`, `touch`, redirecciones `>` o cualquier escritura dentro del repositorio;
- creación de archivos de prueba dentro del repositorio;
- borrado, rename o move de archivos/directorios;
- `git clean`, `git reset`, `git stash`, `git checkout`, `git switch`, `git restore`;
- commit, merge, rebase, cherry-pick o push;
- `chmod`, `Set-Acl`, `icacls /grant`, `icacls /reset`, `takeown`, `attrib +/-R`, `Unblock-File`;
- cambios a Windows Defender, Controlled Folder Access, antivirus, servicios o políticas;
- terminar procesos o liberar handles;
- instalar herramientas;
- descargar Sysinternals u otro software;
- modificar `.gitignore`.

No cambies de rama. Diagnostica el workspace exactamente como quedó.

---

# 2. CONFIRMA EL ESTADO LOCAL SIN MODIFICARLO

Recoge y reporta literalmente:

1. ruta absoluta del repositorio;
2. rama actual;
3. `HEAD`;
4. tree de `HEAD`;
5. `main` local;
6. `origin/main`;
7. si existe la rama local `codex/0b05c-corrective-numerical-execution-v01` y a qué SHA apunta;
8. `git status --porcelain=v2 --untracked-files=all`;
9. lista completa de los paths untracked preexistentes;
10. `git diff --name-only`;
11. `git diff --cached --name-only`;
12. cualquier operación Git en progreso detectada de forma read-only.

No ocultes los tres paths untracked reportados anteriormente: enuméralos y determina si alguno intersecta directa o indirectamente con:

`outputs/evaluation/0b05c_corrective_numerical_v0.1`

Si el estado tracked ya no es limpio, **detén el diagnóstico después de documentarlo** y no repares nada.

---

# 3. INSPECCIONA LA CADENA DE PATHS DEL FALLO

Determina la ruta absoluta exacta de:

- repositorio;
- `outputs`;
- `outputs/evaluation`;
- `outputs/evaluation/0b05c_corrective_numerical_v0.1`.

Para cada nivel informa, sin escribir:

- existe / no existe;
- archivo / directorio / symlink / junction / reparse point;
- atributos de filesystem;
- propietario;
- ACL efectiva visible;
- si la herencia ACL está habilitada o protegida;
- link target si aplica;
- si hay colisión de nombre con un archivo regular;
- timestamps visibles;
- filesystem/drive donde reside.

Usa únicamente comandos read-only equivalentes a:

- `Test-Path -LiteralPath ...`
- `Get-Item -LiteralPath ... -Force`
- `Get-Acl -LiteralPath ...`
- `icacls <path>` **sin opciones de modificación**;
- `attrib <path>` **solo consulta**;
- `fsutil reparsepoint query <path>` solo si el path existe y el comando está disponible;
- `Get-PSDrive` / `Get-Volume` / información de volumen en modo lectura.

Si algún comando requiere elevación o falla, registra el error y continúa únicamente con verificaciones read-only disponibles.

---

# 4. IDENTIDAD Y PERMISOS DEL PROCESO

Reporta:

- usuario efectivo (`whoami`);
- grupos (`whoami /groups`);
- privilegios (`whoami /priv`);
- shell y versión de PowerShell si aplica;
- versión de Python usada por el intento si puede obtenerse sin modificar nada;
- ubicación del ejecutable Python;
- `USERPROFILE`, `TEMP`, `TMP`, `OneDrive` y variables relacionadas, sin exponer secretos;
- si la ruta del repositorio reside dentro de OneDrive, Desktop, Documents u otra ruta potencialmente protegida.

No cambies permisos ni identidad.

---

# 5. CONTROLLED FOLDER ACCESS / DEFENDER — SOLO LECTURA

Si Microsoft Defender está disponible, consulta sin modificar:

- estado de `EnableControlledFolderAccess`;
- protected folders configurados;
- allowed applications configuradas que sean relevantes;
- estado general de Defender relacionado con protección de carpetas.

Si tienes permisos read-only sobre el log operacional de Defender, revisa eventos recientes de Controlled Folder Access, especialmente bloqueos/auditorías (por ejemplo IDs 1123/1124 si existen en ese sistema), buscando referencias a:

- `python.exe`;
- PowerShell;
- la ruta del repositorio;
- `outputs/evaluation/0b05c_corrective_numerical_v0.1`.

No cambies Defender, no agregues exclusiones y no desactives protección.

La mera existencia de Controlled Folder Access **no demuestra causalidad**: clasifica como causa confirmada solo si existe evidencia específica de bloqueo del proceso/path pertinente.

---

# 6. REPARSE POINTS, SINCRONIZACIÓN Y COLISIONES

Comprueba read-only si cualquiera de estos elementos está presente en la cadena del path:

- junctions;
- symlinks;
- reparse points;
- OneDrive Files On-Demand;
- atributos offline/recall-on-data-access;
- rutas sincronizadas;
- un archivo regular ocupando el nombre esperado de un directorio;
- ACL `DENY` explícita;
- ACL heredada sin CreateDirectories/Write equivalente para el usuario efectivo.

No fuerces hidratación, no cambies atributos y no resuelvas el problema todavía.

---

# 7. PROCESOS / LOCKS — SOLO SI ES POSIBLE SIN INSTALAR NADA

Determina si existe evidencia de un proceso que pudiera mantener un lock o interferir con la ruta.

Puedes usar únicamente herramientas que ya estén instaladas y en modo lectura.

- No mates procesos.
- No cierres aplicaciones.
- No descargues `handle.exe` ni Process Explorer.
- Si no existe una herramienta fiable ya instalada para identificar handles, declara `LOCK_OWNER_NOT_DETERMINED` en vez de especular.

Un lock genérico no debe declararse causa confirmada sin evidencia del handle/path concreto.

---

# 8. CONFIRMA EL PUNTO DE FALLO EN EL CÓDIGO — READ-ONLY

Inspecciona el código congelado en `HEAD`, sin modificarlo, y confirma:

1. `UNIFIED_RUNTIME_ROOT`;
2. la ruta de `runtime_authorization_record.json`;
3. la implementación de `_write_json_new`;
4. que `_write_json_new` intenta primero crear `path.parent` mediante `mkdir(parents=True, exist_ok=True)` antes de escribir el JSON;
5. que la primera operación con side effect del pipeline autorizado es la creación del runtime authorization record;
6. que EV03 todavía no debería haber comenzado si el fallo ocurrió en ese `mkdir`.

Incluye archivo + función + números de línea actuales si puedes obtenerlos de forma read-only.

NO invoques la función.

---

# 9. NO HAGAS UNA PRUEBA DE ESCRITURA

En este bloque está **prohibido** probar permisos creando deliberadamente:

- el runtime root;
- un directorio hermano;
- un archivo temporal dentro de `outputs`;
- cualquier otro artefacto dentro del repositorio.

Tampoco vuelvas a ejecutar el runner para reproducir el error.

Si la evidencia read-only no permite identificar la causa, el resultado correcto es:

`ROOT_CAUSE = UNRESOLVED_READONLY`

No rellenes el vacío con una hipótesis presentada como hecho.

---

# 10. CLASIFICACIÓN DEL DIAGNÓSTICO

Asigna exactamente una de estas clases finales:

### A. `ROOT_CAUSE_CONFIRMED`
Solo si hay evidencia directa y específica suficiente.

Ejemplos válidos:

- ACL `DENY` aplicable al usuario efectivo sobre el parent requerido;
- target name ocupado por archivo regular;
- reparse target con acceso denegado probado;
- evento CFA que identifica explícitamente proceso y path del intento;
- otra causa demostrable directamente.

### B. `ROOT_CAUSE_PROBABLE`
Si existe evidencia fuerte pero no concluyente.

Debes distinguir claramente hechos de inferencias.

### C. `ROOT_CAUSE_UNRESOLVED_READONLY`
Si las verificaciones read-only no bastan.

Esta clasificación es preferible a inventar una explicación.

---

# 11. PROPUESTA DE REMEDIACIÓN — SOLO PROPUESTA

Después del diagnóstico puedes proponer la **mínima acción correctiva** necesaria para una fase posterior, pero **NO la ejecutes**.

Para cada acción propuesta indica:

- qué modificaría;
- por qué es necesaria;
- si afecta o no archivos del repositorio;
- si cambia permisos/ACL/Defender/OneDrive;
- reversibilidad;
- riesgo de alterar evidencia;
- si requeriría autorización explícita antes de realizarse.

No propongas modificar código científico como primera respuesta a un `WinError 5` si la evidencia apunta al filesystem/OS.

---

# 12. REPORTE FINAL OBLIGATORIO

Responde en español y entrega exactamente estas secciones:

## A. ESTADO GIT OBSERVADO

- repository_root
- current_branch
- HEAD
- HEAD_tree
- local_main
- origin_main
- local_execution_branch_exists
- local_execution_branch_sha
- tracked_clean
- untracked_paths (lista completa)
- git_operation_in_progress

## B. PATH DEL FALLO

Para cada componente de la cadena:

- absolute_path
- exists
- object_type
- attributes
- reparse/link status
- owner
- ACL relevante
- inheritance
- filesystem/volume

## C. IDENTIDAD DEL PROCESO

- effective_user
- relevant_groups
- relevant_privileges
- shell
- python_executable
- python_version
- repository_location_context

## D. DEFENDER / CFA

- CFA_status
- protected_folder_match
- relevant_allowed_application
- relevant_block_event_found
- event evidence, si existe

## E. LOCK / REPARSE / SYNC

- collision_found
- reparse_found
- sync_context
- lock_owner
- evidence

## F. PUNTO DE FALLO CONTRACTUAL

- runtime_root
- runtime_authorization_record
- code_path
- function
- mkdir_before_write
- EV03_started_expected = false si el mkdir fue el fallo real

## G. DIAGNÓSTICO

Una sola clasificación:

`ROOT_CAUSE_CONFIRMED`

o
`ROOT_CAUSE_PROBABLE`

o
`ROOT_CAUSE_UNRESOLVED_READONLY`

Después:

- causa o hipótesis;
- evidencia a favor;
- evidencia en contra / faltante;
- nivel de confianza.

## H. REMEDIACIÓN PROPUESTA, NO EJECUTADA

Máximo 3 acciones, ordenadas de mínima a mayor intervención.

## I. CONFIRMACIÓN DE NO INTERVENCIÓN

Confirma explícitamente:

- runner_invocations = 0
- files_created_in_repo = 0
- directories_created_in_repo = 0
- files_modified_in_repo = 0
- files_deleted_in_repo = 0
- permissions_changed = false
- defender_changed = false
- processes_terminated = 0
- commits_created = 0
- pushes = 0

## J. ESTADO CIENTÍFICO

Debe seguir exactamente:

- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`

Finaliza y detente. No ejecutes ninguna acción correctiva ni un segundo intento numérico.