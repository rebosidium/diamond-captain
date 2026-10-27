# UXR: from a research question to a design decision

Read the relevant section when planning, conducting or analysing user research. Use [research guardrails](research.md) for depth, evidence limits and stopping rules. Execute permitted analysis of existing material now; a new study is useful only if its answer could change a decision. This guide does not require a research programme for every task.

UXR can expand or narrow **any** diamond: investigate alternative causes in Discover, justify a framing in Define, compare mechanisms in Develop/Deliver, and investigate real use or unintended effects in Deploy/Digest. A session count or polished report is not a phase gate.

## Frame the study and its decision

Reuse the brief, state and existing evidence. Make the smallest study plan that names:

```text
Decision and owner; current phase / selected scope:
Question, competing explanations and what would change the decision:
Known evidence / source dates; material gaps:
Method; target population / roles / contexts; sampling rationale:
Protocol and success/observation definitions; prototype or exposure version:
Collection/analysis owner; permitted access and participant-contact authority:
Participant information, consent/recording and approved storage arrangements:
Review point / stop rule; output location and next decision:
```

Clarify only choices not already settled or delegated. Distinguish business goals, user needs, research questions and interview questions: “reduce missed visits” is a goal, “which handoff creates uncertainty?” is a research question. Decide what evidence would challenge the preferred explanation. See [planning research](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service).

## Select a method that can answer the question

| Question / uncertainty | Useful method | What the result does not establish alone |
| --- | --- | --- |
| How work happens, including handoffs and workarounds | Contextual observation, service walkthrough, recent-event interviews | Population frequency or a causal effect |
| Why people describe a problem or choose a workaround | In-depth interviews grounded in concrete examples | Actual behaviour just because an intention was stated |
| Can someone complete the intended task? | Moderated or suitable unmoderated usability testing | Product-market fit or production reliability |
| Which proposed mechanism meets the need? | Concept comparison, low-cost prototype or process-role walkthrough | Demand from compliments or visual preference alone |
| Can people find information and understand labels? | Card sorting for structure, tree testing for findability | A whole service's usability from one navigation test |
| What happens over time or across contexts? | Diary study, follow-up interviews, field observation | Unbiased completeness of self-reported diaries |
| How common is a reported attitude or difficulty? | A suitably sampled survey or quantitative usability study | Representativeness from convenience sampling |
| What changed during rollout? | Usage/operations data plus targeted follow-up research | Causality from a before/after difference |
| Does a change cause a measured difference? | An appropriate controlled experiment when feasible | Reliability without sound assignment, instrumentation and sufficient data |

Qualitative/quantitative and attitudinal/behavioural are different dimensions; methods may combine them. Choose a complementary sequence when it resolves uncertainty, not as a universal requirement. [Method choices and templates](https://digital.defra.gov.uk/user-research/research-methods) · [Quantitative UXR methods](https://www.nngroup.com/articles/quantitative-user-research-methods/).

## Recruit the relevant people

Specify inclusion/exclusion criteria tied to actual roles, behaviour and context. Consider meaningful variations such as new/experienced users, affected staff, assistive technology, language and access needs. A stakeholder, colleague or AI persona is not automatically a target user. AI-generated reactions can help rehearse a protocol; label them synthetic and never count them as participants or quotations from real users.

Use a neutral screener without revealing the desired answer. Record recruitment source, coverage gaps, incentives/budget and practical access needs. Give a sampling rationale: small qualitative rounds can reveal problems but cannot estimate prevalence; quantitative comparisons require a design and sample suitable for the requested precision/effect. Do not impose a universal participant count or claim saturation from an arbitrary number. [Recruitment guidance](https://design.homeoffice.gov.uk/user-research/participant-recruitment).

Prepare outreach and scheduling artifacts if useful; send, book or pay only within actual authorization. Use participant codes in analysis and keep identity/contact data in approved storage. Pseudonymisation alone does not guarantee anonymity. Confirm voluntary participation, recording permission, access/retention and any required organisational process before collecting the relevant data. [Research consent](https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research).

## Run a session or prepare an executable protocol

For interviews, ask about a recent concrete episode: “Tell me about the last time this happened.” Probe sequence, people involved, constraints, consequences and actual workarounds; request an example when appropriate. Keep a discussion guide, but follow relevant surprises. Avoid leading questions such as “Would this easier screen solve it?” [Interview guidance](https://www.gov.uk/service-manual/user-research/using-in-depth-interviews).

For usability work, give a realistic goal without naming the controls or path. Define success, errors, abandonment and assistance before interpreting results. Check the prototype/service version and materials; a rehearsal checks the protocol, not target-user validity. Record moderator interventions and distinguish independent completion from assisted completion. Check accessibility of the session itself. Prototype task success is not proof of production implementation. [Moderated testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing).

Keep participant code, context, task/version, observation or quote locator, assistance and outcome. Mark quote versus paraphrase versus interpretation. A prepared guide remains planned work until sessions actually occur; do not invent participants, recordings or findings when access is missing.

## Analyse qualitative and quantitative evidence

For qualitative material, preserve source locators and code observations before grouping themes. Keep counterexamples and differences between roles or contexts. Separate frequency in the observed sample, consequence/severity and confidence; several excerpts from one participant are not several users. Retain alternative explanations and note how researcher/moderator involvement may have affected the result. [Session analysis](https://www.gov.uk/service-manual/user-research/analyse-a-research-session).

For surveys and behavioural measures, apply the [data checks](research.md#make-research-executable) before calculating: unit, event definition, unique people/intents versus rows, denominator, exposure/version, missingness, comparable periods and segments. Report counts with rates and uncertainty appropriate to the design. Self-reported ease, successful prototype tasks and completed real-world outcomes are distinct measures. Do not treat response bias, duplicate records or changing customer mix as evidence of a design effect.

Turn material findings into a compact chain in existing artifacts:

`source observation → interpretation / alternative explanation → confidence and limits → decision affected → next check / owner`

Use an evidence table, journey, theme map or report only when it helps that decision. Never create personas, a journey map and a deck merely to complete a research checklist.

## Converge, loop and hand off

Compare findings with the original question and agreed criteria. State which explanation or option became more/less credible, what remains unknown and why further research would or would not change the next action. Recommend proceed, reframe, compare another mechanism, bounded pilot, further research or stop. New evidence can reopen Define, Develop or delivery criteria; preserve the earlier decision and label it superseded rather than deleting it.

Record the study status honestly: planned, recruited, conducted and analysed are different facts. Save source/method/version, coverage and limitations, actual author/performer, result IDs, changed decision, pending acceptance and owner/review trigger in the task checkpoint or linked artifact. A study can finish with “insufficient evidence”; the study's completion does not imply that the solution works or that a live outcome has been achieved.

Finish with the usable result, actual checks, evidence boundaries, what the user needs to decide and the resume line required by the skill. Keep participant material in its approved location; a research summary does not authorize sharing raw recordings, updating Jira/Confluence or contacting participants.
