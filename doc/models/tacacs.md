
# Tacacs

## Structure

`Tacacs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_servers` | [`List of AcctServer3`](../../doc/models/acct-server-3.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `network` | `string` | Optional | which network the TACACS server resides |
| `tacplus_servers` | [`List of TacplusServer1`](../../doc/models/tacplus-server-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "acct_servers": [
    {
      "host": "host1",
      "port": 15,
      "secret": "secret7",
      "timeout": 15
    }
  ],
  "enabled": false,
  "network": "network4",
  "tacplus_servers": [
    {
      "host": "host5",
      "port": 11,
      "secret": "secret9",
      "timeout": 11
    },
    {
      "host": "host6",
      "port": 12,
      "secret": "secret0",
      "timeout": 12
    }
  ]
}
```

