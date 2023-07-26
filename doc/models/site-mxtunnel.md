
# Site Mxtunnel

Site MxTunnel

## Structure

`SiteMxtunnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_subnets` | `List of string` | Optional | list of subnets where we allow AP to establish Mist Tunnels from |
| `clusters` | [`List of Cluster`](../../doc/models/cluster.md) | Optional | for AP, how to connect to tunterm or radsecproxy |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `hello_interval` | `int` | Optional | in seconds, used as heartbeat to detect if a tunnel is alive. AP will try another peer after missing N hellos specified by hello_retries<br>**Default**: `60`<br>**Constraints**: `>= 1`, `<= 300` |
| `hello_retries` | `int` | Optional | **Default**: `7`<br>**Constraints**: `>= 2`, `<= 30` |
| `hosts` | `List of string` | Optional | hostnames or IPs where a Mist Tunnel will use as the Peer (i.e. they are reachable from AP) |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `mtu` | `int` | Optional | 0 to enable PMTU, 552-1500 to start PMTU with a lower MTU<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 1500` |
| `org_id` | `uuid\|string` | Optional | - |
| `protocol` | [`Protocol3Enum`](../../doc/models/protocol-3-enum.md) | Optional | - |
| `radsec` | [`Radsec1`](../../doc/models/radsec-1.md) | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `vlan_ids` | `List of object` | Optional | list of vlan_ids that will be use |

## Example (as JSON)

```json
{
  "hello_interval": 60,
  "hello_retries": 7,
  "mtu": 0,
  "ap_subnets": [
    "ap_subnets4"
  ],
  "clusters": [
    {
      "name": "name9",
      "tunterm_hosts": [
        "tunterm_hosts9",
        "tunterm_hosts0",
        "tunterm_hosts1"
      ]
    },
    {
      "name": "name0",
      "tunterm_hosts": [
        "tunterm_hosts0"
      ]
    }
  ],
  "created_time": 198.3,
  "for_site": false
}
```

