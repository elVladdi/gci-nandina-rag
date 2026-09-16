# Fase 1 — Methods B01 — Revisión V02 / Closed Revision Prompt

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Corrige exclusivamente la entrega `Methods B01 — Design, scope, and units` V01. No avances a B02 ni a ninguna otra sección.

Usa como punto de control editorial el estado posterior al rechazo del autor y lee íntegramente, además del onboarding/MWDP obligatorio:

- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`;
- `article/ARTICLE_STATUS.md`;
- `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`;
- `article/sections/methods/Methods_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`;
- el `SRC-03` vivo indicado en `SOURCE_REGISTRY.md`;
- este prompt.

El estado experimental correcto para este corte es `GROUP3 = NOT_STARTED`. No uses resultados ni inferencias de Grupo 3.

### Correcciones obligatorias

#### B01-M01 — Sustituir lenguaje de gobernanza interna

Eliminar `governing study artifacts` / `artefactos gobernantes del estudio` y sustituirlo por redacción científica autosuficiente orientada al lector.

#### B01-M02 — Definir correctamente DAM en inglés

En la primera aparición inglesa, definir DAM mediante la denominación administrativa `Declaración Aduanera de Mercancías (DAM; customs declaration)` o una formulación natural semánticamente equivalente. En español mantener `Declaración Aduanera de Mercancías (DAM)`.

#### B01-M03 — Eliminar claim positivo de configurabilidad

Eliminar la afirmación positiva de configurabilidad fuera del setting evaluado. Mantener únicamente que la evaluación no establece generalización empírica fuera de Capítulo 87. No añadir C15.

#### B01-M05 — Reencuadre editorial obligatorio solicitado por el autor

La V01 fue rechazada por el autor porque la apertura hace que el trabajo parezca, desde la primera lectura, **un experimento específico para NANDINA/Clase 87** antes de mostrar qué ofrece científicamente el artículo.

La V02 debe invertir el orden conceptual:

1. **Primero:** presentar el objeto científico general como una **arquitectura auditable de apoyo a decisión** que separa explícitamente:
   - generación/ranking histórico de candidatos;
   - recuperación posterior de evidencia normativa para candidatos ya fijados;
   - explicación downstream con LLM local sobre un Top-3 inmutable;
   - ausencia de capacidad del LLM para insertar, eliminar, sustituir o reordenar candidatos, o retroalimentar la clasificación.
2. **Después:** presentar **NANDINA Capítulo 87 como testbed/caso experimental regulatorio** utilizado para evaluar esa arquitectura.
3. El lector debe comprender primero **qué ofrece el artículo** y solo después **dónde se evalúa**.
4. No declarar novelty final, superioridad, generalización fuera de Clase 87 ni ausencia de prior art.
5. El reencuadre debe ser científico y sobrio, no promocional.

Una secuencia conceptual válida es:

```text
AUDITABLE DECISION-SUPPORT ARCHITECTURE
→ functional decoupling of ranking / normative evidence / LLM explanation
→ immutable fixed Top-3 and no generative feedback
→ evaluated in a controlled regulatory testbed
→ NANDINA Chapter 87
```

No es obligatorio usar literalmente esas palabras; sí preservar ese orden y sentido.

### Contenido científico que debe conservarse

Conservar, con los ajustes necesarios para el nuevo encuadre:

- piloto experimental aplicado y offline;
- Capítulo 87 como **alcance empírico del testbed**, no como objeto científico principal de la primera oración;
- apoyo a decisión no vinculante;
- revisión experta fuera del flujo automático;
- historical retrieval = generación/ranking de candidatos;
- normative retrieval = evidencia documental sin sustituir/reordenar el ranking histórico;
- local LLM = explicación downstream del Top-3 fijo, sin clasificación desde cero ni inserción/eliminación/sustitución/reordenamiento/feedback;
- SERIE como unidad de observación/análisis;
- DAM como unidad de agrupamiento cuando la dependencia sea metodológicamente relevante;
- SERIE/descripción comercial normalizada como unidad de consulta;
- historical Top-k y fixed historical Top-3 como objetos de salida correspondientes.

No introduzcas resultados, cifras, métricas, inferencia, causalidad, gap final, novelty, literatura externa ni contenido de B02–B09.

### Claims

Los únicos claims declarados para B01 siguen siendo:

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
```

El reencuadre editorial de B01-M05 no autoriza claims adicionales.

### Citación

Mantener `CITATION_COMMENT_COVERAGE = 0/0`. No añadir literatura externa para resolver estas correcciones.

### Artefactos V02

No sobrescribas ni elimines los artefactos V01. Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V02.md`;
2. `article/sections/methods/Methods_B01_V02.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.docx`.

`ARTICLE_MASTER_CANDIDATE_V02.*` sigue siendo candidato y contiene únicamente B01 revisado. No crees `ARTICLE_MASTER_V001.*`; la integración canónica requiere aprobación expresa del autor.

No modifiques `ARTICLE_STATUS.md`, reviews, prompts, `DECISIONS.md`, `CLAIM_EVIDENCE_MATRIX.md`, literatura congelada ni Plan Maestro.

### Word V02

El `.docx` debe reproducir exactamente el contenido científico de `ARTICLE_MASTER_CANDIDATE_V02.md` y conservar:

- Part I — English manuscript master;
- Part II — Spanish semantic-control mirror;
- layout neutral/reversible y editable;
- cero citas y, por tanto, cero comentarios de cita en este bloque;
- ausencia de Mendeley o campos bibliográficos simulados.

### Checklist de salida

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V02
B01_M01 = ADDRESSED
B01_M02 = ADDRESSED
B01_M03 = ADDRESSED
B01_M05 = ADDRESSED
SOURCE_SNAPSHOT(S) = [SHAs realmente leídos]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```

No declares B01 `APPROVED` ni `FROZEN`.

---

## English

Revise only `Methods B01 — Design, scope, and units` V01. Do not advance to B02. Read both the internal V01 review and the author V01 review in full, together with the mandatory onboarding/MWDP artifacts.

Apply B01-M01, B01-M02, B01-M03, and the author-mandated **B01-M05 positioning correction**. V02 must first present the broader scientific object—an auditable decision-support architecture that functionally decouples candidate ranking, normative-evidence retrieval, and downstream LLM explanation while preserving an immutable fixed Top-3 and preventing generative feedback—and only then introduce NANDINA Chapter 87 as the controlled regulatory experimental testbed.

Do not convert this positioning change into a final novelty, superiority, or generalization claim. Keep `AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]`, add no external literature, results, metrics, or later-Methods content, and keep citation-comment coverage at `0/0`.

Create only the four V02 artifacts listed above. Do not overwrite V01 or create `ARTICLE_MASTER_V001.*`. End with the exact checklist and `POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND`.
