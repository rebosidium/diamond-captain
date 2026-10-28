## The agent cannot find the skill

Check the selected agent/profile, installation coverage and complete skill folder. Invoke it explicitly using the host's supported form. A project-only copy in another project is not available here; a personal copy should be discoverable across local projects unless the host's profile, overrides or permissions prevent it. Avoid duplicate installs with the same name. Follow [Installation](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Installation.md).

## I gave it a GitHub link. Is it installed?

A link asks the agent to read files; it does not prove native installation or successful retrieval. Ask it to confirm it read the actual `SKILL.md`. If browsing is unavailable, supply the relevant files through a supported mechanism. See [Getting started](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Getting-started.md).

## Setup found an old version and left it unchanged

An install request under this guide selects a new personal installation for all local projects, rather than an automatic upgrade. `OUTDATED` means an update is available; `ALREADY_CURRENT` means no update is needed. Give explicit update authority for the intended copy when you want replacement. See [Installation](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Installation.md).

## I already use the previous skill name. Should I install both?

Use the [migration guide](../migration.md). The previous installation does not become Diamond Captain automatically. Check which skill/plugin source is active before changing it, preserve task state and artifacts, and migrate the intended installation and routing only when authorized. Avoid leaving both names active in the same discovery scope. For Codex native use, the new invocation is `$diamond-captain`; plugin invocations depend on the selected host route.

## Why does setup report SOURCE_TREE in a QA project?

The agent identified maintained source or a pinned comparison fixture. Setup preserves its skill files, task state and evidence, including receipts and routing notes. A verified separate personal destination can still be used. If this is an isolated test profile, setup establishes the intended normal profile and access; it asks for a project path only when you explicitly requested project-only installation. A temporary directory, bundled tests or a receipt alone does not make an ordinary installation protected. See [role and target decisions](../installation-decisions.md#protect-source-and-test-files). Disabling a host plugin does not authorize deleting this fixture's tracked payload.

## Where can I check what was installed?

For a new manual personal copy, inspect `~/.diamond-captain-installations/<host-id>/manual.json` in that profile; project-only copies use the relative path inside their project. Service packages use their existing distribution and installer receipts. Compare the recorded source with actual payload hashes and host discovery; a Markdown-link check alone does not establish completeness. See [Installation](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Installation.md).

## Should repeating setup change any files?

On a verified current installation, expect `ALREADY_CURRENT → UNCHANGED`: no new copy, rewritten receipt or changed installation time. Conflicts, incomplete files and unknown provenance are reported separately. Setup does not silently repair or replace those files.

## Must every task go through all six phases?

No. Start with the next decision, compress proportional work and return earlier when evidence warrants it. The agent should not mark skipped work complete. See [Choosing a phase](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Choosing-a-phase.md).

## Can it improve a process without designing screens?

Yes. Policy, content, operations, service and training changes can be valid solutions. Compare mechanisms against the problem rather than assuming an interface is required. See [Examples](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Examples.md).

## It asks too many questions

State which routine choices you delegate and which decisions remain yours. Ask it to reuse settled answers and avoid repeating pending questions. Delegation must have a scope; naming the final approver alone is not advance acceptance. See [Working with the agent](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Working-with-the-agent.md).

## It says READY. Has the phase been accepted?

Not necessarily. Readiness describes evidence for a decision. Phase choice and handoff acceptance are recorded separately. An unanswered accept/revise/reopen question remains pending.

## It chose Deploy, but nothing is live

It can prepare permitted work in your selected phase while keeping exposure unverified. A prepared rollout has phase-4 evidence maturity. It must not invent live observations or claim a measured outcome. See [Choosing a phase](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Choosing-a-phase.md).

## It lost the task in a new chat

Provide the actual state file or saved checkpoint and ask it to recover the active task first. Include the last uncheckpointed user message after an interruption. A chat without a writable store cannot guarantee persistence. See [Task continuity](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Task-continuity.md).

## Do I need every tool in the catalog?

No. Providers are optional candidates, not dependencies. Supplied files or existing tools may be enough. Without access, the agent can prepare a protocol or handoff and state the limitation honestly.

## Does an update change every active chat immediately?

No. Verify installed files and versions; an active conversation may retain earlier instructions. Preserve task state and follow the relevant setup and release guide.

## Can it monitor outcomes after I leave?

The skill does not run by itself. Background work needs an explicitly arranged supported execution or scheduling mechanism. A saved checkpoint alone does not schedule anything.

## How do I report a problem?

Use [Issues](https://github.com/rebosidium/diamond-captain/issues) with the affected release or commit, agent/app/model, reproduction steps, expected and actual behavior, and redacted evidence. For vulnerabilities, follow the [private security reporting instructions](https://github.com/rebosidium/diamond-captain/blob/main/.github/SECURITY.md).
