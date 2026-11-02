# Integrations catalog

**Last checked: November 1, 2026** for the mabl row. Every other row was last checked October 26, 2026. This list ages quickly. Treat it as a starting point, and verify live before telling anyone a connector exists or is safe to use. Quality Engine works with none of these; every row has a manual route.

## Where to go next

To help a person connect a tool, use `connect-guide.md`. For mabl, use `mabl.md`.

## Discovery order

For each tool the person selected, try these in order and stop at the first that works:

1. **Already loaded.** Search the session's available tools for the vendor name. If a read call succeeds, it is Connected.
2. **Host connector list.** If the host can list or search connectors, use it. Connector suggestions can be switched off in the host's settings; if a search returns nothing or says it is disabled, that is not evidence the connector does not exist. Move on.
3. **Vendor's official MCP server or skill.** Find the vendor's own documentation. Prefer an official server over a community one, and say which it is.
4. **CLI or API.** A vendor CLI that is already installed, or an API reachable with credentials supplied through environment variables.
5. **Manual.** Ask the person to paste an export, a screenshot's text, a query result or a file.

Never mark a tool Connected until a read call has succeeded. Never accept credentials pasted into chat to store; use connector auth or environment variables.

## Evidence levels

| Level | Meaning |
| --- | --- |
| read | Official page was read during the last check |
| found | Official documentation page was located, content not read |
| community | Only community or third-party servers were found; official support not confirmed |
| own-use | From the author's own prior use; not re-verified |
| unchecked | Not researched; run discovery |

## Issue trackers and source control

| Tool | Connect route | Level | Notes |
| --- | --- | --- | --- |
| Jira, Confluence (Atlassian) | Atlassian Rovo MCP server, remote endpoint `https://mcp.atlassian.com/v2/mcp` | read | Read, write and delete permissions are controllable; site and space data policies exist. Authentication details are in Atlassian's install guide |
| Linear | Check Linear's documentation | unchecked | Official page could not be fetched at last check |
| Azure DevOps, Shortcut | Check vendor documentation | unchecked | |
| GitHub (issues, PRs, code) | Check GitHub's documentation, or the `gh` CLI if installed | unchecked | Official page could not be fetched at last check |
| GitLab, Bitbucket | Check vendor documentation, or the vendor CLI | unchecked | |

## Test platforms and test management

| Tool | Connect route | Level | Notes |
| --- | --- | --- | --- |
| mabl | Hosted cloud MCP server `https://mcp.mabl.com/mcp` (OAuth) and the mabl CLI (`@mablhq/mabl-cli`). Skills and plugin at `https://github.com/mablhq/skills`. Details in `mabl.md` | read | The local mabl MCP server is deprecated (May 18, 2026) and retired (August 25, 2026) per mabl's documentation. Do not use it. Cloud server tool names were read from the `mablhq/skills` repository, not from a live session |
| Playwright, Cypress, Selenium | No connector needed: read test files from the repository and results from CI | n/a | Coverage is inferred from test files and results, so confidence is lower than with a platform that maps tests to requirements |
| Xray | Community MCP servers exist; Xray Cloud API with client credentials in environment variables | community, own-use | No official MCP server confirmed. Do not store client credentials in a profile |
| TestRail | Community listing only | community | No official MCP server confirmed |
| Zephyr, qTest | Check vendor documentation | unchecked | |

## Error tracking and observability

| Tool | Connect route | Level | Notes |
| --- | --- | --- | --- |
| Sentry | Sentry's official MCP server (documentation page redirects to `mcp.sentry.dev`) | found | Content not read at last check; confirm auth and scopes |
| Datadog | Datadog's official MCP Server documentation under `docs.datadoghq.com/bits_ai/mcp_server/` | found | Page could not be fetched at last check; confirm availability and toolsets for your plan |
| Honeycomb | Honeycomb MCP, OAuth or API key | read | Most tools are read-only; write tools need the `mcp:write` scope. Plan requirements are not stated on the page |
| New Relic, Grafana, Dynatrace, Splunk | Check vendor documentation | unchecked | |
| Rollbar, Bugsnag | Check vendor documentation | unchecked | |

## Product analytics and incidents

| Tool | Connect route | Level | Notes |
| --- | --- | --- | --- |
| Segment | Twilio's hosted MCP at `mcp.twilio.com/docs` | read | **Documentation search only, read-only.** It indexes Segment docs, not your event data. For data, use your warehouse or an export, and paste or connect that instead |
| PostHog, Amplitude, Mixpanel | Check vendor documentation | unchecked | |
| PagerDuty, Opsgenie, incident.io, Statuspage | Check vendor documentation | unchecked | |
| Slack, Microsoft Teams | Check the host's connector list | unchecked | Needed only for notifications |

## Manual routes that always work

- **Tracker:** paste the work item text, acceptance criteria and links.
- **Source control:** paste the PR description and diff summary.
- **Tests:** paste the test list with names, IDs and last results, or point to the test directory.
- **Runtime signals:** paste a saved query result with its time window and the comparison baseline.
- **Incidents:** paste the relevant postmortem excerpts or defect list with identifiers and dates.

## Adding or updating a vendor

Add a row with the official documentation link, the connect route, the evidence level, the date you checked, and any scope or plan limits. If only a community server exists, say so in the notes. Do not describe a connector's tools from memory.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
