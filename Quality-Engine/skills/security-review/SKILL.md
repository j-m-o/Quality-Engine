---
name: security-review
description: Identify feature-level security and privacy test risks from design and requirements, including authentication, authorization, data flows and integrations. Use during refinement or on demand to propose verification, not to claim a penetration test or compliance certification.
metadata:
  author: Jessica Mosley
  linkedin: https://www.linkedin.com/in/jessmosley/
  github: https://github.com/j-m-o/
---
# Security Review

## Purpose
Provide a pragmatic secure-design and security-testing lens for a feature without replacing security specialists or actual technical testing.

## Procedure
1. Summarize entry points, user roles, trust boundaries, sensitive data, integrations and administrative actions.
2. Check relevant concerns: authentication, horizontal and vertical authorization, session safety, data access, input validation, secrets, auditability, rate limiting, logging hygiene, retention and third-party access.
3. Consider applicable privacy and contractual requirements only when specified; do not assert legal obligations without context.
4. Prioritize plausible failure modes by consequence and exposure, distinguishing hypotheses from verified findings.
5. Write testable security conditions and remediation questions with suggested owners.
6. Recommend authorized SAST, DAST, dependency checks, API authorization tests or focused review when suitable.

## Output
### Security Review Snapshot
**Risk Level:** <Low, Medium, High, Critical or Unknown>
**Evidence Confidence:** <High, Medium or Low>

### Sensitive Workflows and Trust Boundaries
- <Workflow and source>

### Verification Scenarios
- <Specific defensive validation and expected control>

### Gaps and Questions
- <Unknown or unverified assumption>

### Recommended Next Actions
- <Risk owner, evidence and priority>

## Boundaries
Do not claim vulnerabilities exist without evidence, do not invent security scan results and do not perform intrusive testing without explicit authorization. Avoid exposing secrets or sensitive incident data. This skill does not certify compliance.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
