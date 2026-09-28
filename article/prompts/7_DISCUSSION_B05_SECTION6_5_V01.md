# Prompt — Discussion B05 V01 / Section 6.5 — Configurability and transfer conditions

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Redacta únicamente Discussion §6.5 en inglés y español a partir del master canónico V027 y del DOCX acumulativo canónico B04 V02. No redactes §6.6 ni Conclusion y no modifiques ningún bloque previamente integrado.

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
17. `article/governance/D140_DISCUSSION_B04_AUTHOR_APPROVAL_V027_VERIFICATION_AND_INTEGRATION.md`.
18. `article/governance/D141_DISCUSSION_B05_SECTION6_5_CONFIGURABILITY_TRANSFER_BOUNDARY.md`.
19. La revisión interna vigente de este prompt.
20. La autorización vigente que apunte expresamente a este prompt.
21. Este prompt completo.
22. `article/manuscript/ARTICLE_MASTER_V027.md`.

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
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V027.md
EXPECTED_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
EXPECTED_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
```

Word acumulativo canónico, adjunto por el autor:

```text
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
EXPECTED_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 66
```

Verifica ambos antes de editar. Si no coinciden, detente. No reconstruyas el DOCX desde Markdown. Edita directamente el DOCX baseline exacto.

### Objetivo científico exclusivo

Redactar §6.5 `Configurability and transfer conditions` como Discussion interpretativa. La sección debe explicar qué puede reconfigurarse y bajo qué condiciones funcionales/procedimentales, conservando una separación estricta entre configurabilidad del diseño y generalización empírica.

Fuentes internas primarias autorizadas:

- Introduction: contribución de reinstanciación y límite de generalización.
- §2.5: reproducibilidad/replicación y límites conceptuales ya establecidos.
- §3.7: configurabilidad e interfaces requeridas.
- §4.1: alcance empírico Chapter 87 / NANDINA-8.
- §4.8: estado y alcance de recursos de reproducibilidad.
- §§6.1–6.4: separación funcional, autoridad de componentes, auditabilidad y límites.
- D-141: boundary científico obligatorio.

No se autoriza nueva literatura, búsqueda externa, citas nuevas, resultados nuevos ni inferencias nuevas.

### Ground truth y relaciones que deben preservarse

```text
CONFIGURABILITY = DESIGN_PROPERTY
TRANSFER = CONDITIONAL_REINSTANTIATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
INTERFACE_COMPATIBILITY != PERFORMANCE_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
REINSTANTIATION != DEPLOYMENT_READINESS
REINSTANTIATION != LEGAL_VALIDITY
CHAPTER87_RESULTS != ASSUMED_TRANSFER_TO_OTHER_SETTINGS
```

La re-instanciación puede sustituir, en principio, el banco histórico etiquetado, el espacio de códigos objetivo, la profundidad arancelaria, un corpus documental compatible y componentes de implementación, pero solo si se preservan las interfaces funcionales y la procedencia necesarias.

Las condiciones mínimas que la prosa debe hacer explícitas son:

1. Consulta comercial reproduciblemente representable/normalizable.
2. Registros históricos vinculados a códigos y procedencia.
3. Recuperador histórico con salida ordenada/trazable que permita formar candidatos únicos y fijar Top-3 antes de etapas downstream.
4. Evidencia documental vinculada a cada candidato fijo y a una fuente identificable/versionada.
5. Contexto que preserve código, rank fijo, soporte histórico, evidencia documental y procedencia.
6. Generador restringido a explicación y sin autoridad para cambiar Top-3 u orden.
7. Recursos que afectan la ejecución identificables/versionables cuando corresponda.
8. Corpus/documentos alternativos compatibles con el espacio de códigos y sujetos a validación de vigencia, autoridad y adecuación para la nueva instancia.

### Reproducción de referencia y replicación externa

La sección puede usar la convención ya definida en el manuscrito:

- **Reference reproduction:** reconstrucción de la instancia identificada usando los mismos insumos/configuración tan estrechamente como permitan los artefactos disponibles.
- **External replication:** aplicación del protocolo con datos independientes o recursos sustitutos compatibles, produciendo su propio manifiesto y resultados.

No presentes esta convención como taxonomía universal. No afirmes que una replicación externa debe reproducir los mismos números.

### Estado del paquete público de reproducibilidad

Si se menciona, debe hacerse brevemente y de forma reader-facing. El snapshot auditado materializa principalmente documentación de protocolos/contratos y una configuración de ejemplo, pero no garantiza actualmente una reproducción de referencia de un solo comando desde un clon limpio. Esta es una limitación del estado del paquete, no evidencia contra la posibilidad conceptual de reinstanciar la arquitectura.

No enumeres códigos internos, gates, hashes, decisiones D-xxx, nombres de auditoría ni artefactos de gobernanza en el texto publicable.

### Estructura argumental recomendada

Redacta aproximadamente 350–450 palabras en inglés, preferentemente en cinco párrafos, con espejo español semánticamente equivalente:

1. **Qué es configurable:** distinguir recursos/componentes reemplazables de las funciones que deben preservarse.
2. **Condiciones de interfaz:** explicar las condiciones concretas de query, histórico, Top-3, evidencia, contexto y generador.
3. **Transferencia documental/normativa:** señalar necesidad de compatibilidad, versión, procedencia, vigencia y validación de autoridad sin equiparar compatibilidad técnica con corrección jurídica.
4. **Reproducción vs replicación:** distinguir reconstruir la instancia evaluada de aplicar el protocolo con recursos independientes; mencionar con prudencia el estado actual del paquete público si mejora la discusión.
5. **Límite de interpretación:** cerrar explícitamente que configurabilidad no transfiere rendimiento, robustez, validez externa, legalidad, readiness ni aceptación humana.

No repitas §3.7 como lista mecánica. La función de §6.5 es interpretar qué significa la configurabilidad y qué precondiciones impone.

### Claims prohibidos

No afirmar ni implicar:

- generalización empírica demostrada fuera del benchmark Chapter 87;
- transferencia automática de Top-k, MRR, auditabilidad o cualquier otra métrica;
- universalidad o robustez cross-domain/cross-jurisdiction;
- que cambiar de jurisdicción, nomenclatura o profundidad es trivial;
- que corpus técnicamente compatible equivale a fuente vigente, suficiente o jurídicamente correcta;
- deployment readiness, human acceptance, expert replacement, safety o hallucination reduction;
- novelty, first-ever, SOTA, superioridad o FINAL_GAP;
- que el repositorio público actual ya garantiza reproducción completa de un comando desde un entorno limpio.

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
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
KBS_CONCRETE_PROSE = PASS
```

Evita expresiones vagas del tipo `the framework is flexible`, `portable`, `generalizable`, `widely applicable` o `easily transferable` sin condición concreta. Recurso → interfaz requerida → función preservada → límite inferencial.

### Bilingüismo

La versión española debe ser un espejo semántico natural, no traducción literal. Evita anglicismos innecesarios. Se pueden conservar términos técnicos estabilizados como Top-3, ranking, LLM y BM25 cuando corresponda. No introduzcas diferencias en fuerza epistémica, condiciones o límites.

### Diferencial autorizado

```text
SECTIONS_1_TO_6_4 = PRESERVE
SECTION_6_5 = DRAFT_V01_EN_AND_ES
SECTION_6_6 = PRESERVE_PLACEHOLDER
CONCLUSION = PRESERVE_PLACEHOLDER
REFERENCES = PRESERVE
END_MATTER = PRESERVE
```

No corrijas la deuda editorial registrada de §6.2 en esta ejecución.

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

1. `article/sections/discussion/Discussion_B05_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx`
4. `article/responses/7_DISCUSSION_B05_SECTION6_5_RESPONSE_V01.md`

### Checklist MWDP obligatorio

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
BLOCK = DISCUSSION_B05_SECTION_6_5
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
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
CITATION_COMMENT_COVERAGE = 48/48 / CUMULATIVE_INHERITED
COMMENTS = 48
TRACKED_CHANGES = 0
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.md / ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
ENGLISH_BLOCK_WORD_COUNT = ...
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Gate de salida

Detente después de §6.5.

```text
EXPECTED_EXIT = DISCUSSION_B05_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Discussion §6.5 from canonical V027 and the exact B04 V02 Word baseline. Discuss configurability as conditional re-instantiation under preserved interfaces, provenance, and component authority. Make explicit that configurability and interface compatibility do not establish empirical generalization or transfer Chapter-87 performance. Distinguish reference reproduction from external replication. Add no literature, citation occurrences, results, inference, or claims. Preserve 48 inherited comments and zero tracked changes; edit the Word directly rather than rebuilding it. Stop at `DISCUSSION_B05_V01_COMPLETED_PENDING_GESTORA_AUDIT`.