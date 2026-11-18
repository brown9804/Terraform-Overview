# Modular Azure environment

**Level:** Advanced

## Overview and purpose

Compose the three Azure modules into a dedicated environment resource group, VNet/subnet security foundation, and private storage account.

## Prerequisites and dependencies

For offline tests: Terraform and AzureRM only. For live use: Azure CLI login, ARM_SUBSCRIPTION_ID, permissions, policy/quota review, and your own globally unique storage name.

## Inputs and outputs

prefix/environment derive names. location is a changeable sample region. storage_account_name is required. Separate environments need separate state, not just a changed variable.

## Source and usage

[Read main.tf](https://github.com/brown9804/Terraform-Overview/blob/main/examples/03-azure-foundation/main.tf) and
[the focused tests](https://github.com/brown9804/Terraform-Overview/blob/main/examples/03-azure-foundation/tests/main.tftest.hcl).
Use this directory as the working directory for the commands below.
Azure modules are child modules: use `examples/03-azure-foundation` as the
live deployment entry point rather than applying a module without its caller.

## Validation and optional execution

The commands use Bash syntax (Azure Cloud Shell supports it). Plan-only
tests never create Azure resources; Azure tests use `mock_provider`.
`init` may download provider plugins from the Terraform Registry.
For Azure live commands, authenticate, select the intended subscription,
and set `ARM_SUBSCRIPTION_ID` and your own `STORAGE_ACCOUNT_NAME` first.
No live Azure apply/destroy is part of CI.

```bash
terraform init
terraform validate
terraform test
terraform plan -var="storage_account_name=$STORAGE_ACCOUNT_NAME" -out=lab.tfplan
terraform apply lab.tfplan
terraform output
terraform plan -destroy -var="storage_account_name=$STORAGE_ACCOUNT_NAME" -out=destroy.tfplan
terraform apply destroy.tfplan
```

Inspect every plan before apply. A saved plan is sensitive and can contain
values from configuration/state; do not commit or publish it.

## Expected results and verification

Live apply would create one group, VNet, workload subnet, NSG/association, and storage account. Tests use mocks and do not establish deployment success or data connectivity.

Read `terraform output` and the plan's resource addresses. A mocked assertion
only checks configuration behavior, not provider APIs, credentials, cost,
regional availability, or application runtime behavior.

## Cleanup

For local data examples, `terraform destroy` removes the exercise's managed
records. For Azure, use the root configuration's reviewed destroy plan with the
same state, credentials, and input values. Confirm the resources are gone.
Do not delete the state file as a substitute for destroying resources.

After confirming destruction, delete ignored local `.terraform/`, plan, and
state files if you no longer need them. Keep committed provider lock files.
Shared or retained resources may need separate approved cleanup.

## Cost, security, and limitations

Live commands can create paid resources. Review plans before applying, including destroy. No application, private endpoint/DNS, or data-plane RBAC is included. Do not manually delete state to clean up cloud resources.

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
