# September handoff carried into October

September bundle ID: `gate4-issue-reproducible-project`

Folder: [`../../../september/gate4-september-milestone-reproducible-project/`](../../../september/gate4-september-milestone-reproducible-project/)

This handoff is not approved. The September teammate sign-off is still blank in [`../../../september/gate4-september-milestone-reproducible-project/review/independent_review.md`](../../../september/gate4-september-milestone-reproducible-project/review/independent_review.md).

## What October used from that package

- Source identity, copied to [`../manifests/source_identity.csv`](../manifests/source_identity.csv). SHA-256 `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03`.
- Anomaly register, copied to [`../registers/anomaly_register.csv`](../registers/anomaly_register.csv). Row `GATE1-000` records 0 blocking anomalies and 0 removed rows.
- Recommendation register: [`../../../september/gate4-september-milestone-reproducible-project/handoff/october_recommendation_register.md`](../../../september/gate4-september-milestone-reproducible-project/handoff/october_recommendation_register.md).

## Recommendation decisions

| Item | October decision |
| --- | --- |
| REC-002, research model types for a paid-amount estimate | Adopted as the random forest and XGBoost comparison in [`../experiments/experiment_register.csv`](../experiments/experiment_register.csv). This package does not name a winner. |
| REC-001, decide whether outlier points need different handling | Deferred. No rows were removed. |

The modeling contract is [`../modeling-contract.md`](../modeling-contract.md).
