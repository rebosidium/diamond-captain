# Host installation routes

Use one active installation and verify its scope, path, version and supporting files. Official host support does not by itself establish that this renamed package was runtime-tested on that host.

| Host | Route | Verify |
| --- | --- | --- |
| Codex | Native `.agents/skills/diamond-captain/`, or the [OpenAI plugin](../distributions/openai/README.md) | Request `$diamond-captain` for native use, or the namespaced plugin skill; inspect the selected source |
| Claude Code | [Claude plugin](../distributions/claude-code/README.md) | Load the package, verify discovery and invoke `/diamond-captain:diamond-captain` |
| OpenCode | [Native distribution](../distributions/opencode/README.md) | Dry-run/install in the chosen workspace and verify one discovered skill |
| Cursor | Native `.cursor/skills/diamond-captain/` where supported, or a supported plugin route | Check the actual active source and packaged references |
| Gemini CLI | Its supported workspace/user native-skill install mechanism | Verify its skill inventory and the selected source; do not assume Codex precedence |
| Grok Build | A [Claude-compatible package route](../distributions/grok-build/README.md), where supported | Validate/install/discover this exact new archive before claiming runtime compatibility |
| Perplexity Computer | Supported Skills import, or complete skill ZIP/plugin upload where the account supports it | Confirm supporting-file preservation and account scope; a text attachment alone is not proof of a complete install |

The native core is [released separately](https://github.com/rebosidium/diamond-captain/releases/tag/v0.3.0). Do not copy SKILL.md alone. Preserve references, templates and the included license.

Official references: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins/create), [OpenCode skills](https://docs.opencode.ai/docs/skills/), [Cursor skills](https://cursor.com/docs/context/skills), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), [Grok plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces), [Perplexity help](https://www.perplexity.ai/help-center).

See [verification limits](validation.md), [installation](../START-HERE.md) and [update/rollback](releases.md).
