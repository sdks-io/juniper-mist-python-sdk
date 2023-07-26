
# Ip Stat 4

OOBM IP stats

## Structure

`IpStat4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip` | `string` | Optional | - |
| `ips` | `dict` | Optional | Property key is the interface name. IPs for each net interface |
| `macs` | `dict` | Optional | Property key is the interface name. MAC for each net interface |

## Example (as JSON)

```json
{
  "ip": "ip4",
  "ips": {
    "key0": "ips4",
    "key1": "ips5"
  },
  "macs": {
    "key0": "macs5",
    "key1": "macs6"
  }
}
```

