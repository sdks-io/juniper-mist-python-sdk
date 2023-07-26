
# Stats Device Gateway

Gateway statistics

## Structure

`StatsDeviceGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cluster_stat` | [`dict`](../../doc/models/cluster-stat.md) | Optional | - |
| `cpu_2_stat` | `string` | Optional | - |
| `cpu_stat` | [`CpuStat`](../../doc/models/cpu-stat.md) | Optional | - |
| `hostname` | `string` | Optional | hostname reported by the device |
| `ip` | `string` | Optional | IP address |
| `ip_stat` | [`IpStat1`](../../doc/models/ip-stat-1.md) | Optional | - |
| `last_seen` | `float` | Optional | last seen timestamp |
| `mac` | `string` | Required | device mac |
| `memory_stat` | [`MemoryStat`](../../doc/models/memory-stat.md) | Optional | - |
| `model` | `string` | Optional | device model |
| `module_2_stat` | `string` | Optional | - |
| `module_stat` | [`List of ModuleStat`](../../doc/models/module-stat.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `name` | `string` | Optional | device name if configured |
| `serial` | `string` | Optional | serial |
| `spu_2_stat` | `string` | Optional | - |
| `spu_stat` | [`SpuStat`](../../doc/models/spu-stat.md) | Optional | - |
| `status` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `uptime` | `float` | Optional | - |
| `version` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "cluster_stat": {
    "key0": {
      "status": "status0"
    }
  },
  "cpu2_stat": "cpu2_stat2",
  "cpu_stat": {
    "idle": 102.08,
    "interrupt": 215.84,
    "load_avg": [
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "system": 13.6,
    "user": 204.52
  },
  "hostname": "hostname4",
  "ip": "ip4",
  "mac": "mac4"
}
```

