# AI Risk Assessment — <system name>

**Assessor:** <name>  ·  **Date:** <YYYY-MM-DD>  ·  **Review due:** <YYYY-MM-DD>

## 1. System summary
<Purpose, users, decision it influences, degree of autonomy.>

## 2. Risk register

Score each risk on likelihood (1–5) and impact (1–5). Score = L × I.
Levels: 1–3 low · 4–8 medium · 9–14 high · 15–25 critical.

| Dimension | Risk description | Likelihood | Impact | Score | Level | Mitigation | Owner |
| --- | --- | :-: | :-: | :-: | --- | --- | --- |
| Fairness | <e.g. disparate impact> | | | | | | |
| Privacy | <e.g. re-identification> | | | | | | |
| Safety | <e.g. harmful action> | | | | | | |
| Robustness | <e.g. distribution shift> | | | | | | |
| Transparency | <e.g. unexplained decision> | | | | | | |
| Security | <e.g. prompt injection> | | | | | | |

> Tip: reproduce this register from code with `rai_toolkit.risk.assess([...])`.

## 3. Decision
- [ ] Accept (residual risk within appetite)
- [ ] Mitigate (actions above; re-assess)
- [ ] Escalate (any high/critical residual risk)

## 4. Sign-off
<Name, role, date for each required approver.>
