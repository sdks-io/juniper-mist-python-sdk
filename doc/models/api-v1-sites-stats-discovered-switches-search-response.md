
# Api V1 Sites Stats Discovered Switches Search Response

## Structure

`ApiV1SitesStatsDiscoveredSwitchesSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result26`](../../doc/models/result-26.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "results": [
    {
      "adopted": true,
      "aps": [
        {
          "hostname": "hostname0",
          "mac": "mac8",
          "poe_status": false,
          "port": "port4",
          "port_id": "port_id4"
        },
        {
          "hostname": "hostname9",
          "mac": "mac9",
          "poe_status": true,
          "port": "port5",
          "port_id": "port_id5"
        }
      ],
      "chassis_id": [
        "chassis_id7",
        "chassis_id8",
        "chassis_id9"
      ],
      "for_site": true,
      "model": "model9",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "site_id": "00002183-0000-0000-0000-000000000000",
      "system_desc": "system_desc3",
      "system_name": "system_name3",
      "timestamp": 63.09,
      "vendor": "vendor9",
      "version": "version9"
    }
  ],
  "start": 224.84,
  "total": 10,
  "next": "next2"
}
```

