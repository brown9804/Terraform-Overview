terraform {
  required_version = ">= 1.7, < 2.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 5.14.0, < 6.0"
    }
  }
}

variable "name" {
  description = "Globally unique lowercase alphanumeric storage account name."
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9]{3,24}$", var.name))
    error_message = "Use 3-24 lowercase letters and digits."
  }
}

variable "resource_group_name" {
  description = "Existing resource group name."
  type        = string
}

variable "location" {
  description = "Approved Azure region."
  type        = string
}

resource "azurerm_storage_account" "this" {
  name                            = var.name
  resource_group_name             = var.resource_group_name
  location                        = var.location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  account_kind                    = "StorageV2"
  min_tls_version                 = "TLS1_2"
  https_traffic_only_enabled      = true
  allow_nested_items_to_be_public = false
  shared_access_key_enabled       = false
  public_network_access           = "Disabled"
  default_to_oauth_authentication = true
}

output "id" {
  description = "Storage account resource ID."
  value       = azurerm_storage_account.this.id
}

output "name" {
  description = "Storage account name, not an access credential."
  value       = azurerm_storage_account.this.name
}
