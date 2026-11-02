---
name: incident-intelligence
description: Analyze accessible defect, outage, support and postmortem evidence to identify patterns relevant to a proposed feature. Use when historical quality signals could change testing priorities, regression scope or rollout safeguards.
metadata:
  author: Jessica Mosley
  linkedin: https://www.linkedin.com/in/jessmosley/
  github: https://github.com/j-m-o/
---
# Incident Intelligence

## Inputs
Authorized incident records, defect history, changes, logs, dates, impacted services, remediation actions and issue context. Use only material the host actually provides or retrieves.

## Procedure
1. Define time window, products, affected workflow, severity criteria and search scope.
2. Retrieve relevant incidents or defects using read-only authorized tools, if available.
3. Separate confirmed root cause from hypothesis and correlation; attach incident identifiers where available.
4. Identify repeating failure modes, unresolved corrective actions, risk concentration and changed assumptions.
5. Recommend targeted regression tests, observability, rollout controls and owner follow-ups.
6. Note data gaps, survivor bias and incomplete incident coverage.

## Output
### Relevant History
**Search window and source:** <scope or Not available>
**Confidence:** <High, Medium or Low>
- <Verified incident identifier, theme and date>

### Recurring Failure Modes
- <Pattern with evidence or Not established>

### Feature Implications
- <Specific change to test or release plan>

### Actions and Open Questions
- <Owner role, test and monitoring action>

## Boundaries
Never invent a customer incident or assert a cause that a source does not support. Do not share private postmortems in externally distributed material. Analysis cannot substitute for a live incident response process.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
