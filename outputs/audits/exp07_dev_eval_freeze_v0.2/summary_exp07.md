# EXP-07 dev/eval freeze

The v0.2 dev split is frozen at 100 cases and SHA-256 `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`; the official eval split is frozen at 1056 cases and SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. DAM overlap is zero among historical, dev and eval. Dev concentration remains a limitation: 6 DAM, largest DAM 91/100, HHI about 0.8302.

Evaluation labels were used to evaluate, not to tune the final system after freeze; labels were not exposed to generation. The v0.1-to-v0.2 split change is an experimental-design correction for dependence/leakage, not eval tuning. D1a did not use eval for training/selection; E 70/30 is diagnostic; G is a 20-case diagnostic; J preserves its specification limitation; K preserves evaluator-modality deviation.
