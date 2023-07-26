
# Rftemplate

RF Template

## Structure

`Rftemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ant_gain_24` | `int` | Optional | - |
| `ant_gain_5` | `int` | Optional | - |
| `band_24` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_24_usage` | [`Band24Usage1Enum`](../../doc/models/band-24-usage-1-enum.md) | Optional | If `band_24_usage`==`5`, by default, `band_5` properties is used, if specific channel/bandwidth/power/... If desired, use `band_5_on_24_radio`<br>**Default**: `'24'` |
| `band_5` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_5_on_24_radio` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `country_code` | `string` | Optional | optional, country code to use. If specified, this gets applied to all sites using the RF Template |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `model_specific` | [`dict`](../../doc/models/model-specific.md) | Optional | overwrites for a specific model. If a band is specified, it will shadow the default. The property key is the model name (e.g. "AP63") |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | The name of the RF template |
| `org_id` | `uuid\|string` | Optional | - |
| `scanning_enabled` | `bool` | Optional | whether scanning radio is enabled |
| `site_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "band_24_usage": "24",
  "name": "name0",
  "ant_gain_24": 152,
  "ant_gain_5": 192,
  "band_24": {
    "allow_rrm_disable": false,
    "ant_gain": 0,
    "antenna_mode": "default",
    "bandwidth": 20,
    "channel": 80
  },
  "band_5": {
    "allow_rrm_disable": false,
    "ant_gain": 52,
    "antenna_mode": "2x2",
    "bandwidth": 40,
    "channel": 132
  }
}
```

