Choose one installation route for your host. The skill is an instruction package: it does not select a model, grant tool permissions or install product integrations.

For agent-assisted setup, share [Install for agents](https://github.com/rebosidium/diamond-captain/blob/main/INSTALL-FOR-AGENTS.md) with your agent and ask it to set up this workspace.

If the previous skill name is already active, follow [migration](../migration.md). Its installed files and project routing do not change just because the product has a new name; check them before adding a new copy.

## Choose a route

| Your environment | Route and authoritative instructions |
| --- | --- |
| Codex workspace | [Native skill installation](../../START-HERE.md#install-in-a-product-workspace); use `$diamond-captain` |
| Supported OpenAI plugin tooling | [OpenAI distribution](https://github.com/rebosidium/diamond-captain/blob/main/distributions/openai/README.md); use the supported picker for `diamond-captain:diamond-captain` and check installation limits |
| Claude Code | [Claude Code distribution](https://github.com/rebosidium/diamond-captain/blob/main/distributions/claude-code/README.md) |
| OpenCode | [OpenCode distribution](https://github.com/rebosidium/diamond-captain/blob/main/distributions/opencode/README.md) |
| Manual native skill installation | [Agent setup guide](https://github.com/rebosidium/diamond-captain/blob/main/START-HERE.md) and [skill guide](https://github.com/rebosidium/diamond-captain/blob/main/.agents/skills/diamond-captain/README.md) |
| Agent with browsing or attached-file support | [Getting started](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Getting-started.md); confirm the agent actually reads the skill |

Use [host installation routes](../host-installation-routes.md) for Cursor, Gemini CLI, Grok Build and Perplexity Computer, including their scope and discovery checks. Use the [repository release table](https://github.com/rebosidium/diamond-captain#install) for current package versions and release downloads. Core and service-distribution version numbers are independent; the distribution identifies its pinned core version and content hash.

## Understand the setup result

The agent checks the workspace, active profile and existing installations before writing. It reports what it found and what actually happened:

| Detected state | What to expect |
| --- | --- |
| `SOURCE_TREE` | Source/fixture stays unchanged. Setup continues in an already supplied safe authorized product workspace, or requests the missing target. |
| `CONFLICT` | Multiple active copies or an unrelated occupied target need a choice of installation route. |
| `UNVERIFIED` | Missing provenance or modified/incomplete files are reported; the agent preserves the copy. |
| `ABSENT` | The agent installs in the requested workspace. |
| `ALREADY_CURRENT` | The matching usable installation, receipt and original installation time stay unchanged. |
| `OUTDATED` | The agent reports the available update and keeps the existing copy until an update is authorized. |
| `BLOCKED` | A host permission/capability is missing; the agent uses the normal permission mechanism or explains the supported fallback. |

An install request permits a new workspace installation; an existing copy needs update authority before replacement. Reuse authority already given. Files in another inactive profile are not automatically an active duplicate. A fallback loading route is reported separately from a persistent native installation. [Install for agents](../../INSTALL-FOR-AGENTS.md) routes to the relevant [decision rules](../installation-decisions.md) and [verification/receipt details](../installation-verification.md).

## Preserve the complete package

For manual installation, copy the entire `diamond-captain` skill folder with its references, assets and license. A lone `SKILL.md` is incomplete. Use the host-specific path in the setup guide and open the agent in the workspace where the skill is discoverable.

Avoid installing two copies with the same skill name. During an update, preserve project task state and follow the relevant distribution's replacement or rollback instructions. A working checkout, an installed copy and a published release may contain different revisions.

## Find the installation receipt

A new manual workspace copy records its provenance in `.diamond-captain-installations/<host-id>/manual.json`, for example `.diamond-captain-installations/codex/manual.json`. This file is outside the skill payload and discovery roots. It identifies the target, core version, published tag/commit, every payload file's SHA-256 and actual installation time. Archive fields are `null` when the copy came from a pinned Git tree instead of a release archive.

Service packages retain their existing `DISTRIBUTION.json` and installer-generated receipts. A receipt records origin; rechecking current files establishes integrity. Rerunning setup on a current installation does not rewrite its receipt or timestamp. A legacy copy without a receipt is reported honestly rather than given an invented installation history.

## Verify the installation

Ask the agent to locate the skill, read its actual name and begin a small task. Check that it produces something useful and saves state or returns an honest checkpoint. Then test continuing that same task in a new chat with the recorded state path.

Check the results separately: `tests/check_package.py` validates Markdown links; payload checks compare file membership and hashes with the selected release; discovery confirms that the host can find the skill. Actual task execution is another check. The [compatibility guide](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Reference-and-compatibility.md) describes the scope and limits of package, discovery and execution checks.

**Next:** [Getting started](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/Getting-started.md) · [Troubleshooting](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/FAQ-and-troubleshooting.md)
