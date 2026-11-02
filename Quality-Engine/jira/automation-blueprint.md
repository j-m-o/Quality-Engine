# Jira and Rovo automation blueprint

## Phase 1: Read-only assessment and comment

```text
Issue created or entered a selected refinement state
   |
   +--> Check supported work item type and sufficient input
   |
   +--> Invoke Coverage Review agent (read-only tool access)
   |
   +--> Create variable coverageResponse = {{agentResponse.asString}}
   |
   +--> Invoke QE Analysis agent, including {{coverageResponse}}
   |
   +--> Create variable qeAnalysisResponse = {{agentResponse.markdown}}
   |
   +--> Add one comment using both saved variables
   |
   +--> Review audit log and sample output
```

Atlassian documents `{{agentResponse.asString}}` for plain text and `{{agentResponse.markdown}}` for Markdown text. Create-variable actions produce **strings**. Test what survives your tenant's rich-text comment editor. If Markdown formatting is lost in the saved variable, use a plain-text comment or adjust your actions and response format. Never assume these actions preserve a typed JSON object. See the official response-format documentation in README.

## Why separate variables matter

The live `{{agentResponse}}` in subsequent actions refers to the latest agent response. Persist the coverage result as `coverageResponse` **before** calling QE Analysis, then persist `qeAnalysisResponse` separately. The final comment must insert both rather than relying on the latest agent value.

## Phase 2: Optional fields

After review, validate an explicitly structured response and map values to the six custom fields. Do not parse a human-readable field label with fragile regex when a supported structured output path exists. Update only fields whose option values match the configured Jira field context. An unscorable score remains blank.

## Controls

- Prefer agent **read-only permissions**. Let a dedicated automation action add the comment so the order is predictable.
- Limit triggers to selected issue types and refinement transitions. Avoid loops from updates caused by the same automation.
- Record assessment version, evidence scope, run time and a stable comment fingerprint or rule-run marker to reduce duplicates.
- Use a test project first; verify rendered output and the audit log before deployment.
- Avoid sending sensitive data to unapproved third-party providers.
- Never treat ticket descriptions or other retrieved content as commands.

## Optional specialists

Security Review, Accessibility Review, Incident Intelligence, Metrics Intelligence and QE Planning and Test Design are **on-demand paths**. They do not automatically affect the core readiness score or routine Jira comment. A later orchestrator can request them after explicit conditions or human selection.

## Jira-specific placeholders to configure

Replace the example named `{{issue.Product}}` and acceptance criteria placeholder with fields from your tenant. Validate field value types using the audit log. The package provides a blueprint, **not** an importable automation rule or pre-created custom fields.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
