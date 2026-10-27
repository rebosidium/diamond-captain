# Diamond Captain — OpenCode native skill

Distribution **0.2.0**, containing complete core **0.3.0**.

Keep the complete packaged skill tree, including any nested references and scripts. See [package contents and source versions](https://github.com/rebosidium/diamond-captain/blob/main/docs/distributions.md); current development source does not update an installed release.

Download the ZIP, JSON receipt and matching checksums from [opencode-v0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/opencode-v0.2.0). Verify SHA-256 and extract into a new version-specific directory.

## Install in the selected workspace

Run from the extracted package directory with Python 3.9 or later:

```sh
python3 install.py --project /absolute/path/to/workspace --dry-run
python3 install.py --project /absolute/path/to/workspace
```

The installer verifies the bundled payload and copies the complete skill to `.opencode/skills/diamond-captain/` in the explicit project. It refuses an existing destination by default. For an authorized update, repeat the dry run and installation with `--replace`; the old directory is backed up under `.diamond-captain-backups/opencode/`, outside scanned skill roots. Keep its receipt and backup for rollback. Project task state and unrelated skills are preserved.

Generated backups and installation receipts are local working records. Exclude `.diamond-captain-backups/` from the target project's tracked files, shared archives and public attachments. Being outside skill-discovery roots does not prevent Git publication. This repository's ignore rules do not automatically protect a different workspace, and the installer does not configure that project's ignore rules. Use the target project's own exclusions and review its tracked-file list; ignore rules alone do not remove files already tracked. Preserve existing records rather than deleting them automatically.

Before installing, check compatible `.agents/skills/` and `.claude/skills/` roots and the active user/profile scope so an already usable skill is not duplicated. A renamed legacy installation is a separate existing copy; `--replace` targets only the Diamond Captain destination and does not migrate old routing or remove another skill. Follow the [migration guide](https://github.com/rebosidium/diamond-captain/blob/main/docs/migration.md) for that transition.

Open OpenCode in the selected workspace and ask it to use `diamond-captain`. Where supported by the installed CLI, `opencode debug skill` checks discovery without a model call. Confirm the actual skill path/version and packaged references; installation or a receipt alone does not prove discovery or task execution. See official [skill discovery](https://docs.opencode.ai/docs/skills/) for supported roots and permissions.

## Rollback or removal

Move the current installed skill outside discovery roots and restore the selected complete backup into `.opencode/skills/diamond-captain/`, or install a saved verified prior package for an authorized replacement. Start a fresh session and verify the restored source. To remove this route, remove only the intended skill directory. Preserve `.product-task/`, artifacts, unrelated skills and host settings. Keep backup directories and installation receipts private during rollback and removal as well. This package is a native skill, not a JavaScript plugin.

[All host routes](https://github.com/rebosidium/diamond-captain/blob/main/docs/host-installation-routes.md) · [Verification scope](https://github.com/rebosidium/diamond-captain/blob/main/docs/validation.md) · [Releases](https://github.com/rebosidium/diamond-captain/blob/main/docs/releases.md)
