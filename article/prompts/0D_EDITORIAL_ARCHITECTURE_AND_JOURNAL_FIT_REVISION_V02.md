# Prompt correctivo 0D — Revisión V02 / 0D Corrective Prompt — V02 Revision

## Español

### Rol y alcance

Actúa exclusivamente como **IA de Redacción y análisis científico-editorial** del artículo principal del proyecto Tesis San Marcos.

Tu tarea es corregir **únicamente** la entrega 0D V01 conforme a `article/reviews/0D_INTERNAL_REVIEW.md`.

No rehagas 0D. No realices nueva búsqueda web. No cambies journal fit, ranking de revistas, arquitectura IMRaD, tablas/figuras, RQs, estados experimentales, gates ni conclusiones.

### Entrada obligatoria

Lee íntegramente:

1. `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`;
2. `article/reviews/0D_INTERNAL_REVIEW.md`.

Conserva V01 como referencia histórica; no la modifiques ni sobrescribas.

### Única corrección autorizada — 0D-M01

La V01 contiene terminología causal no autorizada en dos contextos conceptuales y sus equivalentes bilingües.

Debes aplicar exclusivamente estas normalizaciones:

1. En la fila de **Fig. 1** del mapa de tablas/figuras:
   - español: `separación causal/funcional` → `separación arquitectónica/funcional`;
   - inglés: `causal/functional separation` → `architectural/functional separation`.

2. En la mitigación del riesgo **B vs KBS expectations**:
   - español: `evidenciar separación causal y función de cada evaluación` → `hacer explícitas la separación arquitectónica/funcional y la función diferenciada de cada evaluación`;
   - inglés: sustituye cualquier formulación equivalente que atribuya `causal separation` por una formulación semánticamente equivalente a `make the architectural/functional separation and the differentiated role of each evaluation explicit`.

La razón es estrictamente terminológica y epistemológica: el proyecto documenta aislamiento arquitectónico/funcional e invariantes de flujo, no causalidad experimental entre módulos.

### Preservación obligatoria

Todo lo demás debe permanecer materialmente idéntico a V01, incluyendo:

```text
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

También debes preservar exactamente en sentido:

- arquitectura IMRaD y orden de subsecciones;
- mapa de figuras/tablas y sus estados;
- matriz de redactabilidad;
- todas las cifras experimentales;
- RQ1–RQ4 y sus dependencias;
- `C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE`;
- Grupo 3 como dependencia de RQ4/HE2/HE5;
- evaluación y ranking de los seis journals;
- fuentes web y artículos recientes ya verificados en V01;
- riesgos y mitigaciones salvo la normalización terminológica 0D-M01;
- cierre bilingüe.

No añadas nuevas fuentes, nuevas conclusiones, nuevos journals ni nuevos argumentos.

### Artefacto obligatorio

Crea exactamente:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`

Debe ser bilingüe y semánticamente equivalente ES/EN.

No modifiques ningún otro archivo.

### Cierre obligatorio

Finaliza con el mismo bloque de V01, preservando:

```text
0D_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Commit y respuesta al autor

Versiona únicamente V02 con un mensaje equivalente a:

`article: correct 0D terminology in response v02`

En el chat informa únicamente:

- commit SHA;
- ruta del archivo;
- estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

Detente después del commit.

---

## English

Act only as the Writing/scientific-editorial analysis AI. Revise the 0D V01 artifact only as required by `article/reviews/0D_INTERNAL_REVIEW.md`. Do not redo 0D, perform new web research, alter journal ranking, architecture, RQs, experimental state, or gate conclusions.

Apply only correction `0D-M01`: replace causal terminology with architectural/functional terminology in the Fig. 1 scientific-function wording and the KBS-risk mitigation, in both Spanish and English. The project establishes architectural/functional isolation and workflow invariants, not experimental causality between modules.

Preserve all other content materially unchanged, including the three journal recommendations, `PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS`, all figures/numbers, RQ states, Group-3 and C10/C11 dependencies, web sources, and the required closure block.

Create exactly:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`

Modify no other file. Commit only V02 and report only the commit SHA, path, and `COMPLETED_PENDING_EDITORIAL_REVIEW`.