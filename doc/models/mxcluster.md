
# Mxcluster

mxCluster

## Structure

`Mxcluster`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `mist_das` | [`MxedgeDas`](../../doc/models/mxedge-das.md) | Optional | configure cloud-assisted dynamic authorization service on this cluster of mist edges |
| `mist_nac` | [`MxclusterNac`](../../doc/models/mxcluster-nac.md) | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `proxy` | [`Proxy`](../../doc/models/proxy.md) | Optional | Proxy Configuration to talk to Mist |
| `radsec` | [`MxclusterRadsec`](../../doc/models/mxcluster-radsec.md) | Optional | MxEdge Radsec Configuration |
| `radsec_tls` | [`RadsecTls`](../../doc/models/radsec-tls.md) | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `tunterm_ap_subnets` | `List of string` | Optional | list of subnets where we allow AP to establish Mist Tunnels from |
| `tunterm_dhcpd_config` | [`TuntermDhcpdConfig`](../../doc/models/tunterm-dhcpd-config.md) | Optional | DHCP server/relay configuration of Mist Tunneled VLANs. The property key is the VLAN ID |
| `tunterm_extra_routes` | [`dict`](../../doc/models/tunterm-extra-routes.md) | Optional | extra routes for Mist Tunneled VLANs. The property key is a CIDR |
| `tunterm_hosts` | `List of string` | Optional | hostnames or IPs where a Mist Tunnel will use as the Peer (i.e. they are reachable from AP) |
| `tunterm_hosts_order` | `List of int` | Optional | list of index of tunterm_hosts |
| `tunterm_hosts_selection` | [`TuntermHostsSelectionEnum`](../../doc/models/tunterm-hosts-selection-enum.md) | Optional | Ordering of tunterm_hosts for mxedge within the same mxcluster.<br><br>* When `shuffle`, the ordering of tunterm_hosts is randomized by the device’s MAC.<br>* When `shuffle-by-site`, we shuffle by site_id+tunnel_id (so when client connects to a specific Tunnel, it will go to the same (order of) mxedge, and we load-balancing between tunnels).<br>* When `ordered`, the order is decided by tunterm_hosts_order<br>**Default**: `'shuffle'` |
| `tunterm_monitoring` | [`List of SiteTuntermMonitoring`](../../doc/models/site-tunterm-monitoring.md) | Optional | - |
| `tunterm_monitoring_disabled` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "tunterm_hosts_selection": "shuffle",
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "mist_das": {
    "coa_servers": [
      {
        "disable_event_timestamp_check": false,
        "enabled": false,
        "host": "host4",
        "port": 66,
        "secret": "secret8"
      },
      {
        "disable_event_timestamp_check": true,
        "enabled": true,
        "host": "host5",
        "port": 67,
        "secret": "secret9"
      }
    ],
    "enabled": false
  },
  "mist_nac": {
    "acct_server_port": 70,
    "auth_server_port": 34,
    "client_ips": {
      "key0": {
        "secret": "secret3",
        "site_id": "00002393-0000-0000-0000-000000000000",
        "vendor": "juniper"
      },
      "key1": {
        "secret": "secret2",
        "site_id": "00002394-0000-0000-0000-000000000000",
        "vendor": "aruba"
      },
      "key2": {
        "secret": "secret1",
        "site_id": "00002395-0000-0000-0000-000000000000",
        "vendor": "paloalto"
      }
    },
    "enabled": false,
    "secret": "secret6"
  }
}
```

