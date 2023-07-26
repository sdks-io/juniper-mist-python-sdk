
# L2 Tp Stat

the property key is the L2TP tunnel id

## Structure

`L2tpStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sessions` | [`List of Session`](../../doc/models/session.md) | Optional | list of sessions<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `state` | `string` | Optional | idle / wait-ctrl-reply / wait-ctrl-conn / established / established_with_sessions |
| `uptime` | `int` | Optional | uptime |
| `wxtunnel_id` | `uuid\|string` | Optional | WxlanTunnel ID |

## Example (as JSON)

```json
{
  "sessions": [
    {
      "local_sid": 106,
      "remote_id": "remote_id0",
      "remote_sid": 186,
      "state": "state2"
    },
    {
      "local_sid": 107,
      "remote_id": "remote_id1",
      "remote_sid": 185,
      "state": "state1"
    },
    {
      "local_sid": 108,
      "remote_id": "remote_id2",
      "remote_sid": 184,
      "state": "state0"
    }
  ],
  "state": "state4",
  "uptime": 50,
  "wxtunnel_id": "00001f68-0000-0000-0000-000000000000"
}
```

