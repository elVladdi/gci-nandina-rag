# Cierre formal de Fase 0 / Formal Phase 0 Closure

## Español

### Dictamen

```text
PHASE_0 = CLOSED / APPROVED
0A = CLOSED / APPROVED
0B = CLOSED / APPROVED
0C = CLOSED / APPROVED / FROZEN
0D = CLOSED / APPROVED / FROZEN
0D_AUTHOR_APPROVAL = RECEIVED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = ELIGIBLE_FOR_OPENING
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

### Fundamento del cierre

Fase 0 se cierra después de:

1. congelar el ground truth documental y experimental en 0A;
2. cerrar y congelar el mapa bibliográfico/taxonómico de 0B;
3. congelar en 0C la contribución arquitectónica-metodológica provisional, las RQs y sus condiciones;
4. completar 0D-1 con arquitectura editorial y journal fit;
5. completar 0D-2 con requisitos editoriales verificables, gobernanza de escritura, workflow Markdown/Word, auditoría de citas y cascada de revistas;
6. verificar acceso full-text actual a las 62 fuentes del corpus consolidado;
7. recibir aprobación expresa del autor para 0D;
8. congelar `MWDP_V1.0` como protocolo maestro acumulativo obligatorio.

### Transferencia a Fase 1

La siguiente fase es `1 — Methods`. El cierre de Fase 0 no autoriza redacción libre ni automática. La IA Gestora debe abrir explícitamente el primer bloque de Methods, verificar nuevamente el estado live de las fuentes experimentales y claims aplicables, y emitir un prompt cerrado que obligue a leer y cumplir `MWDP_V1.0`.

Persisten:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

Estas dependencias no bloquean la apertura de los subbloques de Methods que no requieran resultados pendientes, pero sí limitan cualquier afirmación que dependa de ellas.

---

## English

### Decision

```text
PHASE_0 = CLOSED / APPROVED
0A = CLOSED / APPROVED
0B = CLOSED / APPROVED
0C = CLOSED / APPROVED / FROZEN
0D = CLOSED / APPROVED / FROZEN
0D_AUTHOR_APPROVAL = RECEIVED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = ELIGIBLE_FOR_OPENING
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

### Closure basis

Phase 0 closes after frozen documentary/experimental ground truth; closed/frozen literature mapping; frozen provisional architectural-methodological contribution and RQs; completed 0D-1 editorial architecture/journal fit; completed 0D-2 editorial requirements and writing governance; current full-text access to all 62 consolidated sources; express 0D author approval; and freezing of cumulative `MWDP_V1.0`.

### Transfer to Phase 1

The next phase is `1 — Methods`. Phase-0 closure does not authorize free or automatic drafting. The Managing AI must explicitly open the first Methods block, recheck live experimental sources/claims, and issue a constrained prompt requiring full compliance with `MWDP_V1.0`.

`FINAL_GAP` and final novelty remain undefined. C10/C11 reconciliation remains required before EXP-11B article use, and Group 3 remains required for final RQ4 and applicable HE2/HE5 inference. These dependencies do not block Methods blocks that do not rely on pending results, but they constrain any claim that does.
