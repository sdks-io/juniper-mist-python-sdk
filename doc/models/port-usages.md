
# Port Usages

The property key is the port profile name

## Structure

`PortUsages`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dynamic` | [`JunosPortUsagesDynamic`](../../doc/models/junos-port-usages-dynamic.md) | Optional | This is a special mode where the actually usage is determined by a set of rules the port will start with `access` mode and isolated depending on the rules, if resolved, the port will have the resolved usage applied. |

## Example (as JSON)

```json
{
  "dynamic": {
    "mode": "mode8",
    "reset_default_when": "none",
    "rules": [
      {
        "equals": "equals2",
        "equals_any": [
          "equals_any3",
          "equals_any4"
        ],
        "expression": "expression4",
        "src": "radius_username",
        "usage": "usage6"
      },
      {
        "equals": "equals1",
        "equals_any": [
          "equals_any2"
        ],
        "expression": "expression3",
        "src": "lldp_oui",
        "usage": "usage7"
      }
    ]
  }
}
```

