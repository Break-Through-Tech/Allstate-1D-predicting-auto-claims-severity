# October recommendation register

These are the only two October recommendations. Both are future work. September did not do them, and this list does not pick a model.

The source file is `data/allstate_claims_data.csv` (188,318 claims, 132 columns), recorded in `[../source/source_identity.csv](../source/source_identity.csv)`. The target and the MAE rule are in `[../methods/analysis_contract.md](../methods/analysis_contract.md)`.

## REC-001 — Decide whether to look further at features with outliers

- Look again at the features whose plots show outlier points. Decide if any pattern is strong enough to handle that field differently later. This decision does not delete those points.
- Evidence links: `[../eda/continuous/continuous_boxplots.jpg](../eda/continuous/continuous_boxplots.jpg)` shows all 14 `cont*` fields, including points outside the whiskers. `[../eda/continuous/continuous_summary.csv](../eda/continuous/continuous_summary.csv)` shows those values still sit on a 0-to-1 scale. `[../registers/anomaly_register.csv](../registers/anomaly_register.csv)` records that no rows were removed. September did not study which of those outlying points form a pattern worth extra handling.



## REC-002 — Research model types commonly used to estimate a loss amount

- What October would do: Read which machine-learning model types are typically used when the goal is to estimate a loss amount. Create a short list for the team to discuss.
- Evidence links: `[../methods/analysis_contract.md](../methods/analysis_contract.md)` says the target is `loss`, the paid amount, and the score is MAE in original `loss` units. `[../eda/target/target_summary.csv](../eda/target/target_summary.csv)` shows that distribution is right-skewed (mean 3,037.34, median 2,115.57, skewness 3.795). `Challenge-Project-Overview.md` lists GLM, random forest, gradient boosting, and XGBoost as examples only.

