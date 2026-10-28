# Installer fuzzing

`installer_fuzzer.py` uses Atheris coverage-guided fuzzing against the actual native installer. It checks path confinement, malformed manifest string values, payload hashes, source symlink refusal, real installation/replacement controls, dry-run non-mutation and preservation of synthetic project state/settings. An implementation that refuses every input fails the valid-installation controls.

The harness creates bounded synthetic packages in temporary directories. It makes no network calls, invokes no agent/model and never installs into a real user workspace. It is not a complete JSON-schema, archive-extractor, Windows-platform or model-behavior test. The installer accepts extracted distributions; ZIP extraction is not presented as its runtime interface.

The regular test suite invokes the same properties without installing Atheris:

```sh
python3 -B -m unittest discover -s tests -p test_fuzz_properties.py -v
```

## Coverage-guided execution

The CI dependency is pinned by version and wheel SHA-256 for CPython 3.12 on Linux x86_64. It is development tooling and is not included in the skill or host packages. Install into an isolated virtual environment and keep the corpus/crash directories outside source checkouts:

```sh
python3.12 -m venv /tmp/diamond-captain-fuzz-venv
/tmp/diamond-captain-fuzz-venv/bin/pip install --require-hashes --only-binary=:all: --no-deps -r fuzz/requirements.txt
mkdir -p /tmp/diamond-captain-corpus /tmp/diamond-captain-crashes
/tmp/diamond-captain-fuzz-venv/bin/python -B fuzz/installer_fuzzer.py \
  /tmp/diamond-captain-corpus -seed=1 -max_total_time=120 \
  -timeout=5 -rss_limit_mb=512 -max_len=4096 \
  -artifact_prefix=/tmp/diamond-captain-crashes/
```

The CI workflow runs on PRs, main pushes, a weekly schedule and manual dispatch, with a clean process environment and no persisted checkout credentials. It does not use pull_request_target, write permissions, personal tokens, artifact uploads, SARIF uploads or public crash comments. Raw fuzz output and generated inputs stay in runner-temporary storage and expire with the job; a failure is reported as a concise failed check. Reproduce and retain any detailed evidence locally. Corpus generation depends on the engine version and execution budget; do not claim complete coverage or identical cross-platform runs.

The current Scorecard implementation recognizes Python/Atheris fuzz targets. A successful CI run and the subsequent Scorecard result must be checked after deployment; adding an import or workflow file alone is not evidence of an executed fuzz test.
