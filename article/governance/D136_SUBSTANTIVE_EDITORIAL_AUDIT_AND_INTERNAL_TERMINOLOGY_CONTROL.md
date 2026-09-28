# D-136 — Auditoría sustantiva/editorial obligatoria y control de terminología interna / Mandatory substantive-editorial audit and internal-terminology control

## Español

```text
DECISION = D-136
AUTHORITY = AUTHOR_CLARIFICATION_2026-09-28
STATUS = ACTIVE / BINDING
SCOPE = ALL_MANUSCRIPT_BLOCK_AUDITS_FROM_DISCUSSION_B04_ONWARD + FINAL_TRANSVERSAL_QA
SCIENTIFIC_SCOPE_CHANGE = NONE
MWDP_V1_0 = PRESERVED
SPCCR_V1_0 = PRESERVED
KBS_EWG_34_V01 = PRESERVED / ENFORCED
```

### 1. Regla

La auditoría de IA Gestora nunca puede reducirse a identidad de artefactos, SHA-256, Git blobs, commits, diferencial de archivos, OOXML, comentarios o render. Esos controles son necesarios, pero no suficientes para emitir `PASS`.

Toda auditoría de un bloque del manuscrito debe comprobar conjuntamente:

1. **Fidelidad científica y trazabilidad:** cada hecho, cifra, resultado, interpretación y comparación debe estar respaldado por la fuente gobernante o por una claim autorizada. No se inventan datos, mecanismos, resultados, literatura, evidencia, metadatos ni inferencias.
2. **Fuerza epistémica y anti-overclaiming:** el texto no puede convertir asociación en corrección, retrieval en accuracy global, auditabilidad en legal correctness, configurabilidad en generalización, correlación/descripción en causalidad, ni evidencia interna en validez externa. Deben respetarse `CLAIM_EVIDENCE_MATRIX.md`, MWDP y las decisiones científicas congeladas.
3. **Coherencia conceptual y argumental:** cada párrafo debe cumplir la función de la sección, conectar correctamente premisas y evidencia y no contradecir arquitectura, Results, Discussion previa, RQs, hipótesis o límites ya integrados. Discussion interpreta; no inventa resultados ni mecanismos.
4. **Concreción y legibilidad científica:** se aplica `SPCCR_V1.0`. Debe ser identificable qué componente hace qué, sobre qué entrada, con qué salida y bajo qué restricción. Se auditan densidad de abstracción, nominalizaciones, acumulación de conceptos, frases contractuales opacas y relaciones agente–acción–objeto.
5. **Adecuación editorial KBS:** se aplica `KBS_EWG_34_V01`. El manuscrito debe sonar como artículo científico, no como documento de gobernanza, especificación contractual, bitácora de repositorio, reporte de QA o tesis excesivamente abstracta.
6. **Control de terminología interna:** identificadores y etiquetas de operación interna —por ejemplo IDs de decisiones/claims, estados de gate, nombres de prompts/responses, hashes/commits, usernames internos, códigos de microauditoría, nombres de campos de implementación o etiquetas de diagnóstico— no deben filtrarse al texto publicable salvo que constituyan un objeto científico indispensable y se presenten en lenguaje lector-facing, definido y justificado. La evidencia subyacente puede conservarse, pero debe narrarse con terminología científica pública.
7. **Naturalidad terminológica bilingüe:** inglés y español deben preservar la misma carga epistémica, pero el espejo español no debe convertirse en traducción mecánica llena de anglicismos evitables. Se conservan únicamente términos técnicos cuya estabilidad esté gobernada o cuyo uso sea estándar y necesario.
8. **Citas y literatura:** cada cita debe apoyar exactamente el claim asociado; no se usa una fuente por memoria ni se extiende su alcance. La comparación cross-study debe ser metodológicamente válida y no promocional.
9. **Integridad técnica:** solo después de los controles anteriores se consideran identidad, diferencial autorizado, Word/OOXML, comentarios, tracked changes, render, equivalencia MD/DOCX y versionado.

### 2. Regla de veredicto

```text
TECHNICAL_IDENTITY_PASS + SUBSTANTIVE_OR_EDITORIAL_DEFECT = NOT_PASS
SCIENTIFIC_PASS + KBS_EDITORIAL_DEFECT = PASS_WITH_CORRECTIONS_OR_REVISION_REQUIRED
INTERNAL_TERMINOLOGY_LEAKAGE = CORRECTION_REQUIRED_UNLESS_SCIENTIFICALLY_INDISPENSABLE
UNSUPPORTED_OR_OVERSTATED_CLAIM = CORRECTION_REQUIRED_OR_BLOCKED
```

Un `PASS` exige que el bloque supere tanto la auditoría científica/editorial como la auditoría técnica.

### 3. Aplicación inmediata a Discussion B04

La ejecución `Discussion_B04_V01` ya está disponible para auditoría de IA Gestora. D-136 obliga a revisarla contra el texto real de §6.4, no solo contra los hashes declarados por IA Redacción. La auditoría debe inspeccionar especialmente:

- si la inspectabilidad/provenance se formula sin atribuir al sistema explicaciones causales no evaluadas del ranking;
- si las cifras RQ2/RQ3 conservan denominadores, unidad y modalidad del evaluador;
- si `AUDITABILITY ≠ LEGAL_CORRECTNESS` permanece intacto;
- si la prosa evita lenguaje interno de gobernanza/QA y nombres de campos o diagnósticos propios de la implementación;
- si el español es natural y no filtra anglicismos evitables;
- si no se introduce ninguna claim nueva, causalidad, deployment validation, human validation, novelty, SOTA o generalización externa.

### 4. Deuda editorial heredada

Detectar durante una auditoría actual que una sección ya integrada contiene terminología interna o prosa mejorable no autoriza modificarla silenciosamente. La observación debe registrarse como deuda editorial transversal y resolverse únicamente mediante un gate correctivo específico antes del cierre final del manuscrito.

---

## English

D-136 makes explicit that Managing-AI audits are substantive scientific-editorial reviews, not checksum or packaging checks. A block can pass only if scientific fidelity, claim strength, argumentative coherence, KBS editorial function, prose concreteness, terminology hygiene, bilingual naturalness, citation support, and technical integrity all pass together.

Internal project/QA/governance labels must not leak into publication prose unless they are scientifically indispensable and are presented as defined reader-facing scientific objects. Hashes, commits, gate labels, prompt/response identifiers, internal usernames, diagnostic codes, and implementation-field names belong in audit/governance artifacts rather than manuscript prose by default.

Discussion B04 V01 is subject immediately to this rule. Earlier integrated text is not silently reopened; any inherited issue is recorded as controlled editorial debt for a later authorized transversal cleanup.
