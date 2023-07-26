
# Device Upgrade Response

## Structure

`DeviceUpgradeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counts` | [`Counts`](../../doc/models/counts.md) | Optional | - |
| `current_phase` | `int` | Optional | current canary or rrm phase in progress |
| `enable_p_2_p` | `bool` | Optional | whether to allow local AP-to-AP FW upgrade |
| `force` | `bool` | Optional | whether to force upgrade when requested version is same as running version |
| `id` | `uuid\|string` | Required | unique id for the upgrade |
| `max_failure_percentage` | `int` | Optional | percentage of failures allowed |
| `max_failures` | `List of int` | Optional | number of failures allowed within a canary phase or serial rollout |
| `reboot_at` | `int` | Optional | reboot start time in epoch |
| `start_time` | `float` | Optional | firmware download start time in epoch |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | status upgrade is in |
| `strategy` | [`Strategy1Enum`](../../doc/models/strategy-1-enum.md) | Optional | upgrade strategy<br>**Default**: `'big_bang'`<br>**Constraints**: *Minimum Length*: `1` |
| `target_version` | `string` | Optional | version to upgrade to<br>**Constraints**: *Minimum Length*: `1` |
| `upgrade_plan` | `object` | Optional | a dictionary of rrm phase number to devices part of that phase |

## Example (as JSON)

```json
{
  "id": "00001770-0000-0000-0000-000000000000",
  "strategy": "big_bang",
  "counts": {
    "download_requested": 138,
    "downloaded": 70,
    "failed": 166,
    "reboot_in_progress": 88,
    "rebooted": 76
  },
  "current_phase": 74,
  "enable_p2p": false,
  "force": false,
  "max_failure_percentage": 208
}
```

