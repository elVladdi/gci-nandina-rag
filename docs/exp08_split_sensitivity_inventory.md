# Inventario EXP-08

La version inicial de EXP-08 se publico en `f0a369a`. El microcierre correctivo conserva esa historia y corrige solo semantica, completitud y pruebas de contrato; no reejecuta retrieval ni altera las metricas globales.

- Comparabilidad: `exp08_comparability_audit_v01_vs_v02.json`
- Sensibilidad global: `exp08_global_sensitivity_v01_vs_v02.csv`
- Independencia DAM: `exp08_split_independence_comparison_v01_vs_v02.csv`
- Duplicados por umbral: `exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv`
- Sensibilidad por NANDINA: `exp08_code_sensitivity_v01_vs_v02.csv`
- Cobertura nominal: `exp08_code_coverage_v01_vs_v02.csv`
- Rendimiento estratificado: `exp08_stratified_performance_v01_vs_v02.csv`
- HE2/HE5: `exp08_he2_sensitivity_assessment_v0.2.json`, `exp08_he5_component_assessment_v0.2.csv`, `exp08_final_he5_assessment_v0.2.json`
- Resumen: `summary_exp08.md`
- Manifest correctivo: `gate_exp08_corrective_microclose_manifest_v0.2.json`

Los resultados usan solo artefactos historicos congelados. v0.2 es el benchmark final interno; los deltas son descriptivos y no causales.
