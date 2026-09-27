# FIG010 — Auditoría externa de adaptación de Figuras 4–5 para G7-F02

## Dictamen

```text
FIG010_EXTERNAL_AUDIT = PASS
FIGURE_4_ADAPTATION_REQUIRED = true
FIGURE_5_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
SCIENTIFIC_STRUCTURE_CHANGE_REQUIRED = false
EDITORIAL_REGENERATION_REQUIRED = true
EXISTING_G6_BINARIES_USABLE_AS_IS_IN_THESIS = false
DOCX_EDIT_AUTHORIZED_NOW = false
121F_AUTHORIZED = false
NEXT_ACTOR = CODEX_FOR_TECHNICAL_DETERMINISTIC_REGENERATION
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

La auditoría externa contrastó la respuesta FIG010 contra los artefactos aprobados de G6 y contra el estado visible de la tesis después de 121E.

### Figura 4

Se confirma que el SVG aprobado `figures/group6/g6_fig_01_he2.svg` contiene rótulos internos/no editoriales visibles como `Attempt06`, `D1a`, `Historical`, `Flat`, `Hierarchical`, `Observed values`, `Paired difference` y otros textos en inglés. Por ello el binario aprobado de G6 no debe insertarse tal cual en la tesis.

La estructura científica aprobada sí debe preservarse sin cambios:

- Panel A: cinco métricas primarias y cuatro series visuales (histórico + tres comparadores), sin IC por brazo;
- Panel B: 15 diferencias pareadas histórico − comparador, con IC congelados del 99 %;
- Panel C: único contraste Recall@200 − Recall@100, con IC congelado del 95 %;
- sin valores p;
- sin duplicar Pool@200 como evidencia confirmatoria;
- benchmark 1 056 series / 67 DAM / 42 NANDINA.

La naturalización propuesta por FIG010 es científicamente equivalente y compatible con Tabla 12 y con el contraste profundo vigente.

### Figura 5

Se confirma que el SVG aprobado `figures/group6/g6_fig_02_phase_e.svg` contiene `Phase E`, `hierarchical_only`, `dual_only`, `hierarchical_first_100`, `hierarchical_80_dual_backfill_20`, `hierarchical_70_dual_backfill_30` y rótulos ingleses. El caption aprobado de G6 contiene además identificadores internos que no deben trasladarse a la tesis.

La estructura científica aprobada debe preservarse:

- 15 puntos = 5 variantes × profundidades 50/100/200;
- eje Y desde 0 hasta 0,35;
- sin líneas de conexión;
- sin IC, valores p, tendencias ajustadas o contrastes inferenciales;
- cuatro variantes descriptivas predefinidas + variante 70/30 como contexto adicional;
- unión diagnóstica excluida del rendimiento ordinario;
- orden científico y peso visual no basados en favorabilidad.

Los 15 valores reportados por FIG010 coinciden con el bloque textual/tabular aprobado en 121E.

### Estado de la tesis

Después de 121E, las Figuras 4 y 5 visibles en el DOCX siguen siendo las figuras legacy. Esto era esperado porque A039/A040 quedaron expresamente fuera de 121E. La sustitución visual no debe hacerse antes de disponer de candidatos regenerados y auditados.

## Regla de adaptación vinculante

La regeneración siguiente será exclusivamente editorial y lingüística. Está prohibido alterar:

- fuentes numéricas;
- estimandos;
- denominadores;
- IC congelados;
- posiciones de marcas de datos;
- escalas y rangos;
- orden de métricas, comparadores, variantes y profundidades;
- roles científicos;
- inferencia;
- estructura de paneles.

Se permite únicamente modificar texto visible, saltos de línea y distribución tipográfica de leyendas/rótulos cuando sea necesario para legibilidad, sin mover la geometría de datos.

Para evitar ambigüedad editorial, en Figura 5 se prefiere como encabezado visible:

```text
Cobertura exacta NANDINA según profundidad y variante
```

frente a la formulación menos natural `del conjunto candidato`. Este ajuste es puramente lingüístico y no requiere reejecutar FIG010.

## Protección de los artefactos G6

Los scripts, SVG y PNG aprobados de G6 son fuente congelada y NO deben sobrescribirse. La adaptación para tesis debe producir scripts y binarios nuevos, con rutas específicas de G7/G7-F02, manteniendo trazabilidad a los originales G6 y a las mismas fuentes científicas.

## Estado terminal

```text
FIG010_EXTERNAL_AUDIT = PASS
FIG010_RERUN_REQUIRED = false
SCIENTIFIC_CORRECTION_REQUIRED = false
NEXT_STEP = GENERATE_THESIS_SPECIFIC_FIGURE_4_AND_5_CANDIDATES
NEXT_STEP_ACTOR = CODEX
DOCX_MUST_REMAIN_UNCHANGED_UNTIL_VISUAL_EXTERNAL_AUDIT = true
121F_AUTHORIZED = false
```
