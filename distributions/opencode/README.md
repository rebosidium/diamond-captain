# Diamond Captain — OpenCode native skill

Distribution **0.2.0**, containing complete core **0.3.0**.

Download the ZIP, JSON receipt and matching checksums from [opencode-v0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/opencode-v0.2.0). Verify SHA-256 and extract into a new version-specific directory.

Run `python3 install.py --project /absolute/path/to/workspace --dry-run`, then repeat without `--dry-run` to install `.opencode/skills/diamond-captain/`. Existing installations are not overwritten without explicit replacement.

Keep one active installation and verify the selected path/version and packaged references/templates. A plugin must not be treated as a universal UI import or marketplace listing. The first renamed packages have automated source/package checks; host-specific runtime checks remain limited to what the release notes actually record.

To update or roll back, preserve task state and artifacts, back up the complete previous installation outside discovery roots, and restore or replace the intended package. For a plugin, use the host's supported uninstall or previous-package selection mechanism. Do not erase project state or unrelated settings.

See [all host routes](../../docs/host-installation-routes.md), [verification scope](../../docs/validation.md), [migration](../../docs/migration.md) and [releases](../../docs/releases.md).
