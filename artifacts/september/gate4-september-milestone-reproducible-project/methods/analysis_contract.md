# Plain-language analysis contract

Bundle ID: `gate2-issue-reproducible-project`

Version: `gate2-method-freeze-1`

Source: `data/allstate_claims_data.csv`

This contract freezes what September analysis is trying to answer. It is a project decision record.

## Aim

The project aims to estimate a claim's final paid amount early enough to support reserve planning and a better understanding of factors associated with higher claim severity.

## Unit and target

One row is one anonymized auto-insurance claim. That row is the unit of analysis.

`loss` is the regression target. It is the claim's total paid amount. Business summaries and future evaluation stay in the original `loss` units.

## Success metric

The project success metric is mean absolute error (MAE). Absolute error is the size of the miss: the positive distance between a predicted paid amount and the actual paid amount. MAE is the average of those distances. A smaller MAE means the predictions are closer to the paid amounts, in the original `loss` units.

The notebook calculated one descriptive baseline by predicting the median `loss` for every row. That full-file MAE is 1,809.0487864675708, saved in [`../tables/baseline_mae.csv`](../tables/baseline_mae.csv). It is not held-out model performance. October baselines are fitted on training rows only.

## What the file shows about payments

The project overview says closed claims without payment are excluded. This contract only requires the delivered file to contain positive `loss` values. It does not infer why any individual value is present.

## Anonymous fields

The meanings of individual `cat*` and `cont*` fields are `unknown`. Examples in the project overview are possible field types. They are not a mapping onto these columns.

## Non-uses

September EDA does not establish causation, determine an individual reserve, prove production readiness, or authorize an automated claims decision.
