# Verify installation and record provenance

Read after the target and action are settled, when checking an installation or recording a new copy. [Agent setup](../INSTALL-FOR-AGENTS.md) and relevant [decision rules](installation-decisions.md) establish role, scope and authority first. Setup authority does not grant publication, marketplace submissions, sharing private records, connectors, credentials or background jobs.

## Install or replace safely

Follow the selected [host procedure](host-installation-routes.md). Verify a downloaded archive against its matching published SHA-256 before use; stop on mismatch. For pinned Git source, resolve the selected published tag/commit and compare the complete payload with that tree. An archive hash identifies the archive, not an extracted folder.

Copy the entire skill tree, including nested references, scripts, templates, tests and license. A lone SKILL.md is incomplete. During authorized replacement, preserve the complete previous installation and receipt outside discovery roots, replace the intended directory wholesale, then verify. Preserve `.product-task/`, artifacts, unrelated skills and settings. Keep backups private and outside tracked project files and public attachments; being outside discovery roots alone does not prevent publication. See [update/rollback](releases.md#update-or-roll-back-an-installation).

If copying, receipt recording or verification fails, report `INCOMPLETE` with actual remaining files and restore the prior installation when possible. Do not claim success or overwrite newer task state during recovery. Preserve unrequested files and unfinished work.

## Check actual results

Check complete membership and every payload byte against selected published source, read the installed name/version, and inspect actual host discovery where available. Verify supporting reference/template access and the selected source/cache in a fresh relevant session. Existing conversations can retain previously loaded instructions. Reuse successful checks for unchanged source/files/profile/target; recheck affected inputs if freshness is uncertain. Setup needs no unrelated-fixture audit or design-task experiment.

Keep checks distinct:

- `tests/check_package.py` checks Markdown links, not completeness, provenance or discovery.
- Payload hashes establish identity/integrity. A receipt records provenance but cannot prove current files unchanged.
- Discovery establishes that the host finds the selected skill; it does not prove activation, task execution or live outcomes.

Record the actual result: `INSTALLED`, `UPDATED`, `UNCHANGED`, `FALLBACK` or `INCOMPLETE`. Keep provenance/check details private; give a short result in the user's language: action, relevant version(s), availability (all local projects / one project / this session), invocation and material limits/next step. Use exact paths only when useful; explain blocking failures without manifest, hash or registry dumps. Unavailable checks stay unverified, and a fallback is not persistent installation. No changed installation means no new receipt or invented time.

## Manual installation receipt

For a successful new manual personal copy, save `~/.diamond-captain-installations/<host-id>/manual.json` in the same user profile, using a lowercase host ID such as `codex` or `claude-code`. For an explicitly project-only copy, use `.diamond-captain-installations/<host-id>/manual.json` in that project. Keep receipts outside payload/discovery roots. Use a managed route's existing receipt convention when it provides one; do not put a global installation receipt into an arbitrary project.

This runtime receipt contains private installation details. Keep it local and outside tracked files, shared archives and public attachments, even when the skill itself is public. Do not modify or relocate existing receipts without authority. Public `DISTRIBUTION.json` supplied with a service release is different: retain service packages' distribution and installer-generated formats. Legacy fixture receipts are historical records, not templates to normalize or rewrite.

Record actual values:

| JSON field | Value |
| --- | --- |
| `schema_version`, `route`, `host` | Integer `1`, string `manual-copy`, actual host identifier |
| `target`, `resolved_target` | Actual install path (personal absolute path or project-relative path) and resolved absolute path |
| `source_repository`, `source_tag`, `source_commit` | Repository URL, selected published tag and resolved full commit SHA |
| `core_version` | Version read from installed SKILL.md |
| `artifact_url`, `artifact_sha256` | Downloaded archive URL and verified SHA-256; JSON `null` for both when copied from a pinned Git tree |
| `files_sha256` | Every payload-relative file and verified SHA-256, compared with pinned source, not only itself |
| `installed_at_utc` | Actual successful-copy time in ISO 8601 UTC |

Do not substitute moving `main` for the selected release commit. For unchanged legacy copies without receipts, report verified provenance and unknowns rather than inventing history. Current usable installations keep their receipts and original times unchanged.

After usable setup, invite the user's task. If one was supplied, load the installed skill and recover its state or initialize it in the actual task project. Setup alone creates no product task and requires no six-phase execution.
