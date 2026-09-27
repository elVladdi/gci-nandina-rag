# Experimental Design B07 V01 — Section 4.8

```text
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
VERSION = V01
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
GOVERNING_DECISION = D-080
GROUND_TRUTH_DECISION = D-079
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MASTER_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
BASELINE_MASTER_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
REPRO_MAIN_HEAD_READ = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE_READ = 078a85255fa1f3234b4f7ed51ef2660b903d486e
AUTHORIZED_SCOPE = SECTION_4_8_ONLY
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

## 4.8. Reproducibility resources

The experimental-development repository and the public reproducibility repository serve different functions. The development repository preserves the experimental history, internal artifacts, diagnostics, and frozen sources used during the campaign. The public gci-nandina-rag-reproducibility repository is intended as the clean scientific package for reference reproduction and external replication; it is therefore described here separately from the development history.

In the audited public snapshot, the materialized resources are primarily protocol and contract documentation. They define the experimental workflow, the logical data contract, tariff-hierarchy and nomenclature requirements, normative-corpus compatibility, provenance and redistribution rules, and the documented reference, custom, and synthetic usage modes. The repository also contains an example configuration for compatible user-provided data. Its documentation specifies the metadata that a reproducible run or release should record, including seeds, input and configuration hashes, software and framework versions, parameters, environment information, model and prompt identifiers when applicable, execution metadata, and output identities. These resources support preparation and traceable specification of a compatible run, but they do not by themselves constitute a complete computational reference release.

At this snapshot, the public package does not yet materialize the canonical reference-reproduction runner, the executable validation and experiment runners shown as target interfaces, a frozen Chapter-87 reference preset, a dependency lock, canonical reference outputs, redistributed administrative reference data, or a documented clean-environment validation of the final release. Consequently, the command examples in the repository describe intended interfaces rather than a current guarantee of one-command reproduction from a fresh clone. This limitation concerns the present state of the public package and does not alter the experimental procedures already executed and audited in the development repository.

The repository distinguishes reference reproduction from external replication. Reference reproduction is defined as rerunning a frozen study preset with the same inputs, configuration, and expected outputs once those release artifacts are materialized. External replication applies the protocol to compatible independent data and produces its own manifest and result set; numerical agreement with the reference experiment is not required. The dataset, chapter scope, tariff depth, jurisdiction, and compatible normative corpus can therefore be reconfigured under the documented contracts. This configurability is a property of the design and does not demonstrate empirical generalization beyond the evaluated Chapter-87 setting.

Public redistribution is limited to artifacts whose status permits publication. Administrative reference CSVs are not made public merely because they exist in the development repository; restricted inputs remain outside the public package, with expected hashes, schemas, and reconstruction or placement instructions documented when appropriate. An external replication must instead record the provenance, versions and hashes of its own inputs, the grouping unit, target classification level, and applicable disclosure restrictions. Because this description is bound to a versioned public-repository snapshot, the availability of scripts, presets, redistributable inputs, manifests, and clean-environment validation will be rechecked against the public repository immediately before submission.

## Part II — Spanish semantic-control mirror

## 4.8. Recursos de reproducibilidad

El repositorio de desarrollo experimental y el repositorio público de reproducibilidad cumplen funciones diferentes. El repositorio de desarrollo conserva el historial experimental, los artefactos internos, los diagnósticos y las fuentes congeladas utilizadas durante la campaña. El repositorio público gci-nandina-rag-reproducibility está destinado al paquete científico limpio para la reproducción del estudio de referencia y la replicación externa; por ello se describe aquí de forma separada del historial de desarrollo.

En el snapshot público auditado, los recursos materializados son principalmente documentación de protocolos y contratos. Estos documentos definen el flujo experimental, el contrato lógico de datos, los requisitos de jerarquía y nomenclatura arancelaria, la compatibilidad del corpus normativo, las reglas de procedencia y redistribución y los modos de uso documentados reference, custom y synthetic. El repositorio también contiene una configuración de ejemplo para datos propios compatibles. Su documentación especifica los metadatos que una corrida o release reproducible debería registrar, incluidas las semillas, los hashes de entradas y configuraciones, las versiones de software y del framework, los parámetros, la información del entorno, los identificadores de modelo y prompt cuando correspondan, los metadatos de ejecución y las identidades de las salidas. Estos recursos permiten preparar y especificar de forma trazable una corrida compatible, pero no constituyen por sí solos una release computacional completa de referencia.

En este snapshot, el paquete público todavía no materializa el runner canónico de reproducción del estudio de referencia, los runners ejecutables de validación y experimentación mostrados como interfaces objetivo, un preset de referencia congelado para el Capítulo 87, un lock de dependencias, resultados canónicos de referencia, datos administrativos de referencia redistribuidos ni una validación documentada en un entorno limpio de la release final. En consecuencia, los ejemplos de comandos del repositorio describen interfaces previstas y no una garantía actual de reproducción con un único comando desde un fresh clone. Esta limitación corresponde al estado presente del paquete público y no modifica los procedimientos experimentales ya ejecutados y auditados en el repositorio de desarrollo.

El repositorio distingue la reproducción del estudio de referencia de la replicación externa. La reproducción de referencia se define como volver a ejecutar un preset congelado del estudio con las mismas entradas, configuración y salidas esperadas una vez que esos artefactos de release estén materializados. La replicación externa aplica el protocolo a datos independientes compatibles y produce su propio manifest y conjunto de resultados; no requiere concordancia numérica con el experimento de referencia. Por tanto, el dataset, el alcance por capítulos, la profundidad arancelaria, la jurisdicción y un corpus normativo compatible pueden reconfigurarse bajo los contratos documentados. Esta configurabilidad es una propiedad de diseño y no demuestra generalización empírica fuera del escenario evaluado del Capítulo 87.

La redistribución pública se limita a los artefactos cuyo estatus permite su publicación. Los CSV administrativos de referencia no se hacen públicos por el solo hecho de existir en el repositorio de desarrollo; las entradas restringidas permanecen fuera del paquete público y, cuando corresponde, se documentan sus hashes esperados, esquemas e instrucciones de reconstrucción o colocación. Una replicación externa debe registrar, en cambio, la procedencia, las versiones y los hashes de sus propias entradas, la unidad de agrupamiento, el nivel objetivo de clasificación y las restricciones de divulgación aplicables. Dado que esta descripción queda vinculada a un snapshot versionado del repositorio público, la disponibilidad de scripts, presets, entradas redistribuibles, manifests y validación en entorno limpio se volverá a verificar directamente en el repositorio público inmediatamente antes del envío del manuscrito.
