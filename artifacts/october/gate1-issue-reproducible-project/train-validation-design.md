# Train and validation design

Bundle ID: `gate1-issue-reproducible-project`

Source notebook: [`../../../../notebooks/OctoberMilestones/OctoberGate1.ipynb`](../../../../notebooks/OctoberMilestones/OctoberGate1.ipynb)

## Why this design

October needs one fixed set of claims for fitting, a second set for comparing models, and a third set left untouched until November's final evaluation. The notebook uses a single random split so those three jobs are separated before any feature-based model is fit.

The design is 70% train, 15% validation, and 15% test. The method is `sklearn.model_selection.train_test_split` with `random_state=1`.

1. Hold out 15% of the file as test: `train_test_split(df, test_size=0.15, random_state=1)`.
2. Hold out 15% of the original file from what remains: `train_test_split(train_temp, test_size=(0.15/0.85), random_state=1)`. That second piece is validation. The rest is train.

The seed stays `random_state=1` when a validation MAE looks unfavorable. A new manifest is written only when the team records a separate reason to change the split, and that record has to be saved with the revised file. Trying seeds until the validation MAE looks favorable is outside this design.

## Who is eligible

Every row in `data/allstate_claims_data.csv` is eligible. There is no row filter. High-loss claims stay in whichever partition the split assigned them. The supplied file, per the project overview, already excludes closed claims without payment.

## Partition manifest

[`gate1_partition_manifest.csv`](gate1_partition_manifest.csv) is the frozen manifest. It has one row per claim, keyed by `id`, with partition `train`, `validation`, or `test`. It has 188,318 rows, in the order the notebook stacks the three partitions. The first id is `238427` (train). The last id is `576271` (test).

| Partition | Claims | Share of 188,318 |
| --- | ---: | ---: |
| Train | 131,822 | 70% |
| Validation | 28,248 | 15% |
| Test | 28,248 | 15% |

[`partition_row_counts.csv`](partition_row_counts.csv) stores those counts. [`partition_checks.csv`](partition_checks.csv) stores the membership checks. Each check passed: the manifest has 188,318 distinct `id` values, it has 188,318 rows, and the three partitions share no `id`. Every eligible claim is in exactly one partition.

The test row count and the test ids are part of the manifest. Test `loss` values are not in this folder.

## Target summaries and high-loss support

These summaries cover training and validation only. They use the percentiles the notebook prints. Full precision is in [`target_summaries.csv`](target_summaries.csv).

| Partition | Count | Mean | Std | Min | Median | 90th | 99th | Max |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Train | 131,822 | 3033.688044 | 2915.370042 | 0.67 | 2113.755 | 6382.559 | 14017.4098 | 121012.25 |
| Validation | 28,248 | 3055.652346 | 2907.103183 | 54.34 | 2121.985 | 6467.678 | 14059.7252 | 51383.04 |

High-loss claims are the right tail of `loss`. On the training partition, 1% of claims have `loss` above about 14,017, and the largest training payment is 121,012.25, which is the maximum of the whole file. On the validation partition, 1% of claims have `loss` above about 14,060, and the largest validation payment is 51,383.04. Both tails stay in the analysis. The minimum training `loss` is 0.67, so the smallest payments stay as well.

## Categorical level coverage

Before any model comparison, the notebook checked which category labels appear in validation and are missing from training. Eight fields have at least one such label, 21 labels in total:

| Field | Unseen validation levels |
| --- | ---: |
| `cat92` | 1 |
| `cat104` | 1 |
| `cat105` | 2 |
| `cat109` | 2 |
| `cat110` | 1 |
| `cat113` | 1 |
| `cat114` | 1 |
| `cat116` | 12 |

The labels themselves are in [`unseen_validation_levels.csv`](unseen_validation_levels.csv). The preprocessing plan treats a level the training vocabulary has not seen as an ignored one-hot column. That rule is set without using validation `loss`.
