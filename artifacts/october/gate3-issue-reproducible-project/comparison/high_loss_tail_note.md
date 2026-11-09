# High-loss tail note

The cut is the training 99th percentile of loss, $14,017.41. That slice has 285 validation claims. The other 27,963 validation claims are the remainder.

Both models have a lower overall validation MAE than both constants, and both models also have a lower MAE on the 285 large claims. On that comparison, overall error and large-claim error move together.

They do not move together between the two models. XGBoost has the lower overall validation MAE, $1,171.72 against the forest's $1,291.59. The forest has the lower large-claim MAE, $8,868.69 against XGBoost's $9,265.72. The same split appears between the constants: the median has the lower overall MAE, and the mean has the lower large-claim MAE.

This note does not select a model. The large-claim MAE is a check on 285 claims, not a reason to prefer the forest or XGBoost.
