<p align="center"><img src="assets/mark.svg" width="156" height="64" alt="Three diamonds: Problem, Solution, Outcome"></p>

# Diamond Captain

**Give your AI agent a design process.**

[![Repository checks](https://github.com/rebosidium/diamond-captain/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/rebosidium/diamond-captain/actions/workflows/checks.yml)
[MIT license](LICENSE)

Diamond Captain is an open-source skill for product and service design. It helps your agent investigate a problem, compare solutions, deliver a useful change and review what happens next. You choose the direction and keep control of decisions.

Start at any phase, skip ahead or loop back. The agent keeps a checkpoint, distinguishes evidence from assumptions and asks whether to accept, revise or reopen a handoff. It works with UI and non-UI tasks, using the tools and evidence you actually have.

## Start with your agent

```text
Set up Diamond Captain for this workspace:
https://github.com/rebosidium/diamond-captain/blob/main/INSTALL-FOR-AGENTS.md
```

Then describe your task. [Manual installation](START-HERE.md) · [User guide](docs/guide/README.md)

## Install

Choose one active installation to avoid duplicate skill entries. Download the ZIP and matching checksums from the selected release.

| Host | Package and instructions | Invocation |
| --- | --- | --- |
| Codex / compatible OpenAI plugin tooling | [OpenAI 0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/openai-v0.2.0) · [Guide](distributions/openai/README.md) | `diamond-captain:diamond-captain`, or `$diamond-captain` for a native skill |
| Claude Code | [Claude Code 0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/claude-code-v0.2.0) · [Guide](distributions/claude-code/README.md) | `/diamond-captain:diamond-captain` |
| OpenCode | [OpenCode 0.2.0](https://github.com/rebosidium/diamond-captain/releases/tag/opencode-v0.2.0) · [Guide](distributions/opencode/README.md) | Ask the agent to use `diamond-captain` |
| Cursor, Gemini CLI, Grok Build, Perplexity Computer | [Host installation routes](docs/host-installation-routes.md) | Use the host's supported native/plugin/import route and verify discovery |
| Manual | [Core 0.3.0](https://github.com/rebosidium/diamond-captain/releases/tag/v0.3.0) or the complete [.agents/skills/diamond-captain/](.agents/skills/diamond-captain/) folder | Follow the selected host's skill mechanism |

The packages contain the complete pinned core, including references and templates. Downloadable archives do not imply a marketplace listing or that every host/import surface has been runtime-tested.

## Three diamonds, six thinking modes

| Diamond | Broaden | Focus |
| --- | --- | --- |
| Problem | Discover needs, context and alternative causes | Define the problem, scope and expected change |
| Solution | Develop materially different approaches | Deliver a selected, verified solution or handoff |
| Outcome | Deploy and observe actual use | Digest evidence and decide the next iteration |

These are thinking modes, not mandatory timeboxes. Prepared work, a released change and a verified live outcome are distinct results. No specific model, design app or integration is required.

## Learn and verify

- [User guide](docs/guide/README.md), [skill guide](.agents/skills/diamond-captain/README.md), [full process](docs/process.md).
- [Compatibility and checks](docs/validation.md), [security](docs/security.md), [release and rollback](docs/releases.md).
- [Changelog](CHANGELOG.md), [migration from the previous skill name](docs/migration.md), [contributing](CONTRIBUTING.md).

This repository distributes the product and reproducible checks. Internal development records and execution logs are not included. No third-party security certificate is claimed for this new repository.

## License

[MIT](LICENSE) © 2026 rebosidium. The original triple-diamond mark is included. Stage icons are from [Tabler Icons](assets/icons/README.md), with their [MIT notice](assets/icons/LICENSE). Linked third-party materials retain their licenses.
