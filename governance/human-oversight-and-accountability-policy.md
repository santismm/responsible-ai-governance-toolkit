---
id: "GOV-007"
slug: "human-oversight-and-accountability-policy"
title: "Human Oversight and Accountability Policy"
type: "governance"
frameworks: ["EU AI Act"]
evidence_level: "industry_observation"
source: "https://santismm.com/en/governance/human-oversight-and-accountability-policy"
---
# GOV-007 — Human Oversight and Accountability Policy

> Evidence: industry_observation · Confidence: high · Source: industry_observation, paper

Canonical: https://santismm.com/en/governance/human-oversight-and-accountability-policy

An operational policy that turns EU AI Act Article 14 human oversight into practice for agentic AI. It assigns a named accountable owner per agent, sets the oversight level (in-the-loop, on-the-loop, out-of-the-loop) by risk, and defines intervention, override and stop authority plus escalation paths. It requires overseers to be competent and have time to act, and it guards against rubber-stamping and automation bias. It exists to prevent two failures: the absent human and the token human who cannot actually understand, override, or answer for what the agent does.

## Definition

A human oversight and accountability policy is a binding rule set that assigns a named human to be answerable for each agent and guarantees a competent person can understand, intervene in, and stop its actions.

## Scope

Every production or pilot agent that uses tools, acts on systems, or makes consequential decisions, and the system owners, approvers and operators who oversee them. It operationalizes Article 14; it is not a substitute for legal advice.

## Key requirements

- Each agent has one named, accountable owner — accountability is never transferred to the model.
- Oversight level is matched to risk: in-the-loop for high-impact or irreversible actions, on-the-loop for reversible high-volume actions, out-of-the-loop only for low-risk reversible tasks.
- Every agent exposes tested reject, modify and stop (kill-switch) controls with the context needed for an informed decision.
- Escalation thresholds route consequential decisions to humans by impact, irreversibility, rights or safety, confidence and novelty.
- Overseers must be competent, intelligibly informed, and have genuine authority and time to act.
- Automation bias and rubber-stamping are actively countered, not assumed away.

## Controls

- Named accountable owner: Assign one human answerable for each agent's outcomes. 'The model decided' is not an acceptable account.
- Risk-matched oversight level: Define in-the-loop, on-the-loop or out-of-the-loop per agent based on action impact and reversibility. Implements the human-approval-gate pattern for high-impact actions.
- Override and stop authority: Expose tested reject, modify and stop controls; surface enough context for an informed override. The stop must be fast and reachable.
- Escalation thresholds: Route decisions to humans when impact, irreversibility, rights/safety, low confidence or novelty thresholds are crossed. Implements the human-escalation pattern.
- Overseer competence: Train and certify overseers on the agent's domain and limits so oversight is meaningful, not nominal.
- Anti-rubber-stamping safeguards: Throttle and require justification for approvals; monitor approval time and override rates to detect automation bias.

## Checklist

- Name one accountable owner for each production agent and record it.
- Classify each agent's actions by impact and reversibility and assign an oversight level.
- Implement and test reject, modify and stop (kill-switch) controls for every agent.
- Ensure the agent surfaces intelligible context for any decision that needs oversight.
- Define and configure escalation thresholds for impact, rights/safety, confidence and novelty.
- Train overseers on the agent's domain and limits and keep their certification current.
- Add anti-rubber-stamping safeguards and monitor approval time and override rates.
- Log every approval and override with actor, reason and timestamp, and review thresholds on a schedule.

## Common pitfalls

- Token oversight: a human clicks approve without the context, authority or time to actually evaluate the action.
- Automation bias: approvers trust the agent so much they stop scrutinizing its output.
- Diffuse accountability: no single named owner, so a failure has no answerable human.
- Unreachable override: a stop control that is slow, hidden or never tested.
- Threshold drift: escalation limits set once and never updated as the agent's scope grows.

## FAQs

**Does human oversight mean a human approves everything?**

No. Oversight is tiered: in-the-loop for high-impact or irreversible actions, on-the-loop monitoring for reversible high-volume actions, and a human-in-command posture overall. The model scales to risk so oversight stays meaningful instead of becoming approval fatigue.

**Can accountability sit with the AI vendor?**

No. Vendor relationships are governed separately, but your named system owner remains accountable for how the agent is deployed and used. Automation is a tool, not a defense.

**How do we prevent rubber-stamping and automation bias?**

Surface intelligible context for each decision, throttle and require justification for approvals, monitor approval time and override rates, and keep overseers competent through training and rotation.
