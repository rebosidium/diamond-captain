# Security Policy

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/16014/badge)](https://www.bestpractices.dev/projects/16014)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/rebosidium/diamond-captain/badge)](https://scorecard.dev/viewer/?uri=github.com/rebosidium/diamond-captain)

## Checks and limits

CI checks packages, source, public content and installer fuzzing. [Future-tag attestations](../docs/release-provenance.md) produce Actions artifacts; existing downloads are not retroactively signed. [Controls and limits](../docs/security.md).

Passing is self-assessed; Scorecard is automated. Neither is an independent audit or agent-safety guarantee. No OpenSSF Baseline achievement is claimed.

## Report privately

[Report a vulnerability](https://github.com/rebosidium/diamond-captain/security/advisories/new) (GitHub sign-in required). Keep vulnerability details, credentials and private project data out of public issues/PRs. Include:

- Affected tag/commit and agent/app/model or automation environment.
- Relevant files, security impact and authorization/data boundary.
- Minimal reproduction, expected/actual behavior and redacted evidence; other affected versions or a possible fix, if known.

Use synthetic data and resources you control. Coordinate disclosure with the maintainer during assessment and fixes; response/resolution deadlines are not guaranteed.

## Scope and versions

Covers skill instructions, documentation and repository automation: unauthorized actions/disclosure, unsafe handling of untrusted inputs and package/automation compromise. Demonstrate the impact.

Start with the [latest release](https://github.com/rebosidium/diamond-captain/releases/latest) and identify older affected versions. Fixes use new versions with affected versions and verification limits recorded; published tags/assets are preserved. [Releases and rollback](../docs/releases.md).

Use [Issues](https://github.com/rebosidium/diamond-captain/issues) for usage questions, design feedback and non-security bugs.
