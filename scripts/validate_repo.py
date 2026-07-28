#!/usr/bin/env python3
"""Validate Focus Friendly's portable skill and dual-harness packaging."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "plugins" / "focus-friendly" / "skills" / "focus-friendly"
SKILL_FILE = SKILL_DIR / "SKILL.md"
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RUBRIC_KEY = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
ALLOWED_ACTIVATION = {"should", "should_not", "contextual"}

errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{relative_path}: {exc}")
        return {}


def parse_frontmatter(text: str) -> dict[str, str]:
    check(text.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    check(end != -1, "SKILL.md frontmatter must have a closing delimiter")
    if end == -1:
        return {}

    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        check(bool(separator), f"Invalid frontmatter line: {line}")
        if separator:
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def validate_skill() -> None:
    try:
        text = SKILL_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"Unable to read {SKILL_FILE.relative_to(ROOT)}: {exc}")
        return

    fields = parse_frontmatter(text)
    check(set(fields) == {"name", "description"}, "SKILL.md frontmatter must contain only name and description")
    name = fields.get("name", "")
    description = fields.get("description", "")
    check(bool(SKILL_NAME.fullmatch(name)), "Skill name must use lowercase letters, digits, and single hyphens")
    check(name == SKILL_DIR.name, "Skill name must match its parent directory")
    check(1 <= len(description) <= 1024, "Skill description must contain 1–1024 characters")
    check("Do not invoke for routine coding" in description, "Skill description must retain its negative trigger boundary")
    check("Codex" not in text, "Portable SKILL.md must not contain harness-specific Codex wording")
    check(len(text.splitlines()) < 500, "SKILL.md must remain under 500 lines")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        check((SKILL_DIR / target).is_file(), f"Broken SKILL.md reference: {target}")

    check("references/project-work.md" in text, "SKILL.md must route multi-step work to project-work.md")


def validate_manifests() -> None:
    codex = load_json("plugins/focus-friendly/.codex-plugin/plugin.json")
    claude = load_json("plugins/focus-friendly/.claude-plugin/plugin.json")
    codex_market = load_json(".agents/plugins/marketplace.json")
    claude_market = load_json(".claude-plugin/marketplace.json")

    for label, manifest in (("Codex", codex), ("Claude", claude)):
        check(manifest.get("name") == "focus-friendly", f"{label} plugin name must be focus-friendly")
        check(bool(SEMVER.fullmatch(str(manifest.get("version", "")))), f"{label} plugin version must be semantic")
        check(manifest.get("license") == "MIT", f"{label} plugin license must be MIT")

    check(codex.get("version") == claude.get("version"), "Codex and Claude plugin versions must match")
    check(codex.get("skills") == "./skills/", "Codex manifest must point to ./skills/")

    codex_entries = codex_market.get("plugins", [])
    check(len(codex_entries) == 1, "Codex marketplace must contain exactly one plugin")
    if codex_entries:
        entry = codex_entries[0]
        check(entry.get("name") == "focus-friendly", "Codex marketplace plugin name must match")
        check(entry.get("source", {}).get("path") == "./plugins/focus-friendly", "Codex marketplace source path must match")

    claude_entries = claude_market.get("plugins", [])
    check(len(claude_entries) == 1, "Claude marketplace must contain exactly one plugin")
    if claude_entries:
        entry = claude_entries[0]
        source = entry.get("source", "")
        check(entry.get("name") == "focus-friendly", "Claude marketplace plugin name must match")
        check(source == "./plugins/focus-friendly", "Claude marketplace source path must match")
        if isinstance(source, str):
            check((ROOT / source).is_dir(), "Claude marketplace source directory must exist")

    openai_yaml = SKILL_DIR / "agents" / "openai.yaml"
    try:
        openai_text = openai_yaml.read_text(encoding="utf-8")
        check("$focus-friendly" in openai_text, "OpenAI default prompt must explicitly invoke $focus-friendly")
    except OSError as exc:
        errors.append(f"Unable to read {openai_yaml.relative_to(ROOT)}: {exc}")


def validate_evals() -> None:
    data = load_json("evals/cases.json")
    check(data.get("schema_version") == 1, "Evaluation schema_version must be 1")
    rubric = data.get("rubric", {})
    check(isinstance(rubric, dict) and len(rubric) >= 5, "Evaluation rubric must define reusable assertions")
    if not isinstance(rubric, dict):
        rubric = {}
    for name, definition in rubric.items():
        check(isinstance(name, str) and bool(RUBRIC_KEY.fullmatch(name)), f"Evaluation rubric key must be snake_case: {name}")
        check(isinstance(definition, str) and bool(definition.strip()), f"Evaluation rubric definition is required: {name}")

    cases = data.get("cases", [])
    check(isinstance(cases, list), "Evaluation cases must be an array")
    if not isinstance(cases, list):
        return

    ids: set[str] = set()
    counts: Counter[str] = Counter()
    for index, case in enumerate(cases):
        prefix = f"evals/cases.json case {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: case must be an object")
            continue
        case_id = case.get("id", "")
        activation = case.get("expected_activation", "")
        check(isinstance(case_id, str) and bool(SKILL_NAME.fullmatch(case_id)), f"{prefix}: id must be kebab-case")
        if isinstance(case_id, str):
            check(case_id not in ids, f"{prefix}: duplicate id {case_id}")
            ids.add(case_id)
        valid_activation = isinstance(activation, str) and activation in ALLOWED_ACTIVATION
        check(valid_activation, f"{prefix}: invalid expected_activation")
        if valid_activation:
            counts[activation] += 1
        prompt = case.get("prompt", "")
        rationale = case.get("rationale", "")
        check(isinstance(prompt, str) and bool(prompt.strip()), f"{prefix}: prompt is required")
        check(isinstance(rationale, str) and bool(rationale.strip()), f"{prefix}: rationale is required")
        assertions = case.get("assertions", [])
        check(isinstance(assertions, list) and len(assertions) >= 2, f"{prefix}: at least two assertions are required")
        if isinstance(assertions, list):
            for assertion in assertions:
                check(assertion in rubric, f"{prefix}: undefined rubric assertion {assertion}")
        if activation == "contextual":
            decision_rule = case.get("decision_rule", "")
            check(isinstance(decision_rule, str) and bool(decision_rule.strip()), f"{prefix}: contextual cases require a decision_rule")

    for activation in ALLOWED_ACTIVATION:
        check(counts[activation] >= 3, f"Evaluation corpus needs at least three {activation} cases")


def validate_release_docs() -> None:
    codex = load_json("plugins/focus-friendly/.codex-plugin/plugin.json")
    version = codex.get("version")
    try:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        check(f"(`{version}`)" in readme, "README status version must match the plugin manifests")
    except OSError as exc:
        errors.append(f"Unable to read README.md: {exc}")


def main() -> int:
    validate_skill()
    validate_manifests()
    validate_evals()
    validate_release_docs()

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
