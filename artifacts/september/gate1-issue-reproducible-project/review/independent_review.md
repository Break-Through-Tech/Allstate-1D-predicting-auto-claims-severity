# Gate 1 independent review

Bundle ID: `gate1-issue-reproducible-project`

This file records a fresh reload of `data/allstate_claims_data.csv` on 2026-10-06. The reload used Python 3.12.4, pandas 3.0.6, and NumPy 2.5.3 at git revision `242e65937dc12efd32a9de4eabc74e21a04e8b5a`. It compared the source file with `source_identity.csv`,  and `data_schema_check.csv`.

A teammate who did not produce these tables still needs to sign the reviewer line below. This file does not claim that sign-off has happened.

## Recomputed checks


| Check                                         | Committed table                                                    | Reloaded source                                                    | Match |
| --------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ----- |
| Byte size                                     | 70,025,339                                                         | 70,025,339                                                         | Yes   |
| SHA-256                                       | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03` | `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03` | Yes   |
| Rows                                          | 188,318                                                            | 188,318                                                            | Yes   |
| Columns                                       | 132                                                                | 132                                                                | Yes   |
| Header order                                  | `id`, `cat1`–`cat116`, `cont1`–`cont14`, `loss`                    | Same order                                                         | Yes   |
| Identifier count                              | 1                                                                  | 1                                                                  | Yes   |
| Categorical count                             | 116                                                                | 116                                                                | Yes   |
| Continuous count                              | 14                                                                 | 14                                                                 | Yes   |
| Target count                                  | 1                                                                  | 1                                                                  | Yes   |
| Missing `id` values                           | 0                                                                  | 0                                                                  | Yes   |
| Unique `id` values                            | 188,318                                                            | 188,318                                                            | Yes   |
| Exact duplicate rows                          | 0                                                                  | 0                                                                  | Yes   |
| Missing cells                                 | 0                                                                  | 0                                                                  | Yes   |
| `cont*` numeric and on the 0-to-1 scale       | Passed                                                             | Passed                                                             | Yes   |
| `loss` numeric, finite, and strictly positive | Passed                                                             | Passed                                                             | Yes   |
| `cat*` labels not numeric                     | Passed                                                             | Passed                                                             | Yes   |


`data_schema_check.csv` has 18 checks and every `passed` value is `True`. The three committed CSV hashes match `manifest.json`.

## Reviewer sign-off

- Reviewer: pending
- Date: pending
- Result: pending a teammate who did not produce the tables

