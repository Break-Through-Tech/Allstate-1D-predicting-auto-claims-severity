# Gate 4 — October model development

Bundle ID: `gate4-october-milestone-reproducible-project`

This folder is the October evidence package. A reviewer can check the handoff, the contract, the split, the baseline scores, the comparison, and the reproduction steps without leaving this directory.

Gate 4 is not passed. September's teammate sign-off is still blank, and [`review/independent_review.md`](review/independent_review.md) is unsigned. The lowest validation MAE does not close the gate.

## Files

| Path | Role |
| --- | --- |
| [`handoff/september_handoff.md`](handoff/september_handoff.md) | September handoff and the two recommendation decisions. Sign-off still open. |
| [`handoff/october_report.md`](handoff/october_report.md) | Plain-language October report: split, scores, comparison, and the decision not to name a model |
| [`handoff/november_handoff.md`](handoff/november_handoff.md) | November package: pipeline version, no-selection decision, test plan, deferred feature test, and advisor questions |
| [`modeling-contract.md`](modeling-contract.md) | Task, field roles, MAE rule, and the limits on a score |
| [`evaluation-plan.md`](evaluation-plan.md) | Validation use, 5 training folds, stopping rule, and the November holdout |
| [`field_roles.csv`](field_roles.csv) | Role and model-input flag for all 132 columns |
| [`manifests/source_identity.csv`](manifests/source_identity.csv) | Source path, size, shape, and SHA-256 |
| [`manifests/gate1_partition_manifest.csv`](manifests/gate1_partition_manifest.csv) | Claim `id` and partition for all 188,318 rows |
| [`manifests/train-validation-design.md`](manifests/train-validation-design.md) | Split method, seed, eligibility, and the check results |
| [`baselines/baseline_validation_mae.csv`](baselines/baseline_validation_mae.csv) | Training-mean and training-median validation MAE |
| [`baselines/mean_constant_validation_predictions.csv`](baselines/mean_constant_validation_predictions.csv) | Mean constant for each validation claim |
| [`baselines/median_constant_validation_predictions.csv`](baselines/median_constant_validation_predictions.csv) | Median constant for each validation claim |
| [`preprocessing/training_preprocessor.py`](preprocessing/training_preprocessor.py) | Training-only median fill and one-hot encoding |
| [`experiments/experiment_register.csv`](experiments/experiment_register.csv) | Constants, forest, XGBoost, and the iteration that was not refit |
| [`experiments/validation_mae.csv`](experiments/validation_mae.csv) | Comparison table in original `loss` units |
| [`experiments/high_loss_tail.csv`](experiments/high_loss_tail.csv) | MAE on the 285 high-loss validation claims and on the remainder |
| [`experiments/regenerate_validation_predictions.md`](experiments/regenerate_validation_predictions.md) | Where the constant predictions are, and how to rerun the model predictions |
| [`registers/anomaly_register.csv`](registers/anomaly_register.csv) | September anomaly row `GATE1-000`. No blocking anomaly. |
| [`review/gate2_baseline_run_receipt.md`](review/gate2_baseline_run_receipt.md) | Printed Gate 2 baseline receipt |
| [`review/reproduction.md`](review/reproduction.md) | How a teammate reruns the notebooks and checks this folder |
| [`review/independent_review.md`](review/independent_review.md) | Teammate sign-off. Pending. |
