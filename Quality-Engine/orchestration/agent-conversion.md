# Converting portable skills into orchestrated agents

## Skills are not agents

Each `SKILL.md` captures procedural expertise and output expectations. To convert it into an executing agent, supply an agent host, permissions, tool bindings, prompt or system configuration, input/output validation, triggering and observability. Skill text alone cannot contact Jira, mabl, a test database or an incident platform.

## Core orchestration

1. **Coverage agent**: Bind read-only test inventory tools. Pass issue, product/module mapping and acceptance criteria. Return evidence-linked coverage review and confidence.
2. **QE Analysis agent**: Bind read-only issue context and the preserved Coverage Review output. Return readable analysis plus an optionally validated structured assessment.
3. **Publisher**: Validate outputs, then add one Jira comment and optionally update the six configured custom fields. Publishing should be a separate trusted workflow action.

## Future optional agents

| Agent wrapper | Skill | Required tool category | Trigger to consider |
| --- | --- | --- | --- |
| Coverage Agent | coverage-review | Test management, test execution records | Feature assessment request |
| QE Analysis Agent | qe-analysis | Issue tracker, coverage result | After coverage result or explicit standalone request |
| QE Planning/Test Design Agent | qe-planning-test-design | Requirements, designs and optional test management | On-demand detailed planning |
| Security Review Agent | security-review | Authorized security policies and findings | Sensitive workflow or requested review |
| Accessibility Review Agent | accessibility-review | Design and accessibility test evidence | UI change or requested review |
| Incident Intelligence Agent | incident-intelligence | Incident tracker, defect history and observability | Repeated production risk or requested analysis |
| Metrics Intelligence Agent | metrics-intelligence | Telemetry and product analytics | KPI definition or metric change investigation |

## Contract between agents

- Provide issue metadata, scope, acceptance criteria and explicit evidence references.
- Preserve upstream observations. Downstream agents may challenge conclusions **with new evidence**, but must not falsify or silently replace upstream source records.
- Each agent returns its own output object, with source, date, scope and confidence.
- Pass only minimum necessary context across trust boundaries.
- Do not allow specialist agents to publish, edit issues, run intrusive scans or create test cases automatically unless the workflow explicitly grants and audits the action.
- Validate score type, categories and required fields before updating Jira.
- Define timeout, retry, missing-tool and partial-failure behavior. If Coverage fails, QE Analysis may proceed with Unknown coverage and a visible caveat.
- Keep all on-demand skills outside the default Jira comment unless a human chooses to include them.

## Deployment patterns

**Simple:** Jira automation calls Coverage Agent, saves response, calls QE Analysis Agent, saves response, posts comment. This is the easiest portfolio demo.

**Advanced:** Quality Engine, as the orchestrator, routes to any of the seven specialized agents, validates a JSON contract, stores evidence and publishes a human-readable result. This can be implemented with Rovo, an agent runtime with MCP tools or another orchestration environment, subject to feature and permission support.

## What not to promise

Do not market `SKILL.md` files alone as a fully autonomous multi-agent product. Show a static skill demo and a separately verified live integration when available. Describe business gains as intended outcomes unless you have measured before-and-after results.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
