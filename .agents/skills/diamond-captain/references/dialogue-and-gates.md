# Onboarding, collaboration and Design DoR / DoD

Read at first intake, when the user's next decision is unclear, or when agreeing/revising phase criteria. Work in the user's language. These are local working definitions; use an existing team definition if supplied.

## Onboarding: make the collaboration understandable

For a first-time user, give a short orientation in ordinary language: you will turn the task into a usable result, work in small steps, bring evidence and ask at consequential choices. The current phase can change or loop; there is no obligation to perform six rounds. Explain where the task checkpoint will live (or the pasteable fallback), and that the final handoff will include artifacts, checks/limits and a clear next decision. Tools are optional; onboarding does not require setting up a stack.

Then onboard the actual task using the steps below. Reuse answers already supplied, propose a compact working agreement and leave only consequential unresolved choices for the user. Record whether orientation was shown or unnecessary and whether the agreement is proposed, accepted or delegated. Do not confuse this with passing Design DoR or permission to publish. On resume, read state and briefly restate the agreed result, what changed and the next decision; do not restart the welcome or repeat settled questions.

## A task has just arrived

1. Read supplied material and existing state first. For a new execution task, create its project file immediately from the state template before substantive work, even while intake answers are pending; record the request and initial phase entry with unknowns explicit. Reflect back the requested result in a sentence; separate the requested solution from the problem hypothesis. Identify the phase provisionally from evidence, with the reason.
2. Start a brief dialogue, not a long questionnaire. Ask the highest-value 1–3 unanswered questions in the first round. For example:
   - Free text: “What result should this work produce, for whom, and what prompted it now?”
   - Choice: “What should we deliver in this scope: a problem brief, a tested solution and handoff, or implementation plus outcome review?” Give a recommendation based on the request; allow a custom answer.
   - Free text or choices: “Which deadline, constraint or existing decision most affects this task?”
3. Follow up only on unresolved decisions: existing evidence and its freshness; owner; success measure; available files/tools and permitted actions. Do not make users fill every template field. Unknowns can stay explicitly unknown if they do not block the next action.
4. Propose a compact working agreement: task/outcome, users, scope and non-goals, constraints, current phase, depth, Design DoR, Design DoD, next action and decision owner. Ask the user to accept or adjust the consequential choices. Their original request or subsequent delegation can already settle these choices; do not ask them again.
5. Default to frequent decision questions, particularly phase boundaries. Let the user choose guided collaboration, questions only at phase boundaries, or delegated phase decisions if they want a different cadence. This is a preference, not a repeated setup requirement.
6. Record the working agreement in the project file and perform the independent first action: inspect files, calculate a baseline, synthesize supplied notes, reproduce a problem, or draft the usable artifact. A proposed interview is not a conducted interview; a research guide is a deliverable, not research evidence.

An example opening for a new, vague request:

> I'll help turn this into a usable result, work in short steps and bring you the important choices. We'll keep a task checkpoint so we can resume; at the end you'll get the artifacts, checks and next decision. Problem / Discover ↗ · 1/6 | NOT READY: the cause of manual approval delays is still a hypothesis. I can map the supplied workflow now. What would be a useful first result: a diagnosis, a revised service process, or a tested implementation? I recommend diagnosis because we do not yet know where the delay occurs. You can describe another result.

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
