
# Api V1 Sites Devices Ping Request

## Structure

`ApiV1SitesDevicesPingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | **Default**: `10` |
| `egress_interface` | `string` | Optional | Interface through which packet needs to egress |
| `host` | `string` | Required | - |
| `node` | [`Node4Enum`](../../doc/models/node-4-enum.md) | Optional | Only for HA |
| `size` | `int` | Optional | **Default**: `56`<br>**Constraints**: `>= 56`, `<= 65535` |

## Example (as JSON)

```json
{
  "count": 10,
  "host": "1.1.1.1",
  "size": 56,
  "egress_interface": "egress_interface0",
  "node": "node0"
}
```

