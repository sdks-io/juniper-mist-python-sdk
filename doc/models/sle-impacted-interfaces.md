
# Sle Impacted Interfaces

## Structure

`SleImpactedInterfaces`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifier` | `string` | Optional | - |
| `end` | `int` | Optional | - |
| `failure` | `string` | Optional | - |
| `interfaces` | [`List of Interface1`](../../doc/models/interface-1.md) | Optional | - |
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
  "interfaces": [
    {
      "degraded": 97.41,
      "duration": 226.47,
      "interface_name": "interface_name3",
      "switch_mac": "switch_mac9",
      "switch_name": "switch_name3"
    },
    {
      "degraded": 97.42,
      "duration": 226.48,
      "interface_name": "interface_name4",
      "switch_mac": "switch_mac0",
      "switch_name": "switch_name4"
    }
  ],
  "limit": 172
}
```

