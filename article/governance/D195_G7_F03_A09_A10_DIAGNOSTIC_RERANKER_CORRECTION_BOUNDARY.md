# D-195 — Boundary de corrección científica pre-FAST G7-F03 A09+A10

## Español

```text
DECISION = D-195
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
PREVIOUS_DECISION = D-194
TRIGGER = G7-F03 / REVISION_REQUIRED

CANONICAL_MASTER = ARTICLE_MASTER_V036
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V036.md
CANONICAL_MASTER_MD_GIT_BLOB = c9dcbcc376cdb121d30dc2408756a6c95b569a90
CANONICAL_MASTER_MD_SHA256 = 8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx
CANONICAL_MASTER_DOCX_SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
BASELINE_PAGE_COUNT = 72

EXPERIMENTAL_REVIEW_REPORT =
docs/writing/group7/g7_f03_article_scientific_review_v0.1.md
EXPERIMENTAL_REVIEW_REPORT_GIT_BLOB =
bc4ad51a8b219adb8cd9a9beab69cdfb5f7f1875

EXPERIMENTAL_AUDIT_RECORD =
outputs/audits/group7_closure_v0.1.json
EXPERIMENTAL_AUDIT_RECORD_GIT_BLOB =
ed4f74610ed73ea76427bef2eef2f4319c698441

G7_F03_STATUS = REVISION_REQUIRED / EXECUTED / NOT_APPROVED
AUTHORIZED_FINDINGS = G7F03-A09 + G7F03-A10
FAST_FINALIZATION_MODE = BLOCKED_UNTIL_CORRECTION_AND_EXPERIMENTAL_REAUDIT
```

## 1. Motivo y autoridad científica

IA Experimental ejecutó G7-F03 y determinó que V036 es científicamente consistente en el resto del núcleo auditado, pero conserva una omisión material y reparable: no documenta suficientemente el método ni los resultados del reranker LLM diagnóstico ya ejecutado y congelado.

D-195 acepta el dictamen experimental como trigger vinculante para una reapertura científica estrecha y no reabre ningún otro contenido del manuscrito.

Fuentes gobernantes del hallazgo:

- `reranker_run_metadata_v0.2.json` @ `5daba1ed3f44b2d8906d40588dbe2fcec4bf0e4b`;
- `reranker_metrics_v0.2.json` @ `15800df93cf77f4f2c6e83ac6cb692be013bbeb3`;
- `reranker_win_tie_loss_v0.2.json` @ `a4d508070d1ef61abbd09a34a7f0ba76f5013a2a`;
- `docs/exp04_phase_g_exp06_historical_reranker_audit.md` @ `4f343cc713b006a5d92414879520ca69b3e2843a`;
- `src/configs/diagnostic_llm_reranker_v0.2.json` @ `21c7f4840d7ca7cc10a1da14569ad8843d75f3bd`.

## 2. Scope autorizado

La única modificación científica autorizada es:

### A09 — Methods / Experimental Design

Documentar, en el bloque experimental pertinente, que se ejecutó un reranker LLM **diagnóstico y separado del flujo principal** sobre una muestra reproducible de 20 casos.

Debe quedar explícito, sin sobreinterpretación:

- muestra aleatoria uniforme sin reemplazo de 20 `case_id` elegibles, con seed 0;
- pool diagnóstico cerrado construido sobre v0.2;
- profundidad nominal del pool = 100; tamaño efectivo por caso 63–100;
- input al LLM limitado a 10 candidatos cerrados por caso;
- estrategia del pool `historical_first_80_normative_20`;
- modelo local `qwen2.5:7b-instruct`, Ollama local, Q4_K_M, `temperature=0`, JSON, sin retry, una ejecución por input;
- candidate closure 20/20;
- etiquetas usadas solo para evaluación;
- la ruta no alimenta, sustituye ni modifica el fixed Top-3 del flujo principal;
- no existió test inferencial preespecificado para esta evaluación diagnóstica.

La condición observada `reference_in_pool=19` / `reference_not_in_pool=1` puede mencionarse como característica del conjunto diagnóstico siempre que no se presente como criterio de selección.

### A10 — Results

Reportar como resultado diagnóstico separado:

```text
sample_cases = 20
reference_in_pool = 19
reference_not_in_pool = 1

Top-1: 0.50 -> 0.50
Top-3: 0.65 -> 0.65
Top-5: 0.80 -> 0.80
MRR: 0.632638888888889 -> 0.632638888888889

wins = 0
ties = 19
losses = 0
paired_inference = not run; no pre-specified inferential test exists
candidate_closure = 20/20
```

La prosa puede redondear MRR a cuatro decimales (`0.6326 -> 0.6326`) si conserva el mismo valor en ambos lados y no altera ningún cálculo.

## 3. Ubicación editorial autorizada

Para evitar renumeración transversal del manuscrito:

- A09 debe integrarse dentro de `§4.5 Experimental system configuration and execution` y su espejo español `§4.5 Configuración y ejecución del sistema experimental`, después de describir el flujo principal y antes de cerrar la configuración de ejecución.
- A10 debe integrarse al final de `§5.2 Candidate retrieval performance` y su espejo español `§5.2 Desempeño de recuperación de candidatos`, como párrafo(s) explícitamente identificados como análisis diagnóstico separado.

No crear una nueva sección numerada que fuerce renumeración de §5.3–§5.7.

## 4. Scope explícitamente prohibido

No modificar:

- Title/Título;
- Abstract/Resumen;
- Keywords/Palabras clave;
- Related Work;
- arquitectura §3, salvo que sea estrictamente necesario para corregir una contradicción creada por A09+A10; el texto actual ya separa el reranking diagnóstico;
- §4 fuera del bloque mínimo A09;
- §5 fuera del bloque mínimo A10;
- Discussion §6;
- Conclusion §7;
- End Matter;
- referencias;
- Figure 1 placeholder;
- drafting notes;
- cifras o redondeos no relacionados con A09+A10.

No modificar la disposición de HE3. HE3 permanece `SUPPORTED` según las fuentes congeladas, pero esta corrección no debe convertir el diagnóstico en evidencia de mejora de ranking.

## 5. Claims prohibidos

La corrección NO puede afirmar:

```text
RERANKER_IMPROVED_PERFORMANCE
RERANKER_DEGRADED_PERFORMANCE
RERANKER_STATISTICALLY_EQUIVALENT
RERANKER_NONINFERIOR
RERANKER_SUPERIOR
RERANKER_GENERALIZES
RERANKER_IS_PART_OF_PRIMARY_FLOW
RERANKER_CHANGED_FIXED_TOP3
ZERO_DELTA = PROOF_OF_EQUIVALENCE
0/19/0 = INFERENTIAL_EVIDENCE
```

Solo está autorizado describir el resultado observado en la muestra diagnóstica.

## 6. Bilingüismo

La inserción debe materializarse tanto en inglés como en español con equivalencia semántica natural.

Las cifras, denominadores, modelo, restricciones y límites epistemológicos deben ser idénticos entre ambos idiomas.

## 7. Entregables esperados

La IA de Redacción deberá producir:

- artefacto de sección/bloque de corrección A09+A10;
- master acumulativo Markdown candidato;
- master acumulativo DOCX candidato, editado directamente desde el Word canónico;
- response versionada con preflight, hashes, diff, controles OOXML y QA.

D-195 **no autoriza todavía la ejecución**. La ejecución requiere un prompt versionado, revisión interna PASS y una decisión posterior de autorización que apunte al prompt exacto.

## 8. Gate posterior

Después de la ejecución:

1. IA Gestora audita el candidato;
2. si PASS editorial/técnico, el candidato se envía a IA Experimental;
3. IA Experimental realiza la reauditoría focalizada requerida por G7-F03;
4. solo con PASS experimental se abre gate de aprobación del Autor;
5. tras aprobación e integración, se puede iniciar FINAL-F01.

```text
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = VERSION_AND_AUDIT_CORRECTION_PROMPT
AUTHOR_APPROVAL_GATE = NOT_OPEN
G7_F03_TERMINAL_CLOSED = false
FINAL_F01 = BLOCKED
```

---

## English

D-195 opens only the narrow A09+A10 scientific correction required by Experimental AI's G7-F03 audit. It authorizes no manuscript execution by itself.

The correction must document the already executed 20-case diagnostic LLM reranker protocol in Experimental Design and its frozen observed results in Results, while preserving its diagnostic-only status and separation from the primary fixed-Top-3 workflow.

All other manuscript content remains frozen. After Writing-AI execution and Managing-AI audit, the corrected candidate must return to Experimental AI for the focused re-audit required to close G7-F03.
