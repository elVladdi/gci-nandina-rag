# CODEX — DIAGNÓSTICO READ-ONLY DEL FALLO DE REPRODUCCIÓN EV03 EN 0B-05C

## 0. ROL

Actúa exclusivamente como **DIAGNOSTICADOR FORENSE READ-ONLY**.

El Intento 02 de la ejecución numérica 0B-05C terminó correctamente en modo fail-closed durante `02_EV03_control_reproduction` con:

`ContractViolation: Mandatory control reproduction is not exact`

No estás autorizado a corregir, limpiar, reintentar, resumir, sobrescribir ni continuar la ejecución científica.

Este diagnóstico debe explicar **por qué el control Decision885 EV03 reconstruido no reproduce exactamente el control congelado** y qué evidencia falta para decidir una remediación prospectiva.

---

## 1. ESTADO QUE DEBE PRESERVARSE

Repositorio esperado:

`C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA`

Rama local:

`codex/0b05c-corrective-numerical-execution-v01`

HEAD, main y origin/main deben seguir exactamente en:

`06cc75ec173eb6c4b134a45eeb88fe25999f396e`

Tree esperado:

`c84da63249619e94ae69fb2a6f080dd3f84cbcf4`

No crear commit. No push. No modificar ramas.

No modificar ni eliminar los seis artefactos generados por el Intento 02. Son evidencia de fallo y deben preservarse exactamente como están.

No tocar `main`, Plan Maestro, `article/main-manuscript`, EXP11B, EXP12, ACL, Defender/CFA ni OneDrive.

---

## 2. PROHIBICIONES ABSOLUTAS

No ejecutar:

`python -m src.experiments.run_0b05c_corrective_numerical_v01 --execute-authorized`

ni ningún runner de EV03, EV04 o D1a que genere outputs.

No ejecutar corrected arm.

No calcular métricas correctivas.

No crear índices o corpus nuevos en disco.

No eliminar ni mover:

- `data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1/`
- `outputs/evaluation/0b05c_corrective_numerical_v0.1/`
- `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/`

No modificar código, configs, specs, tests, manifests ni artefactos congelados.

No hacer `git clean`, `git reset --hard`, `git checkout --`, `git restore`, `rm`, `Remove-Item` ni equivalentes sobre evidencia del Intento 02.

---

## 3. HECHOS DEL INTENTO 02 A VERIFICAR READ-ONLY

Verifica mecánicamente, sin asumir el reporte previo:

### Control congelado EV03

- corpus: `data/processed/corpus_rag_v1_index.jsonl`
- corpus SHA-256 esperado: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`
- eval SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`
- índice congelado: `data/processed/indexes/bm25_nandina8.pkl`
- índice SHA-256 esperado: `fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b`
- metadata histórica: `data/processed/indexes/bm25_nandina8_run_metadata.json`
- ranking congelado: `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`
- case summary congelado: `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv`

### Reproducción fallida del Intento 02

- índice generado: `data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1/index.pkl`
- metadata generada: `data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1/index_metadata.json`
- ranking observado: `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_results.csv`
- case summary observado: `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_case_summary.csv`
- metrics observado: `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_metrics.json`

Confirma sus tamaños y SHA-256 antes de cualquier análisis.

---

## 4. PREGUNTA FORENSE CENTRAL

Determina si la divergencia proviene de uno o más de estos niveles:

1. **corpus bytes / row order / corpus filtering**;
2. **document text construction** (`titulo`, `texto_index`, fallback `texto`, concatenación u otra regla);
3. **tokenización / normalización / stopwords**;
4. **BM25 index construction** (doc_ids, doc order, doc_lens, avgdl, vocabulary, IDF, inverted postings);
5. **retrieval / query processing / tie-breaking / top_n**;
6. **environment/runtime numerical behavior**;
7. **historical provenance gap**: el índice original fue creado con una implementación/notebook distinto o no versionado y el gate actual asumió indebidamente equivalencia;
8. otra causa demostrable.

No selecciones una causa por intuición. Demuéstrala con comparaciones mecánicas.

---

## 5. AUDITORÍA DEL ÍNDICE CONGELADO VS ÍNDICE RECONSTRUIDO

Carga ambos `.pkl` **solo en memoria y read-only** usando las clases versionadas actuales. No serialices nada.

Para ambos informa:

- SHA-256 del archivo;
- tamaño;
- `k1`, `b`;
- número de `doc_ids`;
- SHA-256 canónico de la secuencia ordenada de `doc_ids`;
- si los `doc_ids` son idénticos y en el mismo orden;
- número de `doc_texts`;
- SHA-256 canónico de la secuencia ordenada de `doc_texts`;
- primer `doc_idx` donde `doc_texts` difieren, si existe;
- `doc_lens` count/min/max/mean y SHA-256 de su representación binaria/canónica;
- `avgdl`;
- tamaño del vocabulario (`idf`);
- SHA-256 canónico del mapping `idf` ordenado por término;
- número total de postings;
- SHA-256 canónico del inverted index ordenado por término;
- primera diferencia concreta en términos/postings/IDF.

Distingue diferencias de serialización pickle de diferencias semánticas del índice.

---

## 6. CONTRASTE CON METADATA HISTÓRICA

Lee íntegramente:

`data/processed/indexes/bm25_nandina8_run_metadata.json`

Registra literalmente los campos relevantes de procedencia:

- `notebook_name` / script;
- timestamp;
- Python;
- corpus hash;
- schema de campos;
- filtros;
- `k1`, `b`, stopwords y cantidad;
- docs before/after/indexed;
- avg doc length;
- vocabulary size.

Compara esos valores con la metadata del índice reconstruido del Intento 02.

Determina si la metadata histórica afirma ejecución mediante un notebook u otra implementación que **no coincide con la identidad de código congelada por el gate actual**.

Investiga read-only el historial Git (`git log`, `git show`, `git rev-list`, `git grep`) para establecer:

- cuándo apareció por primera vez el índice congelado y su metadata;
- si `04_BM25_Indexacion_NANDINA.ipynb` o el código exacto que construyó el índice original está versionado en algún commit alcanzable;
- si `src/bm25_index.py` y `src/experiments/build_bm25_index.py` existían con exactamente la misma implementación en la fecha/commit de creación del índice;
- si el gate `ev03_corrective_execution_spec_v0.1.json` congela realmente la **identidad del builder original** o solo corpus/config/eval/evaluator/índice.

No cambies el estado del repositorio durante esta investigación.

---

## 7. RECONSTRUCCIÓN DIAGNÓSTICA SOLO EN MEMORIA

Se permite crear objetos Python **solo en RAM** para probar hipótesis de construcción, siempre que no se escriba ningún archivo.

Como mínimo prueba, cuando sea técnicamente posible:

- builder actual con stopwords congeladas;
- sin stopwords;
- `titulo + texto_index`;
- solo `texto_index`;
- `titulo + texto`;
- otras variantes directamente sugeridas por la metadata o por el contenido interno del índice congelado.

Para cada variante compara contra el índice congelado al menos:

- doc_ids/order;
- doc_texts cuando aplique;
- doc_lens/avgdl;
- vocab size;
- IDF hash/postings hash.

No ejecutes el evalset completo para estas variantes y no produzcas métricas científicas. El objetivo es identificar semántica del índice, no observar resultados.

Si una variante reproduce exactamente la estructura lógica del índice congelado, indícalo y demuestra qué campos coinciden.

---

## 8. CASO TESTIGO `DA-EVAL-V02-00001`

Usa el primer caso divergente reportado únicamente como diagnóstico.

Con el **índice congelado** y el **índice reconstruido ya existente**:

- registra la query exacta;
- top-10 con código, score y rank para ambos;
- número total de hits no-cero antes del truncamiento Top-100;
- términos normalizados de la query;
- términos de la query presentes/ausentes en cada vocabulario;
- contribuciones BM25 por término para el Top-1 congelado (`39173210`) y el Top-1 reconstruido (`29314600`), si puede calcularse read-only;
- identifica el primer punto matemático en el que divergen.

No uses el caso para ajustar ninguna regla.

---

## 9. CLASIFICACIÓN OBLIGATORIA DEL HALLAZGO

Emite exactamente uno de estos estados, respaldado por evidencia:

- `EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH`
- `EV03_REPRODUCTION_ROOT_CAUSE = HISTORICAL_BUILDER_PROVENANCE_GAP`
- `EV03_REPRODUCTION_ROOT_CAUSE = ENVIRONMENT_NUMERICAL_DRIFT`
- `EV03_REPRODUCTION_ROOT_CAUSE = CORPUS_OR_INPUT_IDENTITY_DRIFT`
- `EV03_REPRODUCTION_ROOT_CAUSE = MULTIFACTOR_CONFIRMED`
- `EV03_REPRODUCTION_ROOT_CAUSE = NOT_DETERMINED`

Además responde separadamente:

- `ORIGINAL_EV03_INDEX_LOGICALLY_REPRODUCIBLE_FROM_VERSIONED_SOURCE = true/false/not_determined`
- `ORIGINAL_EV03_INDEX_ARTIFACT_ITSELF_VERSIONED_AND_HASH_VERIFIABLE = true/false`
- `CURRENT_0B05C_EV03_CONTROL_REPRODUCTION_CONTRACT_VALID = true/false/not_determined`
- `CORRECTIVE_EV03_EXECUTION_CAN_PROCEED_UNCHANGED = false`

El último campo debe permanecer `false`: el Intento 02 ya cerró el gate por reproducción no exacta.

---

## 10. REMEDIACIONES POSIBLES — SOLO PROPONER

No implementes ninguna.

Para cada alternativa técnicamente viable describe:

- qué problema resuelve;
- qué archivos/contratos necesitaría cambiar;
- si preserva el control histórico original;
- si cambia la semántica científica preregistrada;
- riesgo de sesgo post hoc;
- cómo exigir una nueva reproducción exacta antes del corrected arm;
- si requiere una nueva autorización prospectiva.

Considera al menos estas familias, sin asumir que sean válidas:

A. recuperar/reconstruir exactamente la implementación histórica original;
B. derivar semántica verificable desde el índice congelado y formalizar un builder que reproduzca exactamente ese índice antes de aplicar la corrección;
C. usar un control reconstruido bajo una semántica nueva emparejada con su corrected arm, manteniendo el control histórico solo como referencia — esto constituye cambio metodológico y requeriría justificación/autoridad nueva;
D. declarar EV03 no reejecutable exactamente y limitar el alcance de 0B-05C si no existe solución reproducible.

No recomiendes limpiar los artefactos del Intento 02 todavía.

---

## 11. CONFIRMACIÓN DE NO INTERVENCIÓN

Al final confirma:

- runner invocations = 0;
- files created = 0;
- files modified = 0;
- files deleted = 0;
- directories created = 0;
- commits = 0;
- pushes = 0;
- Attempt 02 evidence preserved = true;
- main/origin-main unchanged = true;
- scientific state unchanged = true.

---

## 12. REPORTE FINAL OBLIGATORIO

Entrega en español y con estas secciones:

A. Git y preservación de evidencia
B. Identidades/hashes de control congelado y reproducción
C. Comparación estructural de los dos índices
D. Metadata histórica vs reconstruida
E. Historial/procedencia del builder original
F. Hipótesis de construcción probadas en memoria
G. Caso testigo DA-EVAL-V02-00001
H. Causa raíz clasificada
I. Implicación para el gate 0B-05C
J. Remediaciones posibles no ejecutadas
K. Confirmación de no intervención

No declares `0B05C_METRIC_IMPACT`, no determines `DOWNSTREAM_REEXECUTION` y no cierres 0B-05C.