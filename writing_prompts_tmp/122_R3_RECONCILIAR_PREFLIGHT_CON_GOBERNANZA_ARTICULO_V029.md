# PROMPT122-R3 — G7-F03: RECONCILIAR PREFLIGHT CON GOBERNANZA VIGENTE DEL ARTÍCULO Y GATE V029

## 0. Estado

Este prompt corrige exclusivamente la **hoja de ruta y gobernanza** derivadas de 122-R2. No corrige ciencia del artículo y no edita el manuscrito.

Lee primero:

```text
writing_prompts_tmp/122_R2_AUDITORIA_EXTERNA_REVISION_REQUIRED_GOBERNANZA.md
commit = e3f53775651a9bc5b26654971ff119bacf54f253
```

Estado vinculante:

```text
PROMPT122_R2_EXTERNAL_AUDIT = REVISION_REQUIRED_GOVERNANCE_ONLY
SCIENTIFIC_ALIGNMENT_AUDIT = PASS
V028_FILE_COMPLETENESS_AUDIT = PASS
ARTICLE_WORKFLOW_GOVERNANCE_AUDIT = REVISION_REQUIRED
123_AUTHORIZED = false
```

No ejecutes 123 ni ningún bloque posterior.

---

## 1. Actor

Actúa como **IA Gestora de Artículo** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No modifiques la tesis final. No edites ni promociones el artículo en este bloque. No ejecutes Grupo 8.

---

## 2. Fuentes gobernantes obligatorias

Trabaja con el snapshot de la rama del artículo:

```text
repository = elVladdi/gci-nandina-rag
branch = article/main-manuscript
snapshot_commit = 235893711cedca743a506f4f5da8f779268b8ed0
```

Lee íntegramente y reconcilia:

```text
article/ARTICLE_STATUS.md
article/ARTICLE_WRITING_PLAN.md
article/DECISIONS.md
article/manuscript/ARTICLE_MASTER_V028.md
```

Además, usa como diagnóstico científico ya auditado:

```text
writing_prompts_tmp/122_R2_RESPUESTA_G7_F03_PREFLIGHT_ARTICLE_MASTER_V028.md
commit = 1edfc04b6cb08204796c957f2852b730835636ae
```

Y como gate de tesis:

```text
writing_prompts_tmp/121N_AUDITORIA_EXTERNA_PASS.md
commit = be902fa0df0cc40ac9a5ad2cb8a040dc3ceeb9e6
```

No sustituyas V028 por V026/V027. V028 sigue siendo el master canónico hasta verificar V029.

---

## 3. Hechos de gobernanza que debes preservar

Debes verificar y registrar explícitamente, sin reinterpretarlos:

```text
ARTICLE_WRITING_PLAN = V3.49
LATEST_EDITORIAL_DECISION = D-150
CANONICAL_MASTER = ARTICLE_MASTER_V028
TARGET_CANONICAL_MASTER = article/manuscript/ARTICLE_MASTER_V029.md
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_SECTION_6_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B05_SECTION_6_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B06_SECTION_6_6 = AUTHOR_APPROVED / V029_PROMOTION_PENDING_VERIFICATION
DISCUSSION_B06_INTEGRATION = PENDING_V029_VERIFICATION
CURRENT_GATE = DISCUSSION_B06_V029_PROMOTION_VERIFICATION
NEXT_ACTION = MATERIALIZE_EXACT_APPROVED_B06_V02_AS_ARTICLE_MASTER_V029
CONCLUSION = NOT_AUTHORIZED
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
```

La promoción autorizada por D-150 es byte-exacta y no puede mezclarse con las correcciones científicas post-tesis detectadas por 122-R2.

---

## 4. Propósito exclusivo

Corrige el **plan de continuidad de G7-F03** para que sea compatible simultáneamente con:

1. el diagnóstico científico válido de 122-R2;
2. el hecho de que V028 es el master canónico vigente;
3. el hecho de que 6.6 B06 V02 ya está aprobado por el autor y solo falta su promoción/verificación como V029;
4. el freeze previo de Experimental design, Results 5.1–5.7 y Discussion 6.1–6.5;
5. la deuda editorial controlada de 6.2;
6. la conclusión todavía no autorizada;
7. la necesidad posterior de sincronizar el artículo con la tesis final sin borrar la historia de aprobaciones del artículo.

No edites `ARTICLE_MASTER_V028.md` y no materialices `ARTICLE_MASTER_V029.md` en este prompt.

---

## 5. Correcciones obligatorias al preflight 122-R2

### 5.1. Separar estado del archivo y estado del flujo

Para cada componente relevante, distingue:

```text
CANONICAL_V028_FILE_STATE
ARTICLE_WORKFLOW_STATE
```

Ejemplo obligatorio para 6.6:

```text
CANONICAL_V028_FILE_STATE = PLACEHOLDER
ARTICLE_WORKFLOW_STATE = AUTHOR_APPROVED / V029_PROMOTION_PENDING_VERIFICATION
```

No vuelvas a describir 6.6 como trabajo de redacción pendiente desde cero.

### 5.2. Mantener hallazgos científicos válidos

Conserva los seis hallazgos no-KEEP de 122-R2 salvo que una fuente gobernante del artículo demuestre que alguno ya fue corregido en un candidato aprobado posterior a V028:

- ARS-010 reranker diagnóstico en Methods;
- ARS-011 reranker en Results/Discussion;
- ARS-013 eliminar `schema compliance = 0/50` como métrica;
- ARS-015 verificar Decisiones 885/906;
- ARS-016 verificar denominación de asociación exacta NANDINA-8;
- ARS-018 revalidar estado del paquete público de reproducibilidad.

Si alguno ya está resuelto en B06 V02, registra `RESOLVED_IN_APPROVED_PENDING_PROMOTION` y no lo programes otra vez.

### 5.3. Respetar contenido congelado

Experimental design, Results 5.1–5.7 y Discussion 6.1–6.5 no deben tratarse como texto libremente editable. Para cualquier cambio post-tesis que resulte necesario, el plan debe prever un **gate explícito de reapertura/sincronización controlada**, con modificación mínima y trazabilidad de qué freeze se altera y por qué.

### 5.4. Gate V029 primero

La hoja de ruta corregida debe colocar antes de cualquier edición científica nueva:

```text
GATE_0 = MATERIALIZE_AND_VERIFY_BYTE_EXACT_V029_FROM_APPROVED_B06_V02
```

Este gate no cuenta como redacción científica nueva. No debes ejecutarlo ahora; solo debes reconocerlo como siguiente acción gobernante.

### 5.5. Conclusion

La conclusión permanece:

```text
CONCLUSION = NOT_AUTHORIZED
```

No la programes como redacción inmediata antes de cerrar el gate V029 y los futuros gates de sincronización que la gobernanza requiera.

---

## 6. Nueva hoja de ruta requerida

Produce una secuencia corregida que distinga al menos:

1. **Gate técnico de V029** — promoción byte-exacta de B06 V02 ya aprobado y verificación independiente;
2. **Gate de sincronización científica post-tesis** — reabrir de manera controlada solo las secciones congeladas afectadas por ARS-010/011/013 y resolver ARS-015/016/018;
3. **Gate de coherencia de Discussion** — preservar B06 V02 aprobado y tratar deuda de 6.2 sin reescribir innecesariamente otras subsecciones;
4. **Conclusion** — solo cuando sea autorizada por la gobernanza del artículo;
5. figuras/tablas;
6. referencias y end matter;
7. front matter final;
8. limpieza/coherencia global del master de envío;
9. auditoría final del artículo.

Puedes agrupar gates únicamente si la gobernanza existente lo permite. No fuerces el número siete de 122-R2 si ya no es correcto.

Debes informar:

```text
ESTIMATED_REMAINING_TECHNICAL_GATES = <n or range>
ESTIMATED_REMAINING_SUBSTANTIVE_BLOCKS = <n or range>
ESTIMATED_REMAINING_FINAL_AUDITS = <n or range>
```

---

## 7. Prohibiciones

No:

- edites V028;
- materialices V029;
- modifiques B06 V02;
- redactes Conclusion;
- ejecutes correcciones ARS-010/011/013 todavía;
- modifiques la tesis final;
- uses web;
- agregues referencias;
- ignores D-150;
- borres o reescribas la historia de aprobaciones del artículo;
- ejecutes Grupo 8;
- autorices 123.

---

## 8. Salida obligatoria

Publica exclusivamente:

```text
writing_prompts_tmp/122_R3_RESPUESTA_RECONCILIAR_PREFLIGHT_CON_GOBERNANZA_ARTICULO.md
```

Debe contener como mínimo:

```text
PROMPT122_R3_EXECUTION = COMPLETE | REVISION_REQUIRED | STOPPED_PRECONDITION
CANONICAL_MASTER = ARTICLE_MASTER_V028
CURRENT_GATE = DISCUSSION_B06_V029_PROMOTION_VERIFICATION
B06_V02 = AUTHOR_APPROVED / PENDING_V029_PROMOTION_VERIFICATION
CONCLUSION = NOT_AUTHORIZED
SCIENTIFIC_FINDINGS_FROM_122_R2_PRESERVED = true|false
ARTICLE_MODIFIED = false
V029_MATERIALIZED = false
THESIS_MODIFIED = false
GROUP8_EXECUTED = false
123_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Incluye:

1. tabla de reconciliación `CANONICAL_V028_FILE_STATE` vs `ARTICLE_WORKFLOW_STATE`;
2. estado corregido de cada hallazgo ARS-010/011/013/015/016/018;
3. hoja de ruta corregida y ordenada por gates;
4. estimación revisada de bloques/gates restantes;
5. bloqueadores autorales/administrativos reales;
6. siguiente acción gobernante exacta, sin ejecutarla.

---

## 9. Parada obligatoria

Al finalizar, detente para auditoría externa.

No materialices V029 y no ejecutes ningún bloque posterior.
