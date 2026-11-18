terraform {
  required_version = ">= 1.7, < 2.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "= 5.14.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "prefix" {
  description = "Short lowercase prefix for the resource group and network."
  type        = string
  default     = "learn"

  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{1,11}$", var.prefix))
    error_message = "Use 2-12 lowercase letters, digits, or hyphens beginning with a letter."
  }
}

variable "environment" {
  description = "Environment boundary; use a separate state per environment."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "Choose dev, test, or prod."
  }
}

variable "location" {
  description = "Approved Azure region."
  type        = string
  default     = "eastus2"
}

variable "storage_account_name" {
  description = "Your globally unique lowercase alphanumeric storage name."
  type        = string
}

locals {
  name = "${var.prefix}-${var.environment}"
  tags = {
    environment = var.environment
    managedBy   = "terraform"
  }
}

module "group" {
  source   = "../../modules/azure-resource-group"
  name     = "rg-${local.name}"
  location = var.location
  tags     = local.tags
}

module "network" {
  source              = "../../modules/azure-network"
  name                = "${local.name}-vnet"
  resource_group_name = module.group.name
  location            = module.group.location
}

module "storage" {
  source              = "../../modules/azure-storage"
  name                = var.storage_account_name
  resource_group_name = module.group.name
  location            = module.group.location
}

output "resource_group_name" {
  description = "Dedicated group created by this root configuration."
  value       = module.group.name
}

output "storage_id" {
  description = "Management-plane ID; no data access is granted."
  value       = module.storage.id
}

output "subnet_ids" {
  description = "Named workload subnet IDs."
  value       = module.network.subnet_ids
}
