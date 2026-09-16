# Regla acumulativa de claridad y concreción de la prosa científica / Cumulative Scientific-Prose Clarity and Concreteness Rule

```text
RULE_ID = SPCCR
RULE_VERSION = 1.0
STATUS = AUTHOR_APPROVED / ACTIVE
SCOPE = PHASE_1_AND_LATER_MANUSCRIPT_DRAFTING
ORIGIN = METHODS_B01_V02_AUTHOR_REVIEW
```

## Español

Esta regla complementa `article/STYLE_GUIDE.md` y `MWDP_V1.0` sin modificar sus reglas científicas, de claims, evidencia, versionado o citación. Se aplica a todos los bloques de manuscrito desde Methods B01 V03 en adelante.

### 1. Principio

La precisión técnica no debe lograrse mediante acumulación de abstracciones. La prosa debe permitir que el lector identifique con facilidad **qué entidad o componente realiza qué acción, sobre qué entrada, con qué salida y bajo qué restricción**.

### 2. Evitar acumulación de abstracciones

Evitar cadenas densas de sustantivos abstractos, nominalizaciones y etiquetas conceptuales cuando puedan expresarse mediante verbos y relaciones concretas. Términos técnicos necesarios —por ejemplo `historical retrieval`, `fixed Top-3`, `normative evidence` o `local LLM`— pueden mantenerse, pero no deben apilarse sin explicación operativa.

No convertir una oración en una lista comprimida de conceptos. Si una idea contiene varias operaciones, dividirla de manera que el flujo y la responsabilidad de cada componente sean visibles.

### 3. Preferir acción y relación causal/no causal explícita

Preferir formulaciones como:

- el componente X recibe Y y produce Z;
- el ranking histórico fija los candidatos antes de la recuperación normativa;
- la recuperación normativa aporta evidencia para esos candidatos y no cambia su orden;
- el LLM recibe el Top-3 y la evidencia recuperada y genera la explicación bajo restricciones explícitas.

Estas formulaciones no autorizan lenguaje causal cuando el diseño no lo sustenta; solo exigen claridad sintáctica y operacional.

### 4. Balance entre concisión y explicación

`Economía expresiva` no significa omitir relaciones necesarias. Una frase más corta pero conceptualmente opaca no es preferible a una frase ligeramente más extensa que haga visible el proceso. Cada párrafo debe tener una función científica principal y conducir al lector desde la idea general hacia el detalle necesario.

### 5. Configurabilidad y generalización

Cuando se describa configurabilidad, replicabilidad o reutilización de la arquitectura, debe quedar claro qué elementos pueden cambiar —por ejemplo dataset/banco histórico, universo de clases o corpus documental— y qué contrato funcional permanece. Esa propiedad de diseño **no debe presentarse como evidencia de desempeño o generalización empírica fuera del escenario evaluado**.

### 6. QA obligatorio de prosa

Antes de entregar cada bloque, la IA de Redacción debe revisar explícitamente:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS / NOT_APPLICABLE
```

Una falla en cualquiera de estos controles requiere revisión antes de declarar la entrega lista para auditoría interna.

---

## English

This rule complements `article/STYLE_GUIDE.md` and `MWDP_V1.0` without changing their scientific, claim-evidence, versioning, or citation requirements. It applies to all manuscript blocks from Methods B01 V03 onward.

### 1. Principle

Technical precision must not rely on stacked abstractions. Prose should allow the reader to identify **which entity or component performs which action, on what input, with what output, and under what constraint**.

### 2. Avoid stacked abstractions

Avoid dense strings of abstract nouns, nominalizations, and conceptual labels when the same meaning can be expressed through verbs and explicit relationships. Necessary technical terms may remain, but they should not be stacked without operational explanation.

### 3. Prefer explicit action and relationships

Prefer concrete formulations such as: component X receives Y and produces Z; the historical ranking fixes candidates before normative retrieval; normative retrieval provides evidence for those candidates without changing their order; and the LLM receives the fixed Top-3 plus retrieved evidence and produces an explanation under explicit constraints.

This clarity requirement does not authorize causal language unsupported by the study design.

### 4. Balance concision and explanation

Economy of expression does not mean omitting relationships needed for comprehension. A shorter but opaque sentence is not preferable to a slightly longer sentence that makes the process clear. Each paragraph should serve one main scientific function and move from the general idea to the necessary detail.

### 5. Configurability versus generalization

When configurability, replicability, or architectural reuse is described, the text should identify which resources can change—such as the labeled historical dataset, target class universe, or documentary corpus—and which functional contract remains fixed. This design property must **not** be presented as evidence of empirical performance or generalization beyond the evaluated setting.

### 6. Mandatory prose QA

Before delivery, the Writing AI must explicitly check:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS / NOT_APPLICABLE
```
