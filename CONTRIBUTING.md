# Contributing

Use Issues for ordinary defects and suggestions; report vulnerabilities through [.github/SECURITY.md](.github/SECURITY.md). Include the affected version, minimal anonymized reproduction, expected/actual behavior and verification limits.

Contribute focused product changes through a topic branch and PR. Keep internal working reports, raw agent/tool logs, resource measurements, populated task states and credentials out of every public branch, description and attachment. Preserve licenses, user project state and published package bytes.

Run before proposing a change:

```sh
python3 .agents/skills/diamond-captain/tests/check_package.py
python3 scripts/check_docs.py
python3 scripts/check_public_content.py --history HEAD
python3 -m unittest discover -s tests -v
python3 -m compileall -q .agents/skills/diamond-captain/tests scripts tests
```

Explain the user-facing change and concise checks/limits. CI is a second barrier after upload; review the full outgoing history and files before pushing any public branch. Maintainers merge through protected main after checks. Core and host versions remain independent; new public packages must preserve their declared source/hash pins and include checksums.
