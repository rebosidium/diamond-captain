# Install Diamond Captain for this workspace

You are an agent setting up Diamond Captain at the user's request. Set up the skill first; start product work when the user supplies a task.

## 1. Identify and protect

Identify the host, active profile and product workspace. Read applicable project instructions. Resolve symlinks for the workspace and candidate installation paths before writing.

If this workspace is the skill's source checkout, a plugin/marketplace source, or a pinned QA/comparison fixture, classify it as `SOURCE_TREE` and make **no setup writes**, including receipts or routing notes. The same protection applies when the proposed target resolves into such a tree. Establish the repository's role from origin, authoring/build metadata or fixture documentation. A Git checkout, temporary directory, bundled tests or a receipt with a source pin alone is not proof of that role. If its role is unclear, inspect the evidence or ask before dependent writes. An install/update request does not authorize altering maintained source or test evidence; use a separate product workspace.

An installation request authorizes a new installation in the requested workspace. It does **not** authorize upgrading/replacing an existing copy, changing global settings or adding connectors, credentials or background jobs. Honor any explicit update authorization already given.

## 2. Detect and decide

Before classifying installation state, select the route using [host installation routes](docs/host-installation-routes.md):

1. Identify the actual product and surface: CLI, local desktop, cloud agent or ordinary chat. A shared model name does not imply shared installation support.
2. Preserve an existing usable route. Otherwise use a native workspace skill for one project, a supported published plugin for managed/versioned distribution, or the documented import/link fallback when native discovery is unavailable. Do not treat a development-only plugin loading path as a permanent installation.
3. Select the requested scope explicitly. Default to the product workspace; if the host route only supports a user/global change, obtain scope authorization before writing. Native managers may default to the user profile.
4. Inspect the active source, host-specific precedence and disabled registrations before adding anything. Same-name folders may be shadowed, separately selectable or namespaced; do not apply one host's duplicate rules to another. Do not change another tool's shared skill or configuration to resolve a conflict.

Use [START-HERE.md](START-HERE.md) and the selected host's section in [host installation routes](docs/host-installation-routes.md) to choose this host's route. Check active native discovery and plugin registrations as applicable, rather than just searching for a folder. For example, Claude Code workspace marketplace installs may be registered through `extraKnownMarketplaces` and `enabledPlugins` in `.claude/settings.json`; follow the host guide for other scopes. A physically present copy outside the active profile is not automatically an active duplicate.

Read the actual `SKILL.md`, available receipts and the selected route's metadata. Choose a published release from the [README release table](README.md#install), unless the user selected another version. Core and service-distribution versions are independent; compare each with its own release and declared dependency/hash, never require both numbers to match.

Apply protection first, then use the relevant outcome:

| Detected state | Action |
| --- | --- |
| `SOURCE_TREE` — source or pinned fixture involved | Report the protected path and pin; do not install, update, repair or write metadata there. |
| `CONFLICT` — multiple active copies/registrations or an unrelated occupied target | Report the paths, versions where known and scope. Do not delete, disable or add another copy without a decision about the intended route. |
| `UNVERIFIED` — incomplete/modified copy or unresolved provenance | Preserve it and report the evidence gap. Do not call it current, replace it or invent its source. |
| `ABSENT` — no active copy and the intended target is unused | Install within the requested scope; no extra setup explanation is needed from the user. |
| `ALREADY_CURRENT` — matches the selected release and is usable in this profile | Keep it unchanged, including its receipt and original installation time. |
| `OUTDATED` — verified older release | Keep it usable and report the available update. Replace only if that update is authorized. |
| `BLOCKED` — required access or host capability unavailable | Use the host's normal permission mechanism where supported; do not bypass restrictions. Otherwise offer the documented link/attachment/import fallback and state its limits. |

Do not overwrite an unrelated occupied target. If no installation was changed, do not create a receipt that implies a new installation or invent an earlier install time.

## 3. Install or explicitly update

Follow the selected release's host-specific setup guide; use [distributions](docs/distributions.md) only as needed for that route. Verify a downloaded archive against its matching published checksum before using it; stop on mismatch. For a manual native install, copy the **entire** released `.agents/skills/diamond-captain/` package, preserving references, assets and license, to the documented host path.

For an authorized update, back up the old directory and its receipt outside skill-discovery roots, replace the directory wholesale, then re-verify. Preserve `.product-task/`, artifacts, unrelated skills and existing project instructions. Follow the route's [backup/rollback procedure](docs/releases.md#update-or-roll-back-an-installation). If copying, receipt recording or verification fails, report `INCOMPLETE` and the actual remaining files; restore the prior backup when possible rather than claiming success.

### Provenance for a manual workspace copy

After a successful manual copy, save `.diamond-captain-installations/<host-id>/manual.json` in the product workspace, using the host's lowercase identifier, such as `codex` or `claude-code`. Keep this receipt **outside** the skill payload and scanned skill roots. This convention is for manual workspace copies; retain existing `DISTRIBUTION.json` and installer-generated receipts for service packages rather than replacing their formats.

Record actual values, not example placeholders:

| JSON field | Value |
| --- | --- |
| `schema_version`, `route`, `host` | Integer `1`, string `manual-copy`, actual host identifier |
| `target`, `resolved_target` | Workspace-relative install path and its resolved absolute path |
| `source_repository`, `source_tag`, `source_commit` | Repository URL, selected published tag and its resolved full commit SHA |
| `core_version` | Version read from the installed `SKILL.md` |
| `artifact_url`, `artifact_sha256` | Downloaded archive URL and verified SHA-256; JSON `null` for both if copied from the pinned Git tree instead |
| `files_sha256` | Object mapping **every** payload-relative file path to its verified SHA-256; compare installed files with the pinned source, not only with themselves |
| `installed_at_utc` | Actual successful-copy time in ISO 8601 UTC |

Record archive and Git-source provenance accurately; do not substitute the moving `main` SHA for the release commit. On an unchanged legacy installation without a receipt, report the provenance actually verified and any unknowns; do not fabricate a receipt or timestamp. For an explicitly authorized non-workspace install, follow that route's receipt convention and report its actual location.

## 4. Verify and report

Verify file membership and bytes against the selected published source, read the installed manifest version, and check actual host discovery when available. `tests/check_package.py` checks Markdown links only; it is not a completeness, provenance or discovery check. A receipt records provenance but does not prove current integrity. Discovery alone does not prove design-task execution.

Report these facts briefly:

```text
Detected state → result: INSTALLED / UPDATED / UNCHANGED / FALLBACK / INCOMPLETE
Host/product surface/profile; route and scope; active installation path or loading route
Core version; distribution version if applicable; source tag/commit
Receipt path or why none was written
Checks actually run: payload, links, discovery, task execution
Remaining step and correct invocation for this host
```

Choose the result that actually occurred. Separate copied files from verified discovery and task execution; label unavailable checks unverified. A fallback is not a persistent native installation. Invite the user to describe their task when setup is usable.

When a task is supplied, follow the installed skill, recover that task's state or create it in the product workspace, and perform the next useful action. Setup alone does not require creating a product task or running all six phases.

[Manual setup](START-HERE.md) · [User guide](https://github.com/rebosidium/diamond-captain/blob/main/docs/guide/README.md) · [Release and rollback policy](docs/releases.md)
