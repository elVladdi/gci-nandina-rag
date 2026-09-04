# Prompt 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales / Authority, currency, and traceability of normative/official sources

## Español

### Rol y alcance

Actúa como IA de análisis documental del artículo científico principal. Ejecuta **exclusivamente** `0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales`.

Este bloque **no es revisión de literatura académica**. Es una auditoría de fuentes primarias oficiales y de su relación temporal/documental con el corpus normativo efectivamente usado por el experimento.

No redactes secciones del manuscrito, no declares novelty ni gap definitivo, no modifiques GitHub, no modifiques el Plan Maestro, no alteres 0A, no actualices el corpus experimental y no avances a 0B-06, 0C ni fases posteriores.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/DECISIONS.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/STYLE_GUIDE.md`;
8. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
9. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
10. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`;
11. los freezes de `0B-01` a `0B-05B`;
12. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
13. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
14. este prompt completo.

No reabras ni reinterpretes freezes anteriores. Si detectas una incompatibilidad con hechos/claims experimentales congelados, **no la resuelvas**: clasifícala conforme a la sección de drift y devuelve el caso al editor científico.

### Regla crítica: dos estados documentales que no deben mezclarse

Debes mantener separados:

1. **`EXPERIMENTAL_SOURCE_SNAPSHOT`**: las fuentes exactas que alimentaron el corpus normativo del experimento congelado;
2. **`CURRENT_OFFICIAL_SOURCE_STATE`**: el estado oficial verificable de los instrumentos/normas al momento de esta auditoría.

Un instrumento posterior, una modificación o una fuente actualmente vigente **no sustituye retrospectivamente** la fuente usada por el experimento. Del mismo modo, que el experimento haya usado un PDF identificable no demuestra que ese PDF representara toda la normativa vigente en la fecha de ejecución.

### Snapshot experimental obligatorio

Usa el repositorio de desarrollo `elVladdi/gci-nandina-rag`, ref congelado de 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`

Verifica directamente:

- `data/external/Arancel 2022.pdf`;
- `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
- `data/processed/corpus/nandina/run_metadata.json`;
- los artefactos procesados de `data/processed/corpus/arancel/` y `data/processed/corpus/nandina/` cuando sean necesarios para identificar el alcance de lo efectivamente ingerido.

Los metadatos congelados que debes comprobar, no asumir, incluyen:

- `Arancel 2022.pdf`: SHA-256 registrado `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- `CAN Desición 885 - Nanadina Gaceta 4359.pdf`: SHA-256 registrado `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

No confundas el SHA-256 del archivo fuente registrado por el pipeline con el blob SHA de GitHub.

### Fuentes oficiales primarias controladas

La auditoría debe cubrir, como mínimo, las siguientes capas.

#### A. Organización Mundial de Aduanas — nivel HS

Verifica en fuentes oficiales de la WCO/OMA:

- Convenio Internacional del Sistema Armonizado, en lo necesario para identificar qué integra el HS y la obligación relativa a GIR/notas;
- `HS Nomenclature 2022 edition`;
- `General Rules for the Interpretation of the Harmonized System` de la edición 2022;
- en la medida necesaria para la vigencia, las enmiendas complementarias de la edición 2022 y sus fechas de entrada en vigor;
- el estatus documental de las Explanatory Notes solo si se usa un claim sobre su carácter interpretativo. No las confundas con el texto de la Nomenclatura/Convenio.

Punto de entrada oficial:
`https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition/hs-nomenclature-2022-edition.aspx`

#### B. Comunidad Andina — nivel NANDINA

Verifica directamente en Gacetas/portal oficial de la Comunidad Andina:

- **Decisión 885**, Gaceta Oficial 4359 — aprobación de la NANDINA y vigencia;
- **Decisión 906**, Gaceta Oficial 5062 — modificación de la Decisión 885 y vigencia;
- **Resolución 2592**, Gaceta Oficial 5761, 18-05-2026 — Notas Explicativas Complementarias de la NANDINA, incluyendo su alcance por capítulos y su estatus como texto auxiliar;
- cualquier otra modificación oficial estrictamente necesaria para determinar el estado vigente o el impacto sobre **Capítulo 87**, únicamente si se identifica mediante fuente oficial primaria.

URLs de partida oficiales:
- `https://www.comunidadandina.org/normativa-files/uploads/Gaceta_4359_d848f7904e.pdf`
- `https://www.comunidadandina.org/DocOficialesFiles/Gacetas/GACETA%205062.pdf`
- `https://www.comunidadandina.org/normativa-files/uploads/Gaceta_5761_8b9418963b.pdf`

Control específico obligatorio: la Decisión 906 documenta modificaciones en la NANDINA con vigencia desde `2023-01-01`; audita expresamente si existen modificaciones de Capítulo 87 y si pueden intersectar el corpus/candidatos/casos del experimento. **No infieras impacto experimental solo porque una modificación pertenece al Capítulo 87.** Debes comprobar el solapamiento concreto cuando sea posible.

#### C. Perú — Arancel de Aduanas y fuentes SUNAT/MEF

Verifica mediante fuentes oficiales MEF/El Peruano/SUNAT:

- **Decreto Supremo N.° 404-2021-EF**, que aprueba el Arancel de Aduanas 2022, incluyendo fecha/entrada en vigor y relación declarada con la Decisión 885;
- modificaciones posteriores del Arancel de Aduanas 2022 que sean necesarias para determinar si afectaron Capítulo 87 o los artefactos utilizados por el proyecto;
- página oficial SUNAT/gob.pe `Nomenclatura común Nandina`, solo como fuente institucional/orientativa y **no** como sustituto de la Decisión comunitaria;
- `DESPA-PG.01 — Importación para el consumo (versión 8)` y su estado de modificaciones, únicamente para claims del proyecto sobre procedencia/contexto administrativo de las DAM;
- `DESPA-PE.00.03 — Reconocimiento físico - extracción y análisis de muestras (versión 4)` y su estado de modificaciones, únicamente cuando el proyecto use esa fuente para caracterizar reconocimiento físico/extracción de muestras.

Puntos de entrada oficiales:
- MEF, DS 404-2021-EF: portal oficial de normativa MEF/El Peruano;
- SUNAT DESPA-PG.01 v8: `https://www.sunat.gob.pe/legislacion/procedim/despacho/importacion/importac/procGeneral/despa-pg.01.htm`;
- SUNAT NANDINA: `https://www.gob.pe/17040-nomenclatura-comun-nandina`.

No incluyas estadísticas SUNAT, anuarios u otras fuentes administrativas salvo que sean estrictamente necesarias para un claim documental del bloque.

### Política de acceso web

A diferencia de los lotes académicos anteriores, **se autoriza y exige consulta web** porque la vigencia debe comprobarse contra fuentes oficiales actuales.

Dominios finales autorizados para evidencia primaria:

- `wcoomd.org` y, cuando corresponda, infraestructura oficial de publicaciones de WCO/OMA;
- `comunidadandina.org`;
- `sunat.gob.pe`;
- `gob.pe`;
- `mef.gob.pe`;
- `elperuano.pe`.

Puedes usar un buscador únicamente para localizar la fuente oficial. **No uses como evidencia final** vLex, blogs, Wikipedia, agregadores, despachos legales, páginas de terceros, papers académicos ni snippets del buscador cuando exista la fuente primaria oficial.

Si el número/título/fecha de un instrumento no puede verificarse en una fuente primaria oficial, marca `NO_VERIFICABLE_EN_FUENTE_OFICIAL` y no lo completes desde memoria.

### Jerarquía y función documental

No construyas una jerarquía jurídica universal por intuición. Para cada fuente registra exactamente:

- emisor;
- tipo de instrumento/documento;
- número/identificador;
- fecha de adopción/publicación;
- fecha de entrada en vigor cuando conste;
- instrumento que aprueba/modifica/deroga cuando conste;
- alcance territorial/material;
- nivel: `HS_INTERNATIONAL`, `NANDINA_SUPRANATIONAL`, `PERU_NATIONAL`, `ADMINISTRATIVE_PROCEDURE`, `INSTITUTIONAL_ORIENTATION` u otro justificado;
- función documental: texto normativo, nomenclatura, regla interpretativa, texto auxiliar, procedimiento administrativo, orientación institucional, etc.;
- URL/identificador oficial;
- relación con el corpus experimental;
- limitaciones.

`OFFICIAL_SOURCE` no significa automáticamente `LEGALLY_SUFFICIENT_FOR_CASE`.

`TEXT_AUXILIARY_FOR_INTERPRETATION` no debe denominarse norma vinculante salvo que la fuente primaria establezca expresamente ese estatus.

`OFFICIAL / AUTHORITATIVE SOURCE ≠ CORRECT LEGAL APPLICATION ≠ CORRECT CLASSIFICATION`.

### Auditoría temporal obligatoria

Construye una línea temporal mínima que permita responder:

1. ¿Qué instrumento estaba vigente cuando entró en vigor HS/NANDINA 2022?
2. ¿Qué modificaciones oficiales posteriores existen y desde cuándo?
3. ¿Qué fuentes exactas fueron procesadas por el experimento?
4. ¿Las fuentes experimentales representan una edición/snapshot anterior a alguna modificación vigente en la fecha de ejecución?
5. Si existe drift, ¿afecta potencialmente Capítulo 87 o elementos concretos utilizados en evaluación?

No llames `STALE`, `INVALID` o `OUTDATED` al experimento sin separar:

- `SOURCE_VERSION_DRIFT_PRESENT`;
- `SCOPE_OVERLAP_CONFIRMED`;
- `EXPERIMENTAL_METRIC_IMPACT_CONFIRMED`.

Son tres afirmaciones diferentes.

### Estados de drift

Usa exactamente uno por hallazgo:

- `NO_DRIFT_IDENTIFIED`;
- `SOURCE_VERSION_DRIFT_PRESENT_NO_SCOPE_OVERLAP`;
- `SOURCE_VERSION_DRIFT_PRESENT_SCOPE_OVERLAP_POSSIBLE`;
- `SOURCE_VERSION_DRIFT_PRESENT_SCOPE_OVERLAP_CONFIRMED`;
- `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`;
- `NO_VERIFICABLE_WITH_AVAILABLE_OFFICIAL_SOURCE`.

Si detectas `SOURCE_VERSION_DRIFT_PRESENT_SCOPE_OVERLAP_CONFIRMED` o una posibilidad razonable de que el corpus normativo congelado no reflejara instrumentos vigentes aplicables a Capítulo 87, **no cambies resultados, claims, 0A ni Plan Maestro**. Marca `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED` y explica exactamente qué debe revisar la IA experimental.

La IA experimental es la única autorizada a modificar el Plan Maestro o decidir ajustes experimentales.

### Verificación de solapamiento con Capítulo 87

Cuando una modificación oficial enumere códigos/subpartidas, contrástalos cuando sea posible con artefactos congelados del benchmark, por ejemplo:

- listas de códigos EVAL;
- códigos del banco histórico;
- candidatos producidos/slots de integración si existe artefacto accesible;
- corpus normativo procesado.

No concluyas `impacto = 0` únicamente porque el código modificado no aparezca como label de referencia EVAL: podría aparecer como candidato o evidencia. Si no puede verificarse todo el alcance, usa el estado de incertidumbre correspondiente.

### Relación con 0B y F1–F5

0B-05C es una auditoría documental oficial, **no un pressure test de novelty**.

- F1: como máximo `METHOD_BOUNDARY_RELEVANT` por separación entre ranking histórico y autoridad/evidencia normativa.
- F2: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`, salvo frontera explicación ≠ decisión oficial.
- F3: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- F4: `METHOD_BOUNDARY_RELEVANT` para separar fuente oficial/evidencia de corrección jurídica adjudicada.
- F5: `METHOD_BOUNDARY_RELEVANT` para distinguir trazabilidad de fuente de suficiencia/auditabilidad sustantiva.

No reabras G6 ni G7.

### Formato obligatorio de salida

#### A. Inventario de fuentes oficiales
`ID | emisor | instrumento/documento | tipo | fecha | vigencia | URL/identificador oficial | nivel | rol en el proyecto | estado de verificación`.

#### B. Snapshot experimental de fuentes
`fuente experimental | ruta repo | SHA-256 registrado | fecha de procesamiento | contenido/artefactos derivados | correspondencia oficial verificada | limitaciones`.

#### C. Matriz de autoridad y función documental
`fuente | autoridad emisora | función documental | aprueba/modifica/deroga | alcance | qué claim permite | qué claim no permite`.

#### D. Línea temporal de vigencia
Incluye como mínimo HS 2022, Decisión 885, Decisión 906, Arancel 2022 y cualquier modificación posterior material identificada.

#### E. Comparación `EXPERIMENTAL_SOURCE_SNAPSHOT` vs `CURRENT_OFFICIAL_SOURCE_STATE`
`elemento | snapshot experimental | estado oficial actual | diferencia | alcance Chapter 87 | estado de drift | evidencia primaria`.

#### F. Auditoría específica de Capítulo 87
Lista cada modificación oficial detectada que toque Capítulo 87 y comprueba, hasta donde los artefactos congelados permitan, su intersección con labels, candidatos o evidencia experimental.

#### G. Claims oficiales autorizables
Cada claim debe incluir fuente oficial exacta, alcance y límite. No redactes todavía el manuscrito.

#### H. Claims prohibidos/excesivos
Incluye como mínimo las equivalencias que confundan oficialidad, vigencia, evidencia, suficiencia jurídica, corrección de aplicación y corrección clasificatoria.

#### I. Drift y trigger experimental
`hallazgo | estado de drift | evidencia | posible componente afectado | ¿requiere IA experimental? | razón`.

#### J. Relación metodológica con F1–F5
Usa solo etiquetas metodológicas; no novelty.

#### K. Dictamen
Concluye uno de:

- `PASS`;
- `PASS WITH CORRECTIONS`;
- `REVIEW_REQUIRED`;
- `BLOCKED`.

Además informa por separado:

- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` o `EXPERIMENTAL_REVIEW = REQUIRED`;
- `SOURCE_VERSION_DRIFT = NONE / PRESENT / NOT_VERIFIABLE`;
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`;
- `NOVELTY = NOT_DECLARED`;
- `FINAL_GAP = NOT_DEFINED`.

### Prohibiciones finales

No:

- modifiques el Plan Maestro;
- modifiques el corpus normativo;
- actualices o reruns experimentos;
- recalcules métricas salvo una comprobación documental explícitamente requerida y no experimental;
- sustituyas retroactivamente las fuentes del experimento;
- concluyas legal correctness a partir de fuente oficial;
- confundas página orientativa SUNAT con instrumento comunitario;
- confundas HS-6, NANDINA-8 y subpartida nacional peruana de 10 dígitos;
- declares novelty o gap definitivo;
- redactes el manuscrito;
- avances a 0B-06, 0C o 0D.

Detente al finalizar 0B-05C y devuelve el entregable al editor científico.

---

## English

### Role and scope

Act as the official-source documentary-analysis AI for the main scientific article. Execute **only** `0B-05C — Authority, currency, and traceability of normative/official sources`.

This is not an academic-literature review. It audits primary official sources and their temporal/documentary relationship to the normative corpus actually used by the frozen experiment.

Do not draft manuscript sections, declare novelty/final gap, modify GitHub or the Master Plan, alter 0A, update the experimental corpus, or proceed to 0B-06/0C/0D.

### Mandatory separation

Keep two states distinct:

- `EXPERIMENTAL_SOURCE_SNAPSHOT`: exact sources ingested by the frozen experiment;
- `CURRENT_OFFICIAL_SOURCE_STATE`: officially verifiable current state at the time of audit.

Current instruments do not retrospectively replace the experimental snapshot, and an identifiable experimental PDF does not by itself prove complete currency at execution time.

### Experimental snapshot

Use development-repository ref `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` and directly verify the Arancel 2022 and CAN Decision 885 source files, their run metadata, and relevant processed artifacts. Confirm the recorded SHA-256 values rather than assuming them.

### Controlled official-source layers

Audit primary official sources at:

- WCO HS level: HS Convention as needed, HS Nomenclature 2022, GIR, relevant complementary amendments, and Explanatory Notes status only when a claim requires it;
- Andean level: Decision 885/Gazette 4359, Decision 906/Gazette 5062, Resolution 2592/Gazette 5761, plus only additional official instruments strictly needed to determine Chapter-87 currency;
- Peru level: DS 404-2021-EF (Arancel de Aduanas 2022), material subsequent tariff amendments, SUNAT NANDINA orientation, DESPA-PG.01 v8 and DESPA-PE.00.03 v4 only for the administrative-data provenance claims for which they are relevant.

Web access is required, but final evidence must come from official WCO, Andean Community, SUNAT, gob.pe, MEF or El Peruano sources. Search engines may be used only for discovery. Third-party aggregators and academic sources are not final authority for this batch.

### Authority, hierarchy, and currency controls

For every source record issuer, exact document type/identifier, adoption/publication date, effective date where stated, amendment/repeal relationship, territorial/material scope, documentary level/function, official URL, relationship to the experiment, and limitations.

Do not infer a universal legal hierarchy. Preserve:

`OFFICIAL / AUTHORITATIVE SOURCE ≠ CORRECT LEGAL APPLICATION ≠ CORRECT CLASSIFICATION`.

Texts described by the primary source as interpretative/auxiliary must not be relabeled binding norms without primary-source support.

### Drift audit

Build the minimum timeline needed to compare HS/NANDINA 2022, Decision 885, Decision 906, Peru's Arancel 2022, and subsequent material changes. Explicitly inspect Chapter 87.

Use only the allowed drift states specified in the Spanish section. Distinguish source-version drift, confirmed scope overlap, and confirmed experimental-metric impact. They are not equivalent.

If a later/current official instrument plausibly affects frozen Chapter-87 experimental sources, do not alter results/claims/0A/Master Plan. Return `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED` and specify what the experimental AI must assess.

Absence of a modified code from EVAL reference labels does not prove zero impact because it may appear among candidates or evidence.

### Required output

Return sections A–K exactly as specified in the Spanish instructions: official-source inventory; experimental snapshot; authority/function matrix; currency timeline; snapshot-vs-current comparison; Chapter-87 audit; authorized and prohibited claims; drift/experimental trigger matrix; F1–F5 methodological relation; and verdict.

Report separately `EXPERIMENTAL_REVIEW`, `SOURCE_VERSION_DRIFT`, `MANUSCRIPT_DRAFTING`, `NOVELTY`, and `FINAL_GAP`.

Stop after 0B-05C.