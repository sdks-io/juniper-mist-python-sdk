
# Mxtunnel

MxTunnel

## Structure

`Mxtunnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `anchor_mxtunnel_ids` | `List of uuid\|string` | Optional | list of anchor mxtunnels used for forming edge to edge tunnels |
| `auto_preemption` | [`AutoPreemption1`](../../doc/models/auto-preemption-1.md) | Optional | - |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `hello_interval` | `int` | Optional | in seconds, used as heartbeat to detect if a tunnel is alive. AP will try another peer after missing N hellos specified by `hello_retries`.<br>**Default**: `60`<br>**Constraints**: `>= 1`, `<= 300` |
| `hello_retries` | `int` | Optional | **Default**: `7`<br>**Constraints**: `>= 2`, `<= 30` |
| `id` | `uuid\|string` | Optional | - |
| `ipsec` | [`Ipsec`](../../doc/models/ipsec.md) | Optional | - |
| `modified_time` | `float` | Optional | - |
| `mtu` | `int` | Optional | 0 to enable PMTU, 552-1500 to start PMTU with a lower MTU<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 1500` |
| `mxcluster_ids` | `List of uuid\|string` | Optional | list of mxclusters to deploy this tunnel to |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `protocol` | [`Protocol3Enum`](../../doc/models/protocol-3-enum.md) | Optional | **Default**: `'udp'` |
| `site_id` | `uuid\|string` | Optional | - |
| `vlan_ids` | `List of int` | Optional | list of vlan_ids that will be used |

## Example (as JSON)

```json
{
  "hello_interval": 60,
  "hello_retries": 7,
  "mtu": 0,
  "protocol": "udp",
  "anchor_mxtunnel_ids": [
    "00001ad0-0000-0000-0000-000000000000",
    "00001ad1-0000-0000-0000-000000000000"
  ],
  "auto_preemption": {
    "day_of_week": "tue",
    "enabled": false,
    "time_of_day": "time_of_day4"
  },
  "created_time": 198.3,
  "for_site": false
}
```

