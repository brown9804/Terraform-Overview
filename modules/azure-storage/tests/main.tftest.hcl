mock_provider "azurerm" {}

variables {
  name                = "stlearningexample"
  location            = "eastus2"
  resource_group_name = "rg-learning"
}

run "private_identity_defaults" {
  command = plan

  assert {
    condition     = azurerm_storage_account.this.public_network_access == "Disabled" && !azurerm_storage_account.this.shared_access_key_enabled && !azurerm_storage_account.this.allow_nested_items_to_be_public
    error_message = "Public networking, shared keys, and public containers must remain disabled."
  }
}

run "reject_invalid_storage_name" {
  command = plan

  variables {
    name = "Invalid-Storage"
  }

  expect_failures = [var.name]
}
