# Reusable Azure resource group

**Level:** Intermediate

## Overview and purpose

Define a provider-independent child-module interface for an Azure resource group, with caller-owned provider authentication and tags.

## Prerequisites and dependencies

Offline validation/tests require Terraform and downloaded AzureRM 5.x. A live deployment requires the Azure foundation root and scoped Azure permissions.

## Inputs and outputs

name, location, and optional tags are the module contract. Outputs return name, normalized location, and ID, not credentials.

## Source and usage

[Read main.tf](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-resource-group/main.tf) and
[the focused tests](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-resource-group/tests/main.tftest.hcl).
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
terraform init -backend=false
terraform validate
terraform test
```

Inspect every plan before apply. A saved plan is sensitive and can contain
values from configuration/state; do not commit or publish it.

## Expected results and verification

The mocked plan preserves the requested resource group metadata. No group is created by the tests.

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

A resource group has no direct charge, but its contents may. Do not mix unmanaged resources into a group that Terraform may destroy.

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
