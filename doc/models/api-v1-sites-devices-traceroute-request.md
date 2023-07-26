
# Api V1 Sites Devices Traceroute Request

## Structure

`ApiV1SitesDevicesTracerouteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Required | host name |
| `network` | `string` | Optional | optional<br>for gateway only<br>the source to initiate traceroute from. by default, host (internal for SSR, master RI for SRX) is assumed<br>**Default**: `'internal'` |
| `port` | `int` | Optional | when protocol=udp, the udp port to use |
| `protocol` | [`Protocol9Enum`](../../doc/models/protocol-9-enum.md) | Optional | udp (default) /icmp<br>**Default**: `'udp'` |
| `timeout` | `int` | Optional | maximum time in seconds to wait for the response<br>**Default**: `60` |

## Example (as JSON)

```json
{
  "host": "1.1.1.1",
  "network": "corp",
  "port": 33434,
  "protocol": "udp",
  "timeout": 120
}
```

