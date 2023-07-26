
# Security to Group

## Structure

`SecurityToGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | [`List of Content1`](../../doc/models/content-1.md) | Optional | - |
| `security_model` | [`SecurityModelEnum`](../../doc/models/security-model-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "content": [
    {
      "group": "group4",
      "security_name": "security_name4"
    },
    {
      "group": "group5",
      "security_name": "security_name3"
    },
    {
      "group": "group6",
      "security_name": "security_name2"
    }
  ],
  "security_model": "v2c"
}
```

