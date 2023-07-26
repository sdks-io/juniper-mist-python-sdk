
# Vrf Instances

## Structure

`VrfInstances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extra_routes` | [`dict`](../../doc/models/extra-routes-6.md) | Optional | Property key is the destination CIDR (e.g. "10.0.0.0/8") |
| `networks` | `List of string` | Optional | - |

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

