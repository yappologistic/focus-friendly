# Design

## Goal

Reduce the cognitive work required to find the point, keep context, and take action—without reducing accuracy or user control.

## Core decisions

### One useful layer first

The first view contains the answer or current priority, a small amount of supporting information, and one next action. Deeper material remains available.

### Orientation before detail

Long material starts with a map. Project work keeps the goal, current step, verified progress, and next step visible.

### Plain language plus exact language

The skill explains jargon but keeps the exact term. Code, commands, units, warnings, and citations remain precise.

### Flexible, not prescriptive

ADHD is heterogeneous. The skill uses accessible defaults and follows the user's feedback about density, pacing, format, and depth.

### Progress without permission loops

For build and research tasks, the assistant continues working after concise updates. “One step at a time” changes presentation, not autonomy.

## Non-goals

- Diagnosing or treating ADHD
- Replacing medical care or formal accommodations
- Hiding uncertainty or inconvenient details
- Infantilizing readers
- Forcing every response into the same template

## Portable architecture

The project keeps one canonical Agent Skill inside a dual-harness plugin package:

```text
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
└── plugins/focus-friendly/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    └── skills/focus-friendly/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

`SKILL.md` and its references are harness-neutral. `agents/openai.yaml` is optional Codex interface metadata; other harnesses can ignore it. Codex and Claude Code each read their own plugin and marketplace manifests while sharing the same skill files.

This follows the Agent Skills progressive-disclosure model: matching metadata stays lightweight, core instructions load when selected, and detailed references load only when needed. Keeping the canonical skill inside the plugin also ensures every file is copied when a plugin manager caches the package.
