
# Wlan App Qos

app qos wlan settings

## Structure

`WlanAppQos`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | [`Apps`](../../doc/models/apps.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `others` | [`List of Other`](../../doc/models/other.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "apps": {
    "skype-business-video": {
      "dscp": 18,
      "dst_subnet": "dst_subnet2",
      "src_subnet": "src_subnet0"
    },
    "skype-business-voice": {
      "dscp": 194
    }
  },
  "enabled": false,
  "others": [
    {
      "dscp": 50,
      "dst_subnet": "dst_subnet4",
      "port_ranges": "port_ranges4",
      "protocol": "protocol4",
      "src_subnet": "src_subnet2"
    },
    {
      "dscp": 51,
      "dst_subnet": "dst_subnet5",
      "port_ranges": "port_ranges3",
      "protocol": "protocol5",
      "src_subnet": "src_subnet3"
    }
  ]
}
```

