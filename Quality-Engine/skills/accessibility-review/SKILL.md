---
name: accessibility-review
description: Plan accessibility acceptance criteria and validation for a software feature based on user journeys and UI or content requirements. Use for keyboard, assistive technology, semantics, focus, forms and contrast risks, typically referencing WCAG 2.2 Level AA.
metadata:
  author: Jessica Mosley
  linkedin: https://www.linkedin.com/in/jessmosley/
  github: https://github.com/j-m-o/
---
# Accessibility Review

## Mission
Find access barriers early and translate them into reproducible accessibility verification scenarios. WCAG 2.2 AA is a useful default **review target** when no other agreed standard is specified, not a claim of conformity.

## Procedure
1. Identify users, devices, modalities, UI elements and interaction states.
2. Evaluate likely keyboard and focus behavior, semantic labels, meaningful order, touch targets, error identification, accessible authentication, status messages, contrast and zoom/responsiveness when relevant.
3. Map each suggestion to a user flow and applicable standard criterion when confident.
4. Separate manual assistive-technology checks from automation-friendly checks. A passing scanner does not establish conformance.
5. Identify where design or implementation access is missing, then propose next evidence to collect.

## Output
### Accessibility Scope
<User journeys, platforms and target standard>

### Priority Barriers to Validate
- **<Concern>:** <Who is affected, expected accessible behavior and basis>

### Test Scenarios
- <Keyboard, screen reader, zoom, errors or dynamic updates with observable pass condition>

### Automation and Manual Testing
- **Automated:** <Viable check>
- **Manual:** <Assistive technology or interaction review>

### Open Questions
- <Missing design, platform or interaction detail>

## Boundaries
Never report compliance or an accessibility audit as completed without examination and test evidence. Avoid making assumptions about users based on disability categories.

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*
