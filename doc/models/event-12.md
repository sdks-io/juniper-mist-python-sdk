
# Event 12

## Structure

`Event12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `uuid\|string` | Optional | uuid of named asset |
| `id` | `uuid\|string` | Required | uuid of SDK-client |
| `mac` | `string` | Optional | mac address of wifi client or asset |
| `map_id` | `uuid\|string` | Required | map id |
| `name` | `string` | Optional | name of the client, may be empty |
| `site_id` | `uuid\|string` | Required | site id |
| `timestamp` | `int` | Required | timestamp of the event, epoch |
| `trigger` | [`TriggerEnum`](../../doc/models/trigger-enum.md) | Required | enter / exit |
| `mtype` | `string` | Required | - |
| `zone_id` | `uuid\|string` | Required | zone id |

## Example (as JSON)

```json
{
  "asset_id": "0000253e-0000-0000-0000-000000000000",
  "id": "00001770-0000-0000-0000-000000000000",
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 82,
  "trigger": "enter",
  "type": "type0",
  "zone_id": "000019ec-0000-0000-0000-000000000000"
}
```

