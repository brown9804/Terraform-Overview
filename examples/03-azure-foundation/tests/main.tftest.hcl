mock_provider "azurerm" {}

variables {
  storage_account_name = "stlearningexample"
}

run "compose_environment_names" {
  command = plan

  variables {
    prefix      = "demo"
    environment = "test"
  }

  assert {
    condition     = output.resource_group_name == "rg-demo-test"
    error_message = "The composed group name must separate the chosen environment."
  }
}

run "reject_environment_typo" {
  command = plan

  variables {
    environment = "production"
  }

  expect_failures = [var.environment]
}
