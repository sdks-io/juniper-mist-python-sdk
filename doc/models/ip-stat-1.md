
# Ip Stat 1

## Structure

`IpStat1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of object` | Optional | - |
| `dns_suffix` | `List of object` | Optional | - |
| `gateway` | `string` | Optional | - |
| `gateway_6` | `string` | Optional | - |
| `ip` | `string` | Optional | - |
| `ip_6` | `string` | Optional | - |
| `ips` | [`Ips`](../../doc/models/ips.md) | Optional | - |
| `netmask` | `string` | Optional | - |
| `netmask_6` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "dns": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "dns_suffix": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "gateway": "gateway0",
  "gateway6": "gateway66",
  "ip": "ip4"
}
```

