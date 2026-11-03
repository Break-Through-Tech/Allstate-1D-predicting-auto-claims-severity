# Reproduction

A teammate can rebuild the tables in this folder from the committed source, the manifest, and the October notebooks. This file does not replace an independent rerun.

## Locked inputs

| Item | Location |
| --- | --- |
| Source | `data/allstate_claims_data.csv` |
| Source SHA-256 | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03`, also in [`../manifests/source_identity.csv`](../manifests/source_identity.csv) |
| Split manifest | [`../manifests/gate1_partition_manifest.csv`](../manifests/gate1_partition_manifest.csv) |
| Manifest SHA-256 | `0e97b61a8ad550387f2c7bcbe2b4130064e790337e88d1a5251399ce91830418` |
| Field list | [`../field_roles.csv`](../field_roles.csv) |
| Seed | `random_state=1` |

## Steps

1. Open `notebooks/OctoberMilestones/OctoberGate1.ipynb` from the repository and load `data/allstate_claims_data.csv`. The split is `train_test_split` with `random_state=1`, 15% test, then 15% of the original file as validation.
2. Check the manifest against [`../manifests/partition_checks.csv`](../manifests/partition_checks.csv): 188,318 rows, 188,318 distinct ids, and no shared id across train, validation, and test.
3. Open `notebooks/OctoberMilestones/October_Gate_2.ipynb`. Fit the training-mean and training-median constants on the training `loss` only. Score them on the 28,248 validation claims with `sklearn.metrics.mean_absolute_error`, and again with the mean of absolute differences in NumPy. Match [`../baselines/baseline_validation_mae.csv`](../baselines/baseline_validation_mae.csv) and [`gate2_baseline_run_receipt.md`](gate2_baseline_run_receipt.md).
4. Open `notebooks/OctoberMilestones/October_Gate_3.ipynb`. Fit the pipeline in [`../preprocessing/training_preprocessor.py`](../preprocessing/training_preprocessor.py) on training rows. Use 5 folds inside the training partition, `random_state=1`, then one validation MAE. Match [`../experiments/experiment_register.csv`](../experiments/experiment_register.csv) and [`../experiments/validation_mae.csv`](../experiments/validation_mae.csv).
5. Leave the test partition out of fitting, encoding, and model selection. This folder has no test MAE.

The forest and XGBoost validation prediction rows are produced by step 4. They are not saved as their own files. The constant prediction files in `baselines/` can be checked without refitting: assign the recorded training constant to every validation id.
