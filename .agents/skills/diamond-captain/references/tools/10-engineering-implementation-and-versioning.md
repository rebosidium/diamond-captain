# 10. Engineering implementation and versioning

Choose when an artifact must become a traceable change. Repository access, write scope and release authority are separate decisions.

| Candidate | When to consider it | Route to check |
| --- | --- | --- |
| [GitHub](https://github.com/) | Existing source, pull requests and review history | B / A? / F |
| [GitLab](https://about.gitlab.com/) | Existing repository and integrated delivery pipeline | B / A? / F |
| [Bitbucket](https://bitbucket.org/product/) | Source already connected to an Atlassian workflow | B / A? / F |
| [Git](https://git-scm.com/) | Local version history and reviewable patches | L / F |
| [Gitea](https://about.gitea.com/) | Self-hosted Git collaboration and code review | B / F |
| [Forgejo](https://forgejo.org/) | Self-hosted software forge for existing team workflows | B / F |
| [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/) | Git repositories in an Azure DevOps environment | B / F |
| [GitHub Actions](https://github.com/features/actions) | Automated validation beside the source repository | B / F |
| [Jenkins](https://www.jenkins.io/) | Established team build and delivery automation | B / F |
| [CircleCI](https://circleci.com/) | Existing continuous-integration validation pipeline | B / F |

Use the [shared routing, capability limits and permissions](../tool-options.md#read-only-what-the-next-decision-needs) before acting.
