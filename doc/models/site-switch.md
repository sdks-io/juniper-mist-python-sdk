
# Site Switch

Switch site settings

## Structure

`SiteSwitch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_affinity_threshold` | `int` | Optional | ap_affinity_threshold ap_affinity_threshold can be added as a field under site/setting. By default this value is set to 12. If the field is set in both site/setting and org/setting, the value from site/setting will be used.<br>**Default**: `10` |
| `config_revert_timer` | `float` | Optional | the rollback timer for commit confirmed<br>**Default**: `10`<br>**Constraints**: `>= 1`, `<= 30` |
| `dhcp_option_fqdn` | `bool` | Optional | Enable to provide the FQDN with DHCP option 81<br>**Default**: `False` |
| `mxedge_proxy_host` | `string` | Optional | - |
| `mxedge_proxy_port` | `int` | Optional | **Default**: `2222` |
| `protect_re` | [`ProtectRe2`](../../doc/models/protect-re-2.md) | Optional | restrict inbound-traffic to host  (draft) |
| `root_password` | `string` | Optional | - |
| `tacacs` | [`Tacacs`](../../doc/models/tacacs.md) | Optional | - |
| `use_mxedge_proxy` | `bool` | Optional | to use mxedge as proxy |

## Example (as JSON)

```json
{
  "ap_affinity_threshold": 10,
  "config_revert_timer": 10.0,
  "dhcp_option_fqdn": false,
  "mxedge_proxy_port": 2222,
  "mxedge_proxy_host": "mxedge_proxy_host6"
}
```

