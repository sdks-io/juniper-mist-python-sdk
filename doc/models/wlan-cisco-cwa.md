
# Wlan Cisco Cwa

Cisco CWA (central web authentication) required RADIUS with COA in order to work. See CWA: https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine/115732-central-web-auth-00.html

## Structure

`WlanCiscoCwa`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_hostnames` | `List of string` | Optional | list of hostnames without http(s):// (matched by substring) |
| `allowed_subnets` | `List of string` | Optional | list of CIDRs |
| `blocked_subnets` | `List of string` | Optional | list of blocked CIDRs |
| `enabled` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "enabled": false,
  "allowed_hostnames": [
    "allowed_hostnames0",
    "allowed_hostnames1",
    "allowed_hostnames2"
  ],
  "allowed_subnets": [
    "allowed_subnets6"
  ],
  "blocked_subnets": [
    "blocked_subnets2",
    "blocked_subnets3",
    "blocked_subnets4"
  ]
}
```

