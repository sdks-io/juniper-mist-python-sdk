
# Dmvpn

Dynamic Multipoint VPN configurations

## Structure

`Dmvpn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether DMVPN is enabled<br>**Default**: `False` |
| `holding_time` | `int` | Optional | optional; the holding time for NHRP ‘registration requests’ and ‘resolution replies’ sent from the Mist AP (in seconds); default 600 |
| `host_routes` | `List of string` | Optional | optional; list of IPv4 DMVPN peer host ip-addresses to which traffic is forwarded |

## Example (as JSON)

```json
{
  "enabled": false,
  "holding_time": 138,
  "host_routes": [
    "host_routes0",
    "host_routes1",
    "host_routes2"
  ]
}
```

