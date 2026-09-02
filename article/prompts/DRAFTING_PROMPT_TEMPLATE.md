# Plantilla de prompt de redacción / Drafting Prompt Template

## Español

Usar esta plantilla para solicitar a la IA de redacción un bloque específico. No enviar prompts abiertos del tipo "redacta esta sección".

Antes de cualquier tarea que involucre literatura, Related Work, gap, novelty o nuevas referencias, la IA debe leer `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### OBJETIVO DEL BLOQUE

[Definir sección/subsección exacta y función dentro del argumento del paper.]

### FUENTES AUTORIZADAS

[Listar documentos, commits, archivos, papers y resultados permitidos.]

### BÚSQUEDA DE LITERATURA NUEVA

[Indicar `NO AUTORIZADA` salvo que exista un vacío bibliográfico explícito. Si está autorizada, definir exactamente qué vacío debe cubrir.]

Cuando esté autorizada, toda nueva referencia académica debe cumplir `BIBLIOGRAPHIC_FRAMEWORK.md`: publicación 2022–2026 para el ciclo editorial actual, revista científica revisada por pares de alto impacto, Q1 preferida y Q2 solo si es altamente específica y no existe alternativa Q1 equivalente, indexación verificable, PDF completo legítimamente disponible, DOI o identificador estable y relevancia directa para un claim/gap/método concreto. No insertar la referencia directamente en el manuscrito: devolverla primero como `CANDIDATE_NEW` para revisión.

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
5. Si se autorizó búsqueda bibliográfica: tabla separada de candidatos nuevos con autores, año, título, revista, DOI, indexación, cuartil/indicador y fuente, enlace al PDF, tipo de estudio, método, resultado relevante, limitación, claim que podría respaldar y recomendación `ADMIT / REJECT / REVIEW`.

### PROHIBICIONES GENERALES

- No inventar resultados.
- No modificar cifras.
- No reformular hipótesis/objetivos documentales como si fueran versiones oficiales.
- No convertir candidate retrieval en classification accuracy.
- No atribuir al LLM funciones de clasificación autónoma.
- No convertir asociación normativa en corrección jurídica.
- No declarar novelty sin autorización del editor científico.
- No presentar configurabilidad como generalización empírica.
- No inventar referencias, DOI, revistas, páginas, cuartiles ni disponibilidad de PDF.
- No incorporar una referencia nueva al manuscrito antes de su aprobación.

---

## English

Use this template to request a specific block from the drafting AI. Do not send open-ended prompts such as "draft this section."

Before any task involving literature, Related Work, gap identification, novelty, or new references, the AI must read `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### BLOCK OBJECTIVE

[Define the exact section/subsection and its role in the paper's argument.]

### AUTHORIZED SOURCES

[List the documents, commits, files, papers, and results that may be used.]

### NEW-LITERATURE SEARCH

[Set to `NOT AUTHORIZED` unless an explicit bibliographic gap exists. If authorized, define exactly what gap must be covered.]

When authorized, every new academic reference must comply with `BIBLIOGRAPHIC_FRAMEWORK.md`: publication in 2022–2026 for the current editorial cycle, peer-reviewed high-impact scientific journal, Q1 preferred and Q2 only when highly specific and no equivalent Q1 source exists, verifiable indexing, legitimate full-PDF availability, DOI or another stable identifier, and direct relevance to a concrete claim/gap/method. Do not insert the reference directly into the manuscript: return it first as `CANDIDATE_NEW` for review.

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
5. If a literature search was authorized: a separate candidate table with authors, year, title, journal, DOI, indexing, quartile/impact indicator and source, PDF link, study type, method, relevant result, limitation, claim it could support, and `ADMIT / REJECT / REVIEW` recommendation.

### GENERAL PROHIBITIONS

- Do not invent results.
- Do not modify figures.
- Do not reformulate documentary hypotheses/objectives as if the reformulations were official versions.
- Do not convert candidate retrieval into classification accuracy.
- Do not assign autonomous classification functions to the LLM.
- Do not convert normative association into legal correctness.
- Do not declare novelty without authorization from the scientific editor.
- Do not present configurability as empirical generalization.
- Do not invent references, DOIs, journals, pages, quartiles, or PDF availability.
- Do not incorporate a new reference into the manuscript before approval.
