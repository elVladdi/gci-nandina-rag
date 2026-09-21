# D-028 — Regeneración controlada del DOCX B06 perdido

## Estado

AUTHOR_CUSTODY_RECOVERY_FAILED / CONTROLLED_REGENERATION_AUTHORIZED / ACTIVE

## Motivo

La ejecución de recuperación registrada en `article/responses/3_INTRODUCTION_B01_B06_DOCX_RECOVERY_RESPONSE_V01.md@7d766844006f3ecd4d2603fcfa2af867bc3247d6` confirmó que el binario exacto `ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx` ya no está disponible en la sesión que lo generó. Por tanto, la identidad binaria reportada originalmente para B06 no puede recuperarse ni entregarse al autor.

D-027 prohíbe reconstruir silenciosamente un DOCX perdido y exige autorización específica de la IA Gestora para cualquier regeneración, con nueva identidad SHA-256 y trazabilidad explícita.

## Decisión

Se autoriza una regeneración controlada y exclusivamente técnica del DOCX acumulativo B06 bajo las siguientes condiciones:

1. El punto de partida debe ser el DOCX B05 aprobado y efectivamente disponible, identificado por SHA-256:

   `042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

2. El contenido científico de B06 NO se vuelve a redactar. Debe insertarse exactamente la Section 2.6 aprobada y congelada, usando como fuente canónica:

   - `article/sections/related_work/RelatedWork_B06_V01.md`;
   - `article/manuscript/ARTICLE_MASTER_V006.md`;
   - Git blob canónico `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`.

3. Sections 2.1–2.5, en inglés y español, deben permanecer sin cambios respecto del DOCX B05 aprobado.

4. Los 32 comentarios heredados de B05 deben preservarse íntegramente.

5. Deben recrearse únicamente los cuatro comentarios de auditoría correspondientes a las cuatro citas inglesas de B06. Cada comentario debe anclarse a la cita pertinente y contener evidencia verificable obtenida nuevamente de la fuente primaria correspondiente. No se presume que los comentarios recreados sean byte-for-byte idénticos a los perdidos; deben ser semánticamente adecuados y trazables.

6. El DOCX regenerado debe considerarse un NUEVO binario. Bajo ninguna circunstancia puede conservar como identidad gobernante el SHA-256 perdido `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0` salvo coincidencia fortuita demostrada, que no debe esperarse ni forzarse.

7. El nuevo SHA-256 debe calcularse, registrarse y pasar a ser la identidad gobernante del DOCX B06 regenerado únicamente después de QA y entrega efectiva al autor.

8. El archivo regenerado debe entregarse al autor como archivo descargable en la misma sesión de ejecución. `AUTHOR_HANDOFF = COMPLETED` solo puede declararse después de esa entrega.

9. La regeneración no reabre la aprobación científica de B06. El texto aprobado permanece `APPROVED / FROZEN / INTEGRATED`; lo que se reconstruye es exclusivamente el soporte DOCX acumulativo perdido.

10. Introduction B01 permanece bloqueada hasta que la regeneración, QA y entrega al autor hayan concluido correctamente.

## QA obligatorio

Antes de entregar el DOCX regenerado, la IA de Redacción debe verificar y registrar:

- SHA-256 del baseline B05 exacto;
- 32/32 comentarios heredados preservados;
- texto de Sections 2.1–2.5 preservado;
- Section 2.6 inglesa y española semánticamente idéntica al B06 aprobado, sin reescritura;
- cuatro citas inglesas de B06 presentes;
- cuatro comentarios B06 recreados y correctamente anclados;
- total de 36 comentarios;
- cero tracked changes;
- integridad OOXML;
- render completo sin clipping, solapamiento o pérdida de contenido;
- nuevo SHA-256 del binario regenerado;
- archivo entregado efectivamente al autor.

## Estado durante la recuperación

```text
RELATED_WORK_B06_SCIENTIFIC_STATUS = APPROVED / FROZEN / INTEGRATED
ORIGINAL_B06_DOCX_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0 / LOST_BINARY
B06_DOCX_REGENERATION = AUTHORIZED
INTRODUCTION_B01 = AUTHORIZED / BLOCKED_PENDING_REGENERATED_DOCX_HANDOFF
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
