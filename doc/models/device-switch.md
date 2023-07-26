
# Device Switch

Switch Configuration
You can configure `port_usages` and `networks` settings at the device level, but most of the time it's better use the Site Setting to achieve better consistency and be able to re-use the same settings across switches entries defined here will "replace" those defined in Site Setting/Network Template

## Structure

`DeviceSwitch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acl_policies` | [`List of JunosAclPolicies`](../../doc/models/junos-acl-policies.md) | Optional | - |
| `acl_tags` | [`AclTags`](../../doc/models/acl-tags.md) | Optional | ACL Tags to identify traffic source or destination. Key name is the tag name |
| `additional_config_cmds` | `List of string` | Optional | - |
| `created_time` | `float` | Optional | - |
| `deviceprofile_id` | `uuid\|string` | Optional | - |
| `dhcp_config` | [`JunosDhcpd`](../../doc/models/junos-dhcpd.md) | Optional | if DHCP Server/Relay is intended. The property key is the network name |
| `dhcp_snooping` | [`JunosDhcpSnooping`](../../doc/models/junos-dhcp-snooping.md) | Optional | - |
| `disable_auto_config` | `bool` | Optional | for a claimed switch, we control the configs by default. This option (disables the behavior)<br>**Default**: `False` |
| `dns_servers` | `List of string` | Optional | Global dns settings. To keep compatibility, dns settings in `ip_config` and `oob_ip_config` will overwrite this setting |
| `dns_suffix` | `List of string` | Optional | Global dns settings. To keep compatibility, dns settings in `ip_config` and `oob_ip_config` will overwrite this setting |
| `evpn_config` | [`JunosEvpnConfig`](../../doc/models/junos-evpn-config.md) | Optional | EVPN Junos settings |
| `extra_routes` | [`dict`](../../doc/models/extra-routes-1.md) | Optional | The property key is the network name or a CIDR |
| `id` | `uuid\|string` | Optional | - |
| `image_1_url` | `string` | Optional | - |
| `image_2_url` | `string` | Optional | - |
| `image_3_url` | `string` | Optional | - |
| `ip_config` | [`JunosIpConfig`](../../doc/models/junos-ip-config.md) | Optional | Junos IP Config |
| `managed` | `bool` | Optional | for an adopted switch, we don’t overwrite their existing configs automatically<br>**Default**: `False` |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `networks` | [`JunosNetworks`](../../doc/models/junos-networks.md) | Optional | A network represents a network segment. It can either represent a VLAN (then usually ties to a L3 subnet), optionally associate it with a subnet which can later be used to create addition routes. Used for ports doing `family ethernet-switching`. It can also be a pure L3-subnet that can then be used against a port that with `family inet`. |
| `notes` | `string` | Optional | - |
| `ntp_servers` | `List of string` | Optional | list of NTP servers specific to this device. By default, those in Site Settings will be used |
| `oob_ip_config` | [`JunosOobIpConfig`](../../doc/models/junos-oob-ip-config.md) | Optional | Junos out-of-band (vme/em0/fxp0) IP config |
| `org_id` | `uuid\|string` | Optional | - |
| `ospf_config` | [`JunosOspfConfig`](../../doc/models/junos-ospf-config.md) | Optional | Junos OSPF config |
| `other_ip_configs` | [`dict`](../../doc/models/junos-other-ip-configs.md) | Optional | The property key is the network name |
| `port_config` | [`dict`](../../doc/models/junos-port-config.md) | Optional | The property key is the port name or range (e.g. "ge-0/0/0-10") |
| `port_mirroring` | [`PortMirroring1`](../../doc/models/port-mirroring-1.md) | Optional | - |
| `port_usages` | [`PortUsages`](../../doc/models/port-usages.md) | Optional | The property key is the port profile name |
| `radius_config` | [`JunosRadiusConfig`](../../doc/models/junos-radius-config.md) | Optional | Junos Radius config |
| `role` | [`Role4Enum`](../../doc/models/role-4-enum.md) | Optional | **Default**: `'access'` |
| `router_id` | `string` | Optional | used for OSPF / BGP / EVPN |
| `site_id` | `uuid\|string` | Optional | - |
| `switch_mgmt` | [`SwitchMgmt`](../../doc/models/switch-mgmt.md) | Optional | - |
| `use_router_id_as_source_ip` | `bool` | Optional | whether to use it for snmp / syslog / tacplus / radius<br>**Default**: `False` |
| `vars` | `object` | Optional | a dictionary of name->value, the vars can then be used in Wlans. This can overwrite those from Site Vars |
| `virtual_chassis` | [`VirtualChassis`](../../doc/models/virtual-chassis.md) | Optional | required for preprovisioned Virtual Chassis |
| `vrf_config` | [`JunosVrfConfig`](../../doc/models/junos-vrf-config.md) | Optional | - |
| `vrrp_config` | [`JunosVrrpConfig`](../../doc/models/junos-vrrp-config.md) | Optional | Junos VRRP config |

## Example (as JSON)

```json
{
  "disable_auto_config": false,
  "managed": false,
  "role": "access",
  "router_id": "10.2.1.10",
  "use_router_id_as_source_ip": false,
  "acl_policies": [
    {
      "actions": [
        {
          "action": "deny",
          "dst_tag": "dst_tag3"
        },
        {
          "action": "allow",
          "dst_tag": "dst_tag4"
        }
      ],
      "name": "name8",
      "src_tags": [
        "src_tags5",
        "src_tags6",
        "src_tags7"
      ]
    },
    {
      "actions": [
        {
          "action": "allow",
          "dst_tag": "dst_tag4"
        },
        {
          "action": "deny",
          "dst_tag": "dst_tag5"
        },
        {
          "action": "allow",
          "dst_tag": "dst_tag6"
        }
      ],
      "name": "name9",
      "src_tags": [
        "src_tags6"
      ]
    },
    {
      "actions": [
        {
          "action": "deny",
          "dst_tag": "dst_tag5"
        }
      ],
      "name": "name0",
      "src_tags": [
        "src_tags7",
        "src_tags8"
      ]
    }
  ],
  "acl_tags": {
    "any": {
      "type": "type0"
    }
  },
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "created_time": 198.3,
  "deviceprofile_id": "00000a32-0000-0000-0000-000000000000"
}
```

