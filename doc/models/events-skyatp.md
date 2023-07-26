
# Events Skyatp

SkyATP events

## Structure

`EventsSkyatp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_mac` | `string` | Required | - |
| `for_site` | `bool` | Optional | - |
| `ip` | `string` | Required | - |
| `mac` | `string` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `threat_level` | `int` | Required | - |
| `timestamp` | `float` | Required | - |
| `mtype` | `string` | Required | - |

## Example (as JSON)

```json
{
  "device_mac": "device_mac4",
  "for_site": false,
  "ip": "ip4",
  "mac": "mac4",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "threat_level": 62,
  "timestamp": 128.82,
  "type": "type0"
}
```

