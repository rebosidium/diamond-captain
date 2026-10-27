The project file is the recovery point for a task. It keeps the current checkpoint, phase history, decisions and result records together so you can resume without rebuilding the conversation.

## Where progress lives

In a writable workspace the default path is `.product-task/TASK-STATE.md`. The agent creates it before substantive execution work and fills known facts immediately; unknowns remain explicit.

For multiple tasks, use the actual recorded paths, such as `.product-task/invoice-approvals/TASK-STATE.md`. Keep unrelated task states closed and do not overwrite another task. Task state belongs in the product workspace, rather than this skill's source repository by default.

The state should retain the current phase and scope, evidence and artifact links, settled and pending decisions, acceptance and delegated authority, and the next action. Dated records identify who did what, sources, confidence and limitations. Earlier decisions remain traceable after a loop.

## Resume in a new chat

Open the correct project and provide the actual state path:

```text
Use Diamond Captain to continue the invoice approvals task.
Read .product-task/invoice-approvals/TASK-STATE.md first and keep unrelated
task states closed. Restore the agreed scope and pending decisions.
Continue the next useful action without repeating settled questions.
```

Replace the example path with the one in your handoff. If the previous run was interrupted, include its last uncheckpointed user message too: the state file may predate it.

## Work without file access

Ask for a pasteable checkpoint containing the task, phase and status, last decisions, evidence and artifact references, pending questions and next action. Save it yourself and provide it in the next chat. The agent should not claim durable storage when no writable store exists.

## Update the skill without losing the task

Installed skill files and project task state are different things. Follow the release-specific update or rollback guide, preserve task state and verify the installed version. Updating the skill does not automatically refresh instructions already loaded into every running conversation.

At a pause or handoff, keep the resume line with your project. Saving state does not schedule monitoring or cause the agent to continue in the background.

**Next:** [FAQ](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/FAQ-and-troubleshooting.md) · [State template](https://github.com/rebosidium/diamond-captain/blob/main/.agents/skills/diamond-captain/assets/TASK-STATE.md)
