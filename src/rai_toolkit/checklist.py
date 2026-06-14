"""Governance checklist validation.

Loads a checklist of governance controls and reports coverage and gaps. Ships with
the high-risk obligations from the EU AI Act so a team can answer "are we ready?"
with evidence, not vibes. A control is satisfied only if it is marked ``done`` AND
carries an evidence reference — undocumented controls do not count.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .eu_ai_act import HIGH_RISK_OBLIGATIONS


@dataclass
class Control:
    id: str
    requirement: str
    status: str = "todo"  # "todo" | "in_progress" | "done"
    evidence: str = ""

    @property
    def satisfied(self) -> bool:
        return self.status == "done" and bool(self.evidence.strip())


@dataclass
class ChecklistReport:
    controls: list[Control] = field(default_factory=list)

    @property
    def coverage(self) -> float:
        if not self.controls:
            return 0.0
        return sum(c.satisfied for c in self.controls) / len(self.controls)

    @property
    def gaps(self) -> list[Control]:
        return [c for c in self.controls if not c.satisfied]

    def summary(self) -> str:
        lines = [f"Coverage: {self.coverage:.0%} ({sum(c.satisfied for c in self.controls)}/{len(self.controls)})"]
        if self.gaps:
            lines.append("\nOpen controls:")
            lines += [f"  [ ] {c.id} — {c.requirement} ({c.status})" for c in self.gaps]
        else:
            lines.append("\nAll controls satisfied with evidence.")
        return "\n".join(lines)


def from_controls(controls: list[Control]) -> ChecklistReport:
    return ChecklistReport(controls=controls)


def eu_ai_act_high_risk_checklist() -> list[Control]:
    """A blank checklist seeded with the EU AI Act high-risk obligations."""
    return [
        Control(id=f"AIA-{i+1:02d}", requirement=ob)
        for i, ob in enumerate(HIGH_RISK_OBLIGATIONS)
    ]


def controls_from_dicts(items: list[dict]) -> list[Control]:
    return [
        Control(
            id=str(it.get("id", f"CTRL-{i+1:02d}")),
            requirement=str(it.get("requirement", "")),
            status=str(it.get("status", "todo")),
            evidence=str(it.get("evidence", "")),
        )
        for i, it in enumerate(items)
    ]
