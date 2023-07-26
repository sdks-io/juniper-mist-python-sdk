
# Orggroups Search

## Structure

`OrggroupsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `page` | `int` | Required | - |
| `results` | [`List of Result6`](../../doc/models/result-6.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "limit": 172,
  "page": 30,
  "results": [
    {
      "id": "00000a0d-0000-0000-0000-000000000000",
      "text": "text7",
      "type": "type7"
    }
  ],
  "total": 10,
  "next": "next2"
}
```

