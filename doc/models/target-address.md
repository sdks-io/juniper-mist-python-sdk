
# Target Address

## Structure

`TargetAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Optional | - |
| `address_mask` | `string` | Optional | - |
| `port` | `int` | Optional | **Default**: `161` |
| `tag_list` | `string` | Optional | <refer to notify tag, can be multiple with blank |
| `target_address_name` | `string` | Optional | - |
| `target_parameters` | `string` | Optional | refer to notify target parameters name |

## Example (as JSON)

```json
{
  "address": "address",
  "address_mask": "address_mask",
  "port": 161,
  "target_address_name": "target_address_name",
  "tag_list": "tag_list8"
}
```

