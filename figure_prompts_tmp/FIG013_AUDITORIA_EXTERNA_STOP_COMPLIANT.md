# FIG013 — Auditoría externa de IA Experimental

## Dictamen

```text
FIG013_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
FIG013_STOP_COMPLIANT = true
FIG013_EXECUTION_DEFECT = false
FIGURE_6_CANDIDATE_CREATED = false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
FIGURE_5_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó la respuesta `figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md` publicada en `codex/prompts-temporary` y el prompt gobernante `FIG013_REGENERAR_FIGURA6_TESIS_G7_F02.md@2e7a55900b6db32ba6711880e17a3f17ab82dee6`.

El STOP es conforme al contrato. FIG013 obliga a sustituir `H100 ref.` por `H100 (referencia)`, conservar inicialmente posiciones, tamaños y anclajes del renderer G6 y, si el español no cabe, permite ajustes tipográficos locales únicamente en título, subtítulo y nota inferior. A la vez exige ausencia de solapamiento material y tamaño efectivo mínimo >= 8 pt. Por tanto, FIG013 no autoriza reducir, partir, desplazar ni cambiar el anclaje de la etiqueta categórica H100.

La respuesta reporta que, con la sustitución obligatoria y las posiciones congeladas, `H100 (referencia)` se solapa materialmente con `H75` en los seis paneles. La medición declarada no se limita a cajas tipográficas: se verificó intersección real de tinta. Dado que resolverla exige una decisión editorial/visual adicional fuera de las autorizaciones de FIG013, detenerse antes de crear renderer/SVG/PNG/manifest fue la conducta correcta.

No corresponde interpretar `NON_TEXT_SVG_GEOMETRY_MATCH=false` ni `DETERMINISTIC_RERUN_MATCH=false` como fallas observadas: ambos campos son `false` porque no existe candidato sobre el cual ejecutar esas verificaciones.

## Consecuencia de gobernanza

No se reejecutará FIG013 sin una decisión científico-editorial adicional sobre la etiqueta H100. Esa decisión corresponde primero a la **IA Diseñadora y Auditora de Figuras Científicas**. CODEX no debe escoger autónomamente una abreviatura, reducción de fuente, salto de línea, desplazamiento o cambio de anclaje.

El siguiente paso autorizado es un microbloque visual dedicado a resolver la legibilidad de la etiqueta de condición H100 preservando datos, geometría científica, orden categórico y semántica experimental. Hasta su cierre externo, A043 sigue pendiente y 121G permanece no autorizado.
