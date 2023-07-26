
# Count

## Structure

`Count`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `results` | [`List of Result4`](../../doc/models/result-4.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "distinct": "distinct6",
  "end": 254,
  "limit": 172,
  "results": [
    {
      "count": 143
    }
  ],
  "start": 212,
  "total": 10
}
```

