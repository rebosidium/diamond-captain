# Six phases: purpose, handoff and readiness

Use this **only for the current or adjacent phase** rather than rereading all details every turn. Agree task-specific Design DoR (entry) and DoD (exit) with the user using [dialogue and gates](dialogue-and-gates.md); the table provides evidence criteria, not automatic acceptance.

| Phase | Designer goal | Input | Minimum useful output (not necessarily a new document) | Ready to advance when… |
| --- | --- | --- | --- | --- |
| **1 Discover ↗** · Problem | Understand needs, context and alternative causes | Request, opportunity, feedback or earlier cycle | Relevant discovery evidence, candidate problems and key unknowns | Enough context to choose or refine a problem; material missing evidence is addressed or clearly managed |
| **2 Define ↘** · Problem | Decide what is worth solving and why | Discovery evidence | Focused problem, users/roles, value, product user/job story where relevant, scope, baseline/goal and owner | Decision to proceed/reframe/stop is justified; material assumptions and metrics plan are recorded |
| **3 Develop ↗** · Solution | Explore materially different ways to help | Agreed brief and retained research | Solution hypotheses, trade-offs, small probes, evidence and risks | Enough viable alternatives and evidence to make a deliberate selection; not just cosmetic variants |
| **4 Deliver ↘** · Solution | Select, validate, refine and realize a viable solution | Options and earlier brief | Chosen approach, usability/feasibility rationale, implementation or service change, quality and measurement plan | A real-use-ready solution/pilot is verified; required reviews, ownership and rollout/rollback plans are handled |
| **5 Deploy ↗** · Outcome | Observe the launched change in varied real contexts | Implemented change, instrumentation, rollout context | Usage/operations/feedback evidence, anomalies and issues | Adequate observation window and data quality for the evaluation question; major incidents escalate immediately |
| **6 Digest ↘** · Outcome | Interpret impact and decide what to do next | Usage evidence + original brief | Outcome assessment, limitations, next decision(s), owner, loop target | Findings and uncertainty support a keep/improve/rollback/research/stop decision |

Expansion explores plausible causes, mechanisms or use contexts as relevant; convergence records the evidence and human rationale for a focus, selection or next direction. Use existing alternatives and decisions rather than manufacturing a quota of candidates or rejections. A programme of research can itself be legitimate Discover work when chosen or delegated; document type alone does not determine the phase. Explicit phase choices, skipped modes and proportionate compression remain valid. Preserve the unknowns and decisions in the existing checkpoint.

For an unresolved method choice, open only the relevant menu: [Discover](methods/discover.md) · [Define](methods/define.md) · [Develop](methods/develop.md) · [Deliver](methods/deliver.md) · [Deploy](methods/deploy.md) · [Digest](methods/digest.md). Each links concrete procedures, inputs and limits in the [shared method library](methods/README.md). Methods support the decision; completing a card does not satisfy DoD or accept a handoff automatically.

- **Co-create options where useful.** In Develop/Deliver, involve affected users or frontline staff in generating or refining options when their experience could change the choice. An existing conversation or sketch can suffice; proposals remain hypotheses until tested.
- **Make service dependencies visible when needed.** Sketch the relevant journey and touchpoints → frontstage/backstage work → dependencies, owners and failure points. Ground current-state claims in evidence and label proposed changes. Reuse an existing artifact; a full blueprint is optional.
- **Check viability when framing or selecting a direction.** Compare user value, feasibility and the resources, running/support costs and ownership needed to sustain the solution. Keep decision-critical unknowns in the existing brief; no canvas, workshop or new document is required.

These task-scaled practices draw on Design Council's [collaboration principles](https://www.designcouncil.org.uk/resources/framework-for-innovation/) and [service-design methods](https://www.designcouncil.org.uk/fileadmin/uploads/dc/Documents/DesignCouncil_Design%2520methods%2520for%2520developing%2520services.pdf).

## Entry readiness (Design DoR)

| Phase | Minimum basis to start useful work; clarify a missing critical input before dependent work |
| --- | --- |
| 1 Discover | Initial request/opportunity and a bounded question; unknown users/causes can be discovery questions |
| 2 Define | Usable discovery evidence, its limitations and a problem decision to make |
| 3 Develop | Accepted or explicitly delegated problem/scope and criteria for comparing mechanisms |
| 4 Deliver | A supported selection or a bounded validation decision; available delivery surface and constraints |
| 5 Deploy | Verified live exposure of the change/pilot, a usable observation plan and actual access; rollout preparation has phase-4 evidence maturity even if the user selects phase 5 for planning |
| 6 Digest | Adequate usage evidence and original goal/baseline, or an explicit decision about why evidence is insufficient |

For a multi-candidate intake, record the human's selection rationale and deferred alternatives before Define exit; a comparison alone is not a selected priority.

For a Deliver handoff, agree applicable [artifact quality and rationale criteria](craft-quality.md) for the actual result; a checklist inspection alone does not satisfy DoD or acceptance.

At each exit, compare output and readiness with agreed DoD, then ask for the transition decision unless already chosen or delegated. `READY` can coexist with `decision: pending`. Users can select any work phase after a concrete gap warning; record that choice without declaring missing prerequisites met. A prepared rollout has phase-4 evidence maturity until exposure is verified; choosing phase 5 for planning does not prove deployment. An insufficient observation window limits outcome claims even if the user selects phase 6 for a gap assessment.

## Reorientation rules

- **No brief yet, but explored users and constraints?** Usually Discover → Define.
- **Clear problem, but no concrete alternatives?** Develop even if a stakeholder already supplied a design; test whether the desired solution is an assumption.
- **Options already compared, ready to detail and implement?** Deliver.
- **Solution exists but not deployed?** Recommend Deliver; if the user selects Deploy, do permitted preparation with exposure unverified, never fabricate live observations.
- **Product live with raw telemetry but no synthesis?** Deploy → Digest.
- **Findings challenge problem framing?** Go to Discover or Define with explanation; do not march forward.
- **Small, routine, reversible task?** Compress phases with explicit evidence. Do not force six meetings or research studies.
- **Non-UI work?** A service policy, customer communication, operational workflow or training change is a valid Deliver output.

## Decision statuses

- `READY`: evidence and handoff sufficient for the next decision; no unresolved critical blocker.
- `NOT READY`: one or more decision-critical gaps with a targeted next method/action.
- `LOOP BACK`: newly learned evidence invalidates or meaningfully changes an earlier assumption; name target phase.
- `BLOCKED`: necessary access, authorization, safety/launch requirement or external input prevents progress; do all independent work first.
- `AWAITING LIVE EVIDENCE`: needed live exposure or adequate observation is unverified/unavailable. A prepared but unshipped change has phase-4 evidence maturity regardless of the selected work phase; do not imply launch.
- `COMPLETE`: agreed task scope accepted with its DoD evidenced. Say whether this is design/handoff completion or a reviewed live outcome; an outcome task needs outcome evidence and a documented next decision.

**Never apply these as universal hard stage gates.** They are prompts for a defendable decision. Optional checklists remain optional; security, legal, accessibility, privacy and release requirements are not made optional by the process.

## Five handoffs and the loop

1. Discovery evidence → agreed problem and goal.
2. Agreed brief → solution alternatives.
3. Alternatives and evidence → selected solution.
4. Verified implementation/change → live observations.
5. Live observations → assessment and next decision.
6. Evaluation findings → earliest relevant phase for the next iteration.

On each loop save a compact transition: **new evidence → invalidated decision/artifacts → retained evidence/constraints → target phase → reopened DoR/DoD → next action and decision owner**. Mark affected outputs superseded, not deleted. Recheck answers only when the new finding invalidates them. If repeated returns add no decision-changing evidence, narrow the question or propose a bounded stop/review instead of repeating the same study.

Keep original evidence accessible at later phases; an artifact handoff **adds** information, it doesn't erase prior context.
