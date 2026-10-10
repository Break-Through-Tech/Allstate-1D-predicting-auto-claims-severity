# Gate 3 recalculation

Bundle ID: `gate3-issue-reproducible-project`

This file records a fresh read of `data/allstate_claims_data.csv` on 2026-10-10. The tables and figures in this bundle were calculated from that file. A teammate who did not author `notebooks/SeptemberMilestone/Gate 3.ipynb` has not signed this review yet.

## Checks that matched the milestone values

Rounding is to the published display precision.

| Check | Result |
| --- | --- |
| Rows | 188,318 |
| Columns | 132 |
| Mean `loss` | 3,037.34 |
| Median `loss` | 2,115.57 |
| 95th percentile of `loss` | 8,508.54 |
| Maximum `loss` | 121,012.25 |
| Skewness of `loss` | 3.795 |
| Categorical fields with 2 levels | 72 |
| Categorical fields with at most 4 levels | 88 |
| `cat116` levels | 326 |
| `cat110` levels | 131 |
| `cat109` levels | 84 |
| Pearson `cont2` with `loss` | 0.142 |
| Pearson `cont7` with `loss` | 0.120 |
| Pearson `cont3` with `loss` | 0.111 |
| Pearson `cont11` with `cont12` | 0.994 |
| Pearson `cont1` with `cont9` | 0.930 |
| Pearson `cont6` with `cont10` | 0.883 |

Spearman values in `findings_tables/continuous_target_correlation.csv` and `findings_tables/continuous_feature_pairs.csv` are Pearson correlations of ranks. That is the Spearman coefficient. This environment did not have SciPy installed.

Quantile bins use `pandas.qcut(..., q=10, duplicates="drop")`. `cont2` has 9 bins and `cont5` has 8. The other continuous fields have 10.

## Not signed yet

- Reviewer: pending
- Date of teammate sign-off: pending
- Disagreements: pending

Gate 2 method approval is still pending in `artifacts/september/gate2-issue-reproducible-project/review/team_approval.md`. This recalculation does not replace that sign-off, and it does not close Gate 3.
