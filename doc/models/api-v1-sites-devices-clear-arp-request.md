
# Api V1 Sites Devices Clear Arp Request

## Structure

`ApiV1SitesDevicesClearArpRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip` | `string` | Optional | The IP address for which to clear an ARP entry. port_id must be specified. Both vlan and ip cannot be specified. |
| `node` | [`NodeEnum`](../../doc/models/node-enum.md) | Optional | only for HA |
| `port_id` | `string` | Optional | The device interface on which to clear the ARP cache. |
| `vlan` | `int` | Optional | The VLAN on which to clear the ARP cache. port_id must be specified. Both vlan and ip cannot be specified. |

## Example (as JSON)

```json
{
  "ip": "10.1.1.1",
  "port_id": "wan",
  "vlan": 1000,
  "node": "node0"
}
```

