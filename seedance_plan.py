"""
Seedance 2.5 prompt planning helper.

This script turns a short creative idea into a structured JSON brief that can be
used when working with Seedance 2.5.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_prompt(idea: str, style: str, duration: int, aspect_ratio: str) -> str:
    return (
        f"Create a {duration}-second {style} video in {aspect_ratio}. "
        f"Core idea: {idea}. "
        "Use clear subject continuity, deliberate camera movement, natural pacing, "
        "consistent lighting, and a polished cinematic composition. "
        "Preserve important reference details and avoid random scene changes."
    )


def build_plan(idea: str, style: str, duration: int, aspect_ratio: str) -> dict:
    return {
        "product": "Seedance 2.5",
        "target_url": "https://www.jxp.com/seedance/seedance-2-5",
        "idea": idea,
        "style": style,
        "duration_seconds": duration,
        "aspect_ratio": aspect_ratio,
        "prompt": build_prompt(idea, style, duration, aspect_ratio),
        "references": {
            "image": [],
            "video": [],
            "audio": [],
            "style_notes": [
                "Add product, character, or environment references before generation.",
                "Use the same visual direction across iterations.",
            ],
        },
        "review_checklist": [
            "Does the subject remain consistent?",
            "Is the motion natural and intentional?",
            "Does the camera direction match the brief?",
            "Are lighting and style consistent?",
            "Is the clip suitable for the target platform?",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Seedance 2.5 video prompt plan")
    parser.add_argument("--idea", required=True, help="Short creative video idea")
    parser.add_argument("--style", default="cinematic AI video", help="Visual or campaign style")
    parser.add_argument("--duration", type=int, default=10, help="Planned video duration in seconds")
    parser.add_argument("--aspect-ratio", default="16:9", help="Output aspect ratio, such as 16:9 or 9:16")
    parser.add_argument("--output", default="outputs/seedance-plan.json", help="Output JSON path")
    args = parser.parse_args()

    plan = build_plan(args.idea, args.style, args.duration, args.aspect_ratio)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Seedance 2.5 plan saved to {output_path}")


if __name__ == "__main__":
    main()
