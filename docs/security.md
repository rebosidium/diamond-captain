# Security and trust

Readable skill instructions, host packages and Python helpers use [MIT](../LICENSE), with third-party notices. [Report vulnerabilities privately](../.github/SECURITY.md); omit sensitive reproduction data from public issues.

Protected main requires PRs and passing package, source and public-content checks. Actions are SHA-pinned; checkout credentials are not persisted. [Installer fuzzing](../fuzz/README.md) uses bounded synthetic inputs without raw-evidence uploads. Secret scanning/dependency alerts apply where enabled.

[Future-tag provenance](release-provenance.md) uses separate signing with short-lived GitHub identity: Actions artifacts/attestations only, no release uploads or contents-write permission. Existing downloads remain unchanged and are not retroactively signed.

[OpenSSF Passing](https://www.bestpractices.dev/en/projects/16014/passing) is project-maintained self-assessment; [Scorecard](https://scorecard.dev/viewer/?uri=github.com/rebosidium/diamond-captain) lists automated checks/findings. Neither is an independent audit or agent-safety guarantee. No OpenSSF Baseline achievement is claimed.

Check [Actions](https://github.com/rebosidium/diamond-captain/actions), [Security](https://github.com/rebosidium/diamond-captain/security) and [rules](https://github.com/rebosidium/diamond-captain/rules). Results cover only the checked revision and scope.
