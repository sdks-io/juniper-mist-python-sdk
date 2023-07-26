
# Assets Array Stats Search

## Structure

`AssetsArrayStatsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of StatsAsset`](../../doc/models/stats-asset.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "battery_voltage": 23.99,
      "eddystone_uid_instance": "eddystone_uid_instance7",
      "eddystone_uid_namespace": "eddystone_uid_namespace1",
      "eddystone_url_url": "eddystone_url_url1",
      "ibeacon_major": 139,
      "mac": "mac7"
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

