
# Device Ap

AP

## Structure

`DeviceAp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aeroscout` | [`ApAeroscout`](../../doc/models/ap-aeroscout.md) | Optional | Aeroscout AP settings |
| `ble_config` | [`ApBle`](../../doc/models/ap-ble.md) | Optional | BLE AP settings |
| `centrak` | [`Centrak`](../../doc/models/centrak.md) | Optional | - |
| `client_bridge` | [`ApClientBridge`](../../doc/models/ap-client-bridge.md) | Optional | - |
| `created_time` | `float` | Optional | - |
| `deviceprofile_id` | `uuid\|string` | Optional | - |
| `disable_eth_1` | `bool` | Optional | whether to disable eth1 port<br>**Default**: `False` |
| `disable_eth_2` | `bool` | Optional | whether to disable eth2 port<br>**Default**: `False` |
| `disable_eth_3` | `bool` | Optional | whether to disable eth3 port<br>**Default**: `False` |
| `disable_module` | `bool` | Optional | whether to disable module port<br>**Default**: `False` |
| `esl_config` | [`ApEslConfig`](../../doc/models/ap-esl-config.md) | Optional | - |
| `for_site` | `bool` | Optional | - |
| `height` | `float` | Optional | height, in meters, optional |
| `id` | `uuid\|string` | Optional | - |
| `image_1_url` | `string` | Optional | - |
| `image_2_url` | `string` | Optional | - |
| `image_3_url` | `string` | Optional | - |
| `iot_config` | [`ApIot`](../../doc/models/ap-iot.md) | Optional | IoT AP settings |
| `ip_config` | [`ApIp`](../../doc/models/ap-ip.md) | Optional | IP AP settings |
| `led` | [`ApLed`](../../doc/models/ap-led.md) | Optional | LED AP settings |
| `locked` | `bool` | Optional | whether this map is considered locked down |
| `map_id` | `uuid\|string` | Optional | map where the device belongs to |
| `mesh` | [`ApMesh`](../../doc/models/ap-mesh.md) | Optional | Mesh AP settings |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `notes` | `string` | Optional | any notes about this AP |
| `ntp_servers` | `List of string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `orientation` | `float` | Optional | orientation, 0-359, in degrees, up is 0, right is 90.<br>**Constraints**: `>= 0`, `<= 359` |
| `poe_passthrough` | `bool` | Optional | whether to enable power out through module port (for APH) or eth1 (for APL/BT11)<br>**Default**: `False` |
| `port_config` | [`dict`](../../doc/models/ap-port-config.md) | Optional | eth0 is allowed in mesh relay mode, otherwise eth0 is not allowed here.<br>The property key is the interface(s) name (e.g. "eth1" or"eth1,eth2") |
| `pwr_config` | [`PwrConfig`](../../doc/models/pwr-config.md) | Optional | power related configs |
| `radio_config` | [`ApRadio`](../../doc/models/ap-radio.md) | Optional | Radio AP settings |
| `site_id` | `uuid\|string` | Optional | - |
| `uplink_port_config` | [`UplinkPortConfig`](../../doc/models/uplink-port-config.md) | Optional | - |
| `usb_config` | [`ApUsb`](../../doc/models/ap-usb.md) | Optional | USB AP settings<br>Note: if native imagotag is enabled, BLE will be disabled automatically<br>Note: legacy, new config moved to ESL Config. |
| `vars` | `object` | Optional | a dictionary of name->value, the vars can then be used in Wlans. This can overwrite those from Site Vars |
| `x` | `float` | Optional | x in pixel |
| `y` | `float` | Optional | y in pixel |

## Example (as JSON)

```json
{
  "disable_eth1": false,
  "disable_eth2": false,
  "disable_eth3": false,
  "disable_module": false,
  "poe_passthrough": false,
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
  "centrak": {
    "enabled": false
  },
  "client_bridge": {
    "auth": {
      "psk": "psk6",
      "type": "open"
    },
    "enabled": false,
    "ssid": "ssid0"
  },
  "created_time": 198.3
}
```

