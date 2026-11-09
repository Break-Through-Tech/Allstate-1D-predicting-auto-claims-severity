# November handoff

This is the package for November's Evaluation and Presentation milestone. The October comparison is in [`october_report.md`](october_report.md). Teammate sign-off is still open in [`../review/independent_review.md`](../review/independent_review.md). November uses the versions recorded here.

## Pipeline and preprocessing

Use [`../preprocessing/training_preprocessor.py`](../preprocessing/training_preprocessor.py). It is the pipeline from `notebooks/OctoberMilestones/October_Gate_3.ipynb`.

| Piece | Version used |
| --- | --- |
| Code | `build_preprocessor` in that file |
| Dependencies | Python 3.12.4, pandas 3.0.6, NumPy 2.5.3, scikit-learn 1.9.1, XGBoost 3.4.1 |
| Fit rows | The 131,822 training claims only |
| Numbers | Training median fill. The `cont*` fields stay on their recorded 0-to-1 scale. |
| Categories | Training mode fill, then one-hot encoding with `handle_unknown='ignore'` and `sparse_output=False` |
| Left out | `id` and `loss` |

The field list is [`../field_roles.csv`](../field_roles.csv): `cat1` through `cat116` and `cont1` through `cont14`. No field was added or removed after seeing validation error.

## No model was selected

October does not name a provisional model. Both the random forest and XGBoost have a lower validation miss than the training-mean and training-median constants, and the two model scores are close. XGBoost's validation miss is $1,171.72. The forest's is $1,291.59. The gap is about $119.87, under 10% of the forest score. [`../experiments/reliability.md`](../experiments/reliability.md) records that this is too weak to prefer one model.

November reports both models beside both constants. A test score does not create a winner after the fact.

## Evaluation code and split

The score is mean absolute error in original `loss` dollars, from `sklearn.metrics.mean_absolute_error`, on a named partition. The steps to rerun the validation scores are in [`../review/reproduction.md`](../review/reproduction.md).

The frozen split is [`../manifests/gate1_partition_manifest.csv`](../manifests/gate1_partition_manifest.csv), SHA-256 `0e97b61a8ad550387f2c7bcbe2b4130064e790337e88d1a5251399ce91830418`. It has 131,822 training claims, 28,248 validation claims, and 28,248 test claims. The seed is `random_state=1`.

## Anomalies

[`../registers/anomaly_register.csv`](../registers/anomaly_register.csv) has one row, `GATE1-000`: 0 blocking source, schema, or integrity anomalies, and 0 rows removed. No new anomaly was opened in October. High-loss claims stayed in the split.

## Feature experiments

| Experiment | Status |
| --- | --- |
| Keep all 130 inputs | Done. This is the comparison that was scored. |
| Drop a field because its September correlation with `loss` was weak | Not done. `cont1` is about -0.01 on the full September file and stays in. |
| Drop a field only because it is correlated with another field | Not done. These full-file pairs stay in: `cont11` and `cont12` (about 0.994), `cont1` and `cont9` (about 0.930), and `cont6` and `cont10` (about 0.883). Those September figures include claims that are now validation and test. |
| Refit XGBoost after removing one field from the `cont11` and `cont12` pair | Deferred. Choose the removed field from the training claims only. Use this same preprocessing, the same 5 training folds, `random_state=1`, and one validation score on the same 28,248 claims. Keep the field unless that validation score is lower than $1,171.72. This was not run. October had already used its one iteration on the training-versus-fold check, and that check did not support another fit. |
| Target encoding | Out of scope for the recorded comparison. |
| Separate handling for outlier points, without deleting rows | Deferred from September recommendation REC-001. |

## Questions for the Challenge Advisor

- Which of the anonymous fields are known when a claim is first filed? Until that is answered, the scores are a retrospective check on this file. They are not evidence that a model can estimate the payment at first notice.
- No owner is named for that timing question.

## November plan

**Final evaluation.** Score the training mean, the training median, the recorded random forest, and the recorded XGBoost on the 28,248 test claims. Fit preprocessing and models on the training claims only. Do not refit them on the test claims, and do not use the test paid amounts to choose a model, a feature, or a new seed. Report all four test scores in original dollars. The validation table stays as the October comparison. The test table is a separate final check. Because September already explored the full file, say that this internal test is a held-out slice of a file the team has already seen. It is not a later time period.

**Key predictors, if time permits.** Any importance or coefficient check uses training claims only. The result is a rank of anonymous columns on this file. `cat*` and `cont*` names are statistical predictors. They are not confirmed business concepts. The project overview's examples of field types are not a dictionary for these columns. A column score does not show a cause and does not set a reserve for one claim.

**Presentation.** Show the split, the two constant scores, the two model scores, the large-claim check on 285 validation claims, and the decision not to name a model. State that the fields have not been confirmed as available at first filing, and that September had already looked at all 188,318 claims before the split.

**Result documentation.** Add the test scores next to this handoff when they exist. Keep the validation tables in [`../experiments/validation_mae.csv`](../experiments/validation_mae.csv). Keep the plain-language account in [`october_report.md`](october_report.md).
