# Revisión interna — Prompt B06 / Section 4.7 — V01 / Internal review — B06 Section 4.7 prompt — V01

## Español

```text
REVIEW_ID = B06_SECTION_4_7_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-26
REVIEWER = IA_GESTORA
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
PROMPT_GIT_BLOB = 23159f8e85210c78ccfbb2acec4f5b560e83b984
GROUND_TRUTH = D-072
BASELINE_MASTER = ARTICLE_MASTER_V014
VERDICT = PASS
BLOCKING_DEFECTS = NONE
```

### Auditoría

1. **Onboarding:** PASS. El prompt usa exactamente `START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → task-specific prompt` y después invoca MWDP, SPCCR y las decisiones de continuidad Word relevantes.
2. **Baseline acumulativo:** PASS. V014 se fija por SHA-256 y Git blob; el Word B05 V01 se fija por SHA-256 y se exige stop si no está disponible exactamente. Se prohíbe reconstrucción desde Markdown.
3. **Alcance:** PASS. Solo 4.7 EN/ES puede modificarse; 4.8, Results y posteriores permanecen cerrados.
4. **Inferencia primaria:** PASS. El prompt reproduce el contrato congelado: SERIE como unidad, DAM como cluster, estimando ponderado por series, emparejamiento por caso, 10.000 bootstrap clusters, seed 20263001, matriz común de remuestreo, cinco métricas tempranas, IC percentil bilateral 99% con regla Bonferroni FWER 95%, sin p-values.
5. **Cobertura profunda:** PASS. Solo `Recall@200 - Recall@100`, bootstrap cluster-aware e IC 95%, sin duplicar Pool@200 como contraste confirmatorio.
6. **Medida de efecto:** PASS. Conserva diferencia absoluta pareada y prohíbe medidas estandarizadas post hoc.
7. **Sensibilidad/robustez:** PASS. EXP11A queda como sensibilidad conjunta tamaño/composición; EXP11B descriptivo sin inferencia a superpoblación de seeds; Attempt06 y pools Phase E descriptivos; EXP12 no estimable; categorías HE5 descriptivas/no estimables según contrato.
8. **Separación Methods/Results:** PASS. Se prohíben valores observados, intervalos observados, disposición HE2/HE5 y conclusiones de superioridad.
9. **Claims:** PASS. El prompt exige consultar la matriz vigente y registrar el estado real de cada claim usado. La expresión “claims condicionados por alcance” se entiende como claims cuyo uso tiene límites de alcance; no reasigna su estado de matriz. En particular no autoriza marcar C08/C26/C27 como `CONDITIONAL` si la matriz los mantiene `AUTHORIZED`.
10. **MWDP/DOCX QA:** PASS. Exige continuidad exacta Word, 40 comentarios, 0 tracked changes, OOXML, diff, equivalencia EN/ES, equivalencia MD/DOCX y render completo.
11. **Estilo SPCCR:** PASS. Obliga a prosa operacional, concreta y no organizada por IDs internos.
12. **Experimental review trigger:** ninguno se activa por el prompt: no cambia diseño, métrica, resultado ni evidencia; solo consume el ground truth congelado.

### Dictamen

El prompt es ejecutable sin correcciones previas. Autorizarlo no autoriza Section 4.8 ni Results.

---

## English

```text
REVIEW_ID = B06_SECTION_4_7_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-26
REVIEWER = MANAGING_AI
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
PROMPT_GIT_BLOB = 23159f8e85210c78ccfbb2acec4f5b560e83b984
GROUND_TRUTH = D-072
BASELINE_MASTER = ARTICLE_MASTER_V014
VERDICT = PASS
BLOCKING_DEFECTS = NONE
```

The prompt passes onboarding-order, exact-baseline, scope, inferential-contract, robustness/sensitivity, Methods-vs-Results, claim-control, MWDP/DOCX, bilingual-QA, and SPCCR checks. It preserves the series-weighted estimand with DAM-cluster dependence, the frozen 10,000-replicate bootstrap and interval/multiplicity rules, the single deep-coverage contrast, and all descriptive/not-estimable boundaries. It prohibits observed results and final hypothesis dispositions in Methods. No experimental-review trigger is created because the prompt changes no experimental rule or evidence. The prompt is executable as written; Section 4.8 and Results remain unauthorized.