# Onboarding, collaboration and Design DoR / DoD

Read when the user's next decision is unclear or when agreeing/revising phase criteria. Work in the user's language. These are local working definitions; use an existing team definition if supplied.

## Onboarding: make the collaboration understandable

Follow SKILL.md's taskless greeting or task intake/resume route. Keep orientation to what helps the next decision; introduce navigation, storage and handoff details when useful or requested. Reuse supplied scope and answers, leaving consequential unresolved choices to the human. Record actual orientation and agreement status separately from readiness and action permission. On resume, recover state and briefly identify the agreed result, what changed and the next decision.

## A task has just arrived

1. Follow [start/resume ordering and fallbacks](../SKILL.md#start-resume-and-act), including intake before supplied-file reads. Recover the active state on resume; for new work record the known request or unopened path, then append what the material adds. Briefly reflect the requested result. Refine a provisional phase from evidence with the reason; do not invent a user-selected phase or delay independent analysis for its approval.
2. Begin bounded independent work within [the skill's course-choice rules](../SKILL.md#keep-the-user-involved). Ask 1–3 focused questions only for consequential unanswered gaps, not as a mandatory first round. For example:
   - Free text: “What result should this work produce, for whom, and what prompted it now?”
   - Choice: “What should we deliver in this scope: a problem brief, a tested solution and handoff, or implementation plus outcome review?” Give a recommendation based on the request; allow a custom answer.
   - Free text or choices: “Which deadline, constraint or existing decision most affects this task?”
3. Follow up only on unresolved decisions: existing evidence and its freshness; owner; success measure; available files/tools and permitted actions. Do not make users fill every template field. Unknowns can stay explicitly unknown if they do not block the next action.
4. Propose a compact working agreement: task/outcome, users, scope and non-goals, constraints, current phase, depth, Design DoR, Design DoD, next action and decision owner. Ask the user to accept or adjust the consequential choices. Their original request or subsequent delegation can already settle these choices; do not ask them again.
5. Ask at consequential unresolved choices, particularly phase boundaries; follow the user's cadence and delegation. Do not repeatedly offer collaboration modes or ask settled questions.
6. Record the agreement, then follow [explain → perform → assess](../SKILL.md#start-resume-and-act) for the first action within scope. Record preparation as preparation and collected evidence as evidence.

For a vague task, initialise intake, select/read the card, then explain the next action before work:

> Problem / Discover ↗ · 1/6 | NOT READY. I’ll use DS-05, Service blueprint, to locate handoffs that might explain delays. I’ll use this host’s file reader and editor to map the supplied workflow in Markdown; this exposes candidate bottlenecks, not measured causes. Is there a deadline that changes the scope?

If the user answers “make reasonable decisions and finish locally,” record the delegation and continue within that scope. If they request “only explain,” answer without creating product artifacts or changing external systems.

## Design Definition of Ready (DoR)

DoR answers: **Do we know enough, and have the necessary inputs and authority, to start this phase's work?** It does not demand a fully known solution.

Agree only the criteria relevant to this task: intended decision/deliverable; usable input evidence; critical constraints and dependencies; owner or clearly unassigned ownership; available work surface; permitted actions; a bounded next action and research review point where needed. Unknowns that cannot affect that action are not blockers.

## Design Definition of Done (DoD)

DoD answers: **What observable result will let the accountable person accept this scope or phase?** Separate phase DoD, requested task DoD, engineering/release readiness and live outcome evaluation.

Define concrete evidence, an acceptance owner and remaining obligations for the relevant result. For a selected design, examples are behavior/edge states, understandable handoff, relevant accessibility/usability/feasibility evidence, resolved critical risks and a measurement/rollout plan. For a non-UI process, use roles, rules, exceptions, handoffs and a walkthrough. Include only what is relevant or mandated. The existence of a Figma file does not satisfy DoD by itself.

Do not invent a universal requirement to run interviews, use Figma, hold six meetings, or reach a fixed sample. Do not silently weaken criteria to close a task. Record any negotiated revision, reason and owner; mandatory controls cannot be waived by an ordinary phase decision.

Use a small table in existing state/artifacts:

| Scope / criterion | Evidence or acceptance test | Owner | Result |
| --- | --- | --- | --- |
| Phase 2 exit: focused problem and goal | Brief grounded in named evidence; owner accepts scope | Named person or unassigned | met / unmet / unknown / not applicable + reason |

`READY` means an evidence gate is met. A separate field records `pending / accepted / delegated / rejected` for the phase decision. Do not label a pending decision as accepted. A missing stakeholder answer may block a transition while drafting or analysis can continue.

## User-directed navigation

The user controls the work phase: any entry, forward skip or return is valid. Recommend the best-supported phase without enforcing the six-phase order. If the user says "go straight to Develop" with an untested problem, briefly explain the consequence ("we can explore options; selection will still depend on validating the problem"), record the choice and begin useful exploration. Their explicit direction already decides that move; no second confirmation is needed. Otherwise ask the consequential decision as usual.

Keep selected work phase, evidence-supported maturity and readiness separate in the project file. Mark omitted phases skipped/unassessed, preserve unmet DoR/DoD and record who chose, when, why, the warning and retained work. A user may work on an outcome-review plan without live data; label it a plan/gap assessment, never measured impact. Mandatory permissions and release obligations still govern actual actions. Explain the concrete trade-off once; avoid a recurring veto or generic disclaimer.

## Questions at phase boundaries

Show the current result and evidence first. Then ask one concrete decision, normally with 2–4 choices and free text. Tailor options to actual findings; avoid vague “continue?” prompts.

| Transition | What the user decides |
| --- | --- |
| 1 Discover → 2 Define | Which supported problem to frame, which critical gap to investigate, or whether to stop |
| 2 Define → 3 Develop | Accept/adjust the brief, scope, success measure and solution exploration criteria |
| 3 Develop → 4 Deliver | Which mechanism to select, which risky assumption to test first, or which option to revisit |
| 4 Deliver → 5 Deploy | Accept the verified deliverable and rollout/observation plan; actual deployment still needs its own valid authority |
| 5 Deploy → 6 Digest | Whether the observed window/data are adequate for the evaluation question or more observation is needed |
| 6 Digest → next loop/close | Keep, improve, research, roll back or stop; name the next phase, owner and trigger |

For a loop, say what contradicted the prior decision, what remains useful and what will be reopened. Ask about the new direction unless already delegated. Keep invalidated work and its history instead of erasing it.

Record each outstanding question with its reason, whether it blocks a decision, and the independent action underway. Record the actual question channel: text choices are plain text; record a question UI/tool only after a successful invocation. A dispatch acknowledgment is not a user answer. Reuse answers after resume. If a structured question tool returns without an answer, keep required questions pending; do not repeatedly call it or silently accept its default. If a user answer changes scope, update DoR/DoD before doing dependent work.

## Dialogue versus tool permission

A product decision is not blanket authorization for external writes. Preserve already granted permission and task boundaries. Read/inspect with available authorized sources; local reversible work can proceed within scope. Sending a message, scheduling participants, changing a live design, publishing, spending or releasing needs authority for that concrete action under governing rules. Prepare reviewable artifacts while that authority is missing. Tool availability, authentication, read access, write access, and user authorization are different facts; record only those verified. Tool catalogs suggest candidates, not dependencies.

## Time, timeboxes and deadline triage

Give each planned next action a timebox (clock time or session budget) and a review date/trigger; mark an unagreed estimate as proposed. A timebox is a decision point, not a completion promise. Intake may leave the plan unknown until evidence is read.
For multi-step work, sequence the next 2–5 useful actions by what they unblock; identify dependent work and independent work that can run in parallel. Do not invent extra actions for a one-step task.
At expiry, report what is known, what changed and the choice to converge, narrow, loop or stop. Follow existing scoped delegation; otherwise leave that choice to the human rather than silently extending work.
When a deadline forces cuts, propose reducing research breadth/optional artifacts first, then the number of compared mechanisms, then non-mandatory evaluation depth. Explain the evidence lost; retain adequate alternatives for the actual decision.
Never cut mandatory privacy, accessibility, legal, safety or release controls or honesty of status. Time running out is not evidence; an unfinished check stays unmet/unknown.

## Multiple performers

For a real handoff, record who does what (human, this agent, another agent/team), their authorized actions, expected output and where it lands. Do not create a roster ceremony for solo work.
Distinguish requested, delivered and verified: dispatch is not delivery, and another performer's report is evidence to check, not acceptance. Preserve their source/version/limits and reference their state/output instead of merging task histories.
Define the receiving performer's next decision and verification owner; unknown ownership remains unassigned and blocks only work that depends on it. Existing contact, sharing and external-action permissions still apply.
