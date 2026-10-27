# Acceptance scenarios for Diamond Captain

These are **behavioral test cases and expected responses**, not claims that a live Codex session, users or external tools were tested. Run them in fresh sessions after installing the skill. Check reorientation, evidence handling, appropriate action and non-fabrication.

| Prompt / fixture | Expected phase and behavior | Failure to watch for |
| --- | --- | --- |
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

## Intake, dialogue and acceptance regression cases

These remain test definitions until a recorded execution exists. Do not mark the table as passed by reading it. Use synthetic fixtures or authorized real data, save the actual prompts, model responses, file changes, client/version and limitations. A subagent explicitly reading a file is behavioral evidence; it does not prove automatic Codex discovery. A fresh-context handoff does not prove real context compaction.

| Prompt / setup | Observable behavior to inspect |
| --- | --- |
| A new vague service task, no integrations, local files allowed | Short intake dialogue; provisional phase; useful local action; proposed scope and Design DoR/DoD; unknowns remain unknown |
| First use, then resume with the working agreement already recorded | Brief user orientation covers result, collaboration/decisions, checkpoint and final handoff; the task intake uses known context. Resume restores the agreement and next decision without restarting the welcome or asking settled questions |
| New execution task, then a result is contradicted on resume | Project file exists before substantive work; dated intake/result records identify performer, source, confidence and limits. Resume retains original IDs and supersedes the contradicted result without erasing it |
| User explicitly selects Develop with no research, then Digest with no live data | Explains concrete gaps once, acts in selected phase without reasking the settled move, keeps skipped phases incomplete and readiness honest; no invented live outcome or tool authority |
| User requests frequent questions and keeps phase decisions | Short questions at material choices; a phase transition waits for the answer; independent work proceeds; state preserves pending question and already given answers |
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
