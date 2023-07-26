
# Auto Device Naming

## Structure

`AutoDeviceNaming`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable` | `bool` | Optional | - |
| `rules` | [`List of OrgAutoRules`](../../doc/models/org-auto-rules.md) | Optional | - |

## Example (as JSON)

```json
{
  "enable": false,
  "rules": [
    {
      "expression": "expression8",
      "model": "model8",
      "prefix": "prefix2",
      "src": "model",
      "subnet": "subnet2",
      "suffix": "suffix6"
    }
  ]
}
```

