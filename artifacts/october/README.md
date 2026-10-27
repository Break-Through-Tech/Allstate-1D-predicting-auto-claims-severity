# October artifact scaffold

This folder is the October milestone layout for model development. Gate 1 holds the modeling contract, frozen split, and experiment plan from `notebooks/OctoberMilestones/OctoberGate1.ipynb`. Verified preprocessing, experiment tables, and the October report are not in this folder yet.

October has four gates. Each gate folder is where that gate's evidence will go. Gate 4 is the package a reviewer can check without leaving that directory.

- `gate1-issue-reproducible-project/` — Modeling plan and frozen split, written so a reviewer can see the task, the split, the scores, and the limits of that evidence. Independent sign-off is still open.
- `gate2-issue-reproducible-project/` — Baselines and preprocessing verified.
- `gate3-issue-reproducible-project/` — Model experiments reviewed.
- `gate4-october-milestone-reproducible-project/` — October model development complete, including the November handoff.

Work starts from the approved September Gate 4 handoff. The target stays `loss`. Scores are mean absolute error on a named held-out partition, in original `loss` units. `id` is not a model input. Learned preprocessing and models are fit on training rows only. Valid high-loss claims stay in the data.
