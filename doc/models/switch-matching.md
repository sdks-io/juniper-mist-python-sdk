
# Switch Matching

## Structure

`SwitchMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | additional CLI commands to append if this rule matches<br>NOTE: no check is done |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `rules` | [`List of Rules6`](../../doc/models/rules-6.md) | Optional | - |

## Example (as JSON)

```json
{
  "enabled": false,
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "rules": [
    {
      "additionalProperty": "additionalProperty2",
      "match_model": "match_model6",
      "name": "name4",
      "port_config": {
        "key0": {
          "usage": "usage8"
        },
        "key1": {
          "usage": "usage9"
        }
      }
    }
  ]
}
```

