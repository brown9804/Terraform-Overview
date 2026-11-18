# Terraform Overview

Atlanta, USA

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)
[![Validation and Pages](https://github.com/brown9804/Terraform-Overview/actions/workflows/validate-and-deploy.yml/badge.svg)](https://github.com/brown9804/Terraform-Overview/actions/workflows/validate-and-deploy.yml)

Last updated: 2026-11-18

A practical introduction to Terraform and Infrastructure as Code: learn the
language, providers, state, reusable modules, testing, and safe deployment
workflows before adapting real Azure infrastructure.

[Read the website](https://brown9804.github.io/Terraform-Overview/) |
[Start learning](docs/getting-started.md) |
[Learning paths](docs/learning-paths.md) |
[Azure template library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)

<details>
<summary><b>Table of contents</b></summary>

- [Start here](#start-here)
- [Companion Azure templates](#companion-azure-templates)
- [Repository structure](#repository-structure)
- [Run an example](#run-an-example)
- [Validation and website](#validation-and-website)
- [Safety and community](#safety-and-community)

</details>

## Start here

| Topic | Lesson |
| --- | --- |
| IaC, Terraform, ARM, Bicep, and state | [Fundamentals](docs/fundamentals.md) |
| Installation and first local workflow | [Getting started](docs/getting-started.md) |
| Inputs, locals, functions, loops, outputs | [Language](docs/language.md) |
| Providers, lock files, dependencies | [Provider management](docs/providers.md) |
| State, locking, backends, environments | [State and backends](docs/state-backends.md) |
| Reusable module interfaces | [Modules](docs/modules.md) |
| Init, plan, approval, apply, destroy | [Workflow](docs/workflow.md) |
| Mocked tests and safe automation | [Testing and CI](docs/testing.md) |
| Complete Azure learning foundation | [Project](docs/azure-project.md) |
| Reference and errors | [Cheat sheet](docs/cheat-sheet.md), [troubleshooting](docs/troubleshooting.md) |

## Companion Azure templates

**[AzureTerraformTemplates-v0.0.0](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)**
is the companion **Azure service template library**. Use this overview to
understand Terraform, then explore that repository's resource-group,
networking, compute, storage/database, security, monitoring, analytics,
AI, and other service examples.

[Browse its website](https://cloud2br-msftlearninghub.github.io/AzureTerraformTemplates-v0.0.0/) |
[Choose a template safely](docs/azure-templates.md)

The repositories have separate owners, licenses, provider constraints, and
validation histories. This overview does not copy, certify, or automatically
deploy the companion templates. Review each template's code, dependencies,
provider versions, costs, and security settings before using it.

## Repository structure

```text
docs/                         Markdown lessons and shared Material styling
examples/01-first-plan/        Built-in resource: no cloud account needed
examples/02-expressions/       Stable keys, loops, validation, conditional values
examples/03-azure-foundation/   Composed Azure resource group, network, and storage
modules/azure-resource-group/  Reusable child module
modules/azure-network/         VNet, subnets, deny-inbound NSG and associations
modules/azure-storage/         Private-only storage without shared key access
.github/                      Plan-only tests, validation, Pages, community forms
```

Each configuration includes a README and focused `.tftest.hcl` tests.
Website source views include the actual repository files at build time.
Do not maintain pasted source copies in lessons.

## Run an example

Install [Terraform](https://developer.hashicorp.com/terraform/install), clone or
download the repository, and run from its root:

```shell
terraform -chdir=examples/01-first-plan init
terraform -chdir=examples/01-first-plan validate
terraform -chdir=examples/01-first-plan test
terraform -chdir=examples/01-first-plan plan
```

Expected: one built-in `terraform_data` record, no Azure resource, and no
cloud credentials. Follow [getting started](docs/getting-started.md) to
practice apply, inspect local state, and destroy safely.

Azure learning configurations use AzureRM 5.x; the project pins 5.14.0.
CI uses Terraform 1.17.2. Provider lock files record selected versions/checksums.
Review lock-file changes when upgrading dependencies.

## Validation and website

The MkDocs Material website follows the same full-width navy visual format as
[LaTeX for Everyone](https://brown9804.github.io/LaTeX-For-Everyone/) and
[Bicep for Everyone](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/):
responsive navigation, light/dark themes, search, breadcrumbs, copy-code,
Mermaid diagrams, and the organization logo/favicon.

GitHub Actions formats/checks Terraform, initializes without remote backends,
validates every configuration, and runs **plan-only tests with mocked Azure
providers**. It checks synchronized documentation, builds MkDocs in strict
mode, checks local links, and deploys Pages only from validated `main`.
No Azure login, real Azure plan, apply, or destroy is part of CI.

See [maintenance](docs/maintaining.md) for reproduction commands and
[testing](docs/testing.md) for what mocks do and do not prove.

## Safety and community

State and saved plans can contain sensitive data even when outputs are marked
`sensitive`. Never commit them, credentials, private keys, live subscription IDs,
or real environment parameters. Review all live plans and destruction.
No live Azure deployment is claimed by this repository's offline validation.

Read [CONTRIBUTING](CONTRIBUTING.md), [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md),
[CHANGELOG](CHANGELOG.md), and [CITATION](CITATION.cff).
The repository's existing [GPL-3.0 license](LICENSE) is preserved. Terraform,
providers, companion templates, and external documentation retain their own licenses.
