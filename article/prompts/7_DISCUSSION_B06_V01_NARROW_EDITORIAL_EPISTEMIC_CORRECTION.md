# Prompt — Discussion B06 V01 narrow editorial/epistemic correction to V02

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Corrige únicamente Discussion §6.6 en inglés y español a partir de los candidatos acumulativos B06 V01 exactos. No redactes Conclusion y no modifiques ningún bloque previamente integrado.

### Onboarding obligatorio

Antes de modificar artefactos, lee íntegramente y aplica, en este orden:

1. `article/START_HERE.md`.
2. `article/README.md`.
3. `article/ARTICLE_STATUS.md`.
4. `article/ARTICLE_WRITING_PLAN.md`.
5. `article/DECISIONS.md`.
6. `article/SOURCE_REGISTRY.md`.
7. `article/CLAIM_EVIDENCE_MATRIX.md`.
8. `article/STYLE_GUIDE.md`.
9. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — MWDP v1.0.
10. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` — SPCCR v1.0.
11. `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`.
12. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md` — contenido sustantivo aprobado por D-013.
13. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`.
14. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`.
15. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`.
16. `article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md`.
17. `article/governance/D144_DISCUSSION_B05_AUTHOR_APPROVAL_V028_VERIFICATION_AND_INTEGRATION.md`.
18. `article/governance/D145_DISCUSSION_B06_SECTION6_6_LIMITATIONS_BOUNDARY.md`.
19. `article/governance/D146_DISCUSSION_B06_SECTION6_6_EXECUTION_AUTHORIZATION.md`.
20. `article/responses/7_DISCUSSION_B06_SECTION6_6_RESPONSE_V01.md`.
21. `article/reviews/7_DISCUSSION_B06_SECTION6_6_INTERNAL_REVIEW_V01.md`.
22. `article/governance/D147_DISCUSSION_B06_V01_AUDIT_PASS_WITH_CORRECTIONS_AND_V02_GATE.md`.
23. La revisión interna vigente de este prompt.
24. La autorización vigente que apunte expresamente a este prompt.
25. Este prompt completo.
26. `article/manuscript/ARTICLE_MASTER_V028.md` solo como referencia canónica de §§1–6.5; no lo uses para reconstruir los candidatos B06.

No uses una conversación anterior como fuente de verdad. Si el estado vivo contradice esta instrucción o falta un baseline exacto, detente y registra el bloqueo en la response versionada.

### Preflight obligatorio

La response debe registrar:

```text
ARCHIVOS LEÍDOS:
FASE ACTIVA:
ESTADO DEL BLOQUE ASIGNADO:
CORRECCIÓN AUTORIZADA: SÍ / NO
DECISIONES CONGELADAS RELEVANTES:
CLAIMS AUTORIZADOS RELEVANTES:
CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:
FUENTES EXTERNAS QUE DEBEN VERIFICARSE:
BLOQUEOS O CONTRADICCIONES DETECTADOS:
```

### Baselines exactos de esta corrección

Markdown acumulativo B06 V01 entregado por el autor:

```text
INPUT_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.md
EXPECTED_SHA256 = c73518750ac9faff5e69eca3f5e363ef386efd0ac78969315b9dedf4ce7ec2e1
EXPECTED_GIT_BLOB = 20028e1c0e9fc8fe9c98b1b1bf3f00b3cf95fef7
```

Word acumulativo B06 V01 entregado por el autor:

```text
INPUT_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.docx
EXPECTED_SHA256 = 3859c8686679777d64910839842b4a771befb84dca715e1054a524fa52c75d27
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 69
```

Verifica ambas identidades antes de editar. Si no coinciden, detente. **No reconstruyas el DOCX desde Markdown.** Edita directamente el DOCX B06 V01 exacto.

### Scope de corrección

```text
SECTIONS_1_TO_6_5 = PRESERVE_BYTE/TEXT_EQUIVALENT
SECTION_6_6 = NARROW_CORRECTION_V02_EN_AND_ES
CONCLUSION = PRESERVE_PLACEHOLDER
REFERENCES = PRESERVE
END_MATTER = PRESERVE
```

No corrijas la deuda editorial heredada de §6.2. No redactes Conclusion.

### Corrección obligatoria 1 — precisión epistemológica de la sensibilidad documental

La formulación V01:

> `Corrective sensitivity showed that the effect of the updated resource depended on the retrieval method rather than yielding a single uniform pattern.`

es demasiado causal porque D-145 solo autoriza una lectura descriptiva/method-dependent de la sensibilidad correctiva.

Reemplázala por una formulación reader-facing no causal, por ejemplo:

> `The observed changes under the corrective sensitivity were method-dependent rather than uniform across retrieval methods.`

El espejo español debe evitar `efecto` causal, por ejemplo:

> `Los cambios observados en la sensibilidad correctiva fueron dependientes del método y no mostraron un patrón uniforme entre los métodos de recuperación.`

Mantén intacta la conclusión científica: `METHOD_DEPENDENT`; no agregues magnitudes, cálculos ni nuevos resultados.

### Corrección obligatoria 2 — retirar voz interna de “frozen” en no estimabilidad

La formulación V01:

> `because no frozen case-level operationalization existed`

no debe usar `frozen` como término de gobernanza en el manuscrito. Sustituye por lenguaje científico público que exprese preespecificación, por ejemplo:

> `because no case-level operationalization had been prespecified`

En español, sustituye `operacionalización congelada caso por caso` por `operacionalización preespecificada a nivel de caso` o equivalente natural.

No cambies el estado científico: la prevalencia de descripciones ambiguas/incompletas sigue siendo `NOT_ESTIMABLE` y la disposición asociada sigue inconclusa.

### Corrección obligatoria 3 — terminología reader-facing de reproducibilidad

Retira estas expresiones internas/ingenieriles de V01:

- `complete canonical runner` / `ejecutor canónico completo`;
- `a frozen Chapter-87 reference configuration` / `una configuración de referencia congelada del Capítulo 87`.

Preserva exactamente la limitación de §4.8 y D-145, pero exprésala con términos públicos, por ejemplo:

- `a complete executable reference-reproduction workflow or runner`;
- `a versioned Chapter-87 reference configuration/preset`.

En español usa equivalentes naturales como `flujo ejecutable completo de reproducción de referencia` y `configuración/preset de referencia versionado del Capítulo 87`.

No inventes nuevos componentes faltantes y no elimines ninguno de los faltantes ya enumerados: validadores/experiment interfaces completos, dependency lock, canonical/reference outputs, redistributable administrative reference data y documented clean-environment validation deben conservarse semánticamente.

### Corrección obligatoria 4 — naturalidad de deployment

Naturaliza la frase:

> `The evaluated system was not validated as an autonomous legal adjudicator, as a replacement for experts, or as an operational deployment.`

sin alterar su fuerza epistémica. Forma recomendada:

> `The evaluated system was not validated as an autonomous legal adjudicator or a replacement for experts, and it was not validated for operational deployment.`

Espejo español recomendado:

> `El sistema evaluado no fue validado como adjudicador jurídico autónomo ni como sustituto de expertos, y tampoco fue validado para despliegue operativo.`

### Preservaciones científicas obligatorias

No alteres ni suavices en sentido positivo estas relaciones:

```text
DAM_DISJOINT_PARTITIONS != IID_OBSERVATIONS
RESIDUAL_SIMILARITY_DIAGNOSTICS != CAUSAL_EFFECT_ESTIMATE
SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT
ENLARGED_BANK_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE
HISTORICAL_DIVERSITY_EFFECT = NOT_ESTIMABLE
DESCRIPTION_QUALITY_PREVALENCE = NOT_ESTIMABLE
ROBUSTNESS_DISPOSITION = INCONCLUSIVE
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
LLM_AS_JUDGE != HUMAN_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
```

Mantén exactamente las cifras ya usadas en §6.6 si permanecen en el texto:

- `50` casos;
- `28/50 = 56.0%` / `56,0%`;
- `0/50` schema compliance solo por incompatibilidad de especificación.

No introduzcas nueva literatura, búsqueda externa, citas, resultados, cálculos, intervalos, p-values, inferencias, mecanismos causales, novelty, SOTA, superioridad, legal correctness, human validation, deployment readiness ni generalización externa.

### Control D-136 / KBS / SPCCR

La V02 debe cumplir:

```text
SCIENTIFIC_FIDELITY = PASS
EPISTEMIC_STRENGTH = BOUNDED
CAUSAL_DOCUMENTARY_SENSITIVITY_WORDING = ABSENT
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
READER_FACING_REPRODUCIBILITY_TERMINOLOGY = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
LIMITATION_CLAIM_PROXIMITY = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_CONCRETE_PROSE = PASS
```

### Citas, comentarios y Word

No agregues, elimines ni muevas citas o comentarios.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Preserva los 48 comentarios heredados y sus anclajes. Realiza auditoría diferencial OOXML y render completo. No reconstruyas Word desde Markdown.

D-035: no usar Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. D-027: entregar el DOCX exacto al autor como artefacto adjunto. D-022: versionar primero la response en GitHub.

### Entregables

1. `article/sections/discussion/Discussion_B06_V02.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.docx`
4. `article/responses/7_DISCUSSION_B06_SECTION6_6_RESPONSE_V02.md`

### Checklist MWDP obligatorio

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
BLOCK = DISCUSSION_B06_SECTION_6_6
BLOCK_REVISION = V02
INPUT_CANDIDATE_MD_IDENTITY = PASS / BLOCKED
INPUT_CANDIDATE_DOCX_IDENTITY = PASS / BLOCKED
SECTIONS_1_TO_6_5_MODIFIED = NO
SECTION_6_6_MODIFIED = YES / NARROW_CORRECTION_ONLY
CONCLUSION_MODIFIED = NO
NEW_RESULTS_OR_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_ENGLISH_CITATION_OCCURRENCES = 0
CAUSAL_DOCUMENTARY_SENSITIVITY_WORDING = ABSENT
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
READER_FACING_REPRODUCIBILITY_TERMINOLOGY = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
COMMENTS = 48
TRACKED_CHANGES = 0
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Gate de salida

Detente después de producir B06 V02.

```text
EXPECTED_EXIT = DISCUSSION_B06_V02_COMPLETED_PENDING_GESTORA_REAUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Correct only Section 6.6 EN/ES from the exact B06 V01 cumulative Markdown and Word candidates. Remove causal `effect` wording from documentary-resource sensitivity, replace internal `frozen`/`canonical runner` terminology with reader-facing scientific language, and naturalize the operational-deployment sentence. Preserve every scientific limit, figure, citation/comment, prior section, and Conclusion placeholder. Stop at `DISCUSSION_B06_V02_COMPLETED_PENDING_GESTORA_REAUDIT`.
