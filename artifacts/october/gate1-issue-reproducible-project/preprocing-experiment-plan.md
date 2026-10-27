# Preprocessing and experiment plan

Bundle ID: `gate1-issue-reproducible-project`

Source notebook: [`../../../notebooks/OctoberMilestones/OctoberGate1.ipynb`](../../../notebooks/OctoberMilestones/OctoberGate1.ipynb)

This plan is the first comparison the team intends to run after Gate 1 is approved. It freezes the rules. It does not contain fitted model scores.

## Preprocessing

- Every learned step is fit on training rows only, then applied to validation rows. That includes imputers, scalers, category vocabularies, and encoders. Validation `loss` is not an input to those steps.
- Numeric missing values are filled with the training median. September found 0 missing cells in the source file. The rule is still recorded so a later pipeline does not invent a different fill.
- Nominal categories are one-hot encoded. A level that is rare in training, or that shows up later and was absent from training, is ignored (`handle_unknown='ignore'`). The 21 validation levels already known to be absent from training are listed in [`splits/unseen_validation_levels.csv`](splits/unseen_validation_levels.csv). Gate 2 records how many validation claims those levels affect. This plan does not set the ignore rule from validation `loss`.
- Target encoding is out of scope for the first comparison. If a later plan proposes it, that plan has to fit the encoding inside training folds and needs a training-only fallback for unseen or rare levels.
- Feature inclusion or exclusion tests are optional and are not part of the first comparison. A field is not dropped because its September correlation was weak or because it is correlated with another field. Dropping highly correlated features stays deferred in the [modeling contract](modeling-contract.md). Outlier-only row removal is also deferred; high-loss claims remain.

## Constant comparators

The first rows of the comparison are the two constants in [`evalutation-design/baseline_validation_mae.csv`](evalutation-design/baseline_validation_mae.csv):

- Training-mean constant, required. Validation MAE 1978.3970470120255 on 28,248 claims.
- Training-median constant, the companion. Validation MAE 1827.3136338855847 on the same claims. Among constant predictions, the median minimizes absolute error.

Both use the partition manifest [`splits/gate1_partition_manifest.csv`](splits/gate1_partition_manifest.csv) and `sklearn.metrics.mean_absolute_error`.

## Two model approaches

The project overview lists GLM, random forest, gradient boosting, and XGBoost as examples. This plan tests two of them after the constants. It does not require every example to be run, and it does not name a winner.

1. **Random forest.** Hypothesis: a tree ensemble can represent non-linear relationships among the anonymous fields. Practical reason: trees do not need the continuous fields to be rescaled before fitting.
2. **XGBoost.** Hypothesis: gradient boosting aimed straight at absolute error can lower MAE relative to a constant. Practical reason: the booster can use the objective `reg:absoluteerror`, which matches the project metric. The project MAE is still computed in original `loss` units.

Settings, software versions for the fit, runtime, and a workflow run are recorded when those models are actually trained. They are blank at Gate 1.

Validation use and the 3-run stopping rule are in [`evalutation-design/evaluation-design.md`](evalutation-design/evaluation-design.md).

## Planned comparison record

Each later run should add a row with the hypothesis, the feature set, this manifest, the preprocessing and model settings, the seed, the code version, a run receipt, and the resource cost. The planned first comparison is:

| Piece | Planned value | Status |
| --- | --- | --- |
| Hypothesis | A random forest and an XGBoost model, each fit on the frozen training claims, can be compared with the two constants on validation MAE | Planned |
| Feature set | All 130 inputs in [`field_roles.csv`](field_roles.csv). `id` and `loss` excluded | Frozen |
| Partition manifest | [`splits/gate1_partition_manifest.csv`](splits/gate1_partition_manifest.csv), `random_state=1` | Frozen |
| Preprocessing | Training-only median fill for numeric gaps; one-hot encoding with `handle_unknown='ignore'` | Frozen as a rule; pipeline code is Gate 2 |
| Models | Random forest; XGBoost with `reg:absoluteerror` | Chosen; not fit |
| Seed | `random_state=1` for the split. Model seeds are recorded with each fit | Split seed frozen |
| Code version | Notebook `notebooks/OctoberMilestones/OctoberGate1.ipynb`. Split reproduced with Python 3.12.4, pandas 3.0.6, NumPy 2.5.3, scikit-learn 1.9.1 | Recorded for the split |
| Run receipt | None yet for a feature-based model | Open until Gate 3 |
| Resource cost | None yet | Open until Gate 3 |
| Comparison | Validation MAE in original `loss` units, against both constants, on 28,248 claims | Rule frozen |
| Feature inclusion or exclusion | Optional. Not in the first comparison | Deferred |
| Target encoding | Out of scope for the first comparison | Deferred |
| Outlier handling beyond keeping the rows | REC-001, deferred | Deferred |
