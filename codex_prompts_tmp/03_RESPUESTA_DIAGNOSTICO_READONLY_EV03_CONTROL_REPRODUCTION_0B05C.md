**A. Git y preservación de evidencia**

```makefile
branch = codex/0b05c-corrective-numerical-execution-v01
HEAD = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
tree = c84da63249619e94ae69fb2a6f080dd3f84cbcf4
main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
tracked_working_tree_clean = true
git_operations_in_progress = none
```

Los únicos untracked visibles siguen siendo:

```text
Referencias/Antecedentes/
Referencias/Glosario/
data/Series - Descripciones.xlsx
```

Los seis artefactos del Intento 02 permanecen presentes, ignorados por Git y con sus tamaños y SHA-256 intactos.

**B. Identidades/hashes de control congelado y reproducción**

```text
Artefacto                                              Bytes      SHA-256
corpus_rag_v1_index.jsonl                              3622401    83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
data_aduanas_evalset_clase87_v0.2.csv                  1363273    3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
bm25_nandina8.pkl                                      918503     fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b
bm25_nandina8_run_metadata.json                        1545       89d9e87e8c099ecf1ab7a4bca898ed5cdceef1bead21563527756dfe01a3dce0
normative_results.csv congelado                        13145709   d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
normative_case_summary.csv congelado                   497448     f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0

index.pkl reconstruido                                 924566     0db8772a513765aa2d4f214548c1d279a99789ac6fbacc6d72dc99937b43cf6c
index_metadata.json reconstruido                       1373       6b19a88b27af460ff2d83bf0adcb224617f4e5d1848eb1cb83fc81800ea6874f
normative_flat_results.csv observado                   20916984   181deea25633244b85898443deba54babc352c46dd3e23c16a478eb57bf35c29
normative_flat_case_summary.csv observado              501375     bcf60ce0a9e62c95a39140139c911148d1a8f5d8a40f261daca57daf8e704527
normative_flat_metrics.json observado                  5312       c2cb91059d2e860e4660bb779647a239a01871db2d39feb8d0928c8d766c2181
```

**C. Comparación estructural de los dos índices**

Los hashes canónicos se calcularon con JSON UTF-8 compacto y ordenado; los floats IDF se representaron mediante `float.hex()`. Para `doc_lens` se usaron `dtype`, shape y bytes contiguos.

```text
Campo                         Congelado                               Reconstruido
k1 / b                        1.5 / 0.75                              1.5 / 0.75
doc_ids                       7644                                    7644
doc_ids SHA-256               2cfff892b1c6f8d5193a0542a1ded4b551f9a2fdf8e68f2b6858030a3da2f4f1
doc_ids orden exacto          idéntico
doc_texts                     7644                                    7644
doc_texts SHA-256             43a0ecb872c3cca2834141643bf9e9db2a89ac85ea4ffc2341986f14edf938b1
doc_texts orden exacto        idéntico; no existe primera diferencia
doc_lens min/max/mean         2 / 24 / 5.793302059173584              2 / 36 / 6.037153244018555
doc_lens SHA-256              b25e18913d58145cb248c0a465bfe68afb0bc6e7d2f9286c03d1df52c7069ecd
                              1a5bb9ea4ea8ffc3c690fa461f2f96a758e02686ee0e1d77ad7c566ab683b376
vocabulario                   5646                                    5674
IDF SHA-256                   3625597ae8bad7133da7a3428e9fc48f2724c92222925f1973d34e7061910a8f
                              1bf3dba42e6ec9bb12862fb3f131627747289fc1d95b0f61f072c9a86d809e9c
postings totales              21541                                   22320
inverted-index SHA-256        10f8870d6326634a5bd8a73c473ee441986fb5698b88ea69195abd58ed511ee9
                              a9b51f90e4ba624aaa7e9f8a8339e47dd68f35b30f8c61f0d4f569c74878e8a0
```

El reconstruido añade exactamente 28 términos de un carácter:

```text
0 1 2 3 4 5 6 7 8 9 b c d e f g h i k l m n p s t v w x
```

No existe ningún término exclusivo del índice congelado. Para todos los términos compartidos, IDF y postings son iguales.

Primera diferencia léxica: término `0`, ausente en el congelado y presente en el reconstruido con IDF `5.102354805769852` y 46 postings.

Primera diferencia de longitud:

```makefile
doc_idx = 365
code = 04011000
frozen_doc_len = 12
rebuilt_doc_len = 14
extra_token = 1, presente dos veces
```

Por tanto, la divergencia es semántica y no una diferencia meramente causada por serialización `pickle`.

**D. Metadata histórica vs reconstruida**

```text
Campo                    Histórica                              Reconstruida
productor declarado      04_BM25_Indexacion_NANDINA.ipynb      build_bm25_corrective_0b05c_v01.py
timestamp histórico      1768674608 / 2026-01-17T18:30:08Z     no timestamp
Python                   3.11.7                                no registrado
corpus SHA-256           83768faa...                            83768faa...
schema                   tipo/codigo/titulo/texto_index         semántica del builder actual
fallback                 texto                                 texto
filtro                    tipo=nandina_8, 8 dígitos             equivalente
k1 / b                   1.5 / 0.75                            1.5 / 0.75
stopwords                true / 51                             true / DEFAULT_STOPWORDS_ES
docs before/indexed      7748 / 7644                           7748 / 7644
avg doc length           5.793302059173584                     6.037153244018555
vocabulario              5646                                  5674
```

La metadata histórica no registra el filtro de tokens de longitud uno ni una identidad Git del builder/tokenizador. La metadata reconstruida declara como semántica congelada `src/experiments/build_bm25_index.py`, cuya implementación actual conserva tokens de un carácter.

**E. Historial/procedencia del builder original**

```text
689f7436...  2026-05-19  primera aparición del bm25_index.cpython-311.pyc histórico
975bc987...  2026-05-20  primera aparición del índice y metadata congelados
d73ff147...  2026-06-12  primera aparición de bm25_index.py, build_bm25_index.py y notebook
df60c772...  2026-08-29  runner EXP-04 BM25 normativo plano v0.2
```

En el commit que incorporó el índice no existían el notebook ni el fuente `.py`; solo existía el bytecode `src/__pycache__/bm25_index.cpython-311.pyc`.

Ese bytecode tiene:

```makefile
SHA256 = 2c2082f44891dc5a16fd9b8aae7c6e69fd10faf86f6f1a798d31d916e7532c0a
source_path_embedded = ...\src\bm25_index.py
tokenize_es_documented_rule = Elimina tokens de longitud 1
```

El fuente incorporado posteriormente en `d73ff147...` no contiene esa regla y no ha cambiado desde entonces. Sus blobs siguen siendo:

```makefile
src/bm25_index.py = 718895e0658a55cc1590c84ef807f901b75e7c7f
src/experiments/build_bm25_index.py = 5ebad35484c2e42ca036adab41b827b69094e0bb
notebooks/04_BM25_Indexacion_NANDINA.ipynb = 7be77d7939663ffec9a56f24f224650b37f852b1
```

El contrato EV03 congela corpus, config, eval, evaluador e índice, pero no la identidad del builder histórico. El notebook versionado posteriormente llama al módulo actual y no reproduce el comportamiento del bytecode histórico.

**F. Hipótesis de construcción probadas en memoria**

```text
Variante                                  avgdl       vocab  Resultado lógico
builder actual + stopwords                6.037153    5674   NO
sin stopwords                             9.263737    5712   NO
titulo + texto_index                      6.037153    5674   NO
solo texto_index                          3.018577    5674   NO
titulo + texto                            11.037153   5716   NO
solo titulo                               3.018577    5674   NO
titulo + texto_index + eliminar len=1     5.793302    5646   EXACTO
```

La última variante igualó exactamente, en el runtime actual:

```makefile
doc_ids_and_order = true
doc_texts_and_order = true
doc_lens = true
avgdl = true
idf_mapping = true
inverted_index = true
postings = true
logical_index_exact = true
```

Esto descarta deriva del corpus, orden de filas, construcción del texto, stopwords, BM25, plataforma y aritmética numérica como causa primaria.

**G. Caso testigo DA-EVAL-V02-00001**

Query exacta:

```text
M1,NISSAN,MURANO VE:SL,2024 CA:SUV,C1:AZUL,CO:GASOLINA,SN:0 NC:6,CC:3500,CH/VIN:5N1AZ2CJ3RC101423,MO:VQ35754666W AS:5,FR:4X2,TT:AUT,PA:4,PM: 191.00@6000.00,PB:2318,PN:1770,CU:548 BSA,LET, ,KM:24597.00,TE:ENCENDIDO POR CHISPA LA:4850,AN:1850,AL:1720, NR:4,AR:55/20, 55
```

Términos presentes:

```text
Congelado:     00, 20, 55, azul, ca, chispa, encendido, gasolina, te
Reconstruido:  0, 00, 20, 4, 5, 6, 55, azul, ca, chispa, encendido, gasolina, te
```

Los demás términos normalizados de la query están ausentes en ambos vocabularios. Los términos que explican la nueva divergencia son `0`, `4`, `5` y `6`.

```text
Rank  Congelado                            Reconstruido
1     39173210  21.311974833146948         29314600  21.825923130489294
2     48059130  19.802109790880560         39173210  21.781551144981986
3     48059220  19.802109790880560         48059130  20.266054579287797
4     48059320  19.802109790880560         48059220  20.266054579287797
5     72022100  19.774251289715778         48059320  20.266054579287797
6     85122010  18.492026401478550         72022100  20.140192121392936
7     84213100  16.431811858585938         85122010  18.947727188774410
8     85113092  10.988949208231416         84213100  16.767221977809307
9     27101292  10.214432063009113         85232922  16.201274348948324
10    09023000   9.449305809941608         85232932  16.201274348948324
```

```makefile
frozen_nonzero_hits = 38
rebuilt_nonzero_hits = 206
```

Contribuciones BM25:

```text
Índice       Código      Término   qtf  tf  IDF                 Contribución
congelado    39173210    00        3    2   7.237059026124737   21.311974833146948
reconstruido 39173210    00        3    2   7.237059026124737   21.781551144981986
congelado    29314600    —         —    —   —                   0
reconstruido 29314600    6         1    6   5.4918195725315755  6.884634807947774
reconstruido 29314600    5         1    2   4.729679520484678   2.968896416362116
reconstruido 29314600    4         2    6   4.775141894561436   11.972391906179404
```

El primer punto matemático de divergencia ocurre durante la tokenización del índice: el builder actual incorpora tokens de longitud uno. Esto añade postings y modifica `doc_lens` y `avgdl`. El cambio de `avgdl` altera incluso el score de documentos que no contienen esos tokens. Tie-breaking y `top_n` no originan la divergencia.

**H. Causa raíz clasificada**

```makefile
EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH
ORIGINAL_EV03_INDEX_LOGICALLY_REPRODUCIBLE_FROM_VERSIONED_SOURCE = false
ORIGINAL_EV03_INDEX_ARTIFACT_ITSELF_VERSIONED_AND_HASH_VERIFIABLE = true
CURRENT_0B05C_EV03_CONTROL_REPRODUCTION_CONTRACT_VALID = false
CORRECTIVE_EV03_EXECUTION_CAN_PROCEED_UNCHANGED = false
```

La lógica es recuperable y fue reproducida exactamente a partir del artefacto congelado y del bytecode versionado, pero el fuente histórico exacto `.py`/notebook no estaba versionado cuando se creó el índice.

**I. Implicación para el gate 0B-05C**

El fail-closed fue correcto. El gate vinculó la reproducción al builder actual, pero ese builder no representa la semántica del índice histórico. EV03 no puede avanzar al brazo correctivo sin una revisión prospectiva del contrato, una nueva reproducción exacta y nueva auditoría/autorización.

**J. Remediaciones posibles no ejecutadas**

1. **Recuperar la implementación histórica original.** Incorporar y congelar el fuente auténtico que elimina tokens de longitud uno. Preserva el control histórico y no cambia su semántica. Requiere identidades de código, tests de equivalencia lógica, reproducción exacta previa y nueva autorización. Riesgo post hoc bajo si la procedencia se valida independientemente.

2. **Formalizar un builder derivado del índice congelado.** Crear un builder explícito cuya semántica documentada reproduzca exactamente `doc_ids`, textos, longitudes, IDF y postings. Preserva el control, pero requiere cambios en builder, spec, hashes, tests y gate. Riesgo post hoc medio por ingeniería inversa; debe exigir exact-match antes del corrected arm y nueva autorización.

3. **Adoptar una nueva semántica emparejada.** Usar el builder actual para un control nuevo y su corrected arm, dejando Decision885 histórico solo como referencia. Cambia la semántica preregistrada y tiene riesgo post hoc alto. Requiere protocolo, baseline y autorización nuevos, además de una reproducción determinista independiente antes del brazo correctivo.

4. **Declarar EV03 no reejecutable exactamente.** Limitar prospectivamente el alcance de 0B-05C sin ejecutar EV03 correctivo. Preserva intacto el control histórico, pero reduce el alcance científico. Requiere decisión externa y modificación formal del contrato; no requiere limpiar la evidencia existente.

**K. Confirmación de no intervención**

```makefile
runner_invocations = 0
files_created = 0
files_modified = 0
files_deleted = 0
directories_created = 0
commits = 0
pushes = 0
Attempt_02_evidence_preserved = true
main_origin_main_unchanged = true
scientific_state_unchanged = true
```
