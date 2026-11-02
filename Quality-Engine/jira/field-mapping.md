# Jira field mapping and setup

Create the optional six custom fields in your own Jira space, review their project and issue-type contexts, and confirm automation edit permission before writing.

| Portable assessment property | Recommended Jira display name | Field type | Allowed values |
| --- | --- | --- | --- |
| featureQualityReadinessScore | Feature Quality Readiness Score | Number | 0 to 100; blank when unscored |
| featureRiskLevel | Feature Risk Level | Single select | Low; Medium; High; Critical |
| testCoverageLevel | Test Coverage Level | Single select | Strong; Partial; Weak; Missing; Unknown |
| qeEffortEstimate | QE Effort Estimate | Single select | Low; Medium; High; Undetermined |
| automationRoiLevel | Automation ROI Level | Single select | Low; Medium; High; Undetermined |
| coverageRecommendation | Coverage Recommendation | Single select | Maintain existing; Update existing; Add targeted tests; Expand regression coverage; Investigate coverage first |

**Optional vendor-specific alias:** Teams using mabl may use **Mabl Coverage Level** instead of **Test Coverage Level**. Keep the underlying result equivalent, and store the test system name and searched label in the evidence section.

## Recommended operational approach

- **Phase 1:** Comment only. Manually review assessment accuracy and formatting.
- **Phase 2:** Persist the six fields after agent outputs and value parsing are validated.
- **Phase 3:** Build Jira queries, charts or dashboards, with readiness scores treated as a decision support signal.

## Data interpretation safeguards

A missing score should remain **blank**, not zero. Coverage Unknown must not be transformed to Missing. Do not auto-close issues, block deployment or approve release from a single model score. Store the assessment's evidence links and date in the comment or an appropriate artifact.

## Mapping a custom field value

Atlassian supports named smart values such as `{{issue.Product}}` and certain object properties such as `{{issue.Product.value}}`, but the correct expression depends on the actual field type and tenant configuration. Inspect the automation audit log rather than assuming one representation is universal.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
