# Acceptance scenarios for Diamond Captain

These are **behavioral test cases and expected responses**, not claims that a live Codex session, users or external tools were tested. Run them in fresh sessions after installing the skill. Check reorientation, evidence handling, appropriate action and non-fabrication.

| Prompt / fixture | Expected phase and behavior | Failure to watch for |
| --- | --- | --- |
| Only "Use Diamond Captain", no established task | Brief greeting in the user's language and exactly one task question; no phase, status, state creation, reference/tool inventory or resume line. | Gives a process lecture, three intake questions, assumes Discover, or selects an unrelated saved task. |
| A concrete task and relevant material are already supplied | Infer an initial working phase honestly; write intake before dependent reads, use supplied context and execute a useful first action without asking for the task again or waiting for initial phase approval. | Replaces work with a welcome/questionnaire, reads material before intake or claims provisional phase choice was accepted. |
| "Our checkout completion dropped; PM asks for a redesign." No investigation provided. | **Discover ↗ / NOT READY**: check data integrity, affected cohorts, errors, constraints and plausible causes first; propose smallest decision-changing evidence collection. | Assumes the UI is the cause or jumps into Figma. |
| "We have research, prioritized a problem, defined metrics. What now?" | **Define ↘ / READY** or **Develop ↗** depending on brief decision; confirm handoff and explore materially different mechanisms. | Repeats discovery without reason or skips alternative solutions. |
| "Here are two tested approaches and a selected direction; what's my stage?" | **Deliver ↘**; review selection rationale, remaining UX/technical risks, delivery state. | Starts at Discover by default. |
| "Only a two-word legal consent label changed; should we skip testing?" | Depth tied to legal harm and reversibility; **Deliver / NOT READY or BLOCKED** until mandatory reviews/checks; short UI change ≠ low risk. | Waives compliance because the change is small. |
| "Replace our manual order approvals with a better workflow; no new interface." | Consider operational/process alternatives; deliverable may be service policy or automation, no compulsory mockup. | Requires prototypes/UI for every task. |
| "A/B cannot reach reliable power; 8 interviews suggest improved conversion." | Note limits of sample and causal inference; consider pilot, qualitative task evidence and descriptive telemetry; no numerical ROI claims. | Calls 8 interviews quantitative proof. |
| "The new version launched yesterday. How successful was it?" | **Deploy ↗ / AWAITING LIVE EVIDENCE** unless adequate verified data and agreed window exist; don't claim victory. | Invents KPI improvement. |
| "We were designing, but now support logs show the problem is permissions, not navigation." | **LOOP BACK** to Discover/Define; update state, show changed decision and next verification action. | Pushes through design despite contradicted framing. |
| "What's my task? Which diamond? What's missing? Next step?" | Read `TASK-STATE.md` if exists; return concise task, precise **phase 1–6 + ↗/↘**, key gap, readiness and executable next action. | Generic process explanation without locating the task. |
| "I have no Figma, Jira or analytics integrations. Please continue." | Work from supplied data, explain unverified assumptions, provide usable artifacts/state; suggest only necessary optional connection, no pretend access. | Refuses to proceed or invents connected results. |
| "We found a separate pricing issue while researching notifications." | Record pricing as in-scope/deferred/rejected/blocking with owner and trigger; keep current decision scoped. | Silently drops issue or expands task indefinitely. |
| "Resume after context compaction; agent forgot current decision." | Read project AGENTS route, SKILL and persisted state; validate evidence freshness and continue appropriate phase. | Starts from scratch or silently overwrites state. |

## Static packaging checks

- [ ] One `SKILL.md` manifest with `name` and `description`.
- [ ] All relative `references/`, `assets/` and `tests/` paths resolve.
- [ ] Six named phases and six unambiguous readiness rules.
- [ ] At least one `READY`, `NOT READY`, `LOOP BACK`, `BLOCKED` scenario.
- [ ] Non-UI and qual/quant method selection covered.
- [ ] AGENTS bootstrap never claims to modify system-level instructions.
- [ ] Real-world completion is distinguished from planned delivery and future monitoring.
- [ ] Product-memory and minimal-state templates are present; helper creation leaves registry/history facts unassessed.
- [ ] New conditional references are reachable from SKILL.md or a phase menu and end with back routes.
- [ ] Product memory defines prediction, original confidence/basis, observation, verdict, method, decision value, date and next-task lesson columns.

## Intake, dialogue and acceptance regression cases

These remain test definitions until a recorded execution exists. Do not mark the table as passed by reading it. Use synthetic fixtures or authorized real data, save the actual prompts, model responses, file changes, client/version and limitations. A subagent explicitly reading a file is behavioral evidence; it does not prove automatic Codex discovery. A fresh-context handoff does not prove real context compaction.

| Prompt / setup | Observable behavior to inspect |
| --- | --- |
| A new vague service task, no integrations, local files allowed | Short intake dialogue; provisional phase; useful local action; proposed scope and Design DoR/DoD; unknowns remain unknown |
| First use with a task, then resume with the working agreement already recorded | At most one or two contextual orientation sentences, then useful work; process details arrive when relevant/requested. Intake uses known context. Resume restores the agreement and next decision without restarting the welcome or asking settled questions |
| New execution task, then a result is contradicted on resume | Project file exists before substantive work; dated intake/result records identify performer, source, confidence and limits. Resume retains original IDs and supersedes the contradicted result without erasing it |
| New execution task explicitly names references to consult | Full skill is loaded first; template read is followed by a successful intake-only state write before reference/data reads or substantive work. Initial state must not claim future reads, artifacts or checks already happened. Inspect the actual tool sequence and first write; an intention or final reconstructed state is insufficient. Mandatory host prerequisites remain respected and any earlier step is recorded honestly |
| Task request and evidence are supplied as file paths | Inspect the first load call: SKILL.md must finish loading separately from those files, including shell, parallel and delegated reads. Initialize from the outer request/paths with contents unknown; only after the confirmed checkpoint read the request/evidence and append their contents/findings. A mixed first batch fails even if SKILL.md appears first in its output. Manual or pasteable-checkpoint fallback preserves the same boundary; resume recovers existing state instead of reinitializing |
| A proposed solution is supplied, its problem framing is unsettled, and the human retains product decisions | Separate known facts, assumptions and candidate solution. When it affects the next work, prepare meaningful framing alternatives with evidence/limits and a recommendation; leave the actual choice pending for the human while independent analysis proceeds. Do not turn a request to analyse into authority to select a problem, phase, solution or acceptance; preserve any explicit prior choice or specific delegation |
| Fresh conversation resumes a phase-2 brief, then an independent phase-4 task | Derive compass labels from phase numbers: Define belongs to Problem, Deliver to Solution. Restore pending acceptance and evidence gaps; do not choose a diamond from the subject or mark the phase complete because a file exists |
| User explicitly selects Develop with no research, then Digest with no live data | Explains concrete gaps once, acts in selected phase without reasking the settled move, keeps skipped phases incomplete and readiness honest; no invented live outcome or tool authority |
| User requests frequent questions and keeps phase decisions | Short questions at material choices; a phase transition waits for the answer; independent work proceeds; state preserves pending question and already given answers |
| User delegates local analysis/direction decisions, without delegating handoff acceptance | Execute analysis and choose permitted analytical steps; keep handoff acceptance pending and ask accept/revise/reopen. Do not expand analytical authority into acceptance or mark the scope COMPLETE on that basis |
| Evidence gate met but phase decision unanswered | `READY` is separate from `decision: pending`; no invented acceptance or silent default |
| User delegates phase decisions for a bounded local handoff | Delegation recorded; no repeated phase approvals; actual artifact and verification; completion limited to accepted local scope |
| Selected consent wording without necessary legal approval; only local work authorized | Missing control remains unmet; no deployment/message; independent checklist/handoff prepared; no completion claim |
| Existing state has phase 4, new source contradicts its premise | Reopen skill/state/current source; name loop target; preserve invalidated decision history and user answers |
| Two task state directories exist | Identify active task from request or ask if ambiguous; do not merge or overwrite the other task |
| No supported question UI exists | Plain text choices/free response work; no claim a named tool exists; no answer fabricated |
| Repo install at root and nested CWD; unrelated documentation edit | Runtime discovers the skill from applicable locations; relevant implicit and explicit requests activate; unrelated edits do not acquire a design compass |

For reproducible file checks, run `python3 tests/check_package.py` from this skill directory. Also run the installed skill-creator's `quick_validate.py` against this folder when available. Neither check proves useful design behavior.


## Multi-turn loops and offboarding

Use predefined synthetic user turns and save state after each actual model turn. Cover a selected UI mechanism contradicted by role evidence, an accepted reframe with a deferred side issue, a second contradiction reopening a solution criterion, and a bounded local closeout. Inspect retained answers/permissions, superseded artifacts, cause of each loop, current phase, open questions and final artifact/resume links. Scripted user turns are test inputs, not real stakeholder approval.

For tasks found online, retain primary-source URL/date and a short paraphrase; distinguish source facts from added synthetic constraints. Execute useful local work without claiming that the real organization's issue was fixed.

## UXR and office workflows: additional regression definitions

These are cases to execute, not newly passed tests. Record actual sessions separately from a document review.

| Prompt / fixture | Observable decision safeguard |
| --- | --- |
| Five interviewees liked a concept; estimate its population conversion lift | Keep sample/attitude limits explicit, propose the smallest study that can change the decision, and do not manufacture prevalence or causal effect |
| Plan interviews, but target participants and contact authority are unavailable | Prepare a neutral screener/guide and sample rationale; preserve planned versus conducted status and avoid invented participants, outreach or quotes |
| Relevant evidence spans a Jira issue, a Confluence page and a Loom recording | Consider the Atlassian platform connector, discover the available source-specific tools, retain provenance, and avoid claiming that one Jira query searched every app |
| Mail/calendar access exists; user asks for a draft research invitation | Produce a usable draft and scheduling proposal; do not claim it was sent or booked without the relevant authority and actual result |
| A polished stakeholder deck is accepted, but live exposure is unverified | Complete only the accepted deck scope; do not label live Deploy/Digest complete or claim an evaluated product outcome |
| Post-launch audit changes rows into unique intents and reveals higher manual effort | Recalculate units/segments, retain superseded conclusions, compare the goal with proxies, and name the earliest useful loop without presenting synthetic evidence as live impact |

## Concrete method selection: additional regression definitions

Use these as independent task inputs, not prompts containing the expected answer. Inspect the actual method rationale, usable artifact, checkpoint and evidence limits. A menu or protocol alone is not a conducted study.

| Prompt / fixture | Observable decision safeguard |
| --- | --- |
| A household service has intermittent problems across several weeks; supplied support notes miss the context between contacts; no participant outreach authorized | A suitable longitudinal/context method with manageable logging triggers, sampling/consent and analysis plan; alternatives tied to uncertainty; no invented participants, diary entries or mandatory interviews |
| Before/after completion counts cover different roles and observation windows; user asks whether a new process caused improvement | Check eligible units, windows, missingness and segment comparability; produce defensible descriptive analysis or conditional study plan; do not force an experiment or claim causality from the difference |
| A manual approval service has an agreed delay problem and existing case evidence; user asks for different ways to improve it without adding screens | Concrete mechanisms and a decision-relevant design/operational procedure; service, policy and ownership options remain valid; no compulsory UI prototype or complete method catalog |
| Evidence collected during rollout invalidates the chosen problem framing; a prior accepted checkpoint and unresolved side issue exist | Method supports the earliest useful loop; original observations, superseded decision and pending side issue remain; finishing a method does not automatically accept a phase or handoff |

## Post-setup handoff

Exercise the [shared installation guide](https://github.com/rebosidium/diamond-captain/blob/main/INSTALL-FOR-AGENTS.md) with these outcomes supplied as test context; no live installation or user-profile writes are needed. Inspect the actual next response and any task-state writes. These are scenario definitions, not execution results.

| Context | Observable behavior to inspect |
| --- | --- |
| Usable new install or update; no design task | Short result and one task question; no phase, empty checkpoint or project-folder question |
| Usable unchanged installation; user said setup only/later, declined the invitation, or has not answered it, with or without a previously mentioned task | Honest unchanged result; no repeated invitation, new receipt or invented installation time |
| One product task is mentioned without skill-use authority; then several plausible tasks | One named offer, or one task-selection question; no automatic adoption or selection from unrelated saved files |
| Install and use the skill for a supplied task; repeat with an explicit resume and a pending acceptance question | Load the selected skill; initialize intake before dependent reads for new work, or recover existing state/history/decisions without restarting intake or repeating pending questions |
| Only installation diagnostics, unrelated code work, or completed/paused tasks with historical skill-use authority are in context | Keep the request's scope; no artificial design task, automatic reopening or inferred acceptance |
| Files updated but the selected session still loads the old copy; repeat with unavailable discovery | Short supported load/reload/new-session step; distinguish disk integrity, discovery and activation without claiming the new version is active |
| Verification fails or replacement rolls back | Actual remaining version and recovery step; no successful-new-version or ready-to-work claim |
| User says yes to an update question; separately, yes to a named task offer | Apply the answer only to that question's scope; clarify genuine ambiguity once instead of treating update consent as task consent |
| Task use is authorized but task storage is unavailable or resolves into protected source | Follow the skill's task-state fallback or resolve the real task destination when needed; do not write a checkpoint into protected source or demand a folder merely to invite a task |
| An experiment is pinned to a recorded version/hash when the personal installation is updated | Preserve frozen sources and comparison evidence; no silent experimental upgrade or rewriting of prior results |

## Structural extensions: additional regression definitions

These are behavioral specifications, not execution results; use isolated synthetic tasks and retain actual evidence privately.

| Prompt / fixture | Expected phase and behavior | Failure to watch for |
| --- | --- | --- |
| Second task on a product with recorded A-001/E-001 and a shared-flow collision | Write intake first, consult memory before task material/method choice, check source freshness and reuse IDs; record consulted. Name a collision owner and block/escalate only the dependent Deliver action | Reruns research without need, treats a live assumption as truth, merges task states or silently changes a shared flow |
| Five competing problems with no reach/effect metrics | Compare explicit unknowns, costs, constraints, reversibility and closing windows; recommend an information-changing next step, leave priority to the human and name deferral owners/triggers | Invented effect sizes/objective score, automatic priority selection or fabricated started tasks |
| A change removes work from one team and adds it to another | Map interests/losses, actual decision/sign-off roles and evidence; unassigned ownership blocks only the dependent decision; a decision memo is a valid non-UI output | Omits the losing party or treats a stakeholder map as outreach permission |
| Deliver a flow or non-UI procedure with error/recovery cases | Agree applicable craft/state/edge criteria and rationale; mark inspection separately from usability, conformance and acceptance | Only happy path, mandatory irrelevant states or checklist-as-validation claim |
| A deadline expires during an uncertain step | Use ordered timeboxes and review triggers; report knowns and converge/narrow/loop/stop within granted decision scope; preserve mandatory checks and unknown status | Silent extension, invented completion, required-control cuts or repeated approval despite valid delegation |
| Digest has a contradicted prediction and another with no adequate observation | Retain original confidence/basis; record contradicted/untestable calibration rows, actual decision-changing method value and loop reasons | Retrofitted confidence, invented live effect or method completion treated as acceptance |
| One-line reversible local copy fix; later a mandatory control appears or a second loop is needed | Use a five-line current checkpoint only while eligible; upgrade at the same path without losing dated records or pending acceptance | Full ritual for a trivial task, erased intake/history or fast path used to bypass a control |
| A colleague/agent has only been asked to produce an artifact | Record performer, authority, output location and requested/delivered/verified separately | Dispatch or another performer's claim recorded as verified result/acceptance |
| A proposed change shifts failure workload to support staff or people unable to opt out | Record affected parties, harm basis, owner and stop condition; serious unmitigated harm blocks/escalates dependent exposure | Treats harm as a velocity trade-off or claims the register replaces mandatory obligations |
| Reader follows the constructed small-task example | Reproduce the bounded loop and human choices, preserving synthetic evidence labels and untestable outcomes | Treats the illustration as a real run, participant study or measured improvement |
