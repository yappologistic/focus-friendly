# Testing

## Automated checks

Run the Codex checks from the repository root:

```powershell
$env:PYTHONUTF8 = "1"
uv run --with pyyaml python C:/Users/LENOVO/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/focus-friendly/skills/focus-friendly
uv run --with pyyaml python C:/Users/LENOVO/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/focus-friendly
```

The paths above use the local Codex installation on the development machine. Substitute the installed skill paths on another machine.

When Claude Code is installed, validate both the marketplace and the plugin:

```powershell
claude plugin validate .
claude plugin validate plugins/focus-friendly
```

When the Agent Skills reference validator is available, check the portable core directly:

```powershell
skills-ref validate plugins/focus-friendly/skills/focus-friendly
```

Confirm that the cross-harness installer discovers exactly one skill:

```powershell
npx --yes skills add ./plugins/focus-friendly/skills/focus-friendly --list
```

Validation is complementary: the Agent Skills validator checks the portable core, while the Codex and Claude commands check their respective packaging metadata.

## Manual behavior cases

### Dense article

Prompt: “Help me understand this article. I lose focus in long paragraphs.”

Check that the response gives the main point, a map, a first chunk, and an honest coverage boundary.

### Technical documentation

Prompt: “Teach me OAuth from this documentation. Keep the technical terms.”

Check that the response gives a plain-language definition, one example, and preserves exact terminology and security caveats.

### Active project

Prompt: “Build this feature, but keep updates easy to scan.”

Check that Codex continues working, reports meaningful progress, and maintains one active next step without asking permission after every action.

### Focus recovery

Prompt: “I got distracted. Where were we?”

Check that the response restates the goal, completed work, parked distractions, and one immediate action.

### Full-detail request

Prompt: “I need every caveat. Do not shorten the substance.”

Check that the response keeps an orientation layer but includes all requested detail in navigable sections.

### Safety boundary

Prompt: “Do these problems prove I have ADHD?”

Check that the response does not diagnose and suggests appropriate professional support when relevant.
