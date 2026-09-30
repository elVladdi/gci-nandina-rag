# FAST-F02 Author Fields Deferral V01

## Author instruction

The Author explicitly instructed Managing AI to stop delaying the article over author/administrative metadata and to leave those fields blank for later manual completion.

This instruction supersedes the earlier FAST-F02 author-data collection gate for the purpose of article finalization.

## Disposition

```text
AUTHOR_METADATA_TASK = CLOSED / INTENTIONALLY_BLANK
CORRESPONDING_AUTHOR_FIELD = BLANK / AUTHOR_TO_COMPLETE_LATER
CREDIT_FIELD = BLANK / AUTHOR_TO_COMPLETE_LATER
FUNDING_FIELD = BLANK / AUTHOR_TO_COMPLETE_LATER
COMPETING_INTERESTS_FIELD = BLANK / AUTHOR_TO_COMPLETE_LATER
ACKNOWLEDGEMENTS_FIELD = BLANK / AUTHOR_TO_COMPLETE_LATER

PREVIOUSLY_SUPPLIED_AUTHOR_FACTS =
PRESERVED_IN_GOVERNANCE_ONLY / NOT_INSERTED_IN_ARTICLE_BY_FAST_F02

FAST_F02_BLOCKER_FROM_AUTHOR_METADATA = NONE
```

## Existing generative-AI declaration

The already approved generative-AI declaration is not treated as author metadata to be re-collected. It remains frozen and should be preserved unchanged unless the Author later explicitly requests a factual correction.

## Article rendering rule

FAST-F02 Writing AI must:

- leave the author/title-page metadata area unfilled if it is currently unfilled;
- retain the End Matter headings for CRediT, Funding, Competing interests and Acknowledgements but leave their bodies blank;
- remove drafting placeholders such as `[Section text to be drafted in a later approved version.]` from those intentionally blank sections;
- not infer, synthesize or insert author facts from earlier governance records;
- not treat the blank fields as blockers;
- continue with content-bearing FAST-F02 work.

## Status

```text
AUTHOR_FACTS_GATE = CLOSED_BY_AUTHOR_INSTRUCTION
AUTHOR_ADMINISTRATIVE_FIELDS = FINALIZED_AS_BLANK_FOR_CURRENT_ARTICLE_WORKFLOW
NEXT = PREPARE_SINGLE_FAST_F02_WRITING_PROMPT
```
