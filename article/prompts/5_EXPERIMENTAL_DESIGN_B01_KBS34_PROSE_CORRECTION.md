# Prompt operativo — Experimental Design B01: corrección de prosa KBS-34

## Español

### 1. Identidad del bloque

```text
TASK = EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION
GOVERNING_DECISION = D-043
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_KBS34_ARTIFACT_DISCLOSURE_REAUDIT_V01.md
TARGET_SECTION = 4.2.1-4.2.4 ONLY
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

### 2. Rol

Actúa exclusivamente como IA de Redacción. No reabras la arquitectura, no cambies el diseño experimental, no recalcules datos y no avances a 4.3.

### 3. Objetivo único

Revisar la prosa publicable de Sections 4.2.1–4.2.4 para ajustarla al patrón editorial KBS-34: describir los datos y el proceso metodológico con precisión científica, pero retirar metadata interna de trazabilidad que pertenece al repositorio/manifiestos y no al cuerpo narrativo del artículo.

### 4. Baseline obligatorio

Trabaja exclusivamente sobre los dos artefactos V02 exactos entregados por el autor:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md`
  - SHA-256: `bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44`
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx`
  - SHA-256: `53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2`

Si cualquiera no coincide exactamente, detente con `EXPERIMENTAL_DESIGN_B01_KBS34_BASELINE_MISMATCH`.

### 5. Fuentes editoriales gobernantes

Lee antes de editar:

1. `article/governance/D043_EXPERIMENTAL_DESIGN_B01_EDITORIAL_REOPENING_AND_V010_SUSPENSION.md`;
2. `article/reviews/5_EXPERIMENTAL_DESIGN_B01_KBS34_ARTIFACT_DISCLOSURE_REAUDIT_V01.md`;
3. `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`;
4. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md` en el snapshot aprobado por D-013;
5. `article/STYLE_GUIDE.md`;
6. D-041 como fuente de los hechos científicos autorizados del bloque.

La reauditoría de IA Gestora ya contrastó directamente los 34 PDF. No debes inventar una nueva regla editorial ni añadir detalle técnico por iniciativa propia.

### 6. Hechos científicos que deben preservarse

Conserva, con redacción natural y no contractual:

- piloto offline no vinculante en NANDINA Chapter 87;
- SERIE como unidad de análisis y DAM/declaración como agrupamiento cuando importa dependencia;
- reconstrucción del pipeline histórico desde la fuente disponible;
- límite forense: puede sostenerse reproducción funcional del contenido procesado, pero no identidad binaria del workbook histórico original;
- intermedio reconstruido: 11,320 series / 107 DAM;
- Chapter 87 antes de curación: 4,232 registros;
- conjunto curado: 4,106 registros;
- espacio de ocho dígitos y códigos representados, sin convertirlos en universo exhaustivo;
- histórico: 2,950 series / 28 DAM / 66 códigos representados;
- desarrollo: 100 series / 6 DAM / 9 códigos representados;
- evaluación: 1,056 series / 67 DAM / 42 códigos de referencia representados;
- reglas de parsing/normalización y curación metodológicamente relevantes;
- partición construida mediante asignación explícita por DAM, sin solapamiento de DAM entre los tres conjuntos;
- ausencia de solapamiento del identificador de serie entre particiones, expresada de manera descriptiva sin depender del nombre interno del campo;
- diagnósticos detallados de duplicados/near-duplicates reservados a 4.4.

### 7. Correcciones obligatorias

En Part I y Part II:

1. Elimina **todos** los SHA-256 de 4.2.
2. Elimina **todas** las rutas internas de repositorio de 4.2 (`data/...`, `src/...` o equivalentes).
3. Elimina nombres exactos de archivos del workbook y de los CSV cuando solo sirven para localización técnica.
4. No reemplaces las rutas por nombres de archivo sueltos: describe el objeto científicamente (`source workbook`, `historical partition`, `development partition`, `evaluation partition`).
5. No uses `Hoja2` si basta indicar que la ejecución histórica procesó la primera worksheet seleccionada por el parser bajo la configuración utilizada.
6. Sustituye `id_unico` por una formulación descriptiva como `series-level unique identifier` / `identificador único a nivel de serie`, salvo que el nombre de campo sea imprescindible en una operación concreta.
7. Elimina `T5-safe-159` y `seed = 2026` de la prosa principal de 4.2 salvo que puedas demostrar que el lector los necesita para comprender una decisión metodológica. La información esencial es que la partición final se materializó mediante asignaciones explícitas de DAM y no mediante un nuevo sorteo aleatorio ni selección basada en métricas del modelo.
8. Evita `byte-for-byte` como detalle de cierre si puede sustituirse por una formulación científica más natural sobre reproducción exacta de las particiones congeladas. La identidad técnica completa queda en los recursos de reproducibilidad.
9. Si es útil, incluye **una sola referencia breve** a que los datasets versionados y su metadata de integridad están documentados en los recursos de reproducibilidad/Section 4.11. No enumeres artefactos allí.
10. Prioriza la secuencia: `procedencia/selección → espacio objetivo → preparación/curación → composición de las particiones y disponibilidad reproducible`.

### 8. Criterio de estilo

El lector debe entender **qué datos se usaron, de dónde provienen, cómo fueron procesados, qué se excluyó, cómo se evitó compartir DAM entre particiones y qué contiene cada conjunto** sin necesitar conocer la estructura interna del repositorio.

La prosa debe sonar a artículo KBS, no a manifiesto de reproducibilidad, informe forense, inventario de archivos o documento de gobernanza.

### 9. Alcance cerrado

No modifiques:

- Front matter;
- Introduction;
- Related Work;
- Section 3;
- Section 4.1;
- encabezados de 4.2.1–4.2.4 salvo necesidad gramatical menor;
- Section 4.3 o posteriores;
- cifras/hechos autorizados salvo la supresión de identificadores técnicos indicada;
- comentarios heredados.

No añadas resultados, nuevas citas, nuevos experimentos, nuevas métricas, HE2/HE5, EXP11/EXP12, novelty o final gap.

### 10. Entregables

Genera:

1. `article/sections/experimental_design/Experimental_Design_B01_V02.md` — sección corregida completa 4.1 + 4.2.1–4.2.4, bilingüe, versionable en GitHub;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md` — master acumulativo exacto, entregado al autor como archivo;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx` — DOCX acumulativo editado sobre el V02 exacto, entregado al autor como archivo;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION_RESPONSE_V01.md` — respuesta operacional pequeña en GitHub.

Aplica D-035: no intentes transferir el master acumulativo grande por la vía directa que ya produjo timeout; no uses Base64 manual, chunking, fragmentación, recomposición ni workarounds auxiliares.

### 11. Validación obligatoria

Antes de entregar confirma:

```text
SECTION_4_2_SHA256_LITERAL_COUNT = 0
SECTION_4_2_INTERNAL_REPOSITORY_PATH_COUNT = 0
UNNECESSARY_EXACT_FILENAME_COUNT = 0
SECTION_4_1_CHANGED = NO
SECTION_4_3_AND_LATER_CHANGED = NO
SCIENTIFIC_COUNTS_PRESERVED = YES
PART_I_PART_II_EQUIVALENCE = PASS
INHERITED_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_STARTED
```

### 12. Stop conditions

Detente ante mismatch de baseline, contradicción entre hechos congelados y la corrección solicitada, pérdida de comentarios o imposibilidad de entregar los dos masters exactos.

No declares B01 aprobado, cerrado, congelado o integrado. Esos estados pertenecen a IA Gestora/autor.

---

## English

Execute only the KBS-34 prose correction for Experimental Design B01, Sections 4.2.1–4.2.4. Use the exact V02 Markdown and DOCX baselines and preserve all scientifically verified facts while removing publication-facing technical clutter: SHA-256 values, internal repository paths, and filenames that serve only as artifact location. Describe data objects and procedures scientifically rather than as repository entries. Preserve 4.1 and all content from 4.3 onward exactly. Keep the forensic provenance limitation, dataset counts, curation logic, DAM-disjoint partition construction, and represented-code counts. Prefer a single brief pointer to reproducibility resources rather than an artifact inventory. Produce `Experimental_Design_B01_V02.md`, cumulative V03 Markdown and DOCX, and the small GitHub response; apply D-035 and do not promote V010 or open B02.