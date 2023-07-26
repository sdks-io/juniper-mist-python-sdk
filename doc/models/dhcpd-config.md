
# Dhcpd Config

## Structure

`DhcpdConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns_servers` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `fixed_bindings` | [`dict`](../../doc/models/fixed-bindings.md) | Optional | The property key is the device MAC address |
| `gateway` | `string` | Optional | - |
| `ip_end` | `string` | Optional | - |
| `ip_start` | `string` | Optional | - |
| `servers` | `List of string` | Optional | - |
| `mtype` | [`Type18Enum`](../../doc/models/type-18-enum.md) | Optional | **Default**: `'local'` |

## Example (as JSON)

```json
{
  "type": "local",
  "dns_servers": [
    "dns_servers0"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ],
  "fixed_bindings": {
    "key0": {
      "ip": "ip3",
      "name": "name9"
    },
    "key1": {
      "ip": "ip4",
      "name": "name0"
    },
    "key2": {
      "ip": "ip5",
      "name": "name1"
    }
  },
  "gateway": "gateway0",
  "ip_end": "ip_end4"
}
```

