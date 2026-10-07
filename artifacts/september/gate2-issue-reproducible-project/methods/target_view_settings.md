# Target view settings

Bundle ID: `gate2-issue-reproducible-project`

Version: `gate2-method-freeze-1`

These settings freeze how `loss` is summarized and plotted. The notebook's `describe()` result for `loss` is saved in [`../tables/loss_summary.csv`](../tables/loss_summary.csv).

## Required summary

The notebook summary, in original `loss` units, is:

| Statistic | Value |
| --- | --- |
| count | 188,318 |
| mean | 3,037.337686 |
| standard deviation | 2,904.086186 |
| minimum | 0.67 |
| 25th percentile | 1,204.46 |
| median | 2,115.57 |
| 75th percentile | 3,864.045 |
| maximum | 121,012.25 |

That is the output of `df["loss"].describe()`. It does not include skewness or the 90th, 95th, and 99th percentiles.

## Required views

| View | Setting |
| --- | --- |
| Raw `loss` histogram | `seaborn.histplot`, `bins=50`, `kde=True`, color `steelblue`. Saved as the left panel of [`../visualizations/loss_distribution.jpg`](../visualizations/loss_distribution.jpg). |
| `log1p(loss)` histogram | `seaborn.histplot` of `numpy.log1p(loss)`, `bins=50`, `kde=True`, color `darkorange`. Saved as the right panel of [`../visualizations/loss_distribution.jpg`](../visualizations/loss_distribution.jpg). |
| Raw `loss` boxplot | One boxplot of raw `loss` with outliers shown. The notebook has not drawn this view yet. Gate 3 adds it under this setting. |
| Percentile table | The summary above, in original `loss` units. |

## Axis, clipping, and sampling

- No axis limit is applied. The full observed range stays on the plot.
- No tail is clipped, and no rows are sampled out.
- If a later plot limits an axis for readability, the caption must report the full distribution and the share of rows outside the drawn range.
- `log1p_loss` is a visualization field. Headline business statistics and future MAE stay in original `loss` units.
