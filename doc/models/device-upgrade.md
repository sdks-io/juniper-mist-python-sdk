
# Device Upgrade

## Structure

`DeviceUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `canary_phases` | `List of int` | Optional | phases for canary deployment. Each phase represents percentage of AP’s that need to be upgraded. default is [1, 10, 50, 100] |
| `device_ids` | `List of string` | Optional | - |
| `enable_p_2_p` | `bool` | Optional | whether to allow local AP-to-AP FW upgrade |
| `force` | `bool` | Optional | true will force upgrade when requested version is same as running version<br>**Default**: `False` |
| `max_failure_percentage` | `float` | Optional | percentage of failures allowed across the entire upgrade(not applicable for `big_bang`)<br>**Default**: `5`<br>**Constraints**: `>= 0`, `<= 100` |
| `max_failures` | `List of int` | Optional | number of failures allowed within each phase(applicable for `canary` or `rrm`). Will be used if provided, else max_failure_percentage will be used |
| `models` | `List of string` | Optional | - |
| `p_2_p_cluster_size` | `int` | Optional | **Default**: `10`<br>**Constraints**: `>= 0` |
| `p_2_p_parallelism` | `int` | Optional | number of parallel p2p download batches to creat |
| `reboot` | `bool` | Optional | Reboot device immediately after upgrade is completed (Available on Junos OS devices)<br>**Default**: `False` |
| `reboot_at` | `float` | Optional | reboot start time in epoch seconds, default is `start_time` |
| `rrm_first_batch_percentage` | `int` | Optional | percentage of AP’s that need to be present in the first rrm batch |
| `rrm_max_batch_percentage` | `int` | Optional | max percentage of AP’s that need to be present in each rrm batch |
| `rrm_mesh_upgrade` | `string` | Optional | sequential or parallel (default parallel). Whether to upgrade mesh AP’s parallelly or sequentially at the end of the upgrade |
| `rrm_node_order` | [`RrmNodeOrderEnum`](../../doc/models/rrm-node-order-enum.md) | Optional | Used in rrm to determine whether to start upgrade from fringe or center AP’s<br>**Default**: `'fringe_to_center'` |
| `rrm_slow_ramp` | `bool` | Optional | true will make rrm batch sizes slowly ramp up |
| `snapshot` | `bool` | Optional | Perform recovery snapshot after device is rebooted (Available on Junos OS devices)<br>**Default**: `False` |
| `start_time` | `float` | Optional | upgrade start time in epoch seconds, default is now |
| `strategy` | [`StrategyEnum`](../../doc/models/strategy-enum.md) | Optional | `big_bang` (upgrade all at once), `serial` (one at a time), `canary` or `rrm`<br>**Default**: `'big_bang'`<br>**Constraints**: *Minimum Length*: `1` |
| `version` | `string` | Optional | specific version / stable<br>**Default**: `'latest'`<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "canary_phases": [
    215,
    216
  ],
  "force": false,
  "max_failure_percentage": 5.0,
  "p2p_cluster_size": 0,
  "reboot": false,
  "reboot_at": 1624399840,
  "rrm_first_batch_percentage": 2,
  "rrm_max_batch_percentage": 10,
  "rrm_node_order": "fringe_to_center",
  "snapshot": false,
  "start_time": 1624399840,
  "strategy": "big_bang",
  "version": "3.1.5",
  "device_ids": [
    "device_ids9",
    "device_ids0"
  ],
  "enable_p2p": false
}
```

