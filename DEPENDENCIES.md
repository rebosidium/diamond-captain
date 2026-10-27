# Dependencies

The skill is Markdown/YAML plus templates and has no mandatory product integration or model dependency. Packaging, installation and checks use Python standard-library code and Git. Use Python 3.10+ for repository contribution checks; CI selects its declared Python version.

Workflow dependencies are declared in `.github/workflows/` and pinned to exact commits of their upstream Actions. Dependabot proposes updates; they are reviewed through PRs. Optional tools linked by the skill are candidates selected for the user's task, not installed runtime dependencies.

The product and core are MIT licensed. Stage icons have their separate included MIT notice. Third-party host clients and linked documentation retain their own terms.
