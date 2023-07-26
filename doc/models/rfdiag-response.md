
# Rfdiag Response

## Structure

`RfdiagResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `uuid\|string` | Optional | if `type`==`asset`, id of the asset |
| `asset_name` | `string` | Optional | if `type`==`asset`, name of the asset |
| `client_name` | `string` | Optional | if `type`==`client`, hostname of the client |
| `duration` | `int` | Required | recording length in seconds, max is 120 |
| `end_time` | `int` | Required | timestamp of end of recording |
| `frame_count` | `int` | Required | Number of frames in the output |
| `id` | `string` | Optional | - |
| `mac` | `string` | Optional | if `type`==`client` or `asset`, mac of the device |
| `map_id` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `next` | `string` | Optional | Optional. id of the next recoding if present. Only valid for site survey. |
| `raw_events` | `string` | Required | URL to a JSON file that contains array of raw location diag events |
| `ready` | `bool` | Required | whether it’s ready for playback |
| `sdkclient_id` | `uuid\|string` | Optional | if `type`==`sdkclient`, sdkclient_id of this recording |
| `sdkclient_name` | `string` | Optional | if `type`==`sdkclient`, name of the sdkclient |
| `sdkclient_uuid` | `uuid\|string` | Optional | if `type`==`sdkclient`, device_id of sdkclient |
| `start_time` | `int` | Required | timestamp of the recording (the start) |
| `mtype` | [`Type37Enum`](../../doc/models/type-37-enum.md) | Required | sdkclient / client / asset |
| `url` | `string` | Required | URL to a JSON file that contains an array of frames, each frame is the same format |

## Example (as JSON)

```json
{
  "asset_id": "0000253e-0000-0000-0000-000000000000",
  "asset_name": "asset_name8",
  "client_name": "client_name6",
  "duration": 112,
  "end_time": 96,
  "frame_count": 22,
  "id": "id0",
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "raw_events": "raw_events2",
  "ready": false,
  "start_time": 120,
  "type": "asset",
  "url": "url4"
}
```

