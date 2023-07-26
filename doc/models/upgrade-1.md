
# Upgrade 1

## Structure

`Upgrade1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `start_time` | `int` | Optional | upgrade start time in epoch |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Optional | status upgrade is in |
| `targets` | [`Targets`](../../doc/models/targets.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "00001770-0000-0000-0000-000000000000",
  "start_time": 120,
  "status": "created",
  "targets": {
    "downloaded": [
      "00001716-0000-0000-0000-000000000000",
      "00001717-0000-0000-0000-000000000000",
      "00001718-0000-0000-0000-000000000000"
    ],
    "failed": [
      "0000191a-0000-0000-0000-000000000000"
    ],
    "reboot_in_progress": [
      "0000232b-0000-0000-0000-000000000000",
      "0000232c-0000-0000-0000-000000000000"
    ],
    "rebooted": [
      "00000861-0000-0000-0000-000000000000"
    ],
    "scheduled": [
      "00001b97-0000-0000-0000-000000000000",
      "00001b96-0000-0000-0000-000000000000"
    ]
  }
}
```

