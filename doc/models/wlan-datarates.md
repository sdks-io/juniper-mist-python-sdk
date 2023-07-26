
# Wlan Datarates

data rates wlan settings

## Structure

`WlanDatarates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ht` | `string` | Optional | MCS bitmasks for 4 streams (16-bit for each stream, MCS0 is least significant bit), e.g. 00ff 00f0 001f limits HT rates to MCS 0-7 for 1 stream, MCS 4-7 for 2 stream (i.e. MCS 12-15), MCS 1-5 for 3 stream (i.e. MCS 16-20) |
| `legacy` | `List of string` | Optional | list of supported rates (IE=1) and extended supported rates (IE=50) for custom template, append ‘b’ at the end to indicate a rate being basic/mandatory. If `template`==`custom` is configured and legacy does not define at least one basic rate, it will use `no-legacy` default values |
| `min_rssi` | `int` | Optional | Minimum RSSI for client to connect, 0 means not enforcing |
| `template` | `string` | Optional | * `no-legacy`: no 11b<br>* `compatible`: all, like before, default setting that Broadcom/Atheros used<br>* `legacy-only`: disable 802.11n and 802.11ac<br>* `high-density`: no 11b, no low rates<br>* `custom`: user defined |
| `vht` | `string` | Optional | MCS bitmasks for 4 streams (16-bit for each stream, MCS0 is least significant bit), e.g. 03ff 01ff 00ff limits VHT rates to MCS 0-9 for 1 stream, MCS 0-8 for 2 streams, and MCS 0-7 for 3 streams. |

## Example (as JSON)

```json
{
  "ht": "ht8",
  "legacy": [
    "legacy2",
    "legacy3",
    "legacy4"
  ],
  "min_rssi": 210,
  "template": "template6",
  "vht": "vht2"
}
```

