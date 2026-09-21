# D026 — Technical recovery of ARTICLE_MASTER_V006 placeholder

A connector/operator error created `article/manuscript/ARTICLE_MASTER_V006.md` with placeholder text in commit `9c7b92894f36d18ca996be06136304f5e9939857` after D-025 had already defined the intended promotion target.

This is a non-scientific technical deviation. It does not alter the approved B06 content, the candidate blob, the author approval, or the D-025 scientific decision.

The required recovery is to replace that placeholder path with the exact already-approved B06 candidate Git blob:

`7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`

No history rewrite or force-push is authorized. The erroneous commit remains visible in history; the subsequent corrective tree must restore the intended canonical state.

```text
DEVIATION = PLACEHOLDER_MASTER_CREATED_BY_GESTORA_TOOLING_ERROR
SCIENTIFIC_CONTENT_AFFECTED = NO
HISTORY_REWRITE = NO
RECOVERY_TARGET = article/manuscript/ARTICLE_MASTER_V006.md
RECOVERY_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
D025_SCIENTIFIC_DECISION = UNCHANGED
```
