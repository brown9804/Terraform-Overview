# Terraform cheat sheet

| Intent | Command | Caution |
| --- | --- | --- |
| Check CLI | `terraform version` | Match the root's required version |
| Initialize | `terraform init` | Downloads executable providers; configures backend |
| Check format | `terraform fmt -check -recursive` | Does not validate behavior |
| Fix format | `terraform fmt -recursive` | Review changed files |
| Validate | `terraform validate` | Initialize providers first |
| Run tests | `terraform test` | Inspect tests: default runs may apply |
| Preview | `terraform plan` | Needs real context unless mocked |
| Save plan | `terraform plan -out=lab.tfplan` | Sensitive artifact |
| Inspect plan | `terraform show lab.tfplan` | Do not publish secret output |
| Apply reviewed plan | `terraform apply lab.tfplan` | Can create paid resources |
| List managed addresses | `terraform state list` | State access can be sensitive |
| Read outputs | `terraform output` | Raw/JSON output can reveal sensitive values |
| Destroy preview | `terraform plan -destroy` | Review all affected resources |
| Inspect providers | `terraform providers` | Identify inherited requirements |

Use `terraform -chdir=examples/01-first-plan plan` to choose a root without
changing your shell directory. Shell quoting differs across Bash, PowerShell,
and cmd; commands using `$NAME` in this repository are labeled Bash.

## Language reminders

- `var.name`: caller input.
- `local.name`: computed expression within a module.
- `resource_type.name.attribute`: managed resource reference.
- `data.type.name.attribute`: data-source result, not a managed object.
- `module.name.output`: child-module interface.
- `for_each`: stable map/set keys become instance addresses.
- `count`: numeric indices become instance addresses.
- `null`: omission where the receiving argument supports it.

## Review checklist

Correct state? Correct subscription? Compatible provider? Unexpected
replacement? Public access? Secrets in artifacts? Estimated cost? Cleanup owner?
