
# Counts

## Structure

`Counts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `download_requested` | `int` | Optional | count of devices which cloud has requested to download firmware |
| `downloaded` | `int` | Optional | count of ap’s which have the firmware downloaded |
| `failed` | `int` | Optional | count of devices which have failed to upgrade |
| `reboot_in_progress` | `int` | Optional | count of devices which are rebooting |
| `rebooted` | `int` | Optional | count of devices which have rebooted successfully |
| `scheduled` | `int` | Optional | count of devices which cloud has scheduled an upgrade for |
| `skipped` | `int` | Optional | count of devices which skipped upgrade since requested version was same as running version. Use force to always upgrade |
| `total` | `int` | Optional | count of devices part of this upgrade |
| `upgraded` | `int` | Optional | count of devices which have upgraded successfully |

## Example (as JSON)

```json
{
  "download_requested": 152,
  "downloaded": 84,
  "failed": 180,
  "reboot_in_progress": 102,
  "rebooted": 62
}
```

