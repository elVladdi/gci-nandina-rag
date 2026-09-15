# ESTADO ADMINISTRATIVO — PROMPT75 SUPERSEDIDO / NO EJECUTAR

## Propósito

Este registro preserva una decisión explícita posterior a la creación de Prompt75 y evita que un chat futuro interprete erróneamente el número de prompt más alto como bloque activo.

## Disposición

```text
PROMPT75 = SUPERSEDED / DO_NOT_EXECUTE
```

Prompt75 fue creado para realizar dos acciones:

1. integrar la gobernanza prospectiva G3–G8 al Plan Maestro;
2. ejecutar G3-F01 e iniciar controladamente Grupo 3.

Posteriormente, por instrucción expresa del usuario, IA Experimental debía realizar **todo lo pendiente antes de iniciar Grupo 3**, pero **no ejecutar ninguna actividad perteneciente a Grupo 3**.

La primera acción de Prompt75 dejó de ser necesaria porque el candidato de gobernanza G3–G8 ya auditado fue integrado directamente por IA Experimental mediante fast-forward no forzado a la rama canónica del Plan Maestro.

La segunda acción de Prompt75 queda expresamente prohibida hasta una autorización futura independiente del usuario para iniciar Grupo 3.

## Estado verificable al registrar esta supersesión

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238

GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
FICHAS_G3_G8 = REGISTERED_PROSPECTIVELY
GROUP3 = NOT_STARTED
G3-F01 = NOT_ACTIVE / NOT_AUTHORIZED / NOT_EXECUTED
ACTIVE_CODEX_PROMPT = NONE
```

Los SHA anteriores son un checkpoint histórico de esta decisión y deben volver a verificarse al iniciar otro chat; no sustituyen el HEAD vigente.

## Regla para continuidad

- No ejecutar `75_INTEGRAR_GOBERNANZA_G3_G8_Y_EJECUTAR_G3_F01_FREEZE_ANALITICO.md`.
- No inferir que G3-F01 está autorizada por existir la ficha o el prompt histórico.
- Cuando el usuario decida iniciar Grupo 3, crear un **nuevo prompt** dedicado únicamente a la ficha vigente G3-F01, con refs y fuentes reconfirmadas en ese momento.
- Preservar Prompt75 como evidencia histórica; no editarlo ni reutilizarlo.
