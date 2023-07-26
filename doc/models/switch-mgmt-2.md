
# Switch Mgmt 2

## Structure

`SwitchMgmt2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config_revert` | `int` | Optional | **Default**: `10` |
| `protect_re` | [`ProtectRe1`](../../doc/models/protect-re-1.md) | Optional | - |
| `root_password` | `string` | Optional | - |
| `tacacs` | [`Tacacs2`](../../doc/models/tacacs-2.md) | Optional | - |

## Example (as JSON)

```json
{
  "config_revert": 10,
  "protect_re": {
    "enabled": false
  },
  "root_password": "root_password0",
  "tacacs": {
    "acct_servers": [
      {
        "host": "host7",
        "port": "port1",
        "secret": "secret3",
        "timeout": 223
      },
      {
        "host": "host8",
        "port": "port0",
        "secret": "secret4",
        "timeout": 222
      }
    ],
    "enabled": false,
    "network": "network6",
    "tacplus_servers": [
      {
        "host": "host3",
        "port": "port1",
        "secret": "secret7",
        "timeout": 185
      }
    ]
  }
}
```

