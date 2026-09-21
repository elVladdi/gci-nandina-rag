# D023 — Minimal execution mode for approved technical closures

## Español

### Estado

AUTHOR_APPROVED / ACTIVE / BINDING

### Decisión

Cuando un bloque ya tenga `INTERNAL_REVIEW = PASS` y `AUTHOR_APPROVAL = YES`, y la IA Gestora emita un prompt de **cierre técnico**, la IA de Redacción debe operar en modo mínimo de ejecución.

1. No debe reabrir la revisión científica, bibliográfica, estilística ni experimental ya cerrada.
2. No debe volver a consultar literatura, fuentes primarias, `SOURCE_REGISTRY`, `CLAIM_EVIDENCE_MATRIX`, corpus KBS, evidencias experimentales ni el DOCX, salvo que el prompt de cierre lo requiera expresamente por una inconsistencia concreta.
3. El onboarding obligatorio se realiza una sola vez al inicio de la ejecución. No se deben repetir lecturas o verificaciones ya completadas durante la misma ejecución.
4. Los artefactos textuales UTF-8 (`.md`, `.txt`, `.json`, `.csv` cuando corresponda) se transfieren como texto UTF-8 directo. Queda prohibido convertirlos a Base64 para fines de commit ordinario.
5. Queda prohibido fragmentar, trocear, recomponer o analizar por bloques un archivo textual únicamente para subirlo a GitHub. No usar fragmentos de 20k, 60k ni cualquier otra partición artificial.
6. Para un cierre con varios archivos textuales y un único commit, el procedimiento preferido es: verificar HEAD una vez → verificar una vez los hashes locales exigidos → crear un blob UTF-8 por archivo → crear un único tree → crear un único commit → actualizar el ref por fast-forward → verificar el HEAD final una vez.
7. No realizar pruebas repetidas de conectividad, existencia de blobs, `git hash-object`, codificaciones alternativas o round-trips remotos cuando el prompt no las solicite.
8. Si una única llamada UTF-8 para un archivo textual falla por límite o error del conector, detenerse inmediatamente. No intentar Base64, fragmentación, placeholders, commits auxiliares, ramas temporales ni force push. Aplicar D022 para la respuesta de bloqueo.
9. La creación de blobs huérfanos que no se vinculen a un tree/commit no modifica la rama; aun así, no deben crearse como pruebas exploratorias.
10. El objetivo del cierre técnico es versionar exactamente los artefactos ya aprobados, no volver a demostrar su contenido científico.

### Aplicación inmediata a B05 V01

Para `RELATED_WORK_B05 / V01`, el cierre debe limitarse a los dos Markdown científicos ya aprobados y al informe Markdown autorizado. El DOCX permanece bajo D021. No se requiere Base64 para ningún archivo.

## English

### Status

AUTHOR_APPROVED / ACTIVE / BINDING

### Decision

When a block already has `INTERNAL_REVIEW = PASS` and `AUTHOR_APPROVAL = YES`, and the Managing AI issues a **technical-closure** prompt, the Drafting AI must use minimal execution mode.

1. Do not reopen scientific, bibliographic, stylistic, experimental, or editorial review that has already been closed.
2. Do not re-consult literature, primary sources, `SOURCE_REGISTRY`, `CLAIM_EVIDENCE_MATRIX`, the KBS corpus, experimental evidence, or the DOCX unless the closure prompt explicitly requires it for a specific inconsistency.
3. Complete mandatory onboarding once at the beginning of the execution. Do not repeat reads or checks already completed during the same execution.
4. UTF-8 text artifacts (`.md`, `.txt`, `.json`, `.csv` where applicable) must be transferred directly as UTF-8 text. Base64 conversion is prohibited for ordinary textual commits.
5. Do not split, chunk, reconstruct, or inspect a text file in artificial fragments solely to upload it to GitHub.
6. For a multi-file textual closure requiring one commit, the preferred procedure is: verify HEAD once → verify required local hashes once → create one UTF-8 blob per file → create one tree → create one commit → fast-forward the ref → verify final HEAD once.
7. Do not repeat connectivity checks, blob-existence checks, `git hash-object` calculations, alternate encodings, or remote round-trips unless explicitly required.
8. If a single UTF-8 upload call fails because of a connector limit or error, stop immediately. Do not fall back to Base64, chunking, placeholders, auxiliary commits, temporary branches, or force push. Apply D022 for the stop response.
9. Unreferenced blobs do not modify the branch, but they must not be created as exploratory tests.
10. The purpose of technical closure is to version already approved artifacts, not to re-prove their scientific content.

### Immediate application to B05 V01

For `RELATED_WORK_B05 / V01`, closure is limited to the two already approved scientific Markdown files and the authorized Markdown response. The DOCX remains governed by D021. No Base64 operation is required for any file.
