mock_provider "azurerm" {}

run "preserve_metadata" {
  command = plan

  variables {
    name     = "rg-learning"
    location = "eastus2"
    tags     = { environment = "dev" }
  }

  assert {
    condition     = azurerm_resource_group.this.tags["environment"] == "dev"
    error_message = "Caller ownership/environment metadata must reach the resource."
  }
}
