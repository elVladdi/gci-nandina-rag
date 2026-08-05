# Trazabilidad del corpus normativo y de los índices BM25 v0.1

## 1. Objetivo

Este documento registra la procedencia, transformación, auditoría, construcción, serialización y estado de versionamiento de los corpus normativos y de los índices BM25 utilizados en el piloto experimental offline.

Su alcance es documental y reproducible. No modifica los resultados experimentales ni convierte al corpus normativo en el ranking operativo principal.

## 2. Flujo de artefactos

```text
data/processed/corpus/nandina/nandina_corpus.jsonl
        ↓ auditoría de jerarquía y calidad
src/corpus/audit_nandina_hierarchy.py
        ↓
outputs/corpus/auditoria_nandina_jerarquica_v0.1/
        ↓ preparación del campo indexable plano
src/corpus/text_index.py
        ↓
data/processed/corpus_rag_v1_index.jsonl
        ↓ construcción jerárquica
src/corpus/build_hierarchical_nandina_corpus.py
        ↓
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
        ↓ construcción BM25
src/bm25_index.py + scripts versionados de ejecución
        ↓
bm25_nandina8.pkl / bm25_nandina8_hierarchical_v0.1.pkl
```

## 3. Corpus intermedio NANDINA

Ruta metodológica:

```text
data/processed/corpus/nandina/nandina_corpus.jsonl
```

Huella registrada:

```text
SHA-256 = 4f5f2d33e864ee2d5992e76e68b7a7fa1163f98564b79d2533f5131acb5ace58
```

Conteos auditados:

| Nivel | Registros |
|---|---:|
| Partida 4D | 1,020 |
| HS-6 | 1,117 |
| NANDINA8 | 7,648 |
| **Total** | **9,785** |

## 4. Auditoría jerárquica

Script:

```text
src/corpus/audit_nandina_hierarchy.py
```

Controles implementados:

- validación del formato JSONL;
- conteo por nivel;
- descripciones vacías, breves o genéricas;
- posible contaminación por encabezados;
- padres 4D y HS-6 ausentes;
- duplicados conflictivos por código y nivel;
- ejemplos de saltos de orden;
- generación de archivos de auditoría.

Salidas documentadas:

```text
outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.json
outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.md
outputs/corpus/auditoria_nandina_jerarquica_v0.1/missing_parents.csv
outputs/corpus/auditoria_nandina_jerarquica_v0.1/generic_descriptions.csv
outputs/corpus/auditoria_nandina_jerarquica_v0.1/hierarchy_examples.csv
```

Hallazgos principales:

| Control | Resultado |
|---|---:|
| NANDINA8 sin padre 4D explícito | 407 |
| NANDINA8 sin padre HS-6 explícito | 4,504 |
| Grupos código–nivel conflictivos | 56 |
| Descripciones con posible contaminación | 17 |
| Descripciones vacías | 1 |
| Descripciones muy cortas | 3,161 |

La relación 8D→HS-6 es nullable porque el corpus intermedio no representa todos los encabezados HS-6 como filas independientes.

## 5. Corpus plano indexable

Script:

```text
src/corpus/text_index.py
```

Transformación:

- toma el campo `texto`;
- elimina del campo indexable la subcadena iniciada en `Contexto:`;
- normaliza espacios;
- conserva el texto original sin modificación destructiva;
- escribe o actualiza `texto_index`.

Artefacto:

```text
data/processed/corpus_rag_v1_index.jsonl
```

Metadato:

```text
data/processed/corpus/curación/03_curacion_index_text_metadata.json
```

Conteos registrados:

| Control | Resultado |
|---|---:|
| Filas procesadas | 7,748 |
| Filas con remoción estimada de `Contexto:` | 7,644 |

Huella de salida:

```text
SHA-256 = 83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
```

## 6. Corpus jerárquico

Script:

```text
src/corpus/build_hierarchical_nandina_corpus.py
```

Entrada principal:

```text
data/processed/corpus/nandina/nandina_corpus.jsonl
```

Salida:

```text
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
```

Metadato:

```text
data/processed/corpus_nandina_hierarchical_v0.1_metadata.json
```

Campos conservados o construidos:

- `doc_id`, `tipo`, `codigo`, `titulo`, `texto`;
- `fuente`, `version`, `idioma`;
- sección y capítulo;
- partida 4D y descripción;
- HS-6 y descripción cuando existe;
- NANDINA8 y descripción;
- unidad física;
- página, número de línea y texto de origen;
- `texto_index_jerarquico` y `texto_index`.

Conteos:

| Control | Resultado |
|---|---:|
| NANDINA8 esperadas | 7,648 |
| Documentos generados | 7,648 |
| Con padre 4D | 7,241 |
| Con padre HS-6 | 3,144 |
| Sin padre 4D | 407 |
| Sin padre HS-6 | 4,504 |
| Sin ambos padres explícitos | 185 |
| Descripciones 8D genéricas o cortas | 2,736 |
| Textos jerárquicos finales todavía genéricos | 0 |

Huella de salida:

```text
SHA-256 = f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175
```

## 7. Diferencia entre registros y códigos únicos

El corpus jerárquico contiene 7,648 registros, pero 7,644 códigos NANDINA únicos. La diferencia de cuatro registros corresponde a duplicados conflictivos:

- `48051900`: cuatro registros, tres adicionales respecto de un código único;
- `84472010`: dos registros, uno adicional.

La construcción v0.1 conserva esta situación y la documenta como limitación de calidad del corpus.

## 8. Construcción BM25

Implementación común:

```text
src/bm25_index.py
```

La función de construcción:

- valida códigos de ocho dígitos;
- selecciona `texto_index`, con respaldo en `texto`;
- normaliza y tokeniza texto técnico en español;
- construye longitudes documentales e índice invertido;
- calcula IDF;
- serializa objetos compatibles con las evaluaciones;
- registra estadísticas de documentos, vocabulario y filas omitidas.

Parámetros utilizados:

```text
k1 = 1.5
b = 0.75
```

## 9. Estado de serialización y versionamiento

| Artefacto | Estado |
|---|---|
| `data/processed/indexes/bm25_nandina8.pkl` | Serializado y versionado en Git |
| `bm25_nandina8_hierarchical_v0.1.pkl` | Generado localmente; no versionado actualmente |

El índice plano contiene 7,644 documentos. El índice jerárquico local contiene 7,648 documentos y 7,644 códigos distintos. Ambos utilizan `k1 = 1.5` y `b = 0.75`.

El `.pkl` jerárquico puede regenerarse a partir del corpus jerárquico y de los scripts versionados. Su ausencia en Git debe interpretarse como una diferencia de política de artefactos, no como ausencia del procedimiento computacional.

## 10. Condiciones de reproducibilidad

La reconstrucción completa requiere:

1. Python 3.10 y las dependencias de `requirements.txt`;
2. corpus de entrada disponibles;
3. scripts versionados de auditoría, construcción e indexación;
4. parámetros y rutas documentados;
5. para evaluaciones sobre DAM, acceso autorizado al Excel administrativo local no versionado;
6. para generación LLM, Ollama y `qwen2.5:7b-instruct` disponibles localmente.

La reproducibilidad de los procedimientos, corpus normativos e índices se diferencia de la redistribución de la fuente administrativa restringida.

## 11. Interpretación metodológica

- El corpus normativo se utiliza como fuente de evidencia y trazabilidad.
- La recuperación histórica BM25 permanece como ranking operativo principal.
- Las limitaciones jerárquicas y los duplicados deben conservarse en la interpretación de resultados.
- El índice jerárquico no debe describirse como un artefacto binario versionado mientras su `.pkl` no se incorpore al repositorio.
- La revisión experta es externa al sistema automatizado y necesaria para cualquier uso operativo o legal.
