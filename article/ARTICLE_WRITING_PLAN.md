# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.3
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
EXPERIMENTAL_RECONCILIATION_DECISION = D-019
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V003
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V003.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
CANONICAL_MASTER_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_AUTHORIZED_BLOCK = RELATED_WORK_B04_V02 / SECTION_2.4_CORRECTION_ONLY
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construye sobre una estructura acumulativa aprobada y cada bloque autorizado completa esa misma base.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, la Claim–Evidence Matrix, la literatura congelada de 0B y las fuentes experimentales gobernantes cuando correspondan.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- El lector debe comprender primero problema y posicionamiento, después la arquitectura general y solo entonces la instanciación experimental específica.
- NANDINA/Chapter-Class 87 y el corpus concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de recuperación documental y generación.
- La recuperación documental aporta evidencia para candidatos ya fijados y no sustituye ni reordena el ranking.
- El LLM local opera después de recuperación y se usa para explicación controlada; no clasifica desde cero ni retroalimenta la selección de candidatos.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de observación/análisis; DAM es unidad de agrupamiento cuando existe dependencia.
- Ningún resultado pendiente se redactará como hallazgo.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es el manuscript master inglés; Part II es el espejo español de control semántico.

### 3. Arquitectura acumulativa aprobada

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada permanece en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, aprobada mediante D-015. `Limitations` permanece integrada como `6.6 Limitations` salvo futura enmienda expresa.

### 4. Política acumulativa del Word

1. Cada bloque parte del último `ARTICLE_MASTER_V00N` aprobado.
2. El baseline actual es `ARTICLE_MASTER_V003.md/.docx`, SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.
3. No se crean Words independientes por sección.
4. La sección nueva se inserta en su ubicación estructural.
5. Solo se eliminan las notas editoriales correspondientes a la sección completada.
6. Part I y Part II conservan equivalencia semántica.
7. Candidatos no se vuelven canónicos hasta aprobación expresa del autor y auditoría de la IA Gestora.
8. Si el baseline exacto no está disponible, la IA de Redacción se detiene con `BASELINE_DOCX_ACCESS_REQUIRED`; no reconstruye silenciosamente el master.
9. Todo bloque preserva exactamente texto y comentarios de las secciones aprobadas.
10. El DOCX entregado para revisión debe ser el mismo binario comprometido cuando el prompt lo exija; divergencias de hash bloquean integración.

### 5. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| 0D original | CLOSED / APPROVED / FROZEN; arquitectura supersedida por D-014 |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work B01 / 2.1 | APPROVED / FROZEN / INTEGRATED |
| Related Work B02 / 2.2 | APPROVED / FROZEN / INTEGRATED |
| Related Work B03 / 2.3 | APPROVED / FROZEN / INTEGRATED |
| Related Work B04 V01 / 2.4 | REVIEWED / MINOR_CORRECTIONS_REQUIRED / NOT_APPROVED |
| Related Work B04 V02 / 2.4 | AUTHORIZED / ACTIVE |
| Related Work B05 / 2.5 | NOT AUTHORIZED |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

### 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| 2 | Related Work | EN PROGRESO; 2.1–2.3 integradas; 2.4 V02 activa |
| 3 | Introduction provisional | Related Work suficientemente estable + claims/RQs autorizados |
| 4 | Decision-support architecture | Introduction/positioning suficientemente estable |
| 5 | Experimental design | arquitectura suficientemente estable + ground truth experimental vigente |
| 6 | Results disponibles y autorizados | claims experimentales autorizados + gate editorial |
| 7 | Figuras/tablas preliminares | secciones relevantes suficientemente estables |
| 8 | Integración experimental pendiente | cierres/gates restantes del Plan Maestro si fueran necesarios |
| 9 | Results definitivos | evidencia requerida cerrada |
| 10 | Discussion + Limitations | Results definitivos + contraste autorizado |
| 11 | Conclusion | Discussion cerrada |
| 12 | Abstract | manuscrito completo |
| 13 | Title + Keywords | Abstract/manuscrito completos |
| 14 | Adaptación final KBS | requisitos vigentes verificados |

Orden activo:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración experimental pendiente cuando aplique → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

### 7. Estado experimental disponible para fases futuras

D-019 sincroniza el artículo con `SRC-03` después del cierre completo de Grupo 4:

```text
EXPERIMENTAL_PLAN_HEAD = 3ba3557eb10e741b8f49c420850940dee1df08ef
EXPERIMENTAL_MAIN_CHECKPOINT = 38e22c19a0eb0d344e7675761a88d7968091eead
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = NOT_STARTED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Esto elimina la antigua dependencia editorial de “esperar el cierre de Grupo 4” para futuros contrastes con literatura. No abre automáticamente Experimental design, Results o Discussion y no autoriza Grupo 5.

G4-F03 gobierna el futuro contraste con literatura mediante `docs/analysis/group4/g4_literature_contrast_v0.1.md`: 11 registros, 8 puntos autorizados y 14 prohibidos. Cuando se abra Discussion, este registro es vinculante para no sobreinterpretar resultados. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen sin cambios.

### 8. Fase activa — Related Work B04 V02

Related Work se organiza por familias funcionales:

- 2.1 `Automated tariff classification and candidate retrieval` — **APPROVED / FROZEN / INTEGRATED**;
- 2.2 `Knowledge-enhanced retrieval and regulatory reasoning` — **APPROVED / FROZEN / INTEGRATED**;
- 2.3 `LLMs for classification, reasoning, and explanation` — **APPROVED / FROZEN / INTEGRATED**;
- 2.4 `Evidence grounding, explainability, and auditability` — **V02 CORRECTION AUTHORIZED / ACTIVE**;
- 2.5 `Reproducibility and evaluation in knowledge-based decision support` — **NOT AUTHORIZED**;
- 2.6 `Positioning of this study` — **NOT AUTHORIZED**.

Prompt activo:

`article/prompts/2_RELATED_WORK_B04_V02_CORRECTIONS.md`

B04 V02 es una revisión correctiva cerrada: debe aplicar únicamente las tres correcciones científicas menores y cerrar la discrepancia de identidad binaria DOCX establecidas por la revisión interna. No autoriza ampliar 2.4, añadir literatura nueva ni iniciar 2.5.

### 9. Función de las secciones posteriores

- **Introduction:** `problema → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones → contexto de evaluación → RQs → roadmap`.
- **Decision-support architecture:** arquitectura general en relaciones entrada–operación–salida, antes de detalles experimentales.
- **Experimental design:** testbed específico, datos históricos, corpus documental, particiones/dependencia, configuración, evaluación, estadística y reproducibilidad.
- **Results:** organizados por función/RQ, no por códigos internos de experimento.
- **Discussion:** interpretación y comparación limitadas por G4-F03; implicaciones, condiciones de transferencia y limitaciones sin SOTA, novelty absoluta, causalidad no identificada ni generalización no evaluada.
- **Conclusion:** `aporte → evidencia principal → alcance → implicación`.

### 10. Ciclo obligatorio de cada bloque

1. verificar baseline/master acumulativo vigente;
2. leer onboarding y controles gobernantes;
3. verificar fuentes/dependencias;
4. re-recuperar full text primario para cada cita;
5. redactar exclusivamente el bloque autorizado;
6. incluir comentarios de auditoría anclados a cada cita inglesa;
7. auditar contenido científico, prosa, fluidez y ubicación narrativa;
8. activar IA Experimental solo si existe trigger real;
9. resolver observaciones;
10. solicitar aprobación expresa del autor;
11. integrar al master canónico solo después de aprobación y auditoría.

### 11. Criterios de aprobación

Una sección solo pasa a `APPROVED` cuando cumple su función narrativa, cada claim citado está respaldado por fuente primaria exacta, los comentarios Word contienen pasajes reales y pertinentes, no anticipa resultados ni testbed, respeta límites claim–evidencia, mantiene equivalencia EN/ES, preserva artefactos aprobados y recibe aprobación expresa del autor tras auditoría interna.

### 12. Front matter, end matter y journal targeting

Title, Abstract y Keywords se redactan al final. El end matter contemplará `Data availability`, `Code and reproducibility resources` si corresponde, CRediT, Funding, Declaration of competing interest, Acknowledgements si aplica, References y Supplementary material cuando sea necesario.

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

Antes del paquete final se verificarán nuevamente los requisitos oficiales vigentes de KBS.

---

## English

### Governing state

Writing Plan V2.3 preserves the author-approved KBS structure and cumulative-master policy. The canonical master remains `ARTICLE_MASTER_V003.md/.docx`, SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.

Sections 2.1–2.3 are approved, frozen, and integrated. B04 V01 was internally reviewed but not approved; B04 V02 is the only active drafting authorization and must execute `article/prompts/2_RELATED_WORK_B04_V02_CORRECTIONS.md`. Section 2.5 remains blocked.

D-019 reconciles the article with the canonical experimental state after full Group 4 closure: Group 3 is closed, `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, Group 4 is `CLOSED / APPROVED`, and G4-F01–F03 are all integrated. The future Discussion must use the G4-F03 controlled literature-contrast registry (11 comparisons, 8 authorized points, 14 forbidden points). This does not itself open Results/Discussion, establish SOTA or novelty, or authorize Group 5.
