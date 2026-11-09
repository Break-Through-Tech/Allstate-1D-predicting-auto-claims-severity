# Reliability

The forest 5-fold MAE is $1,282.83 and its validation MAE is $1,291.59. The validation score is about $8.76 higher. The XGBoost 5-fold MAE is $1,162.96 and its validation MAE is $1,171.72. The validation score is about $8.76 higher. Both gaps are small next to the MAE.

The recorded validation MAEs for the mean constant, the median constant, the forest, and XGBoost are finite dollar values. A non-finite prediction would have made those scores non-finite. The iteration was not refit, so it has no predictions to check.

Unknown category levels are ignored. The one-hot encoder uses `handle_unknown='ignore'`, fit on the training claims only. The check is the 21 validation levels absent from training, across eight fields, listed in `artifacts/october/gate1-issue-reproducible-project/splits/unseen_validation_levels.csv`. Those levels do not create a new column and do not use validation `loss`.

The two validation MAEs differ by about $119.87. That gap is under 10% of the forest validation MAE, so the two scores are close. The evidence is too weak to prefer one model.
