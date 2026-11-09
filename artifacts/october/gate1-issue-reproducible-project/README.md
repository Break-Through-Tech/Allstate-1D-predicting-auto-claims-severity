# Gate 1 — Modeling plan and splits

Bundle ID: `gate1-issue-reproducible-project`

This folder is the Gate 1 evidence for October model development. A reviewer who was not in the working session can read the decision, the frozen split, and the limits of that evidence without opening the notebook.

Related notebook: [`../../../notebooks/OctoberMilestones/OctoberGate1.ipynb`](../../../notebooks/OctoberMilestones/OctoberGate1.ipynb)

September handoff: [`../../september/gate4-september-milestone-reproducible-project/`](../../september/gate4-september-milestone-reproducible-project/) (Bundle ID `gate4-issue-reproducible-project`)

## What this gate decides

October estimates one claim's final paid amount, `loss`, from anonymous claim fields. The comparison score is mean absolute error (MAE): the average size of the miss, in the original paid-amount units.

The first modeling run uses every row in `data/allstate_claims_data.csv`. `id` identifies the claim and is left out of the model. `loss` is the target and is left out of the inputs. The inputs are 116 nominal fields, `cat1` through `cat116`, and 14 continuous fields, `cont1` through `cont14`.

Claims are split once, with `random_state=1`, into 131,822 training rows (70%), 28,248 validation rows (15%), and 28,248 test rows (15%). Validation is the October comparison partition. The test partition is reserved for November. This folder records the test row count and membership, and it leaves test `loss` values and test scores out.

The seed stays `random_state=1` when a validation MAE looks unfavorable. Tuning stops when validation MAE fails to improve for 3 consecutive tuning runs.

## Identity of this evidence

| Item | Value |
| --- | --- |
| Source | `data/allstate_claims_data.csv` |
| Bytes | 70,025,339 |
| Rows × columns | 188,318 × 132 |
| SHA-256 | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03` |
| Partition manifest | [`splits/gate1_partition_manifest.csv`](splits/gate1_partition_manifest.csv) |
| Split configuration | `train_test_split`, `random_state=1`, test fraction 0.15, then validation fraction 0.15/0.85 |
| Score code | `sklearn.metrics.mean_absolute_error` on the validation partition (28,248 claims) |
| Environment | Python 3.12.4, pandas 3.0.6, NumPy 2.5.3, scikit-learn 1.9.1 |
| Workflow run | None recorded. These tables come from the notebook procedure above, reproduced locally. |

The source hash matches [`../../september/gate4-september-milestone-reproducible-project/source/source_identity.csv`](../../september/gate4-september-milestone-reproducible-project/source/source_identity.csv).

## How to read the scores

The training-mean validation MAE is 1978.3970470120255. The training-median validation MAE is 1827.3136338855847. Both constants were fit on the training rows only. Details are in [`evalutation-design/baseline_validation_mae.csv`](evalutation-design/baseline_validation_mae.csv).

September's full-file median error, 1809.0487864675708, describes the whole file before the split. It is a different number from the validation scores above.

These validation scores describe this supplied file. September had already summarized `loss` on all 188,318 rows, so the later internal partitions are protected from October fitting and are still part of a file the team has already explored. They are a retrospective check. They become evidence about prediction at first notice of a claim only after the Challenge Advisor confirms which fields exist at that moment. This folder does not call the model an up-front estimator.

## Still open

Gate 1 is not passed. An independent teammate still has to check the manifest, the leakage boundaries, the metric code, and this plan. That sign-off is not stored in this folder.

September Gate 4's own sign-off is also unsigned: [`../../september/gate4-september-milestone-reproducible-project/review/independent_review.md`](../../september/gate4-september-milestone-reproducible-project/review/independent_review.md). This plan uses the committed September evidence. Model fitting stays pending until that handoff sign-off and this Gate 1 sign-off are both recorded.

Also still open, with no owner named in this folder:

- The week-by-week Milestone #2 board plan is not stored here.
- The Challenge Advisor has not confirmed which anonymous fields are available when a claim is first filed.
- Cross-validation is named as later training-only work and has no fold count yet.
- Run receipts and resource cost for the random forest and XGBoost fits belong to a later gate. Those models are not fit in this folder.

## Files

| Path | Role |
| --- | --- |
| [`modeling-contract.md`](modeling-contract.md) | Task, eligible rows, field roles, MAE rule, September recommendations, and the limits on what a score can support |
| [`field_roles.csv`](field_roles.csv) | Role and model-input flag for all 132 columns |
| [`evalutation-design/evaluation-design.md`](evalutation-design/evaluation-design.md) | Why validation exists, the stopping rule, the November holdout, and the constant-predictor scores |
| [`evalutation-design/baseline_validation_mae.csv`](evalutation-design/baseline_validation_mae.csv) | Training-mean and training-median MAE, with partition, claim count, and evaluation code |
| [`splits/train-validation-design.md`](splits/train-validation-design.md) | Split method, seed, eligibility, high-loss support, and category coverage |
| [`splits/gate1_partition_manifest.csv`](splits/gate1_partition_manifest.csv) | Claim `id` and partition for all 188,318 rows |
| [`splits/partition_row_counts.csv`](splits/partition_row_counts.csv) | Train, validation, and test row counts |
| [`splits/partition_checks.csv`](splits/partition_checks.csv) | One-membership and overlap checks |
| [`splits/target_summaries.csv`](splits/target_summaries.csv) | Training and validation `loss` summaries, including the high-loss tail |
| [`splits/unseen_validation_levels.csv`](splits/unseen_validation_levels.csv) | Categorical levels present in validation and absent from training |
| [`preprocing-experiment-plan.md`](preprocing-experiment-plan.md) | Preprocessing rules, the two model approaches, and the planned comparison record |
