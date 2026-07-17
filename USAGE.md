# Seedance 2.5 Usage Guide

This repository is a lightweight planning companion for the Seedance 2.5 AI video workflow. It helps you turn a rough creative idea into a structured video-generation brief.

## Install

No heavy dependencies are required.

```bash
pip install -r requirements.txt
```

## Generate a Video Plan

```bash
python seedance_plan.py \
  --idea "A fashion sneaker floating above a reflective floor with slow cinematic camera movement" \
  --style "premium product commercial" \
  --duration 8 \
  --aspect-ratio "9:16"
```

The generated file will be saved as:

```text
outputs/seedance-plan.json
```

## Recommended Prompt Fields

Use the generated plan as a starting point, then refine it before generating the video:

- Subject: What should appear in the scene?
- Scene: Where does it happen?
- Motion: What moves, and how?
- Camera: Static, dolly, orbit, tracking, zoom, handheld, or cinematic pan?
- Style: Realistic, cinematic, product ad, anime, documentary, editorial, etc.
- References: Images, video clips, audio cues, or brand visuals.
- Duration: Short test, social clip, or longer draft.
- Aspect ratio: 16:9, 9:16, 1:1, or campaign-specific format.

## Example

```json
{
  "product": "Seedance 2.5",
  "idea": "A cinematic product demo showing a futuristic camera rotating on a clean studio table",
  "style": "cinematic product ad",
  "duration_seconds": 10,
  "aspect_ratio": "16:9",
  "prompt": "Create a cinematic product ad..."
}
```

## Full Product

Use the finished prompt plan in:

https://www.jxp.com/seedance/seedance-2-5
