# September report

This report describes the labeled auto insurance claims file used for September. It explains what a row is, what `loss` looks like, what the predictors show, what October still has to test, and the limits on what this evidence can support. It does not choose a model, set a reserve for one claim, or treat a chart as a score.

The source is `data/allstate_claims_data.csv`. Identity, schema, and the tables below live in this Gate 4 folder.

## 1. What does one row and each field family represent?

One row of the dataset represents an anonymized auto-insurance claim record. The dataset includes 188,318 rows and 132 columns. The roles are fixed in `methods/analysis_contract.md` and listed field by field in `methods/data_dictionary.csv`.

**Associated Fields Include:**

- `id` identifies the claim. Every `id` is unique. It is an identifier, and September does not use it as a predictor.

- `cat1` through `cat116` fields are categorical predictors. Each value is a label. The dictionary records them as text. The source does not say what any of these 116 fields means in the business.
- `cont1` through `cont14` fields 7are continuous predictors. Every observed value sits on a 0-to-1 scale. Their business meanings are also unknown.
- `loss` is the target. It is the claim's total paid amount. Summaries in this report stay in those original units.

## 2. What does the target represent and why does it's distribution matter?

`loss` is the total auto claim ammount paid. October will try to predict that same amount. The project judges predictions with mean absolute error: the average size of the miss, in original `loss` units.

The shape of `loss` is in `eda/target/target_summary.csv`. Across 188,318 claims `eda/target/target_loss_views.jpg`:


| Statistic       | Paid amount |
| --------------- | ----------- |
| Minimum         | 0.67        |
| 25th percentile | 1,204.46    |
| Median          | 2,115.57    |
| Mean            | 3,037.34    |
| 75th percentile | 3,864.05    |
| 95th percentile | 8,508.54    |
| 99th percentile | 13,981.20   |
| Maximum         | 121,012.25  |
| Skewness        | 3.795       |


`eda/target/target_loss_views.jpg` shows three views of the same claims. The raw histogram shows how large the payments are, including the long right tail. The `log1p(loss)` histogram squeezes that tail so the body of the distribution is easier to see. The raw boxplot keeps the extreme payments visible as points.  The view settings are in `methods/target_view_settings.md`.

## 3. The most important data-quality findings

The delivered file did not need row repairs before exploratory analysis.

`source/source_identity.csv` records the file at 70,025,339 bytes, with 188,318 rows and 132 columns. `source/data_schema_check.csv` records 18 checks, and every check passed. `source/data_quality.csv` records the same shape in roles: 1 identifier, 116 categorical fields, 14 continuous fields, and 1 target. There are 188,318 unique ids, 0 duplicate ids, 0 duplicate rows, 0 missing cells, 0 non-positive `loss` values, and 0 infinite numeric values.

`registers/anomaly_register.csv` records this as GATE1-000. No blocking source, schema, or integrity anomaly was found. No rows were removed or corrected. All 188,318 rows stay in the source.



## 4. Categorical cardinality and support patterns

All 116 `cat*` fields are inventoried in `eda/categorical/categorical_cardinality.csv`. Together they have 1,139 levels. The mix is uneven. 72 fields have 2 levels, and 88 have at most 4. A few fields are much wider: `cat116` has 326 levels, `cat110` has 131, and `cat109` has 84.

Support is the number of claims with a given level. Share is that count divided by 188,318, the number of claims in the file.

`eda/categorical/low_support_levels.csv` lists 227 levels with support below 10. The smallest is a single claim. `eda/categorical/dominant_levels.csv` lists 64 levels that each cover at least 90 percent of claims. `cat70` level A, for example, appears on 188,295 of 188,318 claims. `eda/categorical/categorical_support.jpg` and `eda/categorical/high_cardinality_review.jpg` show that spread. Rare levels were kept.

`eda/categorical/categorical_level_target.csv` reports, for every original level, its support, its share, the raw mean `loss`, the raw median `loss`, and the interquartile range. A difference in median `loss` across levels is an association in this file. The labels are anonymous, so that difference is not a named business cause.

`methods/rare_level_rule.md` freezes a 1 percent display rule. A level is rare for a plot when its share of the 188,318 claims is below 0.01. A plotting copy may group those levels as Other so the common labels stay readable. The source rows stay unchanged. Other is a display label. It does not delete claims.

## 5. Continuous distributions, target relationships, and redundancy

The 14 `cont*` fields are summarized in three separate ways: what they look like, how they move with `loss`, and how they move with each other.

**Distributions:**

`eda/continuous/continuous_summary.csv` gives the count, mean, spread, and range of each field. Every observed value is on the 0-to-1 scale. `cont10` reaches 0 and `cont7` reaches 1. The histograms are in `eda/continuous/continuous_histograms.jpg`, and the boxplots are in `eda/continuous/continuous_boxplots.jpg`.

**Relationship with the target:**

`eda/continuous/continuous_target_correlation.csv` compares each field with raw `loss`. The strongest straight-line associations are modest: Pearson correlation is about 0.142 for `cont2`, 0.120 for `cont7`, and 0.111 for `cont3`. Spearman correlations for those same fields are weaker, about 0.080, 0.055, and 0.068. No continuous field has a strong straight-line relationship with raw `loss`. That result describes one field at a time. It does not measure how useful the field would be inside a later model, and it is not a reason to drop the field.

**Binned views:**

 `methods/quantile_bin_rule.md` splits each `cont*` field with a 10-bin quantile cut, dropping duplicate edges when repeated values cannot support 10 bins. The actual bin count is recorded. `cont2` has 9 bins and `cont5` has 8. The other 12 fields have 10. The table is `eda/continuous/continuous_quantile_bins.csv`, and the figure is `eda/continuous/continuous_binned_target.jpg`.

Those bins show patterns a single correlation hides. For `cont2`, mean `loss` moves from about 2,120 in the lowest bin to about 3,481 in the highest, while the median moves from about 1,740 to about 2,123. For `cont14`, the median is higher in the lowest bin (about 2,477) than in the highest (about 2,122). The shape is not the same for every field. Bin labels are a way to look at this file. They are not September model features.

**Redundancy:**

 Some continuous fields move almost together. `eda/continuous/continuous_feature_pairs.csv` and `eda/continuous/continuous_correlation_heatmap.jpg` record the strongest pairs. Pearson correlation is about 0.994 for `cont11` and `cont12`, 0.930 for `cont1` and `cont9`, and 0.883 for `cont6` and `cont10`. 

## 6. What remains unknown because the predictors are anonymous

`methods/analysis_contract.md` keeps the meaning of every `cat*` and `cont*` field unknown. The source file does not name them. Examples of possible insurance fields in the project overview are examples of field types. They are not a mapping onto these columns.

## 7. What was deferred to October

September prepared the source, the field roles, and the descriptive evidence. We have not yet fit a model, chosen a split, or scored a held-out set. Two future tasks are documented in `handoff/october_recommendation_register.md`. They are not completed work.

- REC-001. Decide whether to look further at the `cont*` features whose boxplots show outlier points, and whether any of those fields need extra handling. The plots are in `eda/continuous/continuous_boxplots.jpg`. No rows were removed.
- REC-002. Research model types that are typically used to estimate a loss amount. `methods/analysis_contract.md` sets the target as `loss` and the score as MAE. This research does not pick a model.



## 8. Important limitations

**The field meanings are anonymous:**

The data source does not say what any `cat*` or `cont*` field represents. `methods/analysis_contract.md` keeps those meanings unknown. A code such as level A, or a value on the 0-to-1 scale, can be counted and compared with `loss`. It cannot be translated into a coverage, a vehicle trait, or any other business name.