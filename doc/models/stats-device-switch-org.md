
# Stats Device Switch Org

Switch statistics

## Structure

`StatsDeviceSwitchOrg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpu_stat` | [`CpuStat1`](../../doc/models/cpu-stat-1.md) | Optional | - |
| `hostname` | `string` | Optional | hostname reported by the device |
| `if_stat` | [`dict`](../../doc/models/if-stat.md) | Optional | Property key is the interface name |
| `ip` | `string` | Optional | - |
| `ip_stat` | [`IpStat2`](../../doc/models/ip-stat-2.md) | Optional | - |
| `last_seen` | `float` | Optional | - |
| `last_trouble` | [`LastTrouble1`](../../doc/models/last-trouble-1.md) | Optional | last trouble code of switch |
| `mac` | `string` | Optional | - |
| `memory_stat` | [`MemoryStat1`](../../doc/models/memory-stat-1.md) | Optional | memory usage stat (for virtual chassis, memory usage of master RE) |
| `model` | `string` | Optional | - |
| `module_stat` | [`List of ModuleStat1`](../../doc/models/module-stat-1.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `name` | `string` | Optional | device name if configured |
| `serial` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `uptime` | `float` | Optional | - |
| `version` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "cpu_stat": {
    "idle": 224,
    "interrupt": 80,
    "load_avg": [
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "system": 80,
    "user": 228
  },
  "hostname": "hostname4",
  "if_stat": {
    "key0": {
      "ips": [
        "ips1",
        "ips2"
      ],
      "port_id": "port_id7",
      "rx_bytes": 195,
      "rx_pkts": 253,
      "tx_bytes": 77
    }
  },
  "ip": "ip4",
  "ip_stat": {
    "dns": [
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "dns_suffix": [
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "gateway": "gateway6",
    "gateway6": "gateway62",
    "ip": "ip0"
  }
}
```

