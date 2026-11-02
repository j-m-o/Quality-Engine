# Agent handoff and result contracts

The canonical structured QE assessment is `schemas/feature-quality-assessment.schema.json`. The JSON properties are for software orchestration; the Jira comment uses human-readable labels without underscore-separated identifiers.

## Coverage Agent output

- `testCoverageLevel`: Strong, Partial, Weak, Missing or Unknown
- `confidence`: High, Medium or Low
- `searchedProduct`: specific mapping used or null
- `relevantTests`: verifiable identifiers and accessible links, if available
- `coveredBehaviors`: requirement-to-test mapping
- `coverageGaps`: risks not confirmed covered
- `recommendation`: one allowed coverage recommendation
- `evidenceStatus`: Verified, Partial or Unavailable

## QE Analysis Agent input

- Work item context, scope and acceptance criteria
- One **immutable upstream Coverage Agent output** or Unknown status
- Optional risk, telemetry or historical data that is actually provided

## QE Analysis Agent output

- Six standard assessment fields
- Readiness component scores with a transparent sum
- Evidence links or pointers
- Separate risks, unknowns, actionable recommendations, confidence and date

## Optional review agents

The remaining specialists emit a `reviewType`, `scope`, `findings`, `evidence`, `unknowns`, `recommendedActions` and `confidence`, with no automatic scoring or publishing. Human reviewers or orchestration policy decide whether findings affect the core assessment.

## Failure contract

- **Test platform unavailable:** Coverage level Unknown, confidence Low, proceed only if automation is allowed to assess a provisional ticket.
- **Ticket missing acceptance criteria:** QE Analysis flags insufficient input, may use Not assessed.
- **Bad or schema-invalid assessment:** Do not update fields. Publish an error to the rule audit log and request human review.
- **Conflicting source claims:** Preserve evidence, mark a discrepancy and prompt verification rather than collapsing to one invented truth.
- **Publish failure:** Do not claim a comment was posted; record the failure for follow-up.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
