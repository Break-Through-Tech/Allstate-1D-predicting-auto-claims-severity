# Modeling contract

Bundle ID: `gate4-october-milestone-reproducible-project`

This is the Gate 1 contract, placed in the October package. The first copy is [`../gate1-issue-reproducible-project/modeling-contract.md`](../gate1-issue-reproducible-project/modeling-contract.md). The calculation notebook is [`../../../notebooks/OctoberMilestones/OctoberGate1.ipynb`](../../../notebooks/OctoberMilestones/OctoberGate1.ipynb).

## Prediction task

- Estimate one claim's final paid amount from the anonymous fields on that claim.
- One row is one anonymized auto-insurance claim. `loss` is that claim's total paid amount, and it is the regression target. The project overview says the supplied file already excludes closed claims that had no payment. Every remaining row stays eligible, including claims with a very large `loss`.
- `id` is used to check that each claim appears once, to record which partition the claim is in, and to trace a prediction back to a claim. It is excluded from model inputs. `loss` is excluded from model inputs.
- The field names do not say whether an input is known when a claim is first filed. Until the Challenge Advisor confirms that timing, results from this contract are a retrospective check on the supplied file. This contract does not call the model an up-front estimator. The timing question is unanswered, and this folder does not name an owner for it.

## Eligible rows and source

The eligible rows are all 188,318 rows of `data/allstate_claims_data.csv`.

| Item | Value |
| --- | --- |
| Bytes | 70,025,339 |
| Columns | 132 |
| SHA-256 | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03` |

That hash is copied in [`manifests/source_identity.csv`](manifests/source_identity.csv). A different file would need its own review before it could replace this one.

## Field roles and feature list

| Role | Columns | Used as a model input |
| --- | --- | --- |
| Identifier | `id` | No |
| Nominal category | `cat1` through `cat116` (116 fields) | Yes |
| Continuous number | `cont1` through `cont14` (14 fields) | Yes |
| Target | `loss` | No |

`cat*` values are category labels. `cont*` values are continuous numbers; September found them on a 0-to-1 scale. This contract does not assign a business meaning to any anonymous field. Examples in the project overview are examples of field types, and they are not a dictionary for these columns.

The frozen list is [`field_roles.csv`](field_roles.csv): 130 inputs, in the source column order, with `id` and `loss` marked as excluded.

## Metric

- The comparison metric is mean absolute error (MAE) in the original `loss` units. Absolute error is the positive distance between a predicted paid amount and the actual paid amount. MAE is the average of those distances on a named held-out partition. A smaller MAE means the predictions are closer to the paid amounts.
- Every reported score in this bundle names its partition, its claim count, and its evaluation code. The scores here use the validation partition, 28,248 claims, and `sklearn.metrics.mean_absolute_error`. A training-set score, or a score on a transformed scale such as `log1p(loss)`, is a diagnostic. The project comparison is the original-unit validation MAE.
- The required comparators are a training-mean constant and a training-median constant. The median is included because, among constant predictions, the median minimizes absolute error. Both are scored in [`baselines/baseline_validation_mae.csv`](baselines/baseline_validation_mae.csv).
- The seed stays `random_state=1` when a validation MAE looks unfavorable. Tuning stops when validation MAE fails to improve for 3 consecutive tuning runs.

## What a result can support

- A result under this contract is evidence about the supplied file and this internal split. It can show whether a recorded approach has a lower validation MAE than the two constants on the same 28,248 claims.
- September exploratory analysis already looked at `loss` relationships across all 188,318 rows, before this split existed. The validation and test claims were inside that full-file look. Keeping the test partition out of October fitting protects it from later tuning. It does not make the test a new sample from a later time period.
- This contract does not treat a validation MAE as proof of future-period stability, a causal effect, production readiness, or a suitable reserve for one claim. Valid high-loss claims stay in the data. A suspected bad value goes through the anomaly register. Rows stay in the file while that review is open.

## September handoff

The September package and the two recommendation decisions are in [`handoff/september_handoff.md`](handoff/september_handoff.md). The September teammate sign-off is still blank. The recorded forest and XGBoost scores are in [`experiments/validation_mae.csv`](experiments/validation_mae.csv). Those scores do not close Gate 4 while that sign-off and [`review/independent_review.md`](review/independent_review.md) are unsigned.

The evaluation plan is [`evaluation-plan.md`](evaluation-plan.md).
