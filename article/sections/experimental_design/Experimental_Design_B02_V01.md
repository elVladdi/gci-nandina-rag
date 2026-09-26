# Experimental Design B02 V01 — Section 4.3

```text
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
VERSION = V01
STATUS = DRAFT / PENDING_GESTORA_AUDIT
```

## Part I — English

### 4.3. Documentary corpus and evidence resource

The documentary resource used in the primary experimental instantiation was a hierarchical NANDINA corpus derived from Decision 885 of the Commission of the Andean Community, which approved the nomenclature that entered into force on 1 January 2022. The official nomenclature was processed into source-anchored records covering the hierarchy represented in the frozen source rather than only Chapter 87. Chapter 87 bounded the empirical candidate set because the codes queried in this resource came from the fixed Top-3 produced upstream for that evaluation setting.

Each valid eight-digit NANDINA entry was represented together with the available section and chapter context, four-digit heading, six-digit HS subheading, eight-digit NANDINA description, physical unit, and source-page or source-line provenance. Parent levels were retained as contextual information; their text was not treated as an exact eight-digit match when a candidate-level record was absent. This representation provided identifiable documentary context without changing candidate generation or ranking.

For each candidate in the fixed Top-3, documentary evidence was associated by exact lookup of that candidate's NANDINA-8 code in the hierarchical corpus. This instantiation did not perform query-based normative retrieval over the commercial description, fuse historical and documentary scores, rerank candidates, or replace a candidate when an exact record was unavailable. Missing exact evidence therefore remained an explicit absence rather than triggering fallback to another code. The matched documentary record and its hierarchical context were passed downstream for controlled explanation while Top-3 membership and order remained unchanged.

This configuration has a temporal and version boundary. Decision 906, published in Official Gazette of the Cartagena Agreement No. 5062 on 25 October 2022 and effective from 1 January 2023, modified the NANDINA approved by Decision 885. The primary experiment nevertheless retained the frozen Decision-885-derived corpus for the 2026 administrative cases. Accordingly, the documentary resource used in the primary path was not retroactively updated to Decision 906; this limitation concerns the version of the documentary evidence and does not by itself imply that every Chapter-87 candidate or associated record was incorrect.

## Part II — Spanish semantic-control mirror

### 4.3. Corpus documental y recurso de evidencia

El recurso documental utilizado en la instanciación experimental primaria fue un corpus NANDINA jerárquico derivado de la Decisión 885 de la Comisión de la Comunidad Andina, que aprobó la nomenclatura que entró en vigencia el 1 de enero de 2022. La nomenclatura oficial se procesó en registros vinculados con su texto fuente y con cobertura de la jerarquía representada en la fuente congelada, no únicamente del Capítulo 87. El Capítulo 87 delimitó el conjunto empírico de candidatos porque los códigos consultados en este recurso provenían del Top-3 fijo generado previamente para ese escenario de evaluación.

Cada registro NANDINA válido de ocho dígitos se representó junto con el contexto disponible de sección y capítulo, la partida de cuatro dígitos, la subpartida HS de seis dígitos, la descripción NANDINA de ocho dígitos, la unidad física y la procedencia por página o línea de la fuente. Los niveles parentales se conservaron como contexto; su texto no se trató como una coincidencia exacta de ocho dígitos cuando faltaba el registro correspondiente al candidato. Esta representación aportó contexto documental identificable sin modificar la generación ni el ranking de candidatos.

Para cada candidato del Top-3 fijo, la evidencia documental se asoció mediante un lookup exacto del código NANDINA-8 del candidato en el corpus jerárquico. Esta instanciación no realizó recuperación normativa basada en la consulta sobre la descripción comercial, no fusionó scores históricos y documentales, no reordenó candidatos ni sustituyó un candidato cuando faltaba un registro exacto. Por tanto, la ausencia de evidencia exacta permaneció explícita en lugar de activar un fallback hacia otro código. El registro documental coincidente y su contexto jerárquico se entregaron downstream para la explicación controlada, mientras la composición y el orden del Top-3 permanecieron inalterados.

Esta configuración presenta una frontera temporal y de versión. La Decisión 906, publicada en la Gaceta Oficial del Acuerdo de Cartagena N.º 5062 el 25 de octubre de 2022 y vigente desde el 1 de enero de 2023, modificó la NANDINA aprobada mediante la Decisión 885. Sin embargo, el experimento primario conservó el corpus congelado derivado de la Decisión 885 para los casos administrativos de 2026. En consecuencia, el recurso documental utilizado en la ruta primaria no fue actualizado retroactivamente con la Decisión 906; esta limitación corresponde a la versión de la evidencia documental y no implica por sí sola que todos los candidatos del Capítulo 87 o sus registros asociados fueran incorrectos.
