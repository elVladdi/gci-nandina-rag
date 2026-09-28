# Internal review — Discussion B06 / Section 6.6 prompt V01

## Español

```text
REVIEW = INTERNAL_PROMPT_REVIEW
PHASE = DISCUSSION
BLOCK = DISCUSSION_B06_SECTION_6_6
PROMPT = article/prompts/7_DISCUSSION_B06_SECTION6_6_V01.md
PROMPT_COMMIT = 395d368e5cb91e2d972f7c804a9f6801d15a53b7
PROMPT_GIT_BLOB = f01fb117ba583a99f283044a2e11c0151d6b61f9
SCIENTIFIC_BOUNDARY = article/governance/D145_DISCUSSION_B06_SECTION6_6_LIMITATIONS_BOUNDARY.md
SCIENTIFIC_BOUNDARY_GIT_BLOB = 5930273b3ad9d73f587533a080400a6676149ac8
CANONICAL_MASTER = ARTICLE_MASTER_V028
CANONICAL_MASTER_MD_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
BASELINE_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

### Revisión científica y de alcance

El prompt conserva el scope definido por D-145: §6.6 consolida límites ya establecidos y no abre nueva investigación. Cubre los dominios obligatorios de validez externa, dependencia intra-DAM y similitud residual, sensibilidad a composición/tamaño del banco histórico, objetos no estimables, drift documental, evaluación de explicación, límites de configurabilidad/generalización y estado actual del paquete público de reproducibilidad.

No autoriza nuevas cifras calculadas, resultados, inferencias, mecanismos causales, literatura o citas. La relación entre cada limitación y el claim que restringe está explícita. Se preservan las separaciones obligatorias `DAM_DISJOINT_PARTITIONS != IID_OBSERVATIONS`, `EXP11A_SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT`, `EXP11B_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE`, `DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS`, `AUDITABILITY != LEGAL_CORRECTNESS`, `LLM_AS_JUDGE != HUMAN_VALIDATION` y `CONFIGURABILITY != EMPIRICAL_GENERALIZATION`.

### Revisión editorial D-136 / KBS / SPCCR

El prompt exige lenguaje publicable y reader-facing y prohíbe filtrar nombres de experiments, gates, hashes, decisiones, usernames, labels de microauditoría o nombres de campos internos en el manuscrito. También distingue expresamente la deuda heredada de §6.2: puede describirse la sustancia de sus limitaciones en §6.6, pero no corregirse silenciosamente dentro de este bloque.

La estructura recomendada evita un inventario contractual y organiza la sección por fuentes de limitación y consecuencias inferenciales. El rango de 600–800 palabras inglesas es adecuado para consolidar los límites sin convertir §6.6 en una repetición de Results.

### Revisión operacional acumulativa

El prompt incluye onboarding completo, preflight `START_HERE`, baseline Markdown V028 exacto, baseline DOCX B05 V01 exacto, MWDP v1.0, SPCCR v1.0, KBS_EWG_34_V01, D-136, D-022, D-027 y D-035. Restringe el diferencial a §6.6 EN/ES; exige 48 comentarios heredados, cero tracked changes, auditoría OOXML y render completo; prohíbe reconstrucción Word desde Markdown, Base64 manual, chunking, fragmentación y reensamblado.

Los entregables y el gate de salida están definidos y la Conclusion permanece no autorizada.

```text
ONBOARDING_COMPLETENESS = PASS
BASELINE_IDENTITY_CONTROLS = PASS
SCIENTIFIC_SCOPE = PASS
LIMITATION_CLAIM_PROXIMITY = PASS
ANTI_OVERCLAIMING = PASS
INTERNAL_TERMINOLOGY_CONTROL = PASS
BILINGUAL_CONTROL = PASS
WORD_OOXML_CONTROL = PASS
D022_D027_D035 = PASS
CONCLUSION_BOUNDARY = PASS
MANDATORY_CORRECTIONS = NONE
FINAL_VERDICT = PASS
```

---

## English

The B06 V01 prompt passes internal review. It is scientifically bounded to consolidation of known limitations, preserves all inferential separations, prohibits new literature/results/inference and internal terminology leakage, requires reader-facing KBS prose, and carries forward the full operational protocol stack and exact baselines. No mandatory correction is required before execution authorization.