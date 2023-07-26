
# Rules 3

## Structure

`Rules3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | - |
| `name` | `string` | Optional | - |
| `port_config` | [`dict`](../../doc/models/junos-port-config.md) | Optional | - |

## Example (as JSON)

```json
{
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "name": "name0",
  "port_config": {
    "key0": {
      "ae_disable_lacp": false,
      "ae_idx": 250,
      "aggregated": false,
      "critical": false,
      "description": "description6",
      "usage": "usage2"
    },
    "key1": {
      "ae_disable_lacp": true,
      "ae_idx": 249,
      "aggregated": true,
      "critical": true,
      "description": "description5",
      "usage": "usage3"
    }
  }
}
```

