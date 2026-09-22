# D-038 — Architecture B02 opening

```text
DECISION_ID = D-038
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-037
CANONICAL_MASTER = ARTICLE_MASTER_V008
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CANONICAL_CITATION_COMMENTS = 40
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTIONS_3_5_TO_3_7_ONLY
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Apertura del bloque

Architecture B01 fue aprobada por el autor y quedó integrada canónicamente mediante D-037. No existe un gate autoral adicional entre la integración de B01 y la apertura editorial de B02. En consecuencia, la IA Gestora abre Architecture B02 como siguiente bloque atómico de redacción.

Architecture B02 comprende exclusivamente:

- `3.5 Candidate-specific documentary retrieval` / `Recuperación documental específica por candidato`;
- `3.6 Evidence-context construction and controlled explanation` / `Construcción de contexto de evidencia y explicación controlada`;
- `3.7 Configurability and interface requirements` / `Configurabilidad y requisitos de interfaz`.

No se autoriza modificar 3.1–3.4 ni abrir Section 4 — Experimental design.

## 2. Ground truth científico de B02

B02 debe continuar exactamente la frontera fijada por B01:

`historical ranking → fixed Top-3 → candidate-specific documentary evidence → evidence-context construction → local LLM controlled explanation`

La recuperación documental/normativa opera sobre candidatos ya fijados. Su función es asociar evidencia identificable con cada candidato; no puede insertar, eliminar, sustituir ni reordenar códigos. La asociación de evidencia no demuestra por sí sola corrección normativa sustantiva.

El contexto entregado al LLM debe mantener identificables, en el nivel arquitectónico pertinente, la consulta/descripción, los candidatos y su orden, el respaldo o precedente histórico disponible, la evidencia documental recuperada y la relación entre candidato, evidencia y explicación. El LLM local opera únicamente después de quedar fijado el Top-3 y genera explicación controlada; no clasifica desde cero, no introduce códigos externos, no cambia el orden y no retroalimenta la etapa de ranking. El reranking LLM permanece diagnóstico y fuera del flujo principal.

La configurabilidad es una propiedad de diseño. B02 puede explicar qué recursos pueden sustituirse en una nueva instanciación —por ejemplo, banco histórico etiquetado, espacio de clases objetivo y corpus documental compatible— y qué interfaces/procedencia/versionamiento deben conservarse. No puede presentar esa configurabilidad como evidencia de transferencia de desempeño o generalización empírica.

## 3. Evidencia autorizada

Fuentes y controles mínimos:

- `article/manuscript/ARTICLE_MASTER_V008.md` como baseline narrativo canónico;
- `article/CLAIM_EVIDENCE_MATRIX.md`, especialmente C02, C03 y C15, y las prohibiciones C12, C13, C16 y C18;
- `article/SOURCE_REGISTRY.md`, con `SRC-02` como fuente gobernante de arquitectura/metodología operativa;
- `SRC-02 = Anexo_1_NANDINA_LLM_RAG_v13.docx` o copia de plataforma de identidad documental equivalente aprobada;
- fuentes de implementación/reproducibilidad del repositorio únicamente para verificar acciones o interfaces concretas, sin convertir decisiones experimentales particulares en requisitos universales de la arquitectura.

La fuente metodológica vigente documenta que el Top-3 entregado al explicador conserva exactamente códigos y orden; define la evidencia normativa como material recuperado del corpus y vinculado con un candidato, cuya presencia no garantiza pertinencia o suficiencia; define la explicación restringida como texto generado a partir de la descripción, el Top-3 fijo y evidencia histórica/normativa; y define trazabilidad, procedencia, versionamiento y reproducibilidad como propiedades que permiten reconstruir objetos y transformaciones sin equivaler a corrección legal.

## 4. Función narrativa de las subsecciones

### 3.5 Candidate-specific documentary retrieval

Debe explicar, a nivel arquitectónico:

1. que la entrada es el Top-3 ya fijado por 3.4;
2. que la recuperación documental se realiza por candidato o de forma que conserve explícitamente la identidad del candidato al que se asocia cada evidencia;
3. que el resultado son asociaciones candidato–evidencia identificables y trazables;
4. que el ranking histórico no se recalcula ni se modifica en esta etapa;
5. que la presencia, oficialidad o recuperabilidad de un fragmento no constituye por sí sola una decisión de corrección jurídica.

Los documentos concretos, fechas regulatorias, estrategia/indexación exacta, parámetros y corpus experimental pertenecen a Section 4.

### 3.6 Evidence-context construction and controlled explanation

Debe explicar, a nivel arquitectónico:

1. cómo se ensambla un contexto que preserve la consulta/descripción, los candidatos fijos y su orden, el soporte histórico disponible y la evidencia documental recuperada;
2. cómo se mantienen identificadores/procedencia suficientes para reconstruir la relación candidato–evidencia–explicación;
3. que el LLM recibe ese contexto después de quedar fijado el ranking;
4. que su única salida autorizada en el flujo principal es la explicación controlada;
5. que debe preservar Top-3 y orden, no incorporar códigos externos y no retroalimentar candidate generation/ranking;
6. que una explicación trazable o estructuralmente válida no equivale por sí sola a una explicación jurídicamente correcta ni demuestra fidelidad causal del razonamiento.

El modelo concreto, versión, prompt, parámetros de generación, formato exacto de salida y controles experimentales pertenecen a Section 4 salvo el mínimo necesario para definir la interfaz arquitectónica.

### 3.7 Configurability and interface requirements

Debe explicar de forma concreta, no abstracta:

1. qué recursos pueden sustituirse en otra instanciación: banco histórico etiquetado, espacio de clases/códigos y corpus documental compatible;
2. qué contratos deben mantenerse: entrada textual normalizable, registros históricos trazables a códigos, candidatos únicos y ordenados, frontera fija del Top-3, evidencia vinculable a candidatos e identificadores/procedencia suficientes para el contexto y la explicación;
3. que datos, corpus, configuraciones, prompts/modelos y otros objetos relevantes deben poder identificarse/versionarse cuando sean necesarios para reproducir una instanciación;
4. que el repositorio de reproducibilidad documentará y distribuirá los artefactos redistribuibles necesarios para reconstruir la instanciación experimental, mientras Section 4 especificará los recursos concretos, hashes, restricciones de redistribución e instrucciones;
5. que reinstanciar el procedimiento con otros recursos no implica que el desempeño observado se transfiera a esos nuevos recursos o dominios.

El lector debe entender que la arquitectura no está intrínsecamente atada al banco histórico, espacio de clases o corpus documental concretos del testbed, pero sí exige que una nueva instanciación cumpla los contratos de interfaz y trazabilidad descritos.

## 5. Prohibiciones

B02 no debe:

- modificar Introduction, Related Work o Architecture B01 (3.1–3.4);
- redactar Section 4 o posteriores;
- introducir cifras de resultados, métricas observadas, tamaños experimentales o conclusiones de hipótesis;
- presentar recuperación normativa como generadora o reordenadora del Top-3 principal;
- presentar el LLM explicador como clasificador o decisor;
- presentar el reranker diagnóstico como parte del flujo principal;
- declarar legal correctness, clasificación oficial, SOTA, superioridad global, novelty absoluta, `FINAL_GAP` o generalización empírica;
- fijar como universales parámetros, nombres de archivos, índices, modelos o corpus propios de una sola instanciación;
- modificar `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, gobernanza, claim matrix o source registry;
- promover `ARTICLE_MASTER_V009`;
- abrir Experimental design.

## 6. Política técnica y timeout-safe

D-021, D-027 y D-035 siguen vinculantes.

La IA de Redacción debe partir del DOCX exacto:

`ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`

SHA-256:

`f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`

Si el binario exacto no está disponible o el hash no coincide, debe detenerse. No puede reconstruir el DOCX desde Markdown.

No usar Base64 manual, fragmentación/chunking ni reintentos de transferencia grande que reproduzcan el timeout ya conocido. Los artefactos acumulativos grandes deben entregarse al autor como archivos exactos descargables para posterior verificación/materialización por la IA Gestora.

## 7. Gate de salida

La IA de Redacción no puede autoasignarse `APPROVED`, `FROZEN`, `INTEGRATED` ni abrir B03/Experimental design.

B02 solo podrá cerrarse después de:

`Drafting AI delivery → independent IA Gestora audit → corrections if needed → PASS → explicit author approval → canonical integration`.
