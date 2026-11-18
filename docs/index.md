# Terraform Overview

[brown9804](https://github.com/brown9804) | Atlanta, USA

<div class="learning-intro" markdown>

**Understand infrastructure automation before creating infrastructure.**

Start without a cloud account, learn Terraform's workflow and state model,
then compose Azure modules and review real deployment plans deliberately.

[Start learning](getting-started.md){ .md-button .md-button--primary }
[Explore Azure templates](azure-templates.md){ .md-button }

</div>

## Find your next step

| Your goal | Start with | Build toward |
| --- | --- | --- |
| Understand IaC | [Fundamentals](fundamentals.md) | [First local plan](getting-started.md) |
| Learn the language | [Expressions and types](language.md) | [Reusable modules](modules.md) |
| Work as a team | [State and backends](state-backends.md) | [Safe workflows](workflow.md) |
| Test without Azure charges | [Testing and CI](testing.md) | [Example catalog](catalog.md) |
| Build Azure infrastructure | [Azure foundation](azure-project.md) | [Companion template library](azure-templates.md) |
| Resolve a failure | [Troubleshooting](troubleshooting.md) | [Official resources](resources.md) |

## Overview versus template library

This repository teaches Terraform concepts and operating practices through
focused, original examples.
**[AzureTerraformTemplates-v0.0.0](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)**
provides a broader service-organized Azure template collection.
Use the [template selection guide](azure-templates.md) before adapting it.
Neither repository is a certification that an example fits production.

## How to learn here

Read a lesson, inspect the canonical source, run the focused plan-only tests,
and compare the expected result. The first two labs need no cloud provider.
Azure exercises require an explicit choice to authenticate and deploy.

## What automation verifies

CI checks format, initialization, validation, plan-only behavior with mocked
Azure providers, documentation synchronization, links, and the website build.
It does not prove live API compatibility, permissions, quotas, connectivity,
application behavior, security accreditation, or a zero-cost deployment.

Use the [learning paths](learning-paths.md) and
[community guide](contributing.md) to continue.
