# Installation decisions

Use the sections relevant to what [agent setup](../INSTALL-FOR-AGENTS.md) found. Resolve protection before choosing an action. Read the selected [host route](host-installation-routes.md), rather than every host guide.

## Establish workspace role

Identify the actual host/surface, profile and requested scope; read applicable project instructions and resolve source/target symlinks before writes. Different surfaces can expose different installation mechanisms.

Use enough relevant origin, authoring/build metadata or fixture documentation to establish the role. Git, tests, a receipt or a temporary path alone do not prove protected source. Stop once the evidence settles the action; no history reconstruction, old-payload hashing or raw experiment records are needed to reinforce it. Clarify an unresolved role before dependent writes.

For `SOURCE_TREE`, preserve source/fixture, unfinished edits, evidence, receipts and routing. A target resolving into it is protected too; ordinary install/update authority does not permit rewriting it. Continue in a supplied safe authorized workspace, or briefly explain protection, ask for its actual path and wait. No release lookup/downloads or further fixture diagnosis is needed before that answer. Keep role evidence and any already known pin private. Do not offer fixture migration as routine setup or switch to global/profile scope without authority.

## Find the active installation

Inspect native discovery, registrations, disabled entries, precedence and resolved paths relevant to the selected host/profile for both skill names. Old-name source payloads or inactive copies do not by themselves require migration. Avoid unrelated host/profile audits and changes to another tool's shared configuration.

For Claude Code, inspect project `.claude/settings.json` and relevant user/profile settings: `extraKnownMarketplaces` identifies sources and `enabledPlugins` identifies enabled entries. An empty personal `installed_plugins.json` does not negate a project-local registration. Establish the selected payload before calling a plugin absent, current or upgraded. For hosts using installed caches, changing a marketplace source alone does not prove the active cached installation changed.

Preserve a usable route. Otherwise recommend native workspace setup for one project, a supported published plugin for managed distribution, or an honest import/link fallback. Ask only about a material scope/behavior/access choice. Session loading is not permanent installation; user-scope defaults still need authority. Reuse successful checks for unchanged source/files/profile/target.

## Choose an action

| Detected state | Action |
| --- | --- |
| `SOURCE_TREE` | Protect source/fixture; continue in a supplied safe authorized target, or ask for its actual path and stop further diagnosis. |
| `CONFLICT` | Multiple active routes or an unrelated occupied target need a choice; do not delete, disable, overwrite or add another copy without that decision. |
| `UNVERIFIED` | Preserve modified/incomplete copies or unresolved provenance; report the gap without replacing them or inventing a source. |
| `ABSENT` | Install into the verified vacant target within the requested scope. |
| `ALREADY_CURRENT` | Keep the usable matching installation, receipt and original time unchanged. |
| `OUTDATED` | Report the update; preserve the working installation until update authority exists. |
| `BLOCKED` | Use the host's normal permission mechanism where supported; otherwise report a supported fallback and limits. Never bypass restrictions. |

Migrating the predecessor name is an update, not a fresh absent-name install. Follow [migration](migration.md), preserve the complete old package, routing and state until replacement is verified, and avoid leaving both names active in the same discovery scope. Do not silently rewrite unrelated routing or task records. Reuse authority already given.

Keep state labels in diagnostics; use a [short result and one actionable question](../INSTALL-FOR-AGENTS.md#one-useful-question-only-when-needed). Explain material failures or unavailable checks, without an unrelated-history report.

## Disable or uninstall a host integration

Distinguish the host's enabled registration/cache from its marketplace source and Git-tracked payload. A request to disable/remove an installed plugin does not authorize deleting a source checkout or pinned fixture. Use the host's supported mechanism within the authorized profile, preserving task state and unrelated settings. If its registration is itself part of a protected fixture, explain that boundary and establish the intended configuration target before changing it. A refusal due to modified files is not permission to force removal; preserve the files and resolve the operation/scope. Do not translate host removal into `git rm`, forced checkout/reset or recursive source deletion.

## Compare the right versions

Read actual SKILL.md, receipts and selected-route metadata. A receipt alone does not prove current integrity. Use the user's version or a published version from the [release table](../README.md#install); a development checkout is not automatically a released update.

Core and host-package versions are independent. For example, OpenAI/Claude Code/OpenCode **0.3.0** packages pin core **0.4.0** and its content hash. Compare core with the selected core, and a host package with its service release. Legacy core **0.2.5** also needs migration to the `diamond-captain` identity; renaming and being outdated can coexist. Never require core and wrapper numbers to match or silently repin published bytes.
