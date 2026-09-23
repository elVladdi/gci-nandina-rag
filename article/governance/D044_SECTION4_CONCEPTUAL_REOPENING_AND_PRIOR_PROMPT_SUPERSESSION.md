# D-044 — Section 4 conceptual reopening and prior prompt supersession

## Español

```text
DECISION_ID = D-044
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-043
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_SECTION4_CONCEPTUAL_REAUDIT_V01.md@035b998f9f068fc2aa4d6c132ba95fdbef3927fc
AUTHOR_COMMENTED_SOURCE = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02(2).docx
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
CANONICAL_MASTER = ARTICLE_MASTER_V009
PROMPT_5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED_FOR_DRAFTING
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
SECTION_3_BACKWARD_DEPENDENCIES = AMENDMENT_REQUIRED_AFTER_SECTION4_REDESIGN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El autor amplió la observación desde la prosa de 4.2 hacia el enfoque de la Sección 4 completa. La revisión del Word comentado confirma que el problema no es únicamente la exposición de SHA, rutas o nombres de archivos: el texto actual mezcla el objeto experimental con una eventual herramienta de apoyo a decisiones y organiza parte de Methods alrededor de la trazabilidad técnica de artefactos en lugar de la lógica científica del experimento.

A partir de esta decisión, toda la Sección 4 queda bajo revisión conceptual. La IA Gestora debe reconstruir su función y estructura antes de generar un nuevo prompt de redacción. El nuevo diseño deberá presentar la evaluación experimental offline de una instanciación concreta de la arquitectura, explicar procedencia/adquisición y preparación de datos y corpus, particionamiento y controles, configuración y ejecución, protocolos de evaluación y límites de interpretación. La información de identidad técnica exhaustiva se reserva para recursos de reproducibilidad/manifiestos, salvo necesidad metodológica expresa.

La formulación «piloto no vinculante de apoyo a decisiones» no debe gobernar la nueva 4.1. El estudio puede describir la arquitectura como base reinstanciable para futuras herramientas de apoyo, pero el experimento es una evaluación del procedimiento/arquitectura, no un despliegue operacional. La terminología deberá conservar la fuerza epistémica del objetivo aprobado: «evaluar» es preferible a «validar» salvo soporte adicional.

La posibilidad de reinstanciar el procedimiento con otros bancos históricos, espacios de clases, profundidades arancelarias, jurisdicciones o corpus compatibles puede describirse como propiedad de configurabilidad/replicación metodológica. No debe convertirse en una afirmación de transferencia de desempeño empírico.

El prompt `article/prompts/5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION.md@e6165d65f44e42a023d1ac9f1a1dacc2f9972d3f` queda expresamente superado y no debe ejecutarse.

Asimismo, quedan registradas para enmienda coordinada dos dependencias ya integradas en Section 3: la anticipación de que Section 4 publicará hashes de evaluación y la anticipación de un inventario concreto de identidades de artefactos en 4.11. Estas frases se corregirán únicamente después de aprobar la nueva estructura de Section 4, para evitar parches locales incoherentes.

No se autoriza todavía la redacción de 4.3 ni de ningún bloque posterior.

## English

```text
DECISION_ID = D-044
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-043
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_SECTION4_CONCEPTUAL_REAUDIT_V01.md@035b998f9f068fc2aa4d6c132ba95fdbef3927fc
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
CANONICAL_MASTER = ARTICLE_MASTER_V009
PROMPT_5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED_FOR_DRAFTING
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
SECTION_3_BACKWARD_DEPENDENCIES = AMENDMENT_REQUIRED_AFTER_SECTION4_REDESIGN
```

The author broadened the observation from Section 4.2 prose to the framing of Section 4 as a whole. The commented Word confirms that the defect is not limited to SHA values, paths, or filenames: the current text partly conflates the experimental object with a future decision-support tool and organizes Methods around internal artifact traceability rather than the scientific logic of the experiment.

The complete Section 4 is therefore reopened for conceptual review. Before any new drafting prompt is issued, the lead scientific editor must redesign the section around the offline experimental evaluation of a concrete architecture instantiation, covering data/corpus provenance and acquisition, preparation, partition/control, concrete system configuration and execution, evaluation protocols, and bounded interpretation. Exhaustive technical artifact identity belongs in reproducibility resources/manifests unless explicitly methodologically necessary.

The phrase “non-binding decision-support pilot” must not govern the revised Section 4.1. The architecture may be described as re-instantiable as a basis for future decision-support tools, but the experiment itself is an evaluation of the procedure/architecture rather than an operational deployment. The epistemic strength of the approved objective must be preserved: “evaluate” is preferred to “validate” absent stronger evidence.

Re-instantiation with other historical banks, class spaces, tariff depths, jurisdictions, or compatible corpora may be described as configurability/methodological replication, not as evidence of empirical performance transfer.

The previously versioned narrow correction prompt is superseded and must not be executed. Two backward dependencies already integrated in Section 3—the expectation that Section 4 will publish evaluation hashes and that Section 4.11 will contain a concrete artifact-identity inventory—are recorded for coordinated amendment only after the revised Section 4 structure is approved.

No drafting of Section 4.3 or later blocks is authorized at this point.