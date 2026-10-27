# Releases, updates and rollback

Core releases use `vX.Y.Z` tags matching SKILL.md metadata. Host packages use independent `<service>-vX.Y.Z` tags and pin the exact core version/hash. Current versions are core 0.3.0 and host packages 0.2.0.

Download the archive and checksums from the selected [release](https://github.com/rebosidium/diamond-captain/releases). Verify SHA-256, extract to a new directory, and follow its setup guide. Public archives and receipts identify their public source revision. Keep a saved complete working installation before replacement.

## Update or roll back an installation

1. Identify the actual active workspace/user installation and its version.
2. Preserve `.product-task/`, artifacts, current decisions and unrelated host settings.
3. Keep a complete backup outside discovery roots. Replace the intended skill directory rather than merging old and new files.
4. Update invocations/routing if the skill identity changed, then verify discovery and supporting files in a fresh session.
5. To roll back, restore the saved complete installation or a previous published package from this repository. Retain current project state.

Never move a published tag or silently replace a released archive during ordinary maintenance. Correct product changes receive a new version. Versioned packages, source history and user task state are separate; reverting source does not restore an earlier task state.

The first Diamond Captain release does not import previous repositories' tags, PRs, releases or internal working history. See [migration](migration.md).
