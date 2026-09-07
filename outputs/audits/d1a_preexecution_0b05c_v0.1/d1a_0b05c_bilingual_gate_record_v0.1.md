# D1a 0B-05C Pre-execution Audit v0.1 / Auditoria pre-ejecucion D1a 0B-05C v0.1

## Spanish

Este registro resuelve prospectivamente la exposicion efectiva de entrenamiento y el solapamiento exhaustivo Top-200 del D1a congelado. No carga pesos, FAISS ni evaluadores, no genera un corpus correctivo y no calcula metricas nuevas.

- Gate: `0B-05C`.
- Main experimental de entrada: `37eaa712bd12914b97e8fc108b96dc6e68c4e460`.
- Exposicion de indice D1a preservada: `CONFIRMED`.
- Exposicion de entrenamiento: `NO_EFFECTIVE_EXPOSURE_IDENTIFIED`.
- Positivos: `NONE_IDENTIFIED`.
- Hard negatives explicitos: `NONE_IDENTIFIED`.
- Exposicion implicita in-batch: `NOT_IDENTIFIED`.
- Solapamiento en Top-200: `NONE_IDENTIFIED`.
- Politica de pesos: `FREEZE_ORIGINAL_D1A_WEIGHTS`.
- Politica de indice: `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`.
- Control primario: `FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT`.
- Control opcional de reproduccion: `REPRODUCIBILITY_CHECK_ONLY`.
- Especificacion D1a: `CLOSED_PROSPECTIVELY`.
- Impacto metrico: `NOT_DETERMINED`.
- Ejecucion numerica D1a: `NOT_AUTHORIZED`.
- Reejecucion downstream: `NOT_YET_JUSTIFIED`.
- Cierre 0B-05C: `NOT_AUTHORIZED`.

La reconstruccion determinista coincide con el metadata real de entrenamiento: 2,950 instancias, 608 batches, seed 2026 y conteos de nivel negativo. La version D1a queda identificada por los commits del runner, selector y configuracion siguientes. El HEAD completo de ejecucion no fue versionado; la limitacion queda preservada sin inferirla como ausencia de evidencia.

### Fuentes experimentales y trazabilidad criptografica

- `docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json`: SHA256 `efed7f1c0b3c0552862fd6f26efb75e3e7549d00593548b383c71d5931c70a2e`.
- `outputs/training/text2trade_mnrl_v0.2/training_metadata.json`: SHA256 `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`; command `python -B -m src.experiments.train_text2trade_mnrl_v02`; started `2026-08-30T05:06:12.903099+00:00`; finished `2026-08-30T05:17:30.522426+00:00`.
- `src/experiments/train_text2trade_mnrl_v02.py` at `a91269ed3b5c52d08511063465be130adf185f0a`: Git blob `0c8bd086c4c2a1774737e603232ddf169430d386`, SHA256 `ce3ae23cb084dbbe248f48b640f3169c999b1a04ccf931ac2d00521a46b5296f`.
- `src/retrieval/text2trade_mnrl_v02.py` at `3f30db4d65faac2e8d8b7ab75aad33119d3bca0b`: Git blob `0d4ecc56ed53bb4016fc0b4a4bec158be4e28798`, SHA256 `47358c8b7242235e1908c219f72509c6822b9cb67be89afb1ce978ccadd00d2b`.
- `src/configs/text2trade_mnrl_v0.2.json` at `c82e6232ef5f0678c3b10fbdb9c3850910aacee0`: Git blob `e30a1d9d5e5f9416e7fa504c5f7bb7fb685146e7`, SHA256 `d5bb787f726330285b1a3d85a2b370a7c37ee055c3d8904225a3b26f18c27254`.
- frozen historical input `data/processed/data_aduanas_historico_clase87_v0.2.csv`: SHA256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- frozen eval input `data/processed/data_aduanas_evalset_clase87_v0.2.csv`: SHA256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- frozen corpus input `data/processed/corpus_rag_v1_index.jsonl`: SHA256 `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- `outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl`: SHA256 `96359579c984b736798b943711b58a9503d38ddb62a576248b720caf05c4570c`; exhaustive scope `1056` cases x `200` candidates.

- `87044110`: positives=0; explicit hard negatives=0; implicit in-batch=NOT_IDENTIFIED (0 co-batch opportunities); evidence=`outputs/training/text2trade_mnrl_v0.2/training_metadata.json` / `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`.
- `87045110`: positives=0; explicit hard negatives=0; implicit in-batch=NOT_IDENTIFIED (0 co-batch opportunities); evidence=`outputs/training/text2trade_mnrl_v0.2/training_metadata.json` / `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`.

Auditoria Top-200 completa: `1056` casos x `200` candidatos. Ocurrencias: `87044110=0`, `87045110=0`, casos afectados=`0`, rango minimo=`None`, rango maximo=`None`.

| affected_code | case_id | rank |
| --- | --- | --- |
| None / Ninguno | - | - |

Acciones no ejecutadas: reentrenamiento, reconstruccion de indice, EV-03, EV-04, D1a correctivo, retrieval H150/H200, metricas nuevas, EXP-12 y cambios editoriales.

Bloqueos residuales: Ningun bloqueo impide esta auditoria forense. El HEAD completo del repositorio de ejecucion es `UNKNOWN`; el runner, selector, configuracion, inputs congelados, seed, conteos de reconstruccion y metadatos documentados proporcionan la vinculacion determinista requerida. La ejecucion numerica D1a permanece prospectivamente no autorizada.

## English

This record prospectively resolves effective training exposure and the exhaustive Top-200 overlap for frozen D1a. It does not load weights, FAISS, or evaluators, does not create a corrected corpus, and does not compute new metrics.

- Gate: `0B-05C`.
- Experimental input main: `37eaa712bd12914b97e8fc108b96dc6e68c4e460`.
- Preserved D1a index exposure: `CONFIRMED`.
- Training exposure: `NO_EFFECTIVE_EXPOSURE_IDENTIFIED`.
- Positive exposure: `NONE_IDENTIFIED`.
- Explicit hard-negative exposure: `NONE_IDENTIFIED`.
- Implicit in-batch exposure: `NOT_IDENTIFIED`.
- Top-200 output overlap: `NONE_IDENTIFIED`.
- Weight policy: `FREEZE_ORIGINAL_D1A_WEIGHTS`.
- Index policy: `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`.
- Primary control: `FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT`.
- Optional control reproduction: `REPRODUCIBILITY_CHECK_ONLY`.
- D1a specification: `CLOSED_PROSPECTIVELY`.
- Metric impact: `NOT_DETERMINED`.
- D1a numerical execution: `NOT_AUTHORIZED`.
- Downstream re-execution: `NOT_YET_JUSTIFIED`.
- 0B-05C closure: `NOT_AUTHORIZED`.

The deterministic reconstruction matches the real training metadata: 2,950 instances, 608 batches, seed 2026, and negative-level counts. The D1a version is identified by the following runner, selector, and configuration commits. The complete execution repository HEAD was not versioned; this limitation is preserved and is not treated as missing training evidence.

### Experimental sources and cryptographic traceability

- `docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json`: SHA256 `efed7f1c0b3c0552862fd6f26efb75e3e7549d00593548b383c71d5931c70a2e`.
- `outputs/training/text2trade_mnrl_v0.2/training_metadata.json`: SHA256 `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`; command `python -B -m src.experiments.train_text2trade_mnrl_v02`; started `2026-08-30T05:06:12.903099+00:00`; finished `2026-08-30T05:17:30.522426+00:00`.
- `src/experiments/train_text2trade_mnrl_v02.py` at `a91269ed3b5c52d08511063465be130adf185f0a`: Git blob `0c8bd086c4c2a1774737e603232ddf169430d386`, SHA256 `ce3ae23cb084dbbe248f48b640f3169c999b1a04ccf931ac2d00521a46b5296f`.
- `src/retrieval/text2trade_mnrl_v02.py` at `3f30db4d65faac2e8d8b7ab75aad33119d3bca0b`: Git blob `0d4ecc56ed53bb4016fc0b4a4bec158be4e28798`, SHA256 `47358c8b7242235e1908c219f72509c6822b9cb67be89afb1ce978ccadd00d2b`.
- `src/configs/text2trade_mnrl_v0.2.json` at `c82e6232ef5f0678c3b10fbdb9c3850910aacee0`: Git blob `e30a1d9d5e5f9416e7fa504c5f7bb7fb685146e7`, SHA256 `d5bb787f726330285b1a3d85a2b370a7c37ee055c3d8904225a3b26f18c27254`.
- frozen historical input `data/processed/data_aduanas_historico_clase87_v0.2.csv`: SHA256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- frozen eval input `data/processed/data_aduanas_evalset_clase87_v0.2.csv`: SHA256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- frozen corpus input `data/processed/corpus_rag_v1_index.jsonl`: SHA256 `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- `outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl`: SHA256 `96359579c984b736798b943711b58a9503d38ddb62a576248b720caf05c4570c`; exhaustive scope `1056` cases x `200` candidates.

- `87044110`: positives=0; explicit hard negatives=0; implicit in-batch=NOT_IDENTIFIED (0 co-batch opportunities); evidence=`outputs/training/text2trade_mnrl_v0.2/training_metadata.json` / `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`.
- `87045110`: positives=0; explicit hard negatives=0; implicit in-batch=NOT_IDENTIFIED (0 co-batch opportunities); evidence=`outputs/training/text2trade_mnrl_v0.2/training_metadata.json` / `3d1c5f3b0a3d0f9bd72e9ab61b60710acd8ff22cb5e8797465cafc217ceff075`.

Complete Top-200 audit: `1056` cases x `200` candidates. Occurrences: `87044110=0`, `87045110=0`, affected cases=`0`, minimum rank=`None`, maximum rank=`None`.

| affected_code | case_id | rank |
| --- | --- | --- |
| None / Ninguno | - | - |

Actions not executed: retraining, index rebuild, EV-03, EV-04, corrective D1a, H150/H200 retrieval, new metrics, EXP-12, and editorial changes.

Residual blockers: No blocker prevents this forensic audit. The complete execution repository HEAD is `UNKNOWN`; the documented runner, selector, config, frozen inputs, seed, reconstruction counts, and run metadata provide the required deterministic linkage. Numerical D1a execution remains prospectively unauthorized.
