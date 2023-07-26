
# Mxagent

## Structure

`Mxagent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ext_ip` | `string` | Optional | external IP from ep-terminator’s point of view. valid only for service having its own cloud connection |
| `last_seen` | `int` | Optional | timestamp when the last stats is seen (cloud unix time, in second). valid only for service having its own stats or whole system (last among last_seen of all services) |
| `package_state` | `string` | Optional | package/service installation state. |
| `package_version` | `string` | Optional | package/service installation state. |
| `running_state` | `string` | Optional | service running state. |
| `uptime` | `int` | Optional | service uptime. |

## Example (as JSON)

```json
{
  "ext_ip": "ext_ip2",
  "last_seen": 42,
  "package_state": "package_state4",
  "package_version": "package_version2",
  "running_state": "running_state8"
}
```

