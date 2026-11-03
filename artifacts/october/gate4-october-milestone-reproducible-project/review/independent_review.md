# Gate 4 independent review

Bundle ID: `gate4-october-milestone-reproducible-project`

This review is not signed. A teammate who did not write the October notebooks still has to follow [`reproduction.md`](reproduction.md) and fill in the lines below. Gate 4 stays open until that rerun is recorded.

September Gate 4 is also unsigned in [`../../../september/gate4-september-milestone-reproducible-project/review/independent_review.md`](../../../september/gate4-september-milestone-reproducible-project/review/independent_review.md).

## Checks

- Source SHA-256 matches [`../manifests/source_identity.csv`](../manifests/source_identity.csv).
- Manifest SHA-256 matches the value in [`reproduction.md`](reproduction.md).
- Train, validation, and test do not share an `id`.
- The mean and median validation MAEs match [`../baselines/baseline_validation_mae.csv`](../baselines/baseline_validation_mae.csv).
- The comparison table matches [`../experiments/validation_mae.csv`](../experiments/validation_mae.csv).
- Learned preprocessing is the training-only pipeline in [`../preprocessing/training_preprocessor.py`](../preprocessing/training_preprocessor.py).

## Sign-off

- Reviewer: pending
- Date: pending
- Git revision checked: pending
- Source SHA-256 checked: pending
- Manifest checked: pending
- Baseline MAE checked: pending
- One candidate comparison checked: pending
- Disagreements: pending
- Result: pending teammate rerun
