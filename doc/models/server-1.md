
# Server 1

## Structure

`Server1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contents` | [`List of Content2`](../../doc/models/content-2.md) | Optional | - |
| `explicit_priority` | `bool` | Optional | - |
| `facility` | [`FacilityEnum`](../../doc/models/facility-enum.md) | Optional | - |
| `host` | `string` | Optional | - |
| `match` | `string` | Optional | - |
| `port` | `int` | Optional | **Default**: `514` |
| `protocol` | [`Protocol4Enum`](../../doc/models/protocol-4-enum.md) | Optional | **Default**: `'udp'` |
| `routing_instance` | `string` | Optional | - |
| `severity` | [`Severity1Enum`](../../doc/models/severity-1-enum.md) | Optional | - |
| `source_address` | `string` | Optional | if source_address is configured, will use the vlan firstly otherwise use source_ip |
| `structured_data` | `bool` | Optional | - |
| `tag` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "host": "syslogd.internal",
  "match": "!alarm|ntp|errors.crc_error[chan]",
  "port": 514,
  "protocol": "udp",
  "routing_instance": "routing-instance-name",
  "contents": [
    {
      "facility": "authorization",
      "severity": "warning"
    }
  ],
  "explicit_priority": false,
  "facility": "daemon"
}
```

