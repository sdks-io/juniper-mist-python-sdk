
# Ble Stat

## Structure

`BleStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beacon_rate` | `int` | Optional | - |
| `eddystone_uid_enabled` | `bool` | Optional | - |
| `eddystone_uid_freq_msec` | `int` | Optional | - |
| `eddystone_uid_instance` | `string` | Optional | - |
| `eddystone_uid_namespace` | `string` | Optional | - |
| `eddystone_url_enabled` | `bool` | Optional | - |
| `eddystone_url_freq_msec` | `int` | Optional | Frequency (msec) of data emmit by Eddystone-UID beacon |
| `eddystone_url_url` | `string` | Optional | - |
| `ibeacon_enabled` | `bool` | Optional | - |
| `ibeacon_major` | `int` | Optional | - |
| `ibeacon_minor` | `int` | Optional | - |
| `ibeacon_uuid` | `uuid\|string` | Optional | - |
| `major` | `int` | Optional | - |
| `minors` | `List of int` | Optional | - |
| `power` | `int` | Optional | - |
| `rx_bytes` | `int` | Optional | - |
| `rx_pkts` | `int` | Optional | - |
| `tx_bytes` | `int` | Optional | - |
| `tx_pkts` | `int` | Optional | - |
| `tx_resets` | `int` | Optional | resets due to tx hung |
| `uuid` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "beacon_rate": 94,
  "eddystone_uid_enabled": false,
  "eddystone_uid_freq_msec": 108,
  "eddystone_uid_instance": "eddystone_uid_instance4",
  "eddystone_uid_namespace": "eddystone_uid_namespace4"
}
```

