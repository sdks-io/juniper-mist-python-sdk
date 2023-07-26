
# Stats Mxedge

## Structure

`StatsMxedge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpu_stat` | [`CpuStat3`](../../doc/models/cpu-stat-3.md) | Optional | CPU/core stats list |
| `created_time` | `int` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `ip_stat` | [`IpStat4`](../../doc/models/ip-stat-4.md) | Optional | OOBM IP stats |
| `lag_stat` | [`dict`](../../doc/models/lag-stat.md) | Optional | Stat for LAG (Link Aggregation Group). Property key is the LAG name |
| `last_seen` | `int` | Optional | - |
| `mac` | `string` | Optional | - |
| `memory_stat` | [`MemoryStat3`](../../doc/models/memory-stat-3.md) | Optional | Memory usage |
| `model` | `string` | Optional | - |
| `modified_time` | `int` | Optional | - |
| `mxagent_registered` | `bool` | Optional | - |
| `mxcluster_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | The name of the tunnel |
| `num_tunnels` | `int` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `port_stat` | [`dict`](../../doc/models/port-stat-1.md) | Optional | - |
| `sensor_stat` | `object` | Optional | - |
| `service_stat` | [`ServiceStat`](../../doc/models/service-stat.md) | Optional | stat for each services |
| `services` | `List of object` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `status` | `string` | Optional | - |
| `tunterm_id` | `uuid\|string` | Optional | - |
| `tunterm_ip_config` | [`TuntermIpConfig1`](../../doc/models/tunterm-ip-config-1.md) | Optional | - |
| `tunterm_port_config` | [`TuntermPortConfig1`](../../doc/models/tunterm-port-config-1.md) | Optional | - |
| `tunterm_registered` | `bool` | Optional | - |
| `tunterm_stat` | [`TuntermStat`](../../doc/models/tunterm-stat.md) | Optional | - |
| `uptime` | `int` | Optional | - |
| `virtualization_type` | `string` | Optional | Virtualization environment |

## Example (as JSON)

```json
{
  "cpu_stat": {
    "cpus": {
      "key0": {
        "idle": 212,
        "interrupt": 68,
        "system": 92,
        "usage": 34,
        "user": 216
      }
    },
    "idle": 224,
    "interrupt": 80,
    "system": 80,
    "usage": 46
  },
  "created_time": 118,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "ip_stat": {
    "ip": "ip0",
    "ips": {
      "key0": "ips0",
      "key1": "ips1",
      "key2": "ips2"
    },
    "macs": {
      "key0": "macs9"
    }
  }
}
```

