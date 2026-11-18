terraform {
  required_version = ">= 1.7, < 2.0"
}

variable "prefix" {
  description = "Short lowercase prefix for the learning records."
  type        = string
  default     = "learn"
}

variable "environments" {
  description = "Unique environment keys; stable keys prevent index-based address changes."
  type        = set(string)
  default     = ["dev", "test"]

  validation {
    condition     = length(var.environments) > 0 && alltrue([for value in var.environments : contains(["dev", "test", "prod"], value)])
    error_message = "Choose one or more of dev, test, and prod."
  }
}

locals {
  environments = {
    for environment in var.environments : environment => {
      name           = "${var.prefix}-${environment}"
      retention_days = environment == "prod" ? 90 : 30
    }
  }
}

resource "terraform_data" "environment" {
  for_each = local.environments
  input    = each.value
}

output "planned_environments" {
  description = "Derived values available during planning; no cloud access occurs."
  value       = local.environments
}
