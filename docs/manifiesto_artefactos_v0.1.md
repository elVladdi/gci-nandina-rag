# Manifiesto de artefactos v0.1

Este documento resume la politica de datos, artefactos, checksums y Git/no Git del protocolo experimental v0.1. El detalle machine-readable esta en `docs/manifest_artifacts_v0.1.json`.

## Insumos oficiales de v0.1

Los insumos oficiales son los archivos necesarios para sostener el piloto offline y reconstruir el baseline BM25:

- `src/configs/experiment_v0.1.json`: snapshot metodologico oficial.
- `src/configs/experiment_config.json`: configuracion operativa usada por scripts.
- `data/raw/Arancel 2022.pdf`: fuente local del corpus arancelario.
- `data/raw/CAN Desición 885 - Nanadina Gaceta 4359.pdf`: fuente local NANDINA/CAN.
- `data/processed/corpus_rag_v1.jsonl`: corpus curado base.
- `data/processed/corpus_rag_v1_index.jsonl`: corpus indexable oficial.
- `data/processed/devset_validacion_intermedia.csv`: devset piloto actual.
- `data/processed/indexes/bm25_nandina8_run_metadata.json`: metadatos del indice BM25.

El indice `data/processed/indexes/bm25_nandina8.pkl` se considera artefacto de aceleracion. Esta disponible localmente y ya esta versionado, pero metodologicamente puede regenerarse desde el corpus indexable y los parametros BM25 congelados.


## Evalset final v0.1

El evalset final v0.1 fue generado desde el Excel SUNAT real en modo `sunat-block` y congelado en `data/processed/evalset_v0.1.csv` con 600 casos unicos validos. Antes de congelarlo se auditaron 647 casos extraidos, 31 grupos duplicados exactos y 47 filas excedentes por la llave `descripcion + nandina_ref + regimen`.

La metadata asociada queda en `data/processed/evalset_v0.1_metadata.json` y registra fuente, fecha de consulta, formato de extraccion, regla de deduplicacion, conteos de calidad y checksums. Estos artefactos sostienen la evaluacion final posterior, pero no constituyen por si mismos resultados experimentales ni validacion de hipotesis. El alcance empirico queda concentrado en regimen `10` (importacion para el consumo), por lo que los resultados no deben generalizarse a otros regimenes aduaneros.

## Resultados preliminares

Las corridas `data/processed/runs/bm25_2pass_llm_*` con archivos existentes son resultados preliminares de BM25 + LLM rewrite. Sirven para inspeccion o comparacion exploratoria, pero no son validacion final.

El manifiesto incluye las corridas no vacias:

- `bm25_2pass_llm_20260117_135306`.
- `bm25_2pass_llm_20260117_145435`.
- `bm25_2pass_llm_20260117_160632`.
- `bm25_2pass_llm_20260117_162840`.
- `bm25_2pass_llm_20260117_175226`.
- `bm25_2pass_llm_20260117_182635`.
- `bm25_2pass_llm_20260117_185139`.

Los directorios vacios se registran como omitidos en el manifiesto JSON y no deben usarse como evidencia de resultados.

## Artefactos exploratorios

Text2Trade/dense retrieval queda como artefacto exploratorio o componente candidato, no como componente formal del protocolo v0.1.

Se documentan como trazabilidad:

- `data/processed/indexes/text2trade_nandina8_v1/retrieval_config.json`.
- `data/processed/indexes/text2trade_nandina8_v1/text2trade_nandina8_run_metadata.json`.

Se documentan como artefactos locales o regenerables:

- `data/processed/indexes/text2trade_nandina8_v1/index/vectors.npy`.
- `data/processed/indexes/text2trade_nandina8_v1/store/nandina8_docstore.jsonl`.
- `data/processed/indexes/text2trade_nandina8_v1/model/model.safetensors`.

Estos ultimos no deben subirse a Git por peso, regenerabilidad o dependencia de modelos locales.

## Politica Git/no Git

Debe versionarse en Git:

- Configuraciones oficiales y operativas.
- Documentacion metodologica.
- Manifiestos.
- Dataset pequeno de validacion intermedia.
- Corpus y metadatos que ya estan trackeados y sostienen la trazabilidad de v0.1.

No debe subirse a Git:

- Nuevos archivos bajo `data/raw/*`.
- Nuevos archivos bajo `data/processed/*` salvo decision explicita.
- Corridas bajo `data/processed/runs/*`.
- Vectores, docstores, indices densos y pesos de modelos pesados.
- Salidas generadas bajo `outputs/*`.

La politica actual de `.gitignore` ya ignora nuevos contenidos en `data/raw`, `data/processed`, `outputs`, `models` e `indexes`, manteniendo solo `.gitkeep`. Algunos artefactos de `data/processed` ya estan versionados por historia del repositorio; el manifiesto los trata como parte congelada de v0.1, no como permiso general para subir nuevos datos procesados.

## Verificacion de integridad

Para verificar un archivo individual en PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "data/processed/corpus_rag_v1_index.jsonl"
```

El valor `Hash` debe coincidir con el campo `sha256` del artefacto correspondiente en `docs/manifest_artifacts_v0.1.json`.

Para revisar todos los paths del manifiesto, cargar el JSON y validar que cada `path` exista cuando `exists` sea `true`. Los directorios tienen `sha256: null`; los archivos listados tienen checksum. El propio manifiesto puede verificarse calculando su hash desde fuera del archivo.

## Reproducibilidad fuerte pendiente

Para una reproducibilidad mas fuerte faltaria:

- Registrar fuente externa oficial, URL o identificador persistente de cada PDF fuente.
- Documentar comandos exactos de reconstruccion de corpus, indice BM25 y artefactos Text2Trade.
- Crear un lockfile de dependencias o contenedor reproducible.
- Separar almacenamiento de artefactos pesados en una ubicacion externa versionada por checksum.
- Definir una politica formal para promover o descartar Text2Trade como componente experimental.
- Ejecutar evaluaciones controladas y registrar resultados finales en una fase posterior.

Hasta entonces, v0.1 debe interpretarse como protocolo congelado de piloto offline, no como validacion final de hipotesis.
