"""Generate source-view pages and example READMEs without duplicating code."""
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPO = "https://github.com/brown9804/Terraform-Overview/blob/main"
EXAMPLES = [
    ("examples/01-first-plan", "First plan without a cloud", "Beginner",
     "Use Terraform's built-in terraform_data resource to understand input, plan, state, apply, and destroy without any cloud provider.",
     "Terraform 1.7 or later; no cloud account or credentials. Start in this directory.",
     "project_name defaults to learning and validates lowercase naming. The output is known after apply because it reads the resource's output, not merely its input.",
     "terraform init\nterraform validate\nterraform test\nterraform plan\nterraform apply\nterraform output\nterraform destroy",
     "Plan shows one terraform_data resource. Apply records the value in local state; destroy removes the state-managed record, not cloud infrastructure.",
     "No cloud charges or Azure resources. State files are still local files to protect; use this exercise only with non-sensitive values."),
    ("examples/02-expressions", "Expressions and stable keys", "Beginner",
     "Create one built-in data record per environment using typed collections, locals, for expressions, interpolation, and conditional retention.",
     "Terraform 1.7 or later; no cloud provider or account.",
     "environments is a set of dev/test/prod values. for_each uses stable environment keys. prefix changes record content without changing those keys.",
     "terraform init\nterraform validate\nterraform test\nterraform plan -var='environments=[\"dev\",\"prod\"]'\nterraform apply -var='environments=[\"dev\",\"prod\"]'\nterraform destroy -var='environments=[\"dev\",\"prod\"]'",
     "The plan contains two local data records keyed by dev and prod; prod retention is 90 and other environments use 30. These numbers are learning data, not a configured cloud retention policy.",
     "No cloud charges. Changing or removing a for_each key changes the corresponding Terraform address and can destroy a real resource in other configurations."),
    ("modules/azure-resource-group", "Reusable Azure resource group", "Intermediate",
     "Define a provider-independent child-module interface for an Azure resource group, with caller-owned provider authentication and tags.",
     "Offline validation/tests require Terraform and downloaded AzureRM 5.x. A live deployment requires the Azure foundation root and scoped Azure permissions.",
     "name, location, and optional tags are the module contract. Outputs return name, normalized location, and ID, not credentials.",
     "terraform init -backend=false\nterraform validate\nterraform test",
     "The mocked plan preserves the requested resource group metadata. No group is created by the tests.",
     "A resource group has no direct charge, but its contents may. Do not mix unmanaged resources into a group that Terraform may destroy."),
    ("modules/azure-network", "Reusable private network foundation", "Intermediate",
     "Build a VNet, named subnets, deny-all-inbound NSG, and an explicit NSG association for every subnet.",
     "Offline tests mock AzureRM. Live use requires an existing group, approved address ranges, region availability, and the Azure foundation root.",
     "subnets maps stable names to CIDRs. CIDR syntax is validated, but overlap/containment still need design review and Azure validation.",
     "terraform init -backend=false\nterraform validate\nterraform test",
     "The plan contains the VNet, NSG, requested subnets, and one association per subnet. All inbound traffic is denied by default, including traffic from the same VNet.",
     "VNet/NSG objects have no direct compute charges, but workloads and networking services can. This module does not configure outbound NAT, gateways, DNS, or approved workload allow rules."),
    ("modules/azure-storage", "Reusable private storage foundation", "Intermediate",
     "Create a TLS-only StorageV2 account with public networking, shared keys, and public containers disabled.",
     "Offline tests mock AzureRM. Live use requires a globally unique storage name and a real Azure root/provider configuration.",
     "name validates Azure lowercase alphanumeric length. location and resource_group_name are supplied by the caller.",
     "terraform init -backend=false\nterraform validate\nterraform test",
     "The mocked plan verifies security defaults. A real account needs private endpoints, private DNS, and data roles before clients can access its data.",
     "Storage capacity, operations, private endpoints, and traffic can be charged. No containers, endpoint, DNS, or role grants are created here. Provider state can contain sensitive resource metadata; protect it."),
    ("examples/03-azure-foundation", "Modular Azure environment", "Advanced",
     "Compose the three Azure modules into a dedicated environment resource group, VNet/subnet security foundation, and private storage account.",
     "For offline tests: Terraform and AzureRM only. For live use: Azure CLI login, ARM_SUBSCRIPTION_ID, permissions, policy/quota review, and your own globally unique storage name.",
     "prefix/environment derive names. location is a changeable sample region. storage_account_name is required. Separate environments need separate state, not just a changed variable.",
     "terraform init\nterraform validate\nterraform test\nterraform plan -var=\"storage_account_name=$STORAGE_ACCOUNT_NAME\" -out=lab.tfplan\nterraform apply lab.tfplan\nterraform output\nterraform plan -destroy -var=\"storage_account_name=$STORAGE_ACCOUNT_NAME\" -out=destroy.tfplan\nterraform apply destroy.tfplan",
     "Live apply would create one group, VNet, workload subnet, NSG/association, and storage account. Tests use mocks and do not establish deployment success or data connectivity.",
     "Live commands can create paid resources. Review plans before applying, including destroy. No application, private endpoint/DNS, or data-plane RBAC is included. Do not manually delete state to clean up cloud resources."),
]


def build_files():
    files = {}
    rows = ["# Learning example catalog\n\n",
            "Source views below include each canonical README and Terraform configuration at build time.\n\n",
            "| Example | Level | Location |\n| --- | --- | --- |\n"]
    for path, title, level, purpose, prerequisites, inputs, commands, expected, safety in EXAMPLES:
        if not (ROOT / path / "main.tf").is_file():
            raise ValueError(f"Missing canonical source: {path}")
        slug = path.replace("/", "--")
        rows.append(f"| [{title}](examples/{slug}.md) | {level} | `{path}` |\n")
        readme = f"""# {title}

**Level:** {level}

## Overview and purpose

{purpose}

## Prerequisites and dependencies

{prerequisites}

## Inputs and outputs

{inputs}

## Source and usage

[Read main.tf]({REPO}/{path}/main.tf) and
[the focused tests]({REPO}/{path}/tests/main.tftest.hcl).
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
{commands}
```

Inspect every plan before apply. A saved plan is sensitive and can contain
values from configuration/state; do not commit or publish it.

## Expected results and verification

{expected}

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

{safety}

These are educational examples, not certified production modules.
For additional Azure services, use the companion
[AzureTerraformTemplates library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0)
after reviewing its individual prerequisites, provider constraints, and security settings.
"""
        files[Path(path) / "README.md"] = readme
        files[Path("docs/examples") / (slug + ".md")] = (
            f'--8<-- "{path}/README.md"\n\n## Complete Terraform source\n\n'
            f'```hcl title="{path}/main.tf"\n--8<-- "{path}/main.tf"\n```\n'
        )
    files[Path("docs/catalog.md")] = "".join(rows)
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    sources = {
        path.parent.relative_to(ROOT).as_posix()
        for folder in ("examples", "modules")
        for path in (ROOT / folder).glob("*/main.tf")
    }
    if sources != {row[0] for row in EXAMPLES}:
        raise SystemExit("Every example/module must have exactly one catalog entry.")
    stale = []
    for relative, content in build_files().items():
        target = ROOT / relative
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != content:
                stale.append(str(relative))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Regenerate example documentation: " + ", ".join(stale))
    print(f"Synchronized {len(EXAMPLES)} example/module README and source views.")
