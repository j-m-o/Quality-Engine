# Connect guide

Plain-language steps for connecting each tool. Use it after the person has said which tools they want, and has chosen how they want to proceed (see `setup-interview.md`).

Three ways to proceed. Offer them in this order:

- **Show me the steps.** Give a short checklist for every selected tool at once, then ask them to say "done" for each. Quality Engine then verifies with a read call.
- **Walk me through it.** Do one tool at a time: say what it is for and what Quality Engine will read, give the single next action, wait, verify, report, move on.
- **Use the vendor's own setup skill.** Where a vendor publishes a skill that sets itself up, tell the person to run it, then come back and Quality Engine verifies. Today the only one confirmed is `mabl-init` (see `mabl.md`). Do not promise one for any other vendor.

At any point the person can say "skip" for a tool. Mark it Manual and use pasted evidence.

## Rules for every tool

- Say in one sentence what Quality Engine will read from the tool and that it reads only.
- Ask for the narrowest access the vendor offers. Prefer a read-only scope or role. Do not ask for write access during setup. Write-back is a separate choice made later.
- Sign in through the host's connector prompt, the vendor's OAuth page, or an environment variable. Never ask the person to paste a token or password into chat, and never put one in the profile.
- After each step, verify with one read call and report the result in the connection table. A tool is not Connected until that call has succeeded.
- If the host cannot add connectors or MCP servers, say so and offer the manual route. Do not suggest workarounds that bypass the host's permissions.
- Do not state a tool name, endpoint or scope that this guide or the catalog does not give. If it is missing, send the person to the vendor's documentation and ask them to paste what they find.

## Checklist template

Use this for any tool, including ones without a section below:

1. Check whether it is already connected in your host (look for it in the connector or MCP list).
2. If not, find the vendor's official MCP server or skill in the vendor's documentation. Prefer official over community, and tell me which you found.
3. Add it in your host's connector or MCP settings and sign in. Choose read-only access where offered.
4. Tell me when done. I will make one read call and report the result.
5. If it will not connect, say "manual". You paste an export or query result and we continue.

## mabl

Read `mabl.md` for the full detail. The short version:

1. Install the mabl plugin: in Claude Code, `/plugin marketplace add mablhq/skills` then `/plugin install mabl@mabl`. In another host, install the skills with `gh skill install mablhq/skills <skill-name>` and add the hosted MCP server `https://mcp.mabl.com/mcp` in the host's MCP settings.
2. Sign in to the hosted server when prompted (OAuth).
3. Run `mabl-init` once. It finds your workspace, applications and environments.
4. Only if you want to run tests from a terminal or CI: `npm install -g @mablhq/mabl-cli`, then `mabl auth login --auto` once. Needs Node 20 or newer.
5. Tell me when done. I will call the server's `get_current_user` and `list_mabl_workspaces`, and `mabl auth info` if you set up the CLI.

mabl runs through the CLI and the cloud server only. The local mabl MCP server is retired and is not used.

## Jira and Confluence (Atlassian)

1. Add the Atlassian Rovo MCP server in your host: remote endpoint `https://mcp.atlassian.com/v2/mcp`.
2. Sign in with your Atlassian account and choose the site and products to allow. Read access is enough to start.
3. Tell me the project key to use. I will search for one work item to confirm a read works.

If your admin restricts the server, ask them to allow it. Atlassian documents site-level controls.

## Honeycomb

1. Add Honeycomb's MCP server in your host and sign in with OAuth, or use an API key through an environment variable.
2. Choose the read-only scopes. Most tools are read-only. Write tools need the `mcp:write` scope, which you do not need.
3. Tell me the environment and the dataset or service names for the modules you care about.
4. I will run one read query to confirm.

## Sentry and Datadog

Both vendors document an official MCP server. This guide has not read their setup pages, so follow the vendor's own current instructions.

1. Open the vendor's MCP documentation (the catalog lists where).
2. Add the server in your host and sign in. Choose read-only access, and confirm your plan includes it.
3. Tell me the project or service names that belong to each module.
4. I will run one read query for recent errors or latency and report the window and the baseline.

## GitHub and GitLab

1. If the `gh` CLI is installed and signed in (`gh auth status`), that is enough for read access to issues and pull requests. For GitLab use the `glab` CLI the same way.
2. Otherwise add the vendor's MCP server in your host if it offers one, or choose manual.
3. Tell me the repository. I will read one pull request or issue to confirm.

## Xray and TestRail

No official MCP server was confirmed for either at the last check.

1. If you use a community server, review who maintains it before adding it. I will tell you it is community.
2. For the Xray Cloud API, set client credentials as environment variables. Never paste them in chat or the profile.
3. Or choose manual: export your test cases and execution results and paste them.

## Segment

The Twilio MCP server covers Segment documentation, not your event data. Connecting it will not give Quality Engine usage numbers. For real data, point to your warehouse or paste an export. Say this plainly before the person spends time connecting it.

## Playwright, Cypress and Selenium

Nothing to connect. Point me to the test directory in the repository and the CI results. Coverage inferred from test files is weaker than a platform that maps tests to requirements, and I will say so.

## After connecting

Show the connection table. Offer to save the profile. Offer to run the quickstart assessment on a real work item. Tell the person which tools are Manual and what to paste for each.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
