
# Junos Vrf Instance

## Structure

`JunosVrfInstance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extra_routes` | [`dict`](../../doc/models/extra-routes-3.md) | Required | - |
| `networks` | `List of string` | Required | - |

## Example (as JSON)

```json
{
  "extra_routes": {
    "key0": {
      "via": "via7"
    },
    "key1": {
      "via": "via8"
    }
  },
  "networks": [
    "networks2",
    "networks3",
    "networks4"
  ]
}
```

