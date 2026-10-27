# Six-stage process

**Problem:** Discover → Define. **Solution:** Develop → Deliver. **Outcome:** Deploy → Digest. Each pair moves from exploration to a focused decision.

**Actions are optional.** Scale them to the task; existing release, accessibility and compliance requirements still apply. Move forward on a documented decision with explicit uncertainties, not a completed checklist. Output artifacts become the next stage's inputs; retain earlier evidence and the agreed brief. Reuse artifacts rather than creating separate documents by default.

Designer goals explain purpose, not sole ownership: collaborate with product, engineering, research and analytics throughout. Each mode is dominant, not exclusive; stages can overlap and loop. Product user stories remain separate artifacts.

## Research and decision guardrails

**Scale the work to uncertainty, potential impact and reversibility—not the size of the interface.** Reuse credible existing evidence first. A small, reversible fix may only need a reproducible issue and verification; a high-risk change may need deeper research even if it affects one sentence.

**Start with the decision, not a preferred research method.** For each material uncertainty, identify: **decision → question → existing evidence → method (if needed) → review point → finding and owner**. Keep this in the existing task or brief rather than creating a document by default.

**Qualitative and quantitative research answer different questions. Neither belongs exclusively to diverging or converging.**

| Research question | Qualitative examples | Quantitative examples |
| --- | --- | --- |
| What is happening, and why? | Contextual observation, interviews about actual work, support-case review | Funnel and event analysis, error rates, segment comparisons |
| Which approach works better? | Concept evaluation, moderated usability testing, workflow walkthroughs | Task-success and error measures, surveys with suitable samples, controlled experiments when feasible |
| What changed after launch? | Follow-up interviews, field observations, feedback analysis | Usage and operational metrics, cohort trends, experiments where justified |

Interviews alone do **not** establish prevalence. A metric difference does **not** explain its cause; an observed change does **not** automatically prove that the design caused it. Check data quality, comparability and uncertainty before claiming an effect. No fixed number of interviews, tests or prototypes applies to every task.

**Protect against three failure modes:**

- **Skipped questions:** Keep material unknowns visible. For each, decide whether it is **in scope**, **deferred** (with owner and revisit trigger), **rejected** (with rationale), or **blocking**. Mandatory safety, legal, accessibility and release obligations still apply.
- **Premature convergence:** Consider plausible alternative *explanations* in Discover and alternative *mechanisms* in Develop—including process, policy, content or service changes, not only interface variations. Capture significant alternatives without exploring everything.
- **Endless divergence:** Investigate a specific decision-changing question. Agree on scope and a review point in advance; expand only when new evidence could change the decision or expose material risk. Converge with an explicit rationale and remaining uncertainty, or choose further research, a bounded pilot or no-go.

| Diamond | What to broaden | What enables a reasoned narrowing |
| --- | --- | --- |
| **Problem** | Causes, affected roles, contexts | Evidence-backed problem, target and material unknowns |
| **Solution** | Mechanisms, trade-offs, risks | Comparison against user value, feasibility and risk |
| **Outcome** | Observed behavior, varied feedback, unexpected effects | Assessment against baseline and goals, with limitations and next decisions |

These are **decision safeguards**, not mandatory workshops or stage gates. The goal is enough appropriate evidence for the next defensible decision—not maximum research coverage.

## 1. Discover — Research

**Problem · Diverge:** Explore user needs, context and possible causes before choosing a problem.

**Designer goal:** *As a designer, I want to investigate user needs and constraints so that the team understands the problem beyond the initial request.*

**Input artifacts**
- Initial request, opportunity or feedback from a previous cycle.

**Optional actions**
- [ ] Clarify the request, intended value, assumptions and open questions with product and relevant stakeholders.
- [ ] Review existing research, analytics, support feedback and relevant market context.
- [ ] Observe or speak with users; map current flows and unmet needs.
- [ ] Explore technical, data, operational and policy constraints with the relevant teams.

**Output artifacts → input to stage 2**
- Discovery evidence: user needs, current flows, constraints and open questions.

## 2. Define — Problem framing

**Problem · Converge:** Synthesize evidence and choose a focused problem and measurable goal.

**Designer goal:** *As a designer, I want to turn research into a focused brief so that the team agrees on the problem worth solving and the expected change.*

**Input artifacts**
- Discovery evidence: user needs, current flows, constraints and open questions.

**Optional actions**
- [ ] Synthesize findings, distinguish evidence from assumptions and prioritize the problem.
- [ ] Define the goal, product user story or job story, scope and constraints.
- [ ] Agree on success measures, baseline, target, review window and decision owner.
- [ ] Agree whether to proceed, reframe, research further or stop; record unresolved assumptions.

**Output artifacts → input to stage 3**
- Agreed brief: problem, goal, user/job story, scope, constraints, measurement plan, decision and owner.

## 3. Develop — Solution exploration

**Solution · Diverge:** Explore alternative solutions and learn through low-cost experiments.

**Designer goal:** *As a designer, I want to explore alternative solutions so that the team can compare trade-offs instead of committing to the first idea.*

**Input artifacts**
- Agreed brief: problem, goal, user/job story, scope, constraints, measurement plan, decision and owner.

**Optional actions**
- [ ] Generate solution hypotheses and alternatives with the team.
- [ ] Use relevant products and existing design patterns as inspiration, not proof.
- [ ] Create lightweight flows, wireframes or prototypes.
- [ ] Explore assumptions with users and engineers; record evidence, trade-offs and unresolved risks.

**Output artifacts → input to stage 4**
- Solution options: hypotheses, prototypes, early evidence, trade-offs and risks.

## 4. Deliver — Selection & implementation

**Solution · Converge:** Choose, refine and implement a solution ready for real use.

**Designer goal:** *As a designer, I want to select and refine a solution with the team so that the implemented experience is usable, feasible and ready to evaluate.*

**Input artifacts**
- Solution options: hypotheses, prototypes, early evidence, trade-offs and risks.

**Optional actions**

*Select*
- [ ] Choose evaluation criteria and methods; test options against the brief.
- [ ] Select a direction with a rationale, or reject the options and return to Develop or Define.

*Design*
- [ ] Detail the selected solution—interface or service workflows, content, edge cases, accessible interactions and operational handoffs; reuse established patterns.
- [ ] Test the experience with users or affected roles; review findings with the team and refine.

*Implement*
- [ ] Document the intended behavior or process change and check implementation with engineering or other delivery teams.
- [ ] Verify tracking and launch readiness with relevant teams; prepare rollout and customer/support communication as needed.

**Output artifacts → input to stage 5**
- Release package: implemented change (interface, service, process, content or pilot), delivery notes, quality checks, tracking and rollout plan.

## 5. Deploy — Use & observation

**Outcome · Diverge:** Broaden evidence through real use, including unexpected outcomes.

**Designer goal:** *As a designer, I want to observe the solution in real use so that the team understands both intended and unexpected outcomes.*

**Input artifacts**
- Release package: implemented change (interface, service, process, content or pilot), delivery notes, quality checks, tracking and rollout plan.

**Optional actions**
- [ ] Support a pilot or rollout and record who received which version and when.
- [ ] Collect behavioral metrics and feedback from users, support and affected teams.
- [ ] Observe varied user contexts and unexpected use, failures or workarounds.
- [ ] Keep an evidence and issue log for the review window; escalate serious problems immediately.

**Output artifacts → input to stage 6**
- Usage evidence: analytics, feedback, observations, issue log and rollout context.

## 6. Digest — Evaluation & next decisions

**Outcome · Converge:** Interpret evidence and decide what to keep, change or investigate next.

**Designer goal:** *As a designer, I want to assess outcomes against agreed goals so that the team can decide what to keep, improve or investigate next.*

**Input artifacts**
- Usage evidence: analytics, feedback, observations, issue log and rollout context.

**Optional actions**
- [ ] Compare usage evidence with the goals and success measures in the brief.
- [ ] Synthesize feedback and assess uncertainty; distinguish observed changes from evidence of causality.
- [ ] Decide whether to keep, improve, roll back, stop or research further; prioritize follow-up work and design debt.
- [ ] Share findings, assign follow-up owners and route work to the relevant earlier stage.

**Output artifacts → next iteration**
- Outcome review: findings, limitations, decisions and prioritized follow-up work.

[Back to overview](../README.md)
