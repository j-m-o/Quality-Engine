# Proposed feature readiness scoring rubric

**This is a transparent starting model, not a statistically validated predictor.** Teams should calibrate weights and thresholds against retrospective outcomes rather than claim a universal quality score.

| Dimension | Maximum | Full-credit evidence | Common deductions |
| --- | ---: | --- | --- |
| Requirements and acceptance criteria | 25 | Clear user outcome, measurable success, normal and failure behavior, acceptance criteria | Ambiguous outcome, absent edge behavior, contradictory requirements |
| Testability and observability | 20 | Inputs, results, test data, environments and useful signals are identifiable | Results cannot be verified, no viable test data or visibility |
| Coverage evidence and regression understanding | 20 | Existing behavior mapped to actual test evidence, target gaps known | Only adjacent tests, unclear impacted paths, unverified evidence |
| Risks and dependencies | 20 | Dependencies, external integrations, permissions, rollout and mitigations known | Unowned dependencies, unclear data contracts or significant unknowns |
| QE execution plan and ownership | 15 | Practical testing approach, owners, sequencing and quality gates are identified | No plan, unclear ownership, unrealistic scope |
| **Total** | **100** | | |

## How to score

1. Assign integer points for each dimension, not exceeding its maximum. Briefly explain any material deduction.
2. Add the five component scores. Do not silently normalize away missing evidence.
3. When key facts are absent, mark the result **provisional** with Low confidence; when the issue lacks meaningful requirement content entirely, use **Not assessed** instead of an invented zero.
4. As suggested discussion bands only: 80 to 100 often indicates strong planning readiness; 60 to 79 indicates targeted refinement; below 60 suggests substantial refinement. **Do not configure hard release gates based solely on these bands.**
5. Critical unmitigated concerns may require escalation regardless of readiness score.

## Feature Risk Level

| Level | Working interpretation |
| --- | --- |
| Low | Limited harm and straightforward recovery, with known mitigation |
| Medium | Meaningful workflow, data or operational impact but bounded exposure |
| High | Significant customer, security, financial, privacy or service exposure with material uncertainty |
| Critical | Credible severe consequence requiring immediate risk-owner review, such as serious unauthorized access or widespread data loss |

Use evidence-based severity and likelihood. A high planning score does not cancel high feature risk.

## QE Effort Estimate

- **Low:** Focused test additions, limited dependencies and predictable test data.
- **Medium:** Several workflows, environments or integrations, plus regression coordination.
- **High:** Cross-system impact, complex data or environments, substantial manual and automation planning.
- **Undetermined:** Scope or baseline information is insufficient.

These are relative sizes, not days or story points. Numeric time requires team benchmarks and assumptions.

## Automation ROI Level

Consider repeat frequency, criticality, test stability, automation feasibility, data setup, maintenance and breadth of regression protection.

- **High:** Valuable recurring verification with repeatable, stable workflow and manageable maintenance.
- **Medium:** Material benefit but uncertain execution frequency, cost or stability.
- **Low:** Rarely repeated, predominantly exploratory, highly volatile or disproportionately costly to maintain.
- **Undetermined:** Benefits or costs lack enough evidence for a reasonable judgment.

If quantitative baselines are available, an optional estimate is `expected avoided manual effort and defect impact minus build and maintenance effort`, with time horizon and assumptions shown. Never imply this is measured financial ROI without appropriate data.

## Coverage Recommendation rules

- **Maintain existing:** direct evidence addresses priority behaviors and no meaningful new risk arises.
- **Update existing:** existing tests align with impacted behavior but need assertion or workflow changes.
- **Add targeted tests:** specific new behavior or risk scenarios lack direct coverage.
- **Expand regression coverage:** change affects multiple critical or existing workflows.
- **Investigate coverage first:** evidence cannot be trusted, searched or mapped.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
