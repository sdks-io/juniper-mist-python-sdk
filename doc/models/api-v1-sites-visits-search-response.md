
# Api V1 Sites Visits Search Response

## Structure

`ApiV1SitesVisitsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Required | - |
| `results` | [`List of Result30`](../../doc/models/result-30.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "next": "next2",
  "results": [
    {
      "enter": 143,
      "scope": "scope9",
      "timestamp": 63.09,
      "user": "user3"
    }
  ],
  "start": 224.84,
  "total": 10
}
```

