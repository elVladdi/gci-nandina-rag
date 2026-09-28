# D-113 — Results B06 ground-truth synchronization and Section 5.6 boundary

## Español

```text
DECISION = D-113
PHASE = RESULTS
BLOCK = RESULTS_B06_SECTION_5_6
SECTION = 5.6 INFERENTIAL RESULTS
CANONICAL_MASTER = ARTICLE_MASTER_V021
GROUND_TRUTH = SYNCHRONIZED
SOURCE_SNAPSHOT = main@db0d0ad0d8435921a7838db6720eaea86a263763
PRIMARY_SCOPE = HE2_A + HE2_B
HE5_ROLE = DISPOSITION_ONLY / NO_NEW_INFERENTIAL_TEST
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

### 1. Fuentes vinculantes

Se reconsultaron los artefactos inferenciales congelados y la matriz claim–evidencia vigente.

```text
outputs/analysis/group3/g3_inferential_results_v0.1.csv
GIT_BLOB = cf3d8d85e099a300330da0214836e70af7a02253

docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
GIT_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436

outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
GIT_BLOB = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

article/CLAIM_EVIDENCE_MATRIX.md
C28 = HE2 SUPPORTED / AUTHORIZED
C29 = HE5 INCONCLUSIVE / AUTHORIZED
```

La disposición final elegible para manuscrito se rige por C28/C29 de la matriz editorial vigente. El artefacto G3-F04 se usa como registro científico de la disposición y de sus componentes, no para reabrir estados históricos de auditoría ya cerrados posteriormente.

### 2. Diseño inferencial congelado

El análisis usa 1,056 SERIE de 67 DAM. SERIE es la unidad de análisis y DAM/declaración es el cluster de dependencia. Se empleó un bootstrap pareado por cluster DAM con 10,000 réplicas y seed 20263001. En cada réplica se preservó el estimando ponderado por SERIE mediante multiplicidad de las DAM remuestreadas.

HE2_A contiene tres familias comparativas independientes en su control de multiplicidad: historical-minus-flat, historical-minus-hierarchical y historical-minus-D1a. Cada familia tiene cinco métricas primarias: Top-1, Top-3, Top-5, Top-10 y MRR@100. Cada familia usa intervalos percentiles bilaterales marginales de 99%, implementando el control Bonferroni familywise 95% congelado. No se calcularon p-values.

Top-50 es suplementario, con intervalo bilateral de 95%, fuera de la familia primaria y sin rol en la disposición de HE2.

HE2_B contiene un único contraste primario: `Recall@200 - Recall@100` para recuperación normativa jerárquica corregida, con intervalo percentil bilateral de 95% y sin ajuste de multiplicidad.

### 3. HE2_A — resultados primarios

Todos los límites inferiores de los 15 intervalos primarios de HE2_A son mayores que cero.

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

La dirección del efecto es `historical - comparator`; valores positivos favorecen al ranking histórico en la métrica correspondiente. Estos contrastes evalúan candidate retrieval en el benchmark interno congelado, no accuracy global del framework ni corrección jurídica.

### 4. HE2_B — cobertura profunda jerárquica

```text
CONTRAST = Recall@200 - Recall@100
POINT_ESTIMATE = 0.202651515
95% CI = [0.066763106, 0.341601308]
DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
```

Este contraste mide incremento de cobertura exacta al profundizar de 100 a 200 posiciones dentro de la familia jerárquica corregida. No es un contraste de early ranking y no debe fusionarse con HE2_A.

### 5. Resultados suplementarios y Phase E

Top-50 es suplementario y no decisional:

```text
historical - flat Top-50 = 0.921401515 ; 95% CI [0.878378085, 0.958395581]
historical - hierarchical Top-50 = 0.900568182 ; 95% CI [0.837868450, 0.946578631]
historical - D1a Top-50 = 0.678030303 ; 95% CI [0.541341338, 0.825779729]
```

Las variantes Phase E son únicamente inventarios descriptivos de cobertura. La progresión Pool@50 < Pool@100 < Pool@200 es direccionalmente consistente en las variantes congeladas elegibles, pero no constituye evidencia inferencial adicional ni reemplaza HE2_B.

### 6. Disposición y límites

```text
HE2_A = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B_PRIMARY = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_OVERALL = SUPPORTED
HE5 = INCONCLUSIVE
```

La disposición HE2 está autorizada únicamente dentro del alcance inferencial congelado. Los intervalos cuantifican incertidumbre por remuestreo de clusters dentro del benchmark interno Chapter 87; no sustentan inferencia a una población externa, causalidad, superioridad universal, accuracy del sistema completo ni validez jurídica.

HE5 no recibe un nuevo test inferencial en §5.6. Su disposición `INCONCLUSIVE` procede de componentes no estimables y descriptivos ya reportados en §5.5; no debe convertirse en `SUPPORTED` o `REJECTED`.

### 7. Frontera editorial de B06

§5.6 puede redactar exclusivamente:

1. el diseño de inferencia de forma mínima para interpretar los resultados, remitiendo a §4.7 para el método completo;
2. los 15 contrastes primarios HE2_A con sus 99% CI y la conclusión de que todos los límites inferiores son positivos;
3. el contraste primario HE2_B con 95% CI;
4. Top-50 como suplementario, si mejora legibilidad, sin rol decisional;
5. una nota breve de consistencia descriptiva Phase E, si es necesaria;
6. `HE2 = SUPPORTED` dentro del alcance congelado;
7. `HE5 = INCONCLUSIVE` sin introducir un nuevo análisis inferencial.

Prohibido en B06:

- p-values o significancia basada en p-values;
- nuevos intervalos, tests, estandarizaciones o recomputaciones;
- inferencia externa/superpoblacional;
- causalidad;
- llamar a candidate retrieval `overall classification accuracy`;
- atribuir HE2 al framework completo, evidencia normativa o LLM;
- convertir HE5 en supported/rejected;
- avanzar a §5.7, Discussion o Conclusion.

`FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen intactos.

---

## English

Results B06 / Section 5.6 is bound to the frozen Group-3 inferential outputs and the current authorized claim matrix. HE2_A comprises three five-metric historical-minus-comparator families with paired DAM-cluster bootstrap 99% marginal percentile intervals under the frozen Bonferroni familywise-95% rule; every primary lower bound is above zero. HE2_B is the single hierarchical `Recall@200 - Recall@100` contrast with point estimate 0.202651515 and 95% CI [0.066763106, 0.341601308]. HE2 is `SUPPORTED` only within the frozen internal inferential scope. HE5 remains `INCONCLUSIVE` and receives no new inferential test. No p-values, new inference, external-population claims, causality, or overall-system-accuracy framing are authorized.