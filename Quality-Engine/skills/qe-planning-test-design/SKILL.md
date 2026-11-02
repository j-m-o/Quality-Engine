---
name: qe-planning-test-design
description: Generate risk-based feature test plans, scenarios and executable test case tables from requirements and acceptance criteria. Use when a person explicitly requests deeper test design, exploratory coverage, API cases, regression mapping or automation candidates; not as an automatic Jira scoring step.
metadata:
  author: Jessica Mosley
  linkedin: https://www.linkedin.com/in/jessmosley/
  github: https://github.com/j-m-o/
---
# QE Planning and Test Design

## When to activate
Activate **only when explicitly requested** by a QE, engineer or automation orchestration action. This skill is not part of the routine assessment comment or readiness score calculation.

## Inputs
Application or product name, intended outcome, issue and acceptance criteria, interfaces, roles, environment, test data, integration dependencies and optional coverage review. If application or intended behavior is unknown, request missing essentials before presenting detailed cases. If issue data already clearly provides these details, do not ask again.

## Method
1. Parse requirements and map scenarios to acceptance criteria.
2. Identify representative positive, negative, boundary, integration, state-transition and regression paths.
3. Add relevant accessibility, security, performance, API, data integrity and analytics considerations, not forced filler.
4. Identify assumptions, dependencies, test data, environments and blocked conditions.
5. Prioritize by business risk and automation maintainability.
6. Make each expected result observable, precise and aligned with system behavior; avoid a fixed generic success suffix for negative cases.
7. Recommend stable, valuable automation candidates with rationale. Tool-specific options (mabl, Playwright, Cypress) are optional adapters.
8. If requested, draw a Mermaid logic flow for an individual test case using supplied facts. When asked for **diagram only**, output only fenced Mermaid syntax.
9. For analytics-sensitive features, recommend relevant user behavior signals, errors, success rates and dashboards using PostHog, Sentry, Datadog or equivalent providers with a reason for each suggestion.

## Required output
Use [test-plan-template.md](assets/test-plan-template.md) for full plans. When the request is **test cases only**, include a concise test description and the three-column table **Action | Data | Expected Result**. When both scenarios and cases are requested, list scenarios first, then cases. Use clear names and traceability to acceptance criteria.

## Guardrails
- **Ownership comes from the input:** derive teams from the ticket, or state Unassigned.
- **Dates come from the input:** provide requested or planned dates only; otherwise state To be scheduled.
- **Do not invent product endpoints, credentials or success responses:** use actual contract expectations, including appropriate error responses.
- **Do not claim to persist memory** beyond context or connected storage actually available to the host.
- Only write to a test management system if a separately approved agent/tool workflow authorizes it.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
