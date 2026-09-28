# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.21
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-100
CANONICAL_MASTER = ARTICLE_MASTER_V018
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V018.md
CANONICAL_MASTER_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
CANONICAL_MASTER_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B03_SECTION_5_3_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B03_V01_ONLY
RESULTS_B04_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V018.md` es el master Markdown canónico verificado. La promoción B02 V02 fue byte-exacta y está registrada en D-098.

El Word acumulativo canónico es `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx`, SHA-256 `3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9`, bajo custodia local del autor, con 40 comentarios preservados y 0 tracked changes.

Experimental Design, Results B01 / §5.1 y Results B02 / §5.2 están cerrados, aprobados, congelados e integrados.

## 2. Estructura congelada de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = OPEN / AUTHORIZED B03 V01
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B03 / Section 5.3

Ground truth:

`article/governance/D099_RESULTS_B03_GROUND_TRUTH_SYNC_AND_SECTION5_3_BOUNDARY.md@dfb21f5ba6c1d8b8b7cc7f30945ead8ae284ce76`

Snapshot experimental congelado:

`db0d0ad0d8435921a7838db6720eaea86a263763`

Fuentes primarias:

```text
integration_metrics.json
GIT_BLOB = 3fddeba15d080468001b1a855749ab23b1f0f0fb

integration_evidence_coverage.json
GIT_BLOB = f8a746933655864cda005f14b41938ae750ec9e5

integration_ranking_invariance.json
GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd

integration_label_leakage_audit.json
GIT_BLOB = cad4b3c5daee8988ecd56a38d6150d98cdd96d94

integration_compatibility.json
GIT_BLOB = 1d9070daea5875f47d9a10cbe714880fc9a06bf2
```

Ground truth principal:

```text
EVAL_CASES = 1056
CANDIDATE_SLOTS = 3168
EXACT_NANDINA8_EVIDENCE = 3168/3168 = 100%
CASE_ALL_TOP3_EXACT_EVIDENCE = 1056/1056 = 100%
HS6_CONTEXT = 2168/3168 = 68.43%
HS4_CONTEXT = 3168/3168 = 100%
CHAPTER_CONTEXT = 3168/3168 = 100%
HISTORICAL_PRECEDENT_COVERAGE = 3168/3168 = 100%
TRACEABILITY_COMPLETE = 3168/3168 = 100%
RANKING_INVARIANCE = 1056/1056 = 100%
```

Los claims C30-C34 fueron registrados en `article/CLAIM_EVIDENCE_MATRIX.md@55476e0d618d979cd1eaf1637aaaff23fe128371` antes de abrir drafting. C12 permanece prohibido: association/coverage no demuestra substantive normative correctness. C21 mantiene el límite de drift del corpus congelado.

## 4. Contrato activo

Prompt:

`article/prompts/6_RESULTS_B03_SECTION5_3.md@10ab3bc7609eda2bbd68cd2e3d3ce27c2d54dbcb`

Git blob:

`f60bd17046ab981bd71f104486e9d7a3acc2be67`

Revisión:

`article/reviews/6_RESULTS_B03_SECTION5_3_PROMPT_INTERNAL_REVIEW_V01.md@ac22162132cdd5e26b341385edd14db50129b0f4` — `PASS`.

Autorización:

`article/governance/D100_RESULTS_B03_SECTION5_3_EXECUTION_AUTHORIZATION.md@20fc83f09cd0eefe90a988274d740d00969a7b05`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V018.md
BASELINE_MASTER_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
BASELINE_MASTER_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx
BASELINE_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo: Base64 manual, chunking, fragmentación y reensamblado están prohibidos. El DOCX no se reconstruye desde Markdown y los candidatos acumulativos deben entregarse como archivos reales.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B03_SECTION_5_3
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B03_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B03_SECTION5_3_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V018 is the canonical verified Markdown master; the approved B02 V02 DOCX is the canonical cumulative Word baseline. Results B01 and B02 are integrated. Results B03 / §5.3 is the only open drafting block under D-099/D-100 and the exact prompt `article/prompts/6_RESULTS_B03_SECTION5_3.md@10ab3bc7609eda2bbd68cd2e3d3ce27c2d54dbcb`.

```text
CURRENT_GATE = RESULTS_B03_SECTION_5_3_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
RESULTS_B03 = AUTHORIZED
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```