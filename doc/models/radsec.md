
# Radsec

Radsec settings

## Structure

`Radsec`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `idle_timeout` | `int` | Optional | - |
| `mxcluster_ids` | `List of uuid\|string` | Optional | To use Org mxedges when this WLAN does not use mxtunnel, specify their mxcluster_ids.<br>Org mxedge(s) identified by mxcluster_ids |
| `proxy_hosts` | `List of string` | Optional | default is site.mxedge.radsec.proxy_hosts which must be a superset of all wlans[*].radsec.proxy_hosts<br>when radsec.proxy_hosts are not used, tunnel peers (org or site mxedges) are used irrespective of use_site_mxedge |
| `server_name` | `string` | Optional | name of the server to verify (against the cacerts in Org Setting). Only if not Mist Edge. |
| `servers` | [`List of Server`](../../doc/models/server.md) | Optional | List of Radsec Servers. Only if not Mist Edge.<br>**Constraints**: *Unique Items Required* |
| `use_mxedge` | `bool` | Optional | use mxedge(s) as radsecproxy |
| `use_site_mxedge` | `bool` | Optional | To use Site mxedges when this WLAN does not use mxtunnel<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "use_site_mxedge": false,
  "enabled": false,
  "idle_timeout": 176,
  "mxcluster_ids": [
    "00002337-0000-0000-0000-000000000000",
    "00002338-0000-0000-0000-000000000000"
  ],
  "proxy_hosts": [
    "proxy_hosts8"
  ],
  "server_name": "server_name4"
}
```

