
# Client

## Structure

`Client`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `degraded` | `int` | Optional | - |
| `duration` | `int` | Optional | - |
| `mac` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `switches` | [`List of Switches2`](../../doc/models/switches-2.md) | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "degraded": 6,
  "duration": 112,
  "mac": "mac4",
  "name": "name0",
  "switches": [
    {
      "interfaces": [
        "interfaces8",
        "interfaces9"
      ],
      "switch_mac": "switch_mac5",
      "switch_name": "switch_name9"
    },
    {
      "interfaces": [
        "interfaces9",
        "interfaces0",
        "interfaces1"
      ],
      "switch_mac": "switch_mac6",
      "switch_name": "switch_name0"
    },
    {
      "interfaces": [
        "interfaces0"
      ],
      "switch_mac": "switch_mac7",
      "switch_name": "switch_name1"
    }
  ]
}
```

