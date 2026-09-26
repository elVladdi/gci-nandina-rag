# Experimental Design B01 V04 — Transversal framework positioning correction

## 1. Identidad y mandato

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION
ROLE = DRAFTING_AI / CONTROLLED_TRANSVERSAL_POSITIONING_CORRECTION
GOVERNING_DECISION = article/governance/D048_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION.md
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_POSITIONING_REVIEW_V01.md
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
BASELINE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
BASELINE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
EXPECTED_COMMENT_COUNT = 40
SCIENTIFIC_REWRITE_OUTSIDE_AUTHORIZED_PARAGRAPHS = PROHIBITED
SECTION_4_1_TO_4_2_3_REWRITE = PROHIBITED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = PROHIBITED
RESULTS = NOT_AUTHORIZED
```

Ejecuta exclusivamente esta corrección conceptual transversal. No reabras el contenido científico o factual de B01, que ya obtuvo PASS.

## 2. Onboarding y precedencia

Antes de editar:

1. confirma repo `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`;
2. lee `article/START_HERE.md`;
3. lee `article/ARTICLE_STATUS.md`;
4. lee D-045, D-046, D-047 y D-048;
5. lee `article/reviews/5_EXPERIMENTAL_DESIGN_B01_V04_STRUCTURE_ALIGNMENT_INTERNAL_REVIEW_V01.md`;
6. lee `article/reviews/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_POSITIONING_REVIEW_V01.md`;
7. verifica los dos baseline adjuntos por SHA-256 antes de modificarlos.

D-021, D-022, D-023, D-035 y D-048 son vinculantes. No uses Base64 manual, chunking, fragmentación, recomposición, archivos auxiliares, ramas temporales ni múltiples commits como workaround de transferencia.

Si cualquiera de los baseline no coincide exactamente, detente con:

`B01_V04_POSITIONING_BASELINE_MISMATCH`

## 3. Objeto científico que debe quedar inequívoco

El artículo debe comunicar como objeto general un **framework configurable para apoyo auditable a la clasificación arancelaria**.

La arquitectura de Section 3 es el **núcleo técnico del framework**, no un objeto alternativo ni reemplazado. El flujo congelado permanece:

```text
commercial description
→ normalization
→ historical retrieval
→ historical ranking
→ fixed Top-3
→ candidate-specific documentary evidence
→ evidence-context construction
→ local LLM
→ controlled explanation of the fixed Top-3
```

La función de apoyo a clasificación debe expresarse con precisión:

- la recuperación histórica genera y ordena candidatos;
- el Top-3 queda fijo;
- la recuperación documental aporta evidencia específica por candidato sin modificar el ranking;
- el LLM local genera explicación controlada del Top-3 fijo;
- la cadena preserva trazabilidad para inspección/revisión/auditoría del caso.

No afirmes que el framework adjudica autónomamente un código jurídico final.

La evaluación de referencia es una **instanciación experimental** del framework en:

- NANDINA a ocho dígitos;
- Capítulo 87;
- contexto administrativo/documental peruano definido en Methods.

Ese testbed no define el alcance conceptual del framework.

La re-instanciación con otros bancos históricos, espacios de clases, profundidades arancelarias o corpus documentales compatibles es una propiedad de configurabilidad. No implica transferencia de desempeño.

## 4. Alcance editable exacto

### 4.1 Introduction — Part I English

Puedes modificar únicamente estos tres párrafos ya existentes:

1. el párrafo que comienza `This study examines a decision-support architecture...`;
2. el párrafo que comienza `The article makes three bounded contributions...`;
3. el párrafo que comienza `The empirical evaluation uses an offline customs-classification testbed...`.

Objetivos:

- definir el objeto general como `framework for auditable tariff-classification decision support` o formulación científicamente equivalente;
- presentar la architecture de Section 3 como technical core del framework;
- explicitar que el framework soporta clasificación mediante ranked candidate recommendation, documentary evidence y controlled explanation;
- hacer visible la trazabilidad/inspectabilidad de la recomendación para revisión/auditoría, sin equipararla con legal correctness;
- introducir la instanciación empírica mediante una transición equivalente a `To evaluate the framework, we instantiate it...`;
- presentar eight-digit NANDINA, Chapter 87 y el contexto peruano como evaluation setting;
- eliminar `The testbed is non-binding` y sustituir esa idea por la frontera científica precisa ya coherente con Section 4.1: no operational customs deployment / no legal adjudication;
- mantener la distinción configurability ≠ empirical generalization.

No cambies las RQ ni el roadmap.

### 4.2 Introduction — Part II Spanish mirror

Aplica una equivalencia semántica natural y académica a los tres párrafos correspondientes. Evita calcos innecesarios.

Debe quedar inequívoco:

`framework general → arquitectura como núcleo → evaluación en una instanciación NANDINA/Capítulo 87/contexto peruano`.

Elimina `el testbed es no vinculante` y usa la frontera científica equivalente.

### 4.3 Section 3.7 — precisión terminológica mínima opcional

Puedes modificar **como máximo la primera oración** de 3.7 en Part I y su espejo español si ello resulta necesario para introducir la relación:

`framework → architecture as technical core`.

Ejemplo semántico permitido: cambiar `The procedure can be re-instantiated...` por una formulación donde `framework` sea el sujeto, sin alterar requisitos, interfaces ni significado científico del resto de 3.7.

No modifiques ningún otro párrafo de Section 3.

## 5. Contenido congelado que debe permanecer textualmente inalterado

Fuera de los párrafos autorizados:

- Introduction completa, incluidas RQ y roadmap;
- Related Work 2.1–2.6;
- Section 3.1–3.6;
- Section 3.7 salvo la primera oración opcional indicada;
- Section 4.1–4.2.3;
- esqueleto 4.3–4.8;
- Section 5 y posteriores.

No cambies cifras, citas, referencias, comentarios, notas de función, títulos de secciones o placeholders.

## 6. Límites científicos obligatorios

```text
FRAMEWORK_GENERAL_SCOPE != NANDINA_CHAPTER87_TESTBED
ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK
TARIFF_CLASSIFICATION_SUPPORT = AUTHORIZED
RANKED_CANDIDATE_RECOMMENDATION = AUTHORIZED
AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION = PROHIBITED
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
AUDITABILITY != LEGAL_CORRECTNESS
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
NOVELTY = NOT_DECLARED
FINAL_GAP = NOT_DEFINED
```

No conviertas la palabra `framework` en un claim de novedad.

## 7. Estilo

La prosa debe ser de artículo KBS, no de documento de gobernanza.

- Preferir verbos y objetos concretos.
- Evitar abstracciones innecesarias, nominalización excesiva y lenguaje contractual.
- No usar SHA, rutas, nombres internos de archivos o IDs experimentales en la prosa científica.
- No introducir literatura nueva ni búsqueda web.
- Mantener inglés de publicación natural y espejo español semánticamente fiel.

## 8. Entregables

Genera exactamente:

1. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx`;
3. `article/responses/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION_RESPONSE_V01.md`.

No generes una nueva versión de la sección B01 aislada porque 4.1–4.2.3 no deben cambiar.

## 9. Verificación diferencial obligatoria

La respuesta GitHub debe demostrar:

- hashes SHA-256 de entrada y salida;
- lista exacta de párrafos modificados;
- que Related Work permanece textualmente idéntico;
- que 4.1–4.2.3 permanece textualmente idéntico;
- que el esqueleto 4.3–4.8 permanece idéntico;
- que Section 5 y posteriores permanecen idénticos;
- que no cambiaron RQ, cifras ni citas;
- que la formulación `non-binding testbed / testbed no vinculante` fue eliminada de Introduction;
- que el objeto general queda identificado como framework y la architecture como su technical core;
- que la instanciación NANDINA/Chapter-87/Peruvian context queda subordinada explícitamente a la evaluación del framework;
- que no se introdujo claim de clasificación jurídica final, novedad o generalización empírica;
- 40 comentarios finales y cero tracked changes;
- integridad OOXML;
- render completo e inspección visual de todas las páginas.

Si cualquier cambio fuera del alcance autorizado parece necesario, detente con:

`B01_V04_POSITIONING_UNEXPECTED_CHANGE_REQUIRED`

## 10. Handoff D-035

Entrega los masters acumulativos V05 como archivos exactos descargables en el chat. No intentes transferirlos a GitHub mediante Base64, fragmentación o reconstrucción.

Versiona únicamente la respuesta pequeña en GitHub.

El chat final debe limitarse a:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_FRAMEWORK_POSITIONING_CORRECTION_RESPONSE_V01.md@<commit_sha>`

más los dos adjuntos V05.

No declares B01 aprobado, cerrado, congelado o integrado. No abras Section 4.3+. Después del handoff, detente.