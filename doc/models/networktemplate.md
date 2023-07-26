
# Networktemplate

Network Template

## Structure

`Networktemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | - |
| `created_time` | `float` | Optional | - |
| `dhcp_snooping` | [`JunosDhcpSnooping`](../../doc/models/junos-dhcp-snooping.md) | Optional | - |
| `dns_servers` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `extra_routes` | [`dict`](../../doc/models/extra-routes-5.md) | Optional | - |
| `group_tags` | `object` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `import_org_networks` | `List of string` | Optional | Org Networks that we'd like to import |
| `mist_nac` | [`MistNac`](../../doc/models/mist-nac.md) | Optional | enable mist_nac to use radsec |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `networks` | [`dict`](../../doc/models/networks-3.md) | Optional | The property key is network name |
| `ntp_servers` | `List of string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `port_usages` | [`PortUsages`](../../doc/models/port-usages.md) | Optional | The property key is the port profile name |
| `radius_config` | [`JunosRadiusConfig`](../../doc/models/junos-radius-config.md) | Optional | Junos Radius config |
| `remote_syslog` | [`RemoteSyslog`](../../doc/models/remote-syslog.md) | Optional | - |
| `snmp_config` | [`JunosSnmpConfig`](../../doc/models/junos-snmp-config.md) | Optional | - |
| `switch_matching` | [`TemplateSwitchMatching`](../../doc/models/template-switch-matching.md) | Optional | Switch template |
| `switch_mgmt` | [`SwitchMgmt2`](../../doc/models/switch-mgmt-2.md) | Optional | - |
| `vrf_config` | [`VrfConfig`](../../doc/models/vrf-config.md) | Optional | - |
| `vrf_instances` | [`dict`](../../doc/models/vrf-instances.md) | Optional | Property key is the VRF name |

## Example (as JSON)

```json
{
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "created_time": 198.3,
  "dhcp_snooping": {
    "all_networks": false,
    "enable_arp_spoof_check": false,
    "enable_ip_source_guard": false,
    "enabled": false,
    "networks": [
      "networks8",
      "networks9"
    ]
  },
  "dns_servers": [
    "dns_servers0"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ]
}
```

