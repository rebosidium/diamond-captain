# Diamond Captain — Claude Code plugin

Distribution **0.2.0**, containing complete core **0.3.0**.

Download the ZIP, JSON receipt and matching checksums from [claude-code-v0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/claude-code-v0.2.0). Verify SHA-256 and extract into a new version-specific directory.

Load the extracted plugin with `claude --plugin-dir /absolute/path/to/plugin` and invoke `/diamond-captain:diamond-captain`. Verify plugin/skill discovery in your installed Claude Code version.

Keep one active installation and verify the selected path/version and packaged references/templates. A plugin must not be treated as a universal UI import or marketplace listing. The first renamed packages have automated source/package checks; host-specific runtime checks remain limited to what the release notes actually record.

To update or roll back, preserve task state and artifacts, back up the complete previous installation outside discovery roots, and restore or replace the intended package. For a plugin, use the host's supported uninstall or previous-package selection mechanism. Do not erase project state or unrelated settings.

See [all host routes](../../docs/host-installation-routes.md), [verification scope](../../docs/validation.md), [migration](../../docs/migration.md) and [releases](../../docs/releases.md).
