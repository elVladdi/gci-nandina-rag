# D-045 — Author approval of Section 4 restructure and Structure V02

## Español

```text
DECISION_ID = D-045
DATE = 2026-09-24
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-044
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_SECTION4_RESTRUCTURE_PROPOSAL_V01.md@acb384221b5dfb72c701f9fc57dc32de6ece69c3
AUTHOR_DECISION = APPROVED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_GIT_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
AMENDMENT_SCOPE = SECTION_4_CONTROLLED_RESTRUCTURE
CANONICAL_MASTER = ARTICLE_MASTER_V009
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
SECTION_4 = RESTRUCTURED / AUTHOR_APPROVED / READY_FOR_ATOMIC_REDRAFTING
EXPERIMENTAL_DESIGN_B01 = ELIGIBLE_FOR_REOPENING_UNDER_STRUCTURE_V02
SECTION_3_BACKWARD_DEPENDENCIES = EDITORIAL_AMENDMENT_REQUIRED_DURING_CONTROLLED_REWRITE
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El autor aprueba la propuesta de reestructuración conceptual de Section 4. La estructura gobernante pasa a `KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, que conserva la organización previamente aprobada del artículo salvo la enmienda controlada de Section 4.

La Sección 4 queda organizada como sigue:

- 4.1 Experimental setting and scope / Entorno y alcance experimental;
- 4.2 Historical data and experimental dataset construction / Datos históricos y construcción de los datasets experimentales;
  - 4.2.1 Source and data collection / Fuente y recolección;
  - 4.2.2 Processing and curation / Procesamiento y curación;
  - 4.2.3 Partition construction and dataset composition / Construcción de particiones y composición;
- 4.3 Documentary corpus and evidence resource / Corpus documental y recurso de evidencia;
- 4.4 Partition validity and dependence controls / Validez de particiones y control de dependencia;
- 4.5 Experimental system configuration and execution / Configuración y ejecución experimental;
- 4.6 Evaluation framework and protocols / Marco y protocolos de evaluación;
  - 4.6.1 Candidate-retrieval evaluation;
  - 4.6.2 Documentary-evidence evaluation;
  - 4.6.3 Controlled-explanation evaluation;
- 4.7 Statistical and robustness analysis / Análisis estadístico y de robustez;
- 4.8 Reproducibility resources / Recursos de reproducibilidad.

Reglas vinculantes derivadas de la aprobación:

1. Section 4 explica cómo se evaluó experimentalmente una instanciación concreta de la arquitectura de Section 3; el experimento no se presenta como una herramienta operativa de apoyo a decisiones.
2. La procedencia de los datos históricos comienza por la fuente administrativa y el procedimiento real de recolección, no por el archivo intermedio.
3. La prosa publicable describe objetos, procedimientos, decisiones y controles científicos. SHA-256, rutas internas y nombres físicos de archivos se reservan a manifiestos/recursos de reproducibilidad salvo necesidad metodológica excepcional.
4. La antigua subsección autónoma `Target class space` desaparece: NANDINA de ocho dígitos/Chapter 87 forma parte de 4.1 y la composición de códigos representados pasa a 4.2.3.
5. Las evaluaciones de candidate retrieval, documentary evidence y controlled explanation se mantienen separadas pero se subordinan a 4.6 como protocolos de evaluación.
6. `evaluate/evaluar` es la fuerza epistémica preferida; `validate/validar` requiere criterio explícito adicional.
7. Configurabilidad/reinstanciación con otros bancos históricos, profundidades arancelarias, clases, jurisdicciones o corpus no equivale a transferencia de desempeño empírico.
8. Los dos forward references integrados en Section 3 que anticipaban hashes/inventarios técnicos en Section 4 deben corregirse de forma editorial y controlada durante la reescritura, sin reabrir la arquitectura científica.

La aprobación estructural no aprueba la prosa B01 previamente observada ni rehabilita `ARTICLE_MASTER_V010`. El master canónico sigue siendo `ARTICLE_MASTER_V009` hasta que un nuevo candidato conforme a Structure V02 supere auditoría y aprobación.

## English

The author approves the conceptual restructuring of Section 4. `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` becomes the governing structure, preserving the previously approved article organization except for the controlled Section-4 amendment.

Section 4 must present the offline experimental evaluation of a concrete Section-3 architecture instantiation; historical-data provenance must begin with the administrative source and actual collection process; publication-facing Methods must not be organized around repository paths, hashes, or filenames; the former standalone target-class-space subsection is removed; the three evaluation families remain distinct under one evaluation-framework section; reproducibility prose explains what can be reconstructed rather than narrating artifact fingerprints; and configurability must not be stated as empirical performance transfer.

The two integrated Section-3 forward references that anticipated hashes/artifact inventories in Section 4 require a controlled editorial amendment during the rewrite. This does not scientifically reopen Architecture.

The prior B01 prose remains unapproved for integration. `ARTICLE_MASTER_V009` remains canonical and `ARTICLE_MASTER_V010` remains suspended until a new candidate under Structure V02 passes the required gates.