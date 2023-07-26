
# Orgs Search

## Structure

`OrgsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result5`](../../doc/models/result-5.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "results": [
    {
      "msp_id": "00000809-0000-0000-0000-000000000000",
      "name": "name3",
      "num_aps": 57,
      "num_gateways": 195,
      "num_sites": 133
    }
  ],
  "start": 224.84,
  "total": 10,
  "next": "next2"
}
```

