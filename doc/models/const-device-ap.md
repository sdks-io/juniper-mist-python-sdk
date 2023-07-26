
# Const Device Ap

## Structure

`ConstDeviceAp`

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

## Example (as JSON)

```json
{
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

