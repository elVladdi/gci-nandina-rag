# 0B-05C EV03 historical builder recovery v0.2

## Scope

This prospective candidate recovers the historical EV03 Decision885 indexing semantics without modifying the immutable historical baseline or the global BM25 implementation. It does not authorize or execute any corrected numerical arm.

## Provenance boundary

The historical index metadata records Python 3.11.7, 7,644 indexed documents, average document length `5.793302059173584`, vocabulary size 5,646, active stopwords, and corpus SHA-256 `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.

The historical index and metadata entered Git in `975bc9879ec89cc945d5432ef0bac3b37598f72c`. At that commit, neither `src/bm25_index.py` nor `notebooks/04_BM25_Indexacion_NANDINA.ipynb` was versioned. A Python 3.11 `.pyc` introduced earlier in `689f7436a8e2011b3399140c90c7eb6e777b2026` is classified only as derived evidence from versioned bytecode, not as authentic historical source.

## Recovered policy

`EV03_RECOVERED_HISTORICAL_TOKEN_POLICY = DROP_SINGLE_CHARACTER_TOKENS`

The EV03-only builder retains lowercase/NFKD normalization, alphanumeric token extraction, the 51 frozen Spanish stopwords, `titulo + texto_index` with `texto` fallback, NANDINA-8 filtering, document order, `k1=1.5`, and `b=0.75`. It additionally removes tokens whose length is one. This behavior is not applied to EV04 or to `src/bm25_index.py` globally.

## Gate behavior

The v0.2 preexecution verifier builds only the frozen Decision885 control in dedicated preexecution roots. It requires exact logical index identity and exact full ranking, case-summary, and metric reproduction before producing the candidate gate bundle. Corrected EV03, corrected EV04, D1a, and unified numerical execution remain unauthorized and unexecuted.

The historical source limitation remains explicit:

`AUTHENTIC_HISTORICAL_SOURCE_PY = NOT_VERSIONED_AT_INDEX_CREATION`

The allowed conclusion after all exact checks pass is:

`HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED`
