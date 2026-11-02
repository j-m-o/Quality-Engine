# Jira comment template

A human-readable final comment using two **preserved** agent responses. Configure the editor in your Jira Cloud tenant and test formatting with a sample issue. Markdown rendering varies with the specific action and editor.

```markdown
## Quality Engine Assessment

**Work item:** {{issue.key}} | {{issue.summary}}

### Existing Test Coverage
{{coverageResponse}}

### Quality, Risk and Planning Assessment
{{qeAnalysisResponse}}

---
*AI-assisted quality planning. Findings reflect available evidence and require QE, Product and Engineering review. This comment is not a release approval.*
```

If the response already includes an assessment title, remove the duplicated wrapper heading. Do not let the QE Analysis agent reprint or silently replace the original coverage summary. Comment the preserved coverage response and preserved QE response separately.

**Option:** Once the workflow is validated, simplify the comment to a single feature snapshot plus expandable links to deeper review artifacts. Keep evidence and unknowns visible.
