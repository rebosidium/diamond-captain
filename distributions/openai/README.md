# Diamond Captain — OpenAI plugin

Distribution **0.3.4**, containing complete core **0.6.1**.

Keep the complete packaged skill tree, including any nested references and scripts. See [package contents and source versions](https://github.com/rebosidium/diamond-captain/blob/main/docs/distributions.md); current development source does not update an installed release.

Download the ZIP, JSON receipt and matching checksums from [openai-v0.3.4](https://github.com/rebosidium/diamond-captain/releases/tag/openai-v0.3.4). Verify SHA-256 and extract into a new version-specific directory. Keep that directory as the local marketplace source.

## Register and install

The archive includes `.agents/plugins/marketplace.json`, named `diamond-captain-openai`, pointing to the plugin in the extracted root. In a supported Codex client, register that root:

```sh
codex plugin marketplace add /absolute/path/to/extracted-plugin
```

Registration makes the source discoverable; it does not establish that the plugin is installed and enabled. Follow the client's local plugin installation flow, find **Diamond Captain — local release**, and install **Diamond Captain** in your personal profile for all local projects by default. Honor an explicitly project-only request; confirm the actual profile rather than configuring another account or every host. Where the supported CLI provides plugin installation, the package identity is `diamond-captain@diamond-captain-openai`. Follow the official [local marketplace guide](https://developers.openai.com/plugins/build/plugins) for your client; local sources and UI availability vary by surface. These steps are not an installation procedure for ordinary ChatGPT web chat.

Start a fresh relevant session, select `diamond-captain:diamond-captain` in the plugin/skill picker or request it explicitly, and verify its installed source/version and supporting files. The client can load an installed cache rather than the extracted source; use its refresh/update mechanism for an authorized update. Editing the extracted directory alone does not prove the active installation changed.

Keep one active route. The standalone `$diamond-captain` native skill is an alternative, not a second required installation. Existing legacy installations require an explicit migration decision. This package does not create or submit a public marketplace listing. Automated source/package checks are distinct from UI installation and design-task execution; see the release's actual verification limits.

## Update and rollback

For an authorized update, preserve task state and artifacts and keep the complete prior package outside discovery roots. Use the host's supported previous-package selection or uninstall/reinstall mechanism, restart the relevant session and verify the active source. Preserve unrelated plugins and settings. If moving from the previous skill name, follow the [migration guide](https://github.com/rebosidium/diamond-captain/blob/main/docs/migration.md); no legacy copy is automatically upgraded.

[All host routes](https://github.com/rebosidium/diamond-captain/blob/main/docs/host-installation-routes.md) · [Verification scope](https://github.com/rebosidium/diamond-captain/blob/main/docs/validation.md) · [Releases](https://github.com/rebosidium/diamond-captain/blob/main/docs/releases.md)
