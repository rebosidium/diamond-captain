# 9. Experiments and feature rollout

Choose when exposure control or a valid comparison can resolve an outcome question. Feature flags alone do not establish causality; define assignment, exposure, metric, guardrails and stopping rules before launch.

| Candidate | When to consider it | Route to check |
| --- | --- | --- |
| [Statsig](https://www.statsig.com/) | Experiment analysis paired with feature rollout | B / A? |
| [GrowthBook](https://www.growthbook.io/) | Warehouse-oriented experiments and feature flags | B / A? |
| [Optimizely](https://www.optimizely.com/) | Existing web or feature experimentation program | B |
| [LaunchDarkly](https://launchdarkly.com/) | Controlled feature exposure and rollback management | B / A? |
| [Flagsmith](https://www.flagsmith.com/) | Feature flags with deployment flexibility | B / A? |
| [Unleash](https://www.getunleash.io/) | Gradual rollout and self-hosted feature management | B / A? |
| [Wingify — VWO / AB Tasty](https://wingify.com/) | Web experimentation in the combined vendor ecosystem | B |
| [Datadog Experiments — formerly Eppo](https://www.geteppo.com/) | Experiment analysis in an existing data/observability stack | B |
| [Firebase Remote Config](https://firebase.google.com/products/remote-config) | Configure mobile/app behavior and controlled exposure | B / A? |
| [PostHog](https://posthog.com/) | Experiments and flags alongside existing product measurement | B / A? |

Use the [shared routing, capability limits and permissions](../tool-options.md#read-only-what-the-next-decision-needs) before acting.
