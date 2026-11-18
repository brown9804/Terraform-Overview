# Reusable private storage foundation

**Level:** Intermediate

## Overview and purpose

Create a TLS-only StorageV2 account with public networking, shared keys, and public containers disabled.

## Prerequisites and dependencies

Offline tests mock AzureRM. Live use requires a globally unique storage name and a real Azure root/provider configuration.

## Inputs and outputs

name validates Azure lowercase alphanumeric length. location and resource_group_name are supplied by the caller.

## Source and usage

[Read main.tf](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-storage/main.tf) and
[the focused tests](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-storage/tests/main.tftest.hcl).
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

The mocked plan verifies security defaults. A real account needs private endpoints, private DNS, and data roles before clients can access its data.

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

Storage capacity, operations, private endpoints, and traffic can be charged. No containers, endpoint, DNS, or role grants are created here. Provider state can contain sensitive resource metadata; protect it.

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
