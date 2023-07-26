
# Event 1

## Structure

`Event1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `uuid\|string` | Required | asset id |
| `beam` | `int` | Required | antenna index, from 1-8, clock-wise starting from the LED |
| `device_id` | `uuid\|string` | Required | device where the asset reading is from |
| `ibeacon_major` | `int` | Optional | iBeacon major |
| `ibeacon_minor` | `int` | Optional | iBeacon minor |
| `ibeacon_uuid` | `uuid\|string` | Optional | iBeacon UUID |
| `mac` | `string` | Required | MAC of the beacon |
| `map_id` | `uuid\|string` | Required | map id |
| `mfg_company_id` | `float` | Required | optional, BLE manufacturing company ID |
| `mfg_data` | `string` | Required | optional, BLE manufacturing data in hex byte-string format (ie: “112233AABBCC”) |
| `rssi` | `float` | Required | signal strength |
| `service_data_data` | `string` | Optional | optional, data from service data |
| `service_data_last_rx_time` | `int` | Optional | optional, last data transmit time from service data |
| `service_data_rx_cnt` | `int` | Optional | optional, data transmit count from service data |
| `service_data_uuid` | `uuid\|string` | Optional | optional, UUID from service data |
| `service_packets` | [`List of ServicePacket`](../../doc/models/service-packet.md) | Optional | list of service data packets heard from the asset/ beacon |
| `site_id` | `uuid\|string` | Required | site id |
| `timestamp` | `float` | Required | - |

## Example (as JSON)

```json
{
  "asset_id": "0000253e-0000-0000-0000-000000000000",
  "beam": 168,
  "device_id": "000008c6-0000-0000-0000-000000000000",
  "ibeacon_major": 222,
  "ibeacon_minor": 172,
  "ibeacon_uuid": "000007ea-0000-0000-0000-000000000000",
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "mfg_company_id": 250.66,
  "mfg_data": "mfg_data8",
  "rssi": 2.78,
  "service_data_data": "service_data_data8",
  "service_data_last_rx_time": 166,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 128.82
}
```

