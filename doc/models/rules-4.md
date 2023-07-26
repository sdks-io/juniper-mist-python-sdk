
# Rules 4

## Structure

`Rules4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | - |
| `match_role` | `string` | Optional | role to match |
| `name` | `string` | Optional | - |
| `port_config` | [`dict`](../../doc/models/junos-port-config.md) | Optional | - |
| `switch_mgmt` | [`SwitchMgmt1`](../../doc/models/switch-mgmt-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "match_role": "match_role0",
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
  },
  "switch_mgmt": {
    "ap_affinity_threshold": "ap_affinity_threshold0",
    "config_revert_timer": 188,
    "dhcp_option_fqdn": false,
    "mxedge_proxy_host": "mxedge_proxy_host8",
    "mxedge_proxy_port": 184
  }
}
```

