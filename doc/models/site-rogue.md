
# Site Rogue

Rogue site settings

## Structure

`SiteRogue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether or not rogue detection is enabled |
| `honeypot_enabled` | `bool` | Optional | whether or not honeypot detection is enabled |
| `min_duration` | `int` | Optional | minimum duration for a bssid to be considered rogue<br>**Default**: `10`<br>**Constraints**: `<= 59` |
| `min_rssi` | `int` | Optional | minimum RSSI for an AP to be considered rogue (ignoring APs that’s far away)<br>**Default**: `-80`<br>**Constraints**: `>= -85` |
| `whitelisted_bssids` | `List of string` | Optional | list of BSSIDs to whitelist. Ex: "cc-:8e-:6f-:d4-:bf-:16", "cc-8e-6f-d4-bf-16", "cc-73-*", "cc:82:*" |
| `whitelisted_ssids` | `List of string` | Optional | list of SSIDs to whitelist |

## Example (as JSON)

```json
{
  "min_duration": 10,
  "min_rssi": -80,
  "enabled": false,
  "honeypot_enabled": false,
  "whitelisted_bssids": [
    "whitelisted_bssids5"
  ]
}
```

