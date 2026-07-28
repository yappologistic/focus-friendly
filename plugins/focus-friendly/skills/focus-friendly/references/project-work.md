# Project work and recovery

Use this reference for multi-step coding, research, planning, or production work where interruptions could erase important operational context.

## Maintain a recoverable checkpoint

Track only state that changes what happens next:

```text
Goal: [requested outcome]
Now: [single active step]
Verified: [facts confirmed by a command, source, inspection, or user decision]
Decisions: [choices and constraints that must remain stable]
Blocker: [current obstacle and its evidence, if any]
Next: [smallest concrete continuation]
Parked: [nonessential branches]
```

Include exact file paths, artifact names, commands, error text, source coverage, or validation results when losing them would force repeated work. Distinguish completed activity from verified results.

Do not create a checkpoint file unless the user requests persistent project state. Keep the checkpoint in working context and surface it only when it helps orientation.

## Report progress without interruption

- Keep one active step.
- Report meaningful state changes, not every tool call.
- Preserve the user's decisions instead of reopening them without new evidence.
- Continue through independently verifiable slices unless authority or essential input is missing.
- Park optional improvements so they do not displace the requested outcome.

## Recover after lost focus

When the user returns after an interruption:

1. Restate the goal in one sentence.
2. Name the last verified result.
3. Repeat decisions or constraints that still govern the work.
4. State the current blocker only if one exists.
5. Give the exact next continuation.

Do not replay the full history or make the user reconstruct prior context.

## Hand off completed work

Lead with the outcome. Then report the strongest verification, material limitations, and any action that genuinely remains. Omit a next action when the work is complete.
