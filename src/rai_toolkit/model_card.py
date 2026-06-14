"""Model card generation.

Turns a structured spec (dict / YAML) into a Markdown model card following the
widely-used Model Cards structure (Mitchell et al., 2019). Missing sections are
rendered as explicit ``_Not specified_`` rather than silently dropped, so a card
never hides what the team failed to document.
"""

from __future__ import annotations

from dataclasses import dataclass, field

_MISSING = "_Not specified_"


@dataclass
class ModelCard:
    name: str
    version: str = "0.1.0"
    overview: str = ""
    owners: list[str] = field(default_factory=list)
    intended_use: str = ""
    out_of_scope: str = ""
    factors: list[str] = field(default_factory=list)
    metrics: dict[str, str] = field(default_factory=dict)
    training_data: str = ""
    evaluation_data: str = ""
    ethical_considerations: str = ""
    limitations: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "ModelCard":
        known = cls.__dataclass_fields__
        return cls(**{k: v for k, v in data.items() if k in known})

    def to_markdown(self) -> str:
        def block(text: str) -> str:
            return text.strip() if text and text.strip() else _MISSING

        def bullets(items: list[str]) -> str:
            return "\n".join(f"- {i}" for i in items) if items else _MISSING

        metrics = (
            "\n".join(f"- **{k}**: {v}" for k, v in self.metrics.items())
            if self.metrics
            else _MISSING
        )

        return f"""# Model Card — {self.name}

**Version:** {self.version}  ·  **Owners:** {", ".join(self.owners) or _MISSING}

## Overview
{block(self.overview)}

## Intended use
{block(self.intended_use)}

## Out-of-scope / prohibited uses
{block(self.out_of_scope)}

## Relevant factors
{bullets(self.factors)}

## Metrics
{metrics}

## Training data
{block(self.training_data)}

## Evaluation data
{block(self.evaluation_data)}

## Ethical considerations
{block(self.ethical_considerations)}

## Caveats and limitations
{block(self.limitations)}
"""

    def completeness(self) -> float:
        """Fraction of substantive sections that are filled in (0..1)."""
        checks = [
            self.overview,
            self.intended_use,
            self.out_of_scope,
            bool(self.factors),
            bool(self.metrics),
            self.training_data,
            self.evaluation_data,
            self.ethical_considerations,
            self.limitations,
        ]
        filled = sum(1 for c in checks if (c if isinstance(c, bool) else bool(str(c).strip())))
        return filled / len(checks)
