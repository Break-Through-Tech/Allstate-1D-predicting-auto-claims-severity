# Gate 3 Artifact Bundle

Bundle ID: `gate3-issue-reproducible-project`

Related milestone checks: data quality, target distribution, categorical evidence, continuous evidence, and the findings register in `docs/coach/september-execution/Allstate-Sept-Milestones.md`.

## Overview

This bundle records the Gate 3 evidence calculated from `data/allstate_claims_data.csv`. Running `notebooks/SeptemberMilestone/Gate 3.ipynb` from the cloned repository writes the tables and figures below. The file has 188,318 rows and 132 columns. Mean `loss` is 3,037.34, median `loss` is 2,115.57, the 95th percentile is 8,508.54, the maximum is 121,012.25, and raw skewness is 3.795. Headline numbers stay in original `loss` units.

72 of 116 categorical fields have 2 levels, and 88 have at most 4. `cat116` has 326 levels, `cat110` has 131, and `cat109` has 84. The strongest Pearson correlations with raw `loss` are `cont2` at 0.142, `cont7` at 0.120, and `cont3` at 0.111. No continuous field was removed.

Gate 2 method approval is still pending. These files record the evidence. They do not mark Gate 3 as team-approved. A teammate recalculation is still open in [`review/independent_review.md`](review/independent_review.md).

## Work done

- Saved the source profile: row count, column count, role counts, unique `id`, missing cells, duplicate rows, and non-positive `loss`.
- Saved the `loss` summary, including the 95th percentile and skewness, plus raw and `log1p(loss)` histograms and a raw boxplot with outliers shown.
- Saved cardinality for all 116 categorical fields and a level-to-target table with support, share, raw mean `loss`, raw median `loss`, and interquartile range. 227 levels have fewer than 10 claims, and those levels appear on 616 rows. 64 levels each cover at least 90 percent of claims.
- Saved support plots for rare and dominant levels, loss boxplots for `cat57`, `cat89`, and `cat7`, and a high-cardinality review of `cat116`, `cat110`, and `cat109` with every level retained.
- Saved the 14-field continuous summary, histograms, and boxplots. Every observed `cont*` value is on the 0-to-1 scale.
- Saved 10-bin quantile target tables. `cont2` has 9 bins and `cont5` has 8 because repeated values cannot make 10 edges. The other continuous fields have 10 bins.
- Saved Pearson and Spearman associations with raw `loss` and `log1p(loss)`, the continuous Pearson matrix, and the three strongest pairs: `cont11`–`cont12` at 0.994, `cont1`–`cont9` at 0.930, and `cont6`–`cont10` at 0.883.
- Saved a findings register with the seven required topics. The reviewer column is pending.

## Files

| Path | Role |
| --- | --- |
| [`findings_tables/data_quality.csv`](findings_tables/data_quality.csv) | Rows, columns, roles, identifier, duplicates, missingness, and non-positive `loss` |
| [`findings_tables/target_summary.csv`](findings_tables/target_summary.csv) | Mean, median, percentiles, maximum, and skewness of `loss` |
| [`findings_tables/categorical_cardinality.csv`](findings_tables/categorical_cardinality.csv) | Observed level count and largest-level share for all 116 `cat*` fields |
| [`findings_tables/categorical_level_target.csv`](findings_tables/categorical_level_target.csv) | Support, share, raw mean, raw median, and interquartile range for 1,139 levels |
| [`findings_tables/low_support_levels.csv`](findings_tables/low_support_levels.csv) | Levels with fewer than 10 claims |
| [`findings_tables/dominant_levels.csv`](findings_tables/dominant_levels.csv) | Levels that cover at least 90 percent of claims |
| [`findings_tables/continuous_summary.csv`](findings_tables/continuous_summary.csv) | `describe()` result for `cont1` through `cont14` |
| [`findings_tables/continuous_quantile_bins.csv`](findings_tables/continuous_quantile_bins.csv) | Quantile bins with support, raw mean `loss`, raw median `loss`, and interquartile range |
| [`findings_tables/continuous_target_correlation.csv`](findings_tables/continuous_target_correlation.csv) | Pearson and Spearman association of each `cont*` field with `loss` and `log1p(loss)` |
| [`findings_tables/continuous_pearson_matrix.csv`](findings_tables/continuous_pearson_matrix.csv) | Pearson correlations among the 14 continuous fields |
| [`findings_tables/continuous_feature_pairs.csv`](findings_tables/continuous_feature_pairs.csv) | Pearson and Spearman values for the three strongest continuous pairs |
| [`findings_tables/findings_register.csv`](findings_tables/findings_register.csv) | Seven findings with evidence status, limitation, and October implication |
| [`visualizations/target_loss_views.jpg`](visualizations/target_loss_views.jpg) | Raw histogram, `log1p(loss)` histogram, and raw boxplot |
| [`visualizations/categorical_binary_loss_boxplots.jpg`](visualizations/categorical_binary_loss_boxplots.jpg) | Raw `loss` by level for `cat57`, `cat89`, and `cat7`, with support in the labels |
| [`visualizations/categorical_support.jpg`](visualizations/categorical_support.jpg) | Examples of levels below 10 claims and levels covering at least 90 percent of claims |
| [`visualizations/high_cardinality_review.jpg`](visualizations/high_cardinality_review.jpg) | Support and median `loss` for every level of `cat116`, `cat110`, and `cat109` |
| [`visualizations/continuous_histograms.jpg`](visualizations/continuous_histograms.jpg) | Histograms of all 14 continuous fields |
| [`visualizations/continuous_boxplots.jpg`](visualizations/continuous_boxplots.jpg) | Boxplots of all 14 continuous fields |
| [`visualizations/continuous_binned_target.jpg`](visualizations/continuous_binned_target.jpg) | Mean and median `loss` across quantile bins for all 14 continuous fields |
| [`visualizations/continuous_binned_loss_boxplots.jpg`](visualizations/continuous_binned_loss_boxplots.jpg) | Raw `loss` boxplots across the quantile bins for all 14 continuous fields |
| [`visualizations/continuous_correlation_heatmap.jpg`](visualizations/continuous_correlation_heatmap.jpg) | Pearson heatmap of the continuous fields |
| [`review/independent_review.md`](review/independent_review.md) | Recalculated milestone checks. Teammate sign-off is pending |
