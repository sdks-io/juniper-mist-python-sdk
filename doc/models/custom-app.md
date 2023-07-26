
# Custom App

## Structure

`CustomApp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_type` | `string` | Optional | - |
| `hostname` | `List of string` | Optional | - |
| `name` | `string` | Optional | - |
| `protocol` | [`Protocol5Enum`](../../doc/models/protocol-5-enum.md) | Optional | **Default**: `'http'` |

## Example (as JSON)

```json
{
  "protocol": "http",
  "app_type": "app_type6",
  "hostname": [
    "hostname2",
    "hostname3",
    "hostname4"
  ],
  "name": "name0"
}
```

