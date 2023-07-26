
# Access

## Structure

`Access`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_name` | `string` | Optional | - |
| `prefix_list` | [`List of PrefixList`](../../doc/models/prefix-list.md) | Optional | - |

## Example (as JSON)

```json
{
  "group_name": "group_name6",
  "prefix_list": [
    {
      "context_prefix": "context_prefix6",
      "notify_view": "notify_view0",
      "read_view": "read_view4",
      "security_level": "none",
      "security_model": "v1"
    },
    {
      "context_prefix": "context_prefix7",
      "notify_view": "notify_view1",
      "read_view": "read_view5",
      "security_level": "privacy",
      "security_model": "v2c"
    }
  ]
}
```

