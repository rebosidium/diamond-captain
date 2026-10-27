# Perplexity Computer compatibility

The [import candidate](../distributions/perplexity/README.md) reuses the published Diamond Captain Claude Code **0.2.0** archive and complete canonical core **0.3.0**, unchanged. The Perplexity wrapper contains metadata/instructions, not a second skill implementation.

| Scope | Result and limit |
| --- | --- |
| Diamond Captain offline preparation | The published ZIP and checksums are verified; preflight compares every core file with the local release tag and preserves archive bytes. This establishes package integrity only. |
| Diamond Captain client import and execution | Not yet tested. Supporting-file preservation, explicit activation, task execution and fresh-session recovery require a new real-client test for this identity and exact source hash. |
| Historical tests before the rename | A prior package installed as one skill and retained its complete supporting files. A bounded Define task and manual state transfer worked, but state initialization was late and the recovered diamond label was wrong. These are historical results, not validation of Diamond Captain. |
| Shared corrections carried forward | Early full-skill loading, an optional intake-only initializer and an explicit phase-to-diamond mapping are part of the unreleased canonical changes. Earlier private previews exercised those corrections; changed names, links and package bytes require fresh client validation. |
| Remaining behavioral limits | Mandatory host planning may precede initialization and must be recorded honestly. Later model-written journal edits can still overstate checks; the initializer protects the first write only. An additional recovery run on the final earlier preview was not started because the client offered Pro access. |
| Unverified surfaces | Native-app management, automatic activation, automatic filesystem transfer between sessions, updates/rollback and the complete six-phase process remain unverified. |

Use explicit skill selection for a bounded client test. Preserve unknowns, pending acceptance and the actual sequence of tool actions. A generated artifact or enabled plugin does not establish acceptance, process compliance or durable task memory. Manual text transfer in historical testing did not independently establish byte identity to the original cloud files.

Internal execution records and failed trials remain private. No raw logs, prompts, responses, populated task states or runtime identifiers belong in the product or import ZIP. New previews remain pinned to a committed source/hash during each comparison.

Official references: [skill import](https://www.perplexity.ai/help-center/en/articles/13914413-how-to-use-computer-skills), [plugin upload](https://www.perplexity.ai/help-center/en/articles/2026100802-create-or-upload-a-custom-plugin), [plugins](https://www.perplexity.ai/help-center/en/articles/2026100701-what-are-plugins). See the broader [verification scope](validation.md).
