# Section 4 — conceptual restructuring proposal V01

## Español

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_SECTION4_RESTRUCTURE_PROPOSAL_V01
GOVERNING_DECISION = D-044
STATUS = PROPOSAL / AUTHOR_REVIEW_REQUIRED
CANONICAL_MASTER = ARTICLE_MASTER_V009
SECTION_4 = CONCEPTUALLY_REOPENED
DRAFTING_AI = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
```

### 1. Principio rector

Section 4 debe explicar cómo se evaluó experimentalmente una instanciación concreta de la arquitectura definida en Section 3. No debe presentar el experimento como una herramienta operativa de apoyo a decisiones ni convertir Methods en un inventario técnico del repositorio.

La secuencia narrativa debe responder, en este orden, a estas preguntas: qué se evaluó; con qué datos históricos y corpus documental; cómo se obtuvieron y prepararon esos recursos; cómo se construyeron las particiones y controles de validez; cómo se instanció y ejecutó la arquitectura; cómo se evaluó cada salida; y qué recursos permiten reproducir la ejecución.

### 2. Estructura propuesta

#### 4. Experimental design

Breve apertura: evaluación experimental offline de una instanciación de la arquitectura. El escenario NANDINA Chapter 87 y el corpus normativo peruano delimitan la evaluación empírica, no el alcance conceptual de la arquitectura.

#### 4.1. Experimental setting and scope / Entorno y alcance experimental

Debe establecer:
- objetivo de la evaluación experimental;
- dominio empírico: NANDINA a ocho dígitos, Chapter 87, corpus documental/normativo peruano;
- SERIE como unidad de análisis;
- DAM/declaración como unidad de agrupamiento cuando exista dependencia;
- carácter offline y condiciones controladas;
- frontera de interpretación: la evaluación caracteriza esta instanciación; la posibilidad de reinstanciar el procedimiento con otros niveles, clases o corpus no implica transferencia del desempeño.

Debe eliminar el encuadre de “piloto no vinculante de apoyo a decisiones” como definición principal del experimento. La distinción jurídica puede conservarse, si se necesita, como límite secundario y no como función narrativa de 4.1.

#### 4.2. Historical data and experimental dataset construction / Datos históricos y construcción de los datasets experimentales

##### 4.2.1. Source and data collection / Fuente y recolección

Debe empezar por la fuente administrativa y el procedimiento real de obtención de los registros: origen, periodo y criterios de selección; recolección manual; campos conservados para representar cada SERIE y su DAM. El Excel intermedio o cualquier archivo físico es un artefacto de trabajo, no la fuente científica que debe encabezar la explicación.

##### 4.2.2. Processing and curation / Procesamiento y curación

Debe describir la transformación automatizada con Python de los registros recolectados hacia una estructura tabular por SERIE, la normalización necesaria, validaciones, reglas de exclusión, control de duplicados/conflictos y delimitación a Chapter 87. Deben explicarse operaciones científicamente relevantes, no nombres de scripts, rutas internas, hojas físicas ni fingerprints.

##### 4.2.3. Partition construction and dataset composition / Construcción de particiones y composición

Debe explicar cómo el pool curado se separó en histórico, desarrollo y evaluación preservando DAM como unidad de agrupamiento. Debe declarar ausencia de DAM compartidas y el control de identificadores de SERIE entre particiones. La composición final se presentará preferentemente en una tabla compacta con número de SERIE, DAM y códigos representados por conjunto. Los nombres internos H100/DEV/EVAL solo deben conservarse si facilitan de forma clara la lectura de Results.

La antigua subsección “Target class space” deja de ser una subsección autónoma. La delimitación a NANDINA de ocho dígitos y Chapter 87 pertenece a 4.1 y la composición de códigos observados pertenece a 4.2.3.

#### 4.3. Documentary corpus and evidence resource / Corpus documental y recurso de evidencia

Debe identificar las fuentes documentales/normativas, alcance, autoridad y frontera temporal utilizadas para proporcionar evidencia a los candidatos. Debe explicar cómo se prepara y representa el corpus para recuperación, incluida la estructura jerárquica cuando sea metodológicamente relevante. Los detalles físicos de archivos e índices permanecen en los recursos de reproducibilidad salvo que sean indispensables para comprender el método.

#### 4.4. Partition validity and dependence controls / Validez de particiones y control de dependencia

Debe concentrar los controles que justifican el uso analítico de los conjuntos: separación por DAM, leakage, duplicados y near-duplicates, soporte histórico necesario y otros diagnósticos de validez autorizados. Debe distinguir controles de diseño de resultados de desempeño.

#### 4.5. Experimental system configuration and execution / Configuración y ejecución experimental

Debe instanciar la arquitectura de Section 3 sin volver a explicarla conceptualmente. Debe especificar únicamente las decisiones que afectan materialmente la ejecución: representación de consulta, recuperador histórico y configuración relevante, construcción del Top-k y Top-3 fijo, recuperación documental por candidato, construcción de contexto, modelo local y restricciones de generación. Los valores concretos pueden organizarse en una tabla de configuración si mejora la lectura.

#### 4.6. Evaluation framework and protocols / Marco y protocolos de evaluación

Debe mapear cada pregunta de investigación y función del sistema con su salida, unidad, métrica y límite interpretativo. En lugar de tres secciones autónomas 4.7–4.9, se propone concentrar los protocolos como subsecciones:
- 4.6.1 Candidate-retrieval evaluation;
- 4.6.2 Documentary-evidence evaluation;
- 4.6.3 Controlled-explanation evaluation.

Esto mantiene separadas las tres salidas sin fragmentar innecesariamente Methods.

#### 4.7. Statistical and robustness analysis / Análisis estadístico y de robustez

Debe contener únicamente los análisis cerrados y autorizados: diseño inferencial, unidades, comparaciones, sensibilidad/robustez y límites permitidos por el Plan Maestro experimental. No debe anticipar resultados.

#### 4.8. Reproducibility resources / Recursos de reproducibilidad

Debe explicar qué permite reconstruir el repositorio de reproducibilidad y qué clases de artefactos contiene o referencia: datos redistribuibles, configuraciones, código, manifiestos, documentación y restricciones de acceso/redistribución. La prosa principal no debe enumerar SHA-256, rutas internas o inventarios de archivos; esos identificadores pertenecen a los manifiestos y al propio repositorio.

### 3. Reglas editoriales transversales

1. Methods describe objetos, procedimientos, decisiones y controles científicos; el repositorio conserva identidad técnica exhaustiva.
2. No SHA-256, rutas internas o nombres físicos de archivos en el cuerpo salvo necesidad metodológica excepcional y justificada.
3. No códigos internos de experimentos/configuraciones si un término científico descriptivo basta.
4. No presentar el experimento como una herramienta de apoyo a decisiones; se evalúa una instanciación experimental de la arquitectura.
5. Preferir “evaluate/evaluar” frente a “validate/validar” salvo que se defina explícitamente un criterio de validación.
6. Configurabilidad/reinstanciación con otros datos, niveles o corpus no equivale a generalización empírica del desempeño.
7. Los conteos que caracterizan los datasets pueden permanecer en Methods; métricas de desempeño pertenecen a Results.
8. La estructura debe permitir que un tercero entienda qué datos debe aportar y qué transformaciones/controles debe reproducir sin necesitar conocer la organización interna del repositorio.

### 4. Enmiendas posteriores necesarias en Section 3

Una vez aprobada la estructura de Section 4, deben corregirse dos anticipaciones editoriales de Section 3 sin alterar la arquitectura científica:
- 3.5 no debe prometer que Section 4 listará hashes;
- 3.7 no debe presentar 4.11 como inventario narrativo de identidades técnicas.

Estas enmiendas son de coherencia editorial, no una reapertura científica de la arquitectura.

### 5. Gate

No se redactará ni corregirá Section 4 hasta que el autor apruebe o modifique esta estructura conceptual. Solo entonces se actualizarán el Plan Maestro y la estructura de trabajo y se generará un nuevo prompt operativo para IA de Redacción.

---

## English

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_SECTION4_RESTRUCTURE_PROPOSAL_V01
GOVERNING_DECISION = D-044
STATUS = PROPOSAL / AUTHOR_REVIEW_REQUIRED
CANONICAL_MASTER = ARTICLE_MASTER_V009
SECTION_4 = CONCEPTUALLY_REOPENED
DRAFTING_AI = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
```

Section 4 should explain how a concrete instantiation of the Section 3 architecture was experimentally evaluated. It should not define the experiment as an operational decision-support tool or turn Methods into a repository artifact inventory.

Proposed structure: 4.1 Experimental setting and scope; 4.2 Historical data and experimental dataset construction, with source/data collection, processing/curation, and partition construction/dataset composition; 4.3 Documentary corpus and evidence resource; 4.4 Partition validity and dependence controls; 4.5 Experimental system configuration and execution; 4.6 Evaluation framework and protocols, with candidate-retrieval, documentary-evidence, and controlled-explanation subsections; 4.7 Statistical and robustness analysis; and 4.8 Reproducibility resources.

The main prose should describe scientific objects, procedures, design decisions, and validity controls. SHA-256 values, internal paths, and physical filenames belong to manifests and reproducibility resources unless a concrete identifier is methodologically indispensable. The empirical evaluation remains bounded to the instantiated setting; architectural re-instantiation with other data, tariff depths/classes, or documentary corpora does not imply transfer of empirical performance.

Once this structure is approved, two editorial forward references in Section 3 must be adjusted: Section 3.5 should no longer promise hashes in Section 4, and Section 3.7 should no longer frame the reproducibility subsection as a narrative inventory of technical identities. These are editorial-coherence amendments, not a scientific reopening of the architecture.
