
# Services

## Structure

`Services`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disable_local` | `bool` | Optional | whether to prevent wireless clients to discover bonjour devices on the same WLAN<br>**Default**: `False` |
| `radius_groups` | `List of string` | Optional | optional, if the service is further restricted for certain RADIUS groups |
| `scope` | `string` | Optional | how bonjour services should be discovered for the same WLAN, same_site (default) / same_map / same_ap |

## Example (as JSON)

```json
{
  "disable_local": false,
  "radius_groups": [
    "radius_groups3"
  ],
  "scope": "scope2"
}
```

