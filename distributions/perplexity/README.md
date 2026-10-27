# Perplexity Computer import candidate

This route reuses the complete, unchanged [Diamond Captain Claude Code 0.2.0 archive](https://github.com/rebosidium/diamond-captain/releases/download/claude-code-v0.2.0/diamond-captain-claude-code-0.2.0-core-0.3.0.zip), containing canonical core **0.3.0**. The [import pin](import.json) records its published archive digest, public build commit and core dependency. No separate Perplexity version or authored copy of the skill is introduced.

ZIP SHA-256: `5620ab99aa94693fadbea38320aadb0a57d72d7c262b18cf68da8907e6cb776a`.

**The renamed Diamond Captain package has not been imported or executed in the real Perplexity client.** Offline verification and earlier tests under another package identity do not establish that compatibility. See the [compatibility summary](../../docs/perplexity-compatibility.md).

## Prepare locally

Download the pinned archive and its published checksums, verify them, then run from this repository with its local `v0.3.0` tag available:

```sh
python3 scripts/prepare_perplexity.py \
  --archive 'PRIVATE_ARCHIVE/diamond-captain-claude-code-0.2.0-core-0.3.0.zip' \
  --output 'PRIVATE_ARCHIVE/perplexity-import'
```

Replace `PRIVATE_ARCHIVE` with a private directory outside the source checkout. The offline preflight checks archive identity, every receipt/payload hash, the complete tagged core, the new plugin identity and import limits. It copies the identical ZIP into a new handoff directory with `PREFLIGHT.json`, the import pin, instructions, compatibility notes and `SHA256SUMS`. It refuses existing output and checks the handoff for private material before writing. It makes no network, account or model calls; `client_import_verified` remains false.

## Client verification procedure

1. In an authorized personal account, use Perplexity's custom plugin upload if available and select only the verified ZIP. Importing a repository, unrelated local context or an organization-wide installation is a separate action.
2. Confirm exactly one enabled `diamond-captain` skill and inspect its complete supporting files. Upload acceptance alone is insufficient.
3. Explicitly choose the Diamond Captain skill in a fresh Computer conversation. Verify template/reference access, intake-only state initialization, the phase-to-diamond compass and the actual output. Preserve task state separately from the installed skill.
4. Transfer state/artifacts explicitly into another fresh conversation and check recovery, pending acceptance and evidence gaps. Do not assume another session's filesystem is available.

Keep prompts, responses, cloud paths, snapshots, screenshots and detailed test receipts private. Record the exact source/hash and retain failed trials. These steps are a test procedure, not completed client verification or permission for account changes.

## Unreleased core preview

The pinned release above stays unchanged.

The unreleased tool indexes link to category files under `references/tools/`. Keep the complete preview skill tree and verify those links after import; uploading only SKILL.md or an index omits instructions. Successful import of the pinned release does not verify a later source snapshot.

To export committed core edits for a separate private test without assigning a release version:

```sh
python3 scripts/build_skill_preview.py \
  --commit SOURCE_COMMIT \
  --output 'PRIVATE_ARCHIVE/preview'
```

The exporter freezes the complete canonical skill, derives the plugin description from its metadata and creates an unversioned `diamond-captain-preview` plugin. Keep `PREVIEW.json` private and upload only `preview.zip` when a client test is authorized. Use a fresh conversation and the preview namespace explicitly; never update it midway through a comparison. The release owner must later reconcile versions and dependencies before release. A preview does not bypass the release builder's dependency checks.

Preserve previous complete installations and task states when updating. Do not edit generated packages as source. Permanent account removal requires its own authorization.

Official references: [skill uploads](https://www.perplexity.ai/help-center/en/articles/13914413-how-to-use-computer-skills), [plugin uploads and manifest formats](https://www.perplexity.ai/help-center/en/articles/2026100802-create-or-upload-a-custom-plugin), [plugins](https://www.perplexity.ai/help-center/en/articles/2026100701-what-are-plugins). Host documentation describes possible routes; it does not verify this package.
