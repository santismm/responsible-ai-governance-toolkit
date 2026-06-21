---
id: "GOV-006"
slug: "audit-framework-for-agentic-systems"
title: "Audit Framework for Agentic Systems"
type: "governance"
frameworks: ["ISO/IEC 42001", "NIST AI RMF"]
evidence_level: "industry_observation"
source: "https://santismm.com/en/governance/audit-framework-for-agentic-systems"
---
# GOV-006 — Audit Framework for Agentic Systems

> Evidence: industry_observation · Confidence: medium · Source: industry_observation, paper

Canonical: https://santismm.com/en/governance/audit-framework-for-agentic-systems

A practical, vendor-neutral framework for making an agent auditable and for auditing it. It defines the evidence an independent reviewer needs — immutable, correlated traces of every decision and tool call, model and version provenance, evaluation reports, approval and incident records — and how to test controls and sample high-volume runs. Each evidence type maps to ISO/IEC 42001 and NIST AI RMF so an auditor can verify the agent stayed within its governed bounds. Use it to design auditability in from the start, not as an afterthought.

## Definition

An agent audit is an independent, evidence-based examination that determines whether an agentic system operated within its authorized scope, controls and policies over a defined period, and whether the governance claims made about it are supported by reliable evidence.

## Scope

Auditors, assurance and risk teams, and the system owners who must make their agents auditable by design. It applies to autonomous or semi-autonomous agents that use tools and act over time, and supports both internal assurance and external or regulatory audit. It is a practical companion to the formal frameworks, not a substitute for legal advice.

## Key requirements

- Auditability by design: the agent must emit enough structured evidence at runtime to reconstruct any run later.
- Every run produces an immutable, correlated trace: goal, each step and tool call with parameters and results, approvals, overrides and outcome.
- Evidence must be complete, attributable, time-stamped and tamper-evident to hold evidentiary value.
- Model and version provenance (prompt, tools, model) is captured per run so behaviour is tied to a known configuration.
- Sampling is layered: risk-stratified, statistical, and 100% review of all exceptions, overrides, denials and incidents.
- Audit evidence maps to ISO/IEC 42001 internal audit (Clause 9) and NIST AI RMF Measure and Manage functions.

## Controls

- Immutable audit logs and traceability: Capture a correlated trace per run — agent identity and version, goal, each step, tool call, result, approvals and outcome — and protect it against alteration. Implements AI observability.
- Model and version provenance: Record the exact prompt, tool set and model version behind each run so behaviour is attributable to a known, reproducible-by-config baseline.
- Evaluation evidence: Retain pre-deployment and ongoing evaluation reports and gate results so the auditor can verify safety and quality were measured — NIST 'Measure'.
- Control testing and sampling: Test each control against evidence using a documented sampling methodology: risk-stratified, statistical, and full exception review.
- Approval and incident records: Capture human approvals, overrides and incidents with actor identity and timestamps. Implements the human-approval-gate pattern.
- Attestations and findings management: System and control owners sign attestations backed by evidence; findings are tracked to closure with severity and deadlines.

## Checklist

- Confirm every agent run produces a complete, correlated trace tied by a stable trace ID.
- Verify logs are tamper-evident, time-stamped and retained for the full audit and regulatory window.
- Check that each run records model and version provenance (prompt, tools, model version).
- Retrieve a control mapping / Statement of Applicability linking each control to its evidence.
- Retain and review pre-deployment and ongoing evaluation reports and gate outcomes.
- Confirm approval, override and incident records exist with actor identity and timestamps.
- Apply a documented sampling methodology — risk-stratified, statistical, and 100% exception coverage.
- Track findings to closure with severity and deadlines, and collect signed owner attestations.

## Common pitfalls

- Non-auditable agents: logging added as an afterthought, leaving gaps no audit can fill.
- Mutable logs: records that could be altered, destroying their evidentiary value.
- Sampling blind spots: random-only sampling that misses rare but catastrophic actions.
- Attestation without evidence: owners signing off on controls they cannot demonstrate.
- Findings graveyard: issues raised but never remediated or re-tested.

## FAQs

**Can you audit a non-deterministic agent at all?**

Yes — you audit the controls and the recorded behaviour, not the determinism. Complete, immutable traces make any specific run reconstructable even if it cannot be reproduced exactly.

**How big should the audit sample be?**

Large enough for your target assurance level statistically, plus 100% of exceptions and high-impact actions. Sampling never replaces full exception review.

**How does audit evidence map to the frameworks?**

Traces and logs support NIST AI RMF Measure and Manage and ISO/IEC 42001 Clause 9 internal audit; a control mapping or Statement of Applicability links each control to the evidence that proves it operated.
