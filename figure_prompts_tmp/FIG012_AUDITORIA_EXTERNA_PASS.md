# FIG012 — Auditoría externa PASS

## Dictamen

```text
FIG012_EXTERNAL_AUDIT = PASS
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_6_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
SCIENTIFIC_GEOMETRY_CHANGE_REQUIRED = false
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE
DOCX_MODIFIED = false
IMAGE_REGENERATED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó `figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md` @ `be0879c44b9d933bc0591bcf498b5e056cc31b20` contra el prompt FIG012 y las fuentes científicas congeladas de G6/G5.

El dictamen es correcto: G6-FIG-03 es científicamente válido como base, pero no debe insertarse tal cual en la tesis porque conserva texto visible interno y parcialmente en inglés (`EXP11A joint size-composition sensitivity`, subtítulo y nota inferior en inglés). El caption G6 también conserva `EXP11A` como identificador de la fase experimental.

La respuesta FIG012 preserva correctamente el contrato científico:

- seis paneles en orden Top1, Top3, Top5, Top10, Top50 y MRR;
- 31 corridas observadas;
- inventario 10 / 5 / 5 / 10 / 1;
- H50-D1 y H50-D2 como composiciones diferenciadas de la condición intermedia;
- H100 como una única referencia congelada;
- jitter horizontal determinista;
- mismas escalas `[0,1]`, categorías y geometría de puntos;
- ausencia de summaries como marcas, CI, valores p, regresiones, suavizados y conexiones entre condiciones;
- interpretación exclusivamente descriptiva y no causal;
- HE5 permanece INCONCLUSIVE.

También es correcto mantener `H25`, `H50-D1`, `H50-D2`, `H75` y `H100` como identificadores científicos de condición. Las fuentes por corrida muestran que las fracciones realizadas y la composición varían al conservar DAM completas; sustituirlas por porcentajes visuales simples sería menos fiel al diseño. La naturalización de `H100 ref.` a `H100 (referencia)` es editorialmente adecuada.

## Adaptación aprobada

Se aprueba como contrato para la futura regeneración determinística:

```text
Título:
Sensibilidad conjunta del banco histórico a tamaño y composición

Subtítulo:
Solo corridas observadas; análisis descriptivo y no causal; sin resúmenes como marcas, IC, valores p ni tendencias ajustadas

Paneles:
Top1 -> Top-1
Top3 -> Top-3
Top5 -> Top-5
Top10 -> Top-10
Top50 -> Top-50
MRR -> MRR

H100 ref. -> H100 (referencia)

Nota inferior:
Las condiciones representan bancos observados categóricos; H100 es una única referencia congelada. El tamaño y la composición varían conjuntamente.
```

El caption propuesto por FIG012 se aprueba para integración posterior, con lenguaje natural de tesis, eliminación de `EXP11A` y preservación explícita de la naturaleza conjunta tamaño-composición, no causal y de alcance interno.

## Próxima acción autorizada

La regeneración determinística editorial de Figura 6 queda autorizada bajo CODEX. Debe producir un candidato G7 separado, sin modificar G6 ni el DOCX, con verificación de identidad de geometría SVG no textual y determinismo entre ejecuciones.

```text
NEXT_FIGURE_STEP = FIG013 / CODEX
A043_EXECUTED = false
DOCX_EDIT_AUTHORIZED = false
121G_AUTHORIZED = false
```
