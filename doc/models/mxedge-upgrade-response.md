
# Mxedge Upgrade Response

## Structure

`MxedgeUpgradeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `counts` | [`Counts1`](../../doc/models/counts-1.md) | Required | - |
| `id` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `status` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `strategy` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `versions` | `object` | Required | - |

## Example (as JSON)

```json
{
  "channel": "channel4",
  "counts": {
    "failed": 166,
    "queued": 234,
    "success": 90,
    "upgrading": 112
  },
  "id": "id0",
  "status": "status8",
  "strategy": "strategy0",
  "versions": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

