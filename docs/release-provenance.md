# Future-tag build provenance

The **Verified release provenance** workflow builds an accepted future version tag and generates a [GitHub artifact attestation](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations). It uses a short-lived workflow identity, without a maintainer's personal signing key. It stores the archive, public source receipt, SHA-256 checksums and Sigstore verification bundle as Actions artifacts for seven days.

The workflow runs when a new supported version tag is pushed, or when manually dispatched against that exact tag. Supported tags are `vX.Y.Z`, `openai-vX.Y.Z`, `claude-code-vX.Y.Z` and `opencode-vX.Y.Z`. Source must be clean, match the tag/version metadata, descend from activation baseline `22c2c935009b009ac7f71c8db95db2e7fef222bc`, and already be accepted in main. Selecting a branch or an existing source revision at or before that baseline is refused.

The read-only build job reuses the existing host-package builder and preserves declared core pins. Core ZIPs contain the complete `diamond-captain/` skill folder. Archives use deterministic entries; output must be outside source and cannot replace different existing bytes. The separate attestation job consumes the build's exact artifact ID without checking out or running source code. It receives only the additional `id-token: write` and `attestations: write` permissions. Neither job has `contents: write`; there is no release or asset upload API call.

## Release owner

1. Follow the [release process](releases.md), accepting the new version and pins before its tag. Do not move existing tags or change published assets.
2. Inspect the completed workflow and download its signed Actions artifact before expiry. These are build artifacts; this workflow does not create or update a GitHub release.
3. Verify checksums and the attestation. Publishing any new release assets is a separate release-owner action using those verified bytes.

For an archive and its matching bundle, use the [GitHub CLI verification command](https://cli.github.com/manual/gh_attestation_verify):

```sh
gh attestation verify ARCHIVE.zip --repo rebosidium/diamond-captain \
  --bundle MATCHING.sigstore.json --hostname github.com \
  --signer-workflow rebosidium/diamond-captain/.github/workflows/release-provenance.yml \
  --source-ref refs/tags/EXPECTED_TAG --source-digest EXPECTED_PUBLIC_COMMIT \
  --signer-digest EXPECTED_PUBLIC_COMMIT --deny-self-hosted-runners
```

Replace placeholders with independently checked filenames, tag and public source commit. The attestation binds artifact bytes to workflow/source identity; it does not certify that the product is free of vulnerabilities or establish a SLSA build level. Adding the workflow does not sign existing releases. Live signing must be verified on the first accepted future tag; this source change alone is not evidence of a successful run or a higher Scorecard score.

Only maintained product bytes and public source identity belong in build artifacts. Internal reports, raw logs, local paths, task state and personal credentials are excluded. Installer [fuzzing](../fuzz/README.md) is a separate read-only workflow with bounded synthetic inputs and no raw-evidence uploads.
