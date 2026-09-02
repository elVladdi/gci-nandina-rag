# Matriz claim–evidencia / Claim–Evidence Matrix

## Español

Esta matriz controla qué afirmaciones pueden utilizarse en el manuscrito. Un claim no puede pasar a `AUTHORIZED` sin evidencia verificable. Los estados son: `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED`, `REVIEW_REQUIRED`.

| ID | Claim | Evidencia actual | Estado | Uso permitido |
|---|---|---|---|---|
| C01 | La recuperación histórica genera y ordena los candidatos principales | arquitectura/metodología vigente | AUTHORIZED | Methods / arquitectura |
| C02 | La recuperación normativa aporta evidencia documental para candidatos y no reemplaza el ranking histórico | arquitectura/metodología vigente | AUTHORIZED | Methods / Discussion |
| C03 | El LLM local explica un Top-3 previamente recuperado y no clasifica desde cero | arquitectura/metodología vigente | AUTHORIZED | Methods / arquitectura |
| C04 | En H100, el código de referencia aparece en el Top-3 histórico en 709/1056 casos (67.14%) | benchmark congelado H100 | AUTHORIZED | Results; denominar candidate retrieval, no accuracy global |
| C05 | En H100, Top-1=50.95%, Top-5=76.33%, Top-10=89.11%, Top-50=99.15% y MRR=0.6297077493524843 | benchmark congelado H100 | AUTHORIZED | Results con definición métrica explícita |
| C06 | El split v0.2 evita solapamiento de DAM entre histórico, desarrollo y evaluación | protocolo/split v0.2 auditado | AUTHORIZED | Methods / validity |
| C07 | La evaluación debe considerar dependencia intra-DAM cuando la inferencia requiera independencia | estructura de datos + metodología de agrupamiento | AUTHORIZED AS METHOD | Methods/statistics; no inventar resultados inferenciales |
| C08 | EXP-11A evidencia sensibilidad descriptiva bajo restricciones naturales de composición | EXP-11A congelado | CONDITIONAL | Results/Discussion con formulación descriptiva |
| C09 | EXP-11A estima el efecto causal aislado del tamaño del banco histórico | no sustentado | PROHIBITED | No usar |
| C10 | Aumentar el banco histórico a H150/H200 mejora el rendimiento | EXP-11B retrieval pendiente | PROHIBITED UNTIL RESULTS | No usar |
| C11 | Aumentar el banco histórico a H150/H200 empeora, estabiliza o no afecta el rendimiento | EXP-11B retrieval pendiente | PROHIBITED UNTIL RESULTS | No usar |
| C12 | La evidencia normativa asociada a un candidato demuestra corrección normativa sustantiva | evidencia insuficiente para equivalencia automática | PROHIBITED | No convertir association/coverage en correctness |
| C13 | Las explicaciones HE4 demuestran corrección jurídica completa | limitaciones conocidas de auditoría HE4 | PROHIBITED | No usar |
| C14 | HE4 aporta evidencia sobre estructura, trazabilidad y auditabilidad bajo su protocolo de evaluación | evaluación HE4 existente | CONDITIONAL | Solo con límites explícitos |
| C15 | El framework puede configurarse para otros capítulos, niveles o jurisdicciones | diseño del framework/repo reproducibilidad | AUTHORIZED AS DESIGN | Methods/Reproducibility; no como generalización empírica |
| C16 | El enfoque ha demostrado generalización empírica fuera de Clase 87 | no evaluado | PROHIBITED | No usar |
| C17 | El protocolo separa reproducción del estudio de referencia y replicación externa con datos independientes | repo reproducibilidad | AUTHORIZED AS PROTOCOL | Reproducibility |
| C18 | El estudio produce clasificaciones aduaneras jurídicamente vinculantes | fuera de alcance | PROHIBITED | No usar |

### Regla de actualización

Todo nuevo resultado experimental deberá agregarse primero aquí con su fuente, alcance y estado antes de aparecer en el manuscrito.

---

## English

This matrix controls which claims may be used in the manuscript. A claim cannot move to `AUTHORIZED` without verifiable evidence. Status values are: `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED`, `REVIEW_REQUIRED`.

| ID | Claim | Current evidence | Status | Permitted use |
|---|---|---|---|---|
| C01 | Historical retrieval generates and ranks the primary candidates | current architecture/methodology | AUTHORIZED | Methods / architecture |
| C02 | Normative retrieval provides documentary evidence for candidates and does not replace the historical ranking | current architecture/methodology | AUTHORIZED | Methods / Discussion |
| C03 | The local LLM explains a previously retrieved Top-3 and does not classify from scratch | current architecture/methodology | AUTHORIZED | Methods / architecture |
| C04 | In H100, the reference code appears within historical Top-3 in 709/1056 cases (67.14%) | frozen H100 benchmark | AUTHORIZED | Results; describe as candidate retrieval, not overall accuracy |
| C05 | In H100, Top-1=50.95%, Top-5=76.33%, Top-10=89.11%, Top-50=99.15%, and MRR=0.6297077493524843 | frozen H100 benchmark | AUTHORIZED | Results with explicit metric definition |
| C06 | The v0.2 split prevents DAM overlap across historical, development, and evaluation partitions | audited v0.2 protocol/split | AUTHORIZED | Methods / validity |
| C07 | Evaluation must account for intra-DAM dependence when inference requires independence | data structure + grouping methodology | AUTHORIZED AS METHOD | Methods/statistics; do not invent inferential results |
| C08 | EXP-11A provides descriptive evidence of sensitivity under natural composition constraints | frozen EXP-11A | CONDITIONAL | Results/Discussion with descriptive wording |
| C09 | EXP-11A estimates the isolated causal effect of historical-bank size | unsupported | PROHIBITED | Do not use |
| C10 | Increasing the historical bank to H150/H200 improves performance | EXP-11B retrieval pending | PROHIBITED UNTIL RESULTS | Do not use |
| C11 | Increasing the historical bank to H150/H200 worsens, stabilizes, or does not affect performance | EXP-11B retrieval pending | PROHIBITED UNTIL RESULTS | Do not use |
| C12 | Normative evidence associated with a candidate demonstrates substantive normative correctness | insufficient evidence for automatic equivalence | PROHIBITED | Do not convert association/coverage into correctness |
| C13 | HE4 explanations demonstrate complete legal correctness | known HE4 audit limitations | PROHIBITED | Do not use |
| C14 | HE4 provides evidence about structure, traceability, and auditability under its evaluation protocol | existing HE4 evaluation | CONDITIONAL | Only with explicit limitations |
| C15 | The framework can be configured for other chapters, levels, or jurisdictions | framework/reproducibility-repository design | AUTHORIZED AS DESIGN | Methods/Reproducibility; not as empirical generalization |
| C16 | The approach has demonstrated empirical generalization beyond Chapter 87 | not evaluated | PROHIBITED | Do not use |
| C17 | The protocol separates reproduction of the reference study from external replication using independent data | reproducibility repository | AUTHORIZED AS PROTOCOL | Reproducibility |
| C18 | The study produces legally binding customs classifications | outside scope | PROHIBITED | Do not use |

### Update rule

Every new experimental result must first be added here with its source, scope, and status before appearing in the manuscript.
