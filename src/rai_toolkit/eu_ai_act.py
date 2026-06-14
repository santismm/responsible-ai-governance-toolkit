"""EU AI Act risk classification.

A pragmatic, transparent rule engine that maps a system description to one of the
four EU AI Act risk tiers and, for high-risk systems, lists the obligations that
follow (Title III, Chapter 2). It is a *decision-support* aid for governance
conversations — not legal advice. Every decision returns the rule that fired, so
the result is explainable and reviewable.

References: Regulation (EU) 2024/1689 (the AI Act). Article numbers are indicative.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class RiskTier(str, Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"


# Practices banned outright (Art. 5).
PROHIBITED_PRACTICES = {
    "social_scoring",
    "subliminal_manipulation",
    "exploits_vulnerabilities",
    "untargeted_face_scraping",
    "realtime_remote_biometric_id_public",  # law-enforcement, narrow exceptions aside
}

# High-risk use-case areas (Annex III).
HIGH_RISK_DOMAINS = {
    "biometric_identification",
    "critical_infrastructure",
    "education",
    "employment",
    "essential_services",  # incl. creditworthiness
    "law_enforcement",
    "migration_asylum_border",
    "justice_democracy",
}

# Transparency-triggering capabilities (Art. 50).
LIMITED_RISK_CAPABILITIES = {
    "interacts_with_humans",
    "generates_synthetic_content",
    "emotion_recognition",
    "biometric_categorization",
    "deepfake",
}

# Obligations for high-risk systems (Title III, Ch. 2; Art. 9–15).
HIGH_RISK_OBLIGATIONS = [
    "Risk management system (Art. 9)",
    "Data and data governance (Art. 10)",
    "Technical documentation (Art. 11)",
    "Record-keeping / logging (Art. 12)",
    "Transparency and information to users (Art. 13)",
    "Human oversight (Art. 14)",
    "Accuracy, robustness and cybersecurity (Art. 15)",
]


@dataclass
class SystemSpec:
    name: str
    purpose: str = ""
    domains: list[str] = field(default_factory=list)
    practices: list[str] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)
    is_safety_component: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> "SystemSpec":
        return cls(
            name=data.get("name", "unnamed-system"),
            purpose=data.get("purpose", ""),
            domains=list(data.get("domains", [])),
            practices=list(data.get("practices", [])),
            capabilities=list(data.get("capabilities", [])),
            is_safety_component=bool(data.get("is_safety_component", False)),
        )


@dataclass
class Classification:
    tier: RiskTier
    rationale: str
    obligations: list[str] = field(default_factory=list)


def classify(spec: SystemSpec) -> Classification:
    banned = sorted(set(spec.practices) & PROHIBITED_PRACTICES)
    if banned:
        return Classification(
            tier=RiskTier.UNACCEPTABLE,
            rationale=f"Uses prohibited practice(s): {', '.join(banned)} (Art. 5).",
        )

    high_domains = sorted(set(spec.domains) & HIGH_RISK_DOMAINS)
    if high_domains or spec.is_safety_component:
        reason = (
            "safety component of a regulated product"
            if spec.is_safety_component and not high_domains
            else f"Annex III area(s): {', '.join(high_domains)}"
        )
        return Classification(
            tier=RiskTier.HIGH,
            rationale=f"High-risk — {reason}.",
            obligations=list(HIGH_RISK_OBLIGATIONS),
        )

    limited = sorted(set(spec.capabilities) & LIMITED_RISK_CAPABILITIES)
    if limited:
        return Classification(
            tier=RiskTier.LIMITED,
            rationale=f"Transparency obligations apply for: {', '.join(limited)} (Art. 50).",
            obligations=["Inform users they interact with / view AI-generated content (Art. 50)."],
        )

    return Classification(
        tier=RiskTier.MINIMAL,
        rationale="No high-risk domain, prohibited practice or transparency trigger identified.",
    )
