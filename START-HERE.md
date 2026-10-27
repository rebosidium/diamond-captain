# Install Diamond Captain

## Install in a product workspace

Copy the complete `.agents/skills/diamond-captain/` directory into your agent's supported skill directory. Preserve its README, references, templates, tests and license. For Codex, use `.agents/skills/diamond-captain/` inside the target workspace, or the host's supported user-scope skill directory.

Open the agent in that workspace and explicitly request `diamond-captain`. In Codex, `$diamond-captain` is the native skill invocation. Ask the agent to report the active skill path/version and verify supporting files; seeing a repository link alone is not proof of installation.

## Service packages

Use the [OpenAI](distributions/openai/README.md), [Claude Code](distributions/claude-code/README.md) or [OpenCode](distributions/opencode/README.md) package for a managed plugin/native distribution. See [all host routes](docs/host-installation-routes.md) for scope, import and discovery differences.

## Start a task

```text
Use Diamond Captain. My task is: …
```

The agent records a checkpoint in `.product-task/TASK-STATE.md` when local writing is available. In chat-only environments it returns a checkpoint you can save. Keep unrelated tasks separate and preserve existing state when updating the skill.

If a host can fetch instructions but cannot install a skill, start with [https://github.com/rebosidium/diamond-captain](https://github.com/rebosidium/diamond-captain) and the [raw entrypoint](https://raw.githubusercontent.com/rebosidium/diamond-captain/main/.agents/skills/diamond-captain/SKILL.md). The agent must confirm it actually read the source and required references. Otherwise attach the complete skill folder.

Read the [user guide](docs/guide/README.md), [compatibility limits](docs/validation.md) and [update/rollback guide](docs/releases.md).
