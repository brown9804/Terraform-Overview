# Maintaining this platform

## Source of truth

Terraform source lives in `examples/` and `modules/`. The example catalog,
module READMEs, and website source-view wrappers are generated from
`.github/scripts/generate_examples.py`. Update that metadata when changing
purpose, inputs, commands, limitations, or expected behavior.

```shell
python .github/scripts/generate_examples.py
python .github/scripts/generate_examples.py --check
```

The website includes canonical code through checked MkDocs snippets.
Do not paste a second manually maintained implementation into a tutorial.
Keep the companion template library linked rather than copied.

## Versions and validation

CI pins Terraform 1.17.2. Azure root examples select AzureRM 5.14.0; child
modules declare a compatible 5.x range. These are reviewed example versions,
not a claim that every future latest release will work unchanged.
Update provider constraints, actual generated lock files, tests, and this
guide together after reviewing upstream release/migration notes.

```shell
terraform fmt -check -recursive
python .github/scripts/validate_terraform.py
python -m unittest discover -s .github/scripts -p "test_*.py"
python -m mkdocs build --strict
python .github/scripts/check_site.py
```

Install `requirements.txt` in an isolated Python environment first.
The validator installs provider plugins and runs every module/example's
validation and explicit plan-only tests. Initialization enforces committed
provider selections with a read-only lock file. It never authenticates to Azure.
For intentional upgrades, regenerate genuine provider locks with Terraform;
never write package hashes by hand.

## GitHub Actions and Pages

`.github/workflows/validate-and-deploy.yml` runs on pull requests, main pushes,
and manual dispatch. The Pages job requires successful validation and runs
only on main outside pull-request events. Configure repository Pages to use
GitHub Actions. No Azure resource deployment belongs in that workflow.

The source/lock diagnostic artifact intentionally excludes state, plans,
and `.terraform/`. Do not broaden its paths to upload the entire workspace.

## Shared design

Keep the navy full-width Material layout, accessible light/dark palettes,
Cloud2BR logo/favicon, search, breadcrumbs, responsive navigation,
copy buttons, Atlanta identity, and disabled generator footer.
Check desktop and narrow mobile widths after layout changes.

Use `/Terraform-Overview/` as the Pages base path in the site checker.
Documentation pages use `.html` URLs because `use_directory_urls` is false.
Navigation should progress from learning to references and contribution.

## Release checklist

Require green CI; review generated links, snippets, catalog rows, and safety
statements; verify the deployed URL before announcing publication.
Record exactly which checks ran. Offline tests do not imply a live Azure
deployment succeeded.
