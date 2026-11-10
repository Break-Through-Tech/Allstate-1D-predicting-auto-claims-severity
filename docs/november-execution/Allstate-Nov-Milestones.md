# Allstate Nov Milestones

This guide is meant to be used as a suggestion for the November milestone for
the Allstate project. The point of the month is a final presentation the team
can give before December 16, 2026. Scoring the held-out test claims and writing
the November report are how the slides get numbers the team can defend.

**November Milestone:**

Evaluation and Presentation -> Make the final slide deck, fill it from the
recorded comparison and the one test score, and practice it before December 16

The starting package is the October handoff:
[`artifacts/october/gate4-october-milestone-reproducible-project/handoff/november_handoff.md`](../../artifacts/october/gate4-october-milestone-reproducible-project/handoff/november_handoff.md).
The plain-language October account is
[`october_report.md`](../../artifacts/october/gate4-october-milestone-reproducible-project/handoff/october_report.md).

**Ready means:** the deck below is written, every number on a slide traces to a
committed table, the team has practiced the full talk out loud, and the Q&A
slide has been rehearsed. That package is finished before December 16, 2026.
December 16 is not the first time the team says the talk.

## Where this month starts

October already did this work. November does not redo it, and the slides do not
replace it.

- The source is [`data/allstate_claims_data.csv`](../../data/allstate_claims_data.csv):
70,025,339 bytes, 188,318 rows, 132 columns, SHA-256
`74037cb248a1064e4d578692a4f4e5d8492ed1b2033daf643496e1b68b14ae03`.
- The split is frozen in
[`gate1_partition_manifest.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/manifests/gate1_partition_manifest.csv),
SHA-256 `0e97b61a8ad550387f2c7bcbe2b4130064e790337e88d1a5251399ce91830418`.
The seed is `random_state=1`. Train has 131,822 claims. Validation has 28,248.
Test has 28,248.
- Preprocessing is
[`training_preprocessor.py`](../../artifacts/october/gate4-october-milestone-reproducible-project/preprocessing/training_preprocessor.py):
training-median fill for `cont*`, training-mode fill and one-hot encoding for
`cat*` with `handle_unknown='ignore'`. `id` and `loss` stay out. All 130
anonymous fields stay in.
- Four approaches already have validation scores in
[`validation_mae.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/validation_mae.csv):
  | Approach | Validation average miss |
  | --- | ---: |
  | Training mean ($3,033.69) | $1,978.40 |
  | Training median ($2,113.76) | $1,827.31 |
  | Random forest | $1,291.59 |
  | XGBoost | $1,171.72 |
- October left the model unnamed. The two validation scores are close, and
the large-claim check points the other way. Gate 1 closes that decision.
The naming rule is the lowest validation MAE. Under that rule the named
model is XGBoost, at $1,171.72. The forest is closer on the 285 validation
claims at or above the training 99th percentile of `loss` (about $14,017.41).
That split is in
[`high_loss_tail.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/high_loss_tail.csv).
It is shown on the winner chart. It is not the naming rule.
- The test claims have no score yet. Gate 2 confirms the named model on those
claims. The results slides leave a blank for that table until then.

These items are still open. The slides record them. They do not close them by
changing a number.

- September Gate 4 sign-off is still blank.
- October Gate 4 sign-off is still unsigned in
[`independent_review.md`](../../artifacts/october/gate4-october-milestone-reproducible-project/review/independent_review.md).
- The Challenge Advisor has not said which anonymous fields are known when a
claim is first filed.
- The optional `cont11` / `cont12` drop was not run.
- September recommendation REC-001, extra handling for continuous outlier
points without deleting rows, stays deferred.

## The slide deck

One shared deck lives in the team's Google Drive so every fellow, the coach,
and the Challenge Advisor can open it. The section order and owners are fixed
below. A section may be more than one slide. The Q&A section is one slide.

| Section | Owner | When it can be drafted |
| --- | --- | --- |
| Presentation hook and introduction | Andre | Now |
| Project overview | Andre | Now. The results preview is filled after Gate 2. |
| Data understanding and data preparation | Matthew | Now, from the September and October packages |
| Modeling and evaluation | Nevaeh | The named model and the winner chart in Gate 1. The test confirmation after Gate 2. |
| Final thoughts | Nevaeh | Skills and acknowledgments now. Future work after the team records what stayed deferred. |
| Audience Q&A | Whole team | After a full draft exists |

The audience includes technical and non-technical stakeholders. Each section
has to make sense to both. Mean absolute error is the average dollar miss. A
slide that needs a notebook to be understood is not done.

### Presentation hook and introduction — Andre

- [ ] Open on the problem in plain language: the final paid amount of a claim
  can take months, and an earlier estimate could help set reserves and show
  what travels with higher claim costs.
- [ ] Say who the team is and what the talk will cover, in the section order
  above.
- [ ] Keep the hook inside what the file supports. The fields are anonymous, and
  the Challenge Advisor has not confirmed which of them exist when a claim is
  first filed. The opening does not call the model an up-front estimator.

### Project overview — Andre

- [ ] Problem statement and potential impact, building on the hook. Impact stays
  a possible use of a closer estimate. It is not a claim that this file already
  set a reserve.
- [ ] Methodology, short enough for one pass: 188,318 claims; a 70/15/15 split
  with `random_state=1`; MAE in original dollars; a training-mean constant and
  a training-median constant; a random forest and XGBoost, fit on the training
  claims only.
- [ ] A preview of the results the later section will show. On validation, both
  models beat both constants. Gate 1 names XGBoost, at $1,171.72, because that
  is the lowest validation MAE. The forest's miss is $1,291.59, and the forest
  is closer on the 285 largest validation claims. The test numbers are added
  after Gate 2, in their own sentence, as a confirmation of the named model.

### Data understanding and data preparation — Matthew

- [ ] Data used: [`data/allstate_claims_data.csv`](../../data/allstate_claims_data.csv).
  One row is one anonymized auto-insurance claim. 188,318 rows and 132 columns:
  `id`, `cat1` through `cat116`, `cont1` through `cont14`, and `loss`. Notable
  characteristics: no missing cells, no duplicate rows, a strictly positive
  right-skewed `loss`, and continuous fields on a 0-to-1 scale. High-loss
  claims stayed in the file.
- [ ] Preprocessing, fit on the 131,822 training claims only: median fill for
  the continuous fields, mode fill and one-hot encoding for the categories,
  unknown levels ignored, continuous fields left unscaled. `id` and `loss` are
  not inputs.
- [ ] A few EDA pictures or tables, not the whole September bundle. Useful
  highlights are the shape of `loss`, the mix of small and very wide category
  fields, and the continuous pairs that move together (`cont11` with `cont12`,
  and the two pairs behind it). Say that those charts were exploration. The 1%
  display rule and the quantile bins were not reused as model features.

### Modeling and evaluation — Nevaeh

- [ ] Models considered: the required training-mean constant, the training-median
  constant beside it, the random forest, and XGBoost. The project overview
  lists GLM and gradient boosting as examples. October tested the forest and
  XGBoost. Record the settings on the slide: forest, 100 trees, `max_depth=12`,
  `min_samples_leaf=20`; XGBoost, `reg:absoluteerror`, 200 trees, `max_depth=6`,
  learning rate 0.1. Both use `random_state=1`.
- [ ] The final-choice slide names XGBoost and shows the Gate 1 winner chart.
  The spoken line is that XGBoost has the lowest validation MAE, about $120
  lower than the forest and about $656 lower than the training median. The
  same slide shows that the forest is closer on the 285 largest validation
  claims. After Gate 2, add whether the test score agrees with that name.
- [ ] Evaluation: MAE in original `loss` dollars, because the project compares
  the average size of the miss. Validation (28,248 claims) is the comparison
  that names the model. Test (28,248 claims) is the November confirmation.
  The two tables stay separate.
- [ ] Results: the winner chart, the validation table, and the test table once
  Gate 2 exists. If the test ranking and the validation ranking disagree, the
  slide says so and keeps the Gate 1 name.

### Final thoughts — Nevaeh

- [ ] Technical and professional skills, written from work this team actually
  did: the September data checks, the October split and baselines, the model
  comparison, and this presentation. Each fellow supplies the skills they can
  point to. The slide does not invent a tool or a role.
- [ ] Future directions that are still open: the first-filing question for the
  Challenge Advisor, the `cont11` / `cont12` drop if it stays unrun, and
  REC-001. A future direction is not a result.
- [ ] Acknowledgments. Thank the Challenge Advisor, Krystal Smuda, Allstate, the
  coach, and the people who reviewed the work. Use only names the team is
  sure of.

### Audience Q&A

- [ ] One simple slide that asks the audience for questions.
- [ ] Leave time for technical and non-technical stakeholders.
- [ ] Practice answers a listener can actually ask from this deck: what MAE
  means in dollars, why the median sits next to the mean, why XGBoost is the
  named model, what the winner chart shows on the large claims, what the team
  does not know about first filing, and what a score does not do for one claim.

## Gate Handoffs

The Allstate project has 4 **[Gates](../coach/september-execution/Glossary.md#gate)**.
The gates are the path to the deck, in this order.

1. **Gate 1:** Story, named model, winner chart, and test protocol frozen
2. **Gate 2:** Held-out comparison scored
3. **Gate 3:** Deck drafted from the tables
4. **Gate 4:** Practiced and presentation-ready before December 16

Use the task statuses in [`docs/Task-Progression-Workflow.md`](../Task-Progression-Workflow.md):
In progress, Ready for Review, In Review, Ready for Documentation, Done.
Notebooks for this month go in `notebooks/NovemberMilestones/`.

### Artifacts

Commit the reproducible notebook, the test-score tables, the November report,  
the reproduction steps, and the practice notes to the repository. Put the  
November evidence package in  
`artifacts/november/gate4-november-milestone-reproducible-project/`. The slide  
file stays in the shared Drive. The repository gets a short note with the deck  
link, the section owners, and the practice date.

## Gate 1 - Story, named model, winner chart, and test protocol frozen

Gate 1 freezes what the talk is allowed to say, names the model from the
validation scores already on file, and freezes the test procedure that will
confirm that name. Gate 1 does not contain a test MAE. Andre and Matthew can
draft their sections from this gate. Nevaeh can draft the choice slide from
the winner chart and leave the test confirmation blank.

### Slide outline

- [ ] Create the shared deck with the six sections and the owners in the table
  above.
- [ ] Andre drafts the hook and the overview. The results preview names XGBoost
  from the validation MAE and leaves the test confirmation for Gate 2.
- [ ] Matthew drafts the data and preprocessing slides from the September bundle
  and the October preprocessor.
- [ ] Nevaeh drafts the model list, the MAE explanation, the named-model line,
  and the winner chart. The test confirmation stays marked unfinished until
  Gate 2.
- [ ] A teammate who did not write the section reads it and marks any sentence
  that is stronger than the named-model record below.

### Confirm and name the winning model

October left this unnamed because the two model scores were close. Gate 1
names one model with one rule, written down before anyone computes a test MAE.

The rule: among the four recorded approaches, the named model is the one with
the lowest validation MAE, in original dollars, on the same 28,248 validation
claims. The large-claim slice is reported beside that choice. It does not
break the tie and it does not replace the rule.

Under that rule the named model is XGBoost.

| Approach | Validation average miss | Role after Gate 1 |
| --- | ---: | --- |
| Training mean ($3,033.69) | $1,978.40 | Constant |
| Training median ($2,113.76) | $1,827.31 | Constant |
| Random forest | $1,291.59 | Comparison model |
| XGBoost | $1,171.72 | Named model |

XGBoost's validation miss is about $119.87 lower than the forest's and about
$655.59 lower than the training median's. Both models still beat both
constants. The forest's miss on the 285 large validation claims is $8,868.69.
XGBoost's miss on those same claims is $9,265.72.

- [ ] Write the rule and the name in the November protocol: XGBoost, chosen by
  lowest validation MAE. Record the gap against the forest and against the
  median.
- [ ] Record the large-claim figures next to the name, with the sentence that
  they are context and not the naming rule.
- [ ] If the optional `cont11` / `cont12` experiment below is run, apply the
  same rule to the new validation score before naming. A version that beats
  $1,171.72 on the same 28,248 claims replaces XGBoost as the named model.
  A version that does not is left out of the name.
- [ ] Have a teammate who did not write the rule recompute the four validation
  MAEs from
  [`validation_mae.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/validation_mae.csv)
  and sign that the name matches the lowest one.

### Winner chart

Make one figure in Gate 1, from the validation tables only, and put it on the
modeling slide. Suggested file:
`artifacts/november/gate4-november-milestone-reproducible-project/figures/validation_winner.png`.
Two panels, shared approach order, dollar axis starting at $0 so the gaps stay
honest.

**Panel A, the naming panel.** Horizontal bars for the four validation MAEs,
top to bottom: training mean ($1,978.40), training median ($1,827.31), random
forest ($1,291.59), XGBoost ($1,171.72). Label each bar in dollars. Draw the
XGBoost bar in a distinct color and label it "Named model." Title the panel
with the claim count: average dollar miss on 28,248 validation claims. A short
caption states the rule: named because this is the lowest validation MAE, about
$120 lower than the forest and about $656 lower than the median.

**Panel B, the context panel.** Grouped bars for the same four approaches.
One group is the 285 validation claims at or above the training 99th percentile,
about $14,017.41. The other group is the remaining 27,963. The forest bar is
lower on the large-claim group ($8,868.69 versus $9,265.72). The XGBoost bar
is lower on the remainder ($1,089.22 versus $1,214.37). Caption: this panel
shows where the misses sit. The named model is still the one in Panel A.

- [ ] Build the figure from
  [`validation_mae.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/validation_mae.csv)
  and
  [`high_loss_tail.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/experiments/high_loss_tail.csv).
  Do not hand-type the bar lengths.
- [ ] A teammate checks that the four overall bars and the two large-claim bars
  match those files, and that only the XGBoost bar is marked as the named model.
- [ ] Leave room on the slide for a test confirmation line. That line is filled
  in Gate 3 from the Gate 2 table. It does not recolor the bars.

### Locked October evidence

- [ ] Confirm the source hash, the manifest hash, the row counts, and the
  package versions in the October handoff: Python 3.12, pandas 3.0.6, NumPy
  2.5.3, scikit-learn 1.9.1, XGBoost 3.4.1.
- [ ] Confirm the field list in
  [`field_roles.csv`](../../artifacts/october/gate4-october-milestone-reproducible-project/field_roles.csv):
  `cat1` through `cat116` and `cont1` through `cont14` are inputs. `id` and
  `loss` are not.
- [ ] Copy the recorded settings into the November protocol and onto the modeling
  slides, unchanged:
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
  The default recorded in October is that it was not run. The future-work
  slide uses whichever decision is written here.
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
  procedure. A later change to settings, features, or the seed reopens Gate 1
  and pulls the results slides back with it.
- [ ] Record how unseen category levels will be handled on the test claims:
  `handle_unknown='ignore'`, fit on training claims only, same as validation.
- [ ] Have someone other than the protocol author confirm:
  - the manifest still has 131,822 / 28,248 / 28,248 and no shared `id`;
  - the notebook does not fit on test rows;
  - the notebook does not read a test score to choose a setting or a name;
  - the named model and the winner chart are already written down;
  - the optional feature decision, if any, is already written down.

## Gate 2 - Held-out comparison scored

Gate 2 is the one time the team computes the test scores. The output is a
table the modeling slides can quote, and a confirmation of the model named in
Gate 1. The output does not select a different model.

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
  a new file. A reader, and a slide, should be able to see which number came
  from which partition.
- [ ] Generate the table from the notebook. Do not type the scores onto a slide
  and leave the notebook unsaved.

### Large-claim check

- [ ] Use the same cut October used: the training 99th percentile of `loss`,
  about $14,017.41. Count how many of the 28,248 test claims fall on that side
  of the cut, and how many remain.
- [ ] Report test MAE for each scored approach on that large-claim slice and on
  the remainder.
- [ ] Treat the slice as a description of where the misses sit. The count will
  be small. It does not rename the model, and it does not retitle the choice
  slide.

### Confirm the named model

- [ ] Say which approaches have a lower test miss than the training-mean
  constant and which have a lower test miss than the training-median constant,
  on these same test claims.
- [ ] Report the gap between the forest and XGBoost in dollars. State whether
  that gap is large or small next to the scores, the same way Gate 1 compared
  the validation gap of about $119.87 with the forest score.
- [ ] Confirm the Gate 1 name in one sentence. If XGBoost also has the lowest
  test MAE, write that the test score agrees. If another approach is lower on
  the test claims, write that the test ranking differs and keep the Gate 1
  name.
- [ ] Put that sentence in the test-score note. Gate 3 copies it onto the choice
  slide under the winner chart. The chart's highlighted bar stays XGBoost.

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
  new value, and a second independent check. Update the slides from the
  corrected table. Do not silent-edit either one.

## Gate 3 - Deck drafted from the tables

Gate 3 finishes the slides and the short report those slides rest on. A slide
is drafted when its owner has written it and another teammate has checked it
against the table.

### Finish the deck

- [ ] Nevaeh adds the test table, the test large-claim check, and the Gate 2
  confirmation sentence to the modeling slides. The winner chart stays the
  Gate 1 figure, with XGBoost marked.
- [ ] Andre updates the overview preview so the test confirmation is one plain
  sentence, separate from the validation result that named the model.
- [ ] Nevaeh drafts final thoughts: skills the fellows supplied, the future
  work still open after Gate 1, and the acknowledgments.
- [ ] Add the single Q&A slide at the end.
- [ ] Read the full deck in order. Cut any number, model, or business meaning
  that the November report does not support.
- [ ] Save speaker notes under each section so the owner can give it without
  reading the notebook.

### November report

The report is the page a slide number comes from. It does not need to be longer
than the talk.

- [ ] Write a plain-language November report that covers:
  - what one row is and what `loss` is;
  - the frozen split and which claims were scored in October versus November;
  - the two constants and why the median is included;
  - the two recorded models and the frozen settings;
  - the validation scores and the test scores, in separate tables;
  - the large-claim check on validation and the same check on test;
  - the Gate 1 rule, the named model, and the winner chart;
  - whether the test score agrees with that name;
  - the optional feature experiment, including a clear "not run" if it was
  skipped;
  - what remains unknown because the fields are anonymous.
- [ ] Put the exact figures in the committed tables. The report and the slides
  may round the way the October report rounds, and both should point at the
  unrounded file.
- [ ] Update the README so a new reader can find the September bundle, the
  October bundle, the November test scores, and the deck.

### Optional key predictors

This block is optional. Skip it if the deck is not yet drafted. It is not
required for December 16.

- [ ] If the team computes importances or coefficients, fit that check on the
  training claims only.
- [ ] If a slide shows a rank, label every named column as an anonymous
  predictor. `cat*` and `cont*` stay codes.
- [ ] Keep the four scored approaches unchanged by this check.

### Limitations on the slides

- [ ] Somewhere in the overview, the modeling section, or final thoughts, the
  deck says:
  - the scores are a retrospective check on the supplied file;
  - September had already looked at all 188,318 claims before the split;
  - the field names do not say what is known at first filing;
  - a score does not set a reserve, show a cause, or show production readiness;
  - high-loss claims stayed in the data.
- [ ] Carry the advisor question onto the future-work slide: which anonymous
  fields are known when a claim is first filed?
- [ ] The slides do not say the September or October teammate sign-offs are
  closed while those lines are still blank.

## Gate 4 - Practiced and presentation-ready before December 16

Gate 4 is a spoken run of the finished deck. Slides that have not been given
out loud do not finish this gate.

**Completion rule:** The team is presentation-ready only when the practice
below has happened before December 16, 2026, and the deck still matches the
tables after that practice. If the test protocol or the Gate 1 name is still
unresolved, keep Gate 4 open and record the blocker. Do not rename the model,
drop a field, or rewrite a score to make the ending cleaner.

### Practice

- [ ] Andre gives the hook and the overview. Matthew gives the data section.
  Nevaeh gives modeling, evaluation, and final thoughts. The whole team takes
  questions after the Q&A slide.
- [ ] Run the full presentation out loud at least once before December 16.
  Record the date and the runtime.
- [ ] In that practice, each speaker can answer, without the notebook:
  - what their section is claiming;
  - why MAE is in original dollars;
  - why the median constant is next to the required mean constant;
  - why XGBoost is the named model, and what Panel B of the winner chart shows;
  - what the test confirmation sentence says, including a disagreement if
  there is one;
  - why the result is not yet an estimate at first notice of a claim.
- [ ] Hold a short question practice for a technical listener and a
  non-technical listener. Use the validation gap of about $119.87, the 285
  large validation claims, the test table, and the unanswered timing question.
- [ ] After the practice, fix any sentence that is stronger than the tables.
  Save the practice notes with the date, who spoke, what ran long, and what
  changed on the slides.
- [ ] If that pass changed a result or a limitation, run the changed sections
  out loud once more. Still finish before December 16.

### Team review

- [ ] Confirm the final November bundle contains:
  - the frozen protocol, including the named model;
  - the winner chart;
  - the November notebook;
  - the test MAE table;
  - the test large-claim table;
  - the November report;
  - reproduction steps;
  - the independent-review record;
  - the deck link, the section owners, and the practice notes.
- [ ] The team watches the deck in order and records approvals, dissent, and
  anything still undone. Unfinished work does not appear on a slide as a
  result.
- [ ] In the team retrospective, record:
  - one practice to keep;
  - one practice to change;
  - one experiment that stayed deferred, and why;
  - one lesson about stating only what the claims file can support.
