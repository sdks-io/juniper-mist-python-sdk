
# Wlan Hotspot 20

hostspot 2.0 wlan settings

## Structure

`WlanHotspot20`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether to enable hotspot 2.0 config |
| `operators` | `List of string` | Optional | list of operators to support, options: att, google, tmobile, charter, boingo, hughes_systique, single_digits, global_reach |
| `venue_name` | `string` | Optional | venue name, default is site name |

## Example (as JSON)

```json
{
  "enabled": false,
  "operators": [
    "operators1"
  ],
  "venue_name": "venue_name6"
}
```

