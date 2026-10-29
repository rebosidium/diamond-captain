# Install Diamond Captain

For agent-assisted setup, give your agent [INSTALL-FOR-AGENTS.md](INSTALL-FOR-AGENTS.md). It defaults to all your local projects for the selected agent, checks the actual profile and existing installations, and preserves protected source/test files. If you use the previous skill name, follow [migration](docs/migration.md) rather than installing a second active copy.

## Install for all your projects

Choose a published version from the [release table](README.md#install), such as the [core 0.6.1 release](https://github.com/rebosidium/diamond-captain/releases/tag/v0.6.1), and verify its matching archive checksum. Copy the complete `diamond-captain` skill folder from that release into your agent's supported skill directory. In a tagged source checkout, that folder is `.agents/skills/diamond-captain/`. Preserve its README, references, templates, tests and license. A development checkout is not a released package. Use the selected agent's supported personal location by default. For Codex, this is `~/.agents/skills/diamond-captain/`; for Claude Code, `~/.claude/skills/diamond-captain/`. Install for just one project only when explicitly requested; use its project-local skill directory. See [host routes](docs/host-installation-routes.md) for other agents and profile differences.

Open the agent in the project you want to work on and explicitly request `diamond-captain`. In Codex, `$diamond-captain` is the native skill invocation. Ask the agent to report the active skill path/version and verify supporting files; seeing a repository link alone is not proof of installation.

If an active copy already exists, preserve it until an update or [migration](docs/migration.md) is authorized. The absence of the new directory name does not mean an older-name skill is absent. Use [INSTALL-FOR-AGENTS.md](INSTALL-FOR-AGENTS.md) to detect the actual route and installation state before writing.

## Service packages

Use the [OpenAI](distributions/openai/README.md), [Claude Code](distributions/claude-code/README.md) or [OpenCode](distributions/opencode/README.md) package for a managed plugin/native distribution. See [all host routes](docs/host-installation-routes.md) for scope, import and discovery differences.

## Start a task

```text
Use Diamond Captain. My task is: …
```

The agent records a checkpoint in `.product-task/TASK-STATE.md` when local writing is available. In chat-only environments it returns a checkpoint you can save. Keep unrelated tasks separate and preserve existing state when updating the skill.

If a host can fetch instructions but cannot install a skill, start with [https://github.com/rebosidium/diamond-captain](https://github.com/rebosidium/diamond-captain) and the [raw entrypoint](https://raw.githubusercontent.com/rebosidium/diamond-captain/main/.agents/skills/diamond-captain/SKILL.md). The agent must confirm it actually read the source and required references. Otherwise attach the complete skill folder.

Read the [user guide](docs/guide/README.md), [compatibility limits](docs/validation.md) and [update/rollback guide](docs/releases.md).
