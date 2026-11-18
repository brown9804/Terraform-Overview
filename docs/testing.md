# Testing and safe CI

## Layers of validation

| Layer | What it checks | What it does not prove |
| --- | --- | --- |
| Format | Canonical HCL presentation | Correct infrastructure behavior |
| Init/validate | Dependency installation and configuration/schema consistency | Azure authorization or service availability |
| Mocked plan tests | Input rules and planned resource contracts | Real API/provider behavior |
| Authenticated plan | Proposed changes in a live context | Successful apply or application function |
| Apply plus runtime checks | Actual deployment and observed behavior | Universal production readiness |

## Tests can create resources

Terraform test runs default to apply unless configured otherwise.
Every test in **this repository** explicitly uses `command = plan`.
Azure tests use `mock_provider "azurerm" {}`; the validator rejects test files
that omit the explicit plan command or Azure mock.
Do not assume these safeguards exist in a downloaded service template.

```hcl title="modules/azure-storage/tests/main.tftest.hcl"
--8<-- "modules/azure-storage/tests/main.tftest.hcl"
```

One assertion protects security defaults. Another expects a specific
variable-validation failure. Invalid-input tests should fail if the
input guard disappears.

## Run focused checks

```shell
terraform -chdir=modules/azure-storage init -backend=false
terraform -chdir=modules/azure-storage validate
terraform -chdir=modules/azure-storage test
```

Expected: two successful test runs, including the expected invalid-name
failure case. No Azure resource or login is involved.
Plugin downloads still need network access and should be checksum-verified.

## Repository automation

Actions pins the Terraform CLI and runs every configuration's init, validate,
and plan-only tests. Formatting changes must already be committed.
Source and lock metadata are available as a diagnostics artifact; state,
saved plans, and `.terraform/` working files are not uploaded.

The website build and local-link checks are separate from Terraform tests.
GitHub Pages is the only automatic deployment. No cloud credentials are
configured or needed for routine validation.

## Designing future live tests

If live tests are added later, separate them behind explicit authorization,
budget/time limits, isolated subscriptions/groups/state, least-privilege
federated identity, and verified cleanup. Protect plan/state artifacts and
avoid running privileged workflows against untrusted pull-request code.
