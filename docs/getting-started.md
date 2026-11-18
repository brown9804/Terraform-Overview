# Getting started without cloud resources

**Goal:** inspect a plan, record a local value, and clean it up.

## Install

Install [Terraform CLI](https://developer.hashicorp.com/terraform/install),
[VS Code](https://code.visualstudio.com/), and the
[HashiCorp Terraform extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform).
Use your platform's official installer and verify:

```shell
terraform version
```

The examples require Terraform 1.7 or later; CI records an exact tested version.
The first lab uses the built-in provider and needs no Azure account.
Clone the repository or choose **Code > Download ZIP**:

```shell
git clone https://github.com/brown9804/Terraform-Overview.git
cd Terraform-Overview
```

## Read the source

```hcl title="examples/01-first-plan/main.tf"
--8<-- "examples/01-first-plan/main.tf"
```

`terraform_data` manages a record in Terraform state; it does not call Azure
or create a file through a cloud provider.
The resource address is `terraform_data.project`.
The input variable has a validated default, and the output reads the
resource's resulting value.

## Initialize, validate, and preview

```shell
terraform -chdir=examples/01-first-plan init
terraform -chdir=examples/01-first-plan validate
terraform -chdir=examples/01-first-plan test
terraform -chdir=examples/01-first-plan plan
```

**Expected:** successful validation/tests and a plan adding one resource.
The resource's output may be unknown until apply. `init` prepares the directory;
`plan` has not created the managed record.

## Apply locally

```shell
terraform -chdir=examples/01-first-plan apply
terraform -chdir=examples/01-first-plan output
terraform -chdir=examples/01-first-plan state list
```

Read the plan and type the requested confirmation. Expected output:
`project_name = "learning"`. State lists `terraform_data.project`.
An immediate second plan should report no changes.

## Change an input and compare

```shell
terraform -chdir=examples/01-first-plan plan -var="project_name=second-lab"
```

Expected: an input update, not an Azure operation. Do not assume the same
behavior for a cloud resource: changing some provider attributes can force
replacement. Always inspect each resource's planned action.

## Cleanup

```shell
terraform -chdir=examples/01-first-plan destroy
terraform -chdir=examples/01-first-plan state list
```

After confirming destruction, the state list is empty. Ignored local state
files may still exist; remove them only after you no longer need the lab.
For Azure, deleting a state file does **not** delete resources.

**Exercise:** use an invalid uppercase name and identify the variable validation
error. Continue with [language](language.md).
