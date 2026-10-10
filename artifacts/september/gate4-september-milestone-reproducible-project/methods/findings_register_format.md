# Findings register format

Bundle ID: `gate2-issue-reproducible-project`

Version: `gate2-method-freeze-1`

Gate 3 writes the findings themselves inside the Gate 3 artifact bundle. This file freezes the columns those rows must use.

| Column | Required content |
| --- | --- |
| `finding_id` | Stable ID, such as `F-001` |
| `title` | Concise title |
| `evidence_link` | Exact table, figure, or notebook path |
| `observed_result` | What was calculated |
| `interpretation` | What the team says that result means |
| `evidence_status` | One of the four statuses below |
| `limitation` | Alternative explanation or limit on the claim |
| `october_implication` | What October might test. This is not completed modeling work. |
| `owner` | Person responsible for the finding |
| `reviewer` | Person who checked the underlying evidence |

## Evidence status

Use only these terms:

- **directly observed:** a result calculated from the supplied data;
- **consistent with a pattern:** a repeated association whose business meaning is still unknown;
- **hypothesis:** a possible explanation that this file does not establish;
- **inconclusive:** the evidence does not support a conclusion.

Gate 3 conclusions wait until the team approves this format together with the data dictionary, rare-level rule, bin rule, and target-view settings. That approval is recorded in [`../review/team_approval.md`](../review/team_approval.md).
