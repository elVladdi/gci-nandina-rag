# 0D-2 — Gate de entrada / Entry Gate

## Español

### Estado de entrada

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

### Propósito

0D-2 se abre para cerrar, antes de redactar el manuscrito, todas las decisiones editoriales y operativas que podrían provocar reescrituras sustantivas si se difirieran a fases posteriores.

0D-2 complementa 0D-1. No invalida la arquitectura ni el journal-fit ya auditados; los somete a una última capa de cumplimiento específico del journal, gobernanza de escritura, protocolo de entregables y estrategia de contingencia de revistas antes de solicitar aprobación final del autor y freeze de 0D.

### Alcance obligatorio

0D-2 debe resolver, con evidencia oficial vigente cuando corresponda:

1. **Revista y tipo de artículo**: confirmar si `Knowledge-Based Systems` permanece como target A y determinar el tipo de artículo exacto aplicable.
2. **Requisitos formales del target A**: estructura/secciones permitidas o requeridas, plantilla o ausencia de plantilla obligatoria, formato de primera submission, extensión, abstract, keywords, highlights, graphical abstract, tablas, figuras, material suplementario, anonimización, declaraciones y checklist.
3. **Referencias**: identificar el estilo bibliográfico final exigido por la revista; durante la redacción, el Word utilizará provisionalmente APA 7 para facilitar la gestión final del autor mediante Mendeley.
4. **Arquitectura definitiva del artículo**: reconciliar la arquitectura candidata 0D-1 con los requisitos reales del target A y fijar secciones/subsecciones antes de Fase 1.
5. **Política de escritura científica**: idioma maestro, variante de inglés si procede, voz, tiempos verbales, tono, precisión terminológica, concisión, estructura de párrafos y reglas contra lenguaje promocional o ambiguo.
6. **Protocolo anti-error / anti-overclaiming / anti-alucinación**: toda cifra, claim, referencia, DOI, configuración, resultado, interpretación o conclusión debe provenir de evidencia autorizada y trazable; se mantienen todas las fronteras epistemológicas congeladas.
7. **Contrato claim–evidence**: reglas operativas para `AUTHORIZED`, `CONDITIONAL`, `REVIEW_REQUIRED` y `PROHIBITED`; ninguna afirmación podrá ampliarse más allá de lo que su fuente demuestra.
8. **Sistema de redacción, versionado y entregables**: cada entrega de IA de Redacción deberá producir el bloque `.md`, un `.md` maestro acumulativo candidato y un `.docx` maestro acumulativo candidato; solo una versión auditada y aprobada se convierte en base canónica de la siguiente entrega.
9. **Protocolo Word y citas**: el Word maestro se actualizará sobre la última versión aprobada y no se reconstruirá desde cero salvo creación inicial basada en la plantilla/formato oficial; las citas y referencias provisionales en Word se expresarán en APA 7 hasta la gestión final por Mendeley del autor.
10. **Comentarios de auditoría por cita en Word**: toda cita debe tener un comentario anclado exactamente a la cita correspondiente que incluya fuente/revista, autor(es), afirmación o extracto original exacto y suficiente, traducción al español y explicación de por qué esa fuente respalda la afirmación del manuscrito. Una misma referencia usada para claims distintos requiere comentarios independientes.
11. **Autoridad operativa**: la IA de Redacción genera y actualiza los artefactos de manuscrito (`.md` y `.docx`); la IA Gestora, la IA Experimental y el autor auditan según sus respectivas competencias. El autor gestionará Mendeley al final.
12. **Estrategia editorial y cascada de revistas**: Target A `Knowledge-Based Systems`; Plan B `Expert Systems with Applications`; Plan C `Information Processing & Management`, salvo que la verificación de 0D-2 obligue a revisar ese orden. Debe definirse un núcleo científico común que minimice reescritura y una matriz de cambios necesarios al migrar de A→B→C.
13. **Estrategia para maximizar aceptación**: framing, riesgos de desk rejection, contribución defendible, tratamiento de limitaciones, reproducibilidad, transparencia, fit editorial y elementos que deben evitarse.
14. **Gate de preparación para escribir**: 0D-2 debe identificar cualquier punto no verificable o no resuelto que todavía impida abrir Methods.

### Reglas de búsqueda externa

La búsqueda web de 0D-2 está autorizada exclusivamente para verificar requisitos editoriales vigentes, plantilla/formato oficial, políticas y estrategia de fit de las revistas de la cascada.

Prioridad de fuentes:

1. página oficial del journal;
2. `Guide for Authors` / submission guidelines oficiales;
3. políticas oficiales del publisher;
4. páginas oficiales de plantillas o recursos de submission;
5. artículos recientes de la revista solo cuando ayuden a observar convenciones editoriales, nunca para reabrir 0B ni probar novelty.

Si un requisito no puede verificarse en una fuente oficial, debe declararse `UNVERIFIED` y no inferirse.

### Prohibiciones

0D-2 no puede:

- redactar ninguna sección del manuscrito;
- modificar resultados experimentales o Plan Maestro;
- reabrir la búsqueda de gap/novelty de 0B;
- declarar `FINAL_GAP` o `NOVELTY` por journal fit;
- usar EXP-11B mientras C10/C11 no estén reconciliados;
- cerrar RQ4/HE2/HE5 antes de Grupo 3;
- inventar requisitos de revista no verificados;
- congelar 0D ni cerrar Fase 0 sin auditoría de la IA Gestora y aprobación expresa del autor.

### Artefacto esperado

```text
article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md
```

### Gate

```text
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

---

## English

### Entry state

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

### Purpose

0D-2 closes, before manuscript drafting, the editorial and operational decisions that could otherwise cause substantive rewriting later. It complements 0D-1 by adding journal-specific compliance, writing governance, deliverable protocol, and a journal-contingency strategy before final author approval and 0D freeze.

### Mandatory scope

0D-2 must resolve: target journal and exact article type; current target-A formatting and submission requirements; final reference style; definitive article architecture; scientific writing policy; anti-error/anti-overclaiming/anti-hallucination rules; operational claim–evidence rules; cumulative Markdown/Word versioning; provisional APA-7 references in Word until final author-side Mendeley management; mandatory citation-anchored Word comments containing source/journal, authors, exact sufficient original-language supporting statement, Spanish translation, and support justification; Drafting-AI ownership of manuscript artifact generation/update; A→B→C journal cascade and transfer matrix; acceptance-maximization strategy; and a final readiness gate for Methods.

Official journal/publisher sources are mandatory for current requirements. Any unverifiable requirement must be labeled `UNVERIFIED`, never inferred.

0D-2 must not draft manuscript sections, alter experimental evidence, reopen the 0B gap/novelty search, use unreconciled EXP-11B, close Group-3-dependent inference, or freeze Phase 0 without editorial audit and explicit author approval.

### Expected artifact

```text
article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md
```

### Gate

```text
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```
