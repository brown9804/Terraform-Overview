# State, locking, backends, and environments

## What state records

State maps Terraform addresses to real object identities and stores attributes
needed for future operations. Treat it as sensitive operational data.
It is not a disposable cache, an audit log, or a mechanism for deleting Azure
resources by deleting a file.

Local state is appropriate for the no-cloud exercises. Team-managed Azure
infrastructure needs a protected remote backend with least-privilege access,
encryption, recovery/versioning, and locking.

## Azure Storage backend

A backend must exist before a configuration can initialize against it.
Bootstrap its storage, private networking, DNS, access roles, and recovery
policy separately; do not make a state store casually destroyable by the
same lab configuration whose state it holds.

The following is a **backend declaration fragment**, not a complete deployable
configuration:

```hcl
terraform {
  backend "azurerm" {}
}
```

Supply non-secret settings in an ignored `backend.local.hcl`:
storage-account name, container name, and a distinct state key.
Use approved Entra authentication (`use_azuread_auth = true`) and your chosen
interactive/OIDC/managed identity method. Do not put keys or tokens in
backend arguments or committed files.

```shell
terraform init -backend-config=backend.local.hcl
```

Backend configuration and credentials can be retained in working-directory
metadata or plans. Protect the entire working environment as well as state.
See the official [Azure backend reference](https://developer.hashicorp.com/terraform/language/backend/azurerm)
for the current fields and authentication requirements.

## Locking and concurrency

The Azure backend uses Azure Blob capabilities for state locking.
Do not disable locking to resolve contention. Determine whether another run
owns the lease; use force-unlock only after confirming the owning operation
is no longer active and following your team's recovery process.
Serialize applies for the same state and keep review/apply identities scoped.

## Environments

Changing `environment = "dev"` to `"prod"` in the same state is not safe
environment isolation: it may propose replacing the dev resources.
Use intentionally separate roots/backends/state keys and appropriately
separate subscriptions or groups and permissions.

CLI workspaces separate state instances within a backend but are not a
universal security or deployment boundary. Choose them only when their shared
configuration and credential model fits your design.

## Import, moves, and recovery

Use reviewed import blocks to adopt existing objects and moved blocks when
refactoring addresses. Import is not permission to manage every object in a
resource group. Back up state and inspect plans before and after refactoring.
Never upload real state into an issue to get troubleshooting help.
