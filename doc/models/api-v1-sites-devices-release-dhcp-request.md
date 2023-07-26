
# Api V1 Sites Devices Release Dhcp Request

## Structure

`ApiV1SitesDevicesReleaseDhcpRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `node` | [`NodeEnum`](../../doc/models/node-enum.md) | Optional | only for HA |
| `port` | `string` | Required | The nework interface on which to release the current DHCP release<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "port": "wan-interface",
  "node": "node0"
}
```

