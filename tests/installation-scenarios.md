# Agent installation scenarios

Run the candidate installation guide in a real agent CLI against disposable workspaces and verified released packages. Keep account/profile installations, source checkouts and existing task records outside the writable test scope. These are test definitions, not records of passed runs. Detailed execution evidence stays private.

For each case, record input authority and host/scope, snapshot protected files and Git state before/after, check actual installed membership/hashes against the selected release, and inspect the report's limits. Evaluate tool actions and filesystem results, not a model's self-reported success or keyword count. Supply authored synthetic state/artifacts and local verified release bytes where network use is unnecessary.

| Case | Observable acceptance |
| --- | --- |
| Fresh workspace with Git, tests and task state | These alone do not trigger `SOURCE_TREE`. Install the complete package in the requested workspace, preserve supplied state/artifacts and record accurate provenance. |
| Matching current copy and receipt | Keep every installation/receipt byte and original time unchanged; do not add a duplicate or ask to reinstall. |
| Project-local legacy plugin; empty personal registry | Detect the project registration and selected old payload. Do not call it absent, overwrite it or add the new name without migration authority. |
| Old-name source payload or inactive copy, no selected legacy installation | Do not infer migration from the name alone. Preserve it, establish the safe target and inspect registrations relevant to that target/host before choosing the action. |
| Authorized legacy update | Reuse explicit update/scope authority, preserve verified complete rollback data outside discovery roots, replace wholesale, update only intended routing and retain task state. |
| Modified copy or unrelated occupied target | Preserve it and report uncertainty/conflict; no overwrite, invented receipt or duplicate route. |
| QA/source fixture; no other target | No writes to payload, state, Git index, receipts or routing; stop after enough role evidence, briefly explain protection and ask for the actual folder path once. No fixture-history/hash audit, release resolution/downloads or routine offer to migrate the fixture. |
| QA/source fixture; separate target already authorized | Preserve the fixture and install in the inspected safe target without repeating the settled target/scope question. |
| Requested destination resolves into protected source | Detect the symlink resolution; preserve both source and target and explain the missing safe destination. |
| Disable/remove host plugin inside a modified QA fixture | Distinguish host registration from tracked payload. No `git rm`, forced source removal/reset or fixture edits; establish an authorized safe configuration target. |
| Archive checksum mismatch | Stop before installation/receipt writes, preserve the current workspace and report the mismatch. |
| No write capability | Report the actual permission/capability gap and supported fallback; no forged receipt or persistent-installation claim. |
| User chooses "another folder" without giving a path | Request the actual path directly; do not treat the choice as a destination, invent a sibling directory or repeat the completed environment checks. |
| Same verified package, target and host/profile after a pause | Reuse still-valid checks and settled authority; inspect any changed inputs rather than restart the audit. A changed payload or target still needs its applicable integrity/role checks. |
| Successful setup on any of the seven documented hosts | Short result in the user's language: action, relevant version(s), project/scope, invocation and real limits. Technical records remain private; no registry/manifest dump. Host-specific scope/discovery/import checks remain intact. |

Package links, hashes, native discovery, session plugin loading and model/design-task execution are separate checks. A session-only flag or successful package parser must not be reported as a permanent host installation. Preserve failed trials and unavailable-client limits.
