
# Path Preferences

The property key is the path name

## Structure

`PathPreferences`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paths` | [`Paths`](../../doc/models/paths.md) | Optional | - |
| `strategy` | [`Strategy2Enum`](../../doc/models/strategy-2-enum.md) | Optional | **Default**: `'ordered'` |

## Example (as JSON)

```json
{
  "strategy": "ordered",
  "paths": {
    "cost": 118,
    "gateway_ip": "gateway_ip0",
    "internet_access": false,
    "name": "name4",
    "networks": [
      "networks6",
      "networks7",
      "networks8"
    ]
  }
}
```

