---
id: "GOV-001"
slug: "eu-ai-act"
title: "EU AI Act"
type: "governance"
frameworks: ["EU AI Act"]
evidence_level: "industry_observation"
source: "https://santismm.com/en/governance/eu-ai-act"
---
# GOV-001 — EU AI Act

> Evidence: industry_observation · Confidence: high · Source: paper, industry_observation

Canonical: https://santismm.com/en/governance/eu-ai-act

The EU AI Act is the European Union's comprehensive, risk-based law for artificial intelligence. It sorts AI systems into risk tiers — unacceptable (banned), high-risk (strict obligations), limited-risk (transparency duties) and minimal-risk — and adds specific obligations for general-purpose AI models. It applies extraterritorially to anyone placing AI on the EU market and phases in over several years, with penalties reaching up to 7% of global annual turnover for the most serious breaches.

## Definition

The EU AI Act is a horizontal European regulation that governs AI by risk tier, imposing obligations on providers and deployers proportional to the risk an AI system poses to health, safety and fundamental rights.

## Scope

Providers and deployers that place AI systems or general-purpose AI models on the EU market or whose output is used in the EU — regardless of where they are established. Some uses (e.g. purely personal, certain research) are out of scope.

## Key requirements

- Risk-based tiers: unacceptable (prohibited), high-risk, limited-risk (transparency), minimal-risk.
- Prohibited practices include social scoring and certain biometric and manipulative uses.
- High-risk systems require risk management, data governance, technical documentation, logging, human oversight, accuracy/robustness and post-market monitoring.
- General-purpose AI (GPAI) models carry their own transparency and, for systemic-risk models, additional obligations.
- Transparency duties: users must be told when they interact with AI, and synthetic content must be marked.
- Phased application with significant penalties for non-compliance.

## Controls

- Risk classification: Determine each system's tier first — it decides every other obligation. Misclassifying a high-risk system is the costliest early mistake.
- Human oversight (Art. 14): High-risk systems must be overseeable by a person who can intervene or stop them — the regulatory basis for human-approval gates.
- Technical documentation & logging: Maintain documentation and automatic event logs so the system is traceable and auditable across its lifecycle.
- Transparency to users: Disclose AI interaction and label AI-generated or manipulated content (deepfakes).
- Post-market monitoring: Monitor performance in the field and report serious incidents; governance does not end at deployment.

## Checklist

- Inventory your AI systems and classify each by risk tier.
- Confirm none fall under prohibited practices.
- For high-risk systems, stand up risk management, data governance and technical documentation.
- Implement human oversight with the ability to intervene or stop the system.
- Enable logging/traceability and define post-market monitoring and incident reporting.
- Add user-facing transparency and content labelling where required.
- Track the phased application dates that apply to your systems.

## Common pitfalls

- Assuming the Act doesn't apply because you're outside the EU — it is extraterritorial.
- Treating GPAI obligations as identical to AI-system obligations; they are distinct.
- Bolting on human oversight that can't actually intervene in time.
- Under-documenting: missing technical documentation and logs is a common gap.

## FAQs

**Does the EU AI Act apply to companies outside the EU?**

Yes. It applies to providers and deployers whose AI systems are placed on the EU market or whose output is used in the EU, regardless of where the company is established.

**What is a 'high-risk' AI system?**

Systems used in sensitive areas (e.g. employment, credit, critical infrastructure, certain biometrics) or as safety components of regulated products. They carry the strictest obligations short of prohibition.

**How does it relate to human-in-the-loop?**

Article 14 requires effective human oversight for high-risk systems — a person able to understand, intervene in or stop the system. The human-approval-gate pattern is one way to implement it.
