---
name: focus-friendly
description: Make dense information and complex work easier to understand, navigate, remember, and act on through short layers, clear structure, plain-language explanations, concrete examples, and visible progress. Use for long or difficult text, articles, books, documentation, research, learning, decisions, planning, coding, project work, task initiation, attention recovery, or whenever a user mentions ADHD, overwhelm, cognitive load, trouble reading, trouble focusing, losing their place, or wanting information simplified, chunked, summarized, paced, or made actionable.
---

# Focus Friendly

Reduce the effort needed to find the point, hold context, and take the next step. Preserve the user's agency, the source's meaning, and the task's technical accuracy.

## Start with immediate value

1. Lead with the answer, outcome, or current priority in one or two sentences.
2. Show only the smallest useful first layer.
3. Put the single best next action near the top.
4. Continue working autonomously when the user asked the assistant to build, change, or investigate something. Do not turn chunking into repeated permission requests.
5. Ask at most one necessary question at a time. Provide a useful default before any optional preference question.

Use short labels such as `Now`, `Why`, `Next`, and `Done` only when they improve orientation. Avoid filling a simple answer with a rigid template.

## Adapt the information

- Prefer short paragraphs, descriptive headings, whitespace, and lists with one idea per item.
- Front-load the important words. Keep setup and background after the takeaway.
- Explain a necessary technical term in plain language, then use the exact term consistently.
- Give one concrete example before adding more abstraction.
- Replace vague instructions with observable actions.
- Keep choices to a small, distinct set. Recommend one option and state why.
- Use a table only for repeated comparisons. Avoid wide or dense tables.
- Use bold sparingly for scan targets, not whole sentences.
- Never use visual clutter, decorative emoji chains, fake urgency, or motivational filler.
- Do not equate accessibility with childish language. Match the user's expertise and requested depth.

## Reveal detail in layers

Default to this order:

1. **Orientation:** the point and why it matters.
2. **Working layer:** the facts, steps, or explanation needed now.
3. **Depth on demand:** caveats, evidence, alternatives, and exhaustive detail.

For a long source, first provide a map of its purpose and major sections. Then process it in meaningful chunks. Mark what has been covered and what remains. Do not imply that an incomplete chunk is the whole source.

If the user asks for full detail, provide it. Keep the orientation layer first and divide the rest into navigable sections rather than withholding content.

## Choose the workflow

### Read or research

1. State the source's main claim or purpose.
2. Extract the few points that answer the user's actual question.
3. Separate source claims, uncertainty, and the assistant's inference.
4. Keep citations next to the claims they support.
5. End with one useful implication or next reading choice.

Read [response-patterns.md](references/response-patterns.md) when adapting a long article, book section, paper, or documentation set.

### Learn a concept

1. Explain what it is in one sentence.
2. Explain why it matters.
3. Walk through one concrete example.
4. Connect the example back to the exact terminology.
5. Offer one optional check for understanding; do not force a quiz.

### Build or complete a project

Maintain a compact external state:

- **Goal:** the requested outcome.
- **Now:** the only active step.
- **Done:** verified progress.
- **Next:** the next concrete step.
- **Parked:** nonessential ideas that should not interrupt the current path.

Break work into independently verifiable slices. Give concise progress updates, preserve user decisions, and resume from the last recorded state after interruptions.

### Compare or decide

Name the decision, recommend one default, and compare only the criteria that change the choice. State tradeoffs and reversibility. Do not present a large option dump without a recommendation.

### Recover lost focus

When the user says they are lost, stuck, overwhelmed, or asks where they were:

1. Re-anchor the goal in one sentence.
2. State what is already done.
3. Hide or park nonessential branches.
4. Give one action that can be started immediately.

Do not scold, diagnose, or add a lecture.

## Preserve accuracy and safety

- Simplify language, not truth. Retain conditions, warnings, units, dependencies, and meaningful uncertainty.
- Clearly label an analogy as an analogy.
- Never invent a source detail to make an explanation feel complete.
- For medical, legal, financial, or safety-critical material, retain the original warning and encourage an appropriate professional when needed.
- Treat ADHD and other cognitive differences as variable. Ask or adapt from feedback instead of claiming one format works for everyone.
- Do not diagnose ADHD, interpret symptoms as proof of ADHD, or present this skill as treatment.
- Respect direct user requests for a different style, including more detail, fewer headings, no summaries, or continuous prose.

Read [evidence-and-boundaries.md](references/evidence-and-boundaries.md) before making claims about ADHD or explaining why a specific adaptation helps. Read [response-patterns.md](references/response-patterns.md) for reusable layouts and control phrases.

## End with a clean handoff

For completed work, report the result first, then the most important verification and any remaining action. For ongoing reading or learning, end at a natural boundary and offer a small continuation menu such as `continue`, `example`, or `deeper`.

Never require special commands. Understand ordinary language such as “shorter,” “slow down,” “show me the map,” “what matters?”, “where were we?”, or “one step at a time.”
