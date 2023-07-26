
# Api V1 Sites Devices Show Route Request

## Structure

`ApiV1SitesDevicesShowRouteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `neighbor` | `string` | Optional | - |
| `node` | [`Node4Enum`](../../doc/models/node-4-enum.md) | Optional | Only for HA |
| `prefix` | `string` | Optional | route prefix |
| `protocol` | `string` | Optional | only bgp is supported |
| `route` | [`RouteEnum`](../../doc/models/route-enum.md) | Optional | if specified, dump both received and advertised<br><br>* for SSR, show bgp neighbors 10.250.18.202 received-routes/advertised-routes<br>* for SRX, show route receive-protocol/advertise-protocol bgp 192.168.255.12 |
| `vrf_name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "neighbor": "192.168.4.1",
  "prefix": "192.168.0.5/30",
  "protocol": "bgp",
  "route": "advertised",
  "vrf_name": "default",
  "node": "node0"
}
```

