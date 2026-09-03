# Aprobación del autor 0B-04B / 0B-04B Author Approval

## Español

### Identificación

- Bloque: `0B-04B — Fundamentos de RAG, transformación de consultas y grounding`.
- Dictamen interno previo: `PASS WITH MINOR CORRECTIONS`.
- Errores materiales detectados: `0`.
- Reejecución completa por la IA de redacción: `NOT_REQUIRED`.
- Revisión experimental: `NOT_REQUIRED`.
- Fecha de aprobación expresa del autor: `2026-09-03`.

### Aprobación

El autor aprobó expresamente el bloque 0B-04B y autorizó su cierre y congelamiento en GitHub.

La aprobación comprende la integración de las normalizaciones C1–C13 registradas en:

`article/reviews/0B04B_INTERNAL_REVIEW.md`

Quedan aceptadas como gobernantes para el freeze:

1. En Lewis et al., la discrepancia entre el `17%` narrativo y `Both good = 11.7%` de la Tabla 4 se preserva y, si se usa el valor cuantitativo, gobierna `11.7%`; la evaluación humana de 452 pares no constituye una tasa universal de reducción de hallucination.
2. RAG se describe como `retrieval-conditioned generation`, no como hard grounding; RAG-Token no ejecuta un nuevo retrieval por token.
3. REALM se conserva como `RETRIEVAL_AUGMENTED_PRETRAINING / RETRIEVE_THEN_PREDICT`; en Open-QA predice answer spans y no es un seq2seq RAG equivalente a Lewis et al.
4. Fusion-in-Decoder conserva la separación `PASSAGE_FUSION ≠ EVIDENCE_ATTRIBUTION`; los beneficios por aumentar pasajes quedan restringidos a los benchmarks/rangos evaluados.
5. Query2doc se clasifica como `QUERY_EXPANSION / LLM_UPSTREAM_OF_RETRIEVAL`; el pseudo-documento no es evidencia factual ni provenance y los resultados OOD permanecen mixtos.
6. Los incrementos de Query2doc se reportan mediante valores inicial/final o puntos de la métrica cuando corresponda, sin reinterpretarlos automáticamente como porcentajes relativos; la latencia permanece condicionada a su configuración.
7. Rewrite-Retrieve-Read se conserva como `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`; la consulta reescrita puede cambiar retrieval y downstream output, y los claims de hallucination no medidos directamente permanecen secundarios.
8. En Asai et al., evidentiality es task-relative; los labels minados dependen parcialmente del comportamiento del generador base y no equivalen a adjudicación humana independiente universal.
9. En Asai et al., gobiernan cinco datasets pese al caption erróneo `six datasets`.
10. El chequeo humano `95%/96%` valida labels bajo el protocolo descrito y no es accuracy global del generador, provenance accuracy, formal auditability ni legal correctness.
11. `PROVENANCE`, `GROUNDING`, `EVIDENTIALITY` y `FORMAL_AUDITABILITY` permanecen conceptualmente separados.
12. Los resultados de QA/IR/fact verification/dialogue no se transfieren como métricas HS/NANDINA ni como corrección normativa aduanera.
13. 0B-04B solo aporta fronteras metodológicas a F1–F5; no modifica sus estados bibliográficos. G6 permanece eliminado y G7 absorbido en F2.

### Estado autorizado

```text
0B-04B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Esta aprobación cierra 0B-04B. No abre automáticamente 0B-05, 0B-06 o 0C ni autoriza la redacción del manuscrito. La apertura de 0B-05 requiere un cambio posterior explícito.

---

## English

### Identification

- Block: `0B-04B — RAG, query-transformation, and grounding foundations`.
- Prior internal verdict: `PASS WITH MINOR CORRECTIONS`.
- Material errors: `0`.
- Full drafting-AI rerun: `NOT_REQUIRED`.
- Experimental review: `NOT_REQUIRED`.
- Express author-approval date: `2026-09-03`.

### Approval

The author expressly approved 0B-04B and authorized its closure and freeze in GitHub.

Approval includes the integration of C1–C13 from `article/reviews/0B04B_INTERNAL_REVIEW.md`:

1. For Lewis et al., the narrative `17%` versus Table-4 `Both good = 11.7%` discrepancy is preserved and `11.7%` governs quantitative use; the 452-pair human evaluation is not a universal hallucination-reduction rate.
2. RAG is described as `retrieval-conditioned generation`, not hard grounding; RAG-Token does not perform a new retrieval at each token.
3. REALM remains `RETRIEVAL_AUGMENTED_PRETRAINING / RETRIEVE_THEN_PREDICT`; its Open-QA regime predicts answer spans and is not a Lewis-style seq2seq RAG generator.
4. Fusion-in-Decoder preserves `PASSAGE_FUSION ≠ EVIDENCE_ATTRIBUTION`; passage-count gains remain specific to the evaluated ranges/benchmarks.
5. Query2doc remains `QUERY_EXPANSION / LLM_UPSTREAM_OF_RETRIEVAL`; pseudo-documents are not factual evidence or provenance and OOD results remain mixed.
6. Query2doc changes are reported through initial/final metric values or metric-point changes where appropriate rather than automatically as relative percentages; latency remains configuration-specific.
7. Rewrite-Retrieve-Read remains `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`; rewritten queries can alter retrieval and downstream output, while unmeasured hallucination claims remain secondary.
8. Asai et al.'s evidentiality is task-relative; mined labels partly depend on base-generator behavior and are not universal independent human adjudication.
9. Five datasets govern Asai et al. despite the erroneous `six datasets` table caption.
10. The `95%/96%` human check validates labels under the stated protocol and is not generator-wide accuracy, provenance accuracy, formal auditability, or legal correctness.
11. `PROVENANCE`, `GROUNDING`, `EVIDENTIALITY`, and `FORMAL_AUDITABILITY` remain conceptually distinct.
12. QA/IR/fact-verification/dialogue results do not transfer as HS/NANDINA metrics or customs legal/normative correctness.
13. 0B-04B provides methodological boundaries only for F1–F5 and does not change their literature status. G6 remains eliminated and G7 remains merged into F2.

### Authorized state

```text
0B-04B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

This approval closes 0B-04B. It does not automatically open 0B-05, 0B-06, or 0C and does not authorize manuscript drafting. Opening 0B-05 requires a later explicit change.
