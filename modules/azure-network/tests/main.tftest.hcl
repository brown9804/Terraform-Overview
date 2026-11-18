mock_provider "azurerm" {}

variables {
  name                = "learning-vnet"
  location            = "eastus2"
  resource_group_name = "rg-learning"
}

run "deny_inbound_and_attach_every_subnet" {
  command = plan

  variables {
    subnets = { application = "10.30.1.0/24", data = "10.30.2.0/24" }
  }

  assert {
    condition     = length(azurerm_subnet_network_security_group_association.this) == 2 && one(azurerm_network_security_group.this.security_rule).access == "Deny"
    error_message = "Every subnet must have the default deny-inbound security policy attached."
  }
}

run "reject_bad_cidr" {
  command = plan

  variables {
    subnets = { application = "not-a-cidr" }
  }

  expect_failures = [var.subnets]
}
