
# Api V1 Sites Devices Synthetic Test Request

## Structure

`ApiV1SitesDevicesSyntheticTestRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hostname` | `string` | Optional | if `type`==`dns` |
| `ip` | `string` | Optional | if `type`==`arp` |
| `password` | `string` | Optional | if `type`==`radius` |
| `mtype` | [`Type54Enum`](../../doc/models/type-54-enum.md) | Optional | - |
| `url` | `string` | Optional | if `type`==`curl` |
| `username` | `string` | Optional | if `type`==`radius` |
| `vlan_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "hostname": "hostname4",
  "ip": "ip4",
  "password": "password4",
  "type": "speedtest",
  "url": "url4"
}
```

