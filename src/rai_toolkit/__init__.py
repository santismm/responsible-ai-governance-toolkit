"""rai_toolkit — responsible AI governance as code.

EU AI Act risk classification, risk scoring, model cards and governance
checklists. Pairs with the Markdown templates under ``templates/``.
"""

from .checklist import (
    ChecklistReport,
    Control,
    controls_from_dicts,
    eu_ai_act_high_risk_checklist,
    from_controls,
)
from .eu_ai_act import (
    HIGH_RISK_OBLIGATIONS,
    Classification,
    RiskTier,
    SystemSpec,
    classify,
)
from .model_card import ModelCard
from .risk import DIMENSIONS, Level, Risk, RiskReport, assess

__version__ = "0.1.0"

__all__ = [
    "ChecklistReport",
    "Control",
    "controls_from_dicts",
    "eu_ai_act_high_risk_checklist",
    "from_controls",
    "HIGH_RISK_OBLIGATIONS",
    "Classification",
    "RiskTier",
    "SystemSpec",
    "classify",
    "ModelCard",
    "DIMENSIONS",
    "Level",
    "Risk",
    "RiskReport",
    "assess",
    "__version__",
]
