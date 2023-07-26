
# Template Gateway Matching

Gateway matching

## Structure

`TemplateGatewayMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable` | `bool` | Optional | - |
| `rules` | [`List of Rules3`](../../doc/models/rules-3.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "enable": false,
  "rules": [
    {
      "additional_config_cmds": [
        "additional_config_cmds2"
      ],
      "name": "name4",
      "port_config": {
        "key0": {
          "ae_disable_lacp": false,
          "ae_idx": 86,
          "aggregated": false,
          "critical": false,
          "description": "description0",
          "usage": "usage8"
        },
        "key1": {
          "ae_disable_lacp": true,
          "ae_idx": 85,
          "aggregated": true,
          "critical": true,
          "description": "description9",
          "usage": "usage9"
        }
      }
    }
  ]
}
```

