# Security and trust

Diamond Captain distributes readable skill instructions, host packaging and installation helpers. [MIT licensing](../LICENSE) and third-party notices are included. Report vulnerabilities through the [private reporting channel](../.github/SECURITY.md); do not disclose private reproduction data in a public issue.

The product repository uses read-only pull-request checks, SHA-pinned workflow dependencies, disabled persisted checkout credentials, public-content inspection and automated package tests. Protected main changes require a PR and successful checks. Secret scanning, dependency alerts and source scanning complement these checks where enabled in repository settings.

Inspect actual [Actions](https://github.com/rebosidium/diamond-captain/actions), [Security](https://github.com/rebosidium/diamond-captain/security) and [repository rules](https://github.com/rebosidium/diamond-captain/rules). A passing result is limited to its checked revision and scope; it is not independent security certification or proof that every agent action is safe.

Diamond Captain has earned [OpenSSF Best Practices Passing](https://www.bestpractices.dev/en/projects/16014/passing) through a project-maintained self-assessment of its published criteria. The separate [OpenSSF Scorecard](https://scorecard.dev/viewer/?uri=github.com/rebosidium/diamond-captain) reports automated repository-practice checks and their remaining findings. These assessments belong to this repository; they do not certify every agent action or constitute an independent security audit. No OpenSSF Baseline achievement is claimed.
