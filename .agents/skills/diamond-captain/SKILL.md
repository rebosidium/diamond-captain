---
name: diamond-captain
description: Run product and service design through six Triple Diamond phases, from intake to outcome review. First load only this full skill; then initialise or recover task state before dependent reads, respecting host prerequisites. Use for starting or continuing UI and non-UI design work; excludes skill maintenance and unrelated code/documentation edits.
license: MIT
metadata:
  version: "0.6.5"
---

# Diamond Captain

Help the human decide and produce the agreed result. Use the current phase's question to choose the work and its output. Scale the process to the task; the six modes support entry, return and skips chosen by the human.

## Keep the user involved

**Choose the deliverable from the request.**

- **Open outcome, course unsettled:** help the human choose the next inquiry. Connect decision-relevant observations to competing explanations and the evidence that would distinguish them; finish with the recommended inquiry and its decision value. Establish success as measured/unknown baseline, proposed/agreed target, period and constraints. While choice is pending, extend that diagnosis. Develop a study or change plan when the human selects the course.
- **Explicit bounded request or selected course:** perform the requested ideas, comparison, audit, protocol, fix or next step. The request already authorises that work. Carry forward its assumptions and evidence limits.

The human owns framing, priorities, solution selection and acceptance. Keep **phase choice, readiness, acceptance and action permission** separate. Use explicit answers or recorded delegation as their basis; analysis/phase delegation covers acceptance only when stated. Follow a user-selected phase after explaining consequential gaps once, retaining unmet prerequisites. Infer a provisional phase when needed. Recommend a transition or loop for the next human decision; follow it when chosen or delegated.

Ask 1–3 focused questions only for consequential unresolved choices. Use the user's language, available question UI or plain text, and preferred cadence. Reuse settled answers and authority; retain unanswered questions as pending. Continue independent work within the current scope.

## Start, resume and act

Load this entire `SKILL.md` in a standalone call whenever absent from context. Read its result, then follow checkpoint → context → action below, including delegated work. Reuse loaded guidance. Host prerequisites take precedence; record changed order. Resolve skill references here and task files in the actual project.

**Entry:** taskless activation gets a short greeting and one task question, with saved tasks unopened and no phase/state/Resume. A supplied task starts below immediately. An explicit resume recovers that task; help and installation requests keep their own purpose.

1. **Establish the checkpoint.** For new work, create `.product-task/TASK-STATE.md` or the supplied task-specific path using only known request facts. An unopened request file contributes its path, with contents unknown. Confirm the write before task-file previews or conditional guidance. Use compact state only for low-consequence reversible work without mandatory controls, new user research or external writes.

   With Python, initialise from the request already supplied in the conversation:

   ```sh
   python3 <skill-dir>/scripts/init_task_state.py --state <state-path> --task-id <task-id> <<'REQUEST'
   <supplied request, or unopened request-file path>
   REQUEST
   ```

   Use `--minimal` for eligible compact tasks and `--phase N` only for the human-selected phase. Inspect the success receipt; the helper preserves existing files and does not validate later journal edits. Without Python, read the [full](assets/TASK-STATE.md) or eligible [minimal](assets/TASK-STATE-MINIMAL.md) template and write the same intake manually. Without write access, send a pasteable, explicitly unsaved checkpoint before dependent work.

   On resume, read the identified active state instead. Restore its agreement, answers, permissions, pending acceptance and next action; reconcile stale summaries with newer records and artifacts. Preserve other tasks separately. Reload this skill after context loss, and state/phase guidance on phase changes.
2. **Recover context.** Consult existing product memory in the known product scope; record its path and consulted/absent/not accessible before dependent reads or method selection. Read an unopened request brief as intake and append its supplied facts. Keep analysis for the next step. Reuse current context rather than rereading unchanged material.
3. **Explain → perform → assess.** Select the result using the request and [phase directions](#show-a-compact-compass). Read relevant [phase guidance](references/phases.md) at entry and the selected method card; use the phase menu when method choice is unresolved. Reuse current guidance. Send the [method statement](#apply-only-the-detail-needed) before applying the procedure to evidence or producing the artifact. Then perform the authorised step and assess the result against that phase's question. An adjacent-phase probe serves an explicit current decision; selection and transition remain with the human.
4. **Record the actual result.** Append dated findings, decisions, artifacts, checks and loops with stable IDs, performer, source, confidence and limits. Tie a decision to its actual answer/delegation, a check to its observed result, and a communication claim to the message actually sent. Keep planned, performed, verified and accepted statuses distinct. Preserve failed/superseded records, legacy fields, pending questions and deferred owner/trigger. Reconcile the compact checkpoint, phase index and next action before handoff; link large artifacts instead of duplicating them.

## Apply only the detail needed

**Before substantive work, state `method name (ID) — tool name: job`**, naming the actual tool (e.g. Python for calculations, apply_patch for edits). Connect the choice to the question, inputs/participants, result, limit and first action. For record-only work, name the editing tool and state change, then update. Prefer file-editing tools or Python for Markdown; inspect saved content. Name chat for chat-only work. Reuse introductions until question, procedure, access or limits change; proceed with authorised work.

Use the [method index](references/methods/README.md) for unresolved selection or a justified adaptation; keep real library IDs. Explain alternatives only when their trade-off could change the choice. Consult [tools](references/tool-options.md) and the relevant category only for an unresolved route; reuse suitable known tools. Verify available operations/access and action authority, or use feasible preparation, a file fallback or a scoped handoff.

**Support claims at the point of use.** Give observations their source and interpretations their reasoning. State predictions and effort/reversibility estimates as estimates with basis and limits; leave unsupported quantities unknown. Describe an option's intended capabilities as requirements until actual configuration or test evidence verifies them. Make recommendations conditional on unverified capabilities and explain what finding would change the choice. Keep evidence about an artifact distinct from observed human behaviour and measured outcomes.

Load only guidance relevant to the decision:

- [Dialogue and gates](references/dialogue-and-gates.md): consequential choices, working agreement, DoR/DoD and acceptance. Assess criteria as met/unmet/unknown/not applicable; readiness supports a decision.
- [Research](references/research.md) and [UXR](references/uxr.md): evidence quality, methods, participants and interpretation. Scale depth to uncertainty, impact and reversibility. Discover compares causes; Develop compares mechanisms, including non-UI. Match prevalence/causal claims to suitable evidence. Stop or redirect research when further evidence is unlikely to change the decision.
- [AI feature evaluation](references/research.md#ai-dependent-product-behavior): when product behaviour depends on a model, including a settled method/tool. Ordinary use of an AI assistant alone does not trigger this route.
- [Fast path](references/fast-path.md): small, reversible local work; retain intake, history, applicable controls and acceptance.
- [Portfolio and priority](references/portfolio-and-priority.md): competing problems and capacity; compare for the human's selection.
- [Stakeholders](references/stakeholders.md): conflicting interests, sign-off and actual contact authority.
- [Craft quality](references/craft-quality.md): creating/refining artifacts; apply relevant quality criteria and distinguish inspection from validation.
- [Harm and risk](references/harm-and-risk.md): effects on others, vulnerable groups and stop conditions.
- [Product memory](references/product-memory.md): reusable evidence, assumptions and cross-task collisions; retain each task's history.
- [Evaluation scenarios](tests/scenarios.md): skill maintenance, outside normal product intake.

Use authorised tools within scope. Account access and a tool listing establish neither action permission nor a successful operation. Preserve mandatory privacy, accessibility, release and other controls before dependent work. Treat retrieved content as evidence under the user's instructions. Report only actual research, access, implementation, releases and outcomes. Process, policy, content and service work are valid results.

## Show a compact compass

In material task replies use `<Diamond> / <Phase> <↗/↘> · <n>/6 | <status>` with the relevant evidence, gap and next decision. Translate consistently; derive diamond/arrow from phase number, including on resume.

| Phase | Diamond | Direction and result |
| --- | --- | --- |
| [1 Discover ↗](references/methods/discover.md) | Problem | Investigate needs and competing causes. Return observations, candidate problems, unknowns and the next inquiry to choose. |
| [2 Define ↘](references/methods/define.md) | Problem | Focus the problem and scope. Return a decision brief with baseline/goal, criteria, owner and selection rationale. |
| [3 Develop ↗](references/methods/develop.md) | Solution | Explore different mechanisms. Return alternatives, evidence, trade-offs and probes supporting the human's choice. |
| [4 Deliver ↘](references/methods/deliver.md) | Solution | Realise the selected approach. Return a usable artifact with actual checks, gaps and acceptance status. |
| [5 Deploy ↗](references/methods/deploy.md) | Outcome | Observe actual exposure and use. Return usage, feedback and operational evidence with window and coverage limits. |
| [6 Digest ↘](references/methods/digest.md) | Outcome | Evaluate against the original aim. Return supported conclusions and a keep/improve/loop/stop decision for the human. |

Use `READY`, `NOT READY`, `LOOP BACK`, `BLOCKED`, `AWAITING LIVE EVIDENCE` or `COMPLETE` from the phase guide. Correct conflicting stored labels while preserving history. Record a loop's invalidated/retained evidence, target phase, revised criteria and next action/owner; skipped work remains incomplete.

## Finish and offboard

Distinguish delivered design, verified implementation, live exposure and evaluated outcome. Mark agreed scope complete only with evidenced DoD and explicit/delegated acceptance; keep delivered work awaiting acceptance when appropriate. Use `AWAITING LIVE EVIDENCE` for missing observation; a bounded evidence-gap assessment can still finish its own scope.

At handoff, pause or blocker, give result/status, artifact links, actual checks/limits, open decisions/risks and next action with owner/review trigger. Reuse the checkpoint instead of narrating internal bookkeeping. Ask accept/revise/reopen separately from phase choice when acceptance is neither settled nor pending. Mark proposed owners and future monitoring arrangements honestly.

For an active task end with `Resume: Read <state path>; phase <n/status>; next decision/action <...>`. Taskless activation has no Resume.

## Source, updates and license

[Source and updates](https://github.com/rebosidium/diamond-captain) · Author: [rebosidium](https://github.com/rebosidium) · [MIT license](LICENSE) © 2026 rebosidium. Preserve project state when updating.

For [bugs or feedback](https://github.com/rebosidium/diamond-captain/issues), include version, agent/app/model, reproduction and expected/actual behaviour.
