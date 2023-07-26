
# V2 C Config

## Structure

`V2cConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `string` | Optional | - |
| `client_list_name` | `string` | Optional | client_list_name here should refer to client_list above |
| `community_name` | `string` | Optional | - |
| `view` | `string` | Optional | view name here should be defined in views above |

## Example (as JSON)

```json
{
  "authorization": "read-only",
  "client_list_name": "clist-1",
  "community_name": "abc123",
  "view": "all"
}
```

