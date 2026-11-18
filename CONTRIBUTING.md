# Contributing

Help make infrastructure learning accurate, practical, and welcoming.
Small corrections, tested examples, diagrams, accessibility improvements,
and reproducible bug reports are welcome.

## Before changing code

Read the current structure, relevant README, and existing tests.
Open an issue for significant scope or architecture changes.
Do not add another service catalog that duplicates the
[companion Azure template library](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0).
Keep this project focused on progressive learning and reusable foundations.

## A good contribution

- Original, licensed content with clear purpose and prerequisites.
- Real Terraform source, typed/documented inputs, minimal outputs.
- Secure defaults and explicit cost, state, and cleanup guidance.
- Focused plan-only tests using provider mocks for Azure.
- Updated catalog metadata and generated README/source views.
- No credentials, real state, private identifiers, or saved plans.

## Validation

Run Terraform format, initialization, validation, and focused tests.
All Azure tests must explicitly plan with mocks; routine CI must not create
paid resources. Existing test runs are not permission to deploy in Azure.

Build documentation with `python -m mkdocs build --strict` and run the local
link checker. Full commands and version policy are in the
[maintenance guide](https://brown9804.github.io/Terraform-Overview/maintaining.html).

## Pull requests

Explain the learning problem, relevant changes, validation actually performed,
limitations, and any live-resource implications. Include screenshots for
layout changes. Do not claim tests passed without running them.
Keep unrelated cleanup out of the pull request.

Contributions to this repository are provided under its existing GPL-3.0
license. Respect linked projects' separate licenses.
