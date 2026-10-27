# Move to Diamond Captain

The previous native skill name was `design-process-dr`. Diamond Captain uses `diamond-captain`; plugin invocations and installed directory names change accordingly.

Preserve the project's `.product-task/`, artifacts, decisions and routing files. Back up the previous complete installation outside skill-discovery roots, install the complete new package, and update project routing/invocation references. Avoid keeping both old and new skill folders active in the same discovery scope.

Core 0.3.0 refreshes the name, source links and package identity. It does not introduce a new design methodology or reset project state. Host plugin packages have their own versions and pin the new core hash.

Verify the active path/version in a fresh host session; an already running conversation can retain previously loaded instructions. To roll back, restore the saved complete installation and its invocation/routing names while retaining current project state. See [releases](releases.md).
