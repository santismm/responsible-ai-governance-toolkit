from __future__ import annotations

from rai_toolkit import (
    Control,
    ModelCard,
    Risk,
    SystemSpec,
    assess,
    classify,
    eu_ai_act_high_risk_checklist,
    from_controls,
)
from rai_toolkit.eu_ai_act import RiskTier


# --- EU AI Act classification ------------------------------------------------

def test_prohibited_practice_is_unacceptable():
    spec = SystemSpec(name="x", practices=["social_scoring"])
    assert classify(spec).tier is RiskTier.UNACCEPTABLE


def test_employment_domain_is_high_risk_with_obligations():
    spec = SystemSpec(name="cv-screener", domains=["employment"])
    result = classify(spec)
    assert result.tier is RiskTier.HIGH
    assert len(result.obligations) == 7


def test_chatbot_is_limited_risk():
    spec = SystemSpec(name="bot", capabilities=["interacts_with_humans"])
    assert classify(spec).tier is RiskTier.LIMITED


def test_plain_system_is_minimal():
    assert classify(SystemSpec(name="spam-filter")).tier is RiskTier.MINIMAL


# --- Risk scoring ------------------------------------------------------------

def test_risk_levels_and_escalation():
    report = assess([
        Risk("fairness", likelihood=4, impact=5),   # score 20 -> critical
        Risk("privacy", likelihood=1, impact=2),     # score 2 -> low
    ])
    assert report.max_level.value == "critical"
    assert report.needs_escalation() is True


def test_risk_validation_rejects_bad_input():
    import pytest

    with pytest.raises(ValueError):
        Risk("fairness", likelihood=9, impact=1)
    with pytest.raises(ValueError):
        Risk("unknown_dimension", likelihood=1, impact=1)


# --- Model card --------------------------------------------------------------

def test_model_card_renders_and_flags_missing():
    card = ModelCard(name="m", overview="An overview.")
    md = card.to_markdown()
    assert "# Model Card — m" in md
    assert "_Not specified_" in md  # empty sections flagged, not dropped
    assert 0 < card.completeness() < 1


# --- Checklist ---------------------------------------------------------------

def test_checklist_requires_evidence():
    controls = [
        Control(id="A", requirement="risk mgmt", status="done", evidence="doc#1"),
        Control(id="B", requirement="logging", status="done"),  # no evidence -> gap
    ]
    report = from_controls(controls)
    assert report.coverage == 0.5
    assert report.gaps[0].id == "B"


def test_seeded_eu_checklist_starts_empty():
    report = from_controls(eu_ai_act_high_risk_checklist())
    assert report.coverage == 0.0
    assert len(report.gaps) == 7
