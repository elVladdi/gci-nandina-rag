# Prompt — Discussion B03 / Section 6.3 — Comparison with prior work

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no recalcules resultados, no declares novelty y no avances fuera del bloque autorizado.

### Autorización

Ejecuta únicamente Discussion B03 V01 / Section 6.3 bajo:

`article/governance/D129_DISCUSSION_B03_SECTION6_3_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md`

Usa exclusivamente como baseline Markdown:

`article/manuscript/ARTICLE_MASTER_V025.md`

```text
SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
```

Usa como baseline Word exclusivamente:

`ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx`

```text
SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
COMMENTS = 44
TRACKED_CHANGES = 0
PAGE_COUNT = 62
```

No reconstruyas Word desde Markdown. D-035 sigue vigente: no Base64 manual, chunking, fragmentación ni reensamblado.

### Fuentes obligatorias

Interpreta exclusivamente contenido ya integrado de Sections 2.6, 3, 5.2–5.4, 5.7, 6.1 y 6.2.

Revalida antes de citar estas cuatro fuentes ya incorporadas en el manuscrito:

1. Lee et al. (2021): heading prediction → HS-manual sentence retrieval → later subheading prediction using description + retrieved sentences.
2. Lee et al. (2023): candidate prediction followed by evidence retrieval for those candidates; close prior art.
3. Marra de Artiñano et al. (2023): direct GPT-3.5 product categorization/classification.
4. Kim et al. (2025): retrieval/reranking coupled to an LLM-based HS classification pipeline.

No introduzcas nueva literatura.

### Función editorial de §6.3

Comparar el estudio con prior work por función, autoridad y secuenciación de componentes. La sección debe dejar claro qué está establecido por antecedentes y qué distingue metodológicamente el contrato evaluado, sin convertir esa diferencia en novelty, first-ever, state of the art ni superioridad.

No hagas comparaciones numéricas entre estudios: datasets, espacios de clases, niveles HS/NANDINA, protocolos y métricas no son equivalentes.

### Contenido obligatorio

Redacta aproximadamente 350–450 palabras en inglés y una versión española semánticamente equivalente. Usa preferentemente cinco párrafos por idioma:

1. **Marco comparativo.** Explica que la literatura combina clasificación, candidate prediction, retrieval, evidence y LLMs con distintos grados de acoplamiento. La comparación relevante es qué componente puede alterar la decisión y qué objeto evalúa cada trabajo.
2. **Retrieval/evidence en la decisión.** Cita exactamente una vez en inglés a Lee et al. (2021) y exactamente una vez a Lee et al. (2023). Explica que Lee 2021 deja que material recuperado participe en una predicción posterior; Lee 2023 ya establece candidate prediction seguida de documentary evidence. Señala que este segundo patrón es prior art cercano y que candidate prediction + evidence retrieval no es novelty del presente estudio.
3. **Autoridad del LLM.** Cita exactamente una vez en inglés a Marra de Artiñano et al. (2023) y exactamente una vez a Kim et al. (2025). Contrasta clasificación generativa directa y clasificación condicionada por retrieval con el rol explanation-only del LLM del presente estudio.
4. **Distinción metodológica evaluada.** Explica que el presente estudio fija el Top-3 histórico antes de evidencia/documentación, impide que downstream stages modifiquen membership/orden y evalúa por separado candidate retrieval, documentary association y controlled explanation. Puedes señalar que Results verificaron ranking invariance y structural preservation, pero sin convertir esos resultados en superioridad externa.
5. **Límite de posicionamiento.** Cierra indicando que la contribución comparativa reside en el contrato explícito de autoridad y en la evaluación descompuesta, no en reclamar componentes inéditos. Reitera que diferencias funcionales entre estudios no permiten inferir mayor accuracy, seguridad, corrección jurídica ni generalización.

### Claims permitidas

Puedes sostener que:

- distintos trabajos asignan distinta autoridad a retrieval, evidence y LLMs;
- Lee et al. (2023) es prior art cercano para candidate prediction + evidence retrieval;
- el presente estudio hace explícito un contrato de Top-3 fijo antes de las etapas downstream;
- documentary association y explanation no pueden modificar ranking en el primary flow;
- candidate retrieval, documentary association y explanation se evalúan como objetos separados;
- este posicionamiento es metodológico y operacional.

### Claims prohibidas

No afirmar ni implicar:

- novelty, first-ever o state of the art;
- superioridad global sobre prior work;
- comparabilidad numérica directa entre estudios;
- causalidad derivada de la separación arquitectónica;
- mayor seguridad o reducción de alucinaciones;
- overall classification accuracy;
- substantive normative correctness o legal correctness;
- external generalization;
- nuevos resultados, CI, p-values o tests;
- `FINAL_GAP`.

### Política de citas y comentarios Word

En la Parte I inglesa introduce exactamente cuatro nuevas ocurrencias bibliográficas, una por cada fuente autorizada. Cada ocurrencia debe tener exactamente un nuevo comentario de cita con soporte claim–fuente y límites de interpretación.

Preserva sin modificación los 44 comentarios heredados.

```text
COMMENTS = 48
TRACKED_CHANGES = 0
```

La Parte II española puede repetir las cuatro referencias, pero sin comentarios adicionales.

### Diferencial autorizado

Modifica exclusivamente los placeholders inglés y español de Section 6.3. Preserva Sections 1–6.2, Discussion §6.4–§6.6, Conclusion y end matter.

### Entregables

1. `article/sections/discussion/Discussion_B03_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx`
4. `article/responses/7_DISCUSSION_B03_SECTION6_3_RESPONSE_V01.md`

La response debe declarar SHA-256, Git blob esperado del Markdown acumulativo, auditoría diferencial, equivalencia EN/ES, comentarios/citas, integridad OOXML, render completo y cumplimiento de D-035.

Detente al completar §6.3. No avances a §6.4 ni a Conclusion.

```text
EXPECTED_EXIT = DISCUSSION_B03_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Discussion Section 6.3 against canonical V025 and the approved B02 Word baseline. Compare the study with Lee et al. (2021), Lee et al. (2023), Marra de Artiñano et al. (2023), and Kim et al. (2025) by component authority and sequencing, not by numerical performance. Make explicit that candidate prediction followed by evidence retrieval is prior art and that the study's bounded distinction is the explicit fixed-Top-3 authority contract plus separate evaluation of ranking, documentary association, and controlled explanation. Exactly four new English citation comments are authorized, taking the cumulative Word comment count from 44 to 48. No novelty, first-ever, state-of-the-art, cross-study numerical superiority, causal safety, legal-correctness, external-generalization, §6.4+, or Conclusion claim is authorized.