# Modeling contract

Bundle ID: `gate1-issue-reproducible-project`

This contract is the plain-language decision for the first October modeling run. The calculation notebook is [`../../../notebooks/OctoberMilestones/OctoberGate1.ipynb`](../../../notebooks/OctoberMilestones/OctoberGate1.ipynb).

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

That hash matches the September source record in [`../../september/gate4-september-milestone-reproducible-project/source/source_identity.csv`](../../september/gate4-september-milestone-reproducible-project/source/source_identity.csv). A different file would need its own review before it could replace this one.

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
- The required comparators are a training-mean constant and a training-median constant. The median is included because, among constant predictions, the median minimizes absolute error. Both are scored in [`evalutation-design/baseline_validation_mae.csv`](evalutation-design/baseline_validation_mae.csv). Gate 2 still has to rerun them independently before feature-based models are compared.
- The seed stays `random_state=1` when a validation MAE looks unfavorable. Tuning stops when validation MAE fails to improve for 3 consecutive tuning runs.

## What a result can support

- A result under this contract is evidence about the supplied file and this internal split. It can show whether a recorded approach has a lower validation MAE than the two constants on the same 28,248 claims.
- September exploratory analysis already looked at `loss` relationships across all 188,318 rows, before this split existed. The validation and test claims were inside that full-file look. Keeping the test partition out of October fitting protects it from later tuning. It does not make the test a new sample from a later time period.
- This contract does not treat a validation MAE as proof of future-period stability, a causal effect, production readiness, or a suitable reserve for one claim. Valid high-loss claims stay in the data. A suspected bad value goes through the anomaly register. Rows stay in the file while that review is open.

## September handoff

- The September package this contract uses is Bundle ID `gate4-issue-reproducible-project`, folder [`../../september/gate4-september-milestone-reproducible-project/`](../../september/gate4-september-milestone-reproducible-project/).
- Its anomaly register has one row, `GATE1-000`: the September reload found 0 blocking source, schema, or integrity anomalies, removed 0 rows, and left all 188,318 claims in the file. No unresolved anomaly is carried forward. No Challenge Advisor question is written in that register. The field-timing question above is new to this October contract and is still open.
- September Gate 4's teammate sign-off is still blank in [`../../september/gate4-september-milestone-reproducible-project/review/independent_review.md`](../../september/gate4-september-milestone-reproducible-project/review/independent_review.md). That open sign-off is the handoff blocker. This contract records the plan and the split. Fitting the random forest and XGBoost models waits until that sign-off and a Gate 1 teammate review are recorded. The Gate 1 sign-off is not stored in this folder.

### Recommendation register

September's register has two items, in [`../../september/gate4-september-milestone-reproducible-project/handoff/october_recommendation_register.md`](../../september/gate4-september-milestone-reproducible-project/handoff/october_recommendation_register.md).

| Item | October decision | Would it reopen a September gate? |
| --- | --- | --- |
| REC-002, research model types for a paid-amount estimate | Adopted as the two planned approaches in [`preprocing-experiment-plan.md`](preprocing-experiment-plan.md): random forest and XGBoost. The notebook also names cross-validation as later training-only work. No fold count is frozen here. | No. September asked for a short list and told October not to name a winner. This contract still names no winner. |
| REC-001, decide whether outlier points need different handling | Deferred. It is not an October experiment in this plan. Plots may be revisited later. Points stay in the file. | Deleting rows to improve MAE would conflict with `GATE1-000`, which kept every row. That change would need a new anomaly review before it could be used. Looking at the plots without deleting rows does not reopen a September gate. |

The notebook also defers dropping highly correlated features. That deferral matches the October rule that a field is not removed only because it is correlated with another field. Adopting that drop later would be a new, explicit feature experiment. It would not, by itself, reopen a September gate.

September's full-file charts are the prior exposure behind this plan: the team has seen how `loss` is shaped and how anonymous fields line up with it on the whole file. The split, the one-hot encoding rule, and the choice of random forest and XGBoost are the hypotheses carried out of that work. The evaluation plan in [`evalutation-design/evaluation-design.md`](evalutation-design/evaluation-design.md) states that exposure next to the scores.
