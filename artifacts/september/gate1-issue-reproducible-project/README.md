# Gate 1 Artifact Bundle

Bundle ID: `gate1-issue-reproducible-project`

Related project task: [GitHub issue 6](https://github.com/Break-Through-Tech/Allstate-1D-predicting-auto-claims-severity/issues/6)

## Overview

This bundle records the source identity, schema and integrity checks, and a machine-readable profile of all 132 fields for Gate 1, Data Readiness. The tables were calculated from `data/allstate_claims_data.csv`. The notebook is at `notebooks/SeptemberMilestone/Data_Readiness_&_Source_Verification.ipynb.`

## Work done

- Confirmed the source file is 70,025,339 bytes, with 188,318 rows and 132 columns, and recorded its SHA-256 digest.
- Confirmed the header order `id`, `cat1` through `cat116`, `cont1` through `cont14`, and `loss`.
- Confirmed the column roles: 1 identifier, 116 categorical predictors, 14 continuous predictors, and 1 regression target.
- Confirmed `id` is present and unique, with 0 duplicate rows and 0 missing cells.
- Confirmed every `cont*` field is numeric and every observed value is on the 0-to-1 scale.
- Confirmed `loss` is numeric, finite, and strictly positive.
- Confirmed every `cat*` value is stored as a category label.
- Wrote an observed dtype, unique count, missing count, and range or level summary for all 132 fields.



## Files


| Path                      | Role                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| `source_identity.csv`     | Source path, byte size, shape, and SHA-256                                                 |
| `data_schema_check.csv`   | Header, roles, identifier, duplicates, missingness, continuous range, and target checks    |
| `data_field_profiles.csv` | Observed dtype, unique count, missing count, and range or level summary for all 132 fields |
| `manifest.json`           | Paths, SHA-256 hashes, source, and code revision                                           |
| `run_receipt.md`          | Where the checks ran and whether they succeeded                                            |
| `independent_review.md`   | Recomputed check of the source and bundle hashes                                           |
| `anomaly_register.csv`    | Gate 1 anomaly record. This reload found no blocking anomaly.                              |


