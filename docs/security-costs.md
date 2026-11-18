# Security and cost review

## Before deployment

- Confirm tenant, subscription, region, state owner, and resource ownership.
- Use least-privilege identity; prefer federation to stored automation secrets.
- Review public access, inbound rules, encryption, diagnostic data, and data roles.
- Estimate costs with the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/).
- Set budget alerts, tagging, and a time-bounded cleanup owner.

The no-cloud examples do not create Azure resources. The Azure foundation
does create resources if you run its live apply commands. Storage capacity,
transactions, and future private endpoints/network traffic can incur charges.
Budget alerts are notifications, not a universal spending cap.

## Sensitive values

`sensitive = true` redacts ordinary display; it does not automatically remove
the value from state or saved plans. Use supported ephemeral/write-only
features only after reviewing their exact provider and version support.
Never commit credentials, private state, secret variable files, or plans.
Ignored files still need filesystem access controls and secure disposal.

## Secure foundations have dependencies

The storage module disables public networking, shared keys, and public
containers. These are configuration defaults, not a complete private access
solution. Clients still need private endpoints, DNS resolution, route access,
and appropriate Entra data roles. Management-plane permission does not imply
data-plane permission.

The network module associates an NSG that denies inbound traffic with every
subnet. It is not a firewall appliance or a complete egress policy.
Review explicit workload allow rules before introducing applications.

## Supply chain

Review providers/modules, pin root versions, commit lock files, verify
checksums, and review updates. A downloaded provider is executable code.
Do not expose secrets to untrusted pull-request workflows or replace
checksum errors with insecure plugin overrides.

## Cleanup is a verification step

Review a destroy plan using the original state. Account for locks, backups,
soft-delete, retention, shared resources, and failed deletes. Check Azure
after cleanup and review cost reporting later. Never promise zero cost based
only on a successful Terraform command.
