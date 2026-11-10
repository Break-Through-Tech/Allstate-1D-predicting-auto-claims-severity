# Allstate Nov Milestones

This guide is meant to be used as a suggestion for the November milestone for
the Allstate project. November is the last month. The work is to finish the
recorded comparison, score the held-out test claims once, write down what those
scores can support, and prepare and practice the final presentation.

**November Milestone:**

Evaluation and Presentation -> Finalize the recorded models, score the held-out
comparison, document the results, and prepare and practice the final presentation

The starting package is the October handoff:
[`artifacts/october/gate4-october-milestone-reproducible-project/handoff/november_handoff.md`](../../../artifacts/october/gate4-october-milestone-reproducible-project/handoff/november_handoff.md).
The plain-language October account is
[`october_report.md`](../../../artifacts/october/gate4-october-milestone-reproducible-project/handoff/october_report.md).

## Where this month starts

October already did this work. November does not redo it.

- The source is [`data/allstate_claims_data.csv`](../../../data/allstate_claims_data.csv):
  70,025,339 bytes, 188,318 rows, 132 columns, SHA-256
  `74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03`.
- The split is frozen in
  [`gate1_partition_manifest.csv`](../../../artifacts/october/gate4-october-milestone-reproducible-project/manifests/gate1_partition_manifest.csv),
  SHA-256 `0e97b61a8ad550387f2c7bcbe2b4130064e790337e88d1a5251399ce91830418`.
  The seed is `random_state=1`. Train has 131,822 claims. Validation has 28,248.
  Test has 28,248.
- Preprocessing is
  [`training_preprocessor.py`](../../../artifacts/october/gate4-october-milestone-reproducible-project/preprocessing/training_preprocessor.py):
  training-median fill for `cont*`, training-mode fill and one-hot encoding for
  `cat*` with `handle_unknown='ignore'`. `id` and `loss` stay out. All 130
  anonymous fields stay in.
- Four approaches already have validation scores in
  [`validation_mae.csv`](../../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/validation_mae.csv):

  | Approach | Validation average miss |
  | --- | ---: |
  | Training mean ($3,033.69) | $1,978.40 |
  | Training median ($2,113.76) | $1,827.31 |
  | Random forest | $1,291.59 |
  | XGBoost | $1,171.72 |

- October did not name a model. XGBoost is closer on the full validation set.
  The forest is closer on the 285 validation claims at or above the training
  99th percentile of `loss` (about $14,017.41). That split is in
  [`high_loss_tail.csv`](../../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/high_loss_tail.csv).
- The test claims have no score yet.

These items are still open. November records them. It does not close them by
changing a number.

- September Gate 4 sign-off is still blank.
- October Gate 4 sign-off is still unsigned in
  [`independent_review.md`](../../../artifacts/october/gate4-october-milestone-reproducible-project/review/independent_review.md).
- The Challenge Advisor has not said which anonymous fields are known when a
  claim is first filed.
- The optional `cont11` / `cont12` drop was not run.
- September recommendation REC-001, extra handling for continuous outlier
  points without deleting rows, stays deferred.

## Gate Handoffs

The Allstate project has 4 [**Gates**](../september-execution/Glossary.md#gate).

1. **Gate 1:** Final evaluation protocol frozen
1. **Gate 2:** Held-out comparison scored
1. **Gate 3:** Results documented
1. **Gate 4:** Presentation ready

In practice, each **Gate Handoff** should work as follows:

1. **Evidence owner prepares:** every checklist item links to an exact committed
   [Artifact](../september-execution/Glossary.md#artifacts) or verified
   [Artifact Bundle ID](../september-execution/Glossary.md#artifact-bundle).
1. **Independent teammate verifies:** someone who did not produce the critical
   Artifact reproduces or independently checks the key result.
1. **Team Readiness Review:** the owner demonstrates the evidence; the team
   records limitations, anomalies, open disagreements, and dissent.
1. **Board updates:** dependent items become ready only after the gate decision is
   recorded.

Use the task statuses in [`docs/Task-Progression-Workflow.md`](../../Task-Progression-Workflow.md):
In progress, Ready for Review, In Review, Ready for Documentation, Done.
Notebooks for this month go in `notebooks/NovemberMilestones/`.

### Artifacts

Keep the working notebook and the slide deck in the team's shared Google Drive
so every fellow, the coach, and the Challenge Advisor can open them. Commit the
reproducible notebook, the test-score tables, the November report, the
reproduction steps, and the practice notes to the repository. Put the November
evidence package in
`artifacts/november/gate4-november-milestone-reproducible-project/`.

### November Scope Protections

- Score only the approaches named in Gate 1. The required four are the training
  mean, the training median, the recorded random forest, and the recorded
  XGBoost.
- Fit preprocessing and models on the 131,822 training claims only. Leave the
  28,248 validation claims out of that fit. Leave the 28,248 test claims out of
  that fit.
- Use the frozen manifest. Keep `random_state=1`. A test score that looks high
  is not a reason to draw a new split or pick a new seed.
- Report mean absolute error in original `loss` dollars, from
  `sklearn.metrics.mean_absolute_error`, on the named partition. A `log1p(loss)`
  figure is a plot. It is not the project score.
- Run the test scoring procedure once, after it is written down. A bug fix may
  be rerun. A hyperparameter, a feature list, or a seed may not be changed
  because the test miss was large.
- A lower test score does not name a winner. Report the four test scores beside
  one another. Keep the October validation table as the October comparison.
- The optional `cont11` / `cont12` experiment, if the team runs it, finishes on
  the validation claims before any test score is computed. Choose the dropped
  field from the training claims only. Keep the field unless the new validation
  MAE is lower than $1,171.72. If the field is dropped, add that approach as an
  extra row. Leave the original four rows in the table.
- Any importance or coefficient check uses training claims only. The result is
  a rank of anonymous columns on this file. It is optional. It does not change
  the four scored approaches, and it does not give a column a business name.
- Keep every claim, including the largest payments. A suspected bad value goes
  in the anomaly register. Rows stay in the file while that review is open.
- State that September already explored all 188,318 claims before the split.
  The test score is a held-out slice of a file the team has already seen. It is
  not a later time period and it is not a new book of business.
- Until the Challenge Advisor confirms which fields exist at first filing, call
  the result a retrospective check. Do not call either model an up-front
  estimator, a reserve for one claim, a cause, or a production system.
- The examples in the project overview are examples of field types. They are
  not a dictionary for `cat*` and `cont*`.

## Gate 1 - Final evaluation protocol frozen

Gate 1 is done when the scoring procedure is written down and a teammate has
confirmed that the test claims have not been used. Gate 1 does not contain a
test MAE.

### Locked October evidence

- [ ] Confirm the source hash, the manifest hash, the row counts, and the
  package versions in the October handoff: Python 3.12, pandas 3.0.6, NumPy
  2.5.3, scikit-learn 1.9.1, XGBoost 3.4.1.
- [ ] Confirm the field list in
  [`field_roles.csv`](../../../artifacts/october/gate4-october-milestone-reproducible-project/field_roles.csv):
  `cat1` through `cat116` and `cont1` through `cont14` are inputs. `id` and
  `loss` are not.
- [ ] Copy the recorded settings into the November protocol, unchanged:
  - random forest: 100 trees, `max_depth=12`, `min_samples_leaf=20`,
    `random_state=1`;
  - XGBoost: `objective='reg:absoluteerror'`, 200 trees, `max_depth=6`,
    learning rate 0.1, `random_state=1`.
- [ ] Confirm the training constants that will be predicted for every test
  claim: training mean $3,033.69 and training median $2,113.76. Both come from
  the training payments only.
- [ ] Confirm that the October validation table stays as historical evidence.
  November does not edit those four validation scores to match a new run.

### Optional feature experiment, before any test score

- [ ] Decide, in writing, whether to run the deferred `cont11` / `cont12` test.
  The default recorded in October is that it was not run.
- [ ] If the team runs it, choose the removed field from the 131,822 training
  claims only. Use the same preprocessor, the same 5 training folds,
  `random_state=1`, and one validation score on the same 28,248 validation
  claims.
- [ ] Keep the field unless that validation MAE is lower than $1,171.72. Record
  the chosen field, the validation MAE, and the keep-or-drop decision in the
  experiment register before Gate 2 starts.
- [ ] Leave REC-001 deferred unless the team writes a separate training-only
  decision in this same gate. That decision still does not delete rows.

### Protocol record

- [ ] Write the test procedure in the November notebook before the test `loss`
  values are used in a score. The procedure names the manifest, the four
  approaches, the training-only fit, the metric, and the output table path.
- [ ] State that validation rows are not added to the training fit for the test
  score. October compared models on validation. November does not refit on
  train plus validation.
- [ ] State the stopping rule for this month: one clean test run of the frozen
  procedure. A later change to settings, features, or the seed reopens Gate 1.
- [ ] Record how unseen category levels will be handled on the test claims:
  `handle_unknown='ignore'`, fit on training claims only, same as validation.
- [ ] Have someone other than the protocol author confirm:
  - the manifest still has 131,822 / 28,248 / 28,248 and no shared `id`;
  - the notebook does not fit on test rows;
  - the notebook does not read a test score to choose a setting;
  - the optional feature decision, if any, is already written down.

## Gate 2 - Held-out comparison scored

Gate 2 is the one time the team computes the test scores. The output is a
table. The output is not a selected model.

### Test scores

- [ ] Score the training mean, the training median, the recorded random forest,
  and the recorded XGBoost on the 28,248 test claims.
- [ ] Fit each learned step on the training claims only, then apply it to the
  test claims.
- [ ] Save one machine-readable table with, for each approach:
  - the approach name;
  - the partition name and the claim count;
  - the test MAE in original dollars;
  - the training constant or the recorded settings;
  - the evaluation code.
- [ ] If Gate 1 dropped one field from the `cont11` / `cont12` pair, add that
  approach as its own row. Keep the original four rows.
- [ ] Keep the October validation MAEs in their own file. Put the test MAEs in
  a new file. A reader should be able to see which number came from which
  partition.
- [ ] Generate the table from the notebook. Do not type the scores into the
  report by hand and leave the notebook unsaved.

### Large-claim check

- [ ] Use the same cut October used: the training 99th percentile of `loss`,
  about $14,017.41. Count how many of the 28,248 test claims fall on that side
  of the cut, and how many remain.
- [ ] Report test MAE for each scored approach on that large-claim slice and on
  the remainder.
- [ ] Treat the slice as a description of where the misses sit. The count will
  be small. It is not a new rule for picking a model.

### What the comparison may say

- [ ] Say which approaches have a lower test miss than the training-mean
  constant and which have a lower test miss than the training-median constant,
  on these same test claims.
- [ ] Report the gap between the forest and XGBoost in dollars. State whether
  that gap is large or small next to the scores, the same way October compared
  the validation gap of about $119.87 with the forest score.
- [ ] If the test ranking and the validation ranking disagree, write that
  disagreement down. Do not resolve it by dropping a row or by refitting.
- [ ] Leave the decision as it stood in October unless the team writes a new
  reason that does not depend on shopping the test score. Both models beat
  both constants on validation, and the two validation scores were close.
  October did not name a model.

### Independent reproduction

- [ ] Have someone other than the scoring author rerun the procedure from the
  committed notebook, the committed manifest, and the source file.
- [ ] The rerun should match:
  - the test claim count, 28,248;
  - the training constants;
  - each test MAE at the recorded precision;
  - the large-claim count and the two slice scores for at least one approach.
- [ ] Record the git revision, the source hash, the manifest hash, the
  dependency versions, the seed, and who ran the check.
- [ ] If a correction changes a test MAE, record the reason, the old value, the
  new value, and a second independent check. Do not silent-edit the table.

## Gate 3 - Results documented

Gate 3 turns the Gate 2 table into the project record. The report should be
readable without the notebook.

### November report

- [ ] Write a plain-language November report that covers:
  - what one row is and what `loss` is;
  - the frozen split and which claims were scored in October versus November;
  - the two constants and why the median is included;
  - the two recorded models, in plain language, including the settings that
    were frozen;
  - the validation scores and the test scores, in separate tables;
  - the large-claim check on validation and the same check on test;
  - the decision about naming a model;
  - the optional feature experiment, including a clear "not run" if it was
    skipped;
  - what remains unknown because the fields are anonymous.
- [ ] Put the exact figures in the committed tables. The report may round the
  way the October report rounds, and it should point at the unrounded file.
- [ ] Update the README so a new reader can find the September bundle, the
  October bundle, and the November test scores. The README's "Next Steps"
  section should match what November actually did.

### Optional key predictors

This block is optional. Skip it if the test report and the presentation are
not yet solid. Completing it is not required to finish the month.

- [ ] If the team computes importances or coefficients, fit that check on the
  training claims only.
- [ ] Label every named column as an anonymous predictor. `cat*` and `cont*`
  stay codes. A high rank is not a coverage, a vehicle trait, or a cause.
- [ ] Keep the four scored approaches unchanged by this check.
- [ ] Say what the rank does not support: a reserve for one claim, a business
  meaning, or a change to the test table.

### Limitations and open questions

- [ ] The report states these limits in its own sentences:
  - the scores are a retrospective check on the supplied file;
  - September had already looked at all 188,318 claims before the split;
  - the field names do not say what is known at first filing;
  - a score does not set a reserve, show a cause, or show production readiness;
  - high-loss claims stayed in the data;
  - no anonymous field was given a business meaning.
- [ ] Carry forward the advisor question: which anonymous fields are known when
  a claim is first filed? Name an owner for asking it, or record that no owner
  is named.
- [ ] Record the status of the September and October teammate sign-offs. A
  November report can describe committed evidence while those lines are still
  blank. It should not say those gates are closed.

## Gate 4 - Presentation ready

Gate 4 is the talk and a real practice of the talk. Slides that have not been
spoken out loud do not finish this gate.

**Completion rule:** If the test protocol, the no-winner rule, or a blocking
leakage question is still unresolved at the end of November, keep Gate 4 open
and record the blocker. Do not pick a model, drop a field, or rewrite a score
only to have a cleaner ending.

### What the presentation has to show

- [ ] One row is one anonymized claim. `loss` is the paid amount in dollars.
  The project score is the average dollar miss.
- [ ] The split: 131,822 train, 28,248 validation, 28,248 test, seed
  `random_state=1`. Say what each partition was allowed to do.
- [ ] The two constants, fit on training payments only, and the two models with
  the settings from Gate 1.
- [ ] The October validation table and the November test table, labeled as
  different checks.
- [ ] The large-claim pattern: on validation, XGBoost was closer overall and the
  forest was closer on the 285 largest claims. Add the test version of that
  check once Gate 2 has the counts.
- [ ] The decision not to name a winner from the test score.
- [ ] The limits: anonymous fields, unconfirmed first-filing timing, and the
  fact that September had already seen the full file.
- [ ] Every number on a slide traces to a committed table. A slide does not
  introduce a metric, a model, or a business meaning that the report does not
  support.

### Practice

- [ ] Assign sections so each fellow presents part of the story. The October
  work was split across the modeling plan, the baselines, and the comparison.
  The practice should let each person explain the piece they owned and the
  final test result.
- [ ] Run the full presentation out loud at least once before the final
  delivery. Record the runtime.
- [ ] In that practice, each speaker can answer these questions without the
  notebook:
  - why MAE, in original dollars;
  - why the median constant is next to the required mean constant;
  - why the test claims were held out, and why their score does not pick a
    winner;
  - why the result is not yet an estimate at first notice of a claim;
  - what the team would not claim in front of the Challenge Advisor.
- [ ] After the practice, fix any sentence that is stronger than the tables.
  Save the practice notes with the date, who spoke, what ran long, and what
  was changed.
- [ ] Hold a short question practice. Use questions a coach or the Challenge
  Advisor can actually ask from this file: the $119.87 validation gap, the
  285 large validation claims, the unsigned reviews, and the unanswered
  timing question.

### Team review

- [ ] Confirm the final November bundle contains:
  - the frozen protocol;
  - the November notebook;
  - the test MAE table;
  - the test large-claim table;
  - the November report;
  - reproduction steps;
  - the independent-review record;
  - the presentation and the practice notes.
- [ ] Present the handoff to the full team. Record approvals, dissent,
  unresolved risks, and anything left undone.
- [ ] In the team retrospective, record:
  - one practice to keep;
  - one practice to change;
  - one experiment that stayed deferred, and why;
  - one lesson about stating only what the claims file can support.
