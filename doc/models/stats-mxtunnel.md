
# Stats Mxtunnel

MxTunnels statistics

## Structure

`StatsMxtunnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `last_seen` | `int` | Optional | - |
| `mxcluster_id` | `uuid\|string` | Optional | - |
| `mxedge_id` | `uuid\|string` | Optional | - |
| `mxtunnel_id` | `uuid\|string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `peer_mxedge_id` | `uuid\|string` | Optional | MxEdge ID of the peer(mist edge to mist edge tunnel) |
| `remote_ip` | `string` | Optional | - |
| `remote_port` | `int` | Optional | - |
| `rx_control_pkts` | `int` | Optional | - |
| `sessions` | [`List of Sessions1`](../../doc/models/sessions-1.md) | Optional | list of sessions<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `site_id` | `uuid\|string` | Optional | - |
| `state` | [`State1Enum`](../../doc/models/state-1-enum.md) | Optional | idle / wait-ctrl-reply / wait-ctrl-conn / established / established_with_sessions |
| `tx_control_pkts` | `int` | Optional | - |
| `uptime` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "for_site": false,
  "last_seen": 42,
  "mxcluster_id": "00001040-0000-0000-0000-000000000000",
  "mxedge_id": "00000f74-0000-0000-0000-000000000000"
}
```

