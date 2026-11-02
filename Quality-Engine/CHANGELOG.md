# Changelog

## 1.2.1 | November 2, 2026

- Added creator attribution: byline with LinkedIn and GitHub links, a "Why I created this" section, `NOTICE.md`, author metadata in every skill, and a footer on documentation and reference files.
- Reworded two publishing-guidance lines to refer to "your organization".
- Attribution is deliberately absent from reports, assessment templates, sample comments and Rovo prompts, so users' own tickets stay free of it.

## 1.2.0 | November 1, 2026

- Setup is friendlier. Quality Engine first asks which tools you want to continue with, then asks how you want to connect: show me the steps, walk me through it one tool at a time, run the vendor's own setup skill where one exists, or skip and paste evidence.
- Added a plain-language connect guide with per-tool steps, read-only access guidance and a verify step after each connection.
- mabl now uses the mabl CLI and the hosted cloud MCP server only. The local mabl MCP server is not used: mabl's documentation marks it deprecated from May 18, 2026 and retired as of August 25, 2026. Added a mabl reference covering install routes, first-time setup with `mabl-init`, read-only evidence calls and handoff to the skills at `https://github.com/mablhq/skills`.
- Quality Engine now hands test authoring, editing, debugging and impact runs to mabl's own skills instead of describing generic steps. Running a test is treated as an action that needs confirmation.
- Integrations catalog: mabl row re-checked and raised to evidence level `read`. Other rows keep their October 26, 2026 check date.

## 1.1.0 | October 26, 2026

- Quality Engine is now the orchestrator and entry point. It owns setup, tool access, evidence gathering, routing and gated write-back, and calls the seven specialists.
- Added a setup interview that asks which tools a team uses (issue tracker, source control, test platform, test management, error tracking, observability, analytics, incidents, chat) and connects only those, with a manual route for each.
- Added a dated integrations catalog with evidence levels, a profile template that defaults to read-only, an evidence packet contract and write-back gates.
- Added agent definitions generated from the skills, and a build script that produces a self-contained skill, optional standalone specialists and agents from one source.
- Renamed the toolkit and its assessment heading to Quality Engine.

## 1.0.0 | October 26, 2026

- Initial public-facing, vendor-neutral skills release candidate.
- Seven reusable skill folders created.
- Added quality readiness scoring rubric, field contract, Jira comment and Rovo prompt templates.
- Documented preservation of upstream agent responses in Jira automation.
- Created a synthetic example and JSON schema for optional orchestration.
- Test planning derives ownership, dates and product details from the supplied work item instead of fixed defaults.
- Introduced clearer separation between static skills and tool-enabled agents.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
