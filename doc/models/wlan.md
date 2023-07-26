
# Wlan

WLAN

**Note**: portal_template will be forked out of wlan objects soon. To fetch portal_template, please query portal_template_url. To update portal_template, use Wlan Portal Template.

## Structure

`Wlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_immediate_update` | `bool` | Optional | enable coa-immediate-update and address-change-immediate-update on the access profile.<br>**Default**: `False` |
| `acct_interim_interval` | `int` | Optional | how frequently should interim accounting be reported, 60-65535. default is 0 (use one specified in Access-Accept request from RADIUS Server). Very frequent messages can affect the performance of the radius server, 600 and up is recommended when enabled<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 65535` |
| `acct_servers` | [`List of AcctServer`](../../doc/models/acct-server.md) | Optional | list of RADIUS accounting servers, optional, order matters where the first one is treated as primary |
| `airwatch` | [`WlanAirwatch`](../../doc/models/wlan-airwatch.md) | Optional | airwatch wlan settings |
| `allow_ipv_6_ndp` | `bool` | Optional | only applicable when limit_bcast==true, which allows or disallows ipv6 Neighbor Discovery packets to go through<br>**Default**: `True` |
| `allow_mdns` | `bool` | Optional | only applicable when limit_bcast==true, which allows mDNS / Bonjour packets to go through<br>**Default**: `False` |
| `allow_ssdp` | `bool` | Optional | only applicable when `limit_bcast`==`tru`e, which allows SSDP<br>**Default**: `False` |
| `ap_ids` | `List of uuid\|string` | Optional | list of device ids |
| `app_limit` | [`AppLimit`](../../doc/models/app-limit.md) | Optional | bandwidth limiting for apps (applies to up/down) |
| `app_qos` | [`WlanAppQos`](../../doc/models/wlan-app-qos.md) | Optional | app qos wlan settings |
| `apply_to` | [`ApplyToEnum`](../../doc/models/apply-to-enum.md) | Optional | - |
| `arp_filter` | `bool` | Optional | whether to enable smart arp filter<br>**Default**: `False` |
| `auth` | [`WlanAuth`](../../doc/models/wlan-auth.md) | Optional | authentication wlan settings |
| `auth_server_selection` | [`AuthServerSelectionEnum`](../../doc/models/auth-server-selection-enum.md) | Optional | When ordered, AP will prefer and go back to the first server if possible<br>**Default**: `'ordered'` |
| `auth_servers` | [`List of AuthServer`](../../doc/models/auth-server.md) | Optional | list of RADIUS authentication servers, at least one is needed if `auth type`==`eap`, order matters where the first one is treated as primary |
| `auth_servers_nas_id` | `string` | Optional | optional, up to 48 bytes, will be dynamically generated if not provided. used only for authentication servers |
| `auth_servers_nas_ip` | `string` | Optional | optional, NAS-IP-ADDRESS to use |
| `auth_servers_retries` | `int` | Optional | radius auth session retries. Following fast timers are set if “fast_dot1x_timers” knob is enabled. ‘retries’ are set to value of auth_servers_retries. ‘max-requests’ is also set when setting auth_servers_retries and is set to default value to 3.<br>**Default**: `2` |
| `auth_servers_timeout` | `int` | Optional | radius auth session timeout. Following fast timers are set if “fast_dot1x_timers” knob is enabled. ‘quite-period’ and ‘transmit-period’ are set to half the value of auth_servers_timeout. ‘supplicant-timeout’ is also set when setting auth_servers_timeout and is set to default value of 10.<br>**Default**: `5` |
| `band` | `string` | Optional | `band` is deprecated and kept for backward compability. Use bands instead |
| `band_steer` | `bool` | Optional | whether to enable band_steering, this works only when band==both<br>**Default**: `False` |
| `band_steer_force_band_5` | `bool` | Optional | force dual-band capable client to connect to 5G<br>**Default**: `False` |
| `bands` | [`List of Band8Enum`](../../doc/models/band-8-enum.md) | Optional | list of radios that the wlan should apply to |
| `block_blacklist_clients` | `bool` | Optional | whether to block the clients in the blacklist (up to first 256 macs) |
| `bonjour` | [`WlanBonjour`](../../doc/models/wlan-bonjour.md) | Optional | bonjour gateway wlan settings |
| `cisco_cwa` | [`WlanCiscoCwa`](../../doc/models/wlan-cisco-cwa.md) | Optional | Cisco CWA (central web authentication) required RADIUS with COA in order to work. See CWA: https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine/115732-central-web-auth-00.html |
| `client_limit_down` | `int` | Optional | kbps |
| `client_limit_down_enabled` | `bool` | Optional | if downlink limiting per-client is enabled<br>**Default**: `False` |
| `client_limit_up` | `int` | Optional | kbps |
| `client_limit_up_enabled` | `bool` | Optional | if uplink limiting per-client is enabled<br>**Default**: `False` |
| `coa_servers` | [`List of CoaServer`](../../doc/models/coa-server.md) | Optional | list of COA (change of authorization) servers, optional |
| `created_time` | `float` | Optional | - |
| `disable_11_ax` | `bool` | Optional | some old WLAN drivers may not be compatible<br>**Default**: `False` |
| `disable_ht_vht_rates` | `bool` | Optional | to disable ht or vht rates<br>**Default**: `False` |
| `disable_uapsd` | `bool` | Optional | whether to disable U-APSD<br>**Default**: `False` |
| `disable_v_1_roam_notify` | `bool` | Optional | disable sending v2 roam notification messages<br>**Default**: `True` |
| `disable_v_2_roam_notify` | `bool` | Optional | disable sending v2 roam notification messages<br>**Default**: `False` |
| `disable_wmm` | `bool` | Optional | whether to disable WMM<br>**Default**: `False` |
| `dns_server_rewrite` | [`DnsServerRewrite`](../../doc/models/dns-server-rewrite.md) | Optional | for radius_group-based DNS server (rewrite DNS request depending on the Group RADIUS server returns) |
| `dtim` | `int` | Optional | **Default**: `2` |
| `dynamic_psk` | [`DynamicPsk`](../../doc/models/dynamic-psk.md) | Optional | for dynamic PSK where we get per-user PSK from Radius<br>dynamic_psk allows PSK to be selected at runtime depending on context (wlan/site/user/...) thus following configurations are assumed (currently)<br><br>- PSK will come from RADIUS server<br>- AP sends client MAC as username ans password (i.e. `enable_mac_auth` is assumed)<br>- AP sends BSSID:SSID as Caller-Station-ID<br>- `auth_servers` is required<br>- PSK will come from cloud WLC if source is cloud_psks<br>- default_psk will be used if cloud WLC is not available<br>- `multi_psk_only` and `psk` is ignored<br>- `pairwise` can only be wpa2-ccmp (for now, wpa3 support on the roadmap) |
| `dynamic_vlan` | [`DynamicVlan1`](../../doc/models/dynamic-vlan-1.md) | Optional | for 802.1x |
| `enable_local_keycaching` | `bool` | Optional | enable AP-AP keycaching via multicast<br>**Default**: `False` |
| `enable_wireless_bridging` | `bool` | Optional | whether to enable wireless bridging, which allows more broadcast packets to go through<br>(allows forwarding of DHCP response to client not associated with the AP) |
| `enabled` | `bool` | Optional | if this wlan is enabled<br>**Default**: `True` |
| `fast_dot_1_x_timers` | `bool` | Optional | if set to true, sets default fast-timers with values calculated from ‘auth_servers_timeout’ and ‘auth_server_retries’.<br>**Default**: `False` |
| `for_site` | `bool` | Optional | - |
| `hide_ssid` | `bool` | Optional | whether to hide SSID in beacon<br>**Default**: `False` |
| `hostname_ie` | `bool` | Optional | include hostname inside IE in AP beacons / probe responses<br>**Default**: `False` |
| `hotspot_20` | [`WlanHotspot20`](../../doc/models/wlan-hotspot-20.md) | Optional | hostspot 2.0 wlan settings |
| `id` | `uuid\|string` | Optional | - |
| `interface` | [`InterfaceEnum`](../../doc/models/interface-enum.md) | Optional | where this WLAN will be connected to<br>**Default**: `'all'` |
| `isolation` | `bool` | Optional | whether to allow clients to talk to each other<br>**Default**: `False` |
| `l_2_isolation` | `bool` | Optional | if isolation is enabled, whether to deny clients to talk to L2 on the LAN<br>**Default**: `False` |
| `legacy_overds` | `bool` | Optional | legacy devices requires the Over-DS (for Fast BSS Transition) bit set (while our chip doesn’t support it). Warning! Enabling this will cause problem for iOS devices. |
| `limit_bcast` | `bool` | Optional | whether to limit broadcast packets going to wireless (i.e. only allow certain bcast packets to go through)<br>**Default**: `False` |
| `limit_probe_response` | `bool` | Optional | limit probe response base on some heuristic rules |
| `max_idletime` | `int` | Optional | max idle time in seconds<br>**Default**: `1800`<br>**Constraints**: `>= 60`, `<= 86400` |
| `mist_nac` | [`MistNac2`](../../doc/models/mist-nac-2.md) | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `mxtunnel` | `object` | Optional | when `interface`=`site_medge`, the definition of the Mist Tunnels (key is the name) |
| `mxtunnel_ids` | `List of string` | Optional | when `interface`=`mxtunnel`, id of the Mist Tunnel |
| `mxtunnel_name` | `List of string` | Optional | when `interface`=`site_medge`, name of the mxtunnel that in mxtunnels under Site Setting |
| `no_static_dns` | `bool` | Optional | whether to only allow client to use DNS that we’ve learned from DHCP response<br>**Default**: `False` |
| `no_static_ip` | `bool` | Optional | whether to only allow client that we’ve learned from DHCP exchange to talk<br>**Default**: `False` |
| `org_id` | `uuid\|string` | Optional | - |
| `portal` | [`WlanPortal`](../../doc/models/wlan-portal.md) | Optional | portal wlan settings |
| `portal_allowed_hostnames` | `List of string` | Optional | list of hostnames without http(s):// (matched by substring) |
| `portal_allowed_subnets` | `List of string` | Optional | list of CIDRs |
| `portal_api_secret` | `string` | Optional | api secret (auto-generated) that can be used to sign guest authorization requests |
| `portal_denied_hostnames` | `List of string` | Optional | list of hostnames without http(s):// (matched by substring), this takes precedence over portal_allowed_hostnames |
| `portal_image` | `string` | Optional | Url of portal background image |
| `portal_sso_url` | `string` | Optional | - |
| `portal_template_url` | `string` | Optional | N.B portal_template will be forked out of wlan objects soon. To fetch portal_template, please query portal_template_url. To update portal_template, use Wlan Portal Template. |
| `qos` | [`Qos`](../../doc/models/qos.md) | Optional | - |
| `radsec` | [`Radsec`](../../doc/models/radsec.md) | Optional | Radsec settings |
| `rateset` | [`dict`](../../doc/models/wlan-datarates.md) | Optional | - |
| `roam_mode` | [`RoamModeEnum`](../../doc/models/roam-mode-enum.md) | Optional | **Default**: `'none'` |
| `schedule` | [`Schedule`](../../doc/models/schedule.md) | Optional | WLAN operating schedule, default is disabled |
| `site_id` | `uuid\|string` | Optional | - |
| `sle_excluded` | `bool` | Optional | whether to exclude this WLAN from SLE metrics<br>**Default**: `False` |
| `ssid` | `string` | Required | the name of the SSID |
| `template_id` | `uuid\|string` | Optional | - |
| `thumbnail` | `string` | Optional | Url of portal background image thumbnail |
| `use_eapol_v_1` | `bool` | Optional | if `auth.type`==’eap’ or ‘psk’, should only be set for legacy client, such as pre-2004, 802.11b devices<br>**Default**: `False` |
| `vlan_enabled` | `bool` | Optional | if vlan tagging is enabled<br>**Default**: `False` |
| `vlan_id` | `int` | Optional | **Constraints**: `>= 1`, `<= 4094` |
| `vlan_ids` | `List of int` | Optional | list of VLAN ids<br>**Constraints**: `>= 1`, `<= 4094` |
| `vlan_pooling` | `bool` | Optional | vlan pooling allows AP to place client on different VLAN using a deterministic algorithm<br>**Default**: `False` |
| `wlan_limit_down` | `int` | Optional | kbps |
| `wlan_limit_down_enabled` | `bool` | Optional | if downlink limiting for whole wlan is enabled<br>**Default**: `False` |
| `wlan_limit_up` | `int` | Optional | kbps |
| `wlan_limit_up_enabled` | `bool` | Optional | if uplink limiting for whole wlan is enabled<br>**Default**: `False` |
| `wxtag_ids` | `List of uuid\|string` | Optional | list of wxtag_ids |
| `wxtunnel_id` | `string` | Optional | when `interface`=`wxtunnel`, id of the WXLAN Tunnel |
| `wxtunnel_remote_id` | `string` | Optional | when `interface`=`wxtunnel`, remote tunnel identifier |

## Example (as JSON)

```json
{
  "acct_immediate_update": false,
  "acct_interim_interval": 0,
  "allow_ipv6_ndp": true,
  "allow_mdns": false,
  "allow_ssdp": false,
  "arp_filter": false,
  "auth_server_selection": "ordered",
  "auth_servers_retries": 2,
  "auth_servers_timeout": 5,
  "band_steer": false,
  "band_steer_force_band5": false,
  "client_limit_down_enabled": false,
  "client_limit_up_enabled": false,
  "disable_11ax": false,
  "disable_ht_vht_rates": false,
  "disable_uapsd": false,
  "disable_v1_roam_notify": true,
  "disable_v2_roam_notify": false,
  "disable_wmm": false,
  "dtim": 2,
  "enable_local_keycaching": false,
  "enabled": true,
  "fast_dot1x_timers": false,
  "hide_ssid": false,
  "hostname_ie": false,
  "interface": "all",
  "isolation": false,
  "l2_isolation": false,
  "limit_bcast": false,
  "max_idletime": 1800,
  "no_static_dns": false,
  "no_static_ip": false,
  "roam_mode": "none",
  "sle_excluded": false,
  "ssid": "ssid2",
  "use_eapol_v1": false,
  "vlan_enabled": false,
  "vlan_pooling": false,
  "wlan_limit_down_enabled": false,
  "wlan_limit_up_enabled": false,
  "acct_servers": [
    {
      "host": "host1",
      "keywrap_enabled": true,
      "keywrap_format": "keywrap_format5",
      "keywrap_kek": "keywrap_kek3",
      "keywrap_mack": "keywrap_mack5",
      "port": 15,
      "secret": "secret7"
    }
  ],
  "airwatch": {
    "api_key": "api_key8",
    "console_url": "console_url2",
    "enabled": false,
    "password": "password8",
    "username": "username4"
  }
}
```

