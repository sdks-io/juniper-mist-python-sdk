
# Api V1 Const Ap Channels Response

## Structure

`ApiV1ConstApChannelsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24_channels` | `dict` | Required | The property key is the channel width |
| `band_24_enabled` | `bool` | Required | - |
| `band_5_channels` | `dict` | Required | The property key is the channel width |
| `band_5_enabled` | `bool` | Required | - |
| `code` | `int` | Required | - |
| `dfs_ok` | `bool` | Required | - |
| `key` | `string` | Required | - |
| `name` | `string` | Required | - |

## Example (as JSON)

```json
{
  "band24_channels": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "band24_enabled": false,
  "band5_channels": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "band5_enabled": false,
  "code": 130,
  "dfs_ok": false,
  "key": "key0",
  "name": "name0"
}
```

