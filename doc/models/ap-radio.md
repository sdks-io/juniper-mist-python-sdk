
# Ap Radio

Radio AP settings

## Structure

`ApRadio`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_rrm_disable` | `bool` | Optional | **Default**: `False` |
| `ant_gain_24` | `int` | Optional | antenna gain for 2.4G - for models with external antenna only<br>**Constraints**: `>= 0` |
| `ant_gain_5` | `int` | Optional | antenna gain for 5G - for models with external antenna only<br>**Constraints**: `>= 0` |
| `ant_gain_6` | `int` | Optional | antenna gain for 6G - for models with external antenna only<br>**Constraints**: `>= 0` |
| `antenna_mode` | [`AntennaModeEnum`](../../doc/models/antenna-mode-enum.md) | Optional | **Default**: `'default'` |
| `band_24` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_24_usage` | [`Band24UsageEnum`](../../doc/models/band-24-usage-enum.md) | Optional | if `band_24_usage`==`5`, by default, band_5 properties is used, if specific channel/bandwidth/power/... is desired, use the "band_5_on_24_radio"<br>**Default**: `'24'` |
| `band_5` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_5_on_24_radio` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_6` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `indoor_use` | `bool` | Optional | to make an outdoor operate indoor.<br>for an outdoor-ap, some channels are disallowed by default, this allows the user to use it as an indoor-ap<br>**Default**: `False` |
| `scanning_enabled` | `bool` | Optional | whether scanning radio is enabled |

## Example (as JSON)

```json
{
  "allow_rrm_disable": false,
  "ant_gain_24": 4,
  "ant_gain_5": 5,
  "ant_gain_6": 5,
  "antenna_mode": "default",
  "band_24_usage": "24",
  "indoor_use": false
}
```

