
# Sle Impacted Clients

## Structure

`SleImpactedClients`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifier` | `string` | Optional | - |
| `clients` | [`List of Client`](../../doc/models/client.md) | Optional | - |
| `end` | `int` | Optional | - |
| `failure` | `string` | Optional | - |
| `limit` | `int` | Optional | - |
| `metric` | `string` | Optional | - |
| `page` | `int` | Optional | - |
| `start` | `int` | Optional | - |
| `total_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "classifier": "classifier4",
  "clients": [
    {
      "degraded": 12,
      "duration": 118,
      "mac": "mac8",
      "name": "name4",
      "switches": [
        {
          "interfaces": [
            "interfaces2",
            "interfaces3"
          ],
          "switch_mac": "switch_mac9",
          "switch_name": "switch_name3"
        },
        {
          "interfaces": [
            "interfaces3",
            "interfaces4",
            "interfaces5"
          ],
          "switch_mac": "switch_mac0",
          "switch_name": "switch_name4"
        },
        {
          "interfaces": [
            "interfaces4"
          ],
          "switch_mac": "switch_mac1",
          "switch_name": "switch_name5"
        }
      ]
    }
  ],
  "end": 254,
  "failure": "failure6",
  "limit": 172
}
```

