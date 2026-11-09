# How to regenerate validation predictions

The constant predictions are already in this package.

| File | Rule |
| --- | --- |
| [`../baselines/mean_constant_validation_predictions.csv`](../baselines/mean_constant_validation_predictions.csv) | Every validation `id` in [`../manifests/gate1_partition_manifest.csv`](../manifests/gate1_partition_manifest.csv) gets `3033.6880441807893` |
| [`../baselines/median_constant_validation_predictions.csv`](../baselines/median_constant_validation_predictions.csv) | Every validation `id` gets `2113.755` |

Each file has 28,248 rows and one prediction per validation claim. The MAE from those predictions is in [`../baselines/baseline_validation_mae.csv`](../baselines/baseline_validation_mae.csv).

The random forest and XGBoost prediction rows are not stored. `notebooks/OctoberMilestones/October_Gate_3.ipynb` builds them with the pipeline in [`../preprocessing/training_preprocessor.py`](../preprocessing/training_preprocessor.py), the settings in [`experiment_register.csv`](experiment_register.csv), and `random_state=1`. Rerun that notebook to regenerate the validation predictions and the scores in [`validation_mae.csv`](validation_mae.csv). The iteration row was not refit, so it has no predictions.
