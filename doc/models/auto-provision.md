
# Auto Provision

## Structure

`AutoProvision`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable` | `bool` | Optional | - |
| `latlng` | [`Latlng`](../../doc/models/latlng.md) | Optional | - |
| `primary` | [`Primary`](../../doc/models/primary.md) | Optional | - |
| `region` | [`RegionEnum`](../../doc/models/region-enum.md) | Optional | **Default**: `'auto'` |
| `secondary` | [`Secondary`](../../doc/models/secondary.md) | Optional | - |

## Example (as JSON)

```json
{
  "region": "auto",
  "enable": false,
  "latlng": {
    "lat": 144.64,
    "lng": 22.82
  },
  "primary": {
    "num_hosts": "num_hosts6",
    "wan_names": [
      "wan_names8"
    ]
  },
  "secondary": {
    "num_hosts": "num_hosts8",
    "wan_names": [
      "wan_names0"
    ]
  }
}
```

