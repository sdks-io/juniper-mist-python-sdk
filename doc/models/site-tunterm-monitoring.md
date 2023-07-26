
# Site Tunterm Monitoring

## Structure

`SiteTuntermMonitoring`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Optional | can be ip, ipv6, hostname<br>**Constraints**: *Minimum Length*: `1` |
| `port` | `int` | Optional | when `protocol`==`tcp` |
| `protocol` | [`Protocol2Enum`](../../doc/models/protocol-2-enum.md) | Optional | **Constraints**: *Minimum Length*: `1` |
| `timeout` | `int` | Optional | **Default**: `300` |

## Example (as JSON)

```json
{
  "host": "10.2.8.15",
  "port": 80,
  "protocol": "tcp",
  "timeout": 300
}
```

