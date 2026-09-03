# 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y fuentes normativas / Data, provenance, reproducibility, knowledge, and normative sources

## Español

### 1. Propósito

`0B-05` completa el mapa bibliográfico de la Fase 0B en tres dimensiones que no deben confundirse entre sí:

1. **documentación y gobernanza de datos**;
2. **procedencia, trazabilidad, reproducibilidad y auditoría del ciclo de vida**;
3. **fundamentos conceptuales de información/conocimiento y autoridad documental de fuentes normativas oficiales**.

El bloque no busca demostrar novelty. Su función es establecer qué puede sostenerse científicamente cuando el artículo describa el banco histórico, el corpus normativo, su versionamiento, la trazabilidad de artefactos, la reproducibilidad del experimento, el conocimiento explícito documental y el carácter autoritativo —pero no automáticamente suficiente— de las fuentes regulatorias.

Debe impedir equivalencias inválidas como:

- `documentar un dataset = demostrar que el dataset es adecuado`;
- `versionar = reproducir`;
- `provenance = correctness`;
- `traceability = auditability completa`;
- `reproducibility = external replication/generalization`;
- `audit trail = legal correctness`;
- `documento normativo recuperado = aplicación jurídica correcta`;
- `conocimiento explícito documental = totalidad del conocimiento experto`.

### 2. Criterio de partición

Por heterogeneidad conceptual, 0B-05 se divide en tres sub-lotes. Solo uno puede estar abierto a la vez.

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:

`article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Lote final:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**; se conserva el nombre físico del archivo suministrado sin corregir silenciosamente su metadata desde fuentes externas.

Objetivo gobernante de 0B-05A:

`DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`

sin convertir esa cadena en:

`CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

El sub-lote debe distinguir de manera explícita:

- dataset documentation de dataset quality;
- dataset identity/version de dataset description;
- provenance/lineage de mera presencia de archivos;
- reproducibility de replication y generalization;
- lifecycle/internal audit de output-level auditability;
- transparency trail de substantive correctness;
- disponibilidad de código/datos de capacidad real de reproducir un resultado bajo las mismas condiciones.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse y abrirse después del freeze de 0B-05A.

Fuentes candidatas heredadas, sujetas a confirmación primaria antes de apertura:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- `Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge` únicamente si se confirma acceso al PDF primario completo dentro del corpus heredado.

Objetivo previsto: delimitar `data`, `information`, `documented/explicit knowledge`, conocimiento tácito/no codificado y el alcance legítimo de describir un corpus normativo como conocimiento explícito documental. No se permitirá presentar la recuperación documental como sustituto de conocimiento experto ni adoptar una pirámide DIKW como transformación automática si las fuentes no la sostienen.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B y de verificar qué fuentes oficiales primarias del corpus vigente requieren auditoría documental adicional.

Su función no será una revisión académica, sino una **auditoría de fuente primaria oficial** separada, siguiendo `article/BIBLIOGRAPHIC_FRAMEWORK.md`: autoridad emisora, versión, vigencia, fecha, alcance, jerarquía documental, identificador/enlace estable y función evidencial. Las fuentes WCO/OMA, Comunidad Andina y SUNAT no se tratarán como artículos científicos ni se usarán para sustituir literatura académica cuando el claim sea metodológico.

### 3. Relación con los freezes previos

0B-05 no reabre:

- 0A-01 ni 0A-02;
- los resultados experimentales congelados;
- 0B-01 a 0B-04B;
- G6, eliminado como candidato a gap;
- G7, absorbido en F2.

0B-05A puede aportar fundamento metodológico para describir documentación, versionamiento, provenance, reproducibilidad y audit trails, pero **no puede corregir ni reinterpretar** hechos experimentales congelados.

### 4. Relación con F1–F5

0B-05 es principalmente fundacional y de gobernanza. No constituye por sí mismo evidencia de ausencia de prior art aduanero.

- **F1:** normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE` en 0B-05A; la función de fuentes históricas/normativas ya fue auditada en lotes aduaneros.
- **F2:** normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE` en 0B-05A.
- **F3:** puede recibir `METHOD_FOUNDATION_RELEVANT` cuando documentación de composición/particiones/curación ayude a justificar por qué deben declararse unidades y dependencias, sin convertir documentación genérica en prueba de leakage.
- **F4:** puede recibir `METHOD_BOUNDARY_RELEVANT` para separar reproducibilidad/provenance de correctness sustantiva.
- **F5:** puede recibir `METHOD_BOUNDARY_RELEVANT` para distinguir audit trail, accountability y documentación de una evaluación formal y separada de auditabilidad por salida.

Estas etiquetas no demuestran novelty ni gap.

### 5. Gate de 0B-05A

Gate activo:

`0B-05A READY_FOR_DRAFTING -> IA de redacción -> revisión científica/editorial interna contra los cinco PDF primarios -> corrección si aplica -> aprobación expresa del autor -> freeze -> definir/abrir 0B-05B`.

La IA experimental solo interviene si una interpretación bibliográfica amenaza o modifica un hecho/claim experimental congelado o una restricción bajo su autoridad.

### 6. Prohibiciones

Durante 0B-05A:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva;
- no usar otros PDF del corpus para completar información del lote;
- no confundir documentación con calidad o validez;
- no confundir reproducibilidad con replicación externa o generalización;
- no convertir audit trail en corrección jurídica;
- no modificar 0A ni el Plan Maestro;
- no abrir 0B-05B, 0B-05C, 0B-06 o 0C antes del gate correspondiente.

---

## English

### 1. Purpose

`0B-05` completes the Phase-0B literature map across three dimensions that must remain distinct: dataset documentation/governance; provenance, traceability, reproducibility, and lifecycle audit; and conceptual information/knowledge plus official normative-source authority.

The block is not a novelty search. It establishes the scientific basis for describing the historical bank and normative corpus, artifact versioning, workflow provenance, reproducibility, documented explicit knowledge, and the authority — but not automatic substantive sufficiency — of regulatory sources.

Invalid equivalences to prevent include `documentation = dataset adequacy`, `versioning = reproducibility`, `provenance = correctness`, `traceability = complete auditability`, `reproducibility = external replication/generalization`, `audit trail = legal correctness`, and `retrieved normative document = correct legal application`.

### 2. Controlled sub-batches

#### 0B-05A — Data documentation, provenance, reproducibility, and audit trail

Status: **`READY_FOR_DRAFTING`**.

Active prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

The final inherited set contains Bender & Friedman data statements, Gebru et al. datasheets, the supplied FAIR Data Pipeline paper (whose physical filename begins `AIR data pipeline-`), Pineau et al. reproducibility report, and Raji et al. end-to-end internal algorithmic auditing framework.

The governing chain is `DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`, explicitly not `CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

#### 0B-05B — Information, documented explicit knowledge, and limits of codified knowledge

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may open only after 0B-05A is frozen. Candidate inherited sources are Zins, Hildreth & Kimble, and Al-Hawamdeh only if complete primary-PDF access is confirmed before opening.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It will be a separate primary-official-source audit, not an academic-literature batch. WCO, Andean Community, and SUNAT sources must be evaluated by issuing authority, version, currency, documentary hierarchy, stable identifier, and evidentiary role.

### 3. Prior freezes and gap governance

0B-05 cannot reopen frozen 0A/0B artifacts or experimental results. G6 remains eliminated and G7 remains merged into F2. 0B-05A is methodological/governance-oriented and cannot establish customs novelty.

F3 may receive methodological relevance around documentation of units/partitions/curation; F4 may receive boundary relevance separating provenance/reproducibility from substantive correctness; F5 may receive boundary relevance separating lifecycle audit trails from formal output-level auditability. These labels do not prove a gap.

### 4. Gate

`0B-05A READY_FOR_DRAFTING -> drafting AI -> internal review against the five primary PDFs -> correction if needed -> express author approval -> freeze -> define/open 0B-05B`.

Experimental-AI review is only triggered if a literature interpretation affects a frozen experimental fact/claim or restriction under its authority.

### 5. Prohibitions

No manuscript drafting, final novelty/gap claims, new-literature search, use of out-of-batch PDFs, conflation of documentation with validity, conflation of reproducibility with external replication/generalization, conversion of audit trails into legal correctness, Master-Plan/0A modification, or opening of 0B-05B/0B-05C/0B-06/0C before their gates.
