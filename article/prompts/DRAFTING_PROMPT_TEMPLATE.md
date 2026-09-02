# Plantilla de prompt de redacción / Drafting Prompt Template

## Español

Usar esta plantilla para solicitar a la IA de redacción un bloque específico. No enviar prompts abiertos del tipo "redacta esta sección".

### OBJETIVO DEL BLOQUE

[Definir sección/subsección exacta y función dentro del argumento del paper.]

### FUENTES AUTORIZADAS

[Listar documentos, commits, archivos, papers y resultados permitidos.]

### HECHOS QUE DEBEN APARECER

[Listar hechos verificables obligatorios.]

### CLAIMS AUTORIZADOS

[Listar IDs de `CLAIM_EVIDENCE_MATRIX.md` y formulaciones permitidas.]

### CLAIMS PROHIBIDOS

[Listar afirmaciones que no pueden aparecer.]

### RESULTADOS PENDIENTES

[Listar elementos que deben permanecer explícitamente fuera del texto.]

### TERMINOLOGÍA OBLIGATORIA

[Extraer términos relevantes de `STYLE_GUIDE.md`.]

### RELACIÓN CON LA SECCIÓN ANTERIOR

[Definir qué información ya se explicó para evitar redundancia.]

### RELACIÓN CON LA SECCIÓN SIGUIENTE

[Definir qué debe preparar conceptualmente el cierre del bloque.]

### ESTILO

Redacción científica sobria, precisa y verificable. No usar lenguaje promocional. No sobreinterpretar resultados. No añadir conocimiento externo salvo autorización explícita. Mantener el grado de certeza de las fuentes.

### REGLA BILINGÜE

Entregar primero `## Español` con la versión completa y luego `## English` con una versión científicamente equivalente. Ambas versiones deben contener exactamente las mismas afirmaciones, cifras, citas, limitaciones y nivel de certeza. No traducir mecánicamente si ello perjudica la naturalidad; conservar la equivalencia semántica.

### EXTENSIÓN

[Indicar rango de palabras por idioma.]

### FORMATO DE SALIDA

1. Texto final del bloque en español.
2. Texto final equivalente en inglés.
3. Tabla breve de trazabilidad claim → fuente utilizada.
4. Lista de cualquier punto que no haya podido redactarse por evidencia insuficiente.

### PROHIBICIONES GENERALES

- No inventar resultados.
- No modificar cifras.
- No reformular hipótesis/objetivos documentales como si fueran versiones oficiales.
- No convertir candidate retrieval en classification accuracy.
- No atribuir al LLM funciones de clasificación autónoma.
- No convertir asociación normativa en corrección jurídica.
- No declarar novelty sin autorización del editor científico.
- No presentar configurabilidad como generalización empírica.

---

## English

Use this template to request a specific block from the drafting AI. Do not send open-ended prompts such as "draft this section."

### BLOCK OBJECTIVE

[Define the exact section/subsection and its role in the paper's argument.]

### AUTHORIZED SOURCES

[List the documents, commits, files, papers, and results that may be used.]

### FACTS THAT MUST APPEAR

[List mandatory verifiable facts.]

### AUTHORIZED CLAIMS

[List IDs from `CLAIM_EVIDENCE_MATRIX.md` and permitted formulations.]

### PROHIBITED CLAIMS

[List statements that must not appear.]

### PENDING RESULTS

[List elements that must remain explicitly outside the text.]

### MANDATORY TERMINOLOGY

[Extract relevant terms from `STYLE_GUIDE.md`.]

### RELATION TO THE PREVIOUS SECTION

[Define what has already been explained to prevent redundancy.]

### RELATION TO THE NEXT SECTION

[Define what the end of the block should conceptually prepare.]

### STYLE

Use restrained, precise, and verifiable scientific prose. Do not use promotional language. Do not overinterpret results. Do not add external knowledge unless explicitly authorized. Preserve the degree of certainty of the sources.

### BILINGUAL RULE

Deliver `## Español` first with the complete Spanish version, followed by `## English` with a scientifically equivalent English version. Both versions must contain exactly the same claims, figures, citations, limitations, and degree of certainty. Do not translate mechanically when that harms naturalness; preserve semantic equivalence.

### LENGTH

[Specify word range per language.]

### OUTPUT FORMAT

1. Final Spanish text of the block.
2. Equivalent final English text.
3. Brief claim → source traceability table.
4. List of any point that could not be drafted because evidence was insufficient.

### GENERAL PROHIBITIONS

- Do not invent results.
- Do not modify figures.
- Do not reformulate documentary hypotheses/objectives as if the reformulations were official versions.
- Do not convert candidate retrieval into classification accuracy.
- Do not assign autonomous classification functions to the LLM.
- Do not convert normative association into legal correctness.
- Do not declare novelty without authorization from the scientific editor.
- Do not present configurability as empirical generalization.
