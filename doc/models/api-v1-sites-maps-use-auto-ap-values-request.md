
# Api V1 Sites Maps Use Auto Ap Values Request

## Structure

`ApiV1SitesMapsUseAutoApValuesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `bool` | Optional | If accept is true, accepts placement for devices in list otherwise. If false, reject for devices in list.<br>**Default**: `False` |
| `device_macs` | `List of string` | Optional | A list of macs to accept/reject. If a list is not provided the API will accept/reject for the full map. |
| `mfor` | [`ForEnum`](../../doc/models/for-enum.md) | Optional | The selector to choose auto placement or auto orientation.<br>**Default**: `'placement'` |

## Example (as JSON)

```json
{
  "accept": false,
  "for": "placement",
  "device_macs": [
    "device_macs8",
    "device_macs9",
    "device_macs0"
  ]
}
```

