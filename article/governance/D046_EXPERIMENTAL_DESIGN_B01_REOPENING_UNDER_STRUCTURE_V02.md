# D-046 — Experimental Design B01 reopening under Structure V02

## Español

```text
DECISION_ID = D-046
DATE = 2026-09-24
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-045
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_GIT_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
INHERITED_CITATION_COMMENTS = 40
EXPERIMENTAL_DESIGN_B01 = REOPENED / AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_3_FORWARD_REFERENCE_EDITORIAL_AMENDMENTS_PLUS_SECTION_4_1_AND_4_2_1_TO_4_2_3
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / RESERVED_FOR_FUTURE_APPROVED_INTEGRATION
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Se reabre Experimental Design B01 bajo la estructura V02 aprobada por el autor. La versión B01 previamente observada no es baseline de redacción. La IA de Redacción debe partir del master canónico `ARTICLE_MASTER_V009` y de su DOCX exacto correspondiente.

### Alcance único autorizado

1. Corregir únicamente las dos referencias editoriales forward de Section 3 registradas por D-044/D-045:
   - en 3.5, eliminar la promesa de que Section 4 publicará hashes como parte de la narrativa metodológica;
   - en 3.7, eliminar/reformular la expectativa de que la subsección de reproducibilidad sea un inventario narrativo de identidades técnicas.
   Estas modificaciones no pueden alterar la arquitectura científica, el orden funcional, la autoridad de componentes ni las fronteras ya aprobadas.

2. Reescribir únicamente:
   - 4.1 `Experimental setting and scope` / `Entorno y alcance experimental`;
   - 4.2 `Historical data and experimental dataset construction` / `Datos históricos y construcción de los datasets experimentales`;
   - 4.2.1 `Source and data collection` / `Fuente y recolección`;
   - 4.2.2 `Processing and curation` / `Procesamiento y curación`;
   - 4.2.3 `Partition construction and dataset composition` / `Construcción de particiones y composición`.

No se autoriza redactar 4.3 ni subsecciones posteriores.

### Reglas editoriales vinculantes

- El objeto narrativo es la evaluación experimental offline de una instanciación concreta de la arquitectura, no una herramienta operativa.
- `evaluate/evaluar` es preferible a `validate/validar` salvo criterio de validación explícito y sustentado.
- 4.2.1 comienza por la fuente administrativa y el proceso real de recolección. El archivo Excel intermedio no gobierna la explicación de procedencia.
- Deben diferenciarse claramente recolección, transformación automatizada, curación y construcción de particiones.
- El cuerpo principal no listará SHA-256, rutas internas, nombres de scripts, nombres de hojas o nombres físicos de CSV salvo necesidad metodológica excepcional demostrada.
- Los conteos de composición de datasets son elegibles para Methods; las métricas de desempeño no lo son.
- La separación por DAM y el no solapamiento entre particiones pueden describirse como decisiones/controles de diseño; el análisis detallado de leakage, duplicados y near-duplicates queda principalmente en 4.4.
- La posibilidad de reinstanciar la arquitectura con otros datos, clases, profundidades o corpus no equivale a generalización empírica.

### Fuentes

La ejecución debe verificar directamente:

- `SRC-01`: formulaciones aprobadas del proyecto de tesis, cuando se requiera para fuerza epistémica y alcance;
- `SRC-02`: `Anexo_1_NANDINA_LLM_RAG_v13.docx` como metodología operativa vigente, incluida fuente, periodo, criterios de selección y acopio manual;
- `SRC-03`: Plan Maestro experimental vivo en modo de solo lectura;
- artefactos técnicos congelados identificados en `SOURCE_REGISTRY.md` para composición, procesamiento, curación y particiones v0.2;
- `KBS_EWG_34_V01` y la reauditoría editorial KBS-34 ya registrada para el nivel de detalle publicable.

Una respuesta previa de otra IA, la prosa observada B01 V02 o la tesis preliminar no sustituyen estas fuentes primarias.

### Stop conditions

Detenerse si:

- el DOCX baseline exacto no coincide;
- `SRC-03` presenta un cambio material en hechos usados por B01;
- `SRC-02` exacto no está disponible para verificar procedencia/recolección;
- existe contradicción irresuelta entre fuentes gobernantes sobre fuente, periodo, criterios, conteos, unidades o construcción de particiones;
- una afirmación no puede verificarse sin inventar/reconciliar silenciosamente.

La IA de Redacción no puede promover V010, declarar B01 aprobado/cerrado/integrado ni abrir 4.3.

## English

Experimental Design B01 is reopened under the author-approved Structure V02. The previously observed B01 prose is not a drafting baseline. Drafting must start from canonical `ARTICLE_MASTER_V009` and its exact corresponding DOCX.

Authorized scope is limited to the two editorial Section-3 forward-reference amendments recorded by D-044/D-045 plus Sections 4.1, 4.2, and 4.2.1–4.2.3. Section 4.3 and later remain closed.

The Methods narrative must present an offline experimental evaluation of a concrete architecture instantiation, begin historical-data provenance with the administrative source and actual collection process, distinguish collection from automated processing/curation/partitioning, keep exhaustive technical identifiers out of publication-facing prose, and preserve the boundary between configurability and empirical generalization.