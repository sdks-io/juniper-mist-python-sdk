
# App Limit

bandwidth limiting for apps (applies to up/down)

## Structure

`AppLimit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | `object` | Optional | map from app key to bandwidth in kbps. app key defined in Get Application List |
| `enabled` | `bool` | Optional | - |
| `wxtag_ids` | `object` | Optional | map from wxtag_id of Hostname Wxlan Tags to bandwidth in kbps |

## Example (as JSON)

```json
{
  "apps": {
    "key1": "val1",
    "key2": "val2"
  },
  "enabled": false,
  "wxtag_ids": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

