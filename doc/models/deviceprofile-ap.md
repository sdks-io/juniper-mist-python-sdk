
# Deviceprofile Ap

Device Profile

## Structure

`DeviceprofileAp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aeroscout` | [`ApAeroscout`](../../doc/models/ap-aeroscout.md) | Optional | Aeroscout AP settings |
| `ble_config` | [`ApBle`](../../doc/models/ap-ble.md) | Optional | BLE AP settings |
| `created_time` | `float` | Optional | - |
| `disable_eth_1` | `bool` | Optional | whether to disable eth1 port<br>**Default**: `False` |
| `disable_eth_2` | `bool` | Optional | whether to disable eth2 port<br>**Default**: `False` |
| `disable_eth_3` | `bool` | Optional | whether to disable eth3 port<br>**Default**: `False` |
| `disable_module` | `bool` | Optional | whether to disable module port<br>**Default**: `False` |
| `for_site` | `bool` | Optional | - |
| `height` | `float` | Optional | Device Only. Height, in meters, optional |
| `id` | `uuid\|string` | Optional | - |
| `iot_config` | [`ApIot`](../../doc/models/ap-iot.md) | Optional | IoT AP settings |
| `ip_config` | [`ApIp`](../../doc/models/ap-ip.md) | Optional | IP AP settings |
| `led` | [`ApLed`](../../doc/models/ap-led.md) | Optional | LED AP settings |
| `map_id` | `uuid\|string` | Optional | Device Only.. Map where the device belongs to |
| `mesh` | [`ApMesh`](../../doc/models/ap-mesh.md) | Optional | Mesh AP settings |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `notes` | `string` | Optional | Device Only. Any notes about this AP |
| `ntp_servers` | `List of string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `orientation` | `float` | Optional | Device Only. Orientation, 0-359, in degrees, up is 0, right is 90.<br>**Constraints**: `>= 0`, `<= 359` |
| `orientation_overwrite` | `bool` | Optional | whether the user overwrite the orientation |
| `poe_passthrough` | `bool` | Optional | whether to enable power out through module port (for APH) or eth1 (for APL/BT11)<br>**Default**: `False` |
| `port_config` | [`dict`](../../doc/models/ap-port-config.md) | Optional | The property key is the interface(s) name (e.g. "eth1,eth2") |
| `pwr_config` | [`PwrConfig1`](../../doc/models/pwr-config-1.md) | Optional | power related configs |
| `radio_config` | [`ApRadio`](../../doc/models/ap-radio.md) | Optional | Radio AP settings |
| `site_id` | `uuid\|string` | Optional | - |
| `switch_config` | [`ApSwitch`](../../doc/models/ap-switch.md) | Optional | for people who want to fully control the vlans (advanced) |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Optional | **Default**: `'ap'` |
| `usb_config` | [`ApUsb`](../../doc/models/ap-usb.md) | Optional | USB AP settings<br>Note: if native imagotag is enabled, BLE will be disabled automatically<br>Note: legacy, new config moved to ESL Config. |
| `vars` | `object` | Optional | a dictionary of name->value, the vars can then be used in Wlans. This can overwrite those from Site Vars |
| `x` | `float` | Optional | Device Only. x in pixel |
| `y` | `float` | Optional | Device Only. y in pixel |

## Example (as JSON)

```json
{
  "disable_eth1": false,
  "disable_eth2": false,
  "disable_eth3": false,
  "disable_module": false,
  "poe_passthrough": false,
  "type": "ap",
  "aeroscout": {
    "enabled": false,
    "host": "host6",
    "locate_connected": false
  },
  "ble_config": {
    "beacon_enabled": false,
    "beacon_rate": 110,
    "beacon_rate_mode": "default",
    "beam_disabled": [
      113,
      114,
      115
    ],
    "custom_ble_packet_enabled": false
  },
  "created_time": 198.3
}
```

