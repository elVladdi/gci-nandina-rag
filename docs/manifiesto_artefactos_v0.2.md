# Manifiesto de artefactos v0.2

- Dataset: data_aduanas_clase87
- Version: v0.2
- Estrategia: T5-safe-159
- Fecha: 2026-08-29
- Estado Gate 5: APROBADO_ENDURECIDO
- Manifest JSON SHA-256: 65d466ae1ceb6786e02910394b89322d55961a532f841575dca617260b5b702b

## Resumen Gate 5

- 4106 series asignadas exactamente una vez.
- 0 DAM compartidas entre particiones.
- 0 id_unico compartidos entre particiones.
- 1056/1056 casos de evaluacion con soporte historico.
- Concentracion maxima DAM evaluacion: 14.109848484848486%.
- Historico: 2950 series, 28 DAM, 66 codigos, top-1 DAM 35.42372881355932%, top-2 aprox. 67.29%, HHI 0.23613513358230395, DAM efectivo aprox. 4.23.
- Desarrollo: 100 series, 6 DAM, 9 codigos, DAM dominante 91%, HHI 0.8302, DAM efectivo aprox. 1.20, cobertura dev->eval 14.29%.
- Duplicados exactos historico-evaluacion: 35 filas afectadas; 34 misma NANDINA, 1 distinta, 0 misma DAM.
- Near-duplicates historico-evaluacion: 55 filas a 0.90, 44 a 0.95, 37 a 0.98.
- Tests reforzados: igualdad exacta de universo id_unico v0.1-v0.2 y formato/jerarquia NANDINA.

## Artefactos

| rol | ruta | bytes | sha256 |
|---|---|---:|---|
| configuration | src/configs/data_aduanas_split_clase87_v0.2.json | 6345 | a107cf3121faa304b0d83c3ad5378742a4547c257bc04ed5c324195cbf877954 |
| generator | src/evaluation/group_split_by_dam.py | 29982 | dd31da90f736024be06997cc3e6cc28371bf462ec026208c1e06565e0c9b8409 |
| automated_tests | tests/test_data_aduanas_split_v02.py | 10284 | c30a99009c8db4d417b9ec75f1377be21eaf54533096b4feedcdabcd5a1f56d0 |
| dataset | data/processed/data_aduanas_historico_clase87_v0.2.csv | 3462862 | 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff |
| dataset | data/processed/data_aduanas_devset_clase87_v0.2.csv | 135082 | 434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00 |
| dataset | data/processed/data_aduanas_evalset_clase87_v0.2.csv | 1363273 | 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941 |
| metadata | data/processed/data_aduanas_splits_clase87_v0.2_metadata.json | 10019 | 1ac08e760bc3885866507a4c1ca515430c417e812dc01c7dece0f513c5e4d9ec |
| documentation | docs/protocolo_data_aduanas_clase87_v0.2.md | 5251 | 5a8c31c32618416c658ee9d2913c6ca854ec9053d45e4cdb850f81e475e47586 |
| documentation | docs/ficha_data_aduanas_clase87_v0.2.md | 4122 | 30b85959b2384fc798d5ed1d309491848be5dd8d02cb56f90409bdcfb7be5113 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json | 4125 | 79097fcc162cca8690f9382b5e529cfbd8d714575ad7fb96fc044eca2343d027 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.md | 932 | 24196e8578b5f042d8f443f09294a811f82428c49497e9beb9e63178129d6420 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/concentration_by_dam_v0.2.csv | 7389 | 1a50e59c0c7963a3583d769931097e4e4600a8e55cc51b58babb330c50ddac31 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/concentration_summary_v0.2.json | 555 | 0e8fce3a290f78f745bf1859b6bb10448e54b9d93bb4fcef93a047fde04be246 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/exact_duplicates_cross_split_details_v0.2.csv | 8765 | 691b094fbd4e6a142b235226abea27ba20897418b5929fa7dedcee48bc295525 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/exact_duplicates_cross_split_summary_v0.2.csv | 414 | b5e6239f0c69de7fdc5989f1fb301ba33621fb9c72d5f33fd07830290d5225d1 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/historical_support_by_code_v0.2.csv | 1885 | f392a0ada7b1e1c8a3d1134232ba0ec01a0afeff4adbe150d7be4f6845afa899 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/historical_support_by_eval_row_v0.2.csv | 299774 | 4fed0fe48a8d36718bb65e1adbb5eecce2ca671fbb5aa846bd22a2dc2762f385 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/historical_support_summary_v0.2.json | 559 | f9f781d7f23c4658d8d6cc164fcef930569eb9f6f63c76378f7b5ac7d67c56b9 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/independence_audit_v0.2.json | 317 | aa863c0d5850c8f77230bff6602e803be11316677889bc6b377e99ad34bd5dc9 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/near_duplicates_hist_eval_details_v0.2.csv | 34995 | 0f1f0283c993dd57ab3e02ba064b8c964fd688777726f7ae80c04c47e9c9b955 |
| audit | outputs/audits/data_aduanas_splits_clase87_v0.2/near_duplicates_hist_eval_summary_v0.2.csv | 461 | 80cd723ae6fe7e5fe2898b446baa582dde4d69b127a7e59fce736c324e576e43 |

## Alcance

Este manifiesto cubre configuracion, generador, datasets, metadata, auditorias, tests y documentacion v0.2. No incluye EXP-04 ni ejecuciones finales de BM25, Text2Trade, candidate pools, RAG, reranking LLM ni explicador LLM.
