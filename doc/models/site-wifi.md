
# Site Wifi

Wi-Fi site settings

## Structure

`SiteWifi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cisco_enabled` | `bool` | Optional | - |
| `disable_11_k` | `bool` | Optional | whether to disable 11k<br>**Default**: `False` |
| `disable_radios_when_power_constrained` | `bool` | Optional | - |
| `enable_arp_spoof_check` | `bool` | Optional | when proxy_arp is enabled, check for arp spoofing.<br>**Default**: `False` |
| `enable_channel_144` | `bool` | Optional | whether to enable channel 144 (some older clients may not support it)<br>**Default**: `False` |
| `enable_shared_radio_scanning` | `bool` | Optional | - |
| `enable_vna` | `bool` | Optional | enable Virtual Network Assistant (using SUB-VNA license)<br>**Default**: `False` |
| `enabled` | `bool` | Optional | enable WIFI feature (using SUB-MAN license)<br>**Default**: `True` |
| `locate_connected` | `bool` | Optional | whether to locate connected clients<br>**Default**: `False` |
| `locate_unconnected` | `bool` | Optional | whether to locate unconnected clients<br>**Default**: `False` |
| `mesh_allow_dfs` | `bool` | Optional | whether to allow Mesh to use DFS channels. For DFS channels, Remote Mesh AP would have to do CAC when scanning for new Base AP, which is slow and will distrupt the connection. If roaming is desired, keep it disabled.<br>**Default**: `False` |
| `mesh_enable_crm` | `bool` | Optional | used to enable/disable CRM |
| `mesh_enabled` | `bool` | Optional | whether to enable Mesh feature for the site<br>**Default**: `False` |
| `mesh_psk` | `string` | Optional | optional passphrase of mesh networking, default is generated randomly |
| `mesh_ssid` | `string` | Optional | optional ssid of mesh networking, default is based on site_id |
| `proxy_arp` | [`ProxyArpEnum`](../../doc/models/proxy-arp-enum.md) | Optional | default / enabled / disabled |

## Example (as JSON)

```json
{
  "disable_11k": false,
  "enable_arp_spoof_check": false,
  "enable_channel_144": false,
  "enable_vna": false,
  "enabled": true,
  "locate_connected": false,
  "locate_unconnected": false,
  "mesh_allow_dfs": false,
  "mesh_enabled": false,
  "cisco_enabled": false,
  "disable_radios_when_power_constrained": false
}
```

