
# Result 11

## Structure

`Result11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_24` | `int` | Required | - |
| `channel_5` | `int` | Required | - |
| `radio_macs` | `List of string` | Optional | - |
| `radios` | [`List of Radio`](../../doc/models/radio.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `secpolicy_violated` | `bool` | Required | - |
| `ssids` | `List of string` | Optional | - |
| `ssids_24` | `List of string` | Optional | - |
| `ssids_5` | `List of string` | Optional | - |
| `timestamp` | `float` | Required | - |
| `version` | `string` | Required | - |
| `wlans` | [`List of Wlan2`](../../doc/models/wlan-2.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "channel_24": 230,
  "channel_5": 118,
  "radio_macs": [
    "radio_macs7",
    "radio_macs8",
    "radio_macs9"
  ],
  "radios": [
    {
      "band": "band2",
      "channel": 10
    },
    {
      "band": "band3",
      "channel": 9
    },
    {
      "band": "band4",
      "channel": 8
    }
  ],
  "secpolicy_violated": false,
  "ssids": [
    "ssids9",
    "ssids0"
  ],
  "ssids_24": [
    "ssids_244"
  ],
  "ssids_5": [
    "ssids_50",
    "ssids_51"
  ],
  "timestamp": 128.82,
  "version": "version4"
}
```

