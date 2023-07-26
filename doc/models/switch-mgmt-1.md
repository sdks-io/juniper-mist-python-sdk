
# Switch Mgmt 1

## Structure

`SwitchMgmt1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_affinity_threshold` | `string` | Optional | - |
| `config_revert_timer` | `int` | Optional | **Default**: `10` |
| `dhcp_option_fqdn` | `bool` | Optional | Enable to provide the FQDN with DHCP option 81<br>**Default**: `False` |
| `mxedge_proxy_host` | `string` | Optional | - |
| `mxedge_proxy_port` | `int` | Optional | **Default**: `2222` |
| `use_mxedge_proxy` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "ap_affinity_threshold": "10",
  "config_revert_timer": 10,
  "dhcp_option_fqdn": false,
  "mxedge_proxy_port": 2222,
  "use_mxedge_proxy": false,
  "mxedge_proxy_host": "mxedge_proxy_host6"
}
```

