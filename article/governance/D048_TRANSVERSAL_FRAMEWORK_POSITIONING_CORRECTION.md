# D-048 — Transversal framework positioning correction

## Español

```text
DECISION_ID = D-048
DATE = 2026-09-25
STATUS = ACTIVE / BINDING
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_POSITIONING_REVIEW_V01.md@00a71c5eeb0ed057ae50d814c728c586510651ae
CANONICAL_MASTER = ARTICLE_MASTER_V009
WORKING_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04
WORKING_CANDIDATE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
WORKING_CANDIDATE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
B01_SCIENTIFIC_FACTS = VERIFIED / PASS / PRESERVED
B01_STRUCTURE_V02_ALIGNMENT = VERIFIED / PASS / PRESERVED
AUTHOR_APPROVAL_GATE = SUSPENDED_PENDING_TRANSVERSAL_POSITIONING_CORRECTION
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

La revisión transversal posterior a V04 confirma que la arquitectura científica y el diseño experimental B01 son correctos, pero el master todavía no jerarquiza con suficiente fuerza el objeto científico general que debe comunicar el artículo.

## Objeto científico que debe gobernar la corrección

El artículo debe presentar como objeto general un **framework configurable para apoyo auditable a la clasificación arancelaria**, cuyo núcleo técnico es la arquitectura ya congelada:

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

El framework apoya la clasificación mediante recomendación/ranking de candidatos y explicación trazable; no adjudica autónomamente una clasificación jurídica final.

La instanciación experimental utilizada para evaluar el framework queda delimitada a:

- NANDINA a ocho dígitos;
- Capítulo 87;
- datos históricos y corpus documental/normativo del contexto peruano descrito en Methods.

Esos elementos definen el **testbed empírico**, no el alcance conceptual del framework.

## Reglas vinculantes

1. `FRAMEWORK_GENERAL_SCOPE ≠ NANDINA_CHAPTER87_TESTBED`.
2. `ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK`.
3. `TARIFF_CLASSIFICATION_SUPPORT = RANKED_CANDIDATE_RECOMMENDATION + DOCUMENTARY_EVIDENCE + CONTROLLED_EXPLANATION`.
4. `AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION = NOT_CLAIMED`.
5. `AUDITABILITY = TRACEABLE / INSPECTABLE CASE-LEVEL SUPPORT`, no corrección jurídica ni puntuación formal de auditoría salvo protocolo explícito.
6. `CONFIGURABILITY / RE-INSTANTIATION ≠ EMPIRICAL_GENERALIZATION`.
7. La re-instanciación puede utilizar otros bancos históricos, espacios de clases, profundidades arancelarias y corpus documentales compatibles si se preservan las interfaces y controles declarados.
8. No se permite afirmar transferencia de desempeño a otros capítulos, niveles, jurisdicciones o corpus sin nueva evidencia empírica.

## Alcance autorizado de corrección

Se autoriza una corrección editorial/científica estrecha sobre `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04` únicamente para reforzar esta jerarquía conceptual en:

- los párrafos de Introduction que presentan el objeto propuesto, las contribuciones y la instanciación empírica;
- el espejo semántico español correspondiente;
- una corrección terminológica mínima en Section 3.7 si es necesaria para identificar la arquitectura como núcleo del framework.

La corrección debe:

- introducir `framework` como denominación del objeto científico general;
- mantener `architecture` para el núcleo técnico de Section 3;
- hacer explícito que el framework genera/recomienda candidatos, aporta evidencia y produce explicación controlada para revisión/auditoría;
- presentar NANDINA 8 dígitos / Capítulo 87 / contexto peruano como la instanciación usada para evaluar el framework;
- eliminar de Introduction la formulación residual `the testbed is non-binding` / `el testbed es no vinculante` y sustituirla por una frontera científica clara compatible con Section 4.1;
- preservar las RQ, hechos experimentales, cifras, arquitectura, Related Work y B01 salvo las correcciones expresamente autorizadas.

No se autoriza reescribir Section 4.1–4.2.3, abrir Section 4.3+, modificar resultados, declarar novedad ni promover V010.

## Gate

La aprobación autoral de B01 queda suspendida únicamente porque el master acumulativo será objeto de esta corrección transversal. El PASS científico/factual de B01 V04 no se revoca.

Después de la corrección, la IA Gestora debe ejecutar una auditoría diferencial y conceptual. Si pasa, se reabre el gate de aprobación autoral.

## English

D-048 authorizes a narrow transversal positioning correction. The article-level object must be communicated as a configurable framework for auditable tariff-classification decision support, with the already frozen Section-3 architecture as its technical core. The evaluated primary flow ranks/recommends candidates, attaches candidate-specific documentary evidence, and generates controlled explanations; it does not autonomously adjudicate a legally final tariff code.

Eight-digit NANDINA, Chapter 87, and the Peruvian historical/documentary context define the empirical instantiation used to evaluate the framework, not the framework's conceptual scope. Re-instantiation with other compatible historical banks, class spaces, tariff depths, or documentary corpora is a configurability property and does not imply empirical performance transfer.

B01 V04 scientific facts and Structure-V02 alignment remain PASS. Section 4.3+ scientific drafting and Results remain unauthorized. V010 remains unpromoted.