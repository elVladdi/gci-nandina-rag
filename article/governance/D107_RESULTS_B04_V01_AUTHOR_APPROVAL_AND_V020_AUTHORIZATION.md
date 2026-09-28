# D-107 — Results B04 V01 author approval and V020 promotion authorization

## Español

```text
DECISION = D-107
BLOCK = RESULTS_B04_SECTION_5_4
VERSION = V01
AUTHOR_DECISION = APPROVED
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_PROMOTION = ARTICLE_MASTER_V020
PROMOTION_MODE = BYTE_EXACT
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Aprobación autoral registrada

El autor aprobó explícitamente Results B04 V01 / Section 5.4 después del `PASS` independiente de IA Gestora registrado en D-106.

La aprobación corresponde exclusivamente a los siguientes candidatos exactos:

```text
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
MASTER_CANDIDATE_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
MASTER_CANDIDATE_MD_GIT_BLOB_EXPECTED = 7393bf0db2d577d27168ccbb2a1060f1b337c872

MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
MASTER_CANDIDATE_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

No se autoriza ninguna modificación adicional de §5.4 durante la promoción.

### 2. Estado de B04

Con la aprobación autoral:

```text
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
B04_V01 = AUTHOR_APPROVED
```

El contenido científico, numérico y bilingüe aprobado de §5.4 no debe reabrirse salvo defecto verificable o autorización editorial explícita posterior.

### 3. Promoción autorizada

Se autoriza exclusivamente la promoción byte-exacta:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V020.md
EXPECTED_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
EXPECTED_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872
```

`ARTICLE_MASTER_V019.md` continúa siendo canónico hasta que V020 sea materializado en GitHub y la IA Gestora verifique su identidad exacta.

Por D-035, IA Gestora no debe intentar materializar el master grande mediante Base64 manual, chunking, fragmentación, reensamblado ni otros workarounds. La materialización de V020 se realiza mediante subida directa del archivo exacto por el autor.

### 4. Word aprobado

El Word aprobado permanece bajo custodia local del autor:

```text
APPROVED_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

Después de verificar V020, este DOCX será el Word acumulativo canónico correspondiente a la promoción B04.

### 5. Límites y siguiente gate

```text
CANONICAL_MASTER_BEFORE_VERIFIED_PROMOTION = ARTICLE_MASTER_V019
ARTICLE_MASTER_V020 = AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION
RESULTS_B05_SECTION_5_5 = NOT_AUTHORIZED
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La aprobación de B04 no abre automáticamente B05. Después de materializar y verificar V020, IA Gestora deberá registrar la integración de B04 y solo entonces sincronizar independientemente el ground truth y el contrato editorial de Results B05 / §5.5.

---

## English

The author explicitly approved the exact Results B04 V01 candidates after Gestora PASS. B04 / Section 5.4 is closed, approved, frozen, and ready for integration. Only byte-exact promotion of the approved Markdown candidate to `ARTICLE_MASTER_V020.md` is authorized. V019 remains canonical until V020 is materialized and independently verified. Results B05+, Discussion, and Conclusion remain unauthorized.