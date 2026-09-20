# D-016 — Aprobación e integración de Related Work B01 y apertura de B02 / Related Work B01 Approval, Integration, and B02 Start

## Español

```text
DECISION_ID = D-016
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
INTERNAL_REVIEW = PASS
BLOCK = RELATED_WORK_B01
BLOCK_REVISION = V01
SECTION = 2.1 Automated tariff classification and candidate retrieval
DELIVERY_COMMIT = 9a3acddeee01bd3c78f1b06306b8619a9ad5ccd6
BLOCK_STATUS = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V001
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V001.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V001.docx
CANONICAL_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEXT_BLOCK = RELATED_WORK_B02
NEXT_SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
RELATED_WORK_B02 = AUTHORIZED
SECTIONS_2_3_TO_2_6 = NOT_AUTHORIZED
```

### Decisión

El autor aprobó expresamente `Related Work B01 V01` condicionado a la auditoría de la IA Gestora. La revisión independiente concluyó `PASS` sin correcciones materiales, por lo que la aprobación queda efectiva y el bloque se congela e integra como primera incorporación canónica bajo la nueva estructura KBS.

La integración canónica debe preservar exactamente el contenido científico aprobado y los ocho comentarios de auditoría anclados a las citas inglesas. No se autoriza reutilizar automáticamente prosa rechazada de Methods B01.

### Master canónico

La primera versión canónica bajo la arquitectura aprobada por D-015 es:

- `article/manuscript/ARTICLE_MASTER_V001.md`
- `article/manuscript/ARTICLE_MASTER_V001.docx`

El DOCX canónico debe ser binariamente equivalente al candidato B01 aprobado, con SHA-256 `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5`.

El cover interno conserva etiquetas heredadas del bootstrap estructural. Se registra como asunto de formato no bloqueante; cualquier normalización posterior deberá realizarse de forma controlada sin alterar contenido, comentarios ni trazabilidad aprobados.

### Apertura de B02

Se autoriza exclusivamente `Related Work B02 — Section 2.2 Knowledge-enhanced retrieval and regulatory reasoning`.

B02 deberá partir de `ARTICLE_MASTER_V001.docx` y preservar íntegramente la sección 2.1 aprobada. Su función será sintetizar cómo fuentes documentales, conocimiento estructurado, reglas, retrieval y agentes intervienen en sistemas de clasificación/razonamiento regulatorio, distinguiendo cuándo el conocimiento participa en la decisión de clasificación, cuándo se usa como contexto recuperado y cuándo sirve como evidencia o soporte. No debe describir todavía la arquitectura del presente estudio, su Top-3 fijo, NANDINA Chapter 87 ni resultados propios.

La subsección deberá cerrar preparando 2.3 sobre LLMs para clasificación, razonamiento y explicación. `FINAL_GAP` y novelty universal continúan prohibidos.

---

## English

The author approved Related Work B01 V01 subject to the Managing AI audit. The independent audit passed with no material corrections, making the approval effective. B01 is therefore approved, frozen, and integrated as the first canonical manuscript increment under the D-015 structure.

The canonical master is `ARTICLE_MASTER_V001.md/.docx`; the DOCX must remain binary-equivalent to the approved candidate and retain all eight citation-audit comments. Its SHA-256 is `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5`.

Only Related Work B02 / Section 2.2 is now authorized. It must start from the canonical V001 master, preserve approved 2.1 unchanged, synthesize the functional roles of external knowledge/documentary retrieval/regulatory reasoning, and stop before Section 2.3. No present-study architecture, testbed, results, final gap, or universal novelty claim is authorized.