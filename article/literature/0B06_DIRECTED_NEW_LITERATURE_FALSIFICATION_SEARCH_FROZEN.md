# 0B-06 — Freeze editorial / Editorial freeze

## Español

Estado: `APPROVED / FROZEN`.

Registros gobernantes:

- `article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`;
- `article/reviews/0B06_INTERNAL_REVIEW.md`;
- `article/reviews/0B06_AUTHOR_APPROVAL.md`.

Resultado congelado:

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

F1 y F3 son resultados negativos acotados y no prueban novelty. F2 conserva el requisito de un Top-k externo e inmutable y un generador downstream solo explicativo sin alterar candidatos ni retroalimentar clasificación. F5 no puede sostenerse como ausencia general en regulatory AI; cualquier variante posterior debe ser más estrecha y contextual.

## English

Status: `APPROVED / FROZEN`.

Governing records are the 0B-06 response, internal review, and author approval listed above.

Frozen result:

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

F1 and F3 are bounded negative results and do not establish novelty. F2 retains the requirement for an externally fixed immutable Top-k and a downstream explanation-only generator that cannot alter candidates or feed back into classification. Broad F5 cannot be sustained as an absence claim in regulatory AI; any later variant must be narrower and contextual.
