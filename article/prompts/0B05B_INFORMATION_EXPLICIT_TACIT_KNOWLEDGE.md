# Prompt 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado / Information, documented explicit knowledge, and limits of codified knowledge

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado`.

Este bloque es **fundacional y conceptual**. No busca demostrar novelty ni establecer un gap aduanero. Su finalidad es reconstruir con precisión cómo las fuentes asignadas conceptualizan `data`, `information`, `knowledge`, conocimiento explícito/codificado, conocimiento tácito/no codificado, information management y knowledge management, y establecer límites rigurosos para la operacionalización de estos conceptos en el proyecto.

No redactes secciones del manuscrito, no cierres el gap, no busques literatura nueva, no modifiques GitHub ni el Plan Maestro y no avances a 0B-05C, 0B-06, 0C ni fases posteriores.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/DECISIONS.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/STYLE_GUIDE.md`;
8. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
9. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
10. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`;
11. los freezes de `0B-01`, `0B-02`, `0B-03A`, `0B-03B`, `0B-04A`, `0B-04B` y `0B-05A`;
12. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
13. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
14. este prompt completo.

No reabras ni reinterpretes freezes anteriores.

### PDFs asignados

Analiza **exclusivamente** estos tres trabajos heredados:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

Para el tercer trabajo, acepta únicamente como alias físico un sufijo automático de adjunto, por ejemplo `(2)`, si la copia disponible conserva inequívocamente el título científico **Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge**. No trates el sufijo del archivo como una versión científica.

Si cualquiera de los tres no está accesible o no puede leerse íntegramente, identifica únicamente cuál falta y detente. No sustituyas contenido ausente con web, abstracts, snippets, tesis, Anexo, comentarios de revisión, conocimiento general ni otros PDF.

Todos los demás documentos del corpus quedan `OUT_OF_SCOPE_FOR_0B05B`.

### Objetivo científico del lote

El lote debe permitir responder, sin overclaiming:

1. Qué diversidad de definiciones y relaciones entre `data`, `information` y `knowledge` documenta Zins y qué conclusiones permite o no permite extraer de esa diversidad.
2. Si Zins sostiene realmente una secuencia universal `data -> information -> knowledge` o si documenta concepciones múltiples, discutidas y dependientes de marcos teóricos.
3. Cómo Hildreth & Kimble conceptualizan la dualidad entre conocimiento explícito/codificable y conocimiento tácito, y qué límites asignan a enfoques centrados en documentos, bases de datos o tecnologías.
4. Qué papel asignan Hildreth & Kimble a personas, práctica, interacción social y/o comunidades de práctica cuando el PDF lo documente.
5. Cómo Al-Hawamdeh diferencia `information management` de `knowledge management` y cómo caracteriza el desafío de gestionar conocimiento tácito.
6. Qué puede significar de manera científicamente defendible `documented explicit knowledge` o `conocimiento explícito documental` dentro de este proyecto.
7. Por qué un corpus de documentos normativos puede tratarse, como **operacionalización del proyecto**, como una fuente de conocimiento explícito/documentado sin afirmar que contiene la totalidad del conocimiento jurídico o experto necesario para clasificar.
8. Por qué los precedentes históricos registrados pueden conservar experiencia documentada, pero no deben equipararse automáticamente con toda la experiencia tácita del especialista.
9. Por qué la salida del LLM debe describirse como información/explicación estructurada sustentada en artefactos documentales, y no como conocimiento experto definitivo ni decisión jurídica autónoma.
10. Qué límites conceptuales deben gobernar cualquier uso posterior de `data`, `information`, `knowledge`, `explicit`, `tacit`, `codified`, `documented`, `expertise` y `knowledge management` en el artículo.

### Regla crítica de procedencia y operacionalización

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `OPERACIONALIZACION_DEL_PROYECTO`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

`OPERACIONALIZACION_DEL_PROYECTO` es obligatoria cuando asignes una categoría conceptual a un componente concreto del piloto que la fuente **no asigna directamente**, por ejemplo:

- descripción comercial/etiqueta como datos de entrada;
- precedentes y fragmentos recuperados como información organizada;
- corpus normativo como fuente de conocimiento explícito documental;
- LLM como organizador de una explicación estructurada;
- revisión humana como lugar donde persisten interpretación, juicio profesional o dimensiones tácitas.

Estas correspondencias pueden ser metodológicamente útiles, pero no deben atribuirse a Zins, Hildreth & Kimble o Al-Hawamdeh como si hubieran estudiado NANDINA, customs, LLM o RAG.

Una afirmación que un paper atribuya a otro trabajo no se convierte en hecho independiente del artículo. Clasifícala como `SECONDARY_CLAIM_UNVERIFIED` cuando corresponda.

### Distinciones metodológicas obligatorias

Mantén separadas estas categorías:

- `DATA`;
- `INFORMATION`;
- `KNOWLEDGE`;
- `EXPLICIT_KNOWLEDGE`;
- `TACIT_KNOWLEDGE`;
- `CODIFIED_KNOWLEDGE`;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE`;
- `INFORMATION_MANAGEMENT`;
- `KNOWLEDGE_MANAGEMENT`;
- `DOCUMENT_RETRIEVAL`;
- `EXPERT_JUDGMENT`;
- `PROJECT_OPERATIONALIZATION`.

Reglas concretas:

- no asumir una pirámide DIKW universal;
- no asumir que data se transforma automáticamente en information y luego en knowledge;
- no presentar como equivalentes `explicit`, `codified`, `documented` y `stored` salvo que la fuente lo sostenga en ese contexto;
- no afirmar que todo conocimiento tácito es absolutamente incodificable ni que todo conocimiento experto puede codificarse;
- no afirmar que un documento, base de datos o corpus constituye por sí mismo conocimiento experto completo;
- no afirmar que recuperar un documento equivale a comprenderlo, interpretarlo o aplicarlo correctamente;
- no afirmar que knowledge management equivale a information management;
- no afirmar que un LLM transforma automáticamente información en conocimiento;
- no afirmar que una explicación generada constituye conocimiento jurídico experto;
- no presentar la revisión experta como una propiedad interna del sistema automatizado;
- no convertir conceptos generales de gestión del conocimiento en evidencia empírica de corrección NANDINA.

### Verificaciones específicas por paper

#### P01 — Zins, Conceptual Approaches for Defining Data, Information, and Knowledge

Verifica:

- identidad bibliográfica visible en el PDF;
- número y naturaleza de las definiciones/participantes cuando esté explícitamente documentado;
- propósito del estudio y método de recopilación/conceptualización;
- diversidad de definiciones de data, information y knowledge;
- cómo organiza las concepciones y qué enfoques/relaciones distingue;
- si la relación D-I-K es discutida/debatible en vez de una secuencia única;
- cualquier distinción entre dominios subjetivo/objetivo/colectivo cuando el PDF la sostenga;
- qué afirmaciones corresponden a la propia posición de Zins y cuáles pertenecen a participantes citados.

No selecciones una definición de un participante y la presentes como consenso de los 45 especialistas ni como definición universal de la disciplina.

#### P02 — Hildreth & Kimble, The Duality of Knowledge

Verifica:

- tesis central y propósito del artículo;
- cómo conceptualiza conocimiento explícito y tácito;
- qué critica de los enfoques de captura/codificación tecnológica del conocimiento;
- qué función atribuye a personas, interacción, práctica y comunidades cuando el texto lo sostenga;
- en qué sentido afirma que el conocimiento reside en personas y qué alcance tiene esa formulación;
- si explicit/tacit forman una dicotomía rígida o una dualidad más compleja según los autores;
- límites de transferencia desde gestión del conocimiento general hacia conocimiento experto aduanero.

No conviertas la fuente en evidencia de que un especialista aduanero concreto posee necesariamente determinado conocimiento tácito ni de que ninguna parte de ese conocimiento pueda documentarse.

#### P03 — Al-Hawamdeh, Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge

Verifica:

- identidad y tipo documental visibles;
- distinción propuesta entre information management y knowledge management;
- cómo caracteriza información, conocimiento, conocimiento explícito y conocimiento tácito cuando corresponda;
- qué papel asigna a personas, organización, procesos y tecnología;
- qué significa gestionar conocimiento tácito en el argumento del artículo;
- qué límites reconoce para la captura, almacenamiento o transferencia de conocimiento;
- si las afirmaciones sobre competitividad, aprendizaje organizacional u otros beneficios dependen de fuentes secundarias o son argumentos conceptuales.

No presentes el artículo como benchmark empírico de efectividad de knowledge management ni como evidencia específica del dominio aduanero.

### Relación con el piloto experimental

El proyecto puede usar este lote únicamente para fundamentar fronteras conceptuales y una operacionalización explícita.

Debe preservarse como mínimo:

`DATA != INFORMATION != KNOWLEDGE`, sin afirmar una transformación universal automática.

`DOCUMENTED / EXPLICIT KNOWLEDGE != TOTAL EXPERT KNOWLEDGE`.

`DOCUMENT RETRIEVAL != EXPERT INTERPRETATION != LEGAL CORRECTNESS`.

`LLM-GENERATED EXPLANATION != EXPERT KNOWLEDGE != OFFICIAL CLASSIFICATION`.

Cuando el lote se conecte con el piloto, utiliza `OPERACIONALIZACION_DEL_PROYECTO` y conserva estas restricciones:

- el banco histórico contiene registros/precedentes, no una reproducción completa de expertise tácita;
- el corpus normativo contiene documentos autoritativos que pueden organizarse como fuente documental explícita, pero su recuperación no garantiza aplicación jurídica correcta;
- el LLM local organiza una explicación sobre candidatos/evidencia recibidos, pero no se convierte por ello en poseedor de conocimiento experto jurídico;
- la revisión experta permanece fuera del sistema automatizado.

No modifiques ningún hecho experimental congelado.

### Relación con F1–F5

0B-05B es un lote fundacional y **no** un pressure test de novelty aduanera. Usa exclusivamente:

- `METHOD_FOUNDATION_RELEVANT`;
- `METHOD_CONTRAST_RELEVANT`;
- `METHOD_BOUNDARY_RELEVANT`;
- `NOT_RELEVANT_TO_GAP_CANDIDATE`.

Criterio esperado:

- **F1:** normalmente `METHOD_BOUNDARY_RELEVANT` solo para distinguir evidencia documental de decisión/clasificación; no novelty.
- **F2:** `METHOD_BOUNDARY_RELEVANT` para distinguir explicación organizada de conocimiento/juicio experto; no novelty.
- **F3:** normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- **F4:** `METHOD_BOUNDARY_RELEVANT` para separar disponibilidad/organización documental de correctness sustantiva o jurídica.
- **F5:** como máximo `METHOD_BOUNDARY_RELEVANT`; conocimiento/documentación no sustituye la evaluación formal de auditabilidad por salida.

No reabras G6 ni G7.

### Formato obligatorio de salida

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | tipo documental visible | observaciones`.

#### B. Matriz conceptual comparativa
Una fila por paper:
`paper | problema | data | information | knowledge | explicit/codified | tacit | people/practice | information management | knowledge management | evaluación/base empírica | límite | función`.

#### C. Fichas individuales
Una por paper usando las cinco etiquetas de procedencia/operacionalización.

#### D. Taxonomía metodológica
Clasifica cada paper con las categorías obligatorias, explicando convergencias y contradicciones sin forzar consenso.

#### E. Mapa conceptual por paper
Representa las relaciones que **cada fuente realmente sostiene**. No fuerces un pipeline lineal común. Si una fuente rechaza o problematiza una secuencia, represéntalo explícitamente.

#### F. Matriz de operacionalización para el proyecto
`componente del piloto | categoría propuesta | fuente(s) que permiten la frontera | estado (REPORTADO / OPERACIONALIZACION) | formulación permitida | formulación prohibida`.

Incluye como mínimo:

- descripción comercial/label;
- banco histórico/precedentes;
- corpus normativo/documentos;
- fragmentos recuperados;
- Top-3/candidatos;
- explicación del LLM;
- revisión experta.

#### G. Relación metodológica con F1–F5
`paper | F1 | F2 | F3 | F4 | F5 | justificación` usando solo las etiquetas metodológicas autorizadas.

#### H. Claims conceptuales autorizables
Propón formulaciones precisas potencialmente utilizables después en Methods/Related Work/Conceptual Framework, cada una con fuente, tipo (`REPORTADO_POR_AUTORES` o `OPERACIONALIZACION_DEL_PROYECTO`) y límite explícito. **No redactes todavía el manuscrito.**

#### I. Claims prohibidos o excesivos
Lista cerrada de formulaciones que estos tres papers no autorizan.

#### J. Claims secundarios, contradicciones conceptuales y metadata pendiente
`paper | claim/contradicción/inconsistencia | estado | acción futura necesaria`.

No elimines contradicciones entre autores mediante una síntesis artificial. Si usan de modo diferente `data`, `information`, `knowledge`, `explicit` o `tacit`, conserva esas diferencias.

#### K. Recomendación bibliográfica y dictamen

Primero:
`paper | función científica | uso potencial | recomendación | justificación`.

Usa cuando corresponda:

- `KEEP_CORE_METHOD`;
- `KEEP_SUPPORTING_METHOD`;
- `REVIEW_REQUIRED`;
- `EXCLUDE_FROM_ARTICLE`.

Después concluye uno de:

- `PASS`;
- `PASS WITH CORRECTIONS`;
- `BLOCKED`.

Detente al terminar 0B-05B.

---

## English

### Role and scope

Act as the drafting and bibliographic-analysis AI for the main scientific article. Execute **only** `0B-05B — Information, documented explicit knowledge, and limits of codified knowledge`.

This is a **foundational conceptual** block. It does not establish novelty or a customs research gap. Its purpose is to reconstruct how the assigned primary sources conceptualize data, information, knowledge, explicit/codified knowledge, tacit/non-codified knowledge, information management, and knowledge management, and to define rigorous boundaries for the project's own operationalization of these concepts.

Do not draft manuscript sections, search for new literature, modify GitHub or the Master Plan, or advance to 0B-05C, 0B-06, 0C, or later phases.

### Required onboarding

Read `article/START_HERE.md`, the current article governance/status files, `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`, all frozen 0B artifacts through 0B-05A, frozen 0A ground truth, and this complete prompt. Do not reopen prior freezes.

### Assigned PDFs

Analyze **only**:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

An automatic attachment suffix such as `(2)` is acceptable for the third physical file only when the scientific title is unequivocally the same; the suffix is not a scientific version identifier.

If any source is unavailable or cannot be read in full, identify that source and stop. Do not substitute web material, abstracts, snippets, thesis text, Annex comments, general knowledge, or other PDFs.

### Governing analytical rules

Use `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `OPERACIONALIZACION_DEL_PROYECTO`, `NO_VERIFICABLE_EN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`.

`OPERACIONALIZACION_DEL_PROYECTO` is mandatory whenever a general concept is mapped onto a specific pilot component that the original authors did not study.

Preserve the following boundaries:

`DATA != INFORMATION != KNOWLEDGE`, without assuming a universal automatic transformation.

`DOCUMENTED / EXPLICIT KNOWLEDGE != TOTAL EXPERT KNOWLEDGE`.

`DOCUMENT RETRIEVAL != EXPERT INTERPRETATION != LEGAL CORRECTNESS`.

`LLM-GENERATED EXPLANATION != EXPERT KNOWLEDGE != OFFICIAL CLASSIFICATION`.

Do not impose a universal DIKW pyramid, do not equate explicit/codified/documented/stored without source support, do not claim that all tacit knowledge is absolutely uncodifiable or that all expertise can be codified, and do not treat document retrieval or LLM generation as expert legal understanding.

### Paper-specific verification

For **Zins**, verify the diversity of definitions and theoretical relations among data, information, and knowledge, the study's method, the distinction between author position and panel-participant definitions, and whether the paper supports or problematizes a universal D-I-K sequence.

For **Hildreth & Kimble**, verify the explicit/tacit knowledge duality, critiques of capture/codification-centered knowledge management, the documented role of people/practice/social interaction/communities where supported, and the precise scope of claims that knowledge resides in people.

For **Al-Hawamdeh**, verify the distinction between information management and knowledge management, the treatment of tacit knowledge, the roles of people/process/technology, limits of capture/storage/transfer, and which claimed benefits are conceptual or secondary rather than empirically established.

### Project operationalization

Any mapping from these conceptual papers onto the pilot must be explicitly labeled as project operationalization. The historical bank contains recorded precedents rather than a complete representation of tacit expertise; the normative corpus may be treated as a source of documented explicit knowledge without implying complete legal expertise; the local LLM organizes an explanation rather than becoming an expert knower; and expert review remains outside the automated system.

Do not change frozen experimental facts.

### F1–F5

This block is not a novelty pressure test. Use only methodological labels. F1/F2/F4/F5 may receive boundary relevance; F3 is normally not relevant. G6 and G7 remain closed as previously frozen.

### Mandatory output

Produce sections A–K matching the Spanish specification: integrity control; comparative conceptual matrix; individual source cards; methodology taxonomy; per-paper conceptual maps; project-operationalization matrix; F1–F5 methodological relation; authorized conceptual claims; prohibited/excessive claims; secondary claims/conceptual contradictions/metadata issues; bibliographic recommendation plus `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED` verdict.

Stop after 0B-05B.