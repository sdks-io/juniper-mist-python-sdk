
# Device Radio Channels

## Structure

`DeviceRadioChannels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24_40_mhz_allowed` | `bool` | Required | - |
| `band_24_channels` | `object` | Required | - |
| `band_24_enabled` | `bool` | Required | - |
| `band_5_channels` | `object` | Required | - |
| `band_5_enabled` | `bool` | Required | - |
| `certified` | `bool` | Required | - |
| `code` | `int` | Required | - |
| `dfs_ok` | `bool` | Required | - |
| `key` | `string` | Required | - |
| `name` | `string` | Required | - |
| `uses` | `string` | Required | - |

## Example (as JSON)

```json
{
  "band24_40mhz_allowed": false,
  "band24_channels": {
    "key1": "val1",
    "key2": "val2"
  },
  "band24_enabled": false,
  "band5_channels": {
    "key1": "val1",
    "key2": "val2"
  },
  "band5_enabled": false,
  "certified": false,
  "code": 130,
  "dfs_ok": false,
  "key": "key0",
  "name": "name0",
  "uses": "uses8"
}
```

