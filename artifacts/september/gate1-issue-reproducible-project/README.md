# Gate 1 Artifact Bundle

Bundle ID: `gate1-issue-reproducible-project`

This bundle records the source identity, schema and integrity checks, and a machine-readable profile of all 132 fields. The tables were calculated from `data/allstate_claims_data.csv`. They were not typed in by hand.

Related project task: [GitHub issue 6](https://github.com/Break-Through-Tech/Allstate-1D-predicting-auto-claims-severity/issues/6)

The notebook at `notebooks/SeptemberMilestone/Data_Readiness_&_Source_Verification.ipynb` and the files under `registers/` were left unchanged.

## Files

| Path | Role |
| --- | --- |
| `source_identity.csv` | Source path, byte size, shape, and SHA-256 |
| `data_schema_check.csv` | Header, roles, identifier, duplicates, missingness, continuous range, and target checks |
| `data_field_profiles.csv` | Observed dtype, unique count, missing count, and range or level summary for all 132 fields |
| `manifest.json` | Paths, SHA-256 hashes, source, and code revision |
| `run_receipt.md` | Where the checks ran and whether they succeeded |
| `independent_review.md` | Recomputed check of the source and bundle hashes |
