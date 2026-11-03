# Evaluation plan

Bundle ID: `gate4-october-milestone-reproducible-project`

This is the Gate 1 evaluation design, placed next to the comparison that used it. The split mechanics are in [`manifests/train-validation-design.md`](manifests/train-validation-design.md). The task and the limits on a score are in [`modeling-contract.md`](modeling-contract.md).

## The comparison

October compares approaches with mean absolute error on the validation partition, in original `loss` units. The validation partition has 28,248 claims. The evaluation code is `sklearn.metrics.mean_absolute_error`.

Validation is for comparison and for the stopping rule below. It is kept out of fitting, out of encoders, and out of any rule that is learned from data. The training partition is the only place those steps may be fit.

The seed stays `random_state=1` when a validation MAE looks unfavorable. An unfavorable validation score is not a reason to draw a new split. Tuning stops when validation MAE fails to improve for 3 consecutive tuning runs.

The comparison used 5 folds inside the 131,822 training claims, with `random_state=1`. Validation and test claims stayed outside those folds. That fold count is recorded in [`experiments/experiment_register.csv`](experiments/experiment_register.csv).

## November test partition

A 15% test partition is reserved for November's final evaluation. It has 28,248 claims. Membership and the row count are in [`manifests/gate1_partition_manifest.csv`](manifests/gate1_partition_manifest.csv). This folder has no test MAE.

During October, test claims stay out of fitting, encoding, feature construction, model selection, and the decision to stop. The approved final use of those targets is the November evaluation.

## Constant predictors

Two constants are the reference for every later model. Each constant is one number taken from the training `loss` values and predicted for every validation claim.

| Baseline | Training constant | Validation claims | Validation MAE | Code |
| --- | ---: | ---: | ---: | --- |
| Training mean | 3033.6880441807893 | 28,248 | 1978.3970470120255 | `sklearn.metrics.mean_absolute_error` |
| Training median | 2113.755 | 28,248 | 1827.3136338855847 | `sklearn.metrics.mean_absolute_error` |

The same rows are in [`baselines/baseline_validation_mae.csv`](baselines/baseline_validation_mae.csv). The prediction rows are in [`baselines/mean_constant_validation_predictions.csv`](baselines/mean_constant_validation_predictions.csv) and [`baselines/median_constant_validation_predictions.csv`](baselines/median_constant_validation_predictions.csv). The median sits beside the required mean because a constant median minimizes absolute error. A later model is an improvement on the constants only when its validation MAE is lower than both, on these same 28,248 claims.

September reported a full-file median error of 1809.0487864675708. That figure uses every row, including the rows that are now validation and test. It is a description of the file. It is a different number from the validation scores in the table above.

## Prior exposure

September exploratory analysis summarized and plotted `loss` on the full file of 188,318 claims before this split was drawn. The claims now called validation or test were included in that work. This evaluation plan keeps those claims out of October fitting and tuning. A reader should treat the internal scores as a check on this supplied file after the team had already seen the full-file patterns.
