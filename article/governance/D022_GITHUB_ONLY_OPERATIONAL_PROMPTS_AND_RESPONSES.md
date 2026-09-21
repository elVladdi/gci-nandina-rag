# D022 — GitHub-only operational prompts and responses

## Decision

Effective immediately, operational communication with the Drafting AI is repository-first.

1. Full operational prompts MUST be versioned in GitHub before execution.
2. Full execution responses, reports, findings, hashes, status blocks, warnings, deviations, and handoff information MUST be written to the authorized response file in GitHub.
3. The Drafting AI MUST NOT reproduce the substantive response in chat.
4. If the chat interface requires a terminal message after execution, it may contain only a minimal repository pointer in the form:

   `RESPONSE_VERSIONED_IN_GITHUB = <path>@<commit_sha>`

   No scientific content, QA summary, status block, hashes, findings, explanations, or execution details may be repeated in chat.
5. If execution stops before a commit can be created, the Drafting AI must not provide the substantive stop report in chat. It must create the authorized GitHub response artifact recording the stop condition when repository writing is safe and permitted. If no repository write is permitted by the active prompt, it may return only `EXECUTION_STOPPED / REQUIRES_GESTORA_REVIEW` in chat, without details; the IA Gestora will inspect the repository/session state and issue the next versioned instruction.
6. Any older prompt clause requesting an "informe final en chat" or equivalent is superseded by this decision.
7. The IA Gestora continues to provide the user only the short handoff pointer to the versioned prompt, unless the user explicitly requests the full prompt text.

## Scope

This rule applies to the Drafting AI for all subsequent article blocks, corrections, technical closures, audits, and handoffs on `article/main-manuscript`.

## Rationale

The repository is the authoritative audit trail for prompts and responses. Keeping substantive execution output out of chat prevents divergence between transient chat messages and versioned project state, and preserves reproducible review of the article workflow.
