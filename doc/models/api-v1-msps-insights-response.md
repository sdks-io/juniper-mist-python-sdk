
# Api V1 Msps Insights Response

## Structure

`ApiV1MspsInsightsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `interval` | `float` | Required | - |
| `limit` | `float` | Required | - |
| `results` | `List of object` | Required | **Constraints**: *Unique Items Required* |
| `start` | `float` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "interval": 154.52,
  "limit": 237.24,
  "results": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "start": 224.84
}
```

