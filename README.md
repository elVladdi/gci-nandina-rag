# Gestión de información documental para recomendación auditable de subpartidas NANDINA con LLM+RAG

Repositorio del piloto experimental offline de la investigación de maestría:

**Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.**

El proyecto organiza corpus normativo, recuperación documental y experimentos offline para apoyar la recomendación auditable de subpartidas NANDINA. No produce clasificación oficial ni reemplaza revisión experta.

## Estado de la Fase 1

Esta fase deja una base ejecutable y mínimamente reproducible. Los notebooks siguen disponibles como bitácora experimental, pero la lógica básica de corpus, BM25, recuperación y prueba mínima ya vive en `src/`.

## Estructura

```text
.
├── data/
│   ├── raw/                  # PDFs fuente locales
│   └── processed/            # corpus, índices y artefactos regenerables
├── docs/                     # documentación metodológica
├── notebooks/                # exploración y experimentos originales
├── outputs/                  # salidas generadas
├── src/
│   ├── bm25_index.py         # índice BM25 compatible con notebooks y pickles previos
│   ├── corpus/               # preparación de campos de corpus para recuperación
│   ├── retrieval/            # carga y consulta de índices
│   ├── experiments/          # scripts ejecutables
│   ├── evaluation/           # métricas mínimas
│   └── utils/                # rutas y configuración
├── requirements.txt
└── README.md
```

## Instalación

Desde la raíz del repositorio:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si el proyecto se ejecuta desde otra ruta, puede fijarse la raíz con:

```powershell
$env:NANDINA_PROJECT_ROOT = "C:\ruta\al\repo"
```

## Configuración

La configuración principal está en:

```text
src/configs/experiment_config.json
```

Las rutas son relativas a la raíz del repositorio por defecto. Esto evita depender de rutas absolutas locales.

## Reconstruir o usar el corpus

Si ya existe `data/processed/corpus_rag_v1_index.jsonl`, puede usarse directamente para BM25.

Para regenerar el campo `texto_index` a partir del corpus curado:

```powershell
python -m src.corpus.text_index
```

Entrada por defecto:

```text
data/processed/corpus_rag_v1.jsonl
```

Salida por defecto:

```text
data/processed/corpus_rag_v1_index.jsonl
```

## Construir índice BM25

Para reconstruir el índice NANDINA-8:

```powershell
python -m src.experiments.build_bm25_index
```

Salida por defecto:

```text
data/processed/indexes/bm25_nandina8.pkl
data/processed/indexes/bm25_nandina8_run_metadata.json
```

El índice conserva compatibilidad con los notebooks que importan `bm25_index.BM25Index`.

## Cargar índice y ejecutar una prueba mínima

Con el índice existente o reconstruido:

```powershell
python -m src.experiments.smoke_test --query "computadora portátil con procesador y memoria" --top-n 5
```

El comando imprime los códigos NANDINA recuperados, puntajes BM25 y fragmentos de texto.

## Notebooks de referencia

Los notebooks existentes documentan el desarrollo original:

- `01_Construccion_Corpus_NANDINA.ipynb`
- `02_Construccion_Corpus_Arancel2022_RGI_Notas.ipynb`
- `03_Curacion_Corpus_RAG.ipynb`
- `04_BM25_Indexacion_NANDINA.ipynb`
- `05_BM25_2Pasadas_LLM_Rewrite_Evaluacion.ipynb`
- `05_Text2Trade_Indexacion_NANDINA.ipynb`

## Política de artefactos

No subir modelos pesados, PDFs grandes ni artefactos regenerables nuevos sin decisión explícita. Algunos artefactos ya estaban versionados al iniciar esta fase; no se movieron ni eliminaron.

## Alcance

La Fase 1 no ejecuta evaluación final ni amplía dataset. El objetivo es reproducibilidad mínima: preparar corpus indexable, construir/cargar BM25 y ejecutar una consulta de humo.
