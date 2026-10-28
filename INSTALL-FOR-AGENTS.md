# Install Diamond Captain

**Default: all my projects.** A new install request under this guide selects the current user's personal installation for the selected agent on this computer. Say this briefly and proceed without asking for a project folder or repeating the scope question. Honor an explicit one-project or session-only request. This does not configure every agent, other users, system-wide settings or cloud accounts.

**Before writes:** identify the actual agent and user profile, resolve the installation path and protect maintained skill/plugin/marketplace sources and pinned QA fixtures (`SOURCE_TREE`). Git, temporary paths or receipts alone do not prove that role. An isolated test profile is not the user's normal installation: establish the intended profile before changing it. Preserve task state, unfinished work and unrelated settings; never uninstall by deleting source.

Reuse existing scope/update authority. The default authorizes a new personal installation, not replacement of an existing copy, migration, publication, connectors, credentials or background jobs. Required host permissions still apply.

## Choose the next action

1. **Choose the supported personal route.** Use the agent's normal personal skill location or persistent user plugin installation. A protected current project does not block installation into a verified separate personal location. No new project folder is needed. If the intended profile/location is unresolved or unavailable, stop dependent writes/downloads and ask one useful question; do not invent a sibling folder or silently fall back to a project/session-only copy. Read [decision rules](docs/installation-decisions.md) only for an unresolved choice.
2. **One host and route.** Follow the relevant [host route](docs/host-installation-routes.md). Check native discovery and project/user plugin registrations affecting that host/profile for both `diamond-captain` and `design-process-dr`. Preserve a working route that meets the requested availability; resolve a conflicting/unverified copy before changes. A selected legacy installation needs authorized [migration](docs/migration.md); an empty personal registry alone does not prove absence.
3. **Install and verify once.** Use the requested version or a published release. Follow [verification and receipts](docs/installation-verification.md): verify checksum/pinned source and the complete payload/license, back up an authorized replacement outside discovery roots, and check discovery where available. Reuse successful checks for unchanged source/files/profile/target. On failure report `INCOMPLETE` and restore the previous installation when possible.
4. **Short result.** State the action, relevant core/package versions, availability (all local projects / one project / this session), invocation and any material limitation or next step. Keep detailed provenance private. Distinguish integrity, discovery and execution; never imply an unavailable check passed. Skill availability does not share task data: checkpoints stay with their actual tasks.

## One useful question, only when needed

Use the user's language and reuse settled answers/authority. Ask only about an unknown agent/profile, a conflict or a genuinely missing destination for an explicitly project-only install. Recommend the route instead of asking novices to choose technical equivalents. Do not offer rewriting a protected fixture as routine setup.

For example: "This is a test profile. Should Diamond Captain be available in your normal Claude Code?" If access is unavailable, explain the supported next step. For an explicitly project-only install, ask for the actual project path; "another folder" alone is not a destination.

Start design work only when requested, using the installed skill and existing task state. Setup alone needs no product-task creation or six-phase run.
