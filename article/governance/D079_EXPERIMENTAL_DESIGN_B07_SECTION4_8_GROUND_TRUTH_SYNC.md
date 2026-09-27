# D-079 — Sincronización de ground truth para B07 / Section 4.8 / Ground-truth synchronization for B07 Section 4.8

## Español

```text
DECISION_ID = D-079
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-078
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
PURPOSE = REPRODUCIBILITY_RESOURCES
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
SECTION_4_8 = GROUND_TRUTH_SYNCHRONIZED / DRAFTING_NOT_YET_AUTHORIZED_BY_THIS_DECISION
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Objeto

Section 4.8 debe describir los recursos de reproducibilidad realmente disponibles o inequívocamente documentados para la instanciación evaluada, sin convertir la prosa del artículo en un inventario de rutas/hashes y sin afirmar un grado de reproducibilidad que el paquete público todavía no alcanza.

La fuente pública primaria para este bloque es `elVladdi/gci-nandina-rag-reproducibility`, rama `main`, auditada en HEAD `254831cd955103faa2517065a7eed7fb340bbccc` y tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`.

## 2. Estado público materializado verificado

El snapshot público contiene actualmente:

- `README.md` con el alcance conceptual, modos `reference`/`custom`/`synthetic`, configurabilidad de nomenclatura, nivel objetivo, datos y corpus normativo, y ejemplos de interfaz;
- documentación de contratos y protocolos: `DATA_CONTRACT.md`, `DATA_PROVENANCE.md`, `EXPERIMENT_PROTOCOL.md`, `REPRODUCIBILITY.md`, `TAXONOMY_AND_NORMATIVE_CORPUS.md`, `USING_YOUR_OWN_DATA.md`, `EXPECTED_RESULTS.md`;
- un ejemplo de configuración para datos propios en `configs/examples/custom_dataset.example.yaml`;
- directorios reservados para presets, datos, experimentos, framework, resultados, scripts y tests, cada uno documentado mediante README cuando corresponde.

El snapshot **no contiene todavía** una release de referencia ejecutable completa. En particular, la auditoría del tree no muestra:

- `requirements.txt` o lockfile de dependencias;
- runner canónico `scripts/reproduce_all.py`;
- runners materializados `scripts/validate_dataset.py` o `scripts/run_experiment.py`;
- preset congelado `configs/presets/reference_class87_v0.2.yaml`;
- datasets administrativos de referencia redistribuidos;
- resultados canónicos materializados en `results/`;
- tests ejecutables distintos de la documentación del directorio.

Por tanto, los comandos mostrados en README/REPRODUCIBILITY deben interpretarse como **interfaces objetivo/planificadas**, no como evidencia de que la reproducción computacional integral ya pueda ejecutarse desde un fresh clone.

## 3. Qué sí puede afirmarse

Section 4.8 puede afirmar, con redacción acotada, que el repositorio público:

1. documenta la separación entre reproducción de referencia y replicación externa;
2. define contratos para datos, jerarquía/nomenclatura, corpus normativo, independencia de particiones, procedencia y manifest de ejecución;
3. documenta qué metadatos deben registrarse para una ejecución reproducible: seeds, hashes de entradas/configuraciones, versiones, commit, parámetros, modelo/prompt cuando aplique, comando, timestamp y hashes de salida;
4. proporciona una configuración de ejemplo para reinstanciar el protocolo con datos propios compatibles;
5. distingue recursos redistribuibles de entradas restringidas/no publicables y exige hashes, esquema y rutas de reconstrucción/colocación cuando la redistribución no sea posible;
6. mantiene separado el repositorio limpio de reproducibilidad del historial exploratorio y de desarrollo experimental.

Estas afirmaciones describen **documentación, contratos e interfaces disponibles**, no una certificación de reproducción computacional ya completada.

## 4. Qué no puede afirmarse en el snapshot actual

Queda prohibido afirmar que:

- el repositorio público permite actualmente una reproducción integral con un único comando desde un fresh clone;
- existe ya un preset de referencia congelado y ejecutable para Clase 87;
- los datos administrativos de referencia están redistribuidos públicamente;
- todos los resultados del artículo pueden regenerarse hoy solo con los artefactos públicos del repositorio de reproducibilidad;
- una validación clean-environment del paquete final ya fue completada;
- el paquete público constituye una release estable o final;
- la disponibilidad documental implica generalización empírica, corrección jurídica o replicabilidad numérica sobre datos externos.

## 5. Distinción reproducción vs replicación

La redacción debe conservar la terminología operativa del repositorio:

- **reference reproduction:** repetir un preset congelado con las mismas entradas/configuración/outputs esperados, una vez que esos artefactos se congelen y publiquen;
- **external replication:** ejecutar el mismo protocolo sobre datos propios compatibles; no exige reproducir los mismos valores numéricos del estudio de referencia.

No debe afirmarse que una reinstanciación con otros datos, clases, jurisdicciones o corpus demuestra generalización del desempeño observado.

## 6. Datos y redistribución

`DATA_PROVENANCE.md` establece que los CSV administrativos no deben copiarse al repositorio público hasta validar explícitamente su estatus de publicación. Para entradas restringidas, el contrato exige no publicarlas y, cuando corresponda, proporcionar hash esperado, esquema y una instrucción de reconstrucción/colocación. Section 4.8 debe reflejar esta frontera y evitar prometer disponibilidad pública de datos no verificada.

## 7. Pre-submission recheck obligatorio

Dado que el repositorio de reproducibilidad está explícitamente en consolidación progresiva, Section 4.8 debe incluir en su contrato editorial una obligación de **re-verificación antes del freeze final/submission**. Si en ese momento existen scripts, presets, manifests, datos redistribuibles o una clean-environment validation que no existían en este snapshot, la sección deberá actualizarse mediante un nuevo gate; no deben anticiparse ahora.

## 8. Gate

```text
B07_GROUND_TRUTH = SYNCHRONIZED
B07_DRAFTING = NOT_YET_AUTHORIZED_BY_D079
REPRO_PACKAGE_STATUS = DOCUMENTED_SCAFFOLD / NOT_FULL_REFERENCE_RELEASE
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

```text
DECISION_ID = D-079
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-078
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
REPRO_PACKAGE_STATUS = DOCUMENTED_SCAFFOLD / NOT_FULL_REFERENCE_RELEASE
B07_DRAFTING = NOT_YET_AUTHORIZED_BY_D079
RESULTS = NOT_AUTHORIZED
```

The public reproducibility repository currently provides protocol documentation, data/taxonomy/provenance contracts, an example custom-data configuration, and a documented directory structure for future reference artifacts. The audited tree does not yet contain the canonical reproduction runner, frozen Class-87 reference preset, dependency lock, redistributed reference administrative data, canonical result artifacts, or a recorded clean-environment reference reproduction.

Accordingly, Section 4.8 may describe the public contracts, interfaces, provenance requirements, distinction between reference reproduction and external replication, and redistribution boundaries. It must not state that the current public snapshot already provides a complete one-command computational reproduction or a stable final reference release.

Because the repository is still being progressively consolidated, a mandatory pre-submission recheck is required. Later materialization of scripts, presets, manifests, redistributable data, expected outputs, or clean-environment validation must be incorporated through a new governed update rather than anticipated in the present Methods prose.