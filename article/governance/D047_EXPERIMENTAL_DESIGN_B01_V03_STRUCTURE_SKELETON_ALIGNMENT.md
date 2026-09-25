# D-047 — Experimental Design B01 V03 Structure-V02 skeleton alignment

## Español

```text
DECISION_ID = D-047
DATE = 2026-09-24
STATUS = ACTIVE / BINDING
PARENT_DECISIONS = D-045 / D-046
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_V02_INTERNAL_REVIEW_V01.md@02cc51121311463ea58dd28061a091b13cb743ab
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
GOVERNING_STRUCTURE_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
CANONICAL_MASTER = ARTICLE_MASTER_V009
B01_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03
B01_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
B01_CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
SECTION_3_FORWARD_REFERENCE_AMENDMENTS = VERIFIED / PASS
CUMULATIVE_MASTER_STRUCTURE = CORRECTION_REQUIRED
EXPERIMENTAL_DESIGN_B01 = ACTIVE / TECHNICAL_EDITORIAL_CORRECTION_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

La auditoría independiente de la entrega V03 confirma que la nueva prosa de 4.1–4.2.3 y las dos enmiendas editoriales de Section 3 superan el control científico, factual y editorial. El problema pendiente es exclusivamente estructural en el master acumulativo.

D-046 hizo gobernante Structure V02 y, simultáneamente, prohibió modificar 4.3 y posteriores. Dado que `ARTICLE_MASTER_V009` todavía contenía el esqueleto de Structure V01, esa combinación de instrucciones obligó a preservar encabezados ya superados. Esta contradicción de alcance se atribuye a la gobernanza de la IA Gestora, no a incumplimiento de la IA de Redacción.

### Excepción estrecha a D-046

D-047 sustituye únicamente la prohibición de modificar 4.3+ en la medida necesaria para **alinear mecánicamente el esqueleto aún no redactado** con la Structure V02 ya aprobada. No autoriza redactar contenido científico nuevo en 4.3–4.8.

La corrección permitida es exactamente:

1. conservar sin reescritura científica las dos enmiendas ya verificadas de 3.5/3.7 y toda la prosa B01 de 4.1–4.2.3;
2. sustituir en Part I y Part II el esqueleto V01 no redactado desde 4.3 hasta el final de Section 4 por el esqueleto V02 aprobado:
   - 4.3 Documentary corpus and evidence resource / Corpus documental y recurso de evidencia;
   - 4.4 Partition validity and dependence controls / Validez de particiones y control de dependencia;
   - 4.5 Experimental system configuration and execution / Configuración y ejecución experimental;
   - 4.6 Evaluation framework and protocols / Marco y protocolos de evaluación;
     - 4.6.1 Candidate-retrieval evaluation / Evaluación de recuperación de candidatos;
     - 4.6.2 Documentary-evidence evaluation / Evaluación de evidencia documental;
     - 4.6.3 Controlled-explanation evaluation / Evaluación de explicación controlada;
   - 4.7 Statistical and robustness analysis / Análisis estadístico y de robustez;
   - 4.8 Reproducibility resources / Recursos de reproducibilidad;
3. conservar solo notas de función/placeholder coherentes con `KBS_ARTICLE_WORKING_STRUCTURE_V02.md`; no completar la prosa científica de esas secciones;
4. eliminar el placeholder residual español situado entre `4. Diseño experimental` y `4.1. Entorno y alcance experimental`;
5. no modificar Results, Discussion, Conclusion ni otra prosa cerrada;
6. preservar los 40 comentarios heredados y mantener cero tracked changes.

### Gate

La aprobación autoral de B01 no se abre hasta que la IA Gestora verifique diferencialmente que la corrección modificó únicamente el esqueleto permitido y eliminó el placeholder residual, sin alterar la prosa científica ya auditada.

`ARTICLE_MASTER_V010` permanece suspendido/no materializado. El master canónico continúa siendo `ARTICLE_MASTER_V009`.

## English

D-047 authorizes only a narrow technical/editorial alignment of the still-unwritten Section-4 skeleton with the already author-approved Structure V02. The rewritten B01 scientific prose and the two Section-3 forward-reference amendments have independently passed and must not be scientifically rewritten.

The old V01 headings retained from Section 4.3 onward may be mechanically replaced by the approved V02 4.3–4.8 skeleton, including 4.6.1–4.6.3. No scientific drafting of those later subsections is authorized. The stale Spanish placeholder between the Section-4 heading and 4.1 must also be removed.

This decision resolves a scope contradiction introduced by D-046: Structure V02 was governing while modifications to the legacy 4.3+ skeleton were prohibited. D-047 supersedes that prohibition only for structural alignment. The canonical master remains V009 until a corrected candidate passes differential audit and the subsequent author/integration gates.