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
  description = "Name of the dedicated resource group."
  type        = string
}

variable "location" {
  description = "Approved Azure region for resource group metadata."
  type        = string
}

variable "tags" {
  description = "Ownership and environment metadata, without secrets."
  type        = map(string)
  default     = {}
}

resource "azurerm_resource_group" "this" {
  name     = var.name
  location = var.location
  tags     = var.tags
}

output "name" {
  description = "Resource group name for downstream modules."
  value       = azurerm_resource_group.this.name
}

output "location" {
  description = "Azure-normalized resource group region."
  value       = azurerm_resource_group.this.location
}

output "id" {
  description = "Management-plane resource ID, not a credential."
  value       = azurerm_resource_group.this.id
}
