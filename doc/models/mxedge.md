
# Mxedge

MxEdge

## Structure

`Mxedge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `fips` | [`Fips`](../../doc/models/fips.md) | Optional | FIPS configuration |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `magic` | `string` | Optional | - |
| `model` | `string` | Required | - |
| `modified_time` | `float` | Optional | - |
| `mxagent_registered` | `bool` | Optional | - |
| `mxcluster_id` | `uuid\|string` | Optional | MxCluster this MxEdge belongs to |
| `mxedge_mgmt` | [`MxedgeMgmt`](../../doc/models/mxedge-mgmt.md) | Optional | - |
| `name` | `string` | Required | - |
| `note` | `string` | Optional | - |
| `ntp_servers` | `List of string` | Optional | - |
| `oob_ip_config` | [`OobIpConfig`](../../doc/models/oob-ip-config.md) | Optional | ip configuration of the Mist Edge out-of-band management interface |
| `org_id` | `uuid\|string` | Optional | - |
| `proxy` | [`Proxy1`](../../doc/models/proxy-1.md) | Optional | - |
| `services` | `List of string` | Optional | list of services to run, tunterm only for now |
| `site_id` | `uuid\|string` | Optional | - |
| `tunterm_dhcpd_config` | [`TuntermDhcpdConfig1`](../../doc/models/tunterm-dhcpd-config-1.md) | Optional | global and per-VLAN. The property key is the VLAN ID |
| `tunterm_extra_routes` | [`dict`](../../doc/models/tunterm-extra-routes.md) | Optional | The property key is a CIDR |
| `tunterm_igmp_snooping_config` | [`TuntermIgmpSnoopingConfig`](../../doc/models/tunterm-igmp-snooping-config.md) | Optional | - |
| `tunterm_ip_config` | [`TuntermIpConfig`](../../doc/models/tunterm-ip-config.md) | Optional | ip configuration of the Mist Tunnel interface |
| `tunterm_monitoring` | [`List of SiteTuntermMonitoring`](../../doc/models/site-tunterm-monitoring.md) | Optional | - |
| `tunterm_other_ip_configs` | [`dict`](../../doc/models/tunterm-other-ip-configs.md) | Optional | ip configs by VLAN ID. The property key is the VLAN ID |
| `tunterm_port_config` | [`TuntermPortConfig`](../../doc/models/tunterm-port-config.md) | Optional | ethernet port configurations |
| `tunterm_registered` | `bool` | Optional | - |
| `tunterm_switch_config` | [`TuntermSwitchConfig`](../../doc/models/tunterm-switch-config.md) | Optional | if custom vlan settings are desired |
| `versions` | [`Versions`](../../doc/models/versions.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "95ddd29a-6a3c-929e-a431-51a5b09f36a6",
  "magic": "L-NpT5gi-ADR8WTFd4EiQPY3cP5WdSoD",
  "model": "ME-100",
  "mxcluster_id": "572586b7-f97b-a22b-526c-8b97a3f609c4",
  "name": "Guest",
  "note": "note for mxedge",
  "created_time": 198.3,
  "fips": {
    "enabled": false
  },
  "for_site": false
}
```

