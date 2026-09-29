# G7-F03 — Focused Experimental re-audit A09+A10 v0.1

```text
FICHA = G7-F03
ROLE = IA_EXPERIMENTAL / AUDITORA_METODOLOGICA
DATE = 2026-09-29
AUTHORIZATION = D-198

FOCUSED_REAUDIT_RESULT = PASS
HAVE_G7F03_A09_AND_A10_BEEN_SATISFIED_WITHOUT_NEW_SCIENTIFIC_CONTRADICTION = YES

G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
G8_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED

ARTICLE_MODIFIED = false
NEW_EXPERIMENT_EXECUTED = false
METRICS_RECOMPUTED = false
NEW_INFERENCE = false
NEW_CI = false
NEW_P_VALUE = false
EXP12_REOPENED = false
G8_F01_STARTED = false
```

## 1. Governing handoff and identities

This focused re-audit executes:

- `article/prompts/15_G7_F03_A09_A10_FOCUSED_EXPERIMENTAL_REAUDIT_V01.md`
- Git blob: `249c632058d6773741e2ade3254bca1ef42ae8ef`
- Authorization: `D-198`
- Article request HEAD: `143cf2d9ce0012354a61a1b8a0a6afa6d0ab1466`

Gestora handoff:

- `article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_INTERNAL_REVIEW_V01.md`
- Git blob: `e08df7d8d1e00c56da6acc48907679af5e3b1682`
- Gestora result: `PASS_FOR_FOCUSED_EXPERIMENTAL_REAUDIT`

Versioned correction artifact:

- `article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md`
- Git blob: `8a4578a992d20dc8f96ab88f08e95e666d4247c5`

Prior Experimental G7-F03 verdict re-read from:

- `docs/writing/group7/g7_f03_article_scientific_review_v0.1.md` @ `bc4ad51a8b219adb8cd9a9beab69cdfb5f7f1875`
- `outputs/audits/group7_closure_v0.1.json` @ `ed4f74610ed73ea76427bef2eef2f4319c698441`

The prior blocking findings were exclusively `G7F03-A09` and `G7F03-A10`.

## 2. G7F03-A09 — method correction

**VERDICT = PASS / SATISFIED**

The versioned A09 paragraphs match the frozen Phase-G protocol in all material fields:

- diagnostic route remains separate from the primary fixed-Top-3 workflow;
- closed v0.2 pool;
- nominal depth 100, observed effective pool size 63–100;
- `historical_first_80_normative_20`;
- deduplication by first appearance;
- uniform random sampling without replacement over sorted eligible case IDs;
- seed 0;
- 20 sampled cases;
- 10 closed candidates per reranker input;
- labels excluded from pool construction, selection, prompt and generation, and used only for evaluation;
- local `qwen2.5:7b-instruct`;
- Ollama local backend / Q4_K_M;
- `temperature=0`;
- JSON response;
- no retry / one attempt per frozen input;
- candidate closure 20/20;
- observed 19 reference-in-pool / 1 reference-out-of-pool;
- no prespecified inferential test;
- no feedback to, replacement of, or authority over the primary historical ranking/fixed Top-3.

Frozen supporting identities include:

- config: `21c7f4840d7ca7cc10a1da14569ad8843d75f3bd`;
- pre-LLM freeze: `c553e8e8cafcb03b0a6360bfa430a28501653209`;
- run metadata: `5daba1ed3f44b2d8906d40588dbe2fcec4bf0e4b`;
- label-leakage audit: `8e94a01cdae1e2c1d873de296ec9dabb66f7f3bd`;
- candidate-closure audit: `1a1bc80f08724c6e9e7a732b512607e5eb318b11`.

No retrospective method, new sampling criterion or new experimental authority was introduced.

## 3. G7F03-A10 — result correction

**VERDICT = PASS / SATISFIED**

The versioned A10 paragraphs accurately report the frozen diagnostic values:

```text
sample_cases = 20
reference_in_pool = 19
reference_not_in_pool = 1

Top-1 = 0.50 -> 0.50
Top-3 = 0.65 -> 0.65
Top-5 = 0.80 -> 0.80
MRR = 0.6326 -> 0.6326

wins/ties/losses = 0/19/0
candidate_closure = 20/20
paired_inference = NOT RUN / NO PRE-SPECIFIED TEST
```

Frozen sources:

- metrics: `15800df93cf77f4f2c6e83ac6cb692be013bbeb3`;
- win/tie/loss: `a4d508070d1ef61abbd09a34a7f0ba76f5013a2a`;
- consolidated summary: `2e356497695551c9df61fb36e70d0cd6d2003daa`.

The wording is correctly descriptive and does **not** assert improvement, degradation, statistical equivalence, non-inferiority, superiority, generalization, or a population-level null effect.

## 4. Direct-contradiction check

**VERDICT = PASS / NO DIRECT SCIENTIFIC CONTRADICTION**

The four A09/A10 paragraphs do not contradict the previously passed scientific core:

| Control | Verdict |
|---|---|
| Primary flow authority | PASS — diagnostic reranker explicitly separate |
| Fixed Top-3 | PASS — no feedback/replacement |
| Documentary-evidence role | PASS — unchanged |
| HE3 disposition | PASS — frozen `HE3-G = SUPPORTED`, `HE3 GLOBAL = SUPPORTED` remains consistent |
| EXP12 closure | PASS — not reopened or reinterpreted |
| Inferential boundaries | PASS — no prespecified test; no inferential claim |
| Benchmark scope | PASS — diagnostic sample only; no generalization claim |

No unrelated section is reopened.

## 5. G5/G6 presentation disposition

The prior scientific disposition remains valid without revision.

### Main body

- `G5-MAIN-01`
- `G5-MAIN-02`
- `G6-FIG-01`

### Supplementary / Appendix

- `G5-SECONDARY-01`
- `G5-SECONDARY-02`
- `G5-APPENDIX-01`
- `G5-APPENDIX-02`
- `G5-APPENDIX-03`
- `G5-APPENDIX-04`
- `G5-APPENDIX-05`
- `G6-FIG-02`
- `G6-FIG-03`

The architecture Figure 1 remains scientifically permissible as an editorial architecture schematic, provided any diagnostic reranker is shown only as a separate lateral route with no feedback to the primary flow and no new result claim.

## 6. Terminal disposition

The two prior MAJOR blocking findings are satisfied and no new direct scientific contradiction was introduced.

```text
G7F03-A09 = PASS / CLOSED
G7F03-A10 = PASS / CLOSED

G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED

G8_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

This status makes G8-F01 eligible under the Experimental Plan; it does **not** start, authorize, or execute G8-F01.

FAST-finalization remains under IA Gestora/Author governance. IA Experimental does not authorize FINAL-F01 on their behalf.

## 7. Stop condition

Prompt 15 is complete. No article branch was modified, no new experiment was executed, and no G8-F01 work was started.

Control returns to:

`IA_GESTORA_DEL_ARTICULO`
