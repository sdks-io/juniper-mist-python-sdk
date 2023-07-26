
# Coa Server 1

## Structure

`CoaServer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disable_event_timestamp_check` | `bool` | Optional | whether to disable Event-Timestamp Check<br>**Default**: `False` |
| `enabled` | `bool` | Optional | - |
| `host` | `string` | Optional | this server configured to send CoA\|DM to mist edges |
| `port` | `int` | Optional | mist edges will allow this host on this port<br>**Default**: `3799` |
| `secret` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "disable_event_timestamp_check": false,
  "port": 3799,
  "enabled": false,
  "host": "host8",
  "secret": "secret4"
}
```

