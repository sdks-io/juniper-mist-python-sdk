
# Configs History Search

## Structure

`ConfigsHistorySearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result11`](../../doc/models/result-11.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "channel_24": 57,
      "channel_5": 35,
      "radio_macs": [
        "radio_macs0",
        "radio_macs1",
        "radio_macs2"
      ],
      "radios": [
        {
          "band": "band9",
          "channel": 183
        },
        {
          "band": "band0",
          "channel": 182
        },
        {
          "band": "band1",
          "channel": 181
        }
      ],
      "secpolicy_violated": true,
      "ssids": [
        "ssids6",
        "ssids7"
      ],
      "ssids_24": [
        "ssids_241"
      ],
      "ssids_5": [
        "ssids_53",
        "ssids_54"
      ],
      "timestamp": 63.09,
      "version": "version9"
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

