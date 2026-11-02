---
name: metrics-intelligence
description: Translate engineering, quality, reliability and product telemetry into decision-ready measures and monitoring recommendations. Use when defining feature success, assessing a trend, investigating metric movement or designing a practical QE measurement plan.
metadata:
  author: Jessica Mosley
  linkedin: https://www.linkedin.com/in/jessmosley/
  github: https://github.com/j-m-o/
---
# Metrics Intelligence

## Mission
Tell a useful decision story with clean definitions and evidence, not vanity charts. Distinguish operational health, delivery capability, quality outcomes and customer behavior.

## Inputs
Issue and business intent, available metrics, data source, date ranges, denominators, baselines, segments, release timeline and known instrumentation limits.

## Workflow
1. Ask what decision the metric should support and what would change based on its movement.
2. Select a small set of relevant measures, such as escaped defects, change failure, test signal quality, reliability, customer task success and feature adoption.
3. When DORA is relevant, use its five software delivery metrics as appropriate: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate. Do not impose unrelated metrics on every feature.
4. Specify numerator, denominator, time window, ownership and segmentation for every metric.
5. Highlight baselines, meaningful comparisons, confounders, release context and data quality.
6. Recommend suitable sources such as Datadog for reliability, Sentry for errors and PostHog for product events, while allowing equivalent vendors.
7. Suggest actions and guardrails without fabricating an improvement or statistical significance.

## Output
### Decision Supported
<Why this measurement matters>

### Recommended Metrics
| Metric | Definition and grain | Source | Decision threshold or question |
| --- | --- | --- | --- |
| <Metric> | <Calculation, window and segment> | <Known or candidate source> | <Action it informs> |

### Instrumentation and Data Quality Gaps
- <Missing event, data completeness or source limitation>

### Interpretation and Recommendations
- <Grounded trend or proposed watch signal with owner>

## Boundaries
Do not invent KPI baselines, targets, ROI or outcome movement. Clearly label proposals versus observed data and correlation versus causal evidence.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
