
# Radsec 1

## Structure

`Radsec1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_servers` | [`List of AcctServer`](../../doc/models/acct-server.md) | Optional | - |
| `auth_servers` | [`List of AuthServer`](../../doc/models/auth-server.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `use_mxedge` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "acct_servers": [
    {
      "host": "host1",
      "keywrap_enabled": true,
      "keywrap_format": "keywrap_format5",
      "keywrap_kek": "keywrap_kek3",
      "keywrap_mack": "keywrap_mack5",
      "port": 15,
      "secret": "secret7"
    }
  ],
  "auth_servers": [
    {
      "host": "host9",
      "keywrap_enabled": true,
      "keywrap_format": "keywrap_format3",
      "keywrap_kek": "keywrap_kek5",
      "keywrap_mack": "keywrap_mack7",
      "port": 73,
      "secret": "secret5"
    }
  ],
  "enabled": false,
  "use_mxedge": false
}
```

