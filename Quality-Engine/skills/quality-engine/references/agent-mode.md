# Running Quality Engine as an agent

Quality Engine works as a skill, and each part can also run as an agent. The split stays the same: one orchestrator holds tool access and decisions, and specialists analyze a packet.

## Layout

| Agent | Source | Tool access | Notes |
| --- | --- | --- | --- |
| Quality Engine (orchestrator) | `agents/quality-engine.md` | Whatever the person grants: connectors, CLI, files | Runs setup, gathers evidence, calls specialists, owns write-back |
| `coverage-review`, `qe-analysis`, and the five on-demand specialists | `agents/<name>.md` | Read-only file tools only | Classify from the evidence packet. They never contact trackers, test platforms or chat |

The agent files are generated from the skills by `scripts/build.py`, so skill and agent never drift.

## Why the orchestrator stays on top

- Permissions and credentials live in one place that can be reviewed.
- Specialists cannot be tricked by retrieved text into writing anywhere, because they have no write tools.
- Evidence is gathered once instead of once per agent.

## Adapting to a host

1. Copy the agent files into the host's agent location. In Claude Code that is `.claude/agents/`. Other hosts differ, so follow their documentation.
2. Give the orchestrator only the connectors the profile selected. Leave write tools out until a write-back is enabled.
3. Keep specialists at read-only tools.
4. `qe-analysis` and `qe-planning-test-design` point to a scoring rubric and templates. Place `references/scoring-rubric.md` and the files under `assets/` where the agents can read them, or paste them into the agent's instructions.
5. If the host cannot delegate from the orchestrator to specialists, run the orchestrator at the top level (as the skill, or as the main session) and delegate from there, or paste each specialist's instructions into the orchestrator's context.

## Jira with Rovo

`jira/` contains an optional adapter for Atlassian users: copyable prompts, a comment template and an automation blueprint. It maps onto the same two core steps (coverage review, then analysis) and keeps each response in its own variable before posting.

## Status

The agent definitions are templates generated from the skills. They have not been tested in a live agent host, so verify delegation, permissions and output in a test project first.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
