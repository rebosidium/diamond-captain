# Skill and host packages

The canonical product is `.agents/skills/diamond-captain/`. Host adapters contain metadata and installation instructions; the builder bundles the complete pinned core without maintaining a second authored SKILL.md.

Current core: **0.5.0**. OpenAI, Claude Code and OpenCode packages: **0.3.2** each, pinned to complete core **0.5.0**. Core and service versions are independent. Each service pins both the core version and its aggregate SHA-256; mismatched source fails the build.

The [Perplexity import candidate](../distributions/perplexity/README.md) reuses a separately pinned, unchanged Claude Code archive rather than introducing another version or skill. Offline preparation is checked; real-client compatibility for the Diamond Captain identity is pending. [Historical test limits](perplexity-compatibility.md) remain explicit.

Unreleased canonical edits use a separate committed-source preview for private tests. They cannot silently enter an existing release under its old core hash. Packaging tests exercise pinned release bytes in disposable repositories and separately verify refusal of drift; passing them does not release the working core.

## Complete supporting files

Host wrappers use one canonical skill tree. Tool indexes can link to nested category files under `references/tools/`; copy the whole directory tree, including scripts, templates and license. Do not install only SKILL.md or the indexes. The published package receipt, rather than the current source layout, identifies the files belonging to that release.

Source refactoring keeps the skill identity, host invocations and project state path unchanged. New source files require a new accepted core dependency before they can appear in released host packages. A development preview verifies committed source transport separately; it is not a release or a claim of host runtime compatibility.

Receipts identify the public source/build commit and per-file hashes. ZIPs and JSON receipts have matching checksum assets. Release builds require a clean committed product checkout and the core release tag.

```sh
python3 .agents/skills/diamond-captain/tests/check_package.py
python3 -m unittest discover -s tests -v
python3 scripts/build_distribution.py opencode --release
```

Use the selected [service guide](../README.md#install) for installation. Standalone downloadable packages do not imply a marketplace listing, UI import or end-to-end model execution in every host. See [verification](validation.md) and [release/rollback](releases.md).
