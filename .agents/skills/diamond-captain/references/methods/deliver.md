# Deliver ↘ · Solution

Select, refine and realise a supported solution. Ask: can relevant people complete the task, can the service operate, and what must be verified before exposure? Match evaluation to the actual risk; no single test establishes overall readiness.

| Question or gap | Candidate | Prefer when… |
| --- | --- | --- |
| Why does a realistic task fail? | [QL-05 Moderated usability](qualitative.md#ql-05) | Direct observation and follow-up can diagnose difficulties. |
| What breaks between service moments? | [QL-08 Service walkthrough](qualitative.md#ql-08) | Digital, staff and offline interactions must connect. |
| Will the wording support the right action? | [QL-15 Comprehension test](qualitative.md#ql-15) | Errors depend on understanding instructions, conditions or messages. |
| Is task performance changing? | [QT-10 Task benchmark](quantitative.md#qt-10) | Comparable tasks, success criteria, users and versions exist. |
| Can people find the destination? | [QT-11 Tree testing](quantitative.md#qt-11) | Hierarchy/labels are the uncertainty; full-service performance is separate. |
| Is the first action apparent? | [QT-12 First-click testing](quantitative.md#qt-12) | A navigation cue can be tested before a complete build. |
| How usable did it feel after use? | [QT-20 Usability questionnaire](quantitative.md#qt-20) | A validated instrument fits the context; pair perception with behaviour. |
| Which supported option should proceed? | [DS-12 Criteria-based choice](design-and-delivery.md#ds-12) | Value, feasibility, viability and risk need an explicit trade-off. |
| Will one technical/operational assumption hold? | [DS-14 Feasibility spike](design-and-delivery.md#ds-14) | A bounded trial can resolve a selection or implementation blocker. |
| What access barriers are present? | [DS-15 Accessibility review](design-and-delivery.md#ds-15) | Critical tasks can be inspected for barriers and applicable requirements. |
| Can the whole service handle exceptions? | [DS-17 Operational rehearsal](design-and-delivery.md#ds-17) | Safe scenarios can exercise handoffs, support and recovery. |
| Can exposure grow and stop safely? | [DS-18 Rollout/rollback plan](design-and-delivery.md#ds-18) | Owners, guardrails, pause authority and recovery need a usable plan. |

Record the selected approach, actual checks/defects, residual risks, operational ownership and release conditions. A quick accessibility review is not full conformance; a rehearsal is not deployment. Existing viability and mandatory reviews remain applicable. Preserve the checkpoint and ask for the appropriate handoff/transition decision; completing a method does not grant release authority.

For ownership, required sign-off or a decision readout, use the [stakeholder map and decision path](../stakeholders.md).

When making or refining the artifact itself, use the [craft quality bar](../craft-quality.md) for applicable states, copy and rationale; inspection is not user validation.

When a change can shift harm or effort to others, use the [harm and risk review](../harm-and-risk.md); mandatory controls still apply.

[Methods index](README.md) · [Phase readiness and checkpoints](../phases.md) · [Optional tools](../tool-options.md)
