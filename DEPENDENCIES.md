# Dependencies

The skill is Markdown/YAML plus templates and has no mandatory product integration or model dependency. Packaging, installation and checks use Python standard-library code and Git. Use Python 3.10+ for repository contribution checks; CI selects its declared Python version.

The canonical skill includes an optional standard-library Python intake initializer. It creates only the first task checkpoint, refuses existing files and does not run on plugin import. Hosts without Python use the skill's explicit manual/pasteable-state fallback.

The optional `scripts/prepare_perplexity.py` verifies and copies an explicitly downloaded, pinned Claude ZIP without changing it or making network/account/model calls. `scripts/build_skill_preview.py` exports an explicitly committed canonical skill for private tests without changing release pins, versions or tags. Its plugin description comes from canonical metadata. Keep generated handoffs, preview receipts and execution records outside source checkouts. See the [Perplexity guide](distributions/perplexity/README.md).

Workflow dependencies are declared in `.github/workflows/` and pinned to exact commits of their upstream Actions. Dependabot proposes updates; they are reviewed through PRs. Optional tools linked by the skill are candidates selected for the user's task, not installed runtime dependencies.

The product and core are MIT licensed. Stage icons have their separate included MIT notice. Third-party host clients and linked documentation retain their own terms.

Optional installer fuzzing uses the version/hash-pinned Atheris development dependency in [fuzz/requirements.txt](fuzz/requirements.txt), with its own [scope and execution instructions](fuzz/README.md). It is not a skill runtime or packaging dependency. Release provenance uses the SHA-pinned GitHub Actions declared in its workflow and the runner's GitHub CLI; no personal signing key or stored personal access token is required.
