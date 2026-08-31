# EXP-08: sensibilidad v0.1 vs v0.2

La comparacion es descriptiva y globalmente no pareada: v0.1 tiene 1006 casos y v0.2 tiene 1056. No son evalsets equivalentes; no se realizan pruebas inferenciales ni afirmaciones causales.

v0.2 permanece como benchmark final: su solapamiento DAM historico-evaluacion es cero, frente a 995 DAM de v0.1. La diferencia de metricas refleja sensibilidad entre configuraciones congeladas, no un efecto exclusivo del split: v0.1 tiene profundidad 200, v0.2 profundidad 100 y v0.1 no conserva `run_metadata.json`.

HE2 no se reabre. HE5 queda parcialmente respaldada: se evaluaron proximidad jerarquica, precedentes historicos y alcance interno; calidad descriptiva queda sin evaluar por ausencia de regla congelada por caso.
