# Prompt — Discussion B01 / Section 6.1 Separating candidate ranking from documentary evidence

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no recalcules resultados, no declares novelty y no avances fuera del bloque autorizado.

### Bloque autorizado

```text
BLOCK = DISCUSSION_B01_SECTION_6_1
SECTION = 6.1 SEPARATING CANDIDATE RANKING FROM DOCUMENTARY EVIDENCE
EXECUTION_SCOPE = DISCUSSION_B01_V01_ONLY
CANONICAL_BASELINE_MD = article/manuscript/ARTICLE_MASTER_V023.md
CANONICAL_BASELINE_MD_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
CANONICAL_BASELINE_MD_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
BASELINE_DOCX_SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
BASELINE_COMMENTS = 40
BASELINE_TRACKED_CHANGES = 0
BOUNDARY = article/governance/D121_DISCUSSION_B01_SECTION6_1_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md
```

### Lecturas obligatorias

1. `article/START_HERE.md` y todo onboarding obligatorio.
2. `article/governance/D120_RESULTS_B07_AUTHOR_APPROVAL_V023_VERIFICATION_AND_RESULTS_CLOSURE.md`.
3. `article/governance/D121_DISCUSSION_B01_SECTION6_1_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md`.
4. `article/CLAIM_EVIDENCE_MATRIX.md` y límites C04/C05/C12/C13/C18/C28.
5. `article/manuscript/ARTICLE_MASTER_V023.md`, especialmente Sections 2.1, 2.2, 2.6, 3.3–3.5, 5.2, 5.3, 5.6 y 5.7.
6. Los soportes bibliográficos ya verificados para Lee et al. (2021), `Classification of Goods Using Text Descriptions With Sentences Retrieval`, y Lee et al. (2023), `Explainable Product Classification for Customs`, usando la misma identidad bibliográfica ya presente en el manuscrito y en sus comentarios de cita.

No introduzcas literatura nueva en este bloque.

### Objetivo de Discussion §6.1

Interpretar qué aporta metodológicamente separar la formación del ranking de candidatos de la asociación documental y situar esa separación frente a antecedentes cercanos, sin repetir Results ni convertir una diferencia de diseño en una declaración de novelty.

Debe quedar claro que:

- en el presente estudio, historical retrieval determina el ranking y fija el Top-3 antes de la asociación documental;
- en el piloto, la etapa documental tuvo asociación exacta para los 3,168 candidate slots y preservó membership/order del Top-3 en 1,056/1,056 casos;
- esta invariancia permite atribuir candidate-retrieval performance al componente histórico y documentary coverage/traceability a la etapa documental como objetos evaluativos distintos;
- Lee et al. (2021) utilizan oraciones recuperadas del HS manual junto con la descripción para la posterior predicción del subheading, por lo que la evidencia recuperada participa en una decisión de clasificación posterior;
- Lee et al. (2023) son un antecedente más cercano: primero predicen candidatos y luego recuperan evidencia para cada candidato;
- la distinción permitida del presente estudio es el contrato explícito de Top-3 fijo y la prohibición downstream de insertar, eliminar, sustituir o reordenar candidatos, junto con evaluación separada de ranking y asociación documental;
- esa distinción es metodológica/operativa, no una claim de novelty o superioridad global.

### Interpretación permitida

Puedes explicar que una frontera de autoridad explícita mejora la atribución experimental: si documentary retrieval no puede cambiar el ranking, entonces un cambio o valor observado en Top-k/MRR pertenece al componente de candidate retrieval, mientras que coverage/association/traceability pertenece al componente documental. Esto es una interpretación de diseño y evaluación; no afirmar que la separación cause un mejor desempeño.

Puedes señalar que esta separación también hace visible una limitación: asociación documental completa e invariancia del ranking no establecen que el documento seleccionado sea jurídicamente suficiente, que el candidato sea normativamente correcto ni que la recomendación final sea legalmente válida.

### Comparación bibliográfica obligatoria

Cita exactamente una vez en el texto inglés a cada uno de estos trabajos:

1. Lee et al. (2021): el flujo predice heading → recupera oraciones del HS manual → usa descripción + oraciones para predecir subheading.
2. Lee et al. (2023): el flujo predice clasificación/candidatos → recupera evidencia del HS manual para cada candidato.

No comparar porcentajes de accuracy entre esos trabajos y este estudio. Las tareas, datasets, niveles HS, espacios de clases y protocolos difieren.

### Política de comentarios de cita Word

MWDP permanece vinculante. El baseline tiene 40 comentarios. Añade exactamente **dos** nuevos comentarios de cita en la Parte I inglesa, uno anclado a la nueva cita de Lee et al. (2021) y uno a la nueva cita de Lee et al. (2023), reutilizando la identidad bibliográfica y el tipo de soporte ya verificados en los comentarios heredados correspondientes. No elimines ni modifiques los 40 comentarios existentes.

Resultado esperado:

```text
COMMENTS = 42
TRACKED_CHANGES = 0
```

No añadir comentarios de cita nuevos en el espejo español.

### Forma recomendada

Mantén §6.1 compacta, aproximadamente 4–5 párrafos en inglés y un espejo semántico natural en español:

1. interpretación del significado del Top-3 fijo y de la invariancia documental;
2. contraste funcional con Lee et al. (2021);
3. contraste funcional con Lee et al. (2023) y delimitación de la diferencia del presente estudio;
4. implicación evaluativa/atribucional;
5. límite jurídico/normativo, si requiere un párrafo separado.

No reproduzcas una lista de métricas de §5.2–§5.3. Usa solo cifras indispensables para anclar la interpretación.

### Límites obligatorios

No introducir:

- nuevos resultados o cifras;
- nueva inferencia, CI, p-values o tests;
- causalidad;
- cross-dataset numerical superiority;
- `overall classification accuracy` para el presente pipeline;
- superioridad del framework completo;
- substantive normative correctness;
- legal correctness;
- claim de que evidencia identificable implica pertinencia/suficiencia jurídica;
- novelty, `first`, `first-ever`, SOTA o `FINAL_GAP`;
- §6.2–§6.6;
- Conclusion;
- front matter o end matter.

No reabras ni corrijas Results congelados.

### Bilingüismo

Redacta primero la Parte I inglesa como publication-facing master y luego el espejo semántico español. Las dos versiones deben ser equivalentes en interpretación, comparaciones y límites. El español debe ser natural, no un calco híbrido.

### Integridad acumulativa

Modificar exclusivamente los placeholders de §6.1 en inglés y español.

Preservar sin cambios:

- front matter actual;
- Sections 1–5.7;
- §6.2–§6.6;
- Section 7;
- end matter;
- los 40 comentarios Word heredados;
- estilos, relaciones, tablas y estructura OOXML heredada;
- 0 tracked changes.

No reconstruir DOCX desde Markdown. Editar nativamente el Word acumulativo B07 V01. D-035 permanece vinculante: no Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes.

### Entregables

Generar:

```text
article/sections/discussion/Discussion_B01_V01.md
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.md
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx
article/responses/7_DISCUSSION_B01_SECTION6_1_RESPONSE_V01.md
```

Versionar en GitHub únicamente la sección y la response pequeñas. Entregar ambos masters acumulativos como archivos reales al autor.

La response debe registrar SHA-256 de ambos candidatos, Git blob esperado del Markdown, identidad exacta de baselines, scope diff, equivalencia EN/ES y MD↔DOCX, dos nuevas citas con cobertura de comentario, total de 42 comentarios, 0 tracked changes, integridad OOXML, render completo y cumplimiento D-035.

Al terminar:

```text
DISCUSSION_B01_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Detente ahí.

---

## English

Execute only Discussion B01 / Section 6.1 from canonical V023 and the approved B07 cumulative Word baseline. Interpret the methodological separation between historical candidate ranking and downstream documentary association, compare it functionally with Lee et al. (2021) and Lee et al. (2023), and explain the resulting attribution/evaluation boundary without claiming novelty, causal performance gains, cross-dataset superiority, overall-system accuracy, normative correctness, or legal correctness. Cite each of the two literature anchors exactly once in the English text and add exactly two new Word citation comments while preserving the inherited 40 comments. Modify only Section 6.1 in English and Spanish, preserve all frozen Results and downstream placeholders, and stop before Section 6.2.