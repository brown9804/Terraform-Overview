run "custom_name" {
  command = plan

  variables {
    project_name = "first-lab"
  }

  assert {
    condition     = terraform_data.project.input.name == "first-lab"
    error_message = "The planned input must use the caller's project name."
  }
}

run "reject_invalid_name" {
  command = plan

  variables {
    project_name = "Invalid Name"
  }

  expect_failures = [var.project_name]
}
