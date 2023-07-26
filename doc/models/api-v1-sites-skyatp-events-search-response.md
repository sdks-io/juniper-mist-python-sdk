
# Api V1 Sites Skyatp Events Search Response

## Structure

`ApiV1SitesSkyatpEventsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of EventsSkyatp`](../../doc/models/events-skyatp.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "device_mac": "device_mac7",
      "for_site": true,
      "ip": "ip7",
      "mac": "mac7",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "site_id": "00002183-0000-0000-0000-000000000000",
      "threat_level": 235,
      "timestamp": 63.09,
      "type": "type7"
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

