# Terraform and Infrastructure as Code

## Desired state and repeatability

Infrastructure as Code stores infrastructure intent in reviewable text.
Version control gives you a history and review process; Terraform plans
changes by comparing configuration, its state mapping, and provider-read
information from real systems.

Declarative does not mean every change is harmless or reversible.
Provider behavior, external modifications, permissions, and resource lifecycle
rules matter. Use configuration review and a plan, not just a successful command.

## Terraform's building blocks

- **Configuration:** HCL files describing resources, inputs, and relationships.
- **Provider:** a plugin implementing an API/resource model, such as AzureRM.
- **Resource:** a managed object with an address in Terraform state.
- **Data source:** reads existing information; it does not adopt ownership.
- **Module:** a directory of Terraform configuration with an input/output interface.
- **State:** the mapping and recorded attributes Terraform uses to track objects.
- **Plan:** proposed operations for a particular state/configuration context.

All `.tf` files in a directory are combined into one module. A filename such
as `variables.tf` is a convention, not a separate execution phase.

## Terraform, ARM, and Bicep

| Aspect | Terraform | Bicep/ARM |
| --- | --- | --- |
| Authoring | HCL and provider schemas | Bicep DSL or ARM JSON |
| Execution | Terraform graph and provider operations | ARM deployment engine |
| Scope | Multiple providers | Azure management plane |
| State | Explicit Terraform state/backend | Azure resource/deployment state |
| Reuse | Modules and registries | Modules, registries, templates |

AzureRM uses Azure management APIs, but Terraform does not normally turn
your configuration into one ARM template. AzAPI is a separate provider for
ARM resource/API coverage. Choose the tool based on your team's operating
model and lifecycle needs, not a blanket claim that one is always better.

## What this overview is for

Learn the workflow and reasoning here; browse service examples in the
[Azure template library](azure-templates.md).
Use [Bicep for Everyone](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/)
for the complementary Azure-native approach.

**Exercise:** explain why reading a VNet with a data source does not make
Terraform responsible for deleting it. Ownership requires a resource/state mapping.
