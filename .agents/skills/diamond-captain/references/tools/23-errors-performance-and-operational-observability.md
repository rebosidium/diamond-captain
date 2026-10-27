# 23. Errors, performance and operational observability

Choose when deployment must be observed or failures may explain user outcomes. Error rates and traces need correct instrumentation and user-impact context; they do not replace usability or value evidence.

| Candidate | When to consider it | Route to check |
| --- | --- | --- |
| [Sentry](https://github.com/getsentry/sentry) | Relate application errors/performance to affected flows | B / A? |
| [BugSnag](https://www.bugsnag.com/) | Existing mobile/web stability and error evidence | B |
| [Rollbar](https://rollbar.com/) | Investigate application error occurrence and context | B |
| [Datadog](https://www.datadoghq.com/) | Correlate real-user, service and infrastructure evidence | B / A? |
| [New Relic](https://docs.newrelic.com/) | Existing application performance and observability stack | B / A? |
| [Grafana](https://grafana.com/) | View related operational metrics, logs and traces | B / A? |
| [Elastic Observability](https://www.elastic.co/observability) | Investigate existing indexed logs and service telemetry | B |
| [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | Observe a change in an existing AWS environment | B / A? |
| [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) | Observe application behavior in an Azure environment | B / A? |
| [OpenTelemetry](https://opentelemetry.io/) | Plan or inspect standard telemetry instrumentation | L / F |

Use the [shared routing, capability limits and permissions](../tool-options.md#read-only-what-the-next-decision-needs) before acting.
