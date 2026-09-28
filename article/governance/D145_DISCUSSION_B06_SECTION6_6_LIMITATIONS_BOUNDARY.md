# D-145 — Discussion B06 / Section 6.6 limitations boundary

## Español

```text
DECISION = D-145
PHASE = DISCUSSION
BLOCK = DISCUSSION_B06_SECTION_6_6
SECTION = 6.6 LIMITATIONS
CANONICAL_MASTER = ARTICLE_MASTER_V028
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V028.md
CANONICAL_MASTER_MD_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
CANONICAL_MASTER_MD_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 67
PRIMARY_RESULTS_INPUTS = Sections 5.1-5.7
PRIMARY_METHOD_INPUTS = Sections 4.1, 4.3, 4.4, 4.7, 4.8
PRIMARY_DISCUSSION_INPUTS = Sections 6.1-6.5
PRIMARY_ARCHITECTURE_INPUT = Section 3.7
NEW_LITERATURE = PROHIBITED
NEW_EXPERIMENTAL_RESULTS = PROHIBITED
NEW_INFERENCE = PROHIBITED
LIMITATIONS = CONSOLIDATION_AND_INTERPRETIVE_BOUNDING / NOT_NEW_FINDINGS
EXTERNAL_VALIDITY = NOT_ESTABLISHED
LEGAL_VALIDITY = NOT_ESTABLISHED
HUMAN_VALIDATION = NOT_ESTABLISHED
DEPLOYMENT_READINESS = NOT_ESTABLISHED
CAUSAL_SAFETY_EFFECT = NOT_ESTABLISHED
FINAL_GAP = NOT_DEFINED
NOVELTY_CLAIM = PROHIBITED
CONCLUSION = NOT_AUTHORIZED
```

### Función científica de §6.6

La sección debe consolidar los límites que condicionan la interpretación del estudio sin introducir nuevos resultados ni convertir limitaciones conocidas en afirmaciones más fuertes que la evidencia. Debe cerrar Discussion delimitando de manera explícita qué puede y qué no puede inferirse del benchmark offline Chapter 87, del corpus documental congelado, de las evaluaciones de explicación y del estado actual de reproducibilidad.

### Limitaciones obligatorias

La redacción debe cubrir, de forma integrada y reader-facing, al menos los siguientes dominios:

1. **Muestra administrativa y alcance empírico.** La colección fue purposiva, restringida al contexto administrativo descrito y a Chapter 87/NANDINA-8. No es una muestra probabilística y no sustenta generalización a otras poblaciones, capítulos, jurisdicciones, profundidades arancelarias o regímenes.

2. **Dependencia y similitud residual.** La partición v0.2 elimina solapamiento de DAM e `id_unico` entre particiones, pero las SERIE dentro de una DAM no son automáticamente independientes. Persisten coincidencias exactas y near-duplicates entre declaraciones distintas. Estos controles reducen rutas específicas de leakage/dependencia, pero no establecen i.i.d. ni cuantifican por sí mismos el efecto causal de la similitud residual sobre el rendimiento.

3. **Composición del banco histórico.** EXP11A varió conjuntamente tamaño y composición, por lo que no identifica un efecto causal aislado del tamaño del banco. EXP11B H150/H200 es descriptivo sobre diez semillas emparejadas en el mismo EVAL y no permite inferencia a una superpoblación de semillas ni una conclusión general monotónica sobre aumentar el banco.

4. **No estimabilidad de objetos planificados.** EXP12 no estimó un efecto de diversidad histórica porque no produjo outputs de retrieval para las condiciones congeladas. La prevalencia de descripciones ambiguas/incompletas no fue estimable porque no existió una operacionalización caso-a-caso congelada. HE5 permanece inconclusa.

5. **Corpus documental y drift normativo.** El camino primario utilizó un corpus derivado de Decision 885 mientras Decision 906 ya había modificado NANDINA antes de los casos administrativos de 2026. La sensibilidad correctiva fue dependiente del método. La asociación exacta de código y la trazabilidad documental no establecen vigencia, suficiencia, corrección normativa sustantiva ni corrección jurídica para un caso concreto.

6. **Evaluación de explicación.** Solo 50 casos fueron evaluados cualitativamente. El evaluador fue un LLM-as-judge en rol experto, no humanos. El criterio de auditabilidad fue una rúbrica interna congelada del estudio; no constituye validación humana, aceptación experta ni validación jurídica. El mismatch entre instrucción de generación y esquema produjo 0/50 de schema compliance por una incompatibilidad de especificación y no debe interpretarse como 50 explicaciones sustantivamente inválidas. La trazabilidad estructural no garantiza verificabilidad, claridad, faithfulness causal ni utilidad experta.

7. **Arquitectura y generalización.** Configurabilidad e interfaces preservadas permiten definir una reinstanciación técnicamente coherente, pero no transfieren rendimiento, robustez, auditabilidad ni validez externa a otro escenario. La arquitectura no ha sido validada como deployment operativo ni como adjudicador legal autónomo.

8. **Reproducibilidad pública.** El snapshot público auditado contiene principalmente protocolos/contratos y configuración de ejemplo y todavía no materializa una reproducción de referencia completa de un comando desde clon limpio, incluyendo runner canónico, validadores/experiment runners completos, preset Chapter 87 congelado, lock de dependencias, outputs canónicos, datos administrativos redistribuibles o validación documentada en entorno limpio. Esta limitación del paquete debe distinguirse de la reproducibilidad conceptual/procedimental descrita en el artículo.

### Relaciones que deben permanecer explícitas

```text
DAM_DISJOINT_PARTITIONS != IID_OBSERVATIONS
RESIDUAL_SIMILARITY_DIAGNOSTICS != CAUSAL_EFFECT_ESTIMATE
EXP11A_SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
HE5 = INCONCLUSIVE
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
LLM_AS_JUDGE != HUMAN_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
REFERENCE_REPRODUCIBILITY_PACKAGE = INCOMPLETE_PUBLIC_SNAPSHOT
```

### Interpretaciones permitidas

- Los resultados describen un piloto offline interno y metodológicamente controlado en Chapter 87, no una estimación de desempeño poblacional externo.
- El agrupamiento por DAM mejora el control de partición e inferencia frente al snapshot histórico, pero no elimina toda dependencia ni similitud entre registros.
- La sensibilidad observada a bancos históricos y recursos normativos evidencia dependencia de configuración/composición en partes del análisis, sin autorizar causalidad general.
- La explicación puede ser estructuralmente trazable y aun así presentar verificabilidad o separación de evidencias limitadas.
- La reinstanciación futura requiere nueva validación empírica, documental y, cuando corresponda, jurídica/humana.
- El estado actual del paquete público limita la reproducción operativa inmediata desde un clon limpio y debe revalidarse antes de submission.

### Claims prohibidos

No afirmar ni implicar:

- que el benchmark representa la población aduanera peruana o internacional;
- que DAM-disjoint elimina toda dependencia o leakage;
- que los near-duplicates causaron una fracción específica del rendimiento;
- que aumentar el banco histórico mejora o empeora generalmente el desempeño;
- que Decision 885 vuelve inválidas todas las asociaciones o candidatos;
- que la asociación exacta de documento demuestra corrección jurídica;
- que el LLM-as-judge equivale a revisión humana o experta;
- que 56% de auditabilidad es una tasa operacional generalizable;
- que la arquitectura reduce hallucinations, mejora safety o garantiza auditabilidad operacional;
- que configurabilidad demuestra generalización, portabilidad de desempeño o deployment readiness;
- que el repositorio público ya proporciona reproducción completa one-command;
- novelty, first-ever, SOTA, superioridad o FINAL_GAP.

### Deuda editorial heredada

La deuda de terminología interna ya registrada en §6.2 no forma parte de B06. No se modifica silenciosamente durante esta redacción. Debe resolverse en un gate transversal específico antes del freeze final.

---

## English

Section 6.6 must consolidate the study's known validity and interpretation limits without creating new findings. It must cover the purposive Chapter-87 sample, residual dependence and near-duplicates, historical-bank composition sensitivity, non-estimable robustness objects, documentary/normative drift, the limited 50-case LLM-as-judge explanation evaluation, the separation between configurability and empirical generalization, legal/deployment boundaries, and the incomplete current public reproducibility snapshot.

All limitations must be reader-facing and tied to the claims they bound. No new literature, results, inference, novelty, superiority, causal mechanism, legal-validity claim, human-validation claim, or external-generalization claim is authorized. The inherited Section 6.2 terminology debt remains outside this block and must be handled in a separate transversal gate before final freeze.