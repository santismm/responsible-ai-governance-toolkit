---
id: "GOV-004"
slug: "agentic-ai-governance-checklist"
title: "Agentic AI Governance Checklist"
type: "governance"
frameworks: ["EU AI Act", "ISO/IEC 42001", "NIST AI RMF"]
evidence_level: "industry_observation"
source: "https://santismm.com/en/governance/agentic-ai-governance-checklist"
---
# GOV-004 — Agentic AI Governance Checklist

> Evidence: industry_observation · Confidence: medium · Source: industry_observation, personal_experience

Canonical: https://santismm.com/en/governance/agentic-ai-governance-checklist

A practical, vendor-neutral checklist for governing agentic AI in the enterprise — translating the principles of the EU AI Act, ISO/IEC 42001 and NIST AI RMF into concrete controls you can implement in a harness. It covers human oversight, guardrails, audit logging, evaluation, access control, prompt-injection defence and incident response, and maps each control to the patterns and knowledge units that operationalize it. Use it as a readiness gate before letting an agent act in production.

## Definition

The agentic AI governance checklist is an operational control set that turns AI governance frameworks into concrete, implementable requirements for autonomous agents acting in production.

## Scope

Teams building or deploying autonomous or semi-autonomous agents that use tools, act on systems, or make consequential decisions. It is a practical companion to the formal frameworks, not a substitute for legal advice.

## Key requirements

- Human oversight by risk: gate high-impact, irreversible or regulated actions for human approval.
- Guardrails on inputs and outputs, including prompt-injection and PII defence.
- Full audit logging and observability so every action is traceable.
- Evaluation before and after deployment, against a maintained eval set.
- Least-privilege access for tools and data the agent can reach.
- A defined incident response and kill-switch for agents in production.

## Controls

- Human approval gates: Route high-impact actions through a human checkpoint (EU AI Act Art. 14). Implements the human-approval-gate pattern.
- Guardrails: Validate and constrain inputs and outputs; defend against prompt injection and block out-of-policy actions.
- Audit logging & observability: Trace every decision, tool call and action so the agent is reviewable and incidents are reconstructable.
- Evaluation harness: Score behaviour against an eval set before shipping and monitor for regressions after — NIST 'Measure'.
- Least-privilege access: Scope the tools, data and permissions an agent can reach to the minimum its task requires.
- Incident response & kill-switch: Define how to detect, stop and remediate a misbehaving agent, including a way to halt it immediately.

## Checklist

- Classify the agent's risk and identify which actions need human approval.
- Implement guardrails for inputs/outputs and prompt-injection defence.
- Enable end-to-end audit logging and observability.
- Stand up an evaluation set and run it pre-deployment and continuously.
- Apply least-privilege scoping to tools, data and credentials.
- Define incident response, monitoring thresholds and a kill-switch.
- Map each control to your obligations under the EU AI Act, ISO 42001 and NIST AI RMF.
- Document ownership and review the agent on a schedule.

## Common pitfalls

- Granting an agent broad tool/data access 'to be safe', creating a large blast radius.
- Gating everything (approval fatigue) or nothing (no oversight) instead of gating by risk.
- Shipping without an eval set, so quality and safety are unmeasured.
- No kill-switch or incident plan when an agent misbehaves in production.
- Ignoring prompt injection as an attack surface for tool-using agents.

## FAQs

**Is this a substitute for the EU AI Act or ISO 42001?**

No. It is a practical control set that operationalizes their principles for agents. Use it alongside the formal frameworks and legal advice, not instead of them.

**Which control matters most for autonomous agents?**

Risk-based human oversight plus least-privilege access and audit logging — together they bound what an agent can do and make every action accountable.

**How does it connect to the patterns library?**

Each control maps to patterns that implement it — human-approval-gate for oversight, reflection and evaluator-optimizer for quality — and to knowledge units like guardrails and AI observability.
