# FAST-F02 Global Table/Figure Correction V01

## English

Table 1 (Experimental benchmark and evaluation overview) and Figure 1 (Decision-support architecture and authority boundaries) are retained unchanged from the FAST-F02 V01 baseline.

### Table 2 — Observed candidate-retrieval performance by method

Arm-level values are descriptive observations on the fixed EVAL set; no arm-level confidence intervals are attached.

| Method | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | MRR@100 |
| --- | --- | --- | --- | --- | --- | --- |
| Historical BM25 H100 | 0.5095 | 0.6714 | 0.7633 | 0.8911 | 0.9915 | 0.6297 |
| Flat normative BM25 | 0.0275 | 0.0511 | 0.0616 | 0.0653 | 0.0701 | 0.0423 |
| Hierarchical normative BM25 | 0.0265 | 0.0521 | 0.0625 | 0.0653 | 0.0909 | 0.0420 |
| Corrected D1a Text2Trade-inspired MNRL | 0.0009 | 0.0104 | 0.0511 | 0.1780 | 0.3134 | 0.0381 |

### Table 3 — Primary HE2_A paired Historical-minus-comparator contrasts

Each cell reports the paired difference followed by its frozen 99% marginal percentile CI under the prespecified Bonferroni familywise-95% control. No p-values are reported. The contrasts are noncausal and do not establish external validity.

| Metric | Flat normative BM25: Historical − comparator [99% CI] | Hierarchical normative BM25: Historical − comparator [99% CI] | Corrected D1a: Historical − comparator [99% CI] |
| --- | --- | --- | --- |
| Top-1 | 0.4820 [0.3294, 0.6313] | 0.4830 [0.3304, 0.6308] | 0.5085 [0.3647, 0.6535] |
| Top-3 | 0.6203 [0.4898, 0.7575] | 0.6193 [0.4855, 0.7570] | 0.6610 [0.5413, 0.7816] |
| Top-5 | 0.7017 [0.5826, 0.8180] | 0.7008 [0.5824, 0.8171] | 0.7121 [0.5905, 0.8327] |
| Top-10 | 0.8258 [0.7372, 0.8961] | 0.8258 [0.7366, 0.8949] | 0.7131 [0.5495, 0.8607] |
| MRR@100 | 0.5874 [0.4636, 0.7120] | 0.5877 [0.4652, 0.7120] | 0.5916 [0.4873, 0.7061] |

### Table 4 — HE2_B deep-coverage contrast

| Contrast | Recall@100 | Recall@200 | Paired difference | 95% CI | Pool@200 context | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchical Recall@200 - Recall@100 | 0.1013 | 0.3040 | 0.2027 | [0.0668, 0.3416] | 0.3040 | 1056 | 67 |

Pool@200 is context only and is not duplicated as a second confirmatory interpretation.

### Table 5 — Documentary association and ranking invariance

| Control / evidence level | Numerator / denominator | Rate | Interpretation |
| --- | --- | --- | --- |
| Exact NANDINA-8 evidence | 3168/3168 | 1.0000 | Exact candidate-level documentary association |
| HS6 parent context | 2168/3168 | 0.6843 | Hierarchical parent context only |
| HS4 parent context | 3168/3168 | 1.0000 | Hierarchical parent context only |
| Chapter parent context | 3168/3168 | 1.0000 | Hierarchical parent context only |
| Historical-precedent coverage | 3168/3168 | 1.0000 | Candidate-linked historical precedent retained |
| Complete candidate-level traceability | 3168/3168 | 1.0000 | Candidate/precedent/document links reconstructible |
| Top-3 membership and order preserved | 1056/1056 | 1.0000 | Case-level ranking invariance after documentary association |

Parent-context coverage is distinct from exact NANDINA-8 documentary association. These controls do not establish legal or substantive normative correctness.

### Table 6 — Controlled-explanation evaluation summary

| Control / outcome | Result | Rate / score | Interpretation |
| --- | --- | --- | --- |
| Top-3 membership/order preserved | 50/50 | 1.0000 | Fixed candidate set and order preserved |
| Candidate code / historical reference / normative reference / rank consistency | 150/150 slots | 1.0000 | All four candidate-slot controls valid |
| Schema compliance | 0/50 | 0.0000 | Prompt-schema specification mismatch caused by required `advertencias_globales`; not an explanation-quality score |
| Auditable cases | 28/50 | 56.0% | Met the frozen qualitative auditability criterion |
| Non-auditable cases | 22/50 | 44.0% | Did not meet the frozen qualitative auditability criterion |
| Hard violations | 0/50 | 0.0% | No hard violations recorded |
| Generic-normative-warning present | 41/50 | 82.0% | Warning control present |
| Generic-normative-warning missing | 9/50 | 18.0% | Warning control missing |
| Missing-warning subgroup | 1/9 auditable | mean total score 9.67 | Descriptive/noncausal subgroup result |
| Other cases | 27/41 auditable | mean total score 12.17 | Descriptive/noncausal subgroup result |

The warning subgroup comparison is descriptive/noncausal. The eight qualitative dimension means are not duplicated here.

### Figure 2 — Qualitative explanation-dimension profile

Frozen means on the 0–2 rubric: Traceability 2.00; Verifiability 0.54; Historical–normative evidence separation 1.04; Conclusion prudence 1.78; Fixed-Top-3 consistency 1.96; Detection of generic normative evidence 1.68; Candidate comparison 1.46; Utility for human audit 1.26.

Caption: Qualitative explanation-dimension profile for the frozen 50-case sample. Mean scores use the frozen 0–2 rubric and were assigned by `independent_ai_reviewer_01` in `AI_EXPERT_ROLE`. This is an LLM-as-judge descriptive profile, not human scoring; no confidence intervals, p-values, or significance marks are shown. The profile does not establish human validation, legal correctness, or causal faithfulness.

### Table 7 — Historical-bank sensitivity summary

| Condition | Observed runs | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | MRR@100 | Design note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H25 | 10 | 0.493371 | 0.645170 | 0.737405 | 0.843277 | 0.973106 | 0.603787 | Joint size-composition sensitivity |
| H50 | 10 | 0.428598 | 0.597917 | 0.680303 | 0.776042 | 0.930492 | 0.542492 | Joint size-composition sensitivity |
| H75 | 10 | 0.298295 | 0.463352 | 0.548769 | 0.653883 | 0.837121 | 0.414030 | Joint size-composition sensitivity |
| H100 frozen reference | 1 | 0.509470 | 0.671402 | 0.763258 | 0.891098 | 0.991477 | 0.629708 | One frozen reference, not a replicate distribution |
| H150 | 10 observed seed pairs | 0.512689 | 0.689962 | 0.783333 | 0.891572 | 0.989583 | 0.633268 | Paired observed seed constructions; no seed-superpopulation inference |
| H200 | 10 observed seed pairs | 0.514110 | 0.689489 | 0.782008 | 0.895265 | 0.985227 | 0.633310 | Paired observed seed constructions; no seed-superpopulation inference |

### Figure 3 — EXP11A joint size-composition sensitivity

The already approved G6-FIG-03 is promoted from Supplementary to the main body without scientific alteration. It contains 31 observed runs: H25 n=10, H50-D1 n=5, H50-D2 n=5, H75 n=10, and H100 n=1 frozen reference, across Top1/Top3/Top5/Top10/Top50/MRR. The display remains descriptive/noncausal; size and composition vary jointly; no CI, p-values, regression, smoothing, or isolated monotonic size-effect interpretation is supported.

### Figure 4 — Primary HE2 evidence

The former main Figure 2 / G6-FIG-01 is retained without scientific-content change and mechanically renumbered Figure 4. All 15 primary 99% HE2_A intervals lie entirely above zero; no p-values are reported. The separate HE2_B contrast remains bounded to deep retrieval coverage.

## Español

La Tabla 1 (resumen del benchmark experimental y la evaluación) y la Figura 1 (arquitectura de apoyo a la decisión y fronteras de autoridad) se conservan sin cambios desde el baseline FAST-F02 V01.

### Tabla 2 — Desempeño observado de recuperación de candidatos por método

| Método | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | MRR@100 |
| --- | --- | --- | --- | --- | --- | --- |
| BM25 histórico H100 | 0.5095 | 0.6714 | 0.7633 | 0.8911 | 0.9915 | 0.6297 |
| BM25 normativo flat | 0.0275 | 0.0511 | 0.0616 | 0.0653 | 0.0701 | 0.0423 |
| BM25 normativo jerárquico | 0.0265 | 0.0521 | 0.0625 | 0.0653 | 0.0909 | 0.0420 |
| MNRL D1a corregido inspirado en Text2Trade | 0.0009 | 0.0104 | 0.0511 | 0.1780 | 0.3134 | 0.0381 |

Los valores por brazo son descriptivos en el EVAL fijo; no tienen intervalos de confianza por brazo.

### Tabla 3 — Contrastes primarios HE2_A pareados Histórico menos comparador

| Métrica | BM25 normativo flat: Histórico − comparador [IC 99%] | BM25 normativo jerárquico: Histórico − comparador [IC 99%] | D1a corregido: Histórico − comparador [IC 99%] |
| --- | --- | --- | --- |
| Top-1 | 0.4820 [0.3294, 0.6313] | 0.4830 [0.3304, 0.6308] | 0.5085 [0.3647, 0.6535] |
| Top-3 | 0.6203 [0.4898, 0.7575] | 0.6193 [0.4855, 0.7570] | 0.6610 [0.5413, 0.7816] |
| Top-5 | 0.7017 [0.5826, 0.8180] | 0.7008 [0.5824, 0.8171] | 0.7121 [0.5905, 0.8327] |
| Top-10 | 0.8258 [0.7372, 0.8961] | 0.8258 [0.7366, 0.8949] | 0.7131 [0.5495, 0.8607] |
| MRR@100 | 0.5874 [0.4636, 0.7120] | 0.5877 [0.4652, 0.7120] | 0.5916 [0.4873, 0.7061] |

Los IC son los percentiles marginales congelados de 99% bajo el control Bonferroni familywise-95% preespecificado. No se reportan p-values; los contrastes son no causales.

### Tabla 4 — Contraste HE2_B de cobertura profunda

| Contraste | Recall@100 | Recall@200 | Diferencia pareada | IC 95% | Contexto Pool@200 | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchical Recall@200 - Recall@100 | 0.1013 | 0.3040 | 0.2027 | [0.0668, 0.3416] | 0.3040 | 1056 | 67 |

### Tabla 5 — Asociación documental e invariancia del ranking

| Control / nivel de evidencia | Numerador / denominador | Tasa | Interpretación |
| --- | --- | --- | --- |
| Evidencia NANDINA-8 exacta | 3168/3168 | 1.0000 | Asociación documental exacta a nivel de candidato |
| Contexto padre HS6 | 2168/3168 | 0.6843 | Solo contexto jerárquico de nivel superior |
| Contexto padre HS4 | 3168/3168 | 1.0000 | Solo contexto jerárquico de nivel superior |
| Contexto padre capítulo | 3168/3168 | 1.0000 | Solo contexto jerárquico de nivel superior |
| Cobertura de precedente histórico | 3168/3168 | 1.0000 | Precedente histórico vinculado al candidato conservado |
| Trazabilidad completa a nivel de candidato | 3168/3168 | 1.0000 | Vínculos candidato/precedente/documento reconstruibles |
| Composición y orden del Top-3 preservados | 1056/1056 | 1.0000 | Invariancia del ranking a nivel de caso tras la asociación documental |

El contexto padre no sustituye evidencia NANDINA-8 exacta y estos controles no establecen corrección jurídica ni normativa sustantiva.

### Tabla 6 — Resumen de la evaluación de explicación controlada

| Control / resultado | Resultado | Tasa / puntaje | Interpretación |
| --- | --- | --- | --- |
| Composición/orden del Top-3 preservados | 50/50 | 1.0000 | Conjunto fijo de candidatos y orden preservados |
| Código / referencia histórica / referencia normativa / consistencia de rango | 150/150 posiciones | 1.0000 | Los cuatro controles por posición fueron válidos |
| Cumplimiento del esquema | 0/50 | 0.0000 | Incompatibilidad de especificación prompt-esquema por `advertencias_globales`; no es puntaje de calidad |
| Casos auditables | 28/50 | 56.0% | Cumplieron el criterio cualitativo congelado |
| Casos no auditables | 22/50 | 44.0% | No cumplieron el criterio cualitativo congelado |
| Hard violations | 0/50 | 0.0% | No se registraron hard violations |
| Advertencia normativa genérica presente | 41/50 | 82.0% | Control de advertencia presente |
| Advertencia normativa genérica ausente | 9/50 | 18.0% | Control de advertencia ausente |
| Subgrupo sin advertencia | 1/9 auditable | media total 9.67 | Resultado descriptivo/no causal |
| Otros casos | 27/41 auditables | media total 12.17 | Resultado descriptivo/no causal |

### Figura 2 — Perfil de dimensiones cualitativas de la explicación

Las ocho medias son el espejo semántico de la Figura 2 inglesa, con la misma rúbrica 0–2 y las mismas limitaciones: LLM-as-judge, no puntuación humana, sin CI ni p-values, y sin establecer validación humana, corrección jurídica ni fidelidad causal.

### Tabla 7 — Resumen de sensibilidad del banco histórico

| Condición | Ejecuciones observadas | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | MRR@100 | Nota de diseño |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H25 | 10 | 0.493371 | 0.645170 | 0.737405 | 0.843277 | 0.973106 | 0.603787 | Sensibilidad conjunta tamaño-composición |
| H50 | 10 | 0.428598 | 0.597917 | 0.680303 | 0.776042 | 0.930492 | 0.542492 | Sensibilidad conjunta tamaño-composición |
| H75 | 10 | 0.298295 | 0.463352 | 0.548769 | 0.653883 | 0.837121 | 0.414030 | Sensibilidad conjunta tamaño-composición |
| H100 referencia congelada | 1 | 0.509470 | 0.671402 | 0.763258 | 0.891098 | 0.991477 | 0.629708 | Una referencia congelada, no distribución de réplicas |
| H150 | 10 pares de seeds observados | 0.512689 | 0.689962 | 0.783333 | 0.891572 | 0.989583 | 0.633268 | Construcciones observadas pareadas; sin inferencia a superpoblación de seeds |
| H200 | 10 pares de seeds observados | 0.514110 | 0.689489 | 0.782008 | 0.895265 | 0.985227 | 0.633310 | Construcciones observadas pareadas; sin inferencia a superpoblación de seeds |

### Figura 3 — Sensibilidad conjunta tamaño-composición EXP11A

G6-FIG-03 se promueve editorialmente al cuerpo principal sin alterar su contenido científico. Mantiene 31 corridas observadas, los seis paneles y las limitaciones descriptivas/no causales gobernadas.

### Figura 4 — Evidencia primaria HE2

La antigua Figura 2 / G6-FIG-01 se conserva científicamente intacta y se renumera mecánicamente como Figura 4. Los 15 IC primarios de 99% de HE2_A permanecen completamente por encima de cero; no se reportan p-values.

## Presentation-compaction disposition

Full numeric vectors were removed from prose where Tables 2–7 now carry exact comparison values. Interpretation, scope limitations, the diagnostic 20-case reranker summary, and bounded HE2_B interpretation remain prose. Corrective normative-resource sensitivity points to Supplementary Table S6; error hierarchy/support strata point to Supplementary Table S2. No new scientific content, experiment, metric, CI, p-value, inferential test, hypothesis disposition, literature, reference, or claim is introduced.
