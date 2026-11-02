# November handoff

## Feature decision for October Gate 3

| Decision | Record |
| --- | --- |
| Included | All 130 inputs in `field_roles.csv`: `cat1` through `cat116` and `cont1` through `cont14` |
| Excluded | None. `id` and `loss` were already out of the inputs |
| Selection rule | The list was frozen before the fit. No field was added or removed after seeing validation MAE |
| Gate 3 status | This deferral does not block Gate 3 |

- A weak September correlation with `loss` is not a removal reason. `cont1` is about -0.01 and stays in.
- Correlation with another field is not a removal reason. These pairs stay in: `cont11` and `cont12` (about 0.994), `cont1` and `cont9` (about 0.930), and `cont6` and `cont10` (about 0.883).
- Those September figures use the full file, including claims that are now validation and test.

## Deferred hypothesis

Refit the recorded XGBoost settings after removing one field from the `cont11` and `cont12` pair. Choose the removed field from the training claims only. Use the same preprocessing, the same 5 training folds, `random_state=1`, and one validation MAE on the same 28,248 claims. Keep the field unless that validation MAE is lower than the recorded XGBoost score of $1,171.72.

This was not run in October. Gate 3 had already used its one iteration on the training-versus-fold check, and that check did not support another fit.