# Gate 2 Artifact Bundle

Bundle ID: `gate2-issue-reproducible-project`

Related project task: [GitHub issue 9](https://github.com/Break-Through-Tech/Allstate-1D-predicting-auto-claims-severity/issues/9)

## Overview

This bundle freezes the September analysis contract and records the tables calculated in `notebooks/SeptemberMilestone/Gate_2.ipynb`. The notebook's `loss` mean is 3,037.337686, its median is 2,115.57, and its full-file median baseline MAE is 1,809.0487864675708. `cat112` has 30 levels below the 1 percent display threshold. `cont2` produced 9 quantile bins.

Team approval is still pending in [`review/team_approval.md`](review/team_approval.md).

`gate_2_readme.md` was already in this folder. The frozen files below are the September method record. `log1p(loss)` is a plot field, rare levels stay in the source, and a full-file median MAE is not held-out performance.

## Work done

- Saved the notebook data dictionary for all 132 fields: data type, missing count, and unique count.
- Saved the notebook `loss` summary, the raw and `log1p(loss)` histograms, and the median-constant MAE of 1,809.0487864675708.
- Saved the 14-field continuous summary and the Pearson correlation matrix, including correlations with `loss`.
- Saved the `cat112` level shares and the count and box plots used by the 1 percent display rule. Thirty of 51 levels are below that threshold.
- Saved the `cont2` quantile-bin table and box plot. The requested 10 bins became 9 because of repeated values.

## Files

| Path | Role |
| --- | --- |
| [`methods/analysis_contract.md`](methods/analysis_contract.md) | Aim, unit, target, MAE, anonymous fields, and non-uses |
| [`methods/data_dictionary.csv`](methods/data_dictionary.csv) | Notebook dictionary: data type, missing count, and unique count for 132 fields |
| [`methods/rare_level_rule.md`](methods/rare_level_rule.md) | 1 percent display threshold and how plots use it |
| [`methods/quantile_bin_rule.md`](methods/quantile_bin_rule.md) | 10-bin `qcut` rule and the `cont2` result of 9 bins |
| [`methods/target_view_settings.md`](methods/target_view_settings.md) | Histogram settings and the saved `loss` summary |
| [`methods/findings_register_format.md`](methods/findings_register_format.md) | Columns and evidence-status terms for Gate 3 |
| [`tables/loss_summary.csv`](tables/loss_summary.csv) | Notebook `describe()` result for `loss` |
| [`tables/baseline_mae.csv`](tables/baseline_mae.csv) | Full-file median-constant MAE from the notebook |
| [`tables/continuous_summary.csv`](tables/continuous_summary.csv) | Notebook `describe()` result for `cont1` through `cont14` |
| [`tables/continuous_correlation.csv`](tables/continuous_correlation.csv) | Notebook Pearson correlations among the continuous fields and `loss` |
| [`tables/cat112_level_shares.csv`](tables/cat112_level_shares.csv) | Level support and share for the notebook's `cat112` example |
| [`tables/cont2_quantile_bins.csv`](tables/cont2_quantile_bins.csv) | Nine `cont2` bins with support, mean `loss`, median `loss`, and interquartile range |
| [`visualizations/loss_distribution.jpg`](visualizations/loss_distribution.jpg) | Notebook histograms of raw `loss` and `log1p(loss)` |
| [`visualizations/cat112_distribution.jpg`](visualizations/cat112_distribution.jpg) | Count plot and `log1p(loss)` box plot for `cat112`, with rare levels grouped as Other |
| [`visualizations/cont2_quantile_bins.jpg`](visualizations/cont2_quantile_bins.jpg) | Box plot of `log1p(loss)` across the nine `cont2` quantile bins |
| [`review/team_approval.md`](review/team_approval.md) | Pending approval of this method freeze |
| `gate_2_readme.md` | Earlier folder note. The files above are the September method record. |
