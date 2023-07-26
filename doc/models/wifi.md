
# Wifi

## Structure

`Wifi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cisco_enabled` | `bool` | Optional | - |
| `disable_11_k` | `bool` | Optional | **Default**: `False` |
| `disable_radios_when_power_constrained` | `bool` | Optional | - |
| `enable_arp_spoof` | `bool` | Optional | - |
| `enable_shared_radio_scanning` | `bool` | Optional | **Default**: `False` |
| `enabled` | `bool` | Optional | **Default**: `True` |
| `locate_connected` | `bool` | Optional | **Default**: `False` |
| `locate_unconnected` | `bool` | Optional | **Default**: `False` |
| `mesh_allow_dfs` | `bool` | Optional | **Default**: `False` |
| `mesh_enable_crm` | `bool` | Optional | - |
| `mesh_enabled` | `bool` | Optional | - |
| `proxy_arp` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "disable_11k": false,
  "enable_shared_radio_scanning": false,
  "enabled": true,
  "locate_connected": false,
  "locate_unconnected": false,
  "mesh_allow_dfs": false,
  "proxy_arp": false,
  "cisco_enabled": false,
  "disable_radios_when_power_constrained": false,
  "enable_arp_spoof": false
}
```

