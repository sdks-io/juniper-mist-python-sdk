
# Vacm

## Structure

`Vacm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access` | [`List of Access`](../../doc/models/access.md) | Optional | - |
| `security_to_group` | [`SecurityToGroup`](../../doc/models/security-to-group.md) | Optional | - |

## Example (as JSON)

```json
{
  "access": [
    {
      "group_name": "group_name5",
      "prefix_list": [
        {
          "context_prefix": "context_prefix7",
          "notify_view": "notify_view1",
          "read_view": "read_view5",
          "security_level": "none",
          "security_model": "usm"
        },
        {
          "context_prefix": "context_prefix8",
          "notify_view": "notify_view2",
          "read_view": "read_view6",
          "security_level": "privacy",
          "security_model": "v1"
        }
      ]
    }
  ],
  "security_to_group": {
    "content": [
      {
        "group": "group2",
        "security_name": "security_name4"
      },
      {
        "group": "group3",
        "security_name": "security_name5"
      },
      {
        "group": "group4",
        "security_name": "security_name6"
      }
    ],
    "security_model": "v2c"
  }
}
```

