# Protocolo LLM query rewrite v0.1

## Objetivo

La Fase 6A evalua si un LLM local puede mejorar la recuperacion BM25 mediante reescritura controlada de descripciones comerciales antes del retrieval. El LLM actua solo como normalizador tecnico de la consulta: no clasifica mercancias, no decide codigos y no reemplaza el recuperador.

## Alcance experimental

- Dataset permitido: `data/processed/devset_validacion_intermedia.csv`, con 13 casos y columnas `descripcion,nandina`.
- Dataset prohibido para esta fase: `data/processed/evalset_v0.1.csv`, con 600 casos finales.
- La Fase 6A no ejecuta LLM sobre el evalset final.
- La Fase 6A no modifica devset, evalset, corpus, indice BM25 ni archivos Excel.
- Los outputs son regenerables y se guardan en `outputs/evaluation/llm_query_rewrite_devset_v0.1/`.

## Rol del LLM

El modelo se ubica como una capa pre-retrieval de query rewriting. Recibe una descripcion comercial y produce una consulta reescrita mas tecnica, normalizada y lexicalmente util para BM25. La salida debe conservar el significado del texto de entrada y puede expandir abreviaturas evidentes o normalizar sinonimos cuando esten sustentados por la descripcion.

Queda prohibido que el LLM:

- Sugiera codigos arancelarios, NANDINA, capitulos, partidas o subpartidas.
- Infiera clasificaciones.
- Agregue atributos no presentes ni razonablemente explicitos.
- Cambie la naturaleza del producto.

## Referencias conceptuales

- Wang, Yang y Wei (2023), Query2doc: Query Expansion with Large Language Models, propone expandir consultas con texto generado por LLM para mejorar recuperadores sparse y dense sin fine-tuning: https://arxiv.org/abs/2303.07678.
- Jagerman et al. (2023), Query Expansion by Prompting Large Language Models, estudia expansion de consultas mediante prompting y reporta mejoras en MS-MARCO y BEIR frente a metodos tradicionales: https://arxiv.org/abs/2305.03653.
- Ma et al. (2023), Query Rewriting for Retrieval-Augmented Large Language Models, formaliza el patron rewrite-retrieve-read y enfoca la adaptacion en la consulta antes de recuperar contexto: https://arxiv.org/abs/2305.14283.
- La normalizacion de atributos de producto se trata aqui como una restriccion operacional: extraer material, uso, presentacion, composicion y otros atributos solamente si aparecen en la descripcion o son expansiones terminologicas evidentes.

## Modelo elegido

Modelo seleccionado: `qwen2.5:7b-instruct` via Ollama.

Justificacion preliminar:

- Es gratuito y ejecutable localmente mediante Ollama.
- El model card de `Qwen/Qwen2.5-7B-Instruct` reporta licencia Apache 2.0, soporte multilingue para mas de 29 idiomas incluyendo espanol, mejoras en seguimiento de instrucciones, comprension de datos estructurados y generacion de JSON: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct.
- El reporte tecnico de Qwen2.5 documenta la serie, su post-training para instruction following y sus capacidades de salida estructurada: https://arxiv.org/abs/2412.15115.
- El tamano 7B es un compromiso razonable para ejecucion local frente a alternativas mas grandes.

No se descarga ni prueba `llama3.1:8b-instruct` salvo que Qwen2.5 falle o sea inviable.

## Parametros de generacion

Configuracion inicial fija para Fase 6A:

- `temperature`: 0.0.
- `top_p`: 0.9.
- `num_predict`: 512.
- `format`: `json`.
- API local: `http://127.0.0.1:11434/api/chat`.
- Timeout por caso: 600 segundos.
- Reintentos: 1.

Estos parametros priorizan reproducibilidad, salida estructurada y baja creatividad.

## Formato esperado

El LLM debe devolver JSON estricto con este esquema:

```json
{
  "producto_generico": "...",
  "atributos": {
    "material": "...",
    "uso": "...",
    "presentacion": "...",
    "composicion": "...",
    "otros": []
  },
  "consulta_reescrita": "...",
  "terminos_clave": [],
  "advertencias": []
}
```

Los campos ausentes o no aplicables deben representarse con cadena vacia o listas vacias, no con texto inventado.

## Criterios de aceptacion

Una reescritura se acepta automaticamente si:

- El JSON parsea correctamente.
- Incluye `consulta_reescrita` no vacia.
- No contiene secuencias que parezcan codigos arancelarios de 4, 6, 8 o 10 digitos.
- Los numeros tecnicos con unidad contextual explicita, por ejemplo cantidades o medidas, no se consideran codigos si no estan asociados a terminologia arancelaria.
- No menciona expresiones prohibidas como NANDINA, capitulo, partida, subpartida o codigo arancelario.
- Conserva los atributos centrales de la descripcion original.

## Criterios de rechazo o advertencia

Una salida queda marcada con advertencia si:

- El JSON no parsea.
- La consulta reescrita esta vacia.
- Aparecen codigos numericos de 4, 6, 8 o 10 digitos.
- Se mencionan terminos prohibidos asociados a clasificacion arancelaria.
- La salida parece introducir material, uso, composicion, presentacion o funcion no presentes en el texto original.
- La salida elimina atributos tecnicamente relevantes de la descripcion original.

## Riesgos

- Alucinacion de atributos: el modelo puede agregar detalles no sustentados por la descripcion.
- Sugerencia implicita de codigo: aun sin escribir un codigo, puede orientar hacia una familia arancelaria.
- Perdida de atributos: la normalizacion puede borrar informacion comercial relevante.
- Sobre-expansion lexical: agregar sinonimos excesivos puede mejorar recall pero degradar precision BM25.
- Inestabilidad de formato: el JSON puede fallar si el modelo ignora instrucciones.
- Contaminacion experimental: ejecutar sobre el evalset final en esta fase invalidaria la separacion dev/eval.

## Decision para Fase 6B

Solo se recomienda avanzar a Fase 6B si en el devset:

- La tasa de JSON valido es 100% o cercana a 100% con fallos corregibles.
- No hay violaciones por codigos o referencias arancelarias.
- BM25 con reescritura mejora o al menos no degrada de forma material Top-1, Top-3, Top-5, Top-10 y MRR frente a BM25 original.
- Los ejemplos cualitativos no muestran alucinacion sistematica ni perdida de atributos relevantes.
