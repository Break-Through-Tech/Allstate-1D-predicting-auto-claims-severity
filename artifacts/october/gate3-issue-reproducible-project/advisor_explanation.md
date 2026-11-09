# Advisor explanation

## Shared setup

- **Inputs:** 130 anonymous fields from `field_roles.csv`. `cat1` through `cat116` are categories. `cont1` through `cont14` are numbers. The names do not say what the fields mean.
- **Left out:** `id` and `loss`.
- **Encoding:** Fit on the 131,822 training claims only. Missing numbers use the training median. Missing categories use the training mode. Each category becomes yes-or-no columns. A level absent from training is ignored. The number fields stay on their original 0-to-1 scale.
- **Output:** A predicted paid loss in dollars.
- **Score:** The average dollar miss on the 28,248 validation claims.
- **What the score is:** A retrospective check on this supplied file. It is not a reserve for one claim. It is not an up-front estimator, because the field names do not say which inputs exist when a claim is first filed.

## Models

| | Random forest | XGBoost |
| --- | --- | --- |
| How it learns | Grows 100 trees. Each tree sorts claims into groups with similar paid amounts. The prediction is the average of the trees. | Adds trees one at a time. Each new tree tries to shrink the dollar misses left by the trees already built. |
| Key setting | `max_depth=12` | `objective='reg:absoluteerror'` |
| Other first-fit settings | 100 trees, at least 20 training claims in each final group, `random_state=1` | 200 trees, `max_depth=6`, learning rate 0.1, `random_state=1` |
| Validation MAE | $1,291.59 | $1,171.72 |
| Against the constants | Lower than both | Lower than both |

- The two validation scores differ by about $119.87.
- That gap is under 10% of the forest score.
- This note does not choose a model.
- The iteration did not change a setting, so it is not a third model.

## What a field score cannot mean

- `cat1` through `cat116` and `cont1` through `cont14` stay anonymous predictors. The project overview's examples are examples of field types. They are not a dictionary for these columns.
- This comparison did not compute a coefficient or an importance score.
- A later coefficient or importance score would still be a score for that column on this file. It would not establish the field's business meaning.
- It would not establish a causal effect. The model was fit to predict paid loss, not to say what would happen if one field were changed.