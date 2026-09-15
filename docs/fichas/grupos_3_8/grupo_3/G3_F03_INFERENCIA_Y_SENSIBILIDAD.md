# G3-F03 — Inferencia y análisis de sensibilidad

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Ejecutar únicamente los contrastes preespecificados en G3-F01 sobre el registro aprobado de G3-F02.

## Reglas metodológicas

- la elección de prueba debe estar fijada antes de observar el resultado final y considerar dependencia intra-DAM;
- reportar estimación, incertidumbre, tamaño de efecto y denominador, no solo significancia;
- multiplicidad debe seguir el contrato G3-F01; no añadir familias post hoc;
- EXP11A se analiza como sensibilidad conjunta tamaño/composición; cualquier contraste D1/D2 debe respetar su diseño pareado/estratificado;
- EXP11B puede evaluar diferencia H150/H200 solo con la unidad inferencial y emparejamiento realmente soportados por el diseño;
- correcciones 0B-05C se incorporan como estado científico vigente, sin reabrir resultados supersedidos;
- EXP12 no recibe test de efecto porque no materializó condiciones oficiales.

## Outputs

- `outputs/analysis/group3/g3_inferential_results_v0.1.csv`
- `outputs/analysis/group3/g3_inferential_results_v0.1.json`
- `docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md`

## PASS

Cada contraste coincide con G3-F01, usa la unidad correcta, registra supuestos/diagnósticos y no existe overclaim causal.

**Siguiente:** G3-F04.
