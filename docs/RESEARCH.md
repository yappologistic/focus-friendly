# Research notes

Accessed July 27, 2026.

## What ADHD research changed

Authoritative clinical sources describe ADHD as variable across people and situations. Common adult difficulties can include managing attention, completing lengthy tasks, organization, planning, working memory, following instructions, and finishing projects.

That led to four product rules:

1. Externalize state instead of expecting the user to hold it in memory.
2. Split large tasks into meaningful pieces.
3. Make the current priority and next action obvious.
4. Personalize the format rather than claiming a universal ADHD solution.

Sources:

- [NIMH: ADHD overview](https://www.nimh.nih.gov/health/publications/attention-deficit-hyperactivity-disorder-what-you-need-to-know)
- [NIMH: ADHD in adults](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)
- [CDC: ADHD in adults](https://www.cdc.gov/adhd/about/adhd-in-adults.html)
- [Alderson et al.: adult ADHD and working memory meta-analysis](https://pubmed.ncbi.nlm.nih.gov/23688211/)
- [Onandia-Hinchado et al.: adult ADHD cognitive domains systematic review](https://pubmed.ncbi.nlm.nih.gov/33620582/)

## What accessibility guidance changed

W3C cognitive-accessibility guidance recommends clear words, short sentences and blocks, summaries for long content, separated instructions, whitespace, reduced interruptions, short critical paths, visible structure, and personalization.

That led to layered answers, source maps, limited option sets, predictable labels, and focus-recovery summaries.

Sources:

- [W3C: Clear and Understandable Content](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/)
- [W3C: Help Users Focus](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o5-user-focus/)
- [W3C: Cognitive Accessibility](https://www.w3.org/WAI/cognitive/)
- [W3C: Writing for Web Accessibility](https://www.w3.org/WAI/tips/writing/)

## What Codex guidance changed

Current OpenAI guidance describes skills as reusable workflows with progressive disclosure and plugins as their installable distribution unit. It recommends concise trigger descriptions, imperative steps, and optional references loaded only when needed.

That led to one focused skill, a compact `SKILL.md`, on-demand references, UI metadata, an official plugin manifest, and a local marketplace for testing.

Sources:

- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: Build plugins](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Plugins overview](https://developers.openai.com/plugins/)

## What cross-harness research changed

The open Agent Skills specification and Claude Code use the same portable core: a directory named for the skill, a `SKILL.md` file with `name` and `description` frontmatter, and optional `scripts/`, `references/`, and `assets/` directories. Both recommend progressive disclosure and relative links to bundled resources.

Claude Code supports two relevant distribution paths:

1. Standalone skills in `.claude/skills/` for a project or `~/.claude/skills/` for a user.
2. Plugins with a `.claude-plugin/plugin.json` manifest and skills under `skills/<name>/SKILL.md`, distributed through a `.claude-plugin/marketplace.json` catalog.

The cross-harness Skills CLI can install a direct skill directory from GitHub into Claude Code, Codex, and other supported agents. This is a convenience installer, not part of the Agent Skills file-format specification.

These findings led to one canonical, harness-neutral skill plus thin Codex and Claude Code packaging metadata. Duplicating the skill into vendor-specific folders was rejected because copies would drift. Referencing files outside a plugin was also rejected because Claude Code caches plugins by copying the plugin directory.

Sources:

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [Claude Code: Create plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code: Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code: Discover and install plugins](https://code.claude.com/docs/en/discover-plugins)
- [Vercel Labs Skills CLI](https://github.com/vercel-labs/skills)

## What evaluation guidance changed

Current Agent Skills guidance warns that overly broad descriptions can trigger incorrectly, conflict with other skills, and degrade agent performance. It recommends evaluating trigger accuracy, isolation, coexistence, instruction following, and output quality with representative positive, negative, and ambiguous cases.

W3C cognitive-accessibility guidance also emphasizes personalization and including people with cognitive and learning disabilities in design and testing. Accessible defaults are not a substitute for user feedback.

These findings led to four changes:

1. Narrow implicit activation and state explicit negative boundaries.
2. Add should-activate, should-not-activate, and contextual evaluation cases.
3. Infer presentation preferences from user feedback instead of imposing one template.
4. Validate packaging, references, version parity, and evaluation coverage continuously.

Sources:

- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic: Evaluating Skills before deployment](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)
- [W3C: Cognitive Accessibility](https://www.w3.org/WAI/cognitive/)

## Evidence boundary

The skill combines clinical descriptions with general cognitive-accessibility guidance. This is a design rationale, not evidence that the plugin treats ADHD or that every pattern helps every user. User testing is still required.
