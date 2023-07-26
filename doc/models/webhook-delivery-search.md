
# Webhook Delivery Search

## Structure

`WebhookDeliverySearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`List of WebhookDelivery`](../../doc/models/webhook-delivery.md) | Optional | - |
| `start` | `int` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 1688035193,
  "limit": 10,
  "start": 1687948793,
  "results": [
    {
      "error": "error7",
      "id": "00000a0d-0000-0000-0000-000000000000",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "req_headers": "req_headers3",
      "req_payload": "req_payload1"
    }
  ],
  "total": 10
}
```

