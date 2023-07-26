
# Api V1 Sites Count Response

## Structure

`ApiV1SitesCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `results` | [`List of Result29`](../../doc/models/result-29.md) | Required | **Constraints**: *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "results": [
    {
      "count": 143,
      "scope_id": "00002295-0000-0000-0000-000000000000"
    }
  ],
  "start": 212,
  "total": 10
}
```

