# Diamond Captain — Claude Code plugin

Distribution **0.3.0**, containing complete core **0.4.0**.

Keep the complete packaged skill tree, including any nested references and scripts. See [package contents and source versions](https://github.com/rebosidium/diamond-captain/blob/main/docs/distributions.md); current development source does not update an installed release.

Download the ZIP, JSON receipt and matching checksums from [claude-code-v0.3.0](https://github.com/rebosidium/diamond-captain/releases/tag/claude-code-v0.3.0). Verify SHA-256 and extract into a new version-specific directory.

## Load for a session

Use the installed Claude Code executable to validate and load the extracted plugin:

```sh
claude plugin validate /absolute/path/to/extracted-plugin --strict
claude --plugin-dir /absolute/path/to/extracted-plugin
```

In that session invoke `/diamond-captain:diamond-captain`, then describe your task. Verify the loaded plugin/skill source, version and supporting files in your installed CLI. Session loading does not register a permanent marketplace installation; start the next session without `--plugin-dir` to stop loading it.

A standalone native skill is an alternative: copy the complete released skill to `.claude/skills/diamond-captain/` and invoke `/diamond-captain`. Choose one route and inspect existing project/user installations before adding a copy. A plugin's namespaced command differs from the native skill command. See the official [plugin guide](https://code.claude.com/docs/en/plugins/create) and [skill locations](https://code.claude.com/docs/en/skills). Do not assume these local CLI steps apply to Cowork or claude.ai.

This archive does not create or submit a marketplace listing. Package checks, validation, discovery and actual agent execution are separate results; the first renamed packages do not inherit runtime claims from an older package identity.

## Update and rollback

For an authorized update, preserve task state, artifacts and unrelated settings. Keep the complete previous plugin directory outside discovery roots, then load the intended version in a fresh session and verify its source. To roll back, load the saved previous package; to stop this session-loading route, restart without the flag. A previous skill name requires the explicit [migration procedure](https://github.com/rebosidium/diamond-captain/blob/main/docs/migration.md), including routing/invocation changes.

[All host routes](https://github.com/rebosidium/diamond-captain/blob/main/docs/host-installation-routes.md) · [Verification scope](https://github.com/rebosidium/diamond-captain/blob/main/docs/validation.md) · [Releases](https://github.com/rebosidium/diamond-captain/blob/main/docs/releases.md)
