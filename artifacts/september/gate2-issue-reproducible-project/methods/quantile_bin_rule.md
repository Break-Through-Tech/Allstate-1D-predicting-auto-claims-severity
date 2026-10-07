# Quantile-bin rule

Bundle ID: `gate2-issue-reproducible-project`

Version: `gate2-method-freeze-1`

The notebook `notebooks/SeptemberMilestone/Gate_2.ipynb` bins `cont2` with `pandas.qcut(..., q=10, duplicates="drop")`. Repeated values left 9 bins, not 10. Support, raw mean `loss`, raw median `loss`, and the interquartile range for those 9 bins are in [`../tables/cont2_quantile_bins.csv`](../tables/cont2_quantile_bins.csv). The box plot of `log1p(loss)` across those bins is in [`../visualizations/cont2_quantile_bins.jpg`](../visualizations/cont2_quantile_bins.jpg). This file freezes that method for all 14 continuous predictors.

## Rule

Each `cont*` field is split with:

```text
pandas.qcut(cont_field, q=10, duplicates="drop")
```

The default request is 10 quantile bins. When repeated values make 10 distinct edges impossible, `duplicates="drop"` keeps the bins that the data can support. The actual bin count is recorded for that field. New edges are not invented to force 10 bins.

## What each bin reports

For every bin of every `cont*` field, the table reports:

- support, the number of rows in the bin;
- raw mean `loss`;
- raw median `loss`;
- interquartile range of raw `loss`.

The plot shows support together with the mean and median `loss` pattern. `log1p(loss)` may be used on a visual axis. The table stays in original `loss` units.

## What this rule does not do

A weak correlation with `loss`, or a strong correlation with another `cont*` field, does not remove a field in September. Bin labels are EDA display fields. They are not September model features.
