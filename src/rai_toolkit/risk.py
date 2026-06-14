"""Risk scoring.

A small, explicit likelihood x impact model across the dimensions that matter for
AI systems. The point is not the arithmetic — it is forcing each risk to be named,
scored on a shared scale, and turned into a level that drives a decision (accept /
mitigate / escalate). Deterministic and dependency-free.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

DIMENSIONS = (
    "fairness",
    "privacy",
    "safety",
    "robustness",
    "transparency",
    "security",
)


class Level(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class Risk:
    dimension: str
    likelihood: int  # 1..5
    impact: int  # 1..5
    note: str = ""

    def __post_init__(self) -> None:
        if self.dimension not in DIMENSIONS:
            raise ValueError(f"Unknown dimension '{self.dimension}'. Use one of {DIMENSIONS}.")
        for field_name in ("likelihood", "impact"):
            value = getattr(self, field_name)
            if not 1 <= value <= 5:
                raise ValueError(f"{field_name} must be in 1..5, got {value}.")

    @property
    def score(self) -> int:
        return self.likelihood * self.impact

    @property
    def level(self) -> Level:
        s = self.score
        if s >= 15:
            return Level.CRITICAL
        if s >= 9:
            return Level.HIGH
        if s >= 4:
            return Level.MEDIUM
        return Level.LOW


@dataclass
class RiskReport:
    risks: list[Risk]

    @property
    def max_level(self) -> Level:
        order = [Level.LOW, Level.MEDIUM, Level.HIGH, Level.CRITICAL]
        return max((r.level for r in self.risks), key=order.index, default=Level.LOW)

    def needs_escalation(self) -> bool:
        return self.max_level in (Level.HIGH, Level.CRITICAL)

    def table(self) -> str:
        rows = ["| Dimension | Likelihood | Impact | Score | Level |", "| --- | :-: | :-: | :-: | --- |"]
        for r in sorted(self.risks, key=lambda x: x.score, reverse=True):
            rows.append(f"| {r.dimension} | {r.likelihood} | {r.impact} | {r.score} | **{r.level.value}** |")
        return "\n".join(rows)


def assess(risks: list[Risk]) -> RiskReport:
    return RiskReport(risks=risks)
