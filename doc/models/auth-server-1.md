
# Auth Server 1

## Structure

`AuthServer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Optional | ip / hostname of RADIUS server |
| `keywrap_enabled` | `bool` | Optional | if used for Mist APs, enable keywrap algorithm. Default is false |
| `keywrap_format` | [`KeywrapFormatEnum`](../../doc/models/keywrap-format-enum.md) | Optional | if used for Mist APs |
| `keywrap_kek` | `string` | Optional | if used for Mist APs, encryption key |
| `keywrap_mack` | `string` | Optional | if used for Mist APs, Message Authentication Code Key |
| `port` | `int` | Optional | Auth port of RADIUS server<br>**Default**: `1812` |
| `secret` | `string` | Optional | secret of RADIUS server |
| `ssids` | `List of string` | Optional | list of ssids that will use this server if match_ssid is true and match is found |

## Example (as JSON)

```json
{
  "port": 1812,
  "host": "host8",
  "keywrap_enabled": false,
  "keywrap_format": "hex",
  "keywrap_kek": "keywrap_kek6",
  "keywrap_mack": "keywrap_mack2"
}
```

