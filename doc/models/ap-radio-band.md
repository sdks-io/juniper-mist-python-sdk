
# Ap Radio Band

Radio Band AP settings

## Structure

`ApRadioBand`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_rrm_disable` | `bool` | Optional | - |
| `ant_gain` | `int` | Optional | - |
| `antenna_mode` | [`AntennaModeEnum`](../../doc/models/antenna-mode-enum.md) | Optional | **Default**: `'default'` |
| `bandwidth` | [`BandwidthEnum`](../../doc/models/bandwidth-enum.md) | Optional | channel width for the band, 20 / 40 / 80 / 160, 80 is only applicable for band_5 and 160 is only for band_6, ignored if channel is 0 |
| `channel` | `int` | Optional | For Device. (primary) channel for the band, 0 means using the Site Setting |
| `channels` | `List of int` | Optional | For RFTemplates. List of channels, null or empty array means auto |
| `disabled` | `bool` | Optional | whether to disable the radio |
| `power` | `int` | Optional | TX power of the radio. For Devices, 0 mean using the Site Setting |
| `power_max` | `int` | Optional | when power=0, max tx power to use, HW-specific values will be used if not set |
| `power_min` | `int` | Optional | when power=0, min tx power to use, HW-specific values will be used if not set |
| `preamble` | [`PreambleEnum`](../../doc/models/preamble-enum.md) | Optional | **Default**: `'short'` |
| `usage` | [`UsageEnum`](../../doc/models/usage-enum.md) | Optional | for band_24 radio<br>**Default**: `'24'` |

## Example (as JSON)

```json
{
  "antenna_mode": "default",
  "preamble": "short",
  "usage": "24",
  "allow_rrm_disable": false,
  "ant_gain": 40,
  "bandwidth": 80,
  "channel": 120
}
```

