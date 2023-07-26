
# Devices Array

## Structure

`DevicesArray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aeroscout` | [`ApAeroscout`](../../doc/models/ap-aeroscout.md) | Optional | Aeroscout AP settings |
| `ble_config` | [`ApBle`](../../doc/models/ap-ble.md) | Optional | BLE AP settings |
| `centrak` | [`Centrak`](../../doc/models/centrak.md) | Optional | - |
| `client_bridge` | [`ApClientBridge`](../../doc/models/ap-client-bridge.md) | Optional | - |
| `created_time` | `float` | Optional | - |
| `deviceprofile_id` | `uuid\|string` | Optional | - |
| `disable_eth_1` | `bool` | Optional | whether to disable eth1 port<br>**Default**: `False` |
| `disable_eth_2` | `bool` | Optional | whether to disable eth2 port<br>**Default**: `False` |
| `disable_eth_3` | `bool` | Optional | whether to disable eth3 port<br>**Default**: `False` |
| `disable_module` | `bool` | Optional | whether to disable module port<br>**Default**: `False` |
| `esl_config` | [`ApEslConfig`](../../doc/models/ap-esl-config.md) | Optional | - |
| `for_site` | `bool` | Optional | - |
| `height` | `float` | Optional | height, in meters, optional |
| `id` | `uuid\|string` | Optional | - |
| `image_1_url` | `string` | Optional | - |
| `image_2_url` | `string` | Optional | - |
| `image_3_url` | `string` | Optional | - |
| `iot_config` | [`ApIot`](../../doc/models/ap-iot.md) | Optional | IoT AP settings |
| `ip_config` | [`ApIp1`](../../doc/models/ap-ip-1.md) | Optional | IP AP settings |
| `led` | [`ApLed`](../../doc/models/ap-led.md) | Optional | LED AP settings |
| `locked` | `bool` | Optional | whether this map is considered locked down |
| `map_id` | `uuid\|string` | Optional | map where the device belongs to |
| `mesh` | [`ApMesh`](../../doc/models/ap-mesh.md) | Optional | Mesh AP settings |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `notes` | `string` | Optional | any notes about this AP |
| `ntp_servers` | `List of string` | Optional | list of NTP servers specific to this device. By default, those in Site Settings will be used |
| `org_id` | `uuid\|string` | Optional | - |
| `orientation` | `float` | Optional | orientation, 0-359, in degrees, up is 0, right is 90.<br>**Constraints**: `>= 0`, `<= 359` |
| `poe_passthrough` | `bool` | Optional | whether to enable power out through module port (for APH) or eth1 (for APL/BT11)<br>**Default**: `False` |
| `port_config` | [`PortConfig2`](../../doc/models/port-config-2.md) | Optional | eth0 is allowed in mesh relay mode, otherwise eth0 is not allowed here.<br>The property key is the interface(s) name (e.g. "eth1" or"eth1,eth2") |
| `pwr_config` | [`PwrConfig`](../../doc/models/pwr-config.md) | Optional | power related configs |
| `radio_config` | [`ApRadio`](../../doc/models/ap-radio.md) | Optional | Radio AP settings |
| `site_id` | `uuid\|string` | Optional | - |
| `uplink_port_config` | [`UplinkPortConfig`](../../doc/models/uplink-port-config.md) | Optional | - |
| `usb_config` | [`ApUsb`](../../doc/models/ap-usb.md) | Optional | USB AP settings<br>Note: if native imagotag is enabled, BLE will be disabled automatically<br>Note: legacy, new config moved to ESL Config. |
| `vars` | `object` | Optional | a dictionary of name->value, the vars can then be used in Wlans. This can overwrite those from Site Vars |
| `x` | `float` | Optional | x in pixel |
| `y` | `float` | Optional | y in pixel |
| `acl_policies` | [`List of JunosAclPolicies`](../../doc/models/junos-acl-policies.md) | Optional | - |
| `acl_tags` | [`AclTags`](../../doc/models/acl-tags.md) | Optional | ACL Tags to identify traffic source or destination. Key name is the tag name |
| `additional_config_cmds` | `List of string` | Optional | - |
| `dhcp_config` | [`JunosDhcpd`](../../doc/models/junos-dhcpd.md) | Optional | if DHCP Server/Relay is intended. The property key is the network name |
| `dhcp_snooping` | [`JunosDhcpSnooping`](../../doc/models/junos-dhcp-snooping.md) | Optional | - |
| `disable_auto_config` | `bool` | Optional | for a claimed switch, we control the configs by default. This option (disables the behavior)<br>**Default**: `False` |
| `dns_servers` | `List of string` | Optional | Global dns settings. To keep compatibility, dns settings in `ip_config` and `oob_ip_config` will overwrite this setting |
| `dns_suffix` | `List of string` | Optional | Global dns settings. To keep compatibility, dns settings in `ip_config` and `oob_ip_config` will overwrite this setting |
| `evpn_config` | [`JunosEvpnConfig`](../../doc/models/junos-evpn-config.md) | Optional | EVPN Junos settings |
| `extra_routes` | [`ExtraRoutes7`](../../doc/models/extra-routes-7.md) | Optional | The property key is the network name or a CIDR |
| `managed` | `bool` | Optional | for an adopted switch, we don’t overwrite their existing configs automatically<br>**Default**: `False` |
| `networks` | [`JunosNetworks1`](../../doc/models/junos-networks-1.md) | Optional | A network represents a network segment. It can either represent a VLAN (then usually ties to a L3 subnet), optionally associate it with a subnet which can later be used to create addition routes. Used for ports doing `family ethernet-switching`. It can also be a pure L3-subnet that can then be used against a port that with `family inet`. |
| `oob_ip_config` | [`JunosOobIpConfig`](../../doc/models/junos-oob-ip-config.md) | Optional | Junos out-of-band (vme/em0/fxp0) IP config |
| `ospf_config` | [`JunosOspfConfig`](../../doc/models/junos-ospf-config.md) | Optional | Junos OSPF config |
| `other_ip_configs` | [`dict`](../../doc/models/junos-other-ip-configs.md) | Optional | The property key is the network name |
| `port_mirroring` | [`PortMirroring2`](../../doc/models/port-mirroring-2.md) | Optional | - |
| `port_usages` | [`PortUsages`](../../doc/models/port-usages.md) | Optional | The property key is the port profile name |
| `radius_config` | [`JunosRadiusConfig`](../../doc/models/junos-radius-config.md) | Optional | Junos Radius config |
| `role` | [`Role4Enum`](../../doc/models/role-4-enum.md) | Optional | **Default**: `'access'` |
| `router_id` | `string` | Optional | used for OSPF / BGP / EVPN |
| `switch_mgmt` | [`SwitchMgmt`](../../doc/models/switch-mgmt.md) | Optional | - |
| `use_router_id_as_source_ip` | `bool` | Optional | whether to use it for snmp / syslog / tacplus / radius<br>**Default**: `False` |
| `virtual_chassis` | [`VirtualChassis`](../../doc/models/virtual-chassis.md) | Optional | required for preprovisioned Virtual Chassis |
| `vrf_config` | [`JunosVrfConfig`](../../doc/models/junos-vrf-config.md) | Optional | - |
| `vrrp_config` | [`JunosVrrpConfig`](../../doc/models/junos-vrrp-config.md) | Optional | Junos VRRP config |
| `dhcpd_config` | [`JunosDhcpd`](../../doc/models/junos-dhcpd.md) | Optional | if DHCP Server/Relay is intended. The property key is the network name |
| `msp_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "disable_eth1": false,
  "disable_eth2": false,
  "disable_eth3": false,
  "disable_module": false,
  "poe_passthrough": false,
  "disable_auto_config": false,
  "managed": false,
  "role": "access",
  "router_id": "10.2.1.10",
  "use_router_id_as_source_ip": false,
  "aeroscout": {
    "enabled": false,
    "host": "host6",
    "locate_connected": false
  },
  "ble_config": {
    "beacon_enabled": false,
    "beacon_rate": 110,
    "beacon_rate_mode": "default",
    "beam_disabled": [
      113,
      114,
      115
    ],
    "custom_ble_packet_enabled": false
  },
  "centrak": {
    "enabled": false
  },
  "client_bridge": {
    "auth": {
      "psk": "psk6",
      "type": "open"
    },
    "enabled": false,
    "ssid": "ssid0"
  },
  "created_time": 198.3
}
```

