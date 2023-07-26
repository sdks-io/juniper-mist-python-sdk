
# Service Stat

stat for each services

## Structure

`ServiceStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mxagent` | [`Mxagent`](../../doc/models/mxagent.md) | Optional | - |
| `tunterm` | [`Tunterm`](../../doc/models/tunterm.md) | Optional | - |

## Example (as JSON)

```json
{
  "mxagent": {
    "ext_ip": "ext_ip6",
    "last_seen": 52,
    "package_state": "package_state2",
    "package_version": "package_version0",
    "running_state": "running_state0"
  },
  "tunterm": {
    "ext_ip": "ext_ip8",
    "last_seen": 122,
    "package_state": "package_state4",
    "package_version": "package_version2",
    "running_state": "running_state2"
  }
}
```

