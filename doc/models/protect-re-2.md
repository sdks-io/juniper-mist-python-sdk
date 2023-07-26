
# Protect Re 2

restrict inbound-traffic to host  (draft)

## Structure

`ProtectRe2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_services` | `List of string` | Optional | optionally, services we'll allow |
| `custom` | [`List of Custom1`](../../doc/models/custom-1.md) | Optional | - |
| `enabled` | `bool` | Optional | when enabled, all traffic that is not essential to our operation will be dropped<br>e.g. ntp / dns / traffic to mist will be allowed by default |
| `trusted_hosts` | `List of string` | Optional | when `enabled`==`true`, all traffic that is not essential to our operation will be dropped (e.g. if dhcpd is enabled, we'll make sure it works) |

## Example (as JSON)

```json
{
  "allowed_services": [
    "allowed_services6"
  ],
  "custom": [
    {
      "port_range": "port_range3",
      "protocol": "any",
      "subnets": [
        "subnets6",
        "subnets5",
        "subnets4"
      ]
    }
  ],
  "enabled": false,
  "trusted_hosts": [
    "trusted_hosts8",
    "trusted_hosts9",
    "trusted_hosts0"
  ]
}
```

