
# Ap Ble

BLE AP settings

## Structure

`ApBle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beacon_enabled` | `bool` | Optional | whether Mist beacons is enabled<br>**Default**: `True` |
| `beacon_rate` | `int` | Optional | required if `beacon_rate_mode`==`custom`, 1-10, in number-beacons-per-second |
| `beacon_rate_mode` | [`BeaconRateModeEnum`](../../doc/models/beacon-rate-mode-enum.md) | Optional | **Default**: `'default'` |
| `beam_disabled` | `List of int` | Optional | list of AP BLE location beam numbers (1-8) which should be disabled at the AP and not transmit location information (where beam 1 is oriented at the top the AP, growing counter-clock-wise, with 9 being the omni BLE beam) |
| `custom_ble_packet_enabled` | `bool` | Optional | can be enabled if `beacon_enabled`==`true`, whether to send custom packet<br>**Default**: `False` |
| `custom_ble_packet_frame` | `string` | Optional | The custom frame to be sent out in this beacon. The frame must be a hexstring |
| `custom_ble_packet_freq_msec` | `int` | Optional | Frequency (msec) of data emitted by custom ble beacon<br>**Constraints**: `>= 0` |
| `eddystone_uid_adv_power` | `int` | Optional | advertised TX Power, -100 to 20 (dBm), omit this attribute to use default<br>**Constraints**: `>= -100`, `<= 20` |
| `eddystone_uid_beams` | `string` | Optional | - |
| `eddystone_uid_enabled` | `bool` | Optional | only if `beacon_enabled`==`false`, Whether Eddystone-UID beacon is enabled |
| `eddystone_uid_freq_msec` | `int` | Optional | Frequency (msec) of data emmit by Eddystone-UID beacon |
| `eddystone_uid_instance` | `string` | Optional | Eddystone-UID instance for the device |
| `eddystone_uid_namespace` | `string` | Optional | Eddystone-UID namespace |
| `eddystone_url_adv_power` | `int` | Optional | advertised TX Power, -100 to 20 (dBm), omit this attribute to use default |
| `eddystone_url_beams` | `string` | Optional | - |
| `eddystone_url_enabled` | `bool` | Optional | only if `beacon_enabled`==`false`, Whether Eddystone-URL beacon is enabled |
| `eddystone_url_freq_msec` | `int` | Optional | Frequency (msec) of data emit by Eddystone-UID beacon |
| `eddystone_url_url` | `string` | Optional | URL pointed by Eddystone-URL beacon |
| `ibeacon_adv_power` | `int` | Optional | advertised TX Power, -100 to 20 (dBm), omit this attribute to use default<br>**Constraints**: `>= -100`, `<= 20` |
| `ibeacon_beams` | `string` | Optional | - |
| `ibeacon_enabled` | `bool` | Optional | can be enabled if `beacon_enabled`==`true`, whether to send iBeacon<br>**Default**: `False` |
| `ibeacon_freq_msec` | `int` | Optional | Frequency (msec) of data emmit for iBeacon |
| `ibeacon_major` | `int` | Optional | Major number for iBeacon |
| `ibeacon_minor` | `int` | Optional | Minor number for iBeacon |
| `ibeacon_uuid` | `uuid\|string` | Optional | optional, if not specified, the same UUID as the beacon will be used |
| `power` | `int` | Optional | required if `power_mode`==`custom`<br>**Default**: `9`<br>**Constraints**: `>= 1`, `<= 10` |
| `power_mode` | `string` | Optional | default / custom |

## Example (as JSON)

```json
{
  "beacon_enabled": true,
  "beacon_rate_mode": "default",
  "custom_ble_packet_enabled": false,
  "custom_ble_packet_frame": "0x........",
  "custom_ble_packet_freq_msec": 300,
  "ibeacon_enabled": false,
  "power": 9,
  "beacon_rate": 94,
  "beam_disabled": [
    97,
    98
  ]
}
```

