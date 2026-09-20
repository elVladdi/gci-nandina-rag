# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.1
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
WORD_BASELINE = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
WORD_BASELINE_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_AUTHORIZED_BLOCK = RELATED_WORK_B01 / SECTION_2.1_ONLY
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construirá sobre una **estructura acumulativa completa ya aprobada por el autor** y cada nueva versión completará esa misma base.

La redacción se rige por `KBS_EWG_34_V01`, el protocolo `MWDP_V1.0`, la Claim–Evidence Matrix, la literatura congelada de 0B y las fuentes experimentales gobernantes cuando correspondan.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- El lector debe comprender primero el problema y posicionamiento, después la arquitectura general y solo entonces la instanciación experimental específica.
- NANDINA/Chapter-Class 87 y el corpus documental concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de recuperación documental y generación.
- La recuperación documental aporta evidencia para candidatos ya fijados y no sustituye ni reordena el ranking.
- El LLM local opera después de recuperación y se usa para explicación controlada; no clasifica desde cero ni retroalimenta selección de candidatos.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de observación/análisis; DAM es unidad de agrupamiento cuando existe dependencia.
- Ningún resultado pendiente se redactará como hallazgo.
- Toda afirmación científica deberá quedar trazada a evidencia autorizada.
- Part I es el manuscript master inglés; Part II es el espejo español de control semántico.

### 3. Arquitectura acumulativa aprobada

La estructura congelada para redacción es:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada está en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md` y fue aprobada mediante D-015.

El Word exacto que sirve como baseline de bootstrap es `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`, SHA-256 `0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5`.

`Limitations` permanece integrada como `6.6 Limitations`, salvo futura enmienda aprobada por el autor.

### 4. Política acumulativa del Word

1. El primer bloque parte del Word estructural exacto aprobado.
2. Después de la primera integración canónica, cada bloque parte del último `ARTICLE_MASTER_V00N` aprobado.
3. No se crean Words independientes por sección.
4. La sección nueva se inserta directamente en su ubicación estructural.
5. Solo se eliminan las notas editoriales correspondientes a la sección que se completa.
6. Part I y Part II deben conservar equivalencia semántica.
7. Las versiones de trabajo permanecen como candidatas hasta aprobación expresa del autor.
8. Ningún texto previamente rechazado se reutiliza automáticamente.
9. Si el baseline exacto no es accesible, la IA de Redacción debe detenerse con `BASELINE_DOCX_ACCESS_REQUIRED`; no se autoriza reconstrucción silenciosa.

### 5. Estado previo y reset

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| 0D original | CLOSED / APPROVED / FROZEN; arquitectura de secciones supersedida por D-014 |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

D-014 y D-015 modifican únicamente arquitectura editorial, orden de redacción y activación del nuevo flujo. No cambian alcance científico, RQs, claims autorizados, diseño experimental ni gobernanza del Plan Maestro.

### 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa del artículo | **CLOSED / AUTHOR_APPROVED / FROZEN_FOR_DRAFTING** |
| 2 | Related Work | estructura aprobada + literatura 0B congelada |
| 3 | Introduction provisional | Related Work suficientemente estable + claims/RQs autorizados |
| 4 | Decision-support architecture | Introduction/positioning suficientemente estable |
| 5 | Experimental design | arquitectura suficientemente estable + ground truth experimental vigente |
| 6 | Results disponibles y autorizados | claims experimentales autorizados |
| 7 | Figuras y tablas preliminares | secciones 2–6 suficientemente estables |
| 8 | Integración de resultados experimentales pendientes | cierres/gates del Plan Maestro |
| 9 | Results definitivos | Fase 8 cerrada |
| 10 | Discussion + Limitations | Results definitivos |
| 11 | Conclusion | Discussion cerrada |
| 12 | Abstract | manuscrito completo y resultados finales |
| 13 | Title + Keywords | Abstract y manuscrito completo |
| 14 | Adaptación final KBS | requisitos vigentes de submission verificados |

Orden operativo activado:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración experimental pendiente → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

### 7. Fase activa — Related Work

Related Work se organiza por familias funcionales:

- 2.1 `Automated tariff classification and candidate retrieval`;
- 2.2 `Knowledge-enhanced retrieval and regulatory reasoning`;
- 2.3 `LLMs for classification, reasoning, and explanation`;
- 2.4 `Evidence grounding, explainability, and auditability`;
- 2.5 `Reproducibility and evaluation in knowledge-based decision support`;
- 2.6 `Positioning of this study`.

Cada subsección debe sintetizar por problema/tarea/enfoque, no por cronología de autores. Debe hacer explícitas semejanzas, diferencias y límites relevantes, sin declarar novelty universal ni convertir diferencias arquitectónicas en novelty por sí mismas.

**Bloque actualmente autorizado:** únicamente 2.1.

### 8. Función de las demás secciones

- **Introduction:** `problema → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones → contexto de evaluación → RQs → roadmap`.
- **Decision-support architecture:** arquitectura general en relaciones entrada–operación–salida, antes de detalles experimentales.
- **Experimental design:** testbed específico, datos históricos, corpus documental, particiones/dependencia, configuración, evaluación, estadística y reproducibilidad.
- **Results:** organizados por función/RQ, no por códigos internos de experimento.
- **Discussion:** interpretación, comparación, implicaciones, condiciones de transferencia y limitaciones.
- **Conclusion:** `aporte → evidencia principal → alcance → implicación`.

### 9. Ciclo obligatorio de cada bloque

1. verificar baseline/master acumulativo vigente;
2. leer onboarding, MWDP, KBS-34, SPCCR, estado y decisiones vigentes;
3. verificar fuentes y dependencias;
4. re-recuperar full text para cada cita;
5. redactar exclusivamente el bloque autorizado dentro del Word/Markdown acumulativo;
6. incluir comentarios de auditoría anclados a cada cita inglesa;
7. auditar contenido científico, prosa KBS-34, fluidez y ubicación narrativa;
8. activar IA Experimental solo si existe trigger real;
9. resolver observaciones;
10. solicitar aprobación expresa del autor;
11. integrar al master canónico solo después de aprobación.

### 10. Criterios de aprobación

Una sección solo puede pasar a `APPROVED` cuando:

- cumple su función narrativa;
- cada afirmación está respaldada;
- no presenta resultados pendientes como hechos;
- evita introducción prematura del testbed;
- evita abstracción y nominalización innecesarias;
- mantiene relaciones claras de agente/objeto/acción o entrada–operación–salida;
- respeta separación histórico/documental/LLM;
- no confunde reproducibilidad, configurabilidad y generalización;
- EN/ES son semánticamente equivalentes;
- cifras y referencias coinciden entre idiomas;
- comentarios de cita cumplen MWDP;
- no existe objeción experimental crítica cuando aplique;
- el autor aprueba expresamente.

### 11. Front matter, end matter y journal targeting

Title, Abstract y Keywords se redactan al final. El end matter contemplará `Data availability`, `Code and reproducibility resources` si corresponde, CRediT, Funding, Declaration of competing interest, Acknowledgements si aplica, References y Supplementary material cuando sea necesario.

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

Antes del paquete final se volverán a verificar los requisitos oficiales vigentes de KBS.

---

## English

### 1. Purpose and authority

This V2.1 plan activates drafting under the author-approved article structure. The manuscript must be built cumulatively, under `KBS_EWG_34_V01`, `MWDP_V1.0`, the Claim–Evidence Matrix, frozen 0B literature, and governing experimental sources when relevant.

### 2. Approved cumulative architecture

The frozen drafting structure is `Introduction → Related work → Decision-support architecture → Experimental design → Results → Discussion → Conclusion → KBS end matter`. The exact structure is `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, approved by D-015.

The bootstrap Word baseline is `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`, SHA-256 `0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5`.

### 3. Cumulative Word policy

The first drafting block must use the exact approved structural Word. After the first author-approved integration, each subsequent block starts from the latest approved `ARTICLE_MASTER_V00N`. No section-only Word, silent reconstruction, or automatic reuse of rejected prose is allowed. Lack of exact baseline access requires `BASELINE_DOCX_ACCESS_REQUIRED`.

### 4. Operational drafting order

`Related Work → provisional Introduction → Decision-support architecture → Experimental design → authorized Results → figures/tables → pending-result integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → final KBS adaptation`.

The former Methods-first sequence remains superseded.

### 5. Active phase

Related Work is active. It is organized as 2.1 automated tariff classification and candidate retrieval; 2.2 knowledge-enhanced retrieval and regulatory reasoning; 2.3 LLMs for classification, reasoning, and explanation; 2.4 evidence grounding, explainability, and auditability; 2.5 reproducibility/evaluation in knowledge-based decision support; and 2.6 study positioning.

Only `Related Work B01 — Section 2.1` is currently authorized.

### 6. Block discipline

Each block requires exact baseline/master verification, full onboarding, source re-retrieval for every citation, cumulative bilingual drafting, mandatory citation-audit comments in the English Word, KBS-34 prose QA, author approval, and canonical integration only after approval.

Scientific scope, RQs, claims, experimental design and experimental governance remain unchanged by D-014/D-015.

### 7. Journal targeting

Target A remains Knowledge-Based Systems, with Expert Systems with Applications and Information Processing & Management as Plans B/C. KBS publication route remains subscription. Current official submission requirements will be revalidated before final submission.