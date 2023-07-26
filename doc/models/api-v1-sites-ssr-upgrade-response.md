
# Api V1 Sites Ssr Upgrade Response

## Structure

`ApiV1SitesSsrUpgradeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `device_type` | `string` | Optional | - |
| `id` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `status` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `targets` | [`Targets1`](../../doc/models/targets-1.md) | Required | - |
| `versions` | `object` | Required | - |

## Example (as JSON)

```json
{
  "channel": "channel4",
  "device_type": "device_type0",
  "id": "id0",
  "status": "status8",
  "targets": {
    "failed": [
      "failed6"
    ],
    "queued": [
      "queued8"
    ],
    "success": [
      "success2",
      "success3",
      "success4"
    ],
    "upgrading": [
      "upgrading9"
    ]
  },
  "versions": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

