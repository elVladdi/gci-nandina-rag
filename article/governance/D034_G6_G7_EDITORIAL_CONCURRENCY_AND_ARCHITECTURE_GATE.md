# D-034 — Concurrencia editorial G6/G7 y apertura del gate de arquitectura

## Español

```text
DECISION_ID = D-034
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PURPOSE = RECONCILE_EXPERIMENTAL_G6_G7_SEQUENCE_WITH_ARTICLE_EDITORIAL_FLOW
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
G7_F01_BEFORE_WRITING_INTERPRETATION = BEFORE_FORMAL_G7_DRAFTING_OR_UPDATE
FINAL_FIGURE_INTEGRATION = WAIT_FOR_GROUP6
FINAL_FIGURE_CAPTIONS = WAIT_FOR_GROUP6
FINAL_CROSS_REFERENCES_TO_FIGURES = WAIT_FOR_GROUP6
FINAL_RESULTS_NARRATIVE = PROVISIONAL_UNTIL_GROUP6_WHERE_FIGURE_INTEGRATION_IS_REQUIRED
FINAL_DISCUSSION_INTEGRATION = PROVISIONAL_UNTIL_GROUP6
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_AFTER_GROUP7_ONLY = false
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_YET_AUTHORIZED
GROUP6 = NOT_STARTED / NOT_AUTHORIZED_BY_D034
GROUP7 = NOT_ACTIVATED / PROSPECTIVE
GROUP8 = NOT_ACTIVATED / PROSPECTIVE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Motivo y fuentes revisadas

Después de integrar `Introduction B01 V02` mediante D-033, el gate quedó temporalmente detenido para reconciliar la dependencia prospectiva entre los Grupos 6 y 7 del Plan Maestro experimental con la gobernanza editorial autónoma de `article/main-manuscript`.

La IA Gestora revisó directamente:

- el Plan Maestro experimental vigente, con Grupo 5 `CLOSED / APPROVED`, Grupo 6 `NOT_STARTED` y G6-F01 `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`;
- `docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md`;
- `docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md`;
- `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`;
- G6-F01, G6-F02 y G6-F03;
- G7-F01, G7-F02 y G7-F03;
- el dictamen metodológico solicitado a la IA Experimental, cuya interpretación es consistente con esas fuentes y no modifica el Plan Maestro.

### 2. Interpretación vinculante de la dependencia G6 → G7

La regla `G7 ← GROUP6 CLOSED / APPROVED` gobierna la **activación formal de las fichas del Grupo 7**. No constituye una prohibición global de continuar la redacción progresiva del artículo bajo su propia gobernanza editorial.

Por tanto:

- `Decision-support architecture` puede redactarse antes del cierre de Grupo 6;
- `Experimental design` podrá redactarse después del gate editorial de Architecture, aun si Grupo 6 continúa abierto;
- G7-F01 no puede activarse formalmente hasta que Grupo 6 esté `CLOSED / APPROVED`;
- G7-F02 y G7-F03 continúan sujetos a la secuencia formal del Grupo 7.

La frase de G7-F01 que exige congelar fuentes “antes de escribir” se interpreta, para evitar contradicción con G7-F03 y con la gobernanza editorial ya existente, como **antes de la redacción/actualización formal gobernada por Grupo 7**, no como un embargo sobre todo borrador editorial previo de `article/main-manuscript`.

### 3. Función de Grupo 6 en el artículo

Grupo 6 gobierna la especificación, generación reproducible, captions, accesibilidad y cierre de figuras científicas. No redefine la arquitectura del sistema, el diseño experimental ya ejecutado ni los claims/cifras congelados por G3–G5.

Mientras Grupo 6 no cierre, permanecen no definitivos:

- la selección y numeración final de figuras;
- captions finales;
- referencias cruzadas a figuras;
- ubicación principal/secundaria/suplementaria de representaciones visuales;
- pasajes de Results o Discussion cuya forma final dependa de una figura concreta.

Esto no impide usar evidencia científica ya congelada para preparar texto provisional cuando el gate editorial correspondiente se abra.

### 4. Función de Grupo 7 y Grupo 8

G7-F03 se interpreta como **sincronización y cierre transversal** de un artículo desarrollado progresivamente, no como inicio de su existencia. Debe reconciliar el manuscrito con el estado científico final de G3–G6 respetando la gobernanza propia del artículo.

Grupo 8 conserva una función distinta y posterior: auditoría final claim→evidencia→cifra, coherencia Métodos–Resultados–Discusión, consistencia texto–tablas–figuras, límites de validez y decisión de readiness para el freeze científico.

En forma compacta:

```text
G7 = MATERIALIZA / SINCRONIZA
G8 = AUDITA / DECIDE FREEZE
```

El cierre de Grupo 7 no equivale al freeze científico final.

### 5. Apertura del siguiente gate editorial

D-033 dejó Introduction cerrada e integrada en `ARTICLE_MASTER_V007`. Con la reconciliación anterior, no queda una dependencia G6/G7 que impida el siguiente bloque.

Se autoriza:

```text
CURRENT_DRAFTING_PHASE = DECISION_SUPPORT_ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B01
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
```

La autorización inicial se limita al bloque Architecture B01 que defina la vista general, representación de consulta, recuperación/ranking histórico y conjunto fijo de candidatos. La autorización de cualquier bloque posterior deberá quedar explícita en su prompt y gate correspondiente.

### 6. Lo que D-034 no autoriza

D-034 no autoriza:

- iniciar o cerrar Grupo 6;
- activar Grupo 7;
- activar Grupo 8;
- redactar Results o Discussion como definitivos;
- incorporar figuras finales;
- modificar el Plan Maestro experimental;
- declarar novelty, SOTA, generalización empírica o corrección jurídica;
- abrir `Experimental design` en la misma ejecución que Architecture B01.

---

# D-034 — G6/G7 editorial concurrency and architecture gate opening

## English

```text
DECISION_ID = D-034
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PURPOSE = RECONCILE_EXPERIMENTAL_G6_G7_SEQUENCE_WITH_ARTICLE_EDITORIAL_FLOW
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
G7_F01_BEFORE_WRITING_INTERPRETATION = BEFORE_FORMAL_G7_DRAFTING_OR_UPDATE
FINAL_FIGURE_INTEGRATION = WAIT_FOR_GROUP6
FINAL_FIGURE_CAPTIONS = WAIT_FOR_GROUP6
FINAL_CROSS_REFERENCES_TO_FIGURES = WAIT_FOR_GROUP6
FINAL_RESULTS_NARRATIVE = PROVISIONAL_UNTIL_GROUP6_WHERE_FIGURE_INTEGRATION_IS_REQUIRED
FINAL_DISCUSSION_INTEGRATION = PROVISIONAL_UNTIL_GROUP6
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_AFTER_GROUP7_ONLY = false
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_YET_AUTHORIZED
GROUP6 = NOT_STARTED / NOT_AUTHORIZED_BY_D034
GROUP7 = NOT_ACTIVATED / PROSPECTIVE
GROUP8 = NOT_ACTIVATED / PROSPECTIVE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Rationale and reviewed sources

After `Introduction B01 V02` was integrated through D-033, the gate was temporarily held to reconcile the prospective dependency between experimental Groups 6 and 7 with the autonomous editorial governance of `article/main-manuscript`.

The Managing AI directly reviewed the current experimental Master Plan; the master ficha map, dependency matrix, and state registry; G6-F01–G6-F03; G7-F01–G7-F03; and the methodological opinion requested from the Experimental AI. The Experimental AI interpretation is consistent with those governing sources and does not modify the Master Plan.

### 2. Binding interpretation of the G6 → G7 dependency

The rule `G7 ← GROUP6 CLOSED / APPROVED` governs the **formal activation of Group 7 fichas**. It is not a global prohibition on progressive article drafting under the article's own editorial governance.

Therefore, `Decision-support architecture` may be drafted before Group 6 closes, and `Experimental design` may later be drafted after its own editorial gate. G7-F01 may not be formally activated until Group 6 is `CLOSED / APPROVED`, and G7-F02/G7-F03 remain subject to their formal sequence.

G7-F01's phrase requiring source freezing “before writing” is interpreted as before the formal drafting/update governed by Group 7, not as an embargo on all prior editorial development of `article/main-manuscript`.

### 3. Role of Group 6 for the article

Group 6 governs figure specification, reproducible generation, captions, accessibility, and figure closure. It does not redefine the system architecture, the executed experimental design, or claims/numbers already frozen by G3–G5.

Until Group 6 closes, final figure selection/numbering, final captions, figure cross-references, visual placement, and Results/Discussion passages whose final form depends on a specific figure remain provisional. This does not prevent drafting based on already frozen scientific evidence when the applicable editorial gate is open.

### 4. Roles of Group 7 and Group 8

G7-F03 is interpreted as **synchronization and transversal closure** of an article developed progressively, not as article inception. It must reconcile the manuscript with the final G3–G6 scientific state while respecting article governance.

Group 8 has a separate later function: final claim→evidence→number audit, Methods–Results–Discussion coherence, text–table–figure consistency, validity limits, and scientific-freeze readiness.

```text
G7 = MATERIALIZE / SYNCHRONIZE
G8 = AUDIT / DECIDE FREEZE
```

Group 7 closure alone is not the final scientific freeze.

### 5. Opening the next editorial gate

D-033 closed and integrated Introduction into `ARTICLE_MASTER_V007`. After this reconciliation, no G6/G7 dependency blocks the next manuscript block.

```text
CURRENT_DRAFTING_PHASE = DECISION_SUPPORT_ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B01
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
```

The initial authorization is limited to Architecture B01: overview, query representation, historical retrieval/ranking, and the fixed candidate set. Any later block requires its own explicit gate and prompt.

### 6. What D-034 does not authorize

D-034 does not authorize Group 6, Group 7, or Group 8 execution; final Results or Discussion; final figures; changes to the experimental Master Plan; novelty/SOTA/generalization/legal-correctness claims; or `Experimental design` within the same Architecture B01 execution.