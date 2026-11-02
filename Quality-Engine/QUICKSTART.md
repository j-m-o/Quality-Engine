# Quickstart: one ticket, no integrations, one decision-ready answer

You do not need to connect anything to try Quality Engine. The fictional example below is self-contained.

## Try it with the bundled skill

1. Install `dist/quality-engine.skill` in an assistant that supports skills. If you only have the repository, run `python scripts/build.py` first.
2. Open `examples/sample-ticket.md` and paste it into the chat, including the synthetic test inventory at the bottom.
3. Ask:

```text
Run Quality Engine on this ticket. I have no integrations connected, so use only what I pasted.
```

4. When it offers the setup interview, answer **None, I will paste evidence**. This shows the manual route.
5. Compare the result with `examples/sample-assessment.json` and `examples/sample-jira-comment.md`. The example numbers are illustrative, not targets.

## Then connect your own tools

Run the setup interview again and choose the tools you actually use. Then pick how you want to connect: the steps for each tool, a one-at-a-time walkthrough, or the vendor's own setup skill. Quality Engine checks for an existing connector, then the vendor's official MCP server or skill, then a CLI or API, then falls back to paste. It reports each tool as Connected (read verified), Available but not connected, or Manual. Save the profile it produces as `quality-engine.profile.yaml` next to your code.

## If you use mabl

Say so in the setup interview. Quality Engine uses the mabl CLI and the hosted cloud MCP server only, and hands test design and authoring to mabl's own skills. The quickest start is to install the mabl plugin from `https://github.com/mablhq/skills` and run `mabl-init` once. Details are in [the mabl reference](skills/quality-engine/references/mabl.md).

## Fast standalone requests

Specialists can be used directly when you already have the evidence.

```text
Assess the attached feature ticket using the QE Analysis skill. Include the six standard fields, scored criteria, risk rationale, evidence, gaps, recommended test strategy and final recommendation. Treat missing coverage evidence as Unknown. Do not invent metrics or test counts.
```

```text
Using the attached ticket and the existing assessment, apply the Security Review skill. Return security-sensitive user paths, test conditions, open questions and a prioritized verification plan. Do not edit the ticket or invent a finding.
```

## Definition of a successful trial

- Quality Engine asks what you use before assuming a vendor.
- The skill separates known, inferred and unknown findings.
- Scores can be traced to documented weights and evidence.
- Existing tests are named only if the evidence contains them.
- Anything that could not be checked is shown as not verified, not as zero.
- Nothing is written anywhere unless you enabled and confirmed it.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
