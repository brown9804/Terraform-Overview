# Providers, versions, and dependencies

## Requirements versus configuration

`required_providers` declares provider source addresses and compatible versions.
A `provider` block configures a provider instance, including features and
authentication behavior. Reusable child modules declare requirements but
normally receive provider configurations from their root caller.

The Azure foundation root selects `hashicorp/azurerm` exactly at the version
reviewed with this example. Child modules accept a compatible 5.x range.
This keeps the executable root reproducible while allowing controlled module reuse.

## Lock files

`terraform init` selects plugins within the configured constraints and writes
`.terraform.lock.hcl`. Commit the lock file: it records selected versions and
checksums, not credentials. It does not lock remote module source versions;
pin registry modules or Git references separately.

```shell
terraform -chdir=examples/03-azure-foundation init -backend=false
terraform -chdir=examples/03-azure-foundation providers
```

For intentional upgrades, change constraints when necessary, run
`terraform init -upgrade`, review the lock-file diff and provider migration
guidance, and rerun tests and a live plan before apply.
An exact root constraint does not change just because `-upgrade` was supplied.

## Checksums across platforms

The committed lock file may need additional platform checksums for a team.
Use the official command, review changes, and commit only lock metadata:

```shell
terraform providers lock -platform=linux_amd64 -platform=windows_amd64 -platform=darwin_arm64
```

Run this in the relevant configuration directory. Never bypass checksum
verification merely to make initialization pass.

## Resource graph and module dependencies

References such as `resource_group_name = module.group.name` express
dependencies through values. Prefer those references over broad `depends_on`,
which can unnecessarily delay reads and make values unknown.
Use explicit dependencies only when a real hidden relationship is not captured
by the configuration's data flow.

## Azure authentication

Interactive learners can use Azure CLI with the intended subscription.
Automation should use approved workload identity federation/OIDC or managed
identity rather than committed client secrets. Provider authentication and
backend authentication are related but separately configured concerns.
Offline mocked tests authenticate to neither.

**Exercise:** identify which file controls the selected plugin version and
which block configures the Azure subscription context.
