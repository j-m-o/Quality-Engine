# mabl

Use this file only when the person chose mabl as their test platform. Quality Engine reaches mabl in two ways and no others: the **mabl CLI** and the **hosted (cloud) mabl MCP server**. The local mabl MCP server is not used. mabl's documentation marks it deprecated from May 18, 2026 and retired as of August 25, 2026, and recommends the cloud server.

mabl also publishes agent skills and a plugin at `https://github.com/mablhq/skills`. Prefer them over re-deriving mabl workflows. Quality Engine gathers evidence from mabl and hands test work to those skills. It does not author or run mabl tests itself.

Last checked: November 1, 2026 against the mabl documentation and the `mablhq/skills` repository. Versions and tool names change, so confirm against the repository before relying on them.

## What to install

| Piece | What it is | Needed for |
| --- | --- | --- |
| Hosted `mabl` MCP server | Remote server at `https://mcp.mabl.com/mcp`, sign in with OAuth | Reading tests, plans, runs, impact analysis and quality reports. Needed for Quality Engine evidence |
| mabl CLI | `npm install -g @mablhq/mabl-cli`, then `mabl auth login --auto` once. Needs Node 20 or newer. Check with `mabl auth info` | Running tests from a terminal or CI, and `mabl tests impact`. Optional for read-only evidence |
| mabl plugin or skills | Eight skills: `mabl-init`, `mabl-test-authoring`, `mabl-test-coverage-design`, `mabl-test-edit`, `mabl-version-compare`, `mabl-test-edit-verify`, `mabl-debug`, `mabl-test-impact` | Handing off test design, authoring, debugging and impact work |

The plugin bundles the hosted MCP server entry. Installing only individual skills does not add the server, so add it separately.

Install routes, as documented in the `mablhq/skills` README:

- Claude Code: `/plugin marketplace add mablhq/skills`, then `/plugin install mabl@mabl`.
- Other agents that support skills: `gh skill install mablhq/skills <skill-name>`, then add the hosted MCP server in that host's own MCP settings using the URL above.
- The `mabl-debug` and `mabl-test-coverage-design` skills also use `chrome-devtools-mcp`, which runs a local Chrome helper on the person's machine. That is a different thing from the retired local mabl MCP server. Mention it only if they plan to use those two skills.

## First-time setup

Offer the person the mabl setup skill rather than collecting workspace details by hand: run `mabl-init`. It signs in through the hosted server, lists workspaces, applications and environments, asks the few choices only the person can make, and saves the result where they choose. Afterwards, record in the profile only the vendor and status. Workspace, application and environment choices belong to `mabl-init`'s own output.

## Verify the connection

Connected means a read call succeeded. In order:

1. Call the hosted server's `get_current_user`. If it returns a user, the cloud route works.
2. Call `list_mabl_workspaces`. Confirm the workspace the person expects.
3. Only if CLI use was requested: run `mabl auth info`. If runs fail while the server calls work, authentication on the CLI side is the usual cause. Fix with `mabl auth login --auto`.

Report each route separately in the connection table, for example "mabl cloud MCP: Connected (read verified); mabl CLI: Available, not connected".

## Evidence Quality Engine reads from mabl

Read-only calls on the hosted server, per the tool names the `mablhq/skills` plugin allows:

| Evidence | Tool to try | Goes into the packet as |
| --- | --- | --- |
| Tests that cover a change | `analyze_test_impact`, `search_mabl_tests`, `list_mabl_tests` | Coverage, with the query and its status |
| Test steps, to match assertions to acceptance criteria | `get_mabl_test_steps` | Coverage evidence for a specific criterion |
| Plans that include those tests | `list_mabl_plans`, `get_mabl_plan` | Coverage and regression context |
| Recent results | `list_mabl_test_runs`, `get_mabl_test_run`, `get_mabl_test_run_failure_reason` | Health |
| Test quality | `get_test_quality_report` | Health |

If a tool name is missing or errors, say which one failed, set `search_status: failed` and carry on with Unknown coverage. Do not guess a test exists.

When mabl is the only coverage source, say so in the confidence line. Tests mapped by mabl impact analysis are candidates to review, not proof that an acceptance criterion is verified.

## Handing off instead of doing

| Quality Engine recommendation | Hand off to |
| --- | --- |
| Add targeted tests | `mabl-test-coverage-design` to decide what to cover, then `mabl-test-authoring` to build |
| Update existing | `mabl-test-edit`, then `mabl-test-edit-verify` |
| Expand regression coverage | `mabl-test-impact` to pick and run the impacted set |
| Investigate a failing test | `mabl-debug` |

Running a test consumes cloud execution and is an action, not evidence gathering. Quality Engine only offers it, and runs it after the person confirms in the session. Use the cloud run path. Do not use `run_mabl_test_local`: it only produces a launcher link for a person to watch a browser run, returns no status or results, and belongs to the local path this skill avoids.

If the `mablhq/skills` plugin is installed, call its skills by name. If it is not, tell the person the handoff skill is missing and show the install line from above, then fall back to producing a test plan with `qe-planning-test-design`.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
