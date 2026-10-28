# Host installation routes

Default to a personal installation for all local projects in the selected agent. Use one active route and verify its profile, path, version and supporting files. Project-only or session-only setup requires an explicit choice; personal installation does not sync to other machines or cloud accounts. Official host support does not by itself establish that this renamed package was runtime-tested on that host.

For all seven hosts, follow [shared agent setup](../INSTALL-FOR-AGENTS.md): settle the agent and intended personal profile first, inspect only the relevant installation, verify the selected package and give a short result. Ask one actionable question only when the agent/profile, access or a consequential choice is unresolved; keep technical diagnostics private unless needed to explain a failure. The route-specific checks below still apply.

| Host | Route | Verify |
| --- | --- | --- |
| Codex | Personal `~/.agents/skills/diamond-captain/`, or the [OpenAI plugin](../distributions/openai/README.md) | Request `$diamond-captain` for native use, or the namespaced plugin skill; inspect the selected source |
| Claude Code | Personal native `~/.claude/skills/diamond-captain/`, or a persistent user-scoped [Claude plugin](../distributions/claude-code/README.md) | Plugin: `/diamond-captain:diamond-captain`; native: `/diamond-captain`. Check the selected source; plugin session loading is not persistent installation |
| OpenCode | Personal native `~/.config/opencode/skills/diamond-captain/`; [distribution guide](../distributions/opencode/README.md) | Verify one discovered skill; the published `install.py --project` route installs in one project only |
| Cursor | Supported personal skill/plugin route; `.cursor/skills/diamond-captain/` is the project-only alternative | Check the actual active source and packaged references |
| Gemini CLI | Personal native `~/.gemini/skills/diamond-captain/` or its supported user-scoped installer | Verify its skill inventory and the selected source; do not assume Codex precedence |
| Grok Build | A supported personal [Claude-compatible package route](../distributions/grok-build/README.md); do not assume Claude Code profile settings apply | Validate/install/discover this exact new archive before claiming runtime compatibility |
| Perplexity Computer | [Pinned Claude ZIP import candidate](../distributions/perplexity/README.md), where supported | Account import has that account's reach, not local all-project installation. Offline verification preserves the complete released core; real-client tests for Diamond Captain remain pending. Confirm supporting files, account scope and the actual selected source. |

The listed paths are normal defaults; resolve the intended profile's actual home/config location before copying. Use each host's own discovery rules; a personal path may be shared with compatible hosts, and project overrides can affect which copy loads. Preserve unrelated configuration. Browser chat, cloud import and session-only flags do not establish a personal local installation.

When a previous skill identity is already active, use the [migration procedure](migration.md) rather than adding a second copy. Verify project/user scope and the actual selected source; a local path or invocation valid for one host does not establish another host's installation.

The native core is [released separately](https://github.com/rebosidium/diamond-captain/releases/tag/v0.4.1). Do not copy SKILL.md alone. Preserve references, templates and the included license.

Official references: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins/create), [OpenCode skills](https://docs.opencode.ai/docs/skills/), [Cursor skills](https://cursor.com/docs/context/skills), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), [Grok plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces), [Perplexity help](https://www.perplexity.ai/help-center).

See [verification limits](validation.md), [installation](../START-HERE.md) and [update/rollback](releases.md).
