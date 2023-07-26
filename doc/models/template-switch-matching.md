
# Template Switch Matching

Switch template

## Structure

`TemplateSwitchMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable` | `bool` | Optional | - |
| `rules` | [`List of Rules4`](../../doc/models/rules-4.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "enable": false,
  "rules": [
    {
      "additional_config_cmds": [
        "additional_config_cmds2"
      ],
      "match_role": "match_role4",
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
      },
      "switch_mgmt": {
        "ap_affinity_threshold": "ap_affinity_threshold4",
        "config_revert_timer": 24,
        "dhcp_option_fqdn": false,
        "mxedge_proxy_host": "mxedge_proxy_host2",
        "mxedge_proxy_port": 20
      }
    }
  ]
}
```

