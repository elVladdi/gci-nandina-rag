# D-141 — Discussion B05 / Section 6.5 configurability and transfer boundary

## Español

```text
DECISION = D-141
PHASE = DISCUSSION
BLOCK = DISCUSSION_B05_SECTION_6_5
SECTION = 6.5 CONFIGURABILITY AND TRANSFER CONDITIONS
CANONICAL_MASTER = ARTICLE_MASTER_V027
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V027.md
CANONICAL_MASTER_MD_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
CANONICAL_MASTER_MD_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 66
PRIMARY_ARCHITECTURE_INPUT = Section 3.7
PRIMARY_REPRODUCIBILITY_INPUT = Section 4.8
PRIMARY_CONCEPTUAL_INPUT = Section 2.5
PRIMARY_DISCUSSION_INPUTS = Sections 6.1-6.4
SUPPORTING_SCOPE_INPUTS = Introduction and Section 4.1
NEW_LITERATURE = PROHIBITED
NEW_EXPERIMENTAL_RESULTS = PROHIBITED
NEW_INFERENCE = PROHIBITED
CONFIGURABILITY = DESIGN_PROPERTY / INTERFACE_CONDITIONS
TRANSFER = CONDITIONAL_REINSTANTIATION / NOT_PERFORMANCE_TRANSFER
REFERENCE_REPRODUCTION = SAME_IDENTIFIED_STUDY_CONFIGURATION_AS_CLOSELY_AS_AVAILABLE_ARTIFACTS_PERMIT
EXTERNAL_REPLICATION = INDEPENDENT_DATA_OR_REPLACEMENT_RESOURCES_WITH_FUNCTIONAL_INTERFACES_PRESERVED
REPRODUCTION != EXTERNAL_REPLICATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
INTERFACE_COMPATIBILITY != PERFORMANCE_GENERALIZATION
REINSTANTIATION != DEPLOYMENT_READINESS
REINSTANTIATION != LEGAL_VALIDITY
CHAPTER87_RESULTS = NOT_TRANSFERABLE_BY_ASSUMPTION
NOVELTY_CLAIM = PROHIBITED
FINAL_GAP = NOT_DEFINED
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

### Función científica de §6.5

La sección debe explicar qué partes del framework pueden sustituirse o reconfigurarse y qué condiciones deben preservarse para mantener el significado funcional de la arquitectura. Debe presentar la transferibilidad únicamente como posibilidad de reinstanciar el procedimiento bajo interfaces y procedencia compatibles, no como evidencia de que los resultados empíricos del Capítulo 87 se mantendrán en otro capítulo, jurisdicción, nivel arancelario, banco histórico, corpus documental, modelo o población.

### Ground truth autorizado

La arquitectura permite sustituir, en principio, un banco histórico etiquetado, un espacio de códigos objetivo, un corpus documental compatible y componentes de implementación cuando se conservan las siguientes condiciones:

1. La entrada comercial puede convertirse en una representación de consulta reproducible.
2. Los registros históricos permanecen vinculados a códigos asignados y a procedencia recuperable.
3. El recuperador histórico devuelve resultados ordenados y trazables que permiten construir candidatos únicos y fijar el Top-3 antes de cualquier evidencia documental o generación.
4. La etapa documental mantiene cada evidencia vinculada al candidato fijo correspondiente y a una fuente identificable/versionada.
5. La construcción de contexto conserva, por candidato, código, posición fija, soporte histórico, evidencia documental y procedencia.
6. El generador recibe el conjunto fijo y permanece restringido a explicación; una sustitución de modelo o estrategia de prompting solo es compatible si no puede alterar membresía u orden del Top-3 en el flujo primario.
7. Los recursos que afectan materialmente una ejecución deben ser identificables y versionables cuando corresponda: datos, corpus, código de procesamiento/recuperación, configuraciones, modelo, instrucciones de generación y otros recursos necesarios para repetir o comparar una ejecución.
8. Un corpus documental alternativo debe ser compatible con el espacio de códigos de la instancia y debe registrar versión/procedencia. Su autoridad, vigencia y adecuación normativa deben validarse para la nueva instancia; la compatibilidad técnica no demuestra corrección jurídica.

### Reproducción y replicación

La discusión puede conservar la convención metodológica ya establecida en el manuscrito: la reproducción de referencia busca reconstruir la instancia evaluada identificada con los mismos insumos/configuración tan estrechamente como permitan los artefactos disponibles; una replicación externa puede emplear datos independientes o recursos sustitutos manteniendo las interfaces funcionales y generando su propio manifiesto/resultados. Esta distinción es una convención operativa del estudio, no una taxonomía universal.

### Estado del paquete público de reproducibilidad

Puede mencionarse de forma breve y reader-facing que el snapshot público auditado materializa principalmente documentación de protocolos/contratos y una configuración de ejemplo, pero todavía no garantiza reproducción de referencia de un solo comando desde un clon limpio. No convertir esta condición en una afirmación de que la arquitectura no puede reinstanciarse; es una limitación del estado actual del paquete público, que se consolidará en §6.6 y end matter.

### Interpretaciones permitidas

- La separación de interfaces reduce el acoplamiento entre recursos concretos y funciones del pipeline, lo que permite definir condiciones explícitas de sustitución/reinstanciación.
- La compatibilidad de una nueva instancia depende de preservar orden de autoridad, procedencia e interfaces, no de usar exactamente BM25, NANDINA, Chapter 87, Decision 885 o qwen2.5:7b-instruct.
- Cambiar datos, código objetivo, profundidad arancelaria, jurisdicción o corpus documental requiere reconstruir y validar los recursos correspondientes; no hereda automáticamente los resultados observados.
- Reproducibilidad de la instancia evaluada y replicación externa son objetivos distintos.

### Claims prohibidos

No afirmar ni implicar:

- generalización empírica demostrada fuera del Capítulo 87;
- portabilidad de rendimiento, equivalencia de métricas o mantenimiento del Top-k en otra instancia;
- robustez universal a cambio de dominio, jurisdicción o nomenclatura;
- que la compatibilidad documental garantiza vigencia, pertinencia, suficiencia o corrección jurídica;
- despliegue operativo, readiness, aceptación humana o sustitución experta;
- que el repositorio público actual constituye una release computacional completa si eso no ha sido revalidado;
- novelty, first-ever, SOTA, superioridad general o FINAL_GAP.

### Control editorial

§6.5 debe interpretar condiciones de transferencia sin repetir extensamente §3.7 o §4.8. Debe usar prosa científica reader-facing conforme a KBS, MWDP, SPCCR y D-136. No deben filtrarse IDs de decisiones, nombres de gates, hashes, nombres de prompts/responses, códigos internos de auditoría, etiquetas de experimento ni otra terminología de gobernanza al texto publicable.

La sección debe mantenerse concreta: recurso reemplazable → condición de interfaz/procedencia → qué conserva funcionalmente → qué NO permite inferir.

### Citas y Word

No se autoriza nueva literatura ni nuevas ocurrencias de cita en §6.5. Deben conservarse exactamente los 48 comentarios de citas heredados y 0 tracked changes. El Word debe editarse directamente desde el DOCX canónico B04 V02, nunca reconstruirse desde Markdown.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

---

## English

Section 6.5 must discuss configurability and transfer only as conditional re-instantiation under preserved interfaces, provenance, and component authority. The architecture can in principle accept a different labeled historical bank, target code space, compatible documentary corpus, and replaceable implementation components when the query, ranking, candidate fixation, candidate-linked evidence, context provenance, and explanation-only generator interfaces remain intact.

Configurability is a design property, not evidence of empirical generalization. Interface compatibility does not transfer Chapter-87 performance, legal validity, deployment readiness, human acceptance, or robustness to another jurisdiction, tariff depth, dataset, corpus, model, or population. Reference reproduction and external replication must remain distinct objectives. No new literature, results, inference, citation occurrences, or claims are authorized. Discussion §6.6 and the Conclusion remain closed.