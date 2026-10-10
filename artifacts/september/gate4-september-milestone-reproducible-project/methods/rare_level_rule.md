# Rare-level rule

Bundle ID: `gate2-issue-reproducible-project`

Version: `gate2-method-freeze-1`

The notebook `notebooks/SeptemberMilestone/Gate_2.ipynb` uses `threshold = 0.01` on `cat112`. This file freezes that choice. `cat112` has 51 observed levels, and 30 of them are below 1 percent of rows. Those shares are in [`../tables/cat112_level_shares.csv`](../tables/cat112_level_shares.csv). The grouped count plot and `log1p(loss)` box plot are in [`../visualizations/cat112_distribution.jpg`](../visualizations/cat112_distribution.jpg).

## Rule

A categorical level is rare when its share of the 188,318 rows is below 1 percent.

The threshold is `0.01`. Support is the number of rows with that level. Share is support divided by 188,318.

## Why this threshold

High-cardinality fields such as `cat116` have too many labels for one plot. A 1 percent display cutoff keeps the common levels readable and puts the sparse tail in a separate summary.

## How to apply it

- Count rare levels on the original labels.
- Level-to-target tables keep every original level and report its support, raw mean `loss`, raw median `loss`, and interquartile range.
- A plotting copy may replace levels below 1 percent with the display label `Other`, as the notebook does for `cat112`.
- The source rows stay unchanged. Rare levels are not deleted.
- Alphabetical or integer codes are not treated as an order, and they are not converted to integers before an association is calculated.
- Low-cardinality plots may use a box, violin, or point plot of `log1p(loss)` together with a raw-unit table.
- High-cardinality views use an ordered point plot or table for levels at or above the threshold, and a separate summary of the rare tail. A plot does not show hundreds of labels.
