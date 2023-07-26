
# Site Occupancy Analytics

Occupancy Analytics settings

## Structure

`SiteOccupancyAnalytics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assets_enabled` | `bool` | Optional | indicate whether named BLE assets should be included in the zone occupancy calculation<br>**Default**: `False` |
| `clients_enabled` | `bool` | Optional | indicate whether connected WiFi clients should be included in the zone occupancy calculation<br>**Default**: `True` |
| `min_duration` | `int` | Optional | minimum duration<br>**Default**: `3000` |
| `sdkclients_enabled` | `bool` | Optional | indicate whether SDK clients should be included in the zone occupancy calculation<br>**Default**: `False` |
| `unconnected_clients_enabled` | `bool` | Optional | indicate whether unconnected WiFi clients should be included in the zone occupancy calculation<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "assets_enabled": false,
  "clients_enabled": true,
  "min_duration": 3000,
  "sdkclients_enabled": false,
  "unconnected_clients_enabled": false
}
```

