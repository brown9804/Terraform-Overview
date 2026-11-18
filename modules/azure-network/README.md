# Reusable private network foundation

**Level:** Intermediate

## Overview and purpose

Build a VNet, named subnets, deny-all-inbound NSG, and an explicit NSG association for every subnet.

## Prerequisites and dependencies

Offline tests mock AzureRM. Live use requires an existing group, approved address ranges, region availability, and the Azure foundation root.

## Inputs and outputs

subnets maps stable names to CIDRs. CIDR syntax is validated, but overlap/containment still need design review and Azure validation.

## Source and usage

[Read main.tf](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-network/main.tf) and
[the focused tests](https://github.com/brown9804/Terraform-Overview/blob/main/modules/azure-network/tests/main.tftest.hcl).
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

The plan contains the VNet, NSG, requested subnets, and one association per subnet. All inbound traffic is denied by default, including traffic from the same VNet.

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

VNet/NSG objects have no direct compute charges, but workloads and networking services can. This module does not configure outbound NAT, gateways, DNS, or approved workload allow rules.

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
