
# Stats Site

Site statistics

## Structure

`StatsSite`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Required | - |
| `alarmtemplate_id` | `uuid\|string` | Required | - |
| `country_code` | `string` | Required | - |
| `created_time` | `float` | Required | - |
| `id` | `uuid\|string` | Required | - |
| `lat` | `float` | Required | - |
| `latlng` | [`Latlng2`](../../doc/models/latlng-2.md) | Required | - |
| `lng` | `float` | Required | - |
| `modified_time` | `float` | Required | - |
| `msp_id` | `string` | Required | - |
| `name` | `string` | Required | - |
| `networktemplate_id` | `uuid\|string` | Required | - |
| `num_ap` | `int` | Required | - |
| `num_ap_connected` | `int` | Required | - |
| `num_clients` | `int` | Required | - |
| `num_devices` | `int` | Required | - |
| `num_devices_connected` | `int` | Required | - |
| `num_gateway` | `int` | Required | - |
| `num_gateway_connected` | `int` | Required | - |
| `num_switch` | `int` | Required | - |
| `num_switch_connected` | `int` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `rftemplate_id` | `uuid\|string` | Required | - |
| `secpolicy_id` | `object` | Optional | - |
| `sitegroup_ids` | `List of uuid\|string` | Required | - |
| `timezone` | `string` | Required | - |
| `tzoffset` | `int` | Required | - |

## Example (as JSON)

```json
{
  "address": "address6",
  "alarmtemplate_id": "00001a0e-0000-0000-0000-000000000000",
  "country_code": "country_code0",
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "lat": 78.08,
  "latlng": {
    "lat": 144.64,
    "lng": 22.82
  },
  "lng": 89.38,
  "modified_time": 136.66,
  "msp_id": "msp_id4",
  "name": "name0",
  "networktemplate_id": "0000162a-0000-0000-0000-000000000000",
  "num_ap": 164,
  "num_ap_connected": 50,
  "num_clients": 150,
  "num_devices": 126,
  "num_devices_connected": 18,
  "num_gateway": 230,
  "num_gateway_connected": 206,
  "num_switch": 146,
  "num_switch_connected": 242,
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "rftemplate_id": "00002648-0000-0000-0000-000000000000",
  "secpolicy_id": {
    "key1": "val1",
    "key2": "val2"
  },
  "sitegroup_ids": [
    "000002a0-0000-0000-0000-000000000000",
    "000002a1-0000-0000-0000-000000000000"
  ],
  "timezone": "timezone0",
  "tzoffset": 180
}
```

