# Diamond Captain — Claude Code plugin

Distribution **0.3.2**, containing complete core **0.5.0**.

Keep the complete packaged skill tree, including any nested references and scripts. See [package contents and source versions](https://github.com/rebosidium/diamond-captain/blob/main/docs/distributions.md); current development source does not update an installed release.

Download the ZIP, JSON receipt and matching checksums from [claude-code-v0.3.2](https://github.com/rebosidium/diamond-captain/releases/tag/claude-code-v0.3.2). Verify SHA-256 and extract into a new version-specific directory.

## Install for all your local projects

Default to your normal Claude Code personal profile. For the native route, copy the complete released `skills/diamond-captain/` directory to `~/.claude/skills/diamond-captain/`, including references, scripts, templates and license; invoke `/diamond-captain` in your projects. Verify existing copies before writing and use the [manual verification procedure](https://github.com/rebosidium/diamond-captain/blob/main/docs/installation-verification.md).

If using a registered plugin marketplace instead, choose **Install for you** (user scope). Keep that route instead of adding a native duplicate. This archive alone does not register a marketplace. Isolated test profiles and cloud sessions are separate; verify the actual profile and active source. See [plugin scopes](https://code.claude.com/docs/en/plugins/install#choose-an-install-scope).

## Load for a session

For an explicitly temporary test, use the installed Claude Code executable to validate and load the extracted plugin:

```sh
claude plugin validate /absolute/path/to/extracted-plugin --strict
claude --plugin-dir /absolute/path/to/extracted-plugin
```

In that session invoke `/diamond-captain:diamond-captain`, then describe your task. Verify the loaded plugin/skill source, version and supporting files in your installed CLI. Session loading does not register a permanent marketplace installation; start the next session without `--plugin-dir` to stop loading it.

For an explicitly one-project native installation, copy the complete released skill to that project's `.claude/skills/diamond-captain/` and invoke `/diamond-captain`. Choose one route and inspect existing project/user installations before adding a copy. A plugin's namespaced command differs from the native skill command. See the official [plugin guide](https://code.claude.com/docs/en/plugins/create) and [skill locations](https://code.claude.com/docs/en/skills). Do not assume these local CLI steps apply to Cowork or claude.ai.

This archive does not create or submit a marketplace listing. Package checks, validation, discovery and actual agent execution are separate results; the first renamed packages do not inherit runtime claims from an older package identity.

## Update and rollback

For an authorized update, preserve task state, artifacts and unrelated settings. Replace the selected personal/project native copy using complete verified files, or use the persistent plugin route's update mechanism; retain its scope and rollback copy. Keep the complete previous plugin directory outside discovery roots, then load the intended version in a fresh session and verify its source. To roll back, load the saved previous package; to stop this session-loading route, restart without the flag. A previous skill name requires the explicit [migration procedure](https://github.com/rebosidium/diamond-captain/blob/main/docs/migration.md), including routing/invocation changes.

[All host routes](https://github.com/rebosidium/diamond-captain/blob/main/docs/host-installation-routes.md) · [Verification scope](https://github.com/rebosidium/diamond-captain/blob/main/docs/validation.md) · [Releases](https://github.com/rebosidium/diamond-captain/blob/main/docs/releases.md)
