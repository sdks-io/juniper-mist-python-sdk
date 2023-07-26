
# Const Device Model

## Structure

`ConstDeviceModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_type` | `string` | Optional | - |
| `band_24` | [`Band6`](../../doc/models/band-6.md) | Optional | - |
| `band_5` | [`Band6`](../../doc/models/band-6.md) | Optional | - |
| `band_6` | [`Band6`](../../doc/models/band-6.md) | Optional | - |
| `ce_dfs_ok` | `bool` | Optional | - |
| `cisco_pace` | `bool` | Optional | - |
| `description` | `string` | Optional | - |
| `disallowed_channels` | `dict` | Optional | Property key is a list of country codes (e.g. "GB, DE") |
| `display` | `string` | Optional | - |
| `extio` | [`dict`](../../doc/models/extio.md) | Optional | Property key is the GPIO port name (e.g. "D0", "A1") |
| `fcc_dfs_ok` | `bool` | Optional | - |
| `has_11_ax` | `bool` | Optional | - |
| `has_compass` | `bool` | Optional | - |
| `has_ext_ant` | `bool` | Optional | - |
| `has_extio` | `bool` | Optional | - |
| `has_height` | `bool` | Optional | - |
| `has_module_port` | `bool` | Optional | - |
| `has_poe_out` | `bool` | Optional | - |
| `has_scanning_radio` | `bool` | Optional | - |
| `has_selectable_radio` | `bool` | Optional | - |
| `has_usb` | `bool` | Optional | - |
| `has_vble` | `bool` | Optional | - |
| `has_wifi_band_24` | `bool` | Optional | - |
| `has_wifi_band_5` | `bool` | Optional | - |
| `has_wifi_band_6` | `bool` | Optional | - |
| `max_poe_out` | `int` | Optional | - |
| `max_wlans` | `int` | Optional | - |
| `model` | `string` | Optional | - |
| `other_dfs_ok` | `bool` | Optional | - |
| `outdoor` | `bool` | Optional | - |
| `radios` | `dict` | Optional | Property key is the radio number (e.g. r0, r1, ...). Property value is the RF band (e.g. "24", "5", ...) |
| `shared_scanning_radio` | `bool` | Optional | - |
| `mtype` | [`Type8Enum`](../../doc/models/type-8-enum.md) | Optional | - |
| `unmanaged` | `bool` | Optional | - |
| `vble` | [`Vble`](../../doc/models/vble.md) | Optional | - |
| `alias` | `string` | Optional | - |
| `defaults` | [`Defaults1`](../../doc/models/defaults-1.md) | Optional | Object Key is the interface type name (e.g. "lan_ports", "wan_ports", ...) |
| `evolved_os` | `bool` | Optional | **Default**: `False` |
| `evpn_ri_type` | `string` | Optional | - |
| `experimental` | `bool` | Optional | **Default**: `False` |
| `fans_pluggable` | `bool` | Optional | **Default**: `False` |
| `has_bgp` | `bool` | Optional | **Default**: `False` |
| `has_ets` | `bool` | Optional | **Default**: `False` |
| `has_evpn` | `bool` | Optional | **Default**: `False` |
| `has_irb` | `bool` | Optional | **Default**: `False` |
| `has_snapshot` | `bool` | Optional | **Default**: `True` |
| `has_vc` | `bool` | Optional | **Default**: `True` |
| `modular` | `bool` | Optional | **Default**: `False` |
| `no_shaping_rate` | `bool` | Optional | **Default**: `False` |
| `number_fans` | `int` | Optional | - |
| `oc_device` | `bool` | Optional | **Default**: `False` |
| `oob_interface` | `string` | Optional | - |
| `packet_action_drop_only` | `bool` | Optional | **Default**: `False` |
| `pic` | `dict` | Optional | Object Key is the PIC number |
| `sub_required` | `string` | Optional | - |
| `ha_node_0_fpc` | `int` | Optional | - |
| `ha_node_1_fpc` | `int` | Optional | - |
| `has_fxp_0` | `bool` | Optional | **Default**: `True` |
| `has_ha_control` | `bool` | Optional | **Default**: `False` |
| `has_ha_data` | `bool` | Optional | **Default**: `False` |
| `irb_disabled_by_default` | `bool` | Optional | **Default**: `False` |
| `ports` | [`Ports1`](../../doc/models/ports-1.md) | Optional | Object Key is the interface name (e.g. "ge-0/0/1", ...) |
| `t_128_device` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "evolved_os": false,
  "experimental": false,
  "fans_pluggable": false,
  "has_bgp": false,
  "has_ets": false,
  "has_evpn": false,
  "has_irb": false,
  "has_snapshot": true,
  "has_vc": true,
  "modular": false,
  "no_shaping_rate": false,
  "oc_device": false,
  "packet_action_drop_only": false,
  "has_fxp0": true,
  "has_ha_control": false,
  "has_ha_data": false,
  "irb_disabled_by_default": false,
  "t128_device": false,
  "ap_type": "ap_type8",
  "band24": {
    "max_clients": 176,
    "max_power": 208,
    "min_power": 38
  },
  "band5": {
    "max_clients": 252,
    "max_power": 132,
    "min_power": 142
  },
  "band6": {
    "max_clients": 154,
    "max_power": 230,
    "min_power": 240
  },
  "ce_dfs_ok": false
}
```

