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
  description = "Virtual network name; also prefixes the security group."
  type        = string
}

variable "resource_group_name" {
  description = "Existing resource group name."
  type        = string
}

variable "location" {
  description = "Azure region for the network resources."
  type        = string
}

variable "address_space" {
  description = "Non-overlapping VNet CIDR blocks."
  type        = list(string)
  default     = ["10.30.0.0/16"]
}

variable "subnets" {
  description = "Stable subnet names mapped to CIDRs inside the VNet."
  type        = map(string)
  default     = { workload = "10.30.1.0/24" }

  validation {
    condition     = length(var.subnets) > 0 && alltrue([for prefix in values(var.subnets) : can(cidrhost(prefix, 0))])
    error_message = "Supply at least one valid CIDR prefix."
  }
}

resource "azurerm_virtual_network" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name
  address_space       = var.address_space
}

resource "azurerm_network_security_group" "this" {
  name                = "${var.name}-nsg"
  location            = var.location
  resource_group_name = var.resource_group_name

  security_rule {
    name                       = "DenyAllInbound"
    priority                   = 4096
    direction                  = "Inbound"
    access                     = "Deny"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_subnet" "this" {
  for_each             = var.subnets
  name                 = each.key
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.this.name
  address_prefixes     = [each.value]
}

resource "azurerm_subnet_network_security_group_association" "this" {
  for_each                  = azurerm_subnet.this
  subnet_id                 = each.value.id
  network_security_group_id = azurerm_network_security_group.this.id
}

output "id" {
  description = "Virtual network resource ID."
  value       = azurerm_virtual_network.this.id
}

output "subnet_ids" {
  description = "Map of subnet names to resource IDs."
  value       = { for name, subnet in azurerm_subnet.this : name => subnet.id }
}
