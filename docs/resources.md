# References and next steps

## Primary technical references

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform language](https://developer.hashicorp.com/terraform/language)
- [Terraform CLI](https://developer.hashicorp.com/terraform/cli)
- [Terraform tests](https://developer.hashicorp.com/terraform/language/tests)
- [Provider mocking](https://developer.hashicorp.com/terraform/language/tests/mocking)
- [Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- [AzureRM provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Terraform on Azure](https://learn.microsoft.com/azure/developer/terraform/)
- [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)
- [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

## Companion learning platforms

- [Azure Terraform Templates](https://github.com/Cloud2BR-MSFTLearningHub/AzureTerraformTemplates-v0.0.0):
  service-organized Azure samples; [how to use them here](azure-templates.md).
- [Bicep for Everyone](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/):
  compare Azure-native declarative infrastructure.
- [LaTeX for Everyone](https://brown9804.github.io/LaTeX-For-Everyone/):
  technical writing and reusable document examples.

## Suggested practice

1. Finish both no-cloud examples and explain their resource addresses.
2. Read the three Azure modules and their mocked assertions.
3. Design state boundaries and a private-access diagram for a workload.
4. Review one companion service template against your design.
5. Deploy only in an authorized environment, verify it, and confirm cleanup.

Linked tools, providers, and templates have their own licenses and support
policies. This repository's GPL-3.0 license does not relicense those projects.
