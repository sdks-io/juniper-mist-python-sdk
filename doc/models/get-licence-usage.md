
# Get Licence Usage

## Structure

`GetLicenceUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_entitled` | `dict` | Required | license entitlement for the entire org |
| `svna_enabled` | `bool` | Required | license entitlement for the Switch device whether SVNA enabled |
| `trial_enabled` | `bool` | Required | - |
| `usages` | `dict` | Required | subscriptions and their quantities |
| `vna_enabled` | `bool` | Required | license entitlement for the AP device whether VNA enabled |
| `wvna_enabled` | `bool` | Required | license entitlement for the Gateway device whether WVNA enabled |

## Example (as JSON)

```json
{
  "org_entitled": {
    "key0": 174,
    "key1": 175,
    "key2": 176
  },
  "svna_enabled": false,
  "trial_enabled": false,
  "usages": {
    "key0": 77,
    "key1": 78
  },
  "vna_enabled": false,
  "wvna_enabled": false
}
```

