# Task Progression Workflow

Each project task moves through three people. Use these GitHub project statuses, in order:

**In progress → Ready for Review → In Review → Ready for Documentation → Done**


| GitHub project status       | Who sets it                   |
| --------------------------- | ----------------------------- |
| **In progress**             | Evidence Owner                |
| **Ready for Review**        | Evidence Owner                |
| **In Review**               | Independent Teammate Verifier |
| **Ready for Documentation** | Independent Teammate Verifier |
| **Done**                    | Team Readiness Reviewer       |


## 1. Evidence Owner

1. Set the GitHub project task to **In progress**.
2. Create a notebook titled for the gate and the milestone month. Save it under `notebooks/<milestonemonth>Milestone/`.
3. Write the code in that notebook.
4. Save the notebook in the shared Google Drive folder for Colab notebooks.
5. Add the notebook to this repo.
6. Set the GitHub project task to **Ready for Review**.
7. Notify the reviewer.



## 2. Independent Teammate Verifier

1. Set the GitHub project task to **In Review**.
2. Review the code in the notebook.
3. Document any necessary changes in the findings register inside that gate's artifact bundle.
4. Set the GitHub project task to **Ready for Documentation**.



## 3. Team Readiness Reviewer

1. Review the code in the notebook.
2. Confirm that the findings recorded in the previous step are fixed.
3. Record findings in the findings register inside that gate's artifact bundle.
4. Record anomalies in the anomaly register inside that gate's artifact bundle.
5. Set the GitHub project task to **Done**.

