# Installation decisions

Use the sections relevant to what [agent setup](../INSTALL-FOR-AGENTS.md) found. Resolve protection before choosing an action. Read the selected [host route](host-installation-routes.md), rather than every host guide.

## Establish workspace role

Identify the actual host/product surface, active profile and product workspace; read applicable project instructions and resolve source/target symlinks before writes. CLI, desktop, cloud and ordinary chat can expose different installation mechanisms even with the same model.

Establish a source/fixture role from origin, authoring/build metadata or fixture documentation. Useful evidence includes a marketplace registered to this workspace's authored plugin payload, or comparison records pinning a baseline/rubric. A normal product project can contain Git, tests, an installed skill and a receipt; these alone do not make it protected source. Inspect the role, not just filenames. An unresolved role needs clarification before dependent writes.

For `SOURCE_TREE`, protect the identified source/fixture, including unfinished edits, evidence, receipts and routing notes. A proposed target resolving into it is protected too. An install/update request does not authorize rewriting that material. Report the path, role evidence and any known pin without inventing one. Continue in an already supplied, authorized separate product workspace after inspecting it. If none was supplied, ask for the folder once. Do not escape into a global/profile installation without scope authority.

## Find the active installation

Inspect actual native discovery, plugin registrations, scope/profile, disabled entries, host precedence and resolved paths. Check `diamond-captain` and `design-process-dr`. A copy in an inactive profile is not automatically a duplicate. Do not modify another tool's shared skill or configuration to resolve a conflict.

For Claude Code, inspect project `.claude/settings.json` and relevant user/profile settings: `extraKnownMarketplaces` identifies sources and `enabledPlugins` identifies enabled entries. An empty personal `installed_plugins.json` does not negate a project-local registration. Establish the selected payload before calling a plugin absent, current or upgraded. For hosts using installed caches, changing a marketplace source alone does not prove the active cached installation changed.

Preserve a usable route. Otherwise prefer a native workspace skill for one project, a supported published plugin for managed/versioned distribution, or an honest import/link fallback. A session-only plugin flag is not permanent installation. Native managers may default to user scope; honor existing authorization or obtain it for that scope before writing.

## Choose an action

| Detected state | Action |
| --- | --- |
| `SOURCE_TREE` | Protect source/fixture; continue in a supplied safe authorized target, or ask for it. |
| `CONFLICT` | Multiple active routes or an unrelated occupied target need a choice; do not delete, disable, overwrite or add another copy without that decision. |
| `UNVERIFIED` | Preserve modified/incomplete copies or unresolved provenance; report the gap without replacing them or inventing a source. |
| `ABSENT` | Install into the verified vacant target within the requested scope. |
| `ALREADY_CURRENT` | Keep the usable matching installation, receipt and original time unchanged. |
| `OUTDATED` | Report the update; preserve the working installation until update authority exists. |
| `BLOCKED` | Use the host's normal permission mechanism where supported; otherwise report a supported fallback and limits. Never bypass restrictions. |

Migrating the predecessor name is an update, not a fresh absent-name install. Follow [migration](migration.md), preserve the complete old package, routing and state until replacement is verified, and avoid leaving both names active in the same discovery scope. Do not silently rewrite unrelated routing or task records. Reuse authority already given.

## Disable or uninstall a host integration

Distinguish the host's enabled registration/cache from its marketplace source and Git-tracked payload. A request to disable/remove an installed plugin does not authorize deleting a source checkout or pinned fixture. Use the host's supported mechanism within the authorized profile, preserving task state and unrelated settings. If its registration is itself part of a protected fixture, explain that boundary and establish the intended configuration target before changing it. A refusal due to modified files is not permission to force removal; preserve the files and resolve the operation/scope. Do not translate host removal into `git rm`, forced checkout/reset or recursive source deletion.

## Compare the right versions

Read actual SKILL.md, receipts and selected-route metadata. A receipt alone does not prove current integrity. Use the user's version or a published version from the [release table](../README.md#install); a development checkout is not automatically a released update.

Core and host-package versions are independent. For example, OpenAI/Claude Code/OpenCode **0.3.0** packages pin core **0.4.0** and its content hash. Compare core with the selected core, and a host package with its service release. Legacy core **0.2.5** also needs migration to the `diamond-captain` identity; renaming and being outdated can coexist. Never require core and wrapper numbers to match or silently repin published bytes.
