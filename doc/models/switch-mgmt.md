
# Switch Mgmt

## Structure

`SwitchMgmt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config_revert_timer` | `int` | Optional | rollback timer for commit confirmed<br>**Default**: `10`<br>**Constraints**: `>= 1`, `<= 30` |
| `protect_re` | [`ProtectRe`](../../doc/models/protect-re.md) | Optional | restrict inbound-traffic to host<br>when enabled, all traffic that is not essential to our operation will be dropped<br>e.g. ntp / dns / traffic to mist will be allowed by default, if dhcpd is enabled, we'll make sure it works |
| `root_password` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "config_revert_timer": 10,
  "protect_re": {
    "allowed_services": [
      "allowed_services2",
      "allowed_services3",
      "allowed_services4"
    ],
    "custom": [
      {
        "port_range": "port_range9",
        "protocol": "any",
        "subnets": [
          "subnets2"
        ]
      },
      {
        "port_range": "port_range0",
        "protocol": "tcp",
        "subnets": [
          "subnets3",
          "subnets2",
          "subnets1"
        ]
      },
      {
        "port_range": "port_range1",
        "protocol": "udp",
        "subnets": [
          "subnets4",
          "subnets3"
        ]
      }
    ],
    "enabled": false,
    "trusted_hosts": [
      "trusted_hosts2"
    ]
  },
  "root_password": "root_password0"
}
```

