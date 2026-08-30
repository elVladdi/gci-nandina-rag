# EXP-04 Fase I - Generacion controlada Top-3 HE4 v0.2

## Freeze y modelo

- Freeze H: `{'actual': '117ebffc1a113dfc2e28aeffc05b3e0b88998e6a245cd05f14d16147fbdc1596', 'expected': '117ebffc1a113dfc2e28aeffc05b3e0b88998e6a245cd05f14d16147fbdc1596', 'pass': True}`.
- Prompt: `src/llm/explain_top3_nandina_prompt_v0.2.md` (`1b56ba51863df4d73c8cd882d9154d32df3339a6292d4f72f61d400876f8b1d0`).
- Modelo: `qwen2.5:7b-instruct` (`845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e`, `Q4_K_M`).
- Backend: `Ollama local`; Ollama `0.32.15`.

## Ejecucion

- Inputs: 50.
- Llamadas intentadas/completadas: 50/50.
- Fallos tecnicos: 0; retries: 0.
- Raw preservadas: 50.
- JSON parseable/no parseable: 50/0.
- Latencia total: 1666.662s.

## Provenance

- Una ejecucion primaria por input en el orden congelado; sin recuperacion, etiquetas, evaluation-only ni Fase G.
- El parseo es tecnico y no reparo respuestas ni aplico controles HE4, rubrica o evaluacion cualitativa.
- Hashes de outputs (el manifiesto excluye su propio hash):
  - `gate_i_pre_generation_check_v0.2.json`: `a36232f0846f9babdf12e48c9779e1c10cae5b406dd91de1db7a06a9a231bfbb`.
  - `he4_generation_execution_v0.2.csv`: `323a79cb2a54601c669e711bb4f698fa328f0c51a9f77998612d46bbfbb9cc80`.
  - `he4_generation_metadata_v0.2.json`: `29b5090f9ed64a3c81aa42a2b3c9805551167d44830227886122a6c3ab1c394b`.
  - `he4_generation_status_v0.2.json`: `d8417a1293de5928c4a227e755506c1969e322f1f97b742df06933aafc50c48e`.
  - `he4_responses_parsed_v0.2.jsonl`: `daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6`.
  - `he4_responses_raw_v0.2.jsonl`: `8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4`.

## Limitaciones

- HE4 permanece pendiente de validacion automatica y evaluacion cualitativa.
- Fase J/K no fue ejecutada.
