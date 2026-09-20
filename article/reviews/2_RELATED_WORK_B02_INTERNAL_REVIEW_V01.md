# Related Work B02 — Internal Review V01 / Revisión interna V01

## Español

```text
REVIEW_ID = RELATED_WORK_B02_INTERNAL_REVIEW_V01
REVIEW_DATE = 2026-09-19
BLOCK = RELATED_WORK_B02
SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
DELIVERY_COMMIT = 5e58b5a45b1dcc50a4a324f38e5cc0c9746ef3dc
INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT = PASS
SOURCE_SUPPORT = PASS
COMMENT_SOURCE_ALIGNMENT = PASS
KBS_EDITORIAL_FIT = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
DOCX_INTEGRITY = PASS
CITATION_COMMENT_COVERAGE = 6/6 NEW + 8/8 PRESERVED = 14/14 / PASS
MATERIAL_CORRECTIONS_REQUIRED = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED / CONDITIONAL_ON_AUDIT / NOW_EFFECTIVE
INTEGRATION = AUTHORIZED
```

### 1. Alcance y disciplina de entrega

Se comparó `5e58b5a45b1dcc50a4a324f38e5cc0c9746ef3dc` contra el commit base solicitado `674f55c8573c78cdc01f7eca2b5150b3070fcfb9`. La entrega está exactamente un commit por delante y contiene únicamente los cuatro artefactos autorizados: bloque B02 bilingüe, master candidato Markdown, master candidato DOCX e informe de respuesta. No se inició 2.3 ni ninguna otra sección.

### 2. Auditoría independiente claim–cita–fuente

Las seis fuentes citadas en 2.2 fueron re-recuperadas y contrastadas con su full text primario. No se aceptó el `6/6` de la IA de Redacción como prueba suficiente: se verificó que cada comentario Word contenga un pasaje real de la fuente, que el pasaje respalde el claim al que está anclado y que el límite de alcance sea compatible con el paper.

- **Qi et al. (2025): PASS.** El full text confirma que la información de declaración se convierte en conocimiento de atributos, se construye un knowledge graph y KBGAT formula la predicción HS como link completion. El manuscrito usa la fuente solo para mostrar conocimiento estructurado dentro de la inferencia, sin convertirlo en evidencia normativa posterior.
- **Lee et al. (2021): PASS.** La fuente confirma el flujo `HS4 prediction → key-sentence retrieval from HS manual → HS6 prediction using description + retrieved sentences`. El manuscrito representa correctamente que el retrieval participa en una predicción posterior.
- **Lee et al. (2023): PASS.** El full text declara dos etapas: primero predicción de clasificación y luego recuperación de evidencia sobre cada candidato desde el HS manual; las salidas incluyen candidatos y key sentences para inspección. El manuscrito no eleva esa evidencia visible a corrección jurídica ni auditabilidad formal.
- **Wang et al. (2026): PASS.** El preprint confirma searchable regulatory tree, retrieval local de child nodes y supporting evidence, candidate packages, decisión next-hop/stop y agregación de evidencia después de fijar la ruta para verificación/rationale. El manuscrito conserva correctamente que la normativa participa en la trayectoria clasificatoria. Se mantiene como **preprint** hasta verificar una eventual versión editorial final.
- **Lewis et al. (2020): PASS.** La fuente confirma retriever neuronal + índice no paramétrico + generador seq2seq dentro de un modelo probabilístico, con generación condicionada por input y documentos recuperados. El manuscrito no interpreta RAG como garantía de grounding o atribución completa.
- **Ma et al. (2023): PASS.** La fuente confirma Rewrite-Retrieve-Read, rewriter anterior al retrieval, black-box LLM reader y variante entrenable con feedback del reader mediante reinforcement learning. La interpretación de la query reescrita como control del retrieval y no como evidencia del claim final es consistente con la arquitectura reportada.

Los comentarios nuevos IDs 8–13 reproducen pasajes existentes en las fuentes y sus traducciones/justificaciones son fieles. Los comentarios previos 0–7 de 2.1 permanecen preservados.

### 3. Fronteras científicas

La subsección distingue correctamente conocimiento estructurado usado en predicción, documentos recuperados que alimentan una decisión posterior, evidence retrieval para inspección humana, regulation-driven hierarchical search, RAG y query rewriting. No mezcla estas funciones bajo una sola categoría.

También conserva las fronteras obligatorias `retrieved passage ≠ evidence attribution ≠ grounding guarantee ≠ formal auditability ≠ legal correctness`. No introduce la arquitectura del presente estudio, Top-3 fijo, NANDINA/Chapter 87, H100, DAM, corpus peruano, resultados propios, `FINAL_GAP` ni novelty universal.

No se identificaron errores científicos materiales ni claims que excedan la evidencia disponible.

### 4. Auditoría editorial KBS-34

La prosa es funcional y comparativa, no un catálogo de papers. Cada párrafo responde a una función distinta del conocimiento externo y la subsección concluye preparando 2.3. La densidad de abstracción es aceptable y las relaciones componente–acción–efecto son visibles.

Controles no bloqueantes para etapas posteriores:

1. la caracterización de Wang et al. debe conservarse como preprint mientras no se verifique una versión publicada;
2. afirmaciones metodológicas del tipo `inspectable evidence does not establish legal correctness/auditability` deben mantenerse como delimitaciones epistemológicas y no presentarse como métricas empíricas de esos papers;
3. en 2.3 se deberá distinguir rigurosamente `generative LLM classification`, `fine-tuned transformer classifier`, `LLM as search/decision controller`, `reader/reasoner` y `explanation-only generator`.

### 5. Auditoría independiente del Word

El DOCX proporcionado por el autor fue verificado directamente:

```text
FINAL_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
OOXML_ZIP_INTEGRITY = PASS
WORD_DOCUMENT_XML = PRESENT
COMMENTS_XML = PRESENT
COMMENT_RANGE_START = 14
COMMENT_RANGE_END = 14
COMMENT_REFERENCE = 14
COMMENTS_TOTAL = 14
PRIOR_COMMENTS_2_1 = 8/8 PRESERVED
NEW_COMMENTS_2_2 = 6/6
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
RENDER = PASS / 19_OF_19_PAGES_INSPECTED
LAYOUT_DEFECTS = NONE
```

Se renderizaron nuevamente las 19 páginas mediante el flujo de verificación DOCX y se inspeccionaron visualmente todas las páginas. No se observaron clipping, solapamientos, tablas rotas, pérdida de glifos ni alteraciones accidentales de las demás secciones.

### 6. Dictamen y gate

El autor aprobó B02 V01 condicionado a esta auditoría. Al resultar `PASS`, la aprobación queda efectiva.

```text
RELATED_WORK_B02_V01 = APPROVED / FROZEN / READY_FOR_INTEGRATION
AUTHOR_APPROVAL = EFFECTIVE
BLOCK_REVISION_V02 = NOT_REQUIRED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
NEXT_ELIGIBLE_SECTION_AFTER_INTEGRATION = 2.3 LLMs for classification, reasoning, and explanation
```

---

## English

Related Work B02 V01 was independently audited against the governing prompt, frozen literature maps, six primary full texts, citation-comment contents, KBS-34 editorial guide, and the cumulative DOCX. The delivery contains exactly the four authorized artifacts in one commit over the requested base.

All six new citations passed claim-to-source verification. The quoted passages in comments 8–13 exist in the cited full texts and support the manuscript claims within their stated limits. Prior Section-2.1 comments 0–7 remain preserved. No prohibited present-study claims, final-gap statements, universal novelty claims, or premature testbed details were introduced.

The DOCX independently passed SHA-256 verification, OOXML integrity, 14/14 comment anchors, zero tracked changes, and full 19-page render inspection. No material correction is required. Because the author had approved V01 subject to this audit, the PASS makes that approval effective and authorizes canonical integration and opening of Section 2.3.