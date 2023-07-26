
# Protect Re

restrict inbound-traffic to host
when enabled, all traffic that is not essential to our operation will be dropped
e.g. ntp / dns / traffic to mist will be allowed by default, if dhcpd is enabled, we'll make sure it works

## Structure

`ProtectRe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_services` | `List of string` | Optional | optionally, services we'll allow |
| `custom` | [`List of Custom`](../../doc/models/custom.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `trusted_hosts` | `List of string` | Optional | optionally, host/subnets we'll allow traffic to/from |

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

