
# Wxlan Tunnel

WxLAn Tunnel

## Structure

`WxlanTunnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `dmvpn` | [`Dmvpn`](../../doc/models/dmvpn.md) | Optional | Dynamic Multipoint VPN configurations |
| `for_mgmt` | `bool` | Optional | determined during creation time and cannot be toggled. A management tunnel cannot be used by wxlan rule or by wlan<br>**Default**: `False` |
| `for_site` | `bool` | Optional | - |
| `hello_interval` | `int` | Optional | in seconds, used as heartbeat to detect if a tunnel is alive. AP will try another peer after missing N hellos specified by hello_retries.<br>**Default**: `60`<br>**Constraints**: `>= 1`, `<= 300` |
| `hello_retries` | `int` | Optional | **Default**: `7`<br>**Constraints**: `>= 2`, `<= 30` |
| `hostname` | `string` | Optional | optional, overwrite the hostname in SCCRQ control message, default is “” or null, %H and %M can be used, which will be replace with corresponding values:<br><br>* %H: name of the ap if provided (and will be stripped so it can be used for hostname) and fallbacks to MAC<br>* %M: MAC (e.g. 5c5b350e0060) |
| `id` | `uuid\|string` | Optional | - |
| `ipsec` | [`Ipsec1`](../../doc/models/ipsec-1.md) | Optional | IPSec-related configurations; requires DMVPN be enabled |
| `is_static` | `bool` | Optional | whether it’s static/unmanaged (i.e. no control session). As the session configurations are not compatible, cannot be toggled.<br>**Default**: `False` |
| `modified_time` | `float` | Optional | - |
| `mtu` | `int` | Optional | 0 to enable PMTU, 552-1500 to start PMTU with a lower MTU<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 1500` |
| `name` | `string` | Required | The name of the tunnel |
| `org_id` | `uuid\|string` | Optional | - |
| `peers` | `List of string` | Optional | list of remote peers’ IP or hostname |
| `router_id` | `string` | Optional | optional, overwrite the router-id in SCCRQ control message, default is “0” or null, can also be an IPv4 address |
| `secret` | `string` | Optional | secret, ‘’ if no auth is used |
| `sessions` | [`List of Sessions2`](../../doc/models/sessions-2.md) | Optional | sessions to be established with the tunnel. Has to be >= 1 in order for this tunnel to be useful. For management tunnel, it can only have 1<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `site_id` | `uuid\|string` | Optional | - |
| `udp_port` | `int` | Optional | udp port if `use_udp`==`true` |
| `use_udp` | `bool` | Optional | whether to use UDP instead of IP (proto=115, which is default of L2TPv3)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "for_mgmt": false,
  "hello_interval": 60,
  "hello_retries": 7,
  "is_static": false,
  "mtu": 0,
  "name": "name0",
  "use_udp": false,
  "created_time": 198.3,
  "dmvpn": {
    "enabled": false,
    "holding_time": 188,
    "host_routes": [
      "host_routes6",
      "host_routes7"
    ]
  },
  "for_site": false
}
```

