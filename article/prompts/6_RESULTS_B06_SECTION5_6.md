# Prompt — Results B06 / Section 5.6 Inferential results

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no recalcules resultados y no avances fuera del bloque autorizado.

### Bloque autorizado

```text
BLOCK = RESULTS_B06_SECTION_5_6
SECTION = 5.6 INFERENTIAL RESULTS
EXECUTION_SCOPE = B06_V01_ONLY
CANONICAL_BASELINE_MD = article/manuscript/ARTICLE_MASTER_V021.md
CANONICAL_BASELINE_MD_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
CANONICAL_BASELINE_MD_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
BASELINE_DOCX_SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
GROUND_TRUTH = article/governance/D113_RESULTS_B06_GROUND_TRUTH_SYNC_AND_SECTION5_6_BOUNDARY.md
SOURCE_SNAPSHOT = main@db0d0ad0d8435921a7838db6720eaea86a263763
```

### Lecturas obligatorias antes de redactar

1. `article/START_HERE.md` y todo onboarding obligatorio.
2. `article/governance/D113_RESULTS_B06_GROUND_TRUTH_SYNC_AND_SECTION5_6_BOUNDARY.md`.
3. `article/CLAIM_EVIDENCE_MATRIX.md`, especialmente C28 y C29.
4. `article/manuscript/ARTICLE_MASTER_V021.md`.
5. Fuentes congeladas indicadas por D-113:
   - `outputs/analysis/group3/g3_inferential_results_v0.1.csv`
   - `docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md`
   - `outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json`

Reconsulta las fuentes en el snapshot vinculante. No uses valores de memoria si difieren de las fuentes congeladas.

### Objetivo científico de §5.6

Redactar los resultados inferenciales cerrados que complementan §5.2 y §5.5 sin repetir Methods ni convertir el bloque en Discussion.

Debe quedar inequívoco que:

- HE2_A compara contribuciones pareadas `historical - comparator` para candidate retrieval;
- las tres familias comparadoras son flat normative BM25, hierarchical normative BM25 y corrected D1a;
- las cinco métricas primarias por familia son Top-1, Top-3, Top-5, Top-10 y MRR@100;
- los 15 intervalos primarios son 99% marginal percentile CIs bajo el control Bonferroni familywise-95% congelado;
- todos sus límites inferiores son > 0;
- HE2_B es un objeto distinto: `Recall@200 - Recall@100` para la familia jerárquica corregida, con 95% CI;
- HE2 queda `SUPPORTED` solo dentro del alcance inferencial congelado;
- HE5 permanece `INCONCLUSIVE` y no recibe un nuevo test inferencial.

### Valores congelados obligatorios

#### Historical minus flat normative BM25

```text
Top-1  = 0.482007576 ; 99% CI [0.329446843, 0.631331820]
Top-3  = 0.620265152 ; 99% CI [0.489773908, 0.757505941]
Top-5  = 0.701704545 ; 99% CI [0.582607584, 0.817963384]
Top-10 = 0.825757576 ; 99% CI [0.737159943, 0.896051128]
MRR@100 = 0.587410432 ; 99% CI [0.463626313, 0.712041394]
```

#### Historical minus hierarchical normative BM25

```text
Top-1  = 0.482954545 ; 99% CI [0.330419446, 0.630822238]
Top-3  = 0.619318182 ; 99% CI [0.485491905, 0.757028357]
Top-5  = 0.700757576 ; 99% CI [0.582403679, 0.817063388]
Top-10 = 0.825757576 ; 99% CI [0.736613432, 0.894902163]
MRR@100 = 0.587735966 ; 99% CI [0.465199608, 0.712038535]
```

#### Historical minus corrected D1a

```text
Top-1  = 0.508522727 ; 99% CI [0.364702301, 0.653466144]
Top-3  = 0.660984848 ; 99% CI [0.541305493, 0.781609818]
Top-5  = 0.712121212 ; 99% CI [0.590534359, 0.832721912]
Top-10 = 0.713068182 ; 99% CI [0.549548133, 0.860733443]
MRR@100 = 0.591620610 ; 99% CI [0.487310779, 0.706089907]
```

#### HE2_B

```text
Recall@200 - Recall@100 = 0.202651515
95% CI [0.066763106, 0.341601308]
```

Top-50 es suplementario y no tiene rol de decisión. Puede omitirse si la sección queda más clara sin él. Si se incluye, usar únicamente:

```text
historical - flat = 0.921401515 ; 95% CI [0.878378085, 0.958395581]
historical - hierarchical = 0.900568182 ; 95% CI [0.837868450, 0.946578631]
historical - D1a = 0.678030303 ; 95% CI [0.541341338, 0.825779729]
```

### Forma recomendada

Mantén §5.6 compacta. Una estructura aceptable es:

1. frase de apertura recordando que se usó el bootstrap DAM ya definido en §4.7;
2. un párrafo para HE2_A que resuma las tres familias y presente los valores con suficiente detalle para reproducibilidad;
3. un párrafo separado para HE2_B;
4. un cierre con la disposición HE2 y los límites; HE5 puede mencionarse en una frase final como `INCONCLUSIVE`, sin reanalizar §5.5.

Puedes usar una tabla compacta dentro de §5.6 si mejora sustancialmente la legibilidad y si el Word conserva correctamente su estilo. No es obligatorio.

### Límites obligatorios

No introducir:

- p-values;
- lenguaje de “statistically significant” desligado del criterio de intervalos congelado; preferir describir que los intervalos permanecen completamente por encima de cero;
- nuevas pruebas, intervalos o recomputaciones;
- estandarización post hoc;
- causalidad;
- generalización externa;
- superpoblación de DAM, SERIE o seeds;
- `overall classification accuracy` para estos resultados;
- superioridad del framework completo;
- corrección normativa o jurídica;
- inferencia derivada de Phase E;
- cambio de HE5 a supported/rejected;
- contenido de §5.7, Discussion o Conclusion;
- `FINAL_GAP` o `NOVELTY`.

### Bilingüismo

Redacta primero la Parte I inglesa como publication-facing master y luego el espejo semántico español. Ambos deben ser numérica y semánticamente equivalentes. El español debe ser natural y no un calco híbrido innecesario.

### Integridad acumulativa

Modificar exclusivamente los placeholders de §5.6 en inglés y español.

Preservar sin cambios:

- Sections 1–5.5;
- §5.7;
- Discussion;
- Conclusion;
- end matter;
- los 40 comentarios Word existentes;
- estilos, relaciones, tablas y demás estructura OOXML heredada;
- 0 tracked changes.

No reconstruir el DOCX desde Markdown. Editar el Word acumulativo heredado.

D-035 permanece vinculante: prohibidos Base64 manual, chunking, fragmentación, reensamblado y workarounds equivalentes.

### Entregables

Generar:

```text
article/sections/results/Results_B06_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md
```

Versionar en GitHub únicamente la sección y la response pequeñas. Entregar los dos masters acumulativos como archivos reales al autor.

La response debe registrar SHA-256 de ambos candidatos, Git blob esperado del Markdown, identidad del baseline, controles de scope, equivalencia EN/ES, equivalencia MD↔DOCX, 40 comentarios, 0 tracked changes, integridad OOXML, render completo y cumplimiento D-035.

Al terminar:

```text
RESULTS_B06_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Detente ahí.

---

## English

Execute only Results B06 / Section 5.6 from canonical V021 and the approved B05 cumulative DOCX. Draft the frozen inferential results for HE2_A and HE2_B, preserving the exact interval values and interpretation boundaries defined above and in D-113. HE2 may be reported as `SUPPORTED` only within the frozen internal inferential scope. HE5 remains `INCONCLUSIVE` and receives no new inferential test. Do not calculate p-values, new intervals, new tests, standardized effects, external-population inference, causality, overall-system accuracy, or legal correctness. Modify only the English and Spanish Section 5.6 placeholders, preserve the cumulative Word natively, and stop before Section 5.7.