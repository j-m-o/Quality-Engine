# Setup interview

Purpose: find out which tools this team actually uses so Quality Engine connects only those, then help them connect in the way they prefer. Asking first avoids two failures: assuming a vendor the team does not have, and silently skipping one they do.

## Opening line

Start with one sentence the person can act on, for example:

> I can work with nothing connected, or pull evidence from the tools you use. Tell me which ones to continue with and I will either show you what to do or walk you through it.

## How to ask

- Use the host's multiple-choice question tool if it has one. Otherwise send a short numbered list and accept free text.
- Ask at most four tool questions, each multi-select, then one question on how to proceed. Every tool question includes **None, I will paste evidence** and an **Other** write-in.
- Skip a question whose category cannot matter for what the person asked. A quick risk check on one bug does not need chat or analytics.
- Never preselect a vendor. Order options alphabetically or by category, not by preference.
- Accept "same as last time" if a profile exists.

## Step 1: Which tools do you want to continue with?

### Question 1: Work and code

Which of these hold your work items and code changes?

- Issue tracker: Azure DevOps, GitHub Issues, Jira, Linear, Shortcut
- Source control and pull requests: Bitbucket, GitHub, GitLab
- CI results: CircleCI, GitHub Actions, GitLab CI, Jenkins
- None, I will paste evidence

### Question 2: Tests

Where do your tests live and run, and where are they tracked?

- Test platform or framework: Cypress, mabl, Playwright, Selenium, or another
- Test management: TestRail, Xray, Zephyr, qTest, or none
- None, I will paste evidence

If the person picks mabl, tell them in one line that Quality Engine reaches it through the mabl CLI and the hosted cloud MCP server only, using mabl's own skills at `https://github.com/mablhq/skills`. See `mabl.md`.

### Question 3: Runtime signals

Which of these tell you how production behaves?

- Error tracking: Bugsnag, Rollbar, Sentry
- Observability and APM: Datadog, Dynatrace, Grafana, Honeycomb, New Relic, Splunk
- Product analytics: Amplitude, Mixpanel, PostHog, Segment
- Incident management: incident.io, Opsgenie, PagerDuty, Statuspage
- None, I will paste evidence

### Question 4: Communication and write-back

Where should results go, and what may Quality Engine write?

- Chat: Microsoft Teams, Slack
- Allowed write-backs (default none): comment on the work item, update work item fields, post to chat, link or upload to test management, comment on the pull request
- None, keep it read-only

## Step 2: How do you want to connect them?

Ask once, single choice, after the tool answers are in:

- **Show me what I need to do.** One checklist per selected tool, then say "done".
- **Walk me through it.** One tool at a time, with a check after each.
- **Run the vendor's own setup skill** where one exists. Offer this only for tools where `connect-guide.md` names one.
- **Skip for now.** Use pasted evidence.

Explain the trade-off in a line: the checklist is faster if you are comfortable in your host's settings; the walkthrough is slower but checks each step.

## Step 3: Connect and verify

1. For each selected tool, run discovery from `integrations-catalog.md` first. Something may already be connected, which saves the person work.
2. Follow `connect-guide.md` in the style the person chose. For mabl, follow `mabl.md`.
3. Ask only for what discovery could not resolve: a project or workspace name, the field that holds the product or module, or the module-to-service mapping if runtime signals are connected.
4. Show the connection table, then the profile, then the one-line instruction to save it.
5. If a connection fails twice, offer the manual route rather than looping.

## Connection table format

```text
Tool            Category          Status                          Next step
Jira            Issue tracker     Connected (read verified)       none
mabl (cloud)    Test platform     Connected (read verified)       none
mabl (CLI)      Test platform     Available, not connected        npm install -g @mablhq/mabl-cli, then mabl auth login --auto
Sentry          Error tracking    Available, not connected        Add the vendor's official MCP server
Xray            Test management   Manual                          Paste test cases or export; or supply API access via environment variables
```

Status values are exactly: **Connected (read verified)**, **Available, not connected**, **Manual**. Do not mark Connected from the presence of a tool name alone.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
