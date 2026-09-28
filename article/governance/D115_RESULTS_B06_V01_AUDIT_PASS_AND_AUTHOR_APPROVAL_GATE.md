# D-115 — Results B06 V01 audit PASS and author approval gate

## Español

```text
DECISION = D-115
BLOCK = RESULTS_B06_SECTION_5_6
SECTION = 5.6 INFERENTIAL RESULTS
GESTORA_REVIEW = PASS
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_UNTIL_AUTHOR_APPROVAL
CANONICAL_MASTER = ARTICLE_MASTER_V021
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

IA Gestora auditó independientemente Results B06 V01 bajo D-113/D-114 y emitió `PASS` en:

`article/reviews/6_RESULTS_B06_SECTION5_6_INTERNAL_REVIEW_V01.md@5dd4f0b4632b81acb3c713a2c22732582675cd53`

La respuesta y sección versionadas verificadas son:

```text
RESPONSE = article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md@e7e9ab0efb137243471bd0dc1feb4363b9b1c7d7
SECTION = article/sections/results/Results_B06_V01.md@cbb5cafdf3c9725c0d0caefa565ba694ead93349
SECTION_GIT_BLOB = 092e8f9af2cd96ac7d6ad41f193bd7486ec40938
```

Los únicos candidatos elegibles para aprobación son exactamente:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
GIT_BLOB_EXPECTED = 088eecd537997a3438517f7d206f6d890b0aa064

ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 58
```

El `PASS` cubre:

- identidad exacta de los candidatos recibidos;
- modificación exclusiva de §5.6 inglesa y española;
- fidelidad de los 15 contrastes HE2_A y del contraste HE2_B al ground truth congelado;
- uso correcto de 99% CI para las cinco métricas primarias por familia bajo el control Bonferroni familywise-95% y 95% CI para HE2_B;
- `HE2 = SUPPORTED` exclusivamente dentro del alcance inferencial interno congelado;
- `HE5 = INCONCLUSIVE` sin nuevo test;
- ausencia de p-values, causalidad, generalización externa, accuracy global del framework y corrección jurídica;
- equivalencia EN/ES y Markdown↔DOCX;
- integridad OOXML, 40 comentarios, 0 tracked changes y render de 58 páginas;
- cumplimiento D-035.

B06 / §5.6 queda `GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL`. El `PASS` no equivale a aprobación autoral ni autoriza integración. `ARTICLE_MASTER_V021.md` continúa siendo el master canónico.

Si el autor aprueba, la única promoción permitida será la materialización byte-exacta de `ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md` como:

`article/manuscript/ARTICLE_MASTER_V022.md`

con identidad esperada:

```text
SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
```

Después de su materialización, IA Gestora deberá verificar la promoción antes de integrar B06 y antes de decidir si §5.7 aporta valor suficiente para ser redactada o si debe omitirse por redundancia, conforme a la estructura congelada. B07 no se abre por anticipado.

### Gate vigente

```text
CURRENT_GATE = RESULTS_B06_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_RESULTS_B06_V01
APPROVAL_OBJECT_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
APPROVAL_OBJECT_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
APPROVAL_OBJECT_MD_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
APPROVAL_OBJECT_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
APPROVAL_OBJECT_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
CANONICAL_MASTER_UNTIL_APPROVAL_AND_PROMOTION = ARTICLE_MASTER_V021
TARGET_IF_APPROVED = ARTICLE_MASTER_V022
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

Results B06 V01 passed the independent Gestora audit and now awaits explicit author approval. V021 remains canonical. If approved, only byte-exact promotion of the audited B06 Markdown candidate to V022 is permitted, followed by Gestora verification. Section 5.7, Discussion, and Conclusion remain unauthorized.