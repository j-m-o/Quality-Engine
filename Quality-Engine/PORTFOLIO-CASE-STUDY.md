# Portfolio Case Study: Quality Engine

Created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)

## Why I created this
Teams stitch quality signals together by hand from the tracker, test platform, error tracking and incident history at the moment a decision is due. I built Quality Engine to do that once, from only the tools a team uses, and to answer a question most test tools skip: is this a poor area to build in right now because of recent errors and slowdowns? It is vendor-neutral on purpose.

## One-line positioning
**Turning software requirements, test coverage evidence and delivery risk into decisions engineering teams can actually use.**

## Problem
Traditional refinement and quality reviews often scatter acceptance criteria, test coverage evidence, risk and engineering effort across separate tools and conversations. This makes prioritization harder and reduces visibility into why a feature is or is not ready for testing.

## Solution
I designed a modular, tool-agnostic Quality Engineering intelligence framework that assembles evidence into a **Feature Quality Readiness Score**, separate feature risk assessment, effort and automation ROI estimates, plus a concise coverage recommendation. A single orchestrator, **Quality Engine**, owns tool access: it asks which tools a team uses, connects only those, gathers evidence once and hands the same packet to specialists. The base workflow uses a Coverage Review specialist followed by a QE Analysis specialist. Five additional review skills support deeper analysis when requested.

## What makes the design distinctive

- Separates **readiness** from **risk** so a large but well-planned change is not automatically labeled low quality.
- Distinguishes **Unknown** from **Missing** coverage to prevent fabricated certainty.
- Maps acceptance criteria to actual test evidence instead of relying on label or test counts.
- Uses a published five-dimension rubric rather than opaque scoring.
- Returns both a stakeholder-friendly Jira comment and optional machine-readable contract.
- Asks what the team uses instead of assuming a stack, then lets the person choose between a checklist, a guided walkthrough or a vendor's own setup skill. Every integration (Jira, Xray, mabl, Sentry, Datadog, Honeycomb, Segment and others) is optional with a manual fallback.
- Hands test work to a platform's own skills, for example mabl's, instead of re-implementing them, and avoids connection paths the vendor has retired.
- Keeps tool access in the orchestrator and gives specialists no tools, so analysis cannot cause a write.
- Judges runtime signals against an area's own baseline, not raw counts, and labels each signal observed, correlated or hypothesized.
- Gates every write-back behind profile enablement, in-session confirmation, deduplication and verified success.
- Packages knowledge as portable skills that may later become tool-enabled agents through orchestration.
- Keeps test generation and specialist security, accessibility, incident and metrics reviews outside the default flow unless explicitly requested.

## Architecture

Work item → Quality Engine setup and evidence gathering → Coverage Review → Saved evidence → QE Analysis → Validation → Report and gated write-back.

Optional on-demand paths: Test Planning, Security Review, Accessibility Review, Incident Intelligence and Metrics Intelligence.

## Demonstration sequence

1. Show a fictional user story with acceptance criteria.
2. Run the setup interview and answer "none, I will paste evidence" to show the manual route, then show the connection table for a stack with a few tools.
3. Explain why a test label and raw count cannot prove scenario coverage.
4. Present the evidence-led Coverage Review response.
5. Show QE Analysis calculating its score, identifying risk and explaining automation ROI.
6. Show a clean ticket comment and custom field mapping.
7. Demonstrate a separately requested Security Review or Test Planning skill.
8. Walk through the write-back gates and why the default is read-only.

## Intended outcomes, not unverified claims

Designed to reduce time spent manually assembling planning context, improve consistency in risk conversations, highlight untested behaviors earlier and support transparent prioritization. Measure these outcomes during pilot adoption; do not claim achieved time savings or escape-rate changes without data.

## Suggested measures for a pilot

- Time needed to produce a refinement-ready quality assessment
- Percentage of outputs with cited, verifiable test evidence
- Rate of incorrect coverage classifications found during review
- Human override and correction rate for risk and readiness scores
- Number of actionable acceptance-criteria gaps detected before development
- Stakeholder usefulness rating and maintenance effort

## Public-facing summary

I built **Quality Engine**, an orchestrator plus seven reusable QE specialist skills that helps teams turn requirements, test evidence and runtime signals into meaningful planning decisions. It starts by asking which tools a team uses and connects only those, then combines feature readiness scoring, risk analysis, coverage assessment and automation ROI into a clear review. It is vendor-neutral by design, works with no integrations by pasting evidence, and can run as skills or as agents with governed access to engineering tools.

## Publication guidance

Use a fictional demonstration, disclose which integrations have been tested, provide screenshots only from environments you own or have permission to share, and never publish private tickets or your organization's internal operational data. Select an appropriate license before publishing.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
