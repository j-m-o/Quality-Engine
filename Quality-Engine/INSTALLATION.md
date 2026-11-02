# Installing or adapting Quality Engine

## Recommended: one self-contained skill

`dist/quality-engine.skill` is the orchestrator with all seven specialists bundled under `references/specialists/`. Install that one file in an assistant that supports skills, following the host's own instructions. Quality Engine reads the bundled specialist instructions when it needs them, so nothing else has to be installed.

Generate it from source:

```bash
python scripts/build.py
```

The folders under `skills/` are the source of truth. The build derives every artifact in `dist/` from them and fails on any broken internal reference.

## Specialists on their own

`dist/specialists/*.skill` installs any specialist by itself. If a skill with a specialist's name is installed, Quality Engine calls it directly; otherwise it uses its bundled copy. Installing both is harmless but redundant, so pick one source per specialist to avoid maintaining two.

## As agents

`dist/agents/*.md` holds an agent definition for the orchestrator and for each specialist. Specialists get read-only file tools and work only from the evidence packet. The orchestrator inherits whatever tools you grant. Read [agent mode](skills/quality-engine/references/agent-mode.md) for placement and permissions. These definitions are generated templates and have not been tested in a live agent host.

## Connecting your tools

Quality Engine asks which tools you want to continue with, then either shows you the steps for each or walks you through them. You can also skip and paste evidence. The steps are in the [connect guide](skills/quality-engine/references/connect-guide.md). Connections are made with your host's connectors, a vendor's official MCP server, a CLI, or environment variables for credentials. Credentials never go in the profile, a comment or a report. mabl is the one exception that needs software installed on your side: the mabl plugin or skills from `https://github.com/mablhq/skills`, the hosted MCP server, and optionally the mabl CLI. See the [mabl reference](skills/quality-engine/references/mabl.md). See the [integrations catalog](skills/quality-engine/references/integrations-catalog.md) for what was checked and when.

## Saving your setup

A skill cannot store its own settings. Save the profile Quality Engine produces as `quality-engine.profile.yaml` in your repository root, or as `references/profile.yaml` inside your copy of the skill. Start from `skills/quality-engine/assets/profile-template.yaml`. It defaults to read-only.

## Generic model or custom assistant

If your assistant cannot import skills, paste `skills/quality-engine/SKILL.md` into its instructions and supply the referenced files separately. It will not gain tracker or test-platform access from the text alone; it needs its own connectors or actions.

## Jira and Rovo

Atlassian users can also use the optional adapter under `jira/`. A Rovo agent does not gain a skill because a `SKILL.md` exists. Configure a dedicated agent using the relevant instructions, supply authorized tools, and follow `jira/automation-blueprint.md`. Save the coverage output into `coverageResponse` before running the analysis, save the analysis into `qeAnalysisResponse`, and add the comment through the automation rule. Test read-only operation and formatting before considering field writes.

## Portfolio demo path

Use only the synthetic `examples/` folder. Record a read-only demo, and disclose exactly which integrations are live and which are simulated. Before public publication, choose a license and complete `RELEASE-CHECKLIST.md`.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
