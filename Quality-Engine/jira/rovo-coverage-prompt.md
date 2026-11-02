# Copyable prompt for a coverage-focused agent

```text
Assess test coverage for the issue below. Read the issue's product or module field and use an explicitly configured mapping to search the test platform, if a test connector is available. Do not claim to have searched when you did not. If searches fail or the scope cannot be established, use Unknown, not Missing.

Issue key: {{issue.key}}
Summary: {{issue.summary}}
Product: {{issue.Product}}
Description: {{issue.description}}

Acceptance criteria: <Replace with the smart value configured for your project>

Tasks:
1. Extract the main acceptance criteria and critical user paths.
2. Find directly relevant tests, including test name or ID and a link when available.
3. Separate exact behavior coverage from nearby tests or labels.
4. Identify important positive, negative, role, integration and regression gaps.
5. Recommend the smallest valuable coverage change.

Return only readable Markdown with these labels and no underscore-separated field names:

### Coverage Summary
**Test Coverage Level:** Strong, Partial, Weak, Missing or Unknown
**Coverage Confidence:** High, Medium or Low
**Product or Label Searched:** <value or Not verified>
**Relevant Test Count:** <verified number or Unknown>

### Verified Tests
- <Name, identifier, what it validates and link, or No evidence available>

### Coverage Gaps
- <Specific gap or Unknown due to insufficient evidence>

### Recommended Tests
- <A concrete test with its rationale>

### Final Coverage Recommendation
<One recommendation and why>
```

If the test system cannot be accessed, the response should **not** invent tests, counts or successful searches. This text is a prompt template, not a direct MCP implementation.
