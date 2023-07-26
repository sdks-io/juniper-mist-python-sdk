
# Devices Array Stats Site

## Structure

`DevicesArrayStatsSite`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ble_config` | [`BleConfig`](../../doc/models/ble-config.md) | Optional | - |
| `ble_stat` | [`BleStat`](../../doc/models/ble-stat.md) | Optional | - |
| `cert_expiry` | `float` | Optional | - |
| `env_stat` | [`EnvStat`](../../doc/models/env-stat.md) | Optional | device environment, including CPU temperature, Ambient temperature, Humidity, Attitude, Pressure, Accelerometers, Magnetometers and vCore Voltage |
| `esl_stat` | [`EslStat`](../../doc/models/esl-stat.md) | Optional | - |
| `ext_ip` | `string` | Optional | - |
| `fwupdate` | [`Fwupdate`](../../doc/models/fwupdate.md) | Optional | - |
| `iot_stat` | [`IotStat`](../../doc/models/iot-stat.md) | Optional | - |
| `ip` | `string` | Optional | IP address |
| `ip_config` | [`IpConfig`](../../doc/models/ip-config.md) | Optional | - |
| `ip_stat` | [`IpStat5`](../../doc/models/ip-stat-5.md) | Optional | - |
| `l_2_tp_stat` | [`dict`](../../doc/models/l2-tp-stat.md) | Optional | l2tp tunnel status (key is the wxtunnel_id) |
| `last_seen` | `float` | Optional | last seen timestamp |
| `last_trouble` | [`LastTrouble3`](../../doc/models/last-trouble-3.md) | Optional | last trouble code of switch |
| `led` | [`Led`](../../doc/models/led.md) | Optional | - |
| `lldp_stat` | [`LldpStat`](../../doc/models/lldp-stat.md) | Optional | LLDP Stat (neighbor information, power negotiations) |
| `locating` | `bool` | Optional | - |
| `locked` | `bool` | Optional | whether this AP is considered locked (placement / orientation has been vetted) |
| `mac` | `string` | Optional | device mac |
| `map_id` | `uuid\|string` | Optional | - |
| `mesh_downlinks` | [`dict`](../../doc/models/mesh-downlinks.md) | Optional | - |
| `mesh_uplink` | [`MeshUplink`](../../doc/models/mesh-uplink.md) | Optional | - |
| `model` | `string` | Optional | device model |
| `mount` | `string` | Optional | - |
| `name` | `string` | Optional | device name if configured |
| `num_clients` | [`NumClients1`](../../doc/models/num-clients-1.md) | Optional | how many wireless clients are currently connected |
| `port_stat` | [`dict`](../../doc/models/port-stat.md) | Optional | - |
| `power_budget` | `float` | Optional | in mW, surplus if positie or deficit if negative |
| `power_constrained` | `bool` | Optional | whether insufficient power |
| `power_opmode` | `string` | Optional | constrained mode |
| `power_src` | `string` | Optional | DC Input / PoE 802.3at / PoE 802.3af / LLDP / ? (unknown) |
| `radio_config` | [`RadioConfig`](../../doc/models/radio-config.md) | Optional | - |
| `radio_stat` | [`RadioStat`](../../doc/models/radio-stat.md) | Optional | a map of radio stats, key can be band_24 / band_5 |
| `rx_bps` | `float` | Optional | - |
| `rx_bytes` | `int` | Optional | - |
| `rx_pkts` | `int` | Optional | - |
| `serial` | `string` | Optional | serial |
| `status` | [`Status4Enum`](../../doc/models/status-4-enum.md) | Optional | - |
| `tx_bps` | `float` | Optional | - |
| `tx_bytes` | `float` | Optional | - |
| `tx_pkts` | `float` | Optional | - |
| `mtype` | `string` | Optional | device type, ap / ble |
| `uptime` | `float` | Optional | how long, in seconds, has the device been up (or rebooted) |
| `version` | `string` | Optional | - |
| `x` | `float` | Optional | - |
| `y` | `float` | Optional | - |
| `clients` | [`List of Client1`](../../doc/models/client-1.md) | Optional | - |
| `cpu_stat` | [`CpuStat1`](../../doc/models/cpu-stat-1.md) | Optional | - |
| `hostname` | `string` | Optional | hostname reported by the device |
| `if_stat` | [`dict`](../../doc/models/if-stat.md) | Optional | Property key is the interface name |
| `memory_stat` | [`MemoryStat4`](../../doc/models/memory-stat-4.md) | Optional | memory usage stat (for virtual chassis, memory usage of master RE) |
| `module_stat` | [`List of ModuleStat3`](../../doc/models/module-stat-3.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `cluster_stat` | [`dict`](../../doc/models/cluster-stat.md) | Optional | - |
| `cpu_2_stat` | `string` | Optional | - |
| `module_2_stat` | `string` | Optional | - |
| `spu_2_stat` | `string` | Optional | - |
| `spu_stat` | [`SpuStat`](../../doc/models/spu-stat.md) | Optional | - |

## Example (as JSON)

```json
{
  "mount": "faceup",
  "power_opmode": "[20] 6GHz(2x2) 5GHz(4x4) 2.4GHz(2x2).",
  "ble_config": {
    "beacon_rate": 110,
    "beacon_rate_model": "beacon_rate_model2",
    "beam_disabled": [
      113,
      114,
      115
    ],
    "power": 212,
    "power_mode": "power_mode6"
  },
  "ble_stat": {
    "beacon_rate": 78,
    "eddystone_uid_enabled": false,
    "eddystone_uid_freq_msec": 132,
    "eddystone_uid_instance": "eddystone_uid_instance6",
    "eddystone_uid_namespace": "eddystone_uid_namespace8"
  },
  "cert_expiry": 127.48,
  "env_stat": {
    "accel_x": 122.78,
    "accel_y": 222.08,
    "accel_z": 112.82,
    "ambient_temp": 66,
    "attitude": 104
  },
  "esl_stat": {
    "channel": 242,
    "connected": false,
    "type": "type2",
    "up": false
  }
}
```

