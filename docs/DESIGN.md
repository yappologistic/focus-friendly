# Design

## Goal

Reduce the cognitive work required to find the point, keep context, and take action—without reducing accuracy or user control.

## Core decisions

### One useful layer first

The first view contains the answer or current priority, a small amount of supporting information, and one next action when action is useful. Layering changes presentation, not requested completeness: deeper material remains in the same response when the user requests it and it fits accurately.

### Orientation before detail

Long material starts with a map. Project work keeps the goal, current step, verified progress, and next step visible.

### Plain language plus exact language

The skill explains jargon but keeps the exact term. Code, commands, units, warnings, and citations remain precise.

### Flexible, not prescriptive

ADHD is heterogeneous. The skill uses accessible defaults and follows the user's feedback about density, pacing, format, and depth.

### Progress without permission loops

For build and research tasks, the assistant continues working after concise updates. “One step at a time” changes presentation, not autonomy.

### Precise activation

Focus Friendly activates for explicit requests, expressed focus or cognitive-load barriers in the current task, lost-context recovery, direct questions about whether those barriers prove ADHD, or material whose length and structure clearly require a map. Merely mentioning ADHD or asking for summarization, teaching, planning, research, routine coding, or a short factual answer does not activate the skill without a focus or navigation signal.

### Calibration without setup

The skill infers density, pacing, structure, and guidance preferences from ordinary requests and corrections. The latest direct preference wins within the conversation. It does not require a settings questionnaire or assume one format works for everyone.

### Recoverable operational state

Multi-step work distinguishes activity from verified results and preserves decisions, blockers, exact operational details, and the next continuation. This reduces repeated work after an interruption without forcing every progress update into a visible template.

### Evaluation before expansion

Behavior changes must be tested against requests that should activate, should not activate, and require contextual judgment. Evaluation covers triggering, coexistence, instruction following, accuracy retention, and output quality. Source-backed fixtures make accuracy checks concrete by enumerating facts that must survive adaptation and claims that must not be introduced.

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
├── .github/workflows/validate.yml
├── evals/cases.json
├── scripts/validate_repo.py
└── plugins/focus-friendly/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    └── skills/focus-friendly/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
            ├── evidence-and-boundaries.md
            ├── project-work.md
            └── response-patterns.md
```

`SKILL.md` and its references are harness-neutral. `agents/openai.yaml` is optional Codex interface metadata; other harnesses can ignore it. Codex and Claude Code each read their own plugin and marketplace manifests while sharing the same skill files.

This follows the Agent Skills progressive-disclosure model: matching metadata stays lightweight, core instructions load when selected, and detailed references load only when needed. Keeping the canonical skill inside the plugin also ensures every file is copied when a plugin manager caches the package.
