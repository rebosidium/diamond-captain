Start with a decision or a problem from your actual work. A rough request is enough; the agent can help clarify the rest.

## 1. Give the agent a task and access to the skill

If the skill is installed in the current workspace:

```text
Use $diamond-captain to start this task:
People abandon our mobile payment flow. Help understand what is happening
and decide what to investigate first. Reply in my language.
```

The `$` invocation above is for Codex. Other hosts have their own invocation; use [Installation](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Installation.md).

For a browsing or file-capable agent without a native install:

```text
Use Diamond Captain from https://github.com/rebosidium/diamond-captain.
Read .agents/skills/diamond-captain/SKILL.md, then only the references
needed for this task. Resolve supporting links against the skill folder.
Confirm you could read it. Recover existing task state, or create it
before substantive work. Keep me involved in decisions.

My task: ...
Available evidence: ...
Desired result and constraints: ...
```

A link alone does not install the skill. If the agent cannot read it, supply the complete skill folder or the relevant files through your host's supported mechanism.

## 2. Share what is already known

Useful context includes affected users or roles, the current problem, available research or data, constraints and the decision you need. Unknowns can stay unknown. You do not need to invent a brief or choose a research method before starting.

Prefer redacted or synthetic materials when real records contain private information. Grant only the tool access needed for the work.

## 3. Agree a useful first result

Expect the agent to identify a provisional phase, read existing evidence, ask focused questions and perform the next useful action. In a writable workspace it creates a task-state file before substantive work. Without file access it provides a checkpoint you can save.

For example, agree to produce **a supported problem statement and a plan for one unresolved question**. That is a valid scope; the agent does not need to run all six phases.

You may see a short compass:

```text
Problem / Discover ↗ · 1/6 | NOT READY
```

This describes the current decision and evidence gaps. It is not a score for your project. See [Choosing a phase](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Choosing-a-phase.md).

## 4. Review the handoff

The agent should identify the delivered artifact, actual checks, limitations and remaining decisions. Accept, request a revision or reopen the problem. Accepting a design result does not establish that a change shipped or improved a live metric.

Keep the state path and the copyable resume instruction. Use [Task continuity](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Task-continuity.md) when you return.

**Next:** [Working with the agent](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Working-with-the-agent.md) · [Examples](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Examples.md)
