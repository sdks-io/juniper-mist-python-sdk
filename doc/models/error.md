
# Error

## Structure

`Error`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | `string` | Optional | - |
| `minimum_version` | `string` | Optional | - |
| `reason` | `string` | Optional | - |
| `since` | `int` | Required | - |
| `mtype` | `string` | Required | - |

## Example (as JSON)

```json
{
  "feature": "Mist-Management",
  "minimum_version": "128T-6.0.0-1",
  "since": 1657497600,
  "type": "FW_UPGRADE_REQUIRED_BY_FEATURE",
  "reason": "reason4"
}
```

