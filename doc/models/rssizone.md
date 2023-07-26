
# Rssizone

RSSI Zone

## Structure

`Rssizone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `devices` | [`List of Device`](../../doc/models/device.md) | Required | List of devices and the respective RSSI values to be considered in the zone<br>**Constraints**: *Unique Items Required* |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | The name of the zone |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "devices": [
    {
      "device_id": "00002046-0000-0000-0000-000000000000",
      "rssi": 138
    }
  ],
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "name": "name0"
}
```

