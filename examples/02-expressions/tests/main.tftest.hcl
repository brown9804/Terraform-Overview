run "environment_rules" {
  command = plan

  variables {
    prefix       = "demo"
    environments = ["dev", "prod"]
  }

  assert {
    condition     = terraform_data.environment["prod"].input.retention_days == 90 && terraform_data.environment["dev"].input.name == "demo-dev"
    error_message = "Production retention and interpolated names must follow environment inputs."
  }
}

run "reject_unknown_environment" {
  command = plan

  variables {
    environments = ["staging"]
  }

  expect_failures = [var.environments]
}
