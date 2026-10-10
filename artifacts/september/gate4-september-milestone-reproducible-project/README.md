# Gate 4 Artifact Bundle

Bundle ID: `gate4-issue-reproducible-project`

Related project task: [GitHub issue 12](https://github.com/Break-Through-Tech/Allstate-1D-predicting-auto-claims-severity/issues/12)

## Overview

This folder is the September evidence package. A reviewer can check the source profile, the frozen methods, the exploratory tables and figures, and the findings register without leaving this directory. The copies came from the Gate 1, Gate 2, and Gate 3 bundles at git revision `6f9a709dd40cbae3e6a3e831b2acbe5c5e52b515`. The source file is `data/allstate_claims_data.csv`, SHA-256 `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03`.

Headline `loss` values in original units are mean 3,037.34, median 2,115.57, 95th percentile 8,508.54, maximum 121,012.25, and skewness 3.795. Rare levels use a 1 percent display threshold. Continuous bins use 10-bin `qcut` with `duplicates="drop"`. No random seed was used. These tables are deterministic.

This assembly does not close Gate 4. A teammate who did not author the notebooks still has to rerun the locked source and sign [`review/independent_review.md`](review/independent_review.md). The September report and October handoff are not in this folder yet.

## Work done

- Copied the Gate 1 source identity, schema check, 132-field profile, and anomaly register.
- Copied the Gate 3 data-quality counts into `source/`.
- Copied the Gate 2 analysis contract, data dictionary, rare-level rule, quantile-bin rule, target-view settings, and findings-register format.
- Copied the Gate 2 tables and figures that show those rules applied, into `methods/evidence/`.
- Copied the Gate 3 target, categorical, and continuous tables and figures.
- Copied the findings register.
- Wrote a run receipt, reproduction steps, and a manifest of every file in this folder except the manifest itself.

## Files

| Path | Role |
| --- | --- |
| [`source/source_identity.csv`](source/source_identity.csv) | Source path, byte size, shape, and SHA-256 |
| [`source/data_schema_check.csv`](source/data_schema_check.csv) | Header, roles, identifier, duplicates, missingness, range, and target checks |
| [`source/data_field_profiles.csv`](source/data_field_profiles.csv) | Observed dtype, unique count, missing count, and range or level summary for 132 fields |
| [`source/data_quality.csv`](source/data_quality.csv) | Gate 3 row, column, role, duplicate, and missing counts |
| [`methods/analysis_contract.md`](methods/analysis_contract.md) | Aim, unit, target, MAE, anonymous fields, and non-uses |
| [`methods/data_dictionary.csv`](methods/data_dictionary.csv) | Data type, missing count, and unique count for 132 fields |
| [`methods/rare_level_rule.md`](methods/rare_level_rule.md) | 1 percent display threshold |
| [`methods/quantile_bin_rule.md`](methods/quantile_bin_rule.md) | 10-bin `qcut` rule |
| [`methods/target_view_settings.md`](methods/target_view_settings.md) | Histogram settings and the `loss` summary |
| [`methods/findings_register_format.md`](methods/findings_register_format.md) | Columns and evidence-status terms |
| [`methods/evidence/`](methods/evidence) | Gate 2 tables and figures for `loss`, `cat112`, and `cont2` |
| [`eda/target/`](eda/target) | Gate 3 `loss` summary and distribution figure |
| [`eda/categorical/`](eda/categorical) | Cardinality, level-to-target tables, and category figures |
| [`eda/continuous/`](eda/continuous) | Continuous summaries, bins, correlations, and figures |
| [`registers/anomaly_register.csv`](registers/anomaly_register.csv) | Gate 1 anomaly record. No blocking anomaly was found. |
| [`registers/findings_register.csv`](registers/findings_register.csv) | Seven Gate 3 findings |
| [`review/run_receipt.md`](review/run_receipt.md) | Where this copy was assembled and what is still open |
| [`review/reproduction.md`](review/reproduction.md) | How a teammate reruns the notebooks and checks this folder |
| [`review/independent_review.md`](review/independent_review.md) | Teammate sign-off. Pending. |


The copied method notes still contain links that point at the Gate 2 bundle. The same tables and figures are in `methods/evidence/` inside this folder.
