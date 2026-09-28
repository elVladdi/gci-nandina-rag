# Prompt — Discussion B06 V01 / Section 6.6 — Limitations

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Redacta únicamente Discussion §6.6 en inglés y español a partir del master canónico V028 y del DOCX acumulativo canónico B05 V01. No redactes Conclusion y no modifiques ningún bloque previamente integrado.

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
19. La revisión interna vigente de este prompt.
20. La autorización vigente que apunte expresamente a este prompt.
21. Este prompt completo.
22. `article/manuscript/ARTICLE_MASTER_V028.md`.

No uses una conversación anterior como fuente de verdad. Si el estado vivo contradice esta instrucción o falta un baseline exacto, detente y registra el bloqueo en la response versionada.

### Preflight obligatorio de `START_HERE.md`

Antes de redactar, la response debe registrar:

```text
ARCHIVOS LEÍDOS:
FASE ACTIVA:
ESTADO DEL BLOQUE ASIGNADO:
REDACCIÓN AUTORIZADA: SÍ / NO
DECISIONES CONGELADAS RELEVANTES:
CLAIMS AUTORIZADOS RELEVANTES:
CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:
FUENTES EXTERNAS QUE DEBEN VERIFICARSE:
BLOQUEOS O CONTRADICCIONES DETECTADOS:
```

### Baselines exactos

Markdown canónico:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V028.md
EXPECTED_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
EXPECTED_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
```

Word acumulativo canónico, adjunto por el autor:

```text
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
EXPECTED_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 67
```

Verifica ambos antes de editar. Si no coinciden, detente. No reconstruyas el DOCX desde Markdown. Edita directamente el DOCX baseline exacto.

### Objetivo científico exclusivo

Redactar §6.6 `Limitations` como cierre interpretativo de Discussion. La sección debe consolidar límites ya establecidos en Methods, Results y Discussion. No debe introducir resultados, análisis, explicaciones causales, literatura o inferencias nuevas.

Fuentes internas primarias autorizadas:

- §4.1: alcance empírico y muestra.
- §4.3: versión del corpus documental y drift normativo.
- §4.4: particiones, DAM, dependencia y near-duplicates.
- §4.7: unidad inferencial, EXP11A, EXP11B, EXP12, HE5 y límites estadísticos.
- §4.8: estado del paquete público de reproducibilidad.
- §§5.1–5.7: resultados y disposiciones ya reportadas.
- §§6.1–6.5: límites ya interpretados junto a ranking, evidencia, explicación, auditabilidad y configurabilidad.
- D-145: boundary científico obligatorio.

No se autoriza nueva literatura, búsqueda externa, citas nuevas, resultados nuevos ni inferencias nuevas.

### Limitaciones que deben cubrirse

La prosa debe integrar, sin convertir la sección en una lista mecánica, estos ocho dominios:

1. **Muestra y alcance:** colección purposiva; Chapter 87/NANDINA-8; benchmark offline; no muestra probabilística; no generalización automática a otras poblaciones/jurisdicciones/capítulos/profundidades.
2. **Dependencia y similitud residual:** DAM-disjoint e `id_unico`-disjoint no equivalen a observaciones i.i.d.; persisten exact matches y near-duplicates entre declaraciones distintas; no atribuirles causalmente una fracción del rendimiento.
3. **Banco histórico:** EXP11A cambia tamaño y composición conjuntamente; no hay efecto causal aislado de tamaño. EXP11B H150/H200 es descriptivo, diez semillas emparejadas sobre el mismo EVAL, sin inferencia a superpoblación ni regla monotónica general.
4. **Objetos no estimables:** EXP12 diversity effect `NOT_ESTIMABLE`; prevalencia de descripciones ambiguas/incompletas `NOT_ESTIMABLE`; HE5 `INCONCLUSIVE`.
5. **Corpus documental y drift:** corpus primario derivado de Decision 885 frente a Decision 906 vigente antes de los casos 2026; sensibilidad correctiva method-dependent; asociación exacta y trazabilidad no equivalen a vigencia/suficiencia/corrección normativa o jurídica.
6. **Explicación/auditabilidad:** 50 casos cualitativos; LLM-as-judge, no humanos; criterio de auditabilidad propio del protocolo; mismatch instrucción–esquema produjo 0/50 schema compliance por incompatibilidad de especificación; trazabilidad no garantiza verificabilidad, claridad, causal faithfulness ni utilidad experta.
7. **Generalización y uso:** configurabilidad e interfaces no transfieren rendimiento, robustez, auditabilidad, validez externa, deployment readiness, legal validity ni human acceptance. El sistema no fue validado como adjudicador legal autónomo ni como despliegue operativo.
8. **Reproducibilidad pública:** el snapshot auditado no constituye todavía una reproducción de referencia completa one-command desde clean clone; faltan componentes materiales identificados en §4.8. Este límite del paquete no debe confundirse con imposibilidad conceptual de reproducir/reinstanciar el procedimiento.

### Relaciones que deben preservarse

```text
DAM_DISJOINT_PARTITIONS != IID_OBSERVATIONS
RESIDUAL_SIMILARITY_DIAGNOSTICS != CAUSAL_EFFECT_ESTIMATE
EXP11A_SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
HE5 = INCONCLUSIVE
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
LLM_AS_JUDGE != HUMAN_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
```

### Control de resultados y cifras

Discussion interpreta; no reabre Results. Puedes usar cifras ya integradas solo cuando sean necesarias para explicar una limitación concreta y sin crear nuevos cálculos. No recalcules porcentajes, intervalos, diferencias, agregados ni tasas.

Si mencionas resultados de explicación, preserva exactamente:

- muestra cualitativa `50` casos;
- `28/50 = 56.0%` bajo el criterio congelado, si se necesita;
- LLM-as-judge, no validación humana;
- 0/50 schema compliance únicamente por incompatibilidad de especificación, no como 50 explicaciones sustantivamente inválidas.

Si mencionas similitud residual o sensibilidad, usa únicamente valores ya publicados en §5 y no conviertas asociaciones descriptivas en mecanismos causales.

### Estructura argumental recomendada

Redacta aproximadamente **600–800 palabras en inglés**, preferentemente en **7 párrafos**, con espejo español semánticamente equivalente:

1. alcance de muestra/testbed y límite de validez externa;
2. dependencia de datos, DAM y similitud residual;
3. composición/tamaño del banco histórico y objetos robustness no estimables;
4. drift del corpus documental y límite entre asociación y corrección normativa/jurídica;
5. evaluación de explicación: muestra, LLM-as-judge, schema mismatch y límite de auditabilidad;
6. configurabilidad/reinstanciación y ausencia de transferencia de desempeño/deployment/legal validity;
7. reproducibilidad pública actual y cierre sintético: qué resultados siguen siendo válidos dentro del scope y qué necesita evaluación adicional fuera de él.

No conviertas §6.6 en inventario de IDs internos. Traduce los objetos experimentales a lenguaje científico público cuando sea posible. Los nombres EXP11A, EXP11B, EXP12 o HE5 pueden aparecer en la response/governance, pero **no deben filtrarse al texto publicable** salvo que sean indispensables; en el manuscrito prefiere expresiones reader-facing como `historical-bank size/composition sensitivity`, `enlarged-bank descriptive comparison`, `planned historical-diversity analysis`, etc.

### Claims prohibidos

No afirmar ni implicar:

- representatividad poblacional del benchmark;
- independencia completa por tener particiones disjuntas por DAM;
- efecto causal de near-duplicates sobre performance;
- efecto causal o monotónico general del tamaño del banco;
- que Decision 885 invalida automáticamente todos los resultados o documentos;
- legal correctness derivada de evidencia documental;
- equivalencia entre LLM-as-judge y humanos;
- que 56% es una tasa operacional generalizable;
- safety improvement, hallucination reduction o causal risk reduction;
- external generalization, cross-jurisdiction portability de métricas o universal robustness;
- deployment readiness, expert replacement, human acceptance o legal adjudication;
- que el paquete público actual ya garantiza one-command reproduction;
- novelty, first-ever, SOTA, superioridad o FINAL_GAP.

### Control D-136 / KBS / SPCCR

Audita cada párrafo como contenido publicable, no como reporte interno. Requisitos:

```text
SCIENTIFIC_FIDELITY = PASS
EPISTEMIC_STRENGTH = BOUNDED
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
LIMITATION_CLAIM_PROXIMITY = PASS
KBS_CONCRETE_PROSE = PASS
```

Evita lenguaje de gobernanza, códigos de auditoría, nombres de campos, usernames, hashes, commits, gates, labels internos y diagnóstico de QA. Explica la sustancia científica en términos reader-facing.

### Deuda editorial heredada §6.2

No corrijas `independent_ai_reviewer_01`, `AI_EXPERT_ROLE`, `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, `advertencias_globales` ni otra deuda editorial ya registrada dentro de §6.2. Ese bloque está congelado y su limpieza requiere un gate transversal posterior. En §6.6 debes describir las mismas limitaciones con lenguaje científico público, sin repetir esas etiquetas internas.

### Bilingüismo

La versión española debe ser un espejo semántico natural. Evita anglicismos innecesarios. Conserva solo términos técnicos estabilizados cuando sean necesarios. No introduzcas diferencias de fuerza epistémica, condiciones, denominadores o límites.

### Diferencial autorizado

```text
SECTIONS_1_TO_6_5 = PRESERVE
SECTION_6_6 = DRAFT_V01_EN_AND_ES
CONCLUSION = PRESERVE_PLACEHOLDER
REFERENCES = PRESERVE
END_MATTER = PRESERVE
```

No corrijas ningún bloque previo en esta ejecución.

### Citas, comentarios y Word

No agregues, elimines ni muevas citas o comentarios.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Preserva los 48 comentarios heredados y sus anclajes. Realiza auditoría diferencial OOXML y render completo. No reconstruyas Word desde Markdown.

D-035: no usar Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. D-027: entregar el DOCX exacto al autor como artefacto adjunto. D-022: versionar primero la response en GitHub; el chat debe ser un puntero breve acompañado por los archivos exactos exigidos.

### Entregables

1. `article/sections/discussion/Discussion_B06_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.docx`
4. `article/responses/7_DISCUSSION_B06_SECTION6_6_RESPONSE_V01.md`

### Checklist MWDP obligatorio

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
BLOCK = DISCUSSION_B06_SECTION_6_6
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = ...
BASELINE_MD_IDENTITY = PASS / BLOCKED
BASELINE_DOCX_IDENTITY = PASS / BLOCKED
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
NEW_RESULTS_OR_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_ENGLISH_CITATION_OCCURRENCES = 0
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
LIMITATION_CLAIM_PROXIMITY = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
CITATION_COMMENT_COVERAGE = 48/48 / CUMULATIVE_INHERITED
COMMENTS = 48
TRACKED_CHANGES = 0
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.md / ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V01.docx
ENGLISH_BLOCK_WORD_COUNT = ...
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Gate de salida

Detente después de §6.6.

```text
EXPECTED_EXIT = DISCUSSION_B06_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Discussion §6.6 from canonical V028 and the exact B05 V01 Word baseline. Consolidate known limitations without introducing literature, results, calculations, inference, mechanisms, or claims. Cover sample/scope, DAM dependence and residual similarity, historical-bank sensitivity, non-estimable robustness objects, documentary drift, 50-case LLM-as-judge explanation evaluation, configurability-versus-generalization, legal/deployment boundaries, and the incomplete current public reproducibility snapshot. Keep the publication prose free of internal experiment, governance, repository, and QA labels. Preserve 48 inherited comments and zero tracked changes; edit Word directly and stop at `DISCUSSION_B06_V01_COMPLETED_PENDING_GESTORA_AUDIT`.