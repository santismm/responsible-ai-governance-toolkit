"""Command-line interface for the toolkit.

    rai classify  <system.yaml>     EU AI Act risk tier + obligations
    rai modelcard <model.yaml>      generate a Markdown model card
    rai check     <checklist.yaml>  governance checklist coverage + gaps
    rai demo                        run the bundled end-to-end example

YAML is loaded with PyYAML's safe loader.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from .checklist import controls_from_dicts, eu_ai_act_high_risk_checklist, from_controls
from .eu_ai_act import SystemSpec, classify
from .model_card import ModelCard


def _load(path: str) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def cmd_classify(args: argparse.Namespace) -> int:
    spec = SystemSpec.from_dict(_load(args.path))
    result = classify(spec)
    print(f"System:    {spec.name}")
    print(f"Risk tier: {result.tier.value.upper()}")
    print(f"Rationale: {result.rationale}")
    if result.obligations:
        print("Obligations:")
        for ob in result.obligations:
            print(f"  - {ob}")
    return 0


def cmd_modelcard(args: argparse.Namespace) -> int:
    card = ModelCard.from_dict(_load(args.path))
    md = card.to_markdown()
    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"Wrote {args.out}  (completeness: {card.completeness():.0%})")
    else:
        print(md)
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    data = _load(args.path)
    items = data.get("controls", [])
    controls = controls_from_dicts(items) if items else eu_ai_act_high_risk_checklist()
    report = from_controls(controls)
    print(report.summary())
    return 0 if not report.gaps else 1


def cmd_demo(_: argparse.Namespace) -> int:
    spec = SystemSpec(
        name="cv-screening-assistant",
        purpose="Rank job applicants for a hiring team.",
        domains=["employment"],
        capabilities=["interacts_with_humans"],
    )
    result = classify(spec)
    print(f"[classify] {spec.name} -> {result.tier.value.upper()}")
    print(f"           {result.rationale}")
    print(f"           {len(result.obligations)} obligations apply.\n")

    report = from_controls(eu_ai_act_high_risk_checklist())
    print("[check] seeded EU AI Act high-risk checklist")
    print("        " + report.summary().replace("\n", "\n        "))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rai", description="Responsible AI governance toolkit.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("classify", help="EU AI Act risk classification")
    p.add_argument("path")
    p.set_defaults(func=cmd_classify)

    p = sub.add_parser("modelcard", help="generate a Markdown model card")
    p.add_argument("path")
    p.add_argument("-o", "--out", help="write to file instead of stdout")
    p.set_defaults(func=cmd_modelcard)

    p = sub.add_parser("check", help="governance checklist coverage")
    p.add_argument("path")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("demo", help="run the bundled end-to-end example")
    p.set_defaults(func=cmd_demo)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
