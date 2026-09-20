# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.2
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V003
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V003.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
CANONICAL_MASTER_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_AUTHORIZED_BLOCK = RELATED_WORK_B04 / SECTION_2.4_ONLY
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construye sobre una estructura acumulativa aprobada y cada bloque autorizado completa esa misma base.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, la Claim–Evidence Matrix, la literatura congelada de 0B y las fuentes experimentales gobernantes cuando correspondan.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- El lector debe comprender primero problema y posicionamiento, después la arquitectura general y solo entonces la instanciación experimental específica.
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

La estructura congelada para redacción permanece:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada está en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, aprobada mediante D-015. `Limitations` permanece integrada como `6.6 Limitations` salvo futura enmienda expresa.

### 4. Política acumulativa del Word

1. El bootstrap inicial partió del Word estructural aprobado.
2. Cada bloque posterior parte del último `ARTICLE_MASTER_V00N` aprobado.
3. El baseline actual es `ARTICLE_MASTER_V003.md/.docx`, SHA-256 DOCX `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.
4. No se crean Words independientes por sección.
5. La sección nueva se inserta directamente en su ubicación estructural.
6. Solo se eliminan las notas editoriales correspondientes a la sección que se completa.
7. Part I y Part II deben conservar equivalencia semántica.
8. Las versiones de trabajo permanecen como candidatas hasta aprobación expresa del autor.
9. Ningún texto previamente rechazado se reutiliza automáticamente.
10. Si el baseline exacto no es accesible, la IA de Redacción debe detenerse con `BASELINE_DOCX_ACCESS_REQUIRED`; no se autoriza reconstrucción silenciosa.
11. Todo bloque debe preservar exactamente el texto y los comentarios de auditoría de las secciones ya aprobadas.

### 5. Estado previo y reset

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| 0D original | CLOSED / APPROVED / FROZEN; arquitectura de secciones supersedida por D-014 |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work B01 / 2.1 | APPROVED / FROZEN / INTEGRATED |
| Related Work B02 / 2.2 | APPROVED / FROZEN / INTEGRATED |
| Related Work B03 / 2.3 | APPROVED / FROZEN / INTEGRATED |
| Related Work B04 / 2.4 | AUTHORIZED / ACTIVE |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

D-014 a D-018 modifican únicamente arquitectura/editorial workflow, aprobaciones de bloques y master acumulativo. No cambian alcance científico, RQs, claims autorizados, diseño experimental ni gobernanza del Plan Maestro.

### 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa del artículo | CLOSED / AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| 2 | Related Work | EN PROGRESO; 2.1–2.3 integradas; 2.4 activa |
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

- 2.1 `Automated tariff classification and candidate retrieval` — **APPROVED / FROZEN / INTEGRATED**;
- 2.2 `Knowledge-enhanced retrieval and regulatory reasoning` — **APPROVED / FROZEN / INTEGRATED**;
- 2.3 `LLMs for classification, reasoning, and explanation` — **APPROVED / FROZEN / INTEGRATED**;
- 2.4 `Evidence grounding, explainability, and auditability` — **AUTHORIZED / ACTIVE**;
- 2.5 `Reproducibility and evaluation in knowledge-based decision support` — **NOT AUTHORIZED**;
- 2.6 `Positioning of this study` — **NOT AUTHORIZED**.

Cada subsección debe sintetizar por problema/tarea/función y no por cronología de autores. Debe hacer explícitas semejanzas, diferencias y límites relevantes, sin declarar novelty universal ni convertir diferencias arquitectónicas en novelty por sí mismas.

**Bloque actualmente autorizado:** exclusivamente `Related Work B04 / Section 2.4`.

### 8. Función específica de B04

B04 debe explicar qué puede realmente verificarse cuando un sistema adjunta documentos, citas, rationales o trazas a una salida. La subsección deberá distinguir, cuando las fuentes primarias lo soporten:

- retrieved context frente a soporte semántico real del claim;
- explanation/rationale frente a faithfulness;
- provenance/lineage y traceability frente a substantive correctness;
- transparency trail o lifecycle audit frente a output-level auditability;
- source authority y documentary currency frente a correct legal interpretation;
- auditability frente a legal correctness.

Estas propiedades no deben presentarse como una escalera causal o de madurez. B04 puede utilizar literatura de provenance/auditing para delimitar conceptos, pero debe reservar para 2.5 la discusión principal sobre dataset documentation, reproducibility/replication/generalization, code/data availability y diseño/reporting de evaluación.

B04 no autoriza describir la arquitectura del presente estudio, Top-3 fijo, HE4, NANDINA/Chapter 87 ni resultados propios. Debe cerrar preparando 2.5.

### 9. Función de las demás secciones

- **Introduction:** `problema → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones → contexto de evaluación → RQs → roadmap`.
- **Decision-support architecture:** arquitectura general en relaciones entrada–operación–salida, antes de detalles experimentales.
- **Experimental design:** testbed específico, datos históricos, corpus documental, particiones/dependencia, configuración, evaluación, estadística y reproducibilidad.
- **Results:** organizados por función/RQ, no por códigos internos de experimento.
- **Discussion:** interpretación, comparación, implicaciones, condiciones de transferencia y limitaciones.
- **Conclusion:** `aporte → evidencia principal → alcance → implicación`.

### 10. Ciclo obligatorio de cada bloque

1. verificar baseline/master acumulativo vigente;
2. leer onboarding, MWDP, KBS-34, SPCCR, estado y decisiones vigentes;
3. verificar fuentes y dependencias;
4. re-recuperar full text primario para cada cita;
5. redactar exclusivamente el bloque autorizado dentro del Word/Markdown acumulativo;
6. incluir comentarios de auditoría anclados a cada cita inglesa;
7. auditar contenido científico, prosa KBS-34, fluidez y ubicación narrativa;
8. activar IA Experimental solo si existe trigger real;
9. resolver observaciones;
10. solicitar aprobación expresa del autor;
11. integrar al master canónico solo después de aprobación y auditoría.

### 11. Criterios de aprobación

Una sección solo puede pasar a `APPROVED` cuando:

- cumple su función narrativa;
- cada afirmación citada está respaldada por la fuente primaria exacta;
- los pasajes colocados en comentarios Word existen y soportan el claim anclado;
- no presenta resultados pendientes como hechos;
- evita introducción prematura del testbed;
- evita abstracción y nominalización innecesarias;
- mantiene relaciones claras de agente/objeto/acción o entrada–operación–salida;
- respeta separación histórico/documental/LLM;
- no confunde grounding, provenance, auditability, correctness, reproducibility, configurability y generalization;
- EN/ES son semánticamente equivalentes;
- cifras y referencias coinciden entre idiomas;
- comentarios de cita cumplen MWDP;
- no existe objeción experimental crítica cuando aplique;
- el autor aprueba expresamente.

### 12. Front matter, end matter y journal targeting

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

This V2.2 plan governs cumulative drafting under the author-approved KBS article structure. Related Work B01, B02, and B03 are approved, frozen, and integrated. The active canonical master is `ARTICLE_MASTER_V003.md/.docx`, DOCX SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.

### 2. Operational drafting order

`Related Work → provisional Introduction → Decision-support architecture → Experimental design → authorized Results → figures/tables → pending-result integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → final KBS adaptation`.

### 3. Active phase

Related Work is active. Sections 2.1–2.3 are integrated. Only `Related Work B04 — Section 2.4 Evidence grounding, explainability, and auditability` is currently authorized. Sections 2.5–2.6 and all later manuscript sections remain blocked.

B04 must distinguish visible/retrieved evidence from actual claim support, explanation from faithfulness, provenance/traceability from correctness, lifecycle audit from output-level auditability, and documentary authority/currency from substantive or legal correctness. It must not describe the present-study architecture or claim novelty.

### 4. Cumulative Word policy and audit

B04 must start from the exact canonical V003 DOCX and preserve Sections 2.1–2.3 and all nineteen citation-audit comments unchanged. Every new citation requires primary-full-text re-retrieval and a Word comment with exact supporting passage, Spanish translation, claim-source justification, and scope limitation. Author approval and Managing-AI audit are required before canonical integration.

Scientific scope, RQs, claims, experimental design and experimental governance remain unchanged.