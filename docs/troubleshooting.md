# Troubleshooting

| Symptom | Likely investigation | Safe next step |
| --- | --- | --- |
| Terraform command missing | PATH or installation | Reopen terminal; run `terraform version` |
| Provider schema unavailable | Root not initialized | Run `init` in the same root |
| Checksum mismatch | Lock/platform/cache integrity | Verify official package and regenerate trusted lock metadata; do not bypass |
| Subscription required | Live AzureRM context missing | Confirm CLI account and `ARM_SUBSCRIPTION_ID` |
| Authentication succeeds, authorization fails | Wrong scope or insufficient role | Review tenant/subscription and least-privilege role scope |
| Invalid or unavailable storage name | Global naming rules/collision | Choose your own lowercase alphanumeric name |
| Subnet rejected | CIDR overlap/containment/policy | Review the network design; syntax validation is not enough |
| Storage data access denied | Public access intentionally disabled or data role absent | Check endpoints, DNS, routes, and data-plane roles |
| State lock held | Another operation or orphaned lock | Identify owner before unlocking |
| Unexpected replacement | Changed immutable input/address/provider behavior | Stop and inspect plan/source history |
| Apply partially failed | Earlier resources may already exist | Inspect state and remote objects, correct cause, re-plan |
| Website source page missing | Stale generated documentation | Run the documentation generator and commit its outputs |

## Report a reproducible problem

Include CLI/provider versions, affected example, sanitized command and error,
whether this was a mock or live run, and the expected behavior.
Remove subscription/tenant identifiers, personal data, tokens, state, saved
plans, and secrets. Do not upload `.terraform/` or a complete environment dump.

## Mock versus live failure

A successful mock test cannot establish API compatibility at runtime,
regional SKU availability, authorization, quota, Azure Policy compliance,
or private connectivity. Use a reviewed live plan in an isolated approved
environment to investigate those issues.

## State emergencies

Stop concurrent operations and follow the team's recovery procedure.
Keep protected backups before state editing or migration. Do not experiment
with state commands against production to see what happens.
