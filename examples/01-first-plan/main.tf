terraform {
  required_version = ">= 1.7, < 2.0"
}

variable "project_name" {
  description = "Lowercase project name used to demonstrate inputs and state."
  type        = string
  default     = "learning"

  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{2,19}$", var.project_name))
    error_message = "Use 3-20 lowercase letters, digits, or hyphens, beginning with a letter."
  }
}

resource "terraform_data" "project" {
  input = {
    name = var.project_name
    goal = "Understand plan, apply, state, and destroy without cloud resources."
  }
}

output "project_name" {
  description = "The name recorded by the built-in Terraform data resource."
  value       = terraform_data.project.output.name
}
