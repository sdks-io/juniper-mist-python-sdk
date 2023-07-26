
# Junos Port Usages Dynamic

This is a special mode where the actually usage is determined by a set of rules the port will start with `access` mode and isolated depending on the rules, if resolved, the port will have the resolved usage applied.

## Structure

`JunosPortUsagesDynamic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | `string` | Required, Constant | **Default**: `'dynamic'` |
| `reset_default_when` | [`ResetDefaultWhenEnum`](../../doc/models/reset-default-when-enum.md) | Optional | Control when the DPC port should be changed to the default port usage<br>Configuring to none will let the DPC port keep at the current port usage.<br>**Default**: `'link_down'` |
| `rules` | [`List of Rules2`](../../doc/models/rules-2.md) | Optional | - |

## Example (as JSON)

```json
{
  "mode": "dynamic",
  "reset_default_when": "link_down",
  "rules": [
    {
      "equals": "equals6",
      "equals_any": [
        "equals_any7",
        "equals_any8",
        "equals_any9"
      ],
      "expression": "expression8",
      "src": "lldp_chassis_id",
      "usage": "usage2"
    }
  ]
}
```

