
# Tacacs 2

## Structure

`Tacacs2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_servers` | [`List of AcctServer2`](../../doc/models/acct-server-2.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `network` | `string` | Optional | - |
| `tacplus_servers` | [`List of TacplusServer`](../../doc/models/tacplus-server.md) | Optional | - |

## Example (as JSON)

```json
{
  "acct_servers": [
    {
      "host": "host1",
      "port": "port7",
      "secret": "secret7",
      "timeout": 15
    }
  ],
  "enabled": false,
  "network": "network4",
  "tacplus_servers": [
    {
      "host": "host5",
      "port": "port3",
      "secret": "secret9",
      "timeout": 11
    },
    {
      "host": "host6",
      "port": "port4",
      "secret": "secret0",
      "timeout": 12
    }
  ]
}
```

