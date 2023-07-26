
# Event 7

## Structure

`Event7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_loc` | `List of float` | Optional | coordinates (if any) of reporting AP (updated once in 60s per client) |
| `beam` | `int` | Required | antenna index, from 1-8, clock-wise starting from the LED |
| `device_id` | `uuid\|string` | Required | device id of the reporting AP |
| `ibeacon_major` | `int` | Optional | - |
| `ibeacon_minor` | `int` | Optional | - |
| `ibeacon_uuid` | `uuid\|string` | Optional | - |
| `is_asset` | `bool` | Optional | - |
| `mac` | `string` | Required | MAC of the asset/ beacon |
| `map_id` | `uuid\|string` | Required | - |
| `mfg_company_id` | `string` | Optional | BLE manufacturing company ID |
| `mfg_data` | `string` | Optional | BLE manufacturing data in hex byte-string format (ie: “112233AABBCC”) |
| `org_id` | `uuid\|string` | Required | - |
| `rssi` | `float` | Required | signal strength |
| `service_packets` | [`List of ServicePacket1`](../../doc/models/service-packet-1.md) | Optional | - |
| `site_id` | `uuid\|string` | Required | - |
| `timestamp` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "ap_loc": [
    34.02,
    34.03,
    34.04
  ],
  "beam": 168,
  "device_id": "000008c6-0000-0000-0000-000000000000",
  "ibeacon_major": 222,
  "ibeacon_minor": 172,
  "ibeacon_uuid": "000007ea-0000-0000-0000-000000000000",
  "is_asset": false,
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "rssi": 2.78,
  "site_id": "000007d6-0000-0000-0000-000000000000"
}
```

