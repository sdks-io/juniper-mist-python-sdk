
# Device Gateway

device gateway

## Structure

`DeviceGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | - |
| `created_time` | `float` | Optional | - |
| `deviceprofile_id` | `uuid\|string` | Optional | - |
| `dhcpd_config` | [`JunosDhcpd`](../../doc/models/junos-dhcpd.md) | Optional | if DHCP Server/Relay is intended. The property key is the network name |
| `extra_routes` | [`dict`](../../doc/models/extra-routes.md) | Optional | The property key is the destination |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `image_1_url` | `string` | Optional | - |
| `image_2_url` | `string` | Optional | - |
| `image_3_url` | `string` | Optional | - |
| `ip_config` | [`JunosIpConfig`](../../doc/models/junos-ip-config.md) | Optional | Junos IP Config |
| `managed` | `bool` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | - |
| `networks` | [`dict`](../../doc/models/networks.md) | Optional | The property key is the network name or a CIDR |
| `ntp_servers` | `List of string` | Optional | - |
| `oob_ip_config` | [`JunosOobIpConfig`](../../doc/models/junos-oob-ip-config.md) | Optional | Junos out-of-band (vme/em0/fxp0) IP config |
| `org_id` | `uuid\|string` | Optional | - |
| `port_config` | [`dict`](../../doc/models/junos-port-config-gateway.md) | Optional | The property key is the port name or range (e.g. "ge-0/0/0-10") |
| `port_mirroring` | [`PortMirroring`](../../doc/models/port-mirroring.md) | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `vars` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "created_time": 198.3,
  "deviceprofile_id": "00000a32-0000-0000-0000-000000000000",
  "dhcpd_config": {
    "enabled": false
  },
  "extra_routes": {
    "key0": {
      "via": "via7"
    },
    "key1": {
      "via": "via8"
    }
  }
}
```

