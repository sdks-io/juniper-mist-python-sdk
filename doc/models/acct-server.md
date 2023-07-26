
# Acct Server

## Structure

`AcctServer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Required | ip / hostname of RADIUS server |
| `keywrap_enabled` | `bool` | Optional | - |
| `keywrap_format` | `string` | Optional | - |
| `keywrap_kek` | `string` | Optional | - |
| `keywrap_mack` | `string` | Optional | - |
| `port` | `int` | Required | Acct port of RADIUS server<br>**Default**: `1813` |
| `secret` | `string` | Required | secret of RADIUS server |

## Example (as JSON)

```json
{
  "host": "host8",
  "port": 1813,
  "secret": "secret4",
  "keywrap_enabled": false,
  "keywrap_format": "keywrap_format2",
  "keywrap_kek": "keywrap_kek6",
  "keywrap_mack": "keywrap_mack2"
}
```

