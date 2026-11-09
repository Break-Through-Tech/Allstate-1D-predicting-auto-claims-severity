# Gate 2 baseline run receipt

This is the report printed by `notebooks/OctoberMilestones/October_Gate_2.ipynb`. The notebook also wrote `/content/gate2_baseline_run_receipt.json` in that Colab session. That JSON file is not in the repository. The printed values are below.

| Item | Printed value |
| --- | --- |
| Partition manifest ID | `sha256:0e97b61a8ad550387f2c7bcbe2b4130064e790337e88d1a5251399ce91830418` |
| Validation claims | 28,248 |
| Target | `loss`, original units |
| Source SHA-256 | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03` |
| Code version | Git commit unavailable in that Colab session |
| Mean constant | 3033.6880441807893 |
| Mean validation MAE | 1978.3970470120255 |
| Mean MAE checked with NumPy | 1978.3970470120255 |
| Median constant | 2113.755 |
| Median validation MAE | 1827.3136338855847 |
| Median MAE checked with NumPy | 1827.3136338855847 |

The printed checks all passed: one prediction per validation claim, prediction ids aligned with the validation ids, unique validation ids, finite mean and median predictions, and both MAE checks.

The manifest file in [`../manifests/gate1_partition_manifest.csv`](../manifests/gate1_partition_manifest.csv) has the same SHA-256 as the printed manifest ID.
