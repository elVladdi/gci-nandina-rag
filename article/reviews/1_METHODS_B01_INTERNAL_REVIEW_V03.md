# Methods B01 — Revisión interna V03 / Internal Review V03

## Español

### 1. Alcance de la auditoría

La IA Gestora auditó independientemente la entrega V03 del commit `5a3d78c0eedf6d14b79e5a9470c8f8c90a2dc2b1` contra:

- `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V03.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V02.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`);
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` (`SPCCR_V1.0`);
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`;
- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- el estado editorial y experimental vivo aplicable.

El commit de entrega es descendiente directo del punto de partida autorizado `706df9fc12d40accd05f3910540ad5018fce34f8` y añade únicamente los cuatro artefactos V03 autorizados. No se modificaron V01/V02, archivos de gobernanza, matrices, literatura congelada ni B02.

### 2. Dictamen científico-editorial

```text
METHODS_B01_V03_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
SCIENTIFIC_CONTENT_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = B01-M09
B01_M06 = CLOSED
B01_M07 = CLOSED
B01_M08 = CLOSED
B01_M01_M02_M03_M05 = PRESERVED_CLOSED
AUTHOR_REVIEW_READY = NO
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La prosa científica V03 satisface las correcciones sustantivas solicitadas por el autor:

- **B01-M06 — CLOSED.** Se redujo la acumulación de abstracciones y nominalizaciones. La secuencia identifica de forma concreta qué recibe cada componente, qué hace, qué produce y qué no puede modificar.
- **B01-M07 — CLOSED.** El texto hace visible el contrato funcional completo: recuperación histórica y Top-3 fijo → evidencia documental sin reranking → LLM local que recibe candidatos más evidencia → explicación restringida sin inserción, eliminación, sustitución, reordenamiento ni feedback. Además, deja explícito que ranking, evidencia y explicación se evalúan como funciones distintas, sin anticipar métricas ni resultados.
- **B01-M08 — CLOSED.** Se declara de forma acotada que una instancia puede usar un dataset/banco histórico etiquetado propio, un universo de clases objetivo y un corpus documental o normativo apropiado al dominio, manteniendo el mismo contrato funcional. La frase distingue expresamente esta configurabilidad/replicabilidad de la generalización empírica.

El orden de lectura queda correctamente establecido como:

```text
GENERAL_METHOD_AND_FUNCTIONAL_CONTRACT_FIRST
→ CONFIGURABILITY_BOUNDARY_SECOND
→ NANDINA_CH87_TESTBED_THIRD
→ SCOPE_AND_UNITS
```

No se detectaron resultados, cifras, métricas concretas, inferencias estadísticas, causalidad, novelty final, superioridad, ausencia universal de prior art, literatura externa, EXP-11B, resultados de Grupo 3 ni contenido técnico reservado a B02–B09. Los claims utilizados permanecen dentro de `[C01, C02, C03, C07, C15]`, con C15 restringido a configurabilidad/replicabilidad de diseño.

La equivalencia semántica EN–ES es adecuada en funciones, restricciones, configurabilidad, alcance y unidades. `CITATION_COMMENT_COVERAGE = 0/0` sigue siendo correcto.

### 3. Defecto de entrega obligatorio

#### B01-M09 — Integridad inválida del paquete DOCX

El archivo versionado:

`article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.docx`

no constituye un paquete DOCX/OOXML válido y, por tanto, no puede pasar el gate de entrega de `MWDP_V1.0`.

La auditoría recuperó exactamente el blob GitHub:

```text
DOCX_BLOB_SHA = 5dec60d1ebeff158c114aaed84c992953d256175
DOCX_SIZE_BYTES = 15007
GIT_BLOB_IDENTITY_CHECK = PASS
OOXML_ZIP_INTEGRITY = FAIL
END_OF_CENTRAL_DIRECTORY = MISSING
PYTHON_ZIPFILE_OPEN = FAIL / BadZipFile
LIBREOFFICE_RENDER = FAIL / source file could not be loaded
```

Por este motivo no es posible validar visualmente el Word ni verificar desde un paquete OOXML legible su equivalencia final, comentarios, campos o layout. La afirmación de la respuesta V03 de que el Word reproduce correctamente el master no queda verificada y debe corregirse mediante una nueva entrega versionada, sin sobrescribir V03.

La corrección es **de integridad/entrega, no científica**. El contenido científico de V03 no debe reescribirse.

### 4. Corrección requerida

```text
B01_M09 = REVISION_REQUIRED / DOCX_PACKAGE_INTEGRITY
V03_SCIENTIFIC_TEXT = PRESERVE_WITHOUT_SUBSTANTIVE_CHANGE
NEXT_ACTOR = DRAFTING_AI
NEXT_PROMPT = article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V04.md
AUTHOR_APPROVAL_METHODS_B01_V03 = NOT_REQUESTED_YET
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

V04 debe preservar el contenido científico aprobado internamente de V03 y regenerar un `.docx` válido, editable y renderizable. No se autoriza ninguna expansión científica ni avance a B02.

---

## English

### Internal verdict

```text
METHODS_B01_V03_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
SCIENTIFIC_CONTENT_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = B01-M09
B01_M06 = CLOSED
B01_M07 = CLOSED
B01_M08 = CLOSED
B01_M01_M02_M03_M05 = PRESERVED_CLOSED
AUTHOR_REVIEW_READY = NO
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

V03 satisfactorily resolves the author-mandated prose, complete-functional-contract, and bounded-configurability corrections. The scientific text correctly presents the general method and functional contract first, bounded configurability second, NANDINA Chapter 87 as the empirical testbed third, and scope/units afterward. It introduces no unauthorized results, metrics, inference, novelty, causal claims, literature, EXP-11B, Group-3 results, or later-Methods content.

However, the committed `ARTICLE_MASTER_CANDIDATE_V03.docx` blob (`5dec60d1ebeff158c114aaed84c992953d256175`, 15007 bytes) is not a valid OOXML ZIP package: the end-of-central-directory record is missing, Python `zipfile` raises `BadZipFile`, and LibreOffice cannot load/render the file. Therefore the Word-delivery gate fails and author review cannot begin yet.

`B01-M09` requires a new versioned delivery that preserves V03 scientific content without substantive change and regenerates a valid, editable, renderable bilingual DOCX. B02 remains unauthorized.