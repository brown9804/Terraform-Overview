# First plan without a cloud

**Level:** Beginner

## Overview and purpose

Use Terraform's built-in terraform_data resource to understand input, plan, state, apply, and destroy without any cloud provider.

## Prerequisites and dependencies

Terraform 1.7 or later; no cloud account or credentials. Start in this directory.

## Inputs and outputs

project_name defaults to learning and validates lowercase naming. The output is known after apply because it reads the resource's output, not merely its input.

## Source and usage

[Read main.tf](https://github.com/brown9804/Terraform-Overview/blob/main/examples/01-first-plan/main.tf) and
[the focused tests](https://github.com/brown9804/Terraform-Overview/blob/main/examples/01-first-plan/tests/main.tftest.hcl).
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
terraform plan
terraform apply
terraform output
terraform destroy
```

Inspect every plan before apply. A saved plan is sensitive and can contain
values from configuration/state; do not commit or publish it.

## Expected results and verification

Plan shows one terraform_data resource. Apply records the value in local state; destroy removes the state-managed record, not cloud infrastructure.

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

No cloud charges or Azure resources. State files are still local files to protect; use this exercise only with non-sensitive values.

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
