
# Api V1 Const Mxedge Models Response

## Structure

`ApiV1ConstMxedgeModelsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_ports` | `bool` | Optional | - |
| `display` | `string` | Optional | - |
| `model` | `string` | Optional | - |
| `ports` | [`dict`](../../doc/models/generated-object.md) | Optional | - |

## Example (as JSON)

```json
{
  "custom_ports": false,
  "display": "display8",
  "model": "model2",
  "ports": {
    "key0": {
      "display": "display3",
      "speed": 85
    },
    "key1": {
      "display": "display2",
      "speed": 86
    }
  }
}
```

