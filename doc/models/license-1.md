
# License 1

## Structure

`License1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `end_time` | `int` | Optional | end date of the license term |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `order_id` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `quantity` | `int` | Optional | number of devices entitled for this license |
| `remaining_quantity` | `int` | Optional | Number of licences left in this subscription |
| `start_time` | `int` | Optional | start date of the license term |
| `subscription_id` | `string` | Optional | - |
| `mtype` | [`Type28Enum`](../../doc/models/type-28-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "end_time": 96,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "order_id": "order_id6"
}
```

