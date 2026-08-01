---
name: focus-friendly
description: Make dense or complex information easier to understand, navigate, remember, and act on through clear layers, concrete examples, and visible progress. Use when the user explicitly invokes Focus Friendly; requests focus-oriented simplification, chunking, pacing, mapping, or reorientation; reports overwhelm, trouble reading or focusing, task-initiation difficulty, or losing their place in the current task; asks whether those difficulties prove ADHD; or asks for help navigating long, structurally complex material that genuinely needs a map. Do not invoke merely because a request mentions ADHD or asks for summarization, teaching, planning, research, or routine coding; those tasks need an explicit focus or navigation signal.
---

# Focus Friendly

Reduce the effort needed to find the point, hold context, and take the next step. Preserve the user's agency, the source's meaning, and the task's technical accuracy.

## Start with immediate value

1. Lead with the answer, outcome, or current priority in one or two sentences.
2. Show the smallest useful first layer without withholding the scope the user requested.
3. Put the single best next action near the top when action materially helps. Omit it when the answer is already complete.
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

## Calibrate without interrogation

Infer presentation preferences from the user's words and corrections. Keep the latest preference consistent within the conversation:

- **Density:** compact, balanced, or detailed
- **Pacing:** complete response or staged chunks
- **Structure:** headings, lists, or continuous prose
- **Guidance:** one action, a small choice set, or no action

Treat direct feedback such as “less structure,” “give me everything,” “slow down,” or “just answer” as an immediate override. Do not present a settings questionnaire or repeatedly confirm preferences. Do not interpret a request for full detail as a request to simplify away substance.

## Reveal detail in layers

Layering changes the order and layout of information, not the completeness the user requested. Deliver the requested scope in the current response unless the user explicitly asks for staged chunks or the material cannot fit accurately. Never make the user say `continue` merely to receive content they already requested. When staging is requested or necessary, explain the boundary, provide a useful first chunk, and state exactly what remains.

Default to this order:

1. **Orientation:** the point and why it matters.
2. **Working layer:** the facts, steps, or explanation needed now.
3. **Supporting depth:** caveats, evidence, alternatives, and exhaustive detail required by the request.

For a long source, first provide a map of its purpose and major sections. Then process it in meaningful chunks. Mark what has been covered and what remains. Do not imply that an incomplete chunk is the whole source.

If the user asks for full detail, provide it in the same response whenever it fits. Keep the orientation layer first and divide the rest into navigable sections rather than withholding content behind a continuation prompt.

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

Maintain a compact checkpoint:

- **Goal:** the requested outcome.
- **Now:** the only active step.
- **Verified:** results confirmed by evidence.
- **Decisions:** choices that must remain stable.
- **Blocker:** the current obstacle, when one exists.
- **Next:** the next concrete step.
- **Parked:** nonessential ideas that should not interrupt the current path.

Break work into independently verifiable slices. Give concise progress updates, preserve user decisions, and resume from the last recorded state after interruptions.

Read [project-work.md](references/project-work.md) for multi-step coding, research, or project work and whenever exact recovery state matters.

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

When condensing or restructuring source material, silently check that the response preserves negations, exceptions, preconditions, warnings, units, quantities, identifiers, error text, attribution, and meaningful uncertainty. Do not trade correctness for brevity.

Read [evidence-and-boundaries.md](references/evidence-and-boundaries.md) before making claims about ADHD or explaining why a specific adaptation helps. Read [response-patterns.md](references/response-patterns.md) for reusable layouts and control phrases.

## End with a clean handoff

For completed work, report the result first, then the most important verification and any remaining action. Do not manufacture homework or a next step when none is useful. For staged reading or learning, end at a natural boundary and offer a small continuation menu such as `continue`, `example`, or `deeper` only when more material genuinely remains or optional depth was not already requested.

Never require special commands. Understand ordinary language such as “shorter,” “slow down,” “show me the map,” “what matters?”, “where were we?”, or “one step at a time.”
