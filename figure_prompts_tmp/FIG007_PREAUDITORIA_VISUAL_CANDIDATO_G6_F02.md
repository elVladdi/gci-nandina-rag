# FIG007 — PREAUDITORÍA VISUAL Y CIENTÍFICA DEL CANDIDATO G6-F02

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto `elVladdi/gci-nandina-rag`.

Ejecuta exclusivamente una **preauditoría no gobernante** del candidato ya publicado de G6-F02. Esta tarea NO activa, ejecuta ni cierra G6-F03; NO modifica G6-F02; NO integra nada a `main`; NO modifica Plan Maestro, fichas, artículo ni tesis.

El propósito es aprovechar el intervalo antes de la corrección técnica final de G6-F02 para detectar de una sola vez cualquier problema visual, científico o de accesibilidad adicional que convenga corregir junto con los defectos ya conocidos.

No generes nuevas figuras ni scripts. No edites los artefactos. Solo audita y persiste tu dictamen.

---

## 1. Estado rector congelado

Candidato G6-F02 a auditar:

```text
branch = figures/g6-f02-render-v01
commit = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
parent = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

Contrato científico/visual rector integrado en `main`:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
blob = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
```

Estado operacional actual:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

Prompt104 quedó interrumpido por límite de uso después de publicar el candidato. Existe además un prompt técnico correctivo ya versionado:

```text
codex_prompts_tmp/105_CORREGIR_G6_F02_HASH_LEDGER_Y_ACCESIBILIDAD_FIG03.md
commit = 75197b8c48d4290fee05642e388194a56aa6c569
```

No lo ejecutes ni lo modifiques. Úsalo solo para conocer los dos defectos ya detectados:

1. ledger SHA-256 ligado a bytes materializados CRLF en vez de bytes canónicos Git;
2. etiquetas categóricas de G6-FIG-03 a 7.5 pt cuando el registry exige mínimo efectivo 8.5 pt.

Tu tarea es buscar **cualquier otro problema** antes de que se ejecute la corrección técnica.

---

## 2. Artefactos que debes revisar íntegramente

### Registry rector

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

### Figuras candidatas

```text
figures/group6/g6_fig_01_he2.svg@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
figures/group6/g6_fig_01_he2.png@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5

figures/group6/g6_fig_02_phase_e.svg@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
figures/group6/g6_fig_02_phase_e.png@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5

figures/group6/g6_fig_03_exp11a.svg@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
figures/group6/g6_fig_03_exp11a.png@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

### Scripts candidatos

```text
src/figures/group6/render_g6_fig_01_he2.py@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
src/figures/group6/render_g6_fig_02_phase_e.py@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
src/figures/group6/render_g6_fig_03_exp11a.py@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

### Ledger candidato

```text
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

---

## 3. Auditoría obligatoria por figura

Para cada figura verifica, claim por claim y regla por regla:

1. correspondencia exacta con su especificación del registry;
2. panel count y layout;
3. métricas representadas y ninguna adicional;
4. ejes, unidades, escalas y rangos;
5. orden categórico congelado;
6. marcas y codificación semántica;
7. niveles de incertidumbre autorizados;
8. ausencia de incertidumbre no autorizada;
9. denominadores/N y contexto mostrado;
10. ausencia de sobreclaim visual;
11. ausencia de inferencia nueva;
12. legibilidad a tamaño de publicación;
13. tamaño efectivo de tipografías;
14. posibles solapamientos o recortes;
15. legibilidad en escala de grises;
16. que el color no sea el único canal semántico;
17. consistencia visual entre las tres figuras;
18. si títulos y anotaciones internas son adecuados para una figura científica y no confunden identificadores internos con títulos editoriales;
19. si el SVG y PNG representan la misma información científica;
20. cualquier defecto que pueda justificar una corrección antes de integrar G6-F02.

No rebajes un defecto porque pueda corregirse luego en G6-F03: si afecta la figura generada o su accesibilidad, debes identificarlo ahora.

---

## 4. Guardrails científicos

Preserva estrictamente:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

No derives nuevas métricas, CI, p-values, tendencias, efectos ni conclusiones.

G6-FIG-01:
- Panel A sin CI por brazo;
- Panel B: 15 contrastes y CI 99%;
- Panel C: un solo contraste HE2_B y CI 95%;
- no convertir `Pool@200` en evidencia confirmatoria adicional.

G6-FIG-02:
- descriptiva;
- 15 marcas;
- cuatro variantes formales + una contextual;
- sin CI/p-values/líneas/tendencias;
- diagnostic union excluida.

G6-FIG-03:
- seis paneles;
- 31 corridas observadas;
- `10 / 5 / 5 / 10 / 1`;
- H100 como referencia única;
- tamaño y composición varían conjuntamente;
- sin resumen estadístico nuevo ni lectura causal/monótona de tamaño.

---

## 5. Clasificación de hallazgos

Clasifica cada hallazgo como:

```text
BLOCKING
MAJOR_NONBLOCKING
MINOR
NO_ISSUE
```

Para cada hallazgo indica:

```text
finding_id
figure_id
severity
registry_requirement
observed_candidate_behavior
evidence_path
scientific_or_visual_risk
required_correction
whether_already_covered_by_Prompt105 = true/false
```

No propongas cambios puramente decorativos sin utilidad científica o editorial.

---

## 6. Dictamen requerido

Emite uno de:

```text
PASS_EXCEPT_KNOWN_PROMPT105_CORRECTIONS
ADDITIONAL_CORRECTIONS_REQUIRED
REJECT_CANDIDATE
```

Si hay correcciones adicionales, agrúpalas de forma que puedan incorporarse a **una sola ejecución correctiva** cuando vuelva a estar disponible el ejecutor local.

No autorices integración ni G6-F03.

---

## 7. Persistencia obligatoria

Guarda tu respuesta completa en:

```text
figure_prompts_tmp/FIG007_RESPUESTA_PREAUDITORIA_VISUAL_CANDIDATO_G6_F02.md
```

sobre:

```text
codex/prompts-temporary
```

La respuesta debe contener como mínimo:

```text
FIG007_PREAUDIT_RESULT
CANDIDATE_COMMIT
REGISTRY_COMMIT_OR_BLOB
FIGURE_01_AUDIT
FIGURE_02_AUDIT
FIGURE_03_AUDIT
ACCESSIBILITY_AUDIT
SCIENTIFIC_FIDELITY_AUDIT
CROSS_FIGURE_CONSISTENCY_AUDIT
KNOWN_PROMPT105_FINDINGS_CONFIRMED
ADDITIONAL_FINDING_COUNT
FINDINGS
RECOMMENDED_SINGLE_CORRECTION_SCOPE
G6_F02_APPROVAL_AUTHORIZED = false
G6_F03_AUTHORIZED = false
```

En el chat devuelve únicamente rama, archivo de respuesta y commit.