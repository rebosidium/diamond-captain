# Research, depth and stopping rules

**Method choice starts with a decision, not a tool.** Ask which conclusion or action would change based on the answer. Reuse credible existing evidence first; new research is optional when it would not alter the decision.

For a concrete user study, read the relevant part of the [UXR guide](uxr.md): study decisions, method choice, recruitment, session protocols, analysis and research handoff. Keep it conditional; do not load or perform every method for an ordinary task.

When the procedure is unclear, use the [current phase's method menu](methods/README.md) and selected [qualitative](methods/qualitative.md) or [quantitative](methods/quantitative.md) cards for when to use it, steps, output and limits. Existing evidence may instead need a [synthesis/design method](methods/design-and-delivery.md); no new study is implied.

## Choose evidence suited to the question

| Need | Qualitative options | Quantitative options | Limitations |
| --- | --- | --- | --- |
| Understand motives, context, workarounds | Contextual inquiry, interviews about actual work, moderated usability testing | Segmented behavior trends and event patterns to locate friction | Interviews cannot establish prevalence; event data may lack explanation |
| Estimate reach, severity and frequency | Support case taxonomy, structured observation | Funnels, error and completion rates, appropriately sampled surveys | Biased samples, missing events and selection effects can mislead |
| Compare approaches | Concept testing, task walkthrough, moderated prototype tests | Task success/time/error, controlled experiment when viable | A small convenience sample is not a reliable population estimate |
| Evaluate live outcome | Follow-up fieldwork, feedback/diary studies | Baseline vs follow-up, cohorts, A/B test if justified and possible | Correlation is not automatically causation |

Qual vs quant **is not** the same as diverge vs converge. Either can expand possible explanations or narrow a decision. Prefer a **mixed-method sequence** only where complementary evidence changes decisions (e.g., analytics identifies a drop-off; observation explains it; experiment evaluates a remedy).

## Make research executable

For a research action record the decision, question, method, source/sample selection, collection or analysis steps, review/stop rule, responsible person and artifact path. Execute permitted analysis of supplied files now. For new participants, prepare a usable guide/tasks and recruitment/consent/data handling plan appropriate to the setting; do not contact or book anyone without authorization. Ask the user about decision-changing trade-offs, not facts already in the data.

Before calculating rates/effects verify numerator and denominator, unit (people/sessions/events), population and segment, dates/timezone, missing/duplicate events, exposure/version and comparable windows. Preserve the source/query or local calculation. Label synthetic test fixtures as synthetic. Baseline-vs-follow-up rates can be descriptive even when an experiment lacks power; do not turn them into causal evidence. A qualitative finding, observed count, modeled estimate and causal estimate are different claims.

At the review point synthesize what changed the decision, contradictory observations, limits and remaining unknowns; offer a concrete next decision. If blocked on live research or access, finish the protocol, analysis or handoff that can be done independently and save the blocked action. Do not mark a protocol as collected evidence.

## AI-dependent product behavior

Use when designing or evaluating a feature whose behavior depends on a model, including classification, recommendations or generation. Apply only checks relevant to the decision and consequences; retain existing phases, human choices and checkpoints. Model-output evaluation, human usability research and live service outcomes answer different questions.

- **Cases and criteria:** Define representative tasks, contexts, serious failure conditions and an inspectable scoring rubric for the human's acceptance decision. Record case provenance, permissions and synthetic labels; keep evaluation cases separate from tuning examples where possible and disclose reuse or coverage gaps. Choose repeated trials per case according to variability and consequences; report cases, attempts, failures and uncertainty separately. Repeated outputs are not additional users or independent cases.
- **Configuration and grading:** Record the known tested model/version, prompt, relevant retrieval/data, tools, settings and material unknowns; label simulated versus live behavior. Check automated grades against human-labelled examples and reconcile material disagreements before relying on an LLM judge; retain evaluator limitations. A single successful demonstration does not establish reliability. See [evaluation practice](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
- **Measures and UXR:** Select decision-relevant measures with denominators and severity: task success, unsupported claims, harmful output, appropriate versus mistaken refusal, cost and latency. Evaluate by relevant context/version; an average can hide serious failures. Use [UXR](uxr.md) to test whether people understand limitations, detect/correct errors and recover; offline scores alone do not establish user benefit.
- **Viability and recovery:** Include inference/tool costs, retries, human-review workload, latency variation, quotas and provider withdrawal in plausible demand ranges. Exercise wrong output, unavailable dependencies, escalation and fallback with actual reviewer capacity. For action-taking features, test permission boundaries and recovery from unintended actions. Version the configuration needed for rollback; verify available provider versions and a feasible fallback rather than promising exact reproduction. Recheck quality, cost and latency after changes and during live observation.
- **Data and synthetic material:** Before sending research or user data to a model, confirm authorized access, data minimization and applicable provider/storage rules, including retention, logging and training use separately. Generated claims are not observations of people or external events. Label generated or simulated rehearsals, fixtures, edge cases and load data as synthetic; preserve the provenance of real material. Synthetic cases can exercise behavior but cannot establish participant findings or population prevalence. Verify AI-assisted research codes/summaries against source passages and retain counterexamples.

Keep the tested configuration, evidence limits, pending human decision and next check in the existing checkpoint or linked artifact. Reuse [harm and risk guidance](harm-and-risk.md) for affected people, serious failure and stop authority. No extra state fields or universal trial count are required.

## Right-size the task

Assess **uncertainty, consequence of error, reversibility, reach, regulatory/accessibility risk, data quality and dependencies**.

- **Lightweight:** Known low-risk, reversible issue; reproduce it, inspect existing standards/evidence, implement, verify, note impact.
- **Standard:** Some uncertain assumptions and affected users; compare plausible explanations and approaches, validate the most consequential risks.
- **Deep:** High-cost, irreversible, safety-sensitive, broad/regulated or ambiguous work; research triangulation, ownership, explicit evaluation design, staged rollout where feasible.

Do not give exact interview/sample counts without a defensible sampling rationale. Never claim an A/B test can give reliable answers without adequate traffic, instrumentation or experiment design.

## Stop or continue?

At the start of an exploration, specify:
1. **Decision:** What will this evidence change?
2. **Question:** What needs answering?
3. **Known:** Which credible data already exists?
4. **Method:** What is the smallest credible method?
5. **Review point:** When/how will we assess sufficiency? State a clock/session budget and review date/trigger, not only a condition.
6. **Failure condition:** Which contradictory finding or serious risk warrants reopening?

At review:
- **Converge** if remaining unknowns no longer materially affect the decision at accepted risk.
- **Narrow the question** if work keeps expanding without a new decision to unlock.
- **Loop back** if a core assumption is contradicted.
- **Pilot** if a controlled and reversible release can teach safely.
- **Stop / no-go** if the change is unjustified, unsafe, infeasible or unsupported.
- **Hold/block** if a legally or operationally necessary condition is absent.

Do not equate "time ran out" with "hypothesis confirmed"; document uncertainty honestly.

## Unknowns and discoveries

For each material item record `in scope`, `deferred`, `rejected`, or `blocking`. Deferred items need an **owner and trigger**. Note significant out-of-scope discoveries without hijacking the current task.

State each material confidence label with its basis and what would falsify the claim, so Digest can compare the original prediction with observations rather than rewrite it.

Always distinguish **observed data**, **interpretation**, **hypothesis** and **decision**. Support causal claims with an appropriate design; otherwise describe association/observed change.

## Non-UI tasks

Research and deliverables can include process redesign, support scripts, customer letters, risk/policy changes, training, internal operations, manual workflows, or automation. Do not manufacture a mockup just because the skill is used by a designer.
