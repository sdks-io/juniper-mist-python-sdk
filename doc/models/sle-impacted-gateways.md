
# Sle Impacted Gateways

## Structure

`SleImpactedGateways`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifier` | `string` | Optional | - |
| `end` | `int` | Optional | - |
| `failure` | `string` | Optional | - |
| `gateways` | [`List of Gateways1`](../../doc/models/gateways-1.md) | Optional | - |
| `limit` | `int` | Optional | - |
| `metric` | `string` | Optional | - |
| `page` | `int` | Optional | - |
| `start` | `int` | Optional | - |
| `total_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "classifier": "classifier4",
  "end": 254,
  "failure": "failure6",
  "gateways": [
    {
      "degraded": 107.37,
      "duration": 91,
      "gateway_mac": "gateway_mac5",
      "gateway_model": "gateway_model9",
      "gateway_version": "gateway_version1"
    }
  ],
  "limit": 172
}
```

