# October report

This report describes the October model comparison for the supplied Allstate claims file. It states the split, the two constant scores, the two models that were fit, the validation comparison, the main error pattern, and the decision not to name a model. The exact figures are in the tables linked below.

One row is one anonymized auto-insurance claim. The target is `loss`, the claim's paid amount, in dollars. The score is the average dollar miss on the validation claims: mean absolute error in the original paid-amount units.

## Split

Every one of the 188,318 claims is eligible, including the largest payments. The split uses `train_test_split` and `random_state=1`.

| Partition | Claims | Role |
| --- | ---: | --- |
| Train | 131,822 | Fit the preprocessing and the models |
| Validation | 28,248 | Compare approaches |
| Test | 28,248 | Held for November |

The membership list is [`../manifests/gate1_partition_manifest.csv`](../manifests/gate1_partition_manifest.csv). The design note is [`../manifests/train-validation-design.md`](../manifests/train-validation-design.md). The seed stays `random_state=1` when a validation score looks unfavorable. Tuning stops when validation error fails to improve for 3 consecutive tuning runs.

The test claims were not scored in October. A later score on those claims would still be a score on this same file. September had already explored the full file, including the claims that were later labeled test. That later score would not be a check on a new time period or on claims the team had never seen.

## Inputs and encoding

The model sees 130 anonymous fields, listed in [`../field_roles.csv`](../field_roles.csv). `cat1` through `cat116` are category labels. `cont1` through `cont14` are numbers on a 0-to-1 scale. The column names do not say what any field means in the business. `id` only identifies the claim. `loss` is the target. Both stay out of the inputs.

Encoding is fit on the 131,822 training claims and then applied to validation. A missing number is filled with the training median. A missing category is filled with the training mode. Each category level becomes its own yes-or-no column. A level that shows up in validation and was absent from training is ignored, so it does not create a new column and it does not use the validation paid amount. The code is [`../preprocessing/training_preprocessor.py`](../preprocessing/training_preprocessor.py). Twenty-one validation levels, across eight fields, were already known to be absent from training.

## Baselines

Both constants are one number taken from the training payments and predicted for every validation claim.

| Approach | Training constant | Validation average miss |
| --- | ---: | ---: |
| Training mean | $3,033.69 | $1,978.40 |
| Training median | $2,113.76 | $1,827.31 |

The median is included because, among single-number predictions, the median minimizes absolute error. Full precision is in [`../baselines/baseline_validation_mae.csv`](../baselines/baseline_validation_mae.csv). September's full-file median error, about $1,809.05, describes every row before the split. It is a different number from the validation scores above.

## Approaches tested

Two models were fit after the constants. The project overview lists GLM, random forest, gradient boosting, and XGBoost as examples. October tested two of those examples.

The random forest grows 100 trees. Each tree sorts claims into groups with similar paid amounts. The prediction is the average of the trees. No tree is deeper than 12 splits, and each final group keeps at least 20 training claims. The seed is `random_state=1`.

XGBoost adds trees one at a time. Each new tree tries to shrink the dollar misses left by the trees already built. It uses the objective `reg:absoluteerror`, 200 trees, a maximum depth of 6, a learning rate of 0.1, and `random_state=1`.

Both models were also scored with 5 folds inside the training claims. Those folds did not include validation or test claims. The output of either model is a predicted paid amount in dollars for one claim. The validation score is the average size of the miss across the 28,248 validation claims.

The planned iteration checked whether the in-sample training error was far below the 5-fold error. The two were close for both models, about $8.76 apart on the validation check as well. The iteration did not change a setting and did not refit.

## Validated comparison

| Approach | 5-fold training miss | Validation miss | Better than the mean by | Better than the median by |
| --- | ---: | ---: | ---: | ---: |
| Training mean |  | $1,978.40 | $0 | worse by $151.08 |
| Training median |  | $1,827.31 | $151.08 | $0 |
| Random forest | $1,282.83 | $1,291.59 | $686.81 | $535.72 |
| XGBoost | $1,162.96 | $1,171.72 | $806.68 | $655.59 |

Both models have a lower validation miss than both constants on the same 28,248 claims. XGBoost's validation miss is about $119.87 lower than the forest's. That gap is under 10% of the forest score. The full table is [`../experiments/validation_mae.csv`](../experiments/validation_mae.csv).

## Where the errors sit

The high-payment slice is the training 99th percentile, about $14,017. That slice has 285 validation claims. The other 27,963 validation claims are the remainder. Full figures are in [`../experiments/high_loss_tail.csv`](../experiments/high_loss_tail.csv).

| Approach | Average miss on 285 large claims | Average miss on the other 27,963 |
| --- | ---: | ---: |
| Training mean | $15,529.25 | $1,840.29 |
| Training median | $16,449.18 | $1,678.29 |
| Random forest | $8,868.69 | $1,214.37 |
| XGBoost | $9,265.72 | $1,089.22 |

Both models miss less than both constants on the large claims and on the remainder. Between the two models, the pattern splits. XGBoost has the smaller overall miss and the smaller miss on the 27,963 ordinary claims. The forest has the smaller miss on the 285 large claims. The same split appears between the constants: the median is closer overall, and the mean is closer on the large claims. The large-claim figure is a check on 285 claims. It was not used as a new rule for picking a model.

## Decision

October does not name a provisional model. Both models beat both constants, and the two model scores are close. [`../experiments/reliability.md`](../experiments/reliability.md) records that the evidence is too weak to prefer one. The deferred feature test, dropping one field from the `cont11` and `cont12` pair, was not run. It is written in [`november_handoff.md`](november_handoff.md).

## Limits

These scores are a retrospective check on the supplied file. They show how close the recorded predictions were to paid amounts the file already contains. They do not show that the same fields are known when a claim is first filed. The Challenge Advisor has not confirmed that timing, so this report does not call either model an up-front estimator.

September exploratory analysis had already summarized and plotted `loss` on all 188,318 claims before this split was drawn. The validation claims, and the claims reserved for the internal test, were inside that earlier look. Keeping those claims out of October fitting protects them from later tuning. It does not make the internal test a fresh sample.

A score here does not set a reserve for one claim, does not show a cause, and does not show that a model is ready for production. No field was given a business meaning. This comparison did not compute a coefficient or an importance score. The anonymous column names stay anonymous.

Gate 4 is not closed. The September teammate sign-off is still blank, and [`../review/independent_review.md`](../review/independent_review.md) is unsigned.
