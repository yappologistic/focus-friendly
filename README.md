# Focus Friendly

![Focus Friendly plugin page](docs/assets/focus-friendly-plugin.png)

Focus Friendly is a local Codex plugin that makes dense information and complex work easier to understand, navigate, and act on.

It is designed for people who experience ADHD, attention barriers, working-memory load, reading difficulty, or information overload. Anyone can use it.

## What it does

- Leads with the point and one useful next step.
- Reveals detail in layers instead of one large text wall.
- Turns long sources into a map and manageable chunks.
- Explains technical ideas with plain language and one concrete example.
- Keeps project state visible so interruptions are easier to recover from.
- Preserves caveats, citations, and exact technical details.

It does not diagnose or treat ADHD.

## Try it locally

This repository includes a local marketplace at `.agents/plugins/marketplace.json`.

From the repository root:

```powershell
codex plugin marketplace add .
codex plugin add focus-friendly@personal
```

Then start a new Codex session and try:

```text
Use $focus-friendly to explain this documentation one layer at a time.
```

You can also say:

- “Give me the big picture first.”
- “One step at a time.”
- “I lost my place—where were we?”
- “Keep the details, but make this easier to scan.”

## Project map

- `plugins/focus-friendly/` — installable plugin package
- `plugins/focus-friendly/skills/focus-friendly/SKILL.md` — core behavior
- `docs/DESIGN.md` — design decisions and boundaries
- `docs/RESEARCH.md` — source-backed research notes
- `docs/TESTING.md` — validation and manual test cases

## Status

This is an early local release (`0.1.0`). It is being prepared for future open-source publication and plugin submission.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The project is licensed under the [MIT License](LICENSE).
