# Inputs, expressions, and stable resource keys

## Inputs and derived values

Use variables for caller choices and locals for derived expressions.
Choose types deliberately: `string`, `number`, `bool`, collections,
and structured object types. Validation catches mistakes early; it is not
a replacement for live provider checks.

```hcl title="examples/02-expressions/main.tf"
--8<-- "examples/02-expressions/main.tf"
```

The environment collection is a set. A `for` expression converts it into a
map containing derived names and retention numbers. `for_each` creates
one data record for each stable key.

## Why keys matter

`terraform_data.environment["dev"]` and
`terraform_data.environment["prod"]` are different addresses.
Removing `dev` proposes removing that record. Renaming a key normally means
a different address unless you explicitly describe a supported move.
By contrast, changing the display name inside an existing key keeps its
address, though a provider may still replace the remote object.

Use `count` for genuinely index-based instances and `for_each` for named
entities. Inserting a list item can shift `count` indexes and produce
surprising changes if indexes are being used as identities.

## Expressions and functions

String interpolation uses `"${var.prefix}-${environment}"`.
The conditional `condition ? true_value : false_value` selects retention.
`contains` restricts choices, `alltrue` checks every element, `regex` with
`can` validates shape, and `cidrhost` can validate CIDR syntax.

An expression can be unknown during plan when it depends on an ID the
provider will return during apply. Do not force unknown values into
`for_each` keys. Use stable configuration keys and computed values as map values.

## Outputs and sensitive values

Outputs expose a module interface, not just terminal decoration.
Prefer a resource ID/name over a whole resource object.
`sensitive = true` redacts normal display; it does not encrypt state or saved
plans. Avoid secrets in both examples and outputs.

## Practice

```shell
terraform -chdir=examples/02-expressions init
terraform -chdir=examples/02-expressions test
terraform -chdir=examples/02-expressions plan -var='environments=["dev","prod"]'
```

The quoted array uses Bash-style quoting; adapt it to your shell.
Expected: two stable keys and 90-day production learning metadata.
No actual log retention policy is deployed.
