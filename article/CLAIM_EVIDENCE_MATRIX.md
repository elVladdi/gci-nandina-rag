# Matriz claim–evidencia / Claim–Evidence Matrix

## Español

Esta matriz controla qué afirmaciones pueden utilizarse en el manuscrito. Un claim no puede pasar a `AUTHORIZED` sin evidencia verificable. Los únicos estados permitidos son: `AUTHORIZED`, `CONDITIONAL`, `PENDING`, `PROHIBITED`, `REVIEW_REQUIRED`. `AUTHORIZED` significa que el claim dispone de evidencia elegible dentro del alcance indicado; no abre por sí mismo una sección cuyo gate editorial permanezca cerrado.

| ID | Claim | Evidencia actual | Estado | Uso permitido |
|---|---|---|---|---|
| C01 | La recuperación histórica genera y ordena los candidatos principales | arquitectura/metodología vigente | AUTHORIZED | Methods / arquitectura |
| C02 | La recuperación normativa aporta evidencia documental para candidatos y no reemplaza el ranking histórico | arquitectura/metodología vigente | AUTHORIZED | Methods / Discussion |
| C03 | El LLM local explica un Top-3 previamente recuperado y no clasifica desde cero | arquitectura/metodología vigente | AUTHORIZED | Methods / arquitectura |
| C04 | En H100, el código de referencia aparece en el Top-3 histórico en 709/1056 casos (67.14%) | benchmark congelado H100 | AUTHORIZED | Results; denominar candidate retrieval, no accuracy global |
| C05 | En H100, Top-1=50.95%, Top-5=76.33%, Top-10=89.11%, Top-50=99.15% y MRR=0.6297077493524843 | benchmark congelado H100 | AUTHORIZED | Results con definición métrica explícita |
| C06 | El split v0.2 evita solapamiento de DAM entre histórico, desarrollo y evaluación | protocolo/split v0.2 auditado | AUTHORIZED | Methods / validity |
| C07 | La evaluación debe considerar dependencia intra-DAM cuando la inferencia requiera independencia | estructura de datos + metodología de agrupamiento | AUTHORIZED | Methods/statistics; resultados inferenciales trazados a Grupo 3 |
| C08 | EXP-11A evidencia sensibilidad descriptiva bajo restricciones naturales de composición | G3-F02 + G4-F01 `G4F01-0007`; G4-F03 `ADP-005` | AUTHORIZED | Results/Discussion únicamente como sensibilidad conjunta tamaño/composición; no aislar efecto causal del tamaño |
| C09 | EXP-11A estima el efecto causal aislado del tamaño del banco histórico | no sustentado; G4-F03 `FDP-004` | PROHIBITED | No usar |
| C10 | Aumentar el banco histórico a H150/H200 mejora el rendimiento como conclusión general o causal | EXP-11B descriptivo; G4-F03 `ADP-006`, `FDP-005` | PROHIBITED | No usar; usar C26 para el resultado descriptivo autorizado |
| C11 | Aumentar H150/H200 empeora, estabiliza o no afecta el rendimiento como conclusión general | no existe superpoblación congelada de seeds; G4-F03 `FDP-005` | PROHIBITED | No usar; usar C26 |
| C12 | La evidencia normativa asociada a un candidato demuestra corrección normativa sustantiva | evidencia insuficiente; G4-F03 `FDP-010` | PROHIBITED | No convertir asociación/coverage en correctness |
| C13 | Las explicaciones HE4 demuestran corrección jurídica completa | limitaciones HE4 + G4-F03 `FDP-011` | PROHIBITED | No usar |
| C14 | HE4 aporta evidencia sobre estructura, trazabilidad y auditabilidad bajo su protocolo de evaluación | evaluación HE4 existente | CONDITIONAL | Solo con límites explícitos |
| C15 | El framework puede configurarse para otros capítulos, niveles o jurisdicciones | propiedad de diseño documentada; no generalización empírica | AUTHORIZED | Methods/Reproducibility; solo como propiedad de diseño |
| C16 | El enfoque ha demostrado generalización empírica fuera de Clase 87 | no evaluado | PROHIBITED | No usar |
| C17 | El protocolo separa reproducción del estudio de referencia y replicación externa con datos independientes | protocolo/repositorio de reproducibilidad | AUTHORIZED | Reproducibility; propiedad del protocolo |
| C18 | El estudio produce clasificaciones aduaneras jurídicamente vinculantes | fuera de alcance | PROHIBITED | No usar |
| C19 | En el split v0.1, 995/1006 casos de evaluación pertenecían a DAM también presentes en histórico | artefacto experimental v0.1 auditado/congelado | AUTHORIZED | Methods / validity; identificar como snapshot histórico |
| C20 | En el split v0.1, 48/59 DAM de evaluación estaban también presentes en histórico | observación reportada sin artefacto versionado localizado para recomputación auditable | REVIEW_REQUIRED | No usar como cifra congelada |
| C21 | El snapshot NANDINA ingerido conservaba texto derivado de Decisión 885 pese a vigencia de Decisión 906; hubo drift y solapamiento material en Capítulo 87 para `8704.41.10` y `8704.51.10` | auditoría 0B-05C + fuentes oficiales + reconciliación experimental | AUTHORIZED | Methods/Validity/Limitations; no inferir legal correctness ni impacto métrico desde drift solo |
| C22 | En la sensibilidad correctiva final 0B-05C, EV03 presentó `ZERO_AGGREGATE_CHANGE` | Attempt06 auditado e integrado | AUTHORIZED | Results/Discussion como sensibilidad acotada; no causalidad/significancia |
| C23 | En 0B-05C, EV04 presentó `TINY_NONZERO_MRR_DECREASE_ONLY` | Attempt06 + interpretación final corregida | AUTHORIZED | Results/Discussion restringido a MRR y diseño ejecutado |
| C24 | En 0B-05C, D1a presentó `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT` | Attempt06 + interpretación final corregida | AUTHORIZED | Results/Discussion como efecto específico; no generalizar |
| C25 | El impacto conjunto 0B-05C fue `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`; `DOWNSTREAM_REEXECUTION = NOT_REQUIRED` | cierre 0B-05C + G4-F03 `ADP-007` | AUTHORIZED | Síntesis metodológica; no resumir como impacto global cero ni inferir causalidad/significancia |
| C26 | EXP-11B aporta sensibilidad descriptiva pareada H150/H200 sobre diez seeds pareados en el mismo EVAL de 1056 series | G3-F02 + G4-F01 `G4F01-0008` + G4-F03 `ADP-006` | AUTHORIZED | Results/Discussion descriptivos; sin inferencia a superpoblación de seeds/casos |
| C27 | El efecto de diversidad histórica previsto por EXP-12 no es estimable porque no se produjeron retrievals D-HIGH/D-MID/D-LOW | G3-F02 + G4-F01 + G4-F03 `ADP-008` | AUTHORIZED | Results/Discussion/Limitations; no inviabilidad global ni evidencia para HE5 |
| C28 | HE2 queda `SUPPORTED` dentro del alcance inferencial congelado: HE2_A y el contraste primario HE2_B están apoyados; Phase E es solo direccionalmente consistente en plano descriptivo | cierre G3-F04 + G4-F01 + G4-F03 `ADP-001` | AUTHORIZED | Results/Discussion cuando gate lo permita; contraste con literatura solo interno/cualitativo según G4-F03; no accuracy global ni causalidad externa |
| C29 | HE5 queda `INCONCLUSIVE` | cierre G3-F04 + G4-F01; G4-F03 conserva EXP12 no estimable | AUTHORIZED | Results/Discussion/Limitations; no supported/rejected ni usar EXP12 como evidencia positiva/negativa |

### Control de contraste con literatura — Grupo 4 cerrado

El cierre canónico de Grupo 4 incorpora como overlay obligatorio para futura `Discussion` el artefacto `docs/analysis/group4/g4_literature_contrast_v0.1.md` (`main@38e22c19a0eb0d344e7675761a88d7968091eead`). Contiene 11 registros de contraste, 8 puntos autorizados (`ADP-001..ADP-008`) y 14 prohibidos (`FDP-001..FDP-014`).

Cuando se abra el gate de Discussion, solo pueden emplearse contrastes dentro de esos límites. En particular permanecen prohibidos: superioridad numérica cross-study no comparable; SOTA; novelty absoluta/primero/unicidad/gap definitivo no gobernado; causalidad de tamaño para EXP11A; generalización de EXP11B a una superpoblación de seeds; impacto global cero de 0B-05C; inviabilidad global o evidencia HE5 derivada de EXP12; accuracy global RAG derivada del retrieval histórico; corrección jurídica derivada de evidencia normativa; validación de clasificación derivada de explicación auditable; leakage atribuido a antecedentes por ausencia de group split; y equivalencias entre path validity/rationale/provenance/reproducibility y legal correctness/auditabilidad por salida/correctness.

`FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen sin cambios.

### Regla de actualización

Todo nuevo resultado experimental debe agregarse aquí con fuente, alcance y estado antes de aparecer en el manuscrito. El cierre de Grupo 4 no recalculó métricas ni inferencia: añadió control de interpretación y contraste con literatura. La elegibilidad de evidencia no sustituye el gate editorial.

---

## English

This matrix controls which claims may be used in the manuscript. `AUTHORIZED` means that a claim has eligible evidence within the stated scope; it does not itself open a manuscript section whose editorial gate remains closed.

| ID | Claim | Current evidence | Status | Permitted use |
|---|---|---|---|---|
| C01 | Historical retrieval generates and ranks the primary candidates | current architecture/methodology | AUTHORIZED | Methods / architecture |
| C02 | Normative retrieval provides documentary evidence for candidates and does not replace historical ranking | current architecture/methodology | AUTHORIZED | Methods / Discussion |
| C03 | The local LLM explains a previously retrieved Top-3 and does not classify from scratch | current architecture/methodology | AUTHORIZED | Methods / architecture |
| C04 | In H100, the reference code appears within historical Top-3 in 709/1056 cases (67.14%) | frozen H100 benchmark | AUTHORIZED | Results; candidate retrieval, not overall accuracy |
| C05 | H100 Top-1=50.95%, Top-5=76.33%, Top-10=89.11%, Top-50=99.15%, MRR=0.6297077493524843 | frozen H100 benchmark | AUTHORIZED | Results with explicit metric definition |
| C06 | The v0.2 split prevents DAM overlap across historical, development, and evaluation partitions | audited v0.2 protocol/split | AUTHORIZED | Methods / validity |
| C07 | Evaluation must account for intra-DAM dependence when inference requires independence | data structure + grouping methodology | AUTHORIZED | Methods/statistics; inferential results traced to Group 3 |
| C08 | EXP-11A provides descriptive sensitivity under natural composition constraints | G3-F02 + G4-F01 + G4-F03 `ADP-005` | AUTHORIZED | Joint size/composition sensitivity only; no isolated causal size effect |
| C09 | EXP-11A estimates an isolated causal effect of historical-bank size | unsupported; G4-F03 `FDP-004` | PROHIBITED | Do not use |
| C10 | Increasing the historical bank to H150/H200 improves performance as a general/causal conclusion | descriptive EXP-11B; G4-F03 `ADP-006`, `FDP-005` | PROHIBITED | Use C26 instead |
| C11 | H150/H200 worsens, stabilizes, or has no effect as a general conclusion | no frozen seed superpopulation; G4-F03 `FDP-005` | PROHIBITED | Use C26 instead |
| C12 | Normative evidence associated with a candidate demonstrates substantive normative correctness | insufficient evidence; G4-F03 `FDP-010` | PROHIBITED | Do not convert association into correctness |
| C13 | HE4 explanations demonstrate complete legal correctness | HE4 limitations + G4-F03 `FDP-011` | PROHIBITED | Do not use |
| C14 | HE4 provides evidence about structure, traceability, and auditability under its protocol | existing HE4 evaluation | CONDITIONAL | Explicit limitations required |
| C15 | The framework can be configured for other chapters, levels, or jurisdictions | documented design property; not empirical generalization | AUTHORIZED | Methods/Reproducibility |
| C16 | Empirical generalization beyond Chapter 87 has been demonstrated | not evaluated | PROHIBITED | Do not use |
| C17 | The protocol separates reproduction from external replication with independent data | reproducibility protocol/repository | AUTHORIZED | Reproducibility |
| C18 | The study produces legally binding customs classifications | outside scope | PROHIBITED | Do not use |
| C19 | In v0.1, 995/1006 evaluation cases belonged to DAMs also present in historical data | audited/frozen v0.1 artifact | AUTHORIZED | Methods/validity as historical snapshot |
| C20 | In v0.1, 48/59 evaluation DAMs were also present in historical data | reported observation without located versioned auditable artifact | REVIEW_REQUIRED | Do not use as frozen figure |
| C21 | The ingested NANDINA snapshot retained Decision-885-derived text despite Decision 906 being in force; material Chapter-87 drift overlap was confirmed for `8704.41.10` and `8704.51.10` | 0B-05C audit + official sources + final reconciliation | AUTHORIZED | Methods/Validity/Limitations; no legal correctness or metric impact from drift alone |
| C22 | Final 0B-05C corrective sensitivity EV03 showed `ZERO_AGGREGATE_CHANGE` | audited/integrated Attempt06 | AUTHORIZED | Bounded sensitivity only |
| C23 | EV04 showed `TINY_NONZERO_MRR_DECREASE_ONLY` | Attempt06 + corrected interpretation | AUTHORIZED | Restricted to MRR/executed design |
| C24 | D1a showed `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT` | Attempt06 + corrected interpretation | AUTHORIZED | Method-specific sensitivity; no generalization |
| C25 | Joint 0B-05C impact was `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`; `DOWNSTREAM_REEXECUTION = NOT_REQUIRED` | 0B-05C closure + G4-F03 `ADP-007` | AUTHORIZED | Do not reduce to global-zero impact or significance |
| C26 | EXP-11B provides paired descriptive H150/H200 sensitivity across ten paired seeds on the same 1,056-series EVAL | G3-F02 + G4-F01 + G4-F03 `ADP-006` | AUTHORIZED | Descriptive only; no seed/case superpopulation inference |
| C27 | The EXP-12 historical-diversity effect is not estimable because no D-HIGH/D-MID/D-LOW retrievals were produced | G3-F02 + G4-F01 + G4-F03 `ADP-008` | AUTHORIZED | Non-estimability only; no global infeasibility or HE5 evidence |
| C28 | HE2 is `SUPPORTED` within the frozen inferential scope; Phase E is only directionally consistent descriptively | G3-F04 + G4-F01 + G4-F03 `ADP-001` | AUTHORIZED | Results/Discussion when gate opens; literature contrast bounded by G4-F03 |
| C29 | HE5 is `INCONCLUSIVE` | G3-F04 + G4-F01; G4-F03 preserves EXP12 non-estimability | AUTHORIZED | Results/Discussion/Limitations; never supported/rejected from EXP12 |

### Group 4 literature-contrast control

The canonical Group 4 closure adds a mandatory overlay for future Discussion through `docs/analysis/group4/g4_literature_contrast_v0.1.md` at `main@38e22c19a0eb0d344e7675761a88d7968091eead`: 11 comparison records, 8 authorized discussion points, and 14 forbidden discussion points. These controls prohibit unsupported cross-study numerical superiority, SOTA, absolute novelty, seed-superpopulation inference, unsupported causality, global infeasibility claims, legal-correctness equivalences, and other scope expansions listed in `FDP-001..FDP-014`.

`FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain unchanged. Group 4 closure added interpretation/contrast control and did not recompute metrics or inference. Editorial gates remain independent.
