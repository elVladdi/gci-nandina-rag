# FIG011A — Candidato editorial de Figura 4 para G7-F02

```text
FIG011A_EXECUTION = COMPLETE
FIGURE_4_CANDIDATE_CREATED = true
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
DETERMINISTIC_RERUN_MATCH = true
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
DOCX_MODIFIED = false
FIGURE_5_EXECUTED = false
121F_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## Frozen inputs

The candidate was generated in a clean temporary worktree at `d0ebffcca3abb54ce04cb90e1181c2f420c5f3ff`, using only Git objects from frozen `main = db0d0ad0d8435921a7838db6720eaea86a263763`. The renderer fails closed on a mismatch to any of the five expected source blobs. No source file in G6, Group 5, or the thesis was modified.

| Source | Git blob | SHA-256 | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group6/render_g6_fig_01_he2.py` | `678d5fd49b3bd090c7d7729702741e6dcfe293fa` | `646fe4eacbedcbb7661ceb231c7678aa06957eb634b71f978756ffb9a928cbeb` | 9256 |
| `figures/group6/g6_fig_01_he2.svg` | `f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3` | `534aade80e669db62d86764d2b1695d26654c1d042144ef141f462983d422ca8` | 23792 |
| `figures/group6/g6_fig_01_he2.png` | `1860898f13cdefb311489dd1ec3d8fb28bf24538` | `3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f` | 192986 |
| `outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv` | `cb68583ee2260e4455796bac99ad90995ca7ef92` | `d2bfba2a52907818bfc8e9f4d783d24d7ddc80da2f464321b4ce37319ab8e755` | 2919 |
| `outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv` | `359e4e19b5ef1d44983c03039162209293b2a44c` | `50a18ec31a819ce9c96f3de9c66f3e91920b6f80ee84d7e69393baa3b33187a6` | 340 |

## Candidate artifacts

| Candidate | SHA-256 | Git blob | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group7/render_g7_thesis_fig_04_he2.py` | `2af80603d59ef6690fa3e63f7e6e5daea21cb1326e186a56470f35f562a84442` | `b22d25d41fa9014180fd63a36715942414e779a0` | 5189 |
| `figures/group7/g7_thesis_fig_04_he2.svg` | `6946594f2543f4dced0e2f19ee73b8adc5e7fa3a2fdb92f7c68cb55f0e1e93b9` | `e84fa3ee6aaedb2d3d24b59ce7255214621aae3f` | 25201 |
| `figures/group7/g7_thesis_fig_04_he2.png` | `5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e` | `eb77a4f2289a8701d22ba399d9432defd2092e2a` | 300119 |

The remaining artifact is `outputs/figures/group7/g7_thesis_fig_04_he2_manifest_v0.1.json`, which binds these sources, outputs, label substitutions, reflow and invariants. Manifest JSON parsing and all candidate SHA-256/size/blob bindings passed.

SHA-256 and size in the tables bind the committed Git blob bytes, not platform-dependent working-tree line endings. For the Python script, the LF blob is 5,189 bytes with SHA-256 `2af80603d59ef6690fa3e63f7e6e5daea21cb1326e186a56470f35f562a84442`; the canonical Windows CRLF checkout is 5,308 bytes with SHA-256 `2289a9320264403ed7f5450c0eee5213d0f68ddd2326c7cc59e544f8919e535d`. For the SVG, the LF blob is 25,201 bytes with SHA-256 `6946594f2543f4dced0e2f19ee73b8adc5e7fa3a2fdb92f7c68cb55f0e1e93b9`; the rendered/Windows CRLF file is 25,395 bytes with SHA-256 `053b12ea192175071c4274aa1ee4154ec3769f6c02f057e9fdd93bc159ef0e99`. The PNG has identical Git and checkout bytes.

## Validation

- Two final consecutive script invocations returned identical raw CRLF SVG SHA-256 `053b12ea192175071c4274aa1ee4154ec3769f6c02f057e9fdd93bc159ef0e99` and PNG SHA-256 `5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e`. No candidate output was present before the first render in the clean worktree.
- XML comparison after excluding only `<text>`/`<tspan>` found the same sequence and attributes for all 115 non-text elements, including canvas, axes, ticks, zero-lines, intervals and marks. Hence values, scales, positions, marker semantics and scientific panel structure remain those of G6-FIG-01.
- SVG canvas is 1000 x 1250; PNG is 2500 x 3125 at nominal 300 dpi. Panels A/B/C, five metrics, three comparators, 15 paired contrasts with frozen 99% CI, one deep-coverage contrast with frozen 95% CI, no arm-level CI and no p-values remain unchanged. EVAL=1,056, DAM=67, NANDINA=42.
- All 78 SVG text elements were checked. None contains the prohibited English/internal labels or governance IDs; all text bounds lie within the canvas; no material text-to-text overlap was detected. Minimum SVG font size is 13.5 units, or 8.1 pt at 120 units/inch. The rendered PNG was inspected for clipping and overlap.
- The G6 script, SVG and PNG were re-read from their frozen Git objects and matched the expected blobs and SHA-256 after generation. The candidate creates no Figure 5 artifact, edits no DOCX and does not execute 121F.

This is a thesis-specific Figure 4 candidate only. It has not been inserted into the thesis and remains pending independent visual/scientific audit.
