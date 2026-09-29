# Editorial Review — KBS-34 table/figure use for FAST finalization V01

## Result

```text
REVIEW_TYPE = KBS_34_VISUAL_PRESENTATION_PATTERN_AUDIT
PURPOSE = BOUND_FAST_F01_TABLE_FIGURE_SCOPE
CORPUS = 34 recent Open Access Knowledge-Based Systems articles
RESULT = USE_MIXED_PROSE_TABLE_FIGURE_PRESENTATION / DO_NOT_CHASE_COUNTS
```

## 1. Corpus signal

A caption-index audit over the governed KBS-34 corpus found:

```text
ARTICLES_AUDITED = 34
ARTICLES_WITH_AT_LEAST_ONE_TABLE = 34 / 34
ARTICLES_WITH_AT_LEAST_ONE_FIGURE = 34 / 34

MEDIAN_DETECTED_TABLES_PER_ARTICLE ≈ 8
MEDIAN_DETECTED_FIGURES_PER_ARTICLE ≈ 9
```

These values are an editorial pattern, not a target quota. The corpus includes papers of different lengths, experimental designs, appendices, and figure densities.

The relevant signal is qualitative: KBS research articles normally distribute scientific communication across prose, tables, and figures rather than forcing dense numerical comparisons into paragraphs.

## 2. Functional pattern

The corpus supports three presentation roles:

### Tables

Use tables when the reader needs exact comparison across several conditions, metrics, configurations, denominators, or attributes.

Tables are especially appropriate for:

- benchmark/configuration inventories;
- multi-metric comparisons;
- exact numerical results;
- uncertainty intervals;
- ablation/sensitivity summaries;
- explicit contrasts that are cumbersome in prose.

### Figures

Use figures when the reader needs to understand:

- architecture or workflow;
- component relationships;
- trends or distributions;
- paired effects and uncertainty patterns;
- multi-condition performance profiles.

Figures should not exist only to repeat a table.

### Prose

Prose should state:

- the scientific interpretation;
- the main takeaway;
- the limitation;
- the relation to the research question.

After a table or figure is inserted, prose should not repeat every cell or mark.

## 3. Constraint from Experimental G7-F03

The focused Experimental re-audit closed G7-F03 and preserved this scientific disposition:

### Main body

- G5-MAIN-01
- G5-MAIN-02
- G6-FIG-01

### Supplementary / Appendix

- G5-SECONDARY-01
- G5-SECONDARY-02
- G5-APPENDIX-01
- G5-APPENDIX-02
- G5-APPENDIX-03
- G5-APPENDIX-04
- G5-APPENDIX-05
- G6-FIG-02
- G6-FIG-03

The architecture Figure 1 remains scientifically permissible as an editorial schematic, provided any diagnostic reranker is represented only as a separate lateral path with no feedback to the primary flow.

## 4. Main-body recommendation for this article

To improve readability without overloading the manuscript, the recommended main-body target is deliberately below the KBS-34 median:

```text
MAIN_BODY_TABLES = 3
MAIN_BODY_FIGURES = 2
```

### Table 1 — Experimental benchmark and partition/evaluation overview

Editorial synthesis from already approved V037 content only.

Purpose:

- move recurring benchmark/partition denominators and roles out of prose;
- make the experimental scope quickly inspectable;
- introduce no new metric, calculation, or claim.

### Table 2 — G5-MAIN-01

Canonical HE2_A primary early-ranking comparison table.

Use the frozen G5 canonical table; do not recompute or redesign its scientific content.

### Table 3 — G5-MAIN-02

Canonical HE2_B deep-coverage table.

Use the frozen G5 canonical table; do not recompute or redesign its scientific content.

### Figure 1 — Decision-support architecture

Editorial architecture schematic based strictly on frozen §3 authority boundaries.

Required flow:

```text
INPUT
-> QUERY NORMALIZATION
-> HISTORICAL RETRIEVAL / RANKING
-> FIXED TOP-3
-> CANDIDATE-SPECIFIC DOCUMENTARY EVIDENCE
-> CONTEXT ASSEMBLY
-> LOCAL LLM EXPLANATION
```

If the diagnostic reranker is displayed, it must be a lateral, explicitly diagnostic branch with no arrow feeding back into the primary ranking or fixed Top-3.

### Figure 2 — G6-FIG-01

Use the already approved primary HE2 figure without changing scientific marks, metrics, uncertainty, ordering, or interpretation.

## 5. Supplementary carry-forward

FAST-F01 should not inflate the main body by adding all approved G5/G6 material.

The seven supplementary G5 tables and G6-FIG-02/G6-FIG-03 remain reserved for FAST-F02 supplementary assembly.

## 6. Anti-duplication rule

For every main-body table or figure:

```text
EXACT_VALUES -> TABLE
PATTERN_OR_RELATION -> FIGURE
INTERPRETATION_AND_LIMITS -> PROSE
```

A table and a figure may coexist only when they answer different reading tasks.

## 7. Editorial compression rule

FAST-F01 may shorten only the prose directly made redundant by the three approved tables or two figures.

It may not:

- delete a scientific qualification;
- change a denominator;
- alter an inferential boundary;
- move a supplementary result into primary evidence;
- change RQ/HE disposition;
- add a new metric or calculation;
- rewrite Discussion/Conclusion globally.

## 8. Disposition

```text
FAST_F01_VISUAL_SCOPE =
3 MAIN TABLES + 2 MAIN FIGURES

SUPPLEMENTARY_VISUAL_SCOPE =
DEFER TO FAST_F02

SCIENTIFIC_REAUDIT_REQUIRED =
NO BY DEFAULT / YES ONLY IF NEW SCIENTIFIC CONTENT IS INTRODUCED

NEXT = FORMALIZE_FAST_F01_BOUNDARY
```
