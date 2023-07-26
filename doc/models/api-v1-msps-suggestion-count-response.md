
# Api V1 Msps Suggestion Count Response

## Structure

`ApiV1MspsSuggestionCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`List of Result8`](../../doc/models/result-8.md) | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "distinct": "distinct6",
  "limit": 172,
  "results": [
    {
      "count": 143,
      "status": "status5"
    }
  ],
  "total": 10
}
```

