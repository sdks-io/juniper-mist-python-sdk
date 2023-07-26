
# Targets

## Structure

`Targets`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `downloaded` | `List of uuid\|string` | Optional | devices which have the firmware downloaded |
| `failed` | `List of uuid\|string` | Optional | devices which have the failed to upgrade |
| `reboot_in_progress` | `List of uuid\|string` | Optional | devices which are rebooting |
| `rebooted` | `List of uuid\|string` | Optional | devices which have rebooted successfully |
| `scheduled` | `List of uuid\|string` | Optional | devices which cloud has scheduled an upgrade |
| `skipped` | `List of uuid\|string` | Optional | devices which have skipped upgrade since requested version was same as running version. Use `force` to always upgrade |
| `upgraded` | `List of uuid\|string` | Optional | devices which have upgraded successfully |

## Example (as JSON)

```json
{
  "downloaded": [
    "00000eaa-0000-0000-0000-000000000000",
    "00000eab-0000-0000-0000-000000000000",
    "00000eac-0000-0000-0000-000000000000"
  ],
  "failed": [
    "00001eba-0000-0000-0000-000000000000",
    "00001ebb-0000-0000-0000-000000000000"
  ],
  "reboot_in_progress": [
    "00000aa3-0000-0000-0000-000000000000"
  ],
  "rebooted": [
    "0000136d-0000-0000-0000-000000000000",
    "0000136e-0000-0000-0000-000000000000",
    "0000136f-0000-0000-0000-000000000000"
  ],
  "scheduled": [
    "0000006d-0000-0000-0000-000000000000",
    "0000006e-0000-0000-0000-000000000000",
    "0000006f-0000-0000-0000-000000000000"
  ]
}
```

