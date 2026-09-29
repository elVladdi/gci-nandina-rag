# Diagnostic Reranker A09+A10 V01

## A09 — Method EN

Separately from the primary fixed-Top-3 workflow, we executed a diagnostic LLM reranking analysis over a closed v0.2 candidate pool with nominal depth 100 and effective size 63–100 candidates per case. The pool used the `historical_first_80_normative_20` strategy, with candidates deduplicated by first appearance. From eligible `case_id` values sorted deterministically, 20 cases were sampled uniformly without replacement with seed 0; each reranker input then contained 10 closed candidates. Reference labels were excluded from case selection and generation and were used only for evaluation. Reranking used `qwen2.5:7b-instruct` through a local Ollama backend with Q4_K_M quantization, `temperature=0`, JSON responses, no retry, and one execution per input. Candidate closure was preserved in 20/20 cases. Nineteen sampled cases had the reference code within the diagnostic pool and one did not; this was an observed property of the sampled set, not a sampling criterion. No inferential test was prespecified for this diagnostic analysis, and its outputs did not feed back into or replace the primary historical ranking or fixed Top-3.

## A10 — Result EN

As a separate diagnostic analysis, the reranker was evaluated on 20 sampled cases: 19 had the reference code within the diagnostic pool and one did not. Top-1 remained 0.50 before and after reranking, Top-3 remained 0.65, Top-5 remained 0.80, and MRR remained 0.6326. Among the 19 cases for which the reference code was present in the pool, wins/ties/losses were 0/19/0. Candidate closure was preserved in 20/20 cases. No paired inferential analysis was performed because no inferential test had been prespecified for this diagnostic evaluation. Thus, within this diagnostic sample, no changes were observed in the reported Top-k metrics or MRR after reranking; these descriptive results do not establish statistical equivalence, non-inferiority, superiority, generalization, or a population-level null effect.

## A09 — Método ES

Separadamente del flujo primario con Top-3 fijo, se ejecutó un análisis diagnóstico de reranking con LLM sobre un pool cerrado v0.2 de profundidad nominal 100 y tamaño efectivo de 63–100 candidatos por caso. El pool utilizó la estrategia `historical_first_80_normative_20`, con deduplicación de candidatos por primera aparición. A partir de los `case_id` elegibles ordenados de forma determinista, se seleccionaron uniformemente 20 casos sin reemplazo con seed 0; cada entrada del reranker contuvo después 10 candidatos cerrados. Las etiquetas de referencia se excluyeron de la selección de casos y de la generación y se utilizaron solo en la evaluación. El reranking empleó `qwen2.5:7b-instruct` mediante un backend Ollama local, con cuantización Q4_K_M, `temperature=0`, respuestas JSON, sin retry y una ejecución por input. El cierre de candidatos se preservó en 20/20 casos. En 19 casos muestreados el código de referencia estaba dentro del pool diagnóstico y en uno no; esta fue una propiedad observada del conjunto muestreado, no un criterio de selección. No se preespecificó una prueba inferencial para este análisis diagnóstico, y sus salidas no retroalimentaron ni sustituyeron el ranking histórico primario ni el Top-3 fijo.

## A10 — Resultado ES

Como análisis diagnóstico separado, el reranker se evaluó sobre 20 casos muestreados: en 19 el código de referencia estaba dentro del pool diagnóstico y en uno no. Top-1 se mantuvo en 0,50 antes y después del reranking, Top-3 en 0,65, Top-5 en 0,80 y MRR en 0,6326. Entre los 19 casos cuyo código de referencia estaba presente en el pool, wins/ties/losses fueron 0/19/0. El cierre de candidatos se preservó en 20/20 casos. No se ejecutó análisis inferencial pareado porque no existía una prueba inferencial preespecificada para esta evaluación diagnóstica. Por tanto, dentro de esta muestra diagnóstica no se observaron cambios en las métricas Top-k reportadas ni en MRR después del reranking; estos resultados descriptivos no establecen equivalencia estadística, no inferioridad, superioridad, generalización ni un efecto nulo a nivel poblacional.

## Internal traceability table — not for manuscript insertion

| Block | Frozen source | Git blob | Use |
|---|---|---|---|
| A09 EN/ES | docs/exp04_phase_g_exp06_historical_reranker_audit.md | `4f343cc713b006a5d92414879520ca69b3e2843a` | Executed diagnostic protocol and boundary |
| A09 EN/ES | src/configs/diagnostic_llm_reranker_v0.2.json | `21c7f4840d7ca7cc10a1da14569ad8843d75f3bd` | Pool/model/runtime configuration |
| A09 EN/ES | outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_run_metadata_v0.2.json | `5daba1ed3f44b2d8906d40588dbe2fcec4bf0e4b` | Sampling, execution and candidate-closure metadata |
| A10 EN/ES | outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_metrics_v0.2.json | `15800df93cf77f4f2c6e83ac6cb692be013bbeb3` | Frozen before/after metrics |
| A10 EN/ES | outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_win_tie_loss_v0.2.json | `a4d508070d1ef61abbd09a34a7f0ba76f5013a2a` | Wins/ties/losses denominator and counts |
| A09+A10 | outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md | `2e356497695551c9df61fb36e70d0cd6d2003daa` | Consolidated diagnostic summary |
| A09+A10 | docs/writing/group7/g7_f03_article_scientific_review_v0.1.md | `bc4ad51a8b219adb8cd9a9beab69cdfb5f7f1875` | G7-F03 correction requirement and interpretation boundary |
| A09+A10 | outputs/audits/group7_closure_v0.1.json | `ed4f74610ed73ea76427bef2eef2f4319c698441` | Experimental audit identity and closure status |
