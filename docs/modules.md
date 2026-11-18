# Reusable modules

## Design a small contract

A module is a directory, not a separate provider. Inputs define caller choices;
outputs expose only what downstream code needs. Keep authentication in the
root. Avoid a large collection of loosely related flags that hides important
security behavior.

This repository includes three original Azure child modules:

| Module | Contract | Deliberate limit |
| --- | --- | --- |
| Resource group | Name, location, tags | No subscription or role creation |
| Network | Name, group, region, address space, subnet map | No workload allow rules, NAT, VPN, or DNS |
| Storage | Name, group, region | No containers, endpoint, DNS, or data roles |

Use the [catalog](catalog.md) for the full source and module README pages.

## Actual composition

The Azure foundation root calls the modules with local paths:

```hcl title="examples/03-azure-foundation/main.tf"
--8<-- "examples/03-azure-foundation/main.tf"
```

The group outputs feed the network and storage inputs. This is both a
documented interface and a dependency relationship.
The root selects the provider version and configures the provider once.

## Module scope and ownership

Decide which state owns each resource. Do not have a companion service
template and this foundation manage the same VNet or storage account
without an explicit state/import/migration plan.
Do not duplicate a resource merely to expose it through another module.

For external modules, pin versioned releases and review their source, tests,
license, and change history. Consider
[Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/)
for supported production building blocks; an overview exercise does not
provide equivalent support guarantees.

## Module tests

Tests here plan with mocked AzureRM. The storage test verifies that public
networking, shared keys, and public containers remain disabled.
The network test checks an NSG association for every requested subnet.
Those are meaningful configuration contracts, not evidence that an Azure
client can reach or use a deployed account.

**Exercise:** add a non-sensitive ownership tag input to a module, propagate it
from the root, and add an assertion that would fail if propagation were removed.
