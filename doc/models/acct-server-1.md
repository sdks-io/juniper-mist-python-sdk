
# Acct Server 1

## Structure

`AcctServer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Optional | ip / hostname of RADIUS server |
| `port` | `int` | Optional | Acct port of RADIUS server<br>**Default**: `1813` |
| `secret` | `string` | Optional | secret of RADIUS server |
| `ssids` | `List of string` | Optional | list of ssids that will use this server if match_ssid is true and match is found |

## Example (as JSON)

```json
{
  "port": 1813,
  "host": "host8",
  "secret": "secret4",
  "ssids": [
    "ssids9",
    "ssids0"
  ]
}
```

