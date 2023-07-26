
# Route Exists

## Structure

`RouteExists`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `route` | `string` | Optional | - |
| `vrf_name` | `string` | Optional | name of the vrf instance<br>it can also be the name of the VPN or wan if they<br>**Default**: `'default'` |

## Example (as JSON)

```json
{
  "route": "192.168.0.0/24",
  "vrf_name": "default"
}
```

