<p align="center"><img src="assets/logo.png" width="600" alt="Diamond Captain logo: a cartoon pirate captain with a parrot wearing an AI medallion"></p>

<h1 align="center">Diamond Captain — Your Triple Diamond needs a captain!</h1>

<div align="center">

[![Repository checks](https://github.com/rebosidium/diamond-captain/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/rebosidium/diamond-captain/actions/workflows/checks.yml)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/16014/badge)](https://www.bestpractices.dev/projects/16014)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/rebosidium/diamond-captain/badge)](https://scorecard.dev/viewer/?uri=github.com/rebosidium/diamond-captain)
[![MIT license](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/rebosidium/diamond-captain)](https://github.com/rebosidium/diamond-captain/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/rebosidium/diamond-captain?style=flat)](https://github.com/rebosidium/diamond-captain/stargazers)<br>
[![Support AI: Codex](https://img.shields.io/badge/Support_AI-Codex-2563EB?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIxMDAgMTAwIDQxMSA0MTEiIGZpbGw9Im5vbmUiIGNvbG9yPSJ3aGl0ZSI%2BPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yNTIuNzk0IDEwOC44MDJDMjg5LjE5MSA5OS4wNDg0IDMyNi4yNjUgMTEwLjMwNSAzNTEuMTQ4IDEzNS4xMzVDMzg1LjExMyAxMjYuMDcyIDQyMi44NSAxMzQuODYyIDQ0OS40OTIgMTYxLjUwNUM0NzYuMTM2IDE4OC4xNDkgNDg0LjkyNSAyMjUuODg4IDQ3NS44NjIgMjU5Ljg1VjI1OS44NTRDNTAwLjY5NiAyODQuNzM1IDUxMS45NSAzMjEuODEgNTAyLjE5OCAzNTguMjA3QzQ5Mi40NDcgMzk0LjYwMiA0NjQuMTYxIDQyMS4wODQgNDMwLjIxNSA0MzAuMjE3QzQyMS4wODMgNDY0LjE2MiAzOTQuNjAzIDQ5Mi40NDggMzU4LjIwNiA1MDIuMTk5QzMyMS44MTIgNTExLjk1MSAyODQuNzM0IDUwMC42OTMgMjU5Ljg1MiA0NzUuODY0QzIyNS44ODcgNDg0LjkyNyAxODguMTUgNDc2LjEzNyAxNjEuNTA3IDQ0OS40OTVDMTM0Ljg2NCA0MjIuODUxIDEyNi4wNzMgMzg1LjExMSAxMzUuMTM2IDM1MS4xNDlDMTEwLjMwNCAzMjYuMjY2IDk5LjA0OTYgMjg5LjE5MiAxMDguODAxIDI1Mi43OTVDMTE4LjU1MiAyMTYuNCAxNDYuODQgMTg5LjkxOCAxODAuNzg0IDE4MC43ODVDMTg5LjkxNyAxNDYuODQxIDIxNi4zOTYgMTE4LjU1MyAyNTIuNzk0IDEwOC44MDJaTTM3NC4yOTIgNDA3LjE0NUMzNzQuMjkyIDQxMS4yNzEgMzcyLjA5MiA0MTUuMDg2IDM2OC41MTcgNDE3LjE0OEwyODMuNzIzIDQ2Ni4xMDJDMzAyLjQ4NyA0ODAuNTg1IDMyNy41NTUgNDg2LjQ1OSAzNTIuMjE3IDQ3OS44NTJDMzg2Ljk5NyA0NzAuNTMyIDQxMC4wNjggNDM5LjMxMiA0MTAuNTU1IDQwNS4wMDZWMzE3LjcxN0M0MTAuNTU1IDMxNS4wOCA0MDkuMTI1IDMxMi42MjEgNDA2Ljg0MyAzMTEuMzAzTDM3NC4yOTIgMjkyLjUwOVY0MDcuMTQ1Wk0yNTEuODY4IDQxNS44OTdDMjQ4LjI5NiA0MTcuOTU5IDI0My44OTMgNDE3Ljk1OSAyNDAuMzE3IDQxNS44OTdMMTU1LjUyNiAzNjYuOTQyQzE1Mi4zNjYgMzkwLjQzNiAxNTkuODExIDQxNS4wOCAxNzcuODY2IDQzMy4xMzZIMTc3Ljg2M0MyMDMuMzI1IDQ1OC41OTQgMjQxLjg5NiA0NjIuOTYyIDI3MS44NSA0NDYuMjMyTDM0Ny40NDkgNDAyLjU4NkMzNDkuNzM1IDQwMS4yNjggMzUxLjE0OCAzOTguOCAzNTEuMTQ4IDM5Ni4xNjNWMzU4LjU3OUwyNTEuODY4IDQxNS44OTdaTTM2OC42MDIgMjIwLjYyOEMzNjYuMzE5IDIxOS4zMDkgMzYzLjQ3NCAyMTkuMzE4IDM2MS4xOTEgMjIwLjYzN0wzMjguNjQxIDIzOS40MzFMNDI3LjkyMSAyOTYuNzQ5QzQzMS40OTYgMjk4LjgxMSA0MzMuNjk3IDMwMi42MjcgNDMzLjY5NyAzMDYuNzUyVjQwNC42NjFDNDU1LjYyMiAzOTUuNjU0IDQ3My4yNDQgMzc2Ljg4MSA0NzkuODUxIDM1Mi4yMThDNDg5LjE2OSAzMTcuNDQyIDQ3My42NjggMjgxLjg1IDQ0NC4yMDEgMjY0LjI3NEwzNjguNjAyIDIyMC42MjhaTTE3Ny4zMDMgMjA2LjM0QzE1NS4zNzcgMjE1LjM0OCAxMzcuNzU2IDIzNC4xMjIgMTMxLjE0OCAyNTguNzgzQzEyMS44MzIgMjkzLjU2MSAxMzcuMzMxIDMyOS4xNTMgMTY2Ljc5OSAzNDYuNzI3TDI0Mi4zOTggMzkwLjM3M0MyNDQuNjggMzkxLjY5MiAyNDcuNTI1IDM5MS42ODQgMjQ5LjgwNyAzOTAuMzY2TDI4Mi4zNTcgMzcxLjU3MkwxODMuMDc4IDMxNC4yNTNDMTc5LjUwNCAzMTIuMTg5IDE3Ny4zMDMgMzA4LjM3NSAxNzcuMzAzIDMwNC4yNTFWMjA2LjM0Wk0yNTkuODQ5IDI3OS4xNDVWMzMxLjg1OEwzMDUuNSAzNTguMjEzTDM1MS4xNSAzMzEuODU4VjI3OS4xNDVMMzA1LjUgMjUyLjc4OUwyNTkuODQ5IDI3OS4xNDVaTTMyNy4yNzYgMTQ0LjlDMzA4LjUxMiAxMzAuNDE4IDI4My40NDUgMTI0LjU0MyAyNTguNzgyIDEzMS4xNUMyMjQuMDAyIDE0MC40NzEgMjAwLjkzMSAxNzEuNjkxIDIwMC40NDUgMjA1Ljk5NVYyOTMuMjg2QzIwMC40NDUgMjk1LjkyMyAyMDEuODc1IDI5OC4zODEgMjA0LjE1OCAyOTkuN0wyMzYuNzA3IDMxOC40OTNWMjAzLjg1NkMyMzYuNzA3IDE5OS43MzEgMjM4LjkwOSAxOTUuOTE2IDI0Mi40ODMgMTkzLjg1M0wzMjcuMjc2IDE0NC45Wk00MzMuMTM3IDE3Ny44NjdDNDA3LjY3NSAxNTIuNDA3IDM2OS4xMDMgMTQ4LjAzOCAzMzkuMTQ5IDE2NC43NjlMMjYzLjU1IDIwOC40MTVDMjYxLjI2NSAyMDkuNzM0IDI1OS44NTIgMjEyLjIwMiAyNTkuODUyIDIxNC44MzhWMjUyLjQyM0wzNTkuMTMyIDE5NS4xMDVDMzYyLjcwMyAxOTMuMDQxIDM2Ny4xMDggMTkzLjA0MSAzNzAuNjgyIDE5NS4xMDVMNDU1LjQ3MyAyNDQuMDZDNDU4LjYzNSAyMjAuNTY3IDQ1MS4xODkgMTk1LjkyMiA0MzMuMTM1IDE3Ny44NjdINDMzLjEzN1oiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48L3N2Zz4%3D)](distributions/openai/README.md)
[![Support AI: Claude Code](https://img.shields.io/badge/Support_AI-Claude_Code-2563EB?logo=claudecode&logoColor=white)](distributions/claude-code/README.md)
[![Support AI: OpenCode](https://img.shields.io/badge/Support_AI-OpenCode-2563EB?logo=opencode&logoColor=white)](distributions/opencode/README.md)<br>
[![Install route: Cursor](https://img.shields.io/badge/Install_route-Cursor-64748B?logo=cursor&logoColor=white)](docs/host-installation-routes.md)
[![Install route: Gemini CLI](https://img.shields.io/badge/Install_route-Gemini_CLI-64748B?logo=googlegemini&logoColor=white)](docs/host-installation-routes.md)
[![Compatibility route: Grok Build](https://img.shields.io/badge/Compatibility_route-Grok_Build-64748B?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2aWV3Qm94PSIwIDAgMTAyNCAxMDI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMzk1LjQ3OSA2MzMuODI4TDczNS45MSAzODEuMTA1Qzc1Mi41OTkgMzY4LjcxNSA3NzYuNDU0IDM3My41NDggNzg0LjQwNiAzOTIuNzkyQzgyNi4yNiA0OTQuMjg1IDgwNy41NjEgNjE2LjI1MyA3MjQuMjg4IDY5OS45OTZDNjQxLjAxNiA3ODMuNzM5IDUyNS4xNTEgODAyLjEwNCA0MTkuMjQ3IDc2MC4yNzdMMzAzLjU1NiA4MTQuMTQzQzQ2OS40OSA5MjguMjAyIDY3MC45ODcgODk5Ljk5NSA3OTYuOTAxIDc3My4yODJDODk2Ljc3NiA2NzIuODQzIDkyNy43MDggNTM1LjkzNyA4OTguNzg1IDQxMi40NzZMODk5LjA0NyA0MTIuNzM5Qzg1Ny4xMDUgMjMxLjM3IDkwOS4zNTggMTU4Ljg3NCAxMDE2LjQgMTAuNjMyNkMxMDE4LjkzIDcuMTE3NzEgMTAyMS40NyAzLjYwMjc5IDEwMjQgMEw4ODMuMTQ0IDE0MS42NTFWMTQxLjIxMkwzOTUuMzkyIDYzMy45MTYiIGZpbGw9IndoaXRlIi8%2BCjxwYXRoIGQ9Ik0zMjUuMjI2IDY5NS4yNTFDMjA2LjEyOCA1ODAuODQgMjI2LjY2MiA0MDMuNzc2IDMyOC4yODUgMzAxLjY2OEM0MDMuNDMxIDIyNi4wOTcgNTI2LjU0OSAxOTUuMjU0IDYzNC4wMjYgMjQwLjU5Nkw3NDkuNDU0IDE4Ni45OTRDNzI4LjY1NyAxNzEuODggNzAyLjAwNyAxNTUuNjIzIDY3MS40MjQgMTQ0LjJDNTMzLjE5IDg2Ljk5NDIgMzY3LjY5MyAxMTUuNDY1IDI1NS4zMjMgMjI4LjM4MkMxNDcuMjM0IDMzNy4wODEgMTEzLjI0NCA1MDQuMjE1IDE3MS42MTMgNjQ2LjgzM0MyMTUuMjE2IDc1My40MjMgMTQzLjczOSA4MjguODE4IDcxLjczODUgOTA0LjkxNkM0Ni4yMjM3IDkzMS44OTMgMjAuNjIxNiA5NTguODcgMCA5ODcuNDI5TDMyNS4xMzkgNjk1LjMzOSIgZmlsbD0id2hpdGUiLz4KPC9zdmc%2BCg%3D%3D)](distributions/grok-build/README.md)
[![Import candidate: Perplexity Computer](https://img.shields.io/badge/Import_candidate-Perplexity_Computer-D97706?logo=perplexity&logoColor=white)](distributions/perplexity/README.md)<br>
[![Process: Triple Diamond](https://img.shields.io/badge/Process-Triple_Diamond-8B5CF6)](docs/process.md)
[![Product and Service Design](https://img.shields.io/badge/Product_%26_Service-Design-2563EB)](docs/guide/README.md)
[![Human in the loop](https://img.shields.io/badge/Human-in_the_loop-16A34A)](docs/guide/Working-with-the-agent.md)
[![UX Research](https://img.shields.io/badge/UX-Research-8B5CF6)](.agents/skills/diamond-captain/references/uxr.md)
[![Docs: Read the guide](https://img.shields.io/badge/Docs-Read_the_guide-2563EB)](docs/guide/README.md)
[![GitHub release asset downloads](https://img.shields.io/github/downloads/rebosidium/diamond-captain/total?label=Downloads)](https://github.com/rebosidium/diamond-captain/releases)

</div>

Diamond Captain is an open-source skill that guides your AI agent through product and service design — from problem discovery to solution delivery and outcome review. You choose the direction and keep control of decisions.

Start at any phase, skip ahead or loop back. The agent keeps a checkpoint and distinguishes evidence from assumptions. It works with UI and non-UI tasks, using the tools and evidence you actually have.

## Start with your agent

Use this with a local agent such as Claude Code, Codex or **Gemini CLI**. Installation defaults to all your projects on this computer:

```text
Install Diamond Captain for all my projects:
https://github.com/rebosidium/diamond-captain/blob/main/INSTALL-FOR-AGENTS.md
```

Then describe your task. [Install for agents](INSTALL-FOR-AGENTS.md) · [Manual installation](START-HERE.md) · [User guide](docs/guide/README.md)

Already using the previous skill name? Follow the [migration guide](docs/migration.md) before adding another installation. Existing installations and project state are not automatically migrated.

## How you work together

You set the goal, scope and decision authority; the agent investigates, compares options and creates usable artifacts. At a handoff, you accept, revise or reopen the result separately from choosing the next phase. [Working with the agent](docs/guide/Working-with-the-agent.md).

[Resume a task](docs/guide/Task-continuity.md#resume-in-a-new-chat) — continue in a new chat from the saved checkpoint.

## Install

Package badges link to published distributions; route badges link to setup guidance. Perplexity client verification is pending.

Choose one active installation to avoid duplicate skill entries. Download the ZIP and matching checksums from the selected release. If you already use the previous skill name, follow the [migration guide](docs/migration.md) before adding a new copy; existing installations and user-profile settings are not automatically upgraded. The default is a personal installation for all your local projects in the selected agent; choose project-only setup explicitly. Existing copies still need update or migration authority.

| Host | Package and instructions | Invocation |
| --- | --- | --- |
| Codex / compatible OpenAI plugin tooling | [OpenAI 0.3.2](https://github.com/rebosidium/diamond-captain/releases/tag/openai-v0.3.2) · [Guide](distributions/openai/README.md) | `diamond-captain:diamond-captain`, or `$diamond-captain` for a native skill |
| Claude Code | [Claude Code 0.3.2](https://github.com/rebosidium/diamond-captain/releases/tag/claude-code-v0.3.2) · [Guide](distributions/claude-code/README.md) | `/diamond-captain` for a native skill, or `/diamond-captain:diamond-captain` for the plugin |
| OpenCode | [OpenCode 0.3.2](https://github.com/rebosidium/diamond-captain/releases/tag/opencode-v0.3.2) · [Guide](distributions/opencode/README.md) | Ask the agent to use `diamond-captain` |
| Gemini CLI (terminal) | Install the complete native skill for your user account (all local projects). [Setup guide](docs/host-installation-routes.md) | Request `diamond-captain`; verify with `/skills list` |
| Web-Gemini (browser) | Add this repository through **+ → Import code → GitHub**, where available. [Google's import guide](https://support.google.com/gemini/answer/14903178?hl=en) | Ask Gemini to use Diamond Captain for your task. This provides chat context; it does not install a CLI skill. |
| Cursor, Grok Build, Perplexity Computer | [Host installation routes](docs/host-installation-routes.md) | Use the host's supported native/plugin/import route and verify discovery |
| Manual | [Core 0.5.0](https://github.com/rebosidium/diamond-captain/releases/tag/v0.5.0) or the [complete core folder at v0.5.0](https://github.com/rebosidium/diamond-captain/tree/v0.5.0/.agents/skills/diamond-captain) | Follow the selected host's skill mechanism |

The packages contain the complete pinned core, including references and templates. Downloadable archives do not imply a marketplace listing or that every host/import surface has been runtime-tested.

Core 0.5.0 and host packages 0.3.2 include the optional method library and startup and human framing fixes; see the [changelog](CHANGELOG.md#050). Previous releases remain unchanged. Published downloads retain their pinned core; later development edits do not update an installed release. See [development previews](distributions/perplexity/README.md#development-core-preview) for testing a committed source snapshot separately.

## Three diamonds, six thinking modes

Each diamond broadens the question **↗**, then focuses the decision **↘**. Start where useful, skip ahead or loop back as evidence changes; these are thinking modes, not mandatory timeboxes.

| Phase | Diamond | Work toward |
| --- | --- | --- |
| <img src="assets/icons/discover.svg" width="20" height="20" alt=""> **1 · Discover ↗** | Problem | Understand needs, context and alternative causes. |
| <img src="assets/icons/define.svg" width="20" height="20" alt=""> **2 · Define ↘** | Problem | Agree on the problem, scope and expected change. |
| <img src="assets/icons/develop.svg" width="20" height="20" alt=""> **3 · Develop ↗** | Solution | Compare different ways to help, including non-UI changes. |
| <img src="assets/icons/deliver.svg" width="20" height="20" alt=""> **4 · Deliver ↘** | Solution | Select, validate and realize a usable solution. |
| <img src="assets/icons/deploy.svg" width="20" height="20" alt=""> **5 · Deploy ↗** | Outcome | Observe real use, feedback and unexpected effects. |
| <img src="assets/icons/digest.svg" width="20" height="20" alt=""> **6 · Digest ↘** | Outcome | Assess evidence and decide what to keep, improve or revisit. |

Prepared work, a released change and a verified live outcome are distinct results. No specific model, design app or integration is required. [Read the full process](docs/process.md).

## Learn and verify

- [User guide](docs/guide/README.md), [skill guide](.agents/skills/diamond-captain/README.md), [full process](docs/process.md).
- [UXR methods and handoff](.agents/skills/diamond-captain/references/uxr.md), [office tools and MCP routes](.agents/skills/diamond-captain/references/office-tools.md) — optional references for the task at hand.
- [Compatibility and checks](docs/validation.md), [security](docs/security.md), [release and rollback](docs/releases.md).
- [Changelog](CHANGELOG.md), [migration from the previous skill name](docs/migration.md), [contributing](CONTRIBUTING.md).

## Security

See [security controls and assessment limits](docs/security.md) or [report a vulnerability privately](.github/SECURITY.md). Internal development records and execution logs are excluded.

## License

[MIT](LICENSE) © 2026 rebosidium. The original triple-diamond mark is included. Stage icons are from [Tabler Icons](assets/icons/README.md), with their [MIT notice](assets/icons/LICENSE). Linked third-party materials retain their licenses.

Platform marks belong to their providers: [OpenAI](https://openai.com/brand/) and [Grok](https://x.ai/legal/brand-guidelines).
