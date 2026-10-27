# Grok Build compatibility route

Diamond Captain does not currently publish a separate Grok distribution. Where the installed Grok Build supports Claude-compatible plugins, inspect and test the current Claude Code archive using native validation/install/discovery before relying on that route.

Use a disposable profile and preserve normal user configuration. The optional `scripts/check_grok.py` checker accepts an explicitly supplied archive and checksum and performs its checks without login, model calls or a permanent user-profile installation. Keep its detailed reports private.

For a future package containing category-based tool references, preserve the entire skill tree, including `references/tools/`, and verify access from the installed index. A complete archive establishes file integrity; discovery and task execution still need verification on that exact package.

The renamed archive has not been certified for Grok runtime behavior merely because an earlier identity used a similar layout. Follow [host routes](../../docs/host-installation-routes.md) and the official [Grok skill/plugin documentation](https://docs.x.ai/build/features/skills-plugins-marketplaces).
