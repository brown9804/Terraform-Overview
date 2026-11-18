# Learning paths

## Beginner: learn without a cloud account

1. Read [fundamentals](fundamentals.md): describe configuration, provider,
   resource address, plan, and state in your own words.
2. Follow [getting started](getting-started.md) and plan a built-in data record.
3. Apply locally, inspect the output, and destroy the record.
4. Study [language and expressions](language.md) with the second lab.
5. Change environment keys and explain the planned address changes.

**Checkpoint:** explain why local Terraform state exists even when no cloud
resource was created.

## Intermediate: interfaces and safe changes

Read [providers](providers.md), [state/backends](state-backends.md), and
[modules](modules.md). Inspect the network and storage test assertions,
then run them with mocked providers. Learn what cannot be known from a mock.

**Checkpoint:** distinguish a provider constraint, a selected provider version,
a dependency lock file, and a module source/version.

## Advanced: Azure and team operations

Review [security/cost boundaries](security-costs.md), [workflow](workflow.md),
and [testing/CI](testing.md). Inspect the [Azure project](azure-project.md)
and choose a service from the [companion templates](azure-templates.md).
Write an approved state, identity, network, and cleanup design before live use.

**Checkpoint:** explain how you would recover a failed apply without deleting
state or applying an unreviewed replacement plan.
