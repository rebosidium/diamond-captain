# Diamond Captain — Agent Skill

The full SKILL.md holds shared operating rules. Open phase, dialogue, research and optional tool guidance for the next decision. Tool indexes link to category files; preserve every supporting directory when installing. This source layout may contain unreleased changes; use the installed package receipt to identify its exact files and version.

A **task-running** skill for product and service designers. The agent can start with an ambiguous task, figure out the current Triple Diamond phase, find gaps, use available integrations, execute the next step, loop back on new evidence, and follow the task through real-world outcome review.

This is separate from the explanatory [six-stage process](https://github.com/rebosidium/diamond-captain/blob/main/docs/process.md): it tells an agent **how to operate**, not just what the model means.

## What the designer can ask

- "Here's my task: payments drop on mobile. Start it."
- "Which diamond and which phase am I in?"
- "What do we already know and what's missing?"
- "Can we move forward, or should we go back?"
- "What research method should we use, and when is enough?"
- "Do the next useful thing using my connected tools."
- "We shipped; help evaluate the real outcome."

Every material response contains a short compass: `Problem / Discover ↗ · 1/6 | NOT READY`, for example, plus known evidence, important gaps and the next action. The agent does **not** march blindly through six phases or force all actions.

For other hosts and a GitHub-link entry, see the [cross-agent start guide](https://github.com/rebosidium/diamond-captain/blob/main/START-HERE.md). The package does not pin a model or depend on a particular connector.

## Install for all your local Codex projects

Copy the complete released skill folder to `~/.agents/skills/diamond-captain/` by default. Preserve existing copies until an update or migration is authorized; do not add a duplicate. Open Codex in the project you want to work on and request `$diamond-captain`. The skill is shared across projects; each task keeps its own checkpoint in the actual task project. See [setup and verification](https://github.com/rebosidium/diamond-captain/blob/main/INSTALL-FOR-AGENTS.md).

## Install in a Codex project

Use this alternative only when a one-project installation is explicitly wanted.

1. Copy the entire `.agents/skills/diamond-captain/` directory into your product project's `.agents/skills/`. Codex discovers repository-local skills there.
2. Merge the section in [assets/AGENTS-snippet.md](assets/AGENTS-snippet.md) into the product project's root `AGENTS.md` (optional, but recommended for reliable re-entry).
3. At task start in a writable project, the agent creates `.product-task/TASK-STATE.md` using [assets/TASK-STATE.md](assets/TASK-STATE.md). It fills known facts immediately, before substantive work; unknowns stay unknown. You need not create it manually.
4. Open Codex **inside the product project** (or select that project in the app). A file copied into a different checkout is not automatically a skill in the current chat. For CLI, start with `codex -C /absolute/path/to/product-project`.
5. In the Codex chat, explicitly request: **"Use $diamond-captain to start/continue this product task: …"** (or invoke by skill name using your client).

To use in a generic chat without repo skill discovery, supply the complete skill folder or archive and verify that the agent can read [SKILL.md](SKILL.md) and its supporting files. SKILL.md alone omits the templates and phase guidance. Recover existing task state, or create an intake-only checkpoint before reading task materials and conditional references. Without file access, keep a pasteable checkpoint and provide the supporting files needed for the next step. Carry the checkpoint/state forward when switching chats. This is **not** an always-on installed integration for arbitrary conversations.

Codex discovers repo skills from the current directory up to the Git root. Personal installation is the default above; project installation is the explicit alternative. Verify the host's actual discovery and precedence before adding a second installation; keep an existing working source rather than duplicating it. Codex detects skill-file changes; if an update is missing, restart the client. Already loaded conversation context may still contain an earlier version. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Collaboration and acceptance

Onboarding explains the intended result, how collaboration works, who makes decisions, where progress is saved and what the final handoff contains. The agent then reads existing material, identifies a provisional phase and conducts a short intake dialogue. Questions use choices or free text, 1–3 at a time. By default the agent consults the user at material decisions and before phase transitions, records answers and continues independent work while waiting. On resume it restores context without repeating the welcome or settled questions. The user may delegate decisions or reduce the cadence, and may select any phase. The agent explains concrete gaps and records the move; skipped phases do not become complete.

**Design DoR** defines the inputs and authority needed to start useful phase work. **Design DoD** defines observable completion and acceptance for the relevant phase and requested deliverable. A completed design handoff, release readiness and verified live impact are different outcomes. Read [intake, questions and DoR/DoD](references/dialogue-and-gates.md).

## Persistence, without a giant prompt

- **AGENTS.md**: small *project-level* routing instruction automatically read in supported Codex workspace contexts.
- **SKILL.md**: the repeatable operating loop, activated by explicit invocation or matching skill description.
- **TASK-STATE.md**: one project file with a current checkpoint, phase index and dated records: who did what, when, output/source, confidence and limits. Superseded results remain traceable.
- **Phase transition/resume**: reopen task state and relevant phase guidance. Reuse instructions already in context rather than rereading the whole package for every follow-up.
- **Chat-only fallback**: a pasteable checkpoint; persistence cannot be guaranteed without a writable state store.

The skill **does not modify the model's system prompt**. It cannot run asynchronously or access tools without an actual connected/authorized tool.

## Package

- [SKILL.md](SKILL.md) — operator contract, routing, next-action loop and readiness
- [references/phases.md](references/phases.md) — six phase inputs, outputs and readiness tests
- [references/dialogue-and-gates.md](references/dialogue-and-gates.md) — intake, frequent questions, phase decisions, Design DoR/DoD
- [references/research.md](references/research.md) — qualitative/quantitative methods, depth and stop rules
- [references/uxr.md](references/uxr.md) — conditional study planning, recruitment, sessions, synthesis and research handoff
- [references/methods/README.md](references/methods/README.md) — six phase menus and 60 optional method cards: when, procedure, output and limits
- [references/tool-options.md](references/tool-options.md) — ten *optional* tool candidates per category across an expanded task catalog
- [references/office-tools.md](references/office-tools.md) — email, calendars, files, presentations, approvals and connector/MCP limits
- [references/product-memory.md](references/product-memory.md) and [memory template](assets/PRODUCT-MEMORY.md) — product-scope evidence/decision index; each task keeps its own history
- [references/portfolio-and-priority.md](references/portfolio-and-priority.md), [stakeholders](references/stakeholders.md) and [craft quality](references/craft-quality.md) — conditional task choice, decision path and artifact criteria
- [references/harm-and-risk.md](references/harm-and-risk.md) — indirect effects, affected parties and stop conditions
- [references/fast-path.md](references/fast-path.md) and [minimal template](assets/TASK-STATE-MINIMAL.md) — bounded reversible work, with history-preserving upgrade
- [scripts/init_product_memory.py](scripts/init_product_memory.py) — header-only memory initialization; task initializer also supports `--minimal`
- [assets/TASK-STATE.md](assets/TASK-STATE.md) — persistent task state template
- [assets/AGENTS-snippet.md](assets/AGENTS-snippet.md) — copy/paste project bootstrap
- [tests/scenarios.md](tests/scenarios.md) — behavioral acceptance scenarios

At a closeout, pause or blocker the agent provides artifact paths, checks and limits, pending work/owners/triggers, and a one-line resume instruction. Loop history retains superseded decisions and the evidence that reopened them.

## Source and limitations

Adapted from the [Diamond Captain](https://github.com/rebosidium/diamond-captain/blob/main/docs/process.md), using a **Triple Diamond-inspired** six-phase structure. It is not a hard-coded collection of plugins, a self-running automation, a guaranteed skill activation or a claim of outcome causality. Use appropriate access controls and human authority for production changes.
