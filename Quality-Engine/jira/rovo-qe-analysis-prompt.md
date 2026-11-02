# Copyable prompt for the QE Analysis agent

```text
Assess the feature for quality readiness, engineering risk, testing effort and automation return. Use the QE Analysis skill's five-part scoring rubric. Keep the six standard fields consistent with their allowed options.

Issue key: {{issue.key}}
Summary: {{issue.summary}}
Issue type: {{issue.issueType.name}}
Priority: {{issue.priority.name}}
Product: {{issue.Product}}
Description: {{issue.description}}
Acceptance criteria: <Replace with your project smart value>

Existing coverage assessment from the specialized agent:
{{coverageResponse}}

Important constraints:
- The coverage assessment is evidence from an upstream specialist. Preserve its stated coverage status and tests, and do not overwrite it.
- If the coverage text is empty or unusable, mark Test Coverage Level Unknown.
- If requirements are too incomplete, use Not assessed rather than inventing a readiness score.
- Show evidence, assumptions and score components. ROI may be qualitative; never fabricate savings.
- Do not change the ticket or add comments yourself. Return the analysis only.

Return only readable Markdown:

### Feature Snapshot
**Feature Quality Readiness Score:** <0 to 100 or Not assessed>
**Feature Risk Level:** <Low, Medium, High or Critical>
**Test Coverage Level:** <Strong, Partial, Weak, Missing or Unknown>
**QE Effort Estimate:** <Low, Medium, High or Undetermined>
**Automation ROI Level:** <Low, Medium, High or Undetermined>
**Coverage Recommendation:** <one allowed recommendation>
**Assessment Confidence:** <High, Medium or Low>

### Quality Summary
<Two to four sentences>

### Readiness Scoring Rationale
- Requirements and acceptance criteria: <score>/25, with rationale
- Testability and observability: <score>/20, with rationale
- Coverage evidence and regression: <score>/20, with rationale
- Risks and dependencies: <score>/20, with rationale
- QE execution plan and ownership: <score>/15, with rationale

### Key Risks
- <Specific consequence and evidence>

### Testing Recommendations
1. <Concrete action>

### Automation Recommendations and ROI
<Repeatability, payoff and maintenance tradeoff>

### Missing Information
- <Question and likely owner role>

### Final Recommendation
<Clear next action and suggested owner role>
```

For machine-readable field updates, request a response conforming to `schemas/feature-quality-assessment.schema.json` in a separate validated action. Avoid fragile extraction from freeform prose when updating Jira custom fields.
