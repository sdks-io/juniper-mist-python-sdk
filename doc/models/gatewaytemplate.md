
# Gatewaytemplate

Gateway Template is applied to a site for gateway(s) in a site.

## Structure

`Gatewaytemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | - |
| `bgp_config` | [`dict`](../../doc/models/junos-bgp-config.md) | Optional | - |
| `created_time` | `float` | Optional | - |
| `dhcpd_config` | [`dict`](../../doc/models/dhcpd-config.md) | Optional | The property key is the network name |
| `extra_routes` | [`dict`](../../doc/models/extra-routes-2.md) | Optional | - |
| `gateway_matching` | [`TemplateGatewayMatching`](../../doc/models/template-gateway-matching.md) | Optional | Gateway matching |
| `id` | `uuid\|string` | Optional | - |
| `idp_profiles` | [`IdpProfiles`](../../doc/models/idp-profiles.md) | Optional | Property key is the profile name |
| `ip_configs` | [`dict`](../../doc/models/ip-configs.md) | Optional | The property key is the network name |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `networks` | [`dict`](../../doc/models/network.md) | Optional | The property key is the network name |
| `oob_ip_config` | [`JunosOobIpConfig`](../../doc/models/junos-oob-ip-config.md) | Optional | Junos out-of-band (vme/em0/fxp0) IP config |
| `org_id` | `uuid\|string` | Optional | - |
| `path_preferences` | [`dict`](../../doc/models/path-preferences.md) | Optional | experimental |
| `port_config` | [`dict`](../../doc/models/junos-port-config-gateway.md) | Optional | The property key is the port(s) name or range (e.g. "ge-0/0/0-10") |
| `routing_policies` | [`dict`](../../doc/models/junos-routing-policy.md) | Optional | The property key is the routing policy name |
| `service_policies` | [`List of ServicePolicy2`](../../doc/models/service-policy-2.md) | Optional | - |
| `tunnel_configs` | [`dict`](../../doc/models/gatewaytemplate-tunnel-configs.md) | Optional | Property key is the tunnel name |
| `mtype` | [`Type21Enum`](../../doc/models/type-21-enum.md) | Optional | **Default**: `'standalone'` |

## Example (as JSON)

```json
{
  "name": "name0",
  "type": "standalone",
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "bgp_config": {
    "key0": {
      "auth_key": "auth_key3",
      "bfd_minimum_interval": 215,
      "communities": [
        {
          "id": "id4",
          "local_preference": 210,
          "vpn_name": "vpn_name4"
        }
      ],
      "disable_bfd": true,
      "export": "export1"
    }
  },
  "created_time": 198.3,
  "dhcpd_config": {
    "key0": {
      "dns_servers": [
        "dns_servers0"
      ],
      "dns_suffix": [
        "dns_suffix9"
      ],
      "fixed_bindings": {
        "key0": {
          "ip": "ip3",
          "name": "name9"
        },
        "key1": {
          "ip": "ip4",
          "name": "name0"
        },
        "key2": {
          "ip": "ip5",
          "name": "name1"
        }
      },
      "gateway": "gateway0",
      "ip_end": "ip_end6"
    },
    "key1": {
      "dns_servers": [
        "dns_servers1",
        "dns_servers2"
      ],
      "dns_suffix": [
        "dns_suffix0",
        "dns_suffix1"
      ],
      "fixed_bindings": {
        "key0": {
          "ip": "ip4",
          "name": "name0"
        }
      },
      "gateway": "gateway1",
      "ip_end": "ip_end7"
    },
    "key2": {
      "dns_servers": [
        "dns_servers2",
        "dns_servers3",
        "dns_servers4"
      ],
      "dns_suffix": [
        "dns_suffix1",
        "dns_suffix2",
        "dns_suffix3"
      ],
      "fixed_bindings": {
        "key0": {
          "ip": "ip5",
          "name": "name1"
        },
        "key1": {
          "ip": "ip6",
          "name": "name2"
        }
      },
      "gateway": "gateway2",
      "ip_end": "ip_end8"
    }
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

