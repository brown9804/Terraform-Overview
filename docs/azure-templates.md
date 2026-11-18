# Companion Azure Terraform template library

**[Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)**
is the companion repository for service-organized Azure deployment examples.

[Open its documentation website](https://cloud2br-msftlearninghub.github.io/AzureTerraformTemplates-v0.0.0/){ .md-button .md-button--primary }
[Browse the source templates](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0){ .md-button }

## How the repositories fit together

| Terraform Overview | AzureTerraformTemplates |
| --- | --- |
| Learn concepts and workflows progressively | Explore Azure resource/service-specific samples |
| Begin with no-cloud exercises | Adapt actual Azure deployment configurations |
| Practice state, modules, mocks, review, cleanup | Review each service's dependencies, provider versions, and costs |
| Original small teaching modules | Broader independently maintained sample collection |

The `v0.0.0` repository name is not a Terraform CLI or AzureRM provider version.
Inspect its `required_version`, provider constraints, and lock files.
Do not assume every sample has been migrated to the AzureRM version used here.

## Browse by service

| Area | Companion source category |
| --- | --- |
| Resource groups, VNet, subnets, NSGs, public IP | [Core infrastructure](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/0_core-infrastructure) |
| Storage and data services | [Storage and databases](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/1_storage-databases) |
| VMs, App Service, Functions, containers, AKS | [Compute and containers](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/2_compute-containers) |
| Load balancing, gateways, VPN, firewall | [Networking](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/3_networking) |
| Identity, Key Vault, and policy | [Identity and security](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/4_identity-security) |
| Data Factory, Databricks, Event Hubs, analytics | [Analytics and big data](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/5_analytics-bigdata) |
| Logging, monitoring, automation | [Monitoring and management](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/6_monitoring-management) |
| Connected devices | [IoT](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/7_iot) |
| AI and machine learning | [AI/ML](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/8_ai-ml) |
| Migration and backup | [Migration/backup](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/9_migration-backup) |
| Media delivery and processing | [Media services](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0/tree/main/10_media-services) |

## Adapt a template safely

1. Select the smallest relevant service folder and read all of its files.
2. Record the source commit, license, Terraform/provider versions, and dependencies.
3. Check credentials, sensitive inputs, public endpoints, SKUs, API behavior,
   resource naming, region support, and destructive lifecycle behavior.
4. Decide whether to run it as an isolated root or refactor it into an approved
   module. Do not concatenate multiple roots/provider/backend blocks blindly.
5. Assign each resource to one state owner. Resolve duplicate groups/networks
   deliberately; a data source is a reference, not an import.
6. Run format/init/validate and inspect tests before running them.
7. Review an authenticated plan with your own isolated state and identity.
8. Apply only with approval, verify runtime behavior, and test cleanup.

## Boundaries

This overview links to the library; it does not duplicate its Terraform files,
change its license, validate all of its templates, or certify their deployment.
The companion repository and its templates retain their own license.
Use its current [safety guide](https://cloud2br-msftlearninghub.github.io/AzureTerraformTemplates-v0.0.0/use-templates-safely/)
as well as each template README.
