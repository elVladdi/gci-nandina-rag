# PROMPT121D — Auditoría externa independiente

```text
PROMPT121D_EXTERNAL_AUDIT = REVISION_REQUIRED
PROMPT121D_BLOCK_D = REVISION_REQUIRED / NOT_APPROVED
NUMERICAL_CORRECTION_REQUIRED = false
RESULT_REPORTING_CORRECTION_REQUIRED = true
TARGETED_REVISION_REQUIRED = true
FULL_RERUN_REQUIRED = false
A036 = VERIFIED / KEEP
NEXT_BLOCK_121E_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Artefactos auditados

Se auditó independientemente la ejecución de `PROMPT121D` contra su contrato, el DOCX entregado, la trazabilidad acumulativa y las fuentes científicas primarias.

DOCX auditado:

```text
Molleapasa_gv_G7F02_REVIEW_V03_D.docx
SHA256 = cedc46234c81a94626524d21847b27e5f59bbffb94b8de9bff323498c8c3d575
SIZE_BYTES = 4194621
```

Trazabilidad oficial declarada:

```text
g7_thesis_claim_traceability_v0.3_D.csv
SHA256 = 924f6220e8114bce6f8465e8f2c403cc8e9ebe2a3506136dd4d0533820974828
SIZE_BYTES = 75082
TRACE_ROWS = 84
```

La copia de trazabilidad recibida para auditoría fue un XLSX. Se verificaron sus 84 filas de datos y 25 columnas. Las 75 filas heredadas coinciden exactamente con el CSV C aprobado y las nueve filas nuevas corresponden únicamente a `G7F02-V03D-001` a `G7F02-V03D-009`. Al serializar ese contenido con el mismo formato byte-semántico del CSV C —UTF-8 con BOM, separador coma, quoting mínimo y salto LF— se reconstruye exactamente el tamaño `75082` y el SHA-256 `924f6220e8114bce6f8465e8f2c403cc8e9ebe2a3506136dd4d0533820974828` declarados para el CSV oficial D.

## 2. Integridad acumulativa y alcance

La comparación independiente entre C y D confirmó:

```text
INHERITED_TRACE_ROWS = 75
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 9
NEW_TRACE_ID_RANGE = G7F02-V03D-001 .. G7F02-V03D-009
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
ZIP_ENTRY_SET_PRESERVED = true
DOCX_UNCOMPRESSED_PARTS_CHANGED = word/document.xml; word/comments.xml
```

En el cuerpo principal solo cambiaron dos objetos de nivel superior: la `Tabla 10` y el párrafo inmediato de 4.1.1 posterior a ella. No se identificaron modificaciones visibles en 4.1.2, Tabla 11, 4.1.3 ni en secciones anteriores al alcance autorizado.

```text
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
A036_VISIBLE_CHANGE = false
```

## 3. Comentarios y marcado de revisión

La auditoría OOXML confirmó:

```text
COMMENTS_BEFORE = 167
COMMENTS_AFTER = 176
NEW_COMMENT_IDS = 418..426
INHERITED_COMMENT_TEXT_CHANGED = 0
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
ALL_COMMENT_IDS_ANCHORED = true
ORPHAN_COMMENT_IDS = NONE
```

Los nueve comentarios nuevos contienen los seis encabezados obligatorios y se vinculan a cambios reales de A035. No existe `w:del`; se preserva la convención amarillo + tachado para texto anterior y amarillo sin tachado para texto nuevo.

## 4. A035 — valores corregidos correctamente

La fuente primaria vigente es:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
blob = bcb02c9c3493235a6f80991158c5b24fa7c04510
```

La fuente confirma:

```text
ANALYSIS_UNIT = SERIE
GROUPING_FIELD = DECLARACION / DAM
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
FULL_ASSIGNMENT = 4106
CROSS_SPLIT_DAM_OVERLAP = 0
CROSS_SPLIT_ID_UNICO_OVERLAP = 0
EVAL_CASES_WITH_HISTORICAL_SUPPORT = 1056 / 1056
EVAL_CODES_WITH_HISTORICAL_SUPPORT = 42 / 42
```

Los nueve reemplazos ejecutados son numéricamente correctos: `3000→2950`, `1006→1056`, `69→66`, `44→9` y `62→42`, según el lugar correspondiente. No se requiere revertir ninguno de ellos.

## 5. Hallazgo material — A035 quedó incompleto

El contrato de `PROMPT121D` no congeló únicamente los tamaños y las coberturas NANDINA. Para 4.1.1 también fijó explícitamente:

```text
HISTORICAL = 2950 / 28 DAM / 66 NANDINA
DEV = 100 / 6 DAM / 9 NANDINA
EVAL = 1056 / 67 DAM / 42 NANDINA
SPLIT = DAM-DISJOINT v0.2
CROSS_SPLIT_DAM_OVERLAP = 0
CROSS_SPLIT_ID_UNICO_OVERLAP = 0
```

Además, la fila A035 del plan vinculante exige actualizar las cifras concretas y el alcance `DAM/NANDINA` del benchmark final.

Sin embargo, la versión D visible reporta en Tabla 10 solo:

```text
Banco histórico = 2950 / 66 códigos NANDINA
Desarrollo = 100 / 9 códigos NANDINA
Evaluación = 1056 / 42 códigos NANDINA
```

Y el párrafo inmediato informa únicamente ausencia de solapamiento de `id_unico`. No reporta los conteos `28 / 6 / 67 DAM`, no hace explícito que la partición final v0.2 es `DAM-disjoint` y no registra como resultado observado el `CROSS_SPLIT_DAM_OVERLAP = 0`.

Esto no constituye un error numérico de lo ya escrito, pero sí una omisión material respecto del resultado que motivó la partición v0.2 y del contrato autorizado para A035. La DAM es el grupo de dependencia cuando corresponde; por ello, el resultado de independencia entre declaraciones debe quedar visible en 4.1.1 y no reducirse a la ausencia de identificadores repetidos.

## 6. Corrección mínima obligatoria

La revisión R1 debe limitarse exclusivamente a A035 y preservar todos los cambios correctos de D.

### 6.1 Párrafo inmediato de 4.1.1

Debe quedar explícito, en lenguaje de tesis, que:

- la partición final v0.2 se materializó mediante asignación explícita por DAM, manteniendo cada DAM íntegramente en una sola partición;
- histórico, desarrollo y evaluación reúnen respectivamente `28`, `6` y `67` DAM;
- no hubo solapamiento de DAM ni de `id_unico` entre las tres particiones;
- esta independencia es una condición del benchmark interno y no implica muestreo probabilístico ni validez externa.

No se requiere repetir extensamente el método ya descrito en el Capítulo 3.

### 6.2 Tabla 10

Conservar el mismo objeto y número. Actualizar únicamente las celdas de lectura de las tres filas de partición para que los descriptores finales integren DAM y NANDINA, por ejemplo:

```text
Banco histórico: 28 DAM; 66 códigos NANDINA distintos
Conjunto de desarrollo: 6 DAM; 9 códigos NANDINA distintos
Conjunto de evaluación: 67 DAM; 42 códigos NANDINA distintos
```

No alterar los resultados de curación y deduplicación.

### 6.3 A036

Permanece:

```text
A036 = VERIFY / KEEP
```

No modificar 4.1.2 ni Tabla 11. La fuente primaria confirma los conteos visibles y no existe discrepancia adicional autorizable.

## 7. QA visual

La inspección localizada independiente de 4.1.1–4.1.2 y sus fronteras no encontró clipping, overflow, tablas rotas ni páginas inesperadas. La Tabla 10 y la Tabla 11 son legibles y el marcado de revisión es visible. El problema detectado es de completitud científica del reporte de A035, no de maquetación.

## 8. Dictamen

```text
PROMPT121D_EXTERNAL_AUDIT = REVISION_REQUIRED
PROMPT121D_BLOCK_D = REVISION_REQUIRED / NOT_APPROVED
NUMERICAL_CORRECTION_REQUIRED = false
RESULT_REPORTING_CORRECTION_REQUIRED = true
TARGETED_REVISION_REQUIRED = true
FULL_RERUN_REQUIRED = false
A035_R1_REQUIRED = true
A036 = VERIFIED / KEEP
NEXT_BLOCK_121E_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

No debe ejecutarse 121E hasta que la corrección localizada A035 R1 sea entregada y auditada externamente como PASS.