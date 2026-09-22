# Experimental Design B01 — KBS-34 artifact-disclosure reaudit V01

## Español

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_B01_KBS34_ARTIFACT_DISCLOSURE_REAUDIT_V01
BLOCK = EXPERIMENTAL_DESIGN_B01 / SECTION_4_2
REVIEWER = IA_GESTORA
GOVERNING_DECISION = D-043
EDITORIAL_REFERENCE = KBS_EWG_34_V01
CORPUS = 34 KBS OPEN-ACCESS ARTICLES / 2026 / VOLUMES 341-352
CURRENT_TEXT = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02
SCIENTIFIC_FACTS = PRESERVED
KBS_EDITORIAL_FIT = FAIL_REQUIRES_REVISION
ARTIFACT_SHA_AS_REPRODUCIBILITY_IDENTIFIER_OBSERVED = 0/34
SHA_OR_CHECKSUM_TERM_OTHER_CONTEXT = 1/34 / CRYPTOGRAPHIC_OPERATION_ONLY
CLEAR_METHOD_RELEVANT_FILENAME_OR_PATH_USE = 4/34
CURRENT_SECTION_4_2_SHA_DISCLOSURE = EXCESSIVE / REMOVE
CURRENT_SECTION_4_2_INTERNAL_PATH_DISCLOSURE = EXCESSIVE / REMOVE
CURRENT_SECTION_4_2_FILENAME_DISCLOSURE = REMOVE_UNLESS_METHOD_NECESSARY
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
AUTHOR_APPROVAL_GATE = CLOSED_PENDING_CORRECTION
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
```

### 1. Hallazgo principal

La auditoría científica previa verificó correctamente los hechos experimentales, pero la auditoría editorial fue insuficiente: confundió trazabilidad técnica completa con el nivel de detalle apropiado para la prosa publicable de KBS. Section 4.2 debe documentar procedencia, selección, preparación, curación, composición, versionado metodológicamente relevante y función de los datos; no necesita reproducir identificadores internos destinados al control del repositorio.

La versión V02 introduce, entre otros, la ruta `data/Series - Descripciones.xlsx`, su SHA-256, las rutas completas de los tres CSV de histórico/desarrollo/evaluación y un SHA-256 para cada uno. Esos datos son útiles para manifiestos y auditoría de reproducibilidad, pero no son necesarios para que el lector comprenda el método ni la composición de las particiones.

### 2. Verificación directa del corpus KBS-34

Se revisaron los 34 PDF que sustentan `KBS_EWG_34_V01` con búsquedas textuales dirigidas a `SHA-256`, `SHA256`, `checksum`, nombres de archivos de datos/código y patrones de rutas.

- En 33/34 no aparece `SHA-256`, `SHA256` ni `checksum`.
- El único artículo con esos términos, *Next-Gen metamorphism: Analyzing the potential of LLM-driven knowledge-based malware evasion*, usa SHA-256 como algoritmo criptográfico de derivación de claves y `checksum` como comportamiento del malware; no publica hashes de datasets o artefactos para identificarlos reproduciblemente.
- Por tanto, no se observó en el corpus ningún caso equivalente a listar SHA-256 de datasets/archivos dentro de la prosa metodológica: `0/34`.

Los nombres concretos de archivos o rutas sí aparecen de forma excepcional cuando son parte del objeto metodológico descrito. Casos claros observados:

1. *Automating data-driven modeling and analysis for engineering applications using large language model agents* nombra artefactos como `model.py`, `train_ensemble.py` y `metrics.json` porque el agente debe generarlos, repararlos o validarlos como parte explícita del procedimiento.
2. *HuddsTrafficFL* nombra CSV y scripts porque los archivos corresponden a componentes definidos del benchmark y una tabla explica el contenido de cada archivo.
3. *iTransPASOH* nombra CSV concretos porque constituyen las muestras seleccionadas para un protocolo de evaluación computacional específico.
4. *Metric-privacy-inspired noise calibration...* muestra `dp_fixed_clipping.py` y su estructura de ubicación en un apéndice porque la contribución incluye una modificación concreta del framework Flower que el lector debe localizar.

Estos casos no justifican trasladar al cuerpo de Section 4.2 rutas internas o hashes cuyo único propósito es identificar artefactos del repositorio. El patrón dominante es describir datos, selección, proceso y configuración; cuando existe un repositorio público, su acceso se comunica mediante enlace/availability/reproducibility material, no mediante una lista de fingerprints criptográficos en la narrativa principal.

### 3. Compatibilidad con KBS_EWG_34_V01

La guía aprobada exige para datos y corpus explicar `procedencia, selección, preparación, versión, cobertura y función`. También señala que frameworks y benchmarks suelen separar la descripción conceptual de configuraciones, software, datasets y artefactos y que el repositorio de reproducibilidad debe identificarse y explicarse. Esto no equivale a insertar toda la metadata interna de trazabilidad en Methods.

La versión corregida debe preservar la información científicamente material y desplazar la identidad técnica exhaustiva al repositorio/manifiestos y, cuando corresponda, a Section 4.11.

### 4. Correcciones obligatorias para Section 4.2

1. Eliminar todos los SHA-256 de la prosa publicable de 4.2.
2. Eliminar todas las rutas relativas internas del repositorio de 4.2.
3. Eliminar nombres exactos de archivos fuente/CSV cuando no sean necesarios para comprender una operación científica.
4. Sustituir `Hoja2` y detalles de ubicación de worksheet por una descripción funcional cuando baste: la hoja utilizada por la ejecución histórica / la primera worksheet seleccionada por el parser bajo esa configuración.
5. Mantener la limitación forense importante: el contenido procesado puede reproducirse funcionalmente, pero no puede afirmarse identidad binaria del workbook histórico original. Expresarla sin hashes.
6. Mantener los conteos científicamente relevantes: 11,320 series/107 DAM en el intermedio reconstruido; 4,232 registros de Chapter 87 antes de curación; 4,106 curados; composición H100/DEV/EVAL y códigos representados.
7. Mantener reglas de preparación, curación y particionamiento por DAM, incluida la ausencia de solapamiento DAM y de identificadores de serie entre particiones.
8. Mantener `v0.2` y `T5-safe-159` solo si ayudan a distinguir inequívocamente la configuración experimental; no acompañarlos de rutas o fingerprints.
9. Reducir nombres de campos internos como `id_unico` cuando un término científico descriptivo sea suficiente; conservar `SERIE` y `DAM` por ser unidades metodológicas del estudio.
10. Como máximo, incluir una referencia breve a que los datasets y sus identificadores técnicos/versionados están disponibles en el repositorio de reproducibilidad, preferiblemente remitiendo a Section 4.11. No duplicar ahí el inventario técnico.

### 5. Alcance

No se reabre 4.1 ni se cuestionan los hechos científicos verificados. La revisión se limita a 4.2.1–4.2.4 y a su espejo español. No se autoriza 4.3 ni bloques posteriores.

## English

The previous scientific review correctly verified the experimental facts, but the editorial review did not sufficiently distinguish complete technical traceability from KBS-appropriate publication prose. A direct check of all 34 PDFs underlying `KBS_EWG_34_V01` found no paper that reports dataset/artifact SHA-256 values as reproducibility identifiers in Methods (`0/34`). The only SHA/checksum occurrence was cryptographic functionality in the malware paper, not artifact identity.

Concrete filenames or paths occur exceptionally when they are themselves methodologically meaningful: agent-generated/validated artifacts, benchmark component files, explicitly selected samples, or the exact framework file modified by the contribution. This does not support listing internal repository paths and fingerprints for ordinary dataset identity.

Section 4.2 must therefore be revised to emphasize provenance, acquisition/selection, processing, curation, partition construction, composition, and scientifically relevant versioning. SHA-256 values and internal repository paths must be removed; filenames should remain only if indispensable to understanding a scientific operation. Exact technical identities belong in manifests/reproducibility resources and, where useful, Section 4.11. The scientific facts already verified remain valid. V010 remains suspended and B02 remains unauthorized pending correction and reaudit.