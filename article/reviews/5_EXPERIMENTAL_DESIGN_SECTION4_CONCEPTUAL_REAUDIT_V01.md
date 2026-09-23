# Experimental Design — Section 4 conceptual reaudit V01

## Español

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_SECTION4_CONCEPTUAL_REAUDIT_V01
SCOPE = SECTION_4_COMPLETE_STRUCTURE_AND_CURRENT_DRAFTED_TEXT
SOURCE_WORD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02(2).docx / AUTHOR-COMMENTED COPY
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V009
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
PREVIOUS_NARROW_4_2_CORRECTION_PROMPT = SUPERSEDED / DO_NOT_EXECUTE
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
SCIENTIFIC_FACTS_ALREADY_VERIFIED = PRESERVED_UNLESS_REAUDIT_FINDS_CONTRADICTION
```

### 1. Dictamen general

La revisión de los comentarios del autor muestra que el problema de la Sección 4 no se limita a la presencia de SHA-256, rutas y nombres de archivos. Existe un problema de enfoque más amplio: el diseño experimental está siendo narrado en varios pasajes como si el objeto evaluado fuera ya una herramienta operativa de apoyo a decisiones y como si la función principal de Methods fuera documentar exhaustivamente la trazabilidad interna de los artefactos. El objeto correcto es la evaluación experimental offline de una instanciación concreta de la arquitectura/procedimiento definido en la Sección 3.

La Sección 4 debe responder, en primer término, qué instanciación se evaluó, con qué datos y corpus se construyó, cómo se prepararon y particionaron esos recursos, cómo se configuraron los componentes de la arquitectura, qué protocolos de evaluación se aplicaron y bajo qué límites se interpretan los resultados. El eventual uso de una implementación derivada como herramienta de apoyo a decisiones es una aplicación posterior; no debe confundirse con el experimento mismo.

### 2. Observaciones al texto ya redactado

#### O4-01 — 4.1 confunde experimento con herramienta/piloto de apoyo a decisiones

La formulación «piloto no vinculante de apoyo a decisiones» no es una buena caracterización del objeto experimental. «No vinculante» introduce una advertencia jurídico-operativa antes de establecer con claridad qué se evalúa y resulta retórico/redundante frente a la posterior delimitación de que no existe despliegue operativo ni adjudicación jurídica.

La formulación futura debe presentar 4.1 como una evaluación computacional offline de una instanciación concreta de la arquitectura para recomendación de subpartidas a partir de descripciones comerciales. Debe explicar que NANDINA a ocho dígitos, el Capítulo 87 y el corpus normativo peruano son restricciones de la instanciación experimental, no propiedades universales de la arquitectura.

El verbo editorial preferido es «evaluar», coherente con el objetivo aprobado. No debe elevarse automáticamente a «validar» si ello implica una fuerza epistémica mayor que la evidencia disponible.

#### O4-02 — la frontera operacional está sobrerrepresentada

Es correcto dejar explícito que el experimento no constituye clasificación oficial ni despliegue operativo, pero esa frontera debe aparecer como delimitación breve del alcance, no como el eje retórico de 4.1. El foco debe estar en el objeto experimental, las unidades, los recursos y las condiciones bajo las que se evalúa la arquitectura.

#### O4-03 — 4.2.1 omite la historia científicamente relevante de adquisición de datos

La redacción actual comienza desde el workbook disponible y una reconstrucción forense de su procesamiento. Ese punto de entrada desplaza información metodológicamente más importante: los registros fueron obtenidos mediante consulta administrativa y acopio manual desde Aduanet/SUNAT, bajo criterios y periodo definidos, y después fueron transformados mediante un proceso automatizado en Python hacia una representación por SERIE apta para el experimento.

La procedencia científica debe describirse desde la fuente administrativa y el procedimiento de recolección, no desde la ubicación física del archivo intermedio.

#### O4-04 — trazabilidad técnica interna ocupa el lugar de la metodología

SHA-256, rutas relativas, nombres físicos de archivos, índices de worksheet y otros identificadores internos deben quedar fuera de la prosa principal salvo que un identificador concreto sea indispensable para comprender una operación científica. Esos elementos pertenecen al repositorio de reproducibilidad, manifiestos o material suplementario.

#### O4-05 — 4.2.2 «Espacio de clases objetivo» está mal enfocado

La subsección mezcla tres objetos diferentes: delimitación experimental a NANDINA de ocho dígitos/Capítulo 87, composición observada de los datasets y control de dependencia por DAM. La justificación metodológica de la delimitación debe quedar vinculada al alcance de la instanciación; la composición del histórico/desarrollo/evaluación debe presentarse como composición de datos, preferiblemente de forma compacta o tabular; y DAM como unidad de agrupamiento pertenece a particionamiento/control de dependencia.

Los conteos de 66/9/42 códigos son resultados descriptivos de composición, no la explicación principal del «espacio de clases».

#### O4-06 — 4.2.3 contiene detalle de implementación de bajo valor editorial

Las operaciones que afectan semánticamente la construcción del dato sí deben explicarse: cómo una DAM se transforma en registros por SERIE, cómo se forma la descripción comercial, qué campos son obligatorios, qué reglas de curación se aplican, cómo se tratan duplicados/conflictos y qué unidad identificable se conserva. En cambio, detalles como espacios no separables, nombres de columnas técnicas o nombres internos de claves solo deben mantenerse si afectan la reproducibilidad científica del procedimiento y no pueden describirse con terminología metodológica más clara.

#### O4-07 — 4.2.4 debe describir particiones/composición, no inventario de archivos

La información científicamente pertinente es el tamaño y composición de los tres conjuntos, su función experimental y la regla de separación por DAM/identificador de SERIE. Los nombres físicos de CSV y sus hashes no deben estructurar la subsección. La identidad técnica exacta debe delegarse al repositorio/manifiesto de reproducibilidad.

### 3. Observaciones a la estructura completa 4.1–4.11

La estructura completa debe quedar observada antes de redactar 4.3 en adelante. Las subsecciones actuales cubren contenidos necesarios, pero su organización todavía refleja una lógica de inventario técnico y de control interno más que la secuencia científica del experimento.

La siguiente revisión estructural debe comprobar, como mínimo, que Section 4 siga una progresión experimental reconocible:

1. alcance e instanciación experimental;
2. construcción de los recursos de entrada: banco histórico y corpus documental/normativo;
3. preparación, curación y particionamiento de los datos, con control de dependencia y leakage;
4. configuración concreta de los componentes de la arquitectura y protocolo de ejecución;
5. protocolos y métricas de evaluación por función/RQ;
6. análisis estadístico autorizado y análisis de sensibilidad/validez cuando corresponda;
7. reproducibilidad descrita a nivel de recursos disponibles y condiciones de reconstrucción, sin convertir Methods en un listado de artefactos internos.

No se fija todavía una numeración definitiva de subsecciones. La estructura 4.1–4.11 vigente queda bajo revisión conceptual hasta que se reconstruya contra el objetivo del artículo, el diseño experimental real, las fuentes primarias y el patrón editorial KBS-34.

### 4. Reinstanciación y alcance de transferencia

El artículo debe dejar claro que la arquitectura/procedimiento está diseñada para poder reinstanciarse con otros bancos históricos, espacios de clases, profundidades arancelarias y corpus documentales compatibles cuando se satisfagan las interfaces y controles de procedencia correspondientes. Esto permite explicar cómo el procedimiento podría utilizarse como base para construir futuras herramientas de apoyo a decisiones en otros contextos.

Sin embargo, esa propiedad de diseño no autoriza a afirmar que los resultados empíricos observados en Chapter 87 se transfieren automáticamente a diez dígitos, a todas las clases, a otras jurisdicciones o a otros corpus. La formulación debe preservar la regla `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### 5. Dependencias hacia atrás detectadas en Section 3

La reauditoría detecta dos frases ya integradas en Architecture B02 que inducen el mismo exceso de detalle y deben quedar registradas para corrección coordinada cuando se rediseñe Section 4:

- Section 3.5 indica que «los parámetros y hashes utilizados en la evaluación se especifican en la Sección 4»;
- Section 3.7 anticipa que Section 4.11 registra «el inventario concreto de artefactos, sus identidades...».

Estas frases no invalidan la arquitectura científica, pero ya no son compatibles con la nueva regla editorial de separar prosa metodológica de inventario técnico. No deben corregirse aisladamente antes de definir la nueva estructura de Section 4, porque su redacción final depende de dónde quede ubicada la información de reproducibilidad.

### 6. Estado operativo

No debe entregarse a la IA de Redacción el prompt `5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION.md`. Ese prompt corregía únicamente 4.2 y queda superado por esta revisión conceptual más amplia.

Antes de emitir un nuevo prompt de redacción, la IA Gestora debe realizar una reestructuración editorial completa de Section 4 contra: (i) objetivo/hipótesis aprobados, (ii) fuentes experimentales primarias, (iii) tesis/Anexo como evidencia de adquisición y procesamiento, (iv) KBS_EWG_34_V01 y los 34 artículos de referencia, y (v) dependencias ya integradas de Section 3.

## English

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_SECTION4_CONCEPTUAL_REAUDIT_V01
SCOPE = COMPLETE_SECTION_4_STRUCTURE_AND_CURRENT_DRAFTED_TEXT
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V009
SECTION_4 = REOPENED / CONCEPTUAL_REVIEW_REQUIRED
EXPERIMENTAL_DESIGN_B01 = REVISION_REQUIRED
PREVIOUS_NARROW_4_2_CORRECTION_PROMPT = SUPERSEDED / DO_NOT_EXECUTE
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
```

The author's comments reveal a broader framing problem than the previously identified SHA/path disclosure issue. Section 4 currently tends to describe the evaluated object as an operational decision-support pilot and to use publication prose as a technical artifact inventory. The correct object is the offline experimental evaluation of a concrete instantiation of the architecture/procedure defined in Section 3.

Section 4 must foreground the evaluated instantiation, data and documentary-resource acquisition, preparation and partitioning, system configuration, execution and evaluation protocols, and bounded interpretation of the results. A future implementation may support decision making, but the experiment itself is not an operational decision-support tool.

The historical-data narrative must begin from the administrative source and manual collection process, followed by automated transformation into series-level records, rather than from a workbook path and forensic file identity. SHA values, internal paths and filenames belong to reproducibility manifests/resources unless methodologically indispensable. The current target-class subsection also conflates experimental scope, observed dataset composition and dependence control and must be restructured.

The complete 4.1–4.11 outline is therefore reopened for conceptual review before any further drafting. The final organization must follow a recognizable experimental sequence and keep technical artifact identity separate from publication-facing Methods prose. Configurability to other class spaces, tariff depths, jurisdictions or compatible documentary corpora may be stated as a design/re-instantiation property, but not as empirical performance transfer.

Two backward dependencies in Section 3 must also be corrected in coordination with the Section 4 redesign: the statement that evaluation hashes will be specified in Section 4 and the statement that Section 4.11 will contain a concrete artifact-identity inventory. These do not invalidate the architecture but are no longer editorially compatible with the revised boundary.

The previously versioned narrow 4.2 correction prompt is superseded and must not be executed. A new drafting prompt may be issued only after a complete Section 4 structural and evidential redesign is audited and authorized.